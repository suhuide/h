#
#    Copyright (c) 2026 Project CHIP Authors
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

"""
Zap2Xml - Convert .zap files to PICS XML files

Converts Silicon Labs ZAP configuration files to Matter PICS XML files
using the Matter V1.5 PICS XML templates.

Rules:
1. Server-side items (.S.*) - Set based on ZAP cluster configuration
2. Client-side items (.C.*) - Set based on ZAP cluster configuration (if client role exists)
3. Manually items (.S.M.* or .C.M.*) - Set to false (override template defaults) because ZAP doesn't configure these
4. Base.xml - Generated dynamically from ZAP data (communication capabilities, roles, etc.)
"""

import argparse
import io
import json
import os
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from typing import Optional, List, Dict, Any, Tuple


# Cluster name mapping to handle inconsistent naming between .zap files and PICS XML templates
CLUSTER_TO_PICS_DICT = {
    "ICDManagement": "ICD Management",
    "OTA Software Update Provider": "OTA Software Update",
    "OTA Software Update Requestor": "OTA Software Update",
    "On/Off": "On-Off",
    "GroupKeyManagement": "Group Communication",
    "Group Key Management": "Group Communication",
    "Wake On LAN": "Media Cluster",
    "Wake on LAN": "Media Cluster",
    "Low Power": "Media Cluster",
    "Keypad Input": "Media Cluster",
    "Audio Output": "Media Cluster",
    "Media Input": "Media Cluster",
    "Target Navigator": "Media Cluster",
    "Content Control": "Media Cluster",
    "Channel": "Media Cluster",
    "Media Playback": "Media Cluster",
    "Account Login": "Media Cluster",
    "Application Basic": "Media Cluster",
    "Content Launcher": "Media Cluster",
    "Content App Observer": "Media Cluster",
    "Application Launch": "Media Cluster",
    "Operational Credentials": "Node Operational Credentials",
    "Thermostat": "Thermostat Cluster",
    "Boolean State": "Boolean State Cluster",
    "AccessControl": "Access Control Cluster",
    "Access Control": "Access Control Cluster",
    "Energy EVSE": "Energy EVSE Cluster",
    "Descriptor": "Descriptor Cluster",
    "Basic Information": "Basic Information Cluster",
    "Identify": "Identify Cluster",
    "Groups": "Groups Cluster",
    "Scenes": "Scenes Management Cluster",
    "Scenes Management": "Scenes Management Cluster",
    "OnOff": "On-Off",
    "Level Control": "Level Control Cluster",
    "Binding": "Binding Cluster",
    "Color Control": "Color Control Cluster",
    "Ballast Configuration": "Ballast Configuration Cluster",
    "Illuminance Measurement": "Illuminance Measurement Cluster",
    "Temperature Measurement": "Temperature Measurement Cluster",
    "Pressure Measurement": "Pressure Measurement Cluster",
    "Flow Measurement": "Flow Measurement Cluster",
    "Relative Humidity Measurement": "Relative Humidity Measurement Cluster",
    "Occupancy Sensing": "Occupancy Sensing Cluster",
    "Power Source Configuration": "Power Source Configuration Cluster",
    "Power Source": "Power Source Cluster",
    "Network Commissioning": "Network Commissioning Cluster",
    "Administrator Commissioning": "Administrator Commissioning Cluster",
    "Node Operational Credentials": "Node Operational Credentials Cluster",
    "General Commissioning": "General Commissioning Cluster",
    "General Diagnostics": "General Diagnostics Cluster",
    "Software Diagnostics": "Software Diagnostics Cluster",
    "Thread Network Diagnostics": "Thread Network Diagnostics Cluster",
    "Wi-Fi Network Diagnostics": "Wi-Fi Network Diagnostics Cluster",
    "Ethernet Network Diagnostics": "Ethernet Network Diagnostics Cluster",
    "Time Synchronization": "Time Synchronization Cluster",
    "Localization Configuration": "Localization Configuration Cluster",
    "Fixed Label": "Fixed Label Cluster",
    "User Label": "User Label Cluster",
    "Switch": "Switch Cluster",
    "Mode Select": "Mode Select Cluster",
    "Door Lock": "Door Lock Cluster",
    "Window Covering": "Window Covering Cluster",
    "Pump Configuration and Control": "Pump Configuration and Control Cluster",
    "Thermostat User Interface Configuration": "Thermostat User Interface Configuration Cluster",
    "Fan Control": "Fan Control Cluster",
    "Dishwasher Mode": "Dishwasher Mode Cluster",
    "Dishwasher Alarm": "Dishwasher Alarm Cluster",
    "Refrigerator Alarm": "Refrigerator Alarm Cluster",
    "Laundry Washer Mode": "Laundry Washer Mode Cluster",
    "Laundry Washer Controls": "Laundry Washer Controls Cluster",
    "Laundry Dryer Controls": "Laundry Dryer Controls Cluster",
    "Oven Mode": "Oven Mode Cluster",
    "Oven Cavity Operational State": "Oven Cavity Operational State Cluster",
    "Microwave Oven Mode": "Microwave Oven Mode Cluster",
    "Microwave Oven Control": "Microwave Oven Control Cluster",
    "Refrigerator and Temperature Controlled Cabinet Mode": "Refrigerator and Temperature Controlled Cabinet Mode Cluster",
    "RVC Operational State": "RVC Operational State Cluster",
    "RVC Clean Mode": "RVC Clean Mode Cluster",
    "Actions": "Actions Cluster",
    "Unit Localization": "Unit Localization Cluster",
}

# Network Commissioning Feature bits (from Matter spec)
NETWORK_COMMISSIONING_FEATURES = {
    "WiFi": 0,      # F00 - Bit 0
    "Thread": 1,    # F01 - Bit 1
    "Ethernet": 2,  # F02 - Bit 2
}

# Feature to template suffix mapping
FEATURE_TO_TEMPLATE_SUFFIX = {
    "WiFi": "WiFi",
    "Thread": "Thread",
    "Ethernet": "Ethernet",
}

# Global attribute IDs (always supported by Matter stack)
GLOBAL_ATTRIBUTE_IDS = {
    0xFFF8,  # GeneratedCommandList
    0xFFF9,  # AcceptedCommandList
    0xFFFA,  # EventList
    0xFFFB,  # AttributeList
    0xFFFC,  # FeatureMap
    0xFFFD,  # ClusterRevision
}


def load_pics_xml_file_list(pics_xml_path: str) -> list:
    """Load and return sorted list of PICS XML files."""
    all_files = sorted(os.listdir(pics_xml_path))
    
    # Filter out duplicate files
    clean_files = []
    for file in all_files:
        if " - 副本" in file:
            clean_name = file.replace(" - 副本", "")
            if clean_name not in all_files:
                clean_files.append(file)
        else:
            clean_files.append(file)
    
    return clean_files


def get_network_commissioning_feature_from_zap(cluster_data: dict) -> str:
    """
    Extract which network feature (WiFi/Thread/Ethernet) is enabled from FeatureMap.
    Defaults to Thread if no feature is explicitly set (per Matter spec).
    """
    feature_map = get_feature_map_from_zap(cluster_data)
    
    # Check which feature is enabled (can be multiple, but typically only one)
    enabled_features = []
    for feature_name, bit in NETWORK_COMMISSIONING_FEATURES.items():
        if (feature_map >> bit) & 1:
            enabled_features.append(feature_name)
    
    if len(enabled_features) > 1:
        print(f"    [WARNING] Multiple network features enabled: {enabled_features}. Using first: {enabled_features[0]}")
        return enabled_features[0]
    elif len(enabled_features) == 1:
        return enabled_features[0]
    else:
        # Default to Thread per Matter spec recommendation
        print(f"    [INFO] No network feature explicitly set in FeatureMap, defaulting to Thread")
        return "Thread"


def map_cluster_name_to_pics_xml(
    cluster_name: str, 
    pics_xml_file_list: list, 
    cluster_data: Optional[dict] = None
) -> str:
    """
    Map a cluster name to its corresponding PICS XML template file.
    
    For Network Commissioning cluster, the selection depends on which feature
    (WiFi/Thread/Ethernet) is enabled in the FeatureMap. Defaults to Thread.
    """
    pics_base_name = CLUSTER_TO_PICS_DICT.get(cluster_name, cluster_name)
    
    # Special handling for Network Commissioning cluster
    if cluster_name == "Network Commissioning" and cluster_data is not None:
        feature = get_network_commissioning_feature_from_zap(cluster_data)
        suffix = FEATURE_TO_TEMPLATE_SUFFIX.get(feature, "Thread")
        
        # Look for template with feature suffix
        target_pattern = f"{pics_base_name} Test Plan({suffix}).xml"
        
        # Try exact match first
        for file in pics_xml_file_list:
            if file == target_pattern:
                return file
        
        # Try case-insensitive match
        for file in pics_xml_file_list:
            if file.lower() == target_pattern.lower():
                return file
        
        # If not found, try to find any matching template and log warning
        print(f"    [WARNING] Could not find template '{target_pattern}' for {cluster_name} with feature {feature}")
        
        # Fallback: try to find any Network Commissioning template
        for file in pics_xml_file_list:
            if file.lower().startswith(pics_base_name.lower()):
                print(f"    [WARNING] Using fallback template: {file}")
                return file
        
        return ""
    
    # Default handling for other clusters
    # Try exact match first
    for file in pics_xml_file_list:
        if file.lower().startswith(pics_base_name.lower()):
            return file
    
    # Try without "Test Plan" suffix
    for file in pics_xml_file_list:
        file_base = file.lower().replace(" test plan", "").replace(".xml", "")
        if file_base == pics_base_name.lower():
            return file
    
    return ""


def extract_clusters_from_zap(zap_data: dict) -> dict:
    """Extract cluster information from .zap file data."""
    endpoints = {}
    endpoint_types = zap_data.get("endpointTypes", [])
    endpoints_config = zap_data.get("endpoints", [])
    
    for ep_config in endpoints_config:
        ep_type_index = ep_config.get("endpointTypeIndex")
        ep_number = ep_config.get("endpointId")
        
        if ep_type_index is None or ep_number is None:
            continue
            
        if ep_type_index < 0 or ep_type_index >= len(endpoint_types):
            continue
            
        ep_type = endpoint_types[ep_type_index]
        clusters = ep_type.get("clusters", [])
        
        endpoints[ep_number] = {
            "endpoint_type": ep_type,
            "clusters": clusters,
        }
    
    return endpoints


def parse_item_number(item_text: str) -> Optional[dict]:
    """Parse XML itemNumber to extract type and code.
    
    Returns dict with 'side', 'type', 'code' or None if unparseable.
    
    Examples:
        ACL.S           -> side='S', type='role', code=None
        ACL.S.A0000     -> side='S', type='attribute', code=0x0000
        ACL.S.F00       -> side='S', type='feature', code=0
        ACL.S.C00.Rsp   -> side='S', type='command_received', code=0x00
        ACL.S.C01.Tx    -> side='S', type='command_generated', code=0x01
        ACL.S.E00       -> side='S', type='event', code=0x00
        ACL.C           -> side='C', type='role', code=None
        ACL.C.A0000     -> side='C', type='attribute', code=0x0000
        BINFO.S.M.DeviceConfigurationChange -> side='S', type='manual', code='DeviceConfigurationChange'
        BINFO.C.M.SomeManual -> side='C', type='manual', code='SomeManual'
    """
    if not item_text:
        return None
    
    # Role: PREFIX.S or PREFIX.C
    role_match = re.match(r'^([A-Z]+)\.([SC])$', item_text)
    if role_match:
        return {'prefix': role_match.group(1), 'side': role_match.group(2), 'type': 'role', 'code': None}
    
    # Manual: PREFIX.S.M.Name or PREFIX.C.M.Name
    manual_match = re.match(r'^([A-Z]+)\.([SC])\.M\.([A-Za-z]+)$', item_text)
    if manual_match:
        return {'prefix': manual_match.group(1), 'side': manual_match.group(2), 'type': 'manual', 'code': manual_match.group(3)}
    
    # Attribute: PREFIX.S.AXXXX or PREFIX.C.AXXXX
    attr_match = re.match(r'^([A-Z]+)\.([SC])\.A([0-9a-fA-F]{4})$', item_text)
    if attr_match:
        return {'prefix': attr_match.group(1), 'side': attr_match.group(2), 'type': 'attribute', 'code': int(attr_match.group(3), 16)}
    
    # Feature: PREFIX.S.FXX or PREFIX.C.FXX
    feat_match = re.match(r'^([A-Z]+)\.([SC])\.F([0-9a-fA-F]{1,2})$', item_text)
    if feat_match:
        return {'prefix': feat_match.group(1), 'side': feat_match.group(2), 'type': 'feature', 'code': int(feat_match.group(3), 16)}
    
    # Command received (Rsp): PREFIX.S.CXX.Rsp or PREFIX.C.CXX.Rsp
    cmd_rx_match = re.match(r'^([A-Z]+)\.([SC])\.C([0-9a-fA-F]{2})\.Rsp$', item_text)
    if cmd_rx_match:
        return {'prefix': cmd_rx_match.group(1), 'side': cmd_rx_match.group(2), 'type': 'command_received', 'code': int(cmd_rx_match.group(3), 16)}
    
    # Command generated (Tx): PREFIX.S.CXX.Tx or PREFIX.C.CXX.Tx
    cmd_tx_match = re.match(r'^([A-Z]+)\.([SC])\.C([0-9a-fA-F]{2})\.Tx$', item_text)
    if cmd_tx_match:
        return {'prefix': cmd_tx_match.group(1), 'side': cmd_tx_match.group(2), 'type': 'command_generated', 'code': int(cmd_tx_match.group(3), 16)}
    
    # Event: PREFIX.S.EXX or PREFIX.C.EXX
    evt_match = re.match(r'^([A-Z]+)\.([SC])\.E([0-9a-fA-F]{2})$', item_text)
    if evt_match:
        return {'prefix': evt_match.group(1), 'side': evt_match.group(2), 'type': 'event', 'code': int(evt_match.group(3), 16)}
    
    return None


def get_feature_map_from_zap(cluster_data: dict) -> int:
    """Extract FeatureMap value from cluster attributes (code=65532)."""
    attributes = cluster_data.get('attributes', [])
    for attr in attributes:
        if attr.get('code') == 65532:
            default_val = attr.get('defaultValue')
            if default_val is not None:
                if isinstance(default_val, str):
                    default_val = default_val.strip()
                    if default_val.startswith('0x') or default_val.startswith('0X'):
                        return int(default_val, 16)
                    else:
                        try:
                            return int(default_val)
                        except ValueError:
                            return 0
                elif isinstance(default_val, int):
                    return default_val
    return 0


def get_attributes_by_side(cluster_data: dict, side: str) -> set:
    """Return set of attribute codes that are included and match the given side."""
    attributes = cluster_data.get('attributes', [])
    result = set()
    for attr in attributes:
        attr_side = attr.get('side', '')
        if attr.get('included', 0) and attr_side == side:
            result.add(attr.get('code'))
    return result


def get_commands_by_side_and_type(cluster_data: dict, side: str) -> Tuple[Dict[int, bool], Dict[int, bool]]:
    """Return (received_commands, generated_commands) for a specific cluster side.
    
    For a server cluster (side='server'):
    - received: commands with isIncoming=1
    - generated: commands with isIncoming=0
    
    For a client cluster (side='client'):
    - received: commands with isIncoming=1
    - generated: commands with isIncoming=0
    """
    commands = cluster_data.get('commands', [])
    received = {}
    generated = {}
    for cmd in commands:
        code = cmd.get('code')
        if code is None:
            continue
        if not cmd.get('isEnabled', 0):
            continue
        if cmd.get('isIncoming', 0):
            received[code] = True
        else:
            generated[code] = True
    return received, generated


def get_events_by_side(cluster_data: dict, side: str) -> set:
    """Return set of event codes that are included for a specific side."""
    events = cluster_data.get('events', [])
    result = set()
    for evt in events:
        evt_side = evt.get('side', '')
        if evt.get('included', 0) and evt_side == side:
            result.add(evt.get('code'))
    return result


def determine_server_support(parsed: dict, cluster_data: dict) -> str:
    """Determine support for a server-side PICS item based on ZAP data."""
    item_type = parsed['type']
    item_code = parsed['code']
    
    # Check if cluster is enabled as server
    enabled = cluster_data.get('enabled', 0)
    side = cluster_data.get('side', '')
    is_server = (enabled and side == 'server')
    
    if item_type == 'role':
        # Server role: true if cluster enabled as server
        return 'true' if is_server else 'false'
    
    # For non-role items, if cluster is not server, all are false
    if not is_server:
        return 'false'
    
    if item_type == 'attribute':
        # Global attributes are always supported
        if item_code in GLOBAL_ATTRIBUTE_IDS:
            return 'true'
        # Check if attribute is included for server side
        server_attrs = get_attributes_by_side(cluster_data, 'server')
        return 'true' if item_code in server_attrs else 'false'
    
    elif item_type == 'feature':
        # Check FeatureMap bitmap
        feature_map = get_feature_map_from_zap(cluster_data)
        return 'true' if (feature_map >> item_code) & 1 else 'false'
    
    elif item_type == 'command_received':
        # Commands received by server (from client)
        received, _ = get_commands_by_side_and_type(cluster_data, 'server')
        return 'true' if received.get(item_code, False) else 'false'
    
    elif item_type == 'command_generated':
        # Commands generated by server (to client)
        _, generated = get_commands_by_side_and_type(cluster_data, 'server')
        return 'true' if generated.get(item_code, False) else 'false'
    
    elif item_type == 'event':
        # Events for server side
        server_events = get_events_by_side(cluster_data, 'server')
        return 'true' if item_code in server_events else 'false'
    
    elif item_type == 'manual':
        # Manual items are not configurable in ZAP, always false
        return 'false'
    
    return 'false'


def determine_client_support(parsed: dict, cluster_data: dict) -> str:
    """Determine support for a client-side PICS item based on ZAP data."""
    item_type = parsed['type']
    item_code = parsed['code']
    
    # Check if cluster is enabled as client
    enabled = cluster_data.get('enabled', 0)
    side = cluster_data.get('side', '')
    is_client = (enabled and side == 'client')
    
    if item_type == 'role':
        # Client role: true if cluster enabled as client
        return 'true' if is_client else 'false'
    
    # For non-role items, if cluster is not client, all are false
    if not is_client:
        return 'false'
    
    if item_type == 'attribute':
        # Check if attribute is included for client side
        client_attrs = get_attributes_by_side(cluster_data, 'client')
        return 'true' if item_code in client_attrs else 'false'
    
    elif item_type == 'feature':
        # Features are same for server and client
        feature_map = get_feature_map_from_zap(cluster_data)
        return 'true' if (feature_map >> item_code) & 1 else 'false'
    
    elif item_type == 'command_received':
        # Commands received by client (from server)
        received, _ = get_commands_by_side_and_type(cluster_data, 'client')
        return 'true' if received.get(item_code, False) else 'false'
    
    elif item_type == 'command_generated':
        # Commands generated by client (to server)
        _, generated = get_commands_by_side_and_type(cluster_data, 'client')
        return 'true' if generated.get(item_code, False) else 'false'
    
    elif item_type == 'event':
        # Events for client side
        client_events = get_events_by_side(cluster_data, 'client')
        return 'true' if item_code in client_events else 'false'
    
    elif item_type == 'manual':
        # Manual items are not configurable in ZAP, always false
        return 'false'
    
    return 'false'

def generate_pics_xml_for_ota(
    cluster_data_list: List[dict],
    xml_template_path: str,
    output_path: str,
    pics_xml_file_list: list,
    pics_file_name: str
):
    """
    Special handler for OTA Software Update cluster which combines both
    Provider (client) and Requestor (server) into a single XML template.
    
    For manual items (OTAP.S.M.* and OTAR.C.M.*), they are set to true if
    the corresponding cluster (server or client) is enabled.
    """
    if not cluster_data_list:
        return
    
    # Separate server and client data
    server_cluster = None
    client_cluster = None
    for cd in cluster_data_list:
        if cd.get('side') == 'server':
            server_cluster = cd
        elif cd.get('side') == 'client':
            client_cluster = cd
    
    xml_path = xml_template_path.rstrip('\\/').replace('\\', '/') + '/'
    xml_file = f"{xml_path}{pics_file_name}"
    
    # Read original file content to preserve comments
    with open(xml_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Extract the comment block after <?xml ...?>
    comment_match = re.search(r'(<\?xml[^?]*\?>)(<!--.*?-->)(<clusterPICS)', original_content, re.DOTALL)
    header_comment = None
    if comment_match:
        header_comment = comment_match.group(2)
    
    try:
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  [ERROR] Could not parse \"{pics_file_name}\": {e}")
        return
    except FileNotFoundError:
        print(f"  [ERROR] File not found: \"{xml_file}\"")
        return
    
    print(f"  Processing OTA combined template: {pics_file_name}")
    modified_count = 0
    
    def process_node(node):
        nonlocal modified_count
        item_number_element = node.find('itemNumber')
        if item_number_element is None:
            return
        support_element = node.find('support')
        if support_element is None:
            return
        
        item_text = item_number_element.text
        if not item_text:
            return
        
        parsed = parse_item_number(item_text)
        if parsed is None:
            return
        
        old_value = support_element.text
        
        # Special handling for OTA manual items
        if parsed['type'] == 'manual':
            # Server-side manual items (OTAP.S.M.*): true if server_cluster exists and enabled
            if parsed['side'] == 'S' and server_cluster is not None and server_cluster.get('enabled', 0):
                new_support = 'true'
            # Client-side manual items (OTAR.C.M.*): true if client_cluster exists and enabled
            elif parsed['side'] == 'C' and client_cluster is not None and client_cluster.get('enabled', 0):
                new_support = 'true'
            else:
                new_support = 'false'
        else:
            # For non-manual items, use standard decision logic
            if parsed['side'] == 'S':
                if server_cluster is not None:
                    new_support = determine_server_support(parsed, server_cluster)
                else:
                    new_support = 'false'
            elif parsed['side'] == 'C':
                if client_cluster is not None:
                    new_support = determine_client_support(parsed, client_cluster)
                else:
                    new_support = 'false'
            else:
                return
        
        if old_value != new_support:
            support_element.text = new_support
            modified_count += 1
            print(f"    {'✓' if new_support == 'true' else '✗'} Set {item_text} = {new_support} (was {old_value})")
    
    # Process all XML sections
    usage_node = root.find('usage')
    if usage_node is not None:
        for pics_item in usage_node:
            process_node(pics_item)
    
    # Server side
    server_side = root.find("./clusterSide[@type='Server']")
    if server_side is not None:
        for section in ['attributes', 'features', 'commandsReceived', 'commandsGenerated', 'events', 'manually']:
            sec_node = server_side.find(section)
            if sec_node is not None:
                for pics_item in sec_node:
                    process_node(pics_item)
    
    # Client side
    client_side = root.find("./clusterSide[@type='Client']")
    if client_side is not None:
        for section in ['attributes', 'features', 'commandsReceived', 'commandsGenerated', 'events', 'manually']:
            sec_node = client_side.find(section)
            if sec_node is not None:
                for pics_item in sec_node:
                    process_node(pics_item)
    
    if modified_count == 0:
        print(f"    No modifications needed (all items already match ZAP)")
    
    # Write output
    output_file = f"{output_path}{pics_file_name}"
    indent_xml(root)
    xml_buffer = io.StringIO()
    tree.write(xml_buffer, encoding="unicode", xml_declaration=True)
    xml_content = xml_buffer.getvalue()
    xml_content = xml_content.replace("<?xml version='1.0' encoding='utf-8'?>", '<?xml version="1.0" encoding="utf-8"?>')
    xml_content = xml_content.lstrip()
    if header_comment:
        decl_match = re.search(r'(<\?xml[^?]*\?>)', xml_content)
        if decl_match:
            decl_end = decl_match.end()
            rest_content = xml_content[decl_end:].lstrip()
            xml_content = xml_content[:decl_end] + header_comment + rest_content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"  ✓ Generated: {output_file}")

def generate_pics_xml(
    cluster_name: str,
    cluster_data: dict,
    xml_template_path: str,
    output_path: str,
    pics_xml_file_list: list,
):
    """Generate PICS XML file for a cluster by updating the template."""
    
    # Find matching PICS XML template
    pics_file_name = map_cluster_name_to_pics_xml(cluster_name, pics_xml_file_list, cluster_data)
    if not pics_file_name:
        print(f"  [WARNING] Could not find matching PICS XML template for \"{cluster_name}\"")
        return
    
    xml_path = xml_template_path.rstrip('\\/').replace('\\', '/') + '/'
    xml_file = f"{xml_path}{pics_file_name}"
    
    # Read original file content to preserve comments
    with open(xml_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Extract the comment block after <?xml ...?>
    comment_match = re.search(r'(<\?xml[^?]*\?>)(<!--.*?-->)(<clusterPICS)', original_content, re.DOTALL)
    header_comment = None
    if comment_match:
        header_comment = comment_match.group(2)
    
    try:
        # Parse the XML template
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(xml_file, parser)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  [ERROR] Could not parse \"{pics_file_name}\": {e}")
        return
    except FileNotFoundError:
        print(f"  [ERROR] File not found: \"{xml_file}\"")
        return
    
    print(f"  Processing template: {pics_file_name}")
    modified_count = 0
    
    # Helper function to process a node
    def process_node(node):
        nonlocal modified_count
        item_number_element = node.find('itemNumber')
        if item_number_element is None:
            return
        support_element = node.find('support')
        if support_element is None:
            return
        
        item_text = item_number_element.text
        if not item_text:
            return
        
        parsed = parse_item_number(item_text)
        if parsed is None:
            return
        
        old_value = support_element.text
        
        # Determine new support value based on side
        if parsed['side'] == 'S':
            new_support = determine_server_support(parsed, cluster_data)
        elif parsed['side'] == 'C':
            new_support = determine_client_support(parsed, cluster_data)
        else:
            return
        
        # Update if changed
        if old_value != new_support:
            support_element.text = new_support
            modified_count += 1
            print(f"    {'✓' if new_support == 'true' else '✗'} Set {item_text} = {new_support} (was {old_value})")
    
    # Process all XML sections
    # 1. Usage (role)
    usage_node = root.find('usage')
    if usage_node is not None:
        for pics_item in usage_node:
            process_node(pics_item)
    
    # 2. Server side
    server_side = root.find("./clusterSide[@type='Server']")
    if server_side is not None:
        # Server attributes
        attrs_node = server_side.find('attributes')
        if attrs_node is not None:
            for pics_item in attrs_node:
                process_node(pics_item)
        
        # Server features
        features_node = server_side.find('features')
        if features_node is not None:
            for pics_item in features_node:
                process_node(pics_item)
        
        # Server commands received
        cmds_rx_node = server_side.find('commandsReceived')
        if cmds_rx_node is not None:
            for pics_item in cmds_rx_node:
                process_node(pics_item)
        
        # Server commands generated
        cmds_tx_node = server_side.find('commandsGenerated')
        if cmds_tx_node is not None:
            for pics_item in cmds_tx_node:
                process_node(pics_item)
        
        # Server events
        events_node = server_side.find('events')
        if events_node is not None:
            for pics_item in events_node:
                process_node(pics_item)
        
        # Server manually
        manually_node = server_side.find('manually')
        if manually_node is not None:
            for pics_item in manually_node:
                process_node(pics_item)
    
    # 3. Client side
    client_side = root.find("./clusterSide[@type='Client']")
    if client_side is not None:
        # Client attributes
        attrs_node = client_side.find('attributes')
        if attrs_node is not None:
            for pics_item in attrs_node:
                process_node(pics_item)
        
        # Client features
        features_node = client_side.find('features')
        if features_node is not None:
            for pics_item in features_node:
                process_node(pics_item)
        
        # Client commands received
        cmds_rx_node = client_side.find('commandsReceived')
        if cmds_rx_node is not None:
            for pics_item in cmds_rx_node:
                process_node(pics_item)
        
        # Client commands generated
        cmds_tx_node = client_side.find('commandsGenerated')
        if cmds_tx_node is not None:
            for pics_item in cmds_tx_node:
                process_node(pics_item)
        
        # Client events
        events_node = client_side.find('events')
        if events_node is not None:
            for pics_item in events_node:
                process_node(pics_item)
        
        # Client manually
        manually_node = client_side.find('manually')
        if manually_node is not None:
            for pics_item in manually_node:
                process_node(pics_item)
    
    if modified_count == 0:
        print(f"    No modifications needed (all items already match ZAP)")
    
    # Write the output XML file
    output_file = f"{output_path}{pics_file_name}"
    indent_xml(root)
    
    # Convert tree to string
    xml_buffer = io.StringIO()
    tree.write(xml_buffer, encoding="unicode", xml_declaration=True)
    xml_content = xml_buffer.getvalue()
    
    # Fix single quotes to double quotes in XML declaration
    xml_content = xml_content.replace("<?xml version='1.0' encoding='utf-8'?>", '<?xml version="1.0" encoding="utf-8"?>')
    xml_content = xml_content.lstrip()
    
    # Insert the header comment after <?xml ...?> if it exists
    if header_comment:
        decl_match = re.search(r'(<\?xml[^?]*\?>)', xml_content)
        if decl_match:
            decl_end = decl_match.end()
            rest_content = xml_content[decl_end:].lstrip()
            xml_content = xml_content[:decl_end] + header_comment + rest_content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"  ✓ Generated: {output_file}")


def get_supported_networks(zap_data: dict) -> Dict[str, bool]:
    """
    Determine which network technologies (WiFi, Thread, Ethernet) are supported
    by examining Network Commissioning cluster commands.
    """
    networks = {'wifi': False, 'thread': False, 'ethernet': False}
    endpoints = extract_clusters_from_zap(zap_data)
    
    for ep_data in endpoints.values():
        for cluster in ep_data.get('clusters', []):
            if cluster.get('name') == 'Network Commissioning' and cluster.get('enabled', 0):
                for cmd in cluster.get('commands', []):
                    name = cmd.get('name', '')
                    if name == 'AddOrUpdateWiFiNetwork':
                        networks['wifi'] = True
                    elif name == 'AddOrUpdateThreadNetwork':
                        networks['thread'] = True
                    elif name == 'AddOrUpdateEthernetNetwork':
                        networks['ethernet'] = True
    return networks


def get_device_roles(zap_data: dict) -> Dict[str, bool]:
    """
    Determine the Matter roles of the device:
    - Commissionee: almost always true for Matter devices.
    - Commissioner: true if the device has AdministratorCommissioning client or NetworkCommissioning client.
    - Controller: true if the device has any client cluster that is not a provisioning helper.
    """
    # Commissionee: any device that has OperationalCredentials server is a commissionee.
    # For safety, default True because all Matter devices are commissionable.
    is_commissionee = True
    
    is_commissioner = False
    is_controller = False
    
    endpoints = extract_clusters_from_zap(zap_data)
    
    # Clusters that, when present as client, indicate the device can actively control other devices.
    # Exclude clusters that are only used for OTA or commissioning.
    controller_client_clusters = {
        "OnOff", "Level Control", "Color Control", "Window Covering",
        "Door Lock", "Thermostat", "Fan Control", "Media Playback",
        "Keypad Input", "Wake on LAN", "Channel", "Target Navigator",
        "Media Input", "Audio Output", "Application Launcher",
        "Content Launcher", "Account Login", "Binding", "Scenes Management",
        "Groups", "Identify"
    }
    
    for ep_data in endpoints.values():
        for cluster in ep_data.get('clusters', []):
            if not cluster.get('enabled', 0):
                continue
            side = cluster.get('side')
            name = cluster.get('name')
            
            # Commissioner detection: has client side of AdministratorCommissioning or NetworkCommissioning
            if side == 'client' and name in ('Administrator Commissioning', 'Network Commissioning'):
                is_commissioner = True
            
            # Controller detection: has any client side cluster from the list above
            if side == 'client' and name in controller_client_clusters:
                is_controller = True
    
    return {
        'commissionee': is_commissionee,
        'commissioner': is_commissioner,
        'controller': is_controller
    }


def generate_base_xml(zap_data: dict, xml_template_path: str, output_path: str):
    """
    Generate Base.xml according to the actual device capabilities extracted from .zap file.
    """
    xml_path = xml_template_path.rstrip('\\/').replace('\\', '/') + '/'
    base_template = f"{xml_path}Base.xml"
    if not os.path.exists(base_template):
        print(f"  [WARNING] Base.xml template not found at {base_template}, skipping.")
        return
    
    # Read original file to preserve comments
    with open(base_template, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Extract header comment
    comment_match = re.search(r'(<\?xml[^?]*\?>)(<!--.*?-->)(<generalPICS)', original_content, re.DOTALL)
    header_comment = None
    if comment_match:
        header_comment = comment_match.group(2)
    
    try:
        parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
        tree = ET.parse(base_template, parser)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"  [ERROR] Could not parse Base.xml: {e}")
        return
    
    # Get device capabilities
    networks = get_supported_networks(zap_data)
    roles = get_device_roles(zap_data)
    
    # Determine wireless support summary
    wifi_supported = networks['wifi']
    thread_supported = networks['thread']
    ethernet_supported = networks['ethernet']
    wireless_supported = wifi_supported or thread_supported
    
    print(f"  Detected network capabilities: WiFi={wifi_supported}, Thread={thread_supported}, Ethernet={ethernet_supported}")
    print(f"  Detected roles: Commissionee={roles['commissionee']}, Commissioner={roles['commissioner']}, Controller={roles['controller']}")
    
    # Update each picsItem
    modified_count = 0
    for pics_item in root.findall(".//picsItem"):
        item_elem = pics_item.find('itemNumber')
        support_elem = pics_item.find('support')
        if item_elem is None or support_elem is None:
            continue
        item_text = item_elem.text
        if not item_text:
            continue
        
        old_value = support_elem.text
        new_value = None
        
        # Communication
        if item_text == 'MCORE.COM.BLE':
            # Most Matter devices support BLE commissioning; keep template default (true)
            pass
        elif item_text == 'MCORE.COM.WIFI_2P4GHZ':
            new_value = 'true' if wifi_supported else 'false'
        elif item_text == 'MCORE.COM.WIFI_5GHZ':
            new_value = 'true' if wifi_supported else 'false'
        elif item_text == 'MCORE.COM.WIFI':
            new_value = 'true' if wifi_supported else 'false'
        elif item_text == 'MCORE.COM.ETH':
            new_value = 'true' if ethernet_supported else 'false'
        elif item_text == 'MCORE.COM.THR':
            new_value = 'true' if thread_supported else 'false'
        elif item_text == 'MCORE.COM.WIRELESS':
            new_value = 'true' if wireless_supported else 'false'
        # Roles
        elif item_text == 'MCORE.ROLE.COMMISSIONER':
            new_value = 'true' if roles['commissioner'] else 'false'
        elif item_text == 'MCORE.ROLE.COMMISSIONEE':
            new_value = 'true' if roles['commissionee'] else 'false'
        elif item_text == 'MCORE.ROLE.CONTROLLER':
            new_value = 'true' if roles['controller'] else 'false'
        # For all other items (like MCORE.DD.*), keep template unchanged
        # This includes MCORE.DD.QR, MCORE.DD.MANUAL_PC, etc.
        
        if new_value is not None and new_value != old_value:
            support_elem.text = new_value
            modified_count += 1
            print(f"    {'✓' if new_value == 'true' else '✗'} Set {item_text} = {new_value} (was {old_value})")
    
    if modified_count == 0:
        print(f"  No Base.xml modifications needed (already matches ZAP)")
    
    # Write output
    output_file = f"{output_path}Base.xml"
    indent_xml(root)
    xml_buffer = io.StringIO()
    tree.write(xml_buffer, encoding="unicode", xml_declaration=True)
    xml_content = xml_buffer.getvalue()
    xml_content = xml_content.replace("<?xml version='1.0' encoding='utf-8'?>", '<?xml version="1.0" encoding="utf-8"?>')
    xml_content = xml_content.lstrip()
    if header_comment:
        decl_match = re.search(r'(<\?xml[^?]*\?>)', xml_content)
        if decl_match:
            decl_end = decl_match.end()
            rest_content = xml_content[decl_end:].lstrip()
            xml_content = xml_content[:decl_end] + header_comment + rest_content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"  ✓ Generated Base.xml (customized)")


def indent_xml(elem, level=0):
    """Add indentation to XML element for better readability."""
    indent = "\n" + level * "	"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "	"
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for i, subelem in enumerate(elem):
            indent_xml(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent

def process_zap_file(zap_file: str, xml_template_path: str, output_path: str):
    """Main function to process a .zap file and generate PICS XML files."""
    
    # Load .zap file
    print(f"Loading .zap file: {zap_file}")
    with open(zap_file, 'r', encoding='utf-8') as f:
        zap_data = json.load(f)
    
    # Load PICS XML template list
    print(f"Loading PICS XML templates from: {xml_template_path}")
    pics_xml_file_list = load_pics_xml_file_list(xml_template_path)
    print(f"  Found {len(pics_xml_file_list)} template files")
    
    # Create output directory
    output_path = output_path.rstrip('\\/') + '/'
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_path}")
    
    # Extract clusters from .zap file
    endpoints = extract_clusters_from_zap(zap_data)
    
    if not endpoints:
        print("[WARNING] No endpoints found in .zap file")
        return
    
    print(f"\nFound {len(endpoints)} endpoint(s) in .zap file")
    
    # Process each endpoint
    for ep_number, ep_data in sorted(endpoints.items()):
        print(f"\n{'='*60}")
        print(f"Processing endpoint {ep_number} -> EP{ep_number}")
        print(f"{'='*60}")
        
        clusters = ep_data.get("clusters", [])
        print(f"  Found {len(clusters)} cluster(s)")
        
        # Create endpoint-specific output directory
        ep_output_path = f"{output_path}EP{ep_number}/"
        pathlib.Path(ep_output_path).mkdir(parents=True, exist_ok=True)
        
        # Generate Base.xml only for EP0 (global PICS items)
        if ep_number == 0:
            print(f"\n  Generating Base.xml for endpoint EP0...")
            generate_base_xml(zap_data, xml_template_path, ep_output_path)
        
        # --- Special handling for OTA Software Update (dual cluster) ---
        # Collect clusters that map to the OTA template
        ota_clusters = []
        other_clusters = []
        ota_template_name = "OTA Software Update Test Plan.xml"
        
        for cluster in clusters:
            cluster_name = cluster.get("name", "")
            if not cluster.get("enabled", 0):
                continue
            template = map_cluster_name_to_pics_xml(cluster_name, pics_xml_file_list, cluster)
            if template == ota_template_name:
                ota_clusters.append(cluster)
            else:
                other_clusters.append(cluster)
        
        # Generate OTA combined XML if any OTA clusters exist
        if ota_clusters:
            print(f"\n  Processing OTA Software Update (combined) with {len(ota_clusters)} cluster(s)...")
            generate_pics_xml_for_ota(
                cluster_data_list=ota_clusters,
                xml_template_path=xml_template_path,
                output_path=ep_output_path,
                pics_xml_file_list=pics_xml_file_list,
                pics_file_name=ota_template_name
            )
        
        # Process all other clusters normally
        for cluster in other_clusters:
            cluster_name = cluster.get("name", "")
            cluster_code = cluster.get("code", 0)
            cluster_enabled = cluster.get("enabled", 0)
            cluster_side = cluster.get("side", "")
            
            if not cluster_enabled:
                print(f"\n  Skipping disabled cluster: {cluster_name} (0x{cluster_code:04x})")
                continue
            
            print(f"\n  Processing cluster: {cluster_name} (0x{cluster_code:04x}) [side={cluster_side}]")
            generate_pics_xml(
                cluster_name=cluster_name,
                cluster_data=cluster,
                xml_template_path=xml_template_path,
                output_path=ep_output_path,
                pics_xml_file_list=pics_xml_file_list,
            )
    
    print(f"\n{'='*60}")
    print("Conversion complete!")
    print(f"{'='*60}")
    
    # Print summary
    total_files = 0
    for root, _, files in os.walk(output_path):
        total_files += len(files)
    print(f"\nSummary:")
    print(f"  - Processed {len(endpoints)} endpoint(s)")
    print(f"  - Generated {total_files} PICS XML file(s)")
    print(f"  - Output directory: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert .zap files to PICS XML files using Matter V1.5 PICS XML templates"
    )
    parser.add_argument(
        '-z', '--zap-file',
        required=True,
        help='Path to the .zap file to convert'
    )
    parser.add_argument(
        '-p', '--pics-template',
        required=True,
        help='Path to the folder containing PICS XML templates'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Path to the output folder for generated PICS XML files'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    if not os.path.exists(args.zap_file):
        print(f"Error: .zap file not found: {args.zap_file}")
        sys.exit(1)
    
    if not os.path.exists(args.pics_template):
        print(f"Error: PICS template directory not found: {args.pics_template}")
        sys.exit(1)
    
    print("="*60)
    print("Zap2Xml - Matter PICS XML Generator")
    print("="*60)
    print()
    
    process_zap_file(args.zap_file, args.pics_template, args.output)


if __name__ == "__main__":
    main()