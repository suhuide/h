```c
Administrator@USER-20251222OC MINGW64 /c/hrf/aok/aok02_matter_ac (develop)
$ git diff 779f785c71412d7e0819d177d3c2e63614944675 bae21302fdbcfb275c512754792a525d5c68381b ':!.cproject'
diff --git a/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.2
0221205.gcc.slsproj b/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt
.12.2.1.20221205.gcc.slsproj
index 37273f4..4859979 100644
--- a/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205
.gcc.slsproj
+++ b/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205
.gcc.slsproj
@@ -38,6 +38,7 @@
     <file name="sl_clock_manager_oscillator_config.h" generated="true" linked="false"/>
     <file name="sl_clock_manager_tree_config.h" generated="true" linked="false"/>
     <file name="sl_rail_util_pti_config.h" generated="true" linked="false"/>
+    <file name="sl_simple_led_led0_config.h" generated="true" linked="false"/>^M
     <file name="sl_uartdrv_eusart_serial_config.h" generated="true" linked="false"/>
     <file name="sl_uartdrv_eusart_vcom_config.h" generated="true" linked="false"/>
     <file name="nvm3_default_config.h" generated="true" linked="false"/>
@@ -76,7 +77,6 @@
     <file name="emlib_core_debug_config.h" generated="true" linked="false"/>
     <file name="sl_mbedtls_config.h" generated="true" linked="false"/>
     <file name="sl_mbedtls_device_config.h" generated="true" linked="false"/>
-    <file name="sl_simple_led_led0_config.h" generated="true" linked="false"/>
   </folder>
   <includePath uri="studio:/project/config"/>
   <includePath uri="studio:/project/config/app/icd/server"/>
```
```c
Administrator@USER-20251222OC MINGW64 /c/hrf/aok/aok02_matter_ac (develop)
$ git diff 64d01ae225ad1523ca69bb22a8151a6b3fdfbf67 779f785c71412d7e0819d177d3c2e63614944675 ':!.cproject'
diff --git a/.pdm/uc.module.setup.componentSetup.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj b/.pdm/uc.module.setup.componentSetup.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
index 85e5d4a..e670d28 100644
--- a/.pdm/uc.module.setup.componentSetup.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
+++ b/.pdm/uc.module.setup.componentSetup.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
@@ -1,17 +1,48 @@
 <?xml version="1.0" encoding="UTF-8"?>
 <project name="uc.module.setup.componentSetup.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt:12.2.1.20221205.gcc" propertyScope="project">
   <folder name="src">
-    <file name="AppTask.cpp" linked="false" uri="studio:/project/src/AppTask.cpp"/>
     <file name="main.cpp" linked="false" uri="studio:/project/src/main.cpp"/>
-    <file name="WindowManager.cpp" linked="false" uri="studio:/project/src/WindowManager.cpp"/>
-    <file name="ZclCallbacks.cpp" linked="false" uri="studio:/project/src/ZclCallbacks.cpp"/>
   </folder>
-  <folder name="include">
-    <file name="AppConfig.h" linked="false" uri="studio:/project/include/AppConfig.h"/>
-    <file name="CHIPProjectConfig.h" linked="false" uri="studio:/project/include/CHIPProjectConfig.h"/>
-    <file name="WindowManager.h" linked="false" uri="studio:/project/include/WindowManager.h"/>
-    <file name="AppTask.h" linked="false" uri="studio:/project/include/AppTask.h"/>
-    <file name="AppEvent.h" linked="false" uri="studio:/project/include/AppEvent.h"/>
+  <folder name="common">
+    <folder name="app">
+      <file name="app_ble_mgr.cpp" linked="false" uri="studio:/project/common/app/app_ble_mgr.cpp"/>
+      <file name="app_colorlight_mgr.cpp" linked="false" uri="studio:/project/common/app/app_colorlight_mgr.cpp"/>
+      <file name="app_comm_mgr.cpp" linked="false" uri="studio:/project/common/app/app_comm_mgr.cpp"/>
+      <file name="app_endpoint_mgr.cpp" linked="false" uri="studio:/project/common/app/app_endpoint_mgr.cpp"/>
+      <file name="app_identify_mgr.cpp" linked="false" uri="studio:/project/common/app/app_identify_mgr.cpp"/>
+      <file name="app_msg_mgr.cpp" linked="false" uri="studio:/project/common/app/app_msg_mgr.cpp"/>
+      <file name="app_nwk_mgr.cpp" linked="false" uri="studio:/project/common/app/app_nwk_mgr.cpp"/>
+      <file name="app_phone_mgr.cpp" linked="false" uri="studio:/project/common/app/app_phone_mgr.cpp"/>
+      <file name="app_spm_mgr.cpp" linked="false" uri="studio:/project/common/app/app_spm_mgr.cpp"/>
+      <file name="app_timetask_mgr.cpp" linked="false" uri="studio:/project/common/app/app_timetask_mgr.cpp"/>
+      <file name="app_wdc_mgr.cpp" linked="false" uri="studio:/project/common/app/app_wdc_mgr.cpp"/>
+      <file name="AppTask.cpp" linked="false" uri="studio:/project/common/app/AppTask.cpp"/>
+      <file name="color_format.cpp" linked="false" uri="studio:/project/common/app/color_format.cpp"/>
+      <file name="rgb_light.cpp" linked="false" uri="studio:/project/common/app/rgb_light.cpp"/>
+      <file name="ZclCallbacks.cpp" linked="false" uri="studio:/project/common/app/ZclCallbacks.cpp"/>
+      <file name="log_api.c" linked="false" uri="studio:/project/common/app/log_api.c"/>
+      <file name="app_lockout_mgr.c" linked="false" uri="studio:/project/common/app/app_lockout_mgr.c"/>
+    </folder>
+    <folder name="event_queue">
+      <file name="event_handler.c" linked="false" uri="studio:/project/common/event_queue/event_handler.c"/>
+      <file name="event-queue.c" linked="false" uri="studio:/project/common/event_queue/event-queue.c"/>
+      <file name="hal_ticktimer.c" linked="false" uri="studio:/project/common/event_queue/hal_ticktimer.c"/>
+    </folder>
+    <folder name="hal">
+      <file name="hal_uart.cpp" linked="false" uri="studio:/project/common/hal/hal_uart.cpp"/>
+      <file name="wdg_api.c" linked="false" uri="studio:/project/common/hal/wdg_api.c"/>
+    </folder>
+    <folder name="misc">
+      <file name="ble_connection.cpp" linked="false" uri="studio:/project/common/misc/ble_connection.cpp"/>
+      <file name="dev_mapping.cpp" linked="false" uri="studio:/project/common/misc/dev_mapping.cpp"/>
+      <file name="phone_nvm3_table.cpp" linked="false" uri="studio:/project/common/misc/phone_nvm3_table.cpp"/>
+      <file name="phone_protocol.cpp" linked="false" uri="studio:/project/common/misc/phone_protocol.cpp"/>
+      <file name="rc_nvm3_table.cpp" linked="false" uri="studio:/project/common/misc/rc_nvm3_table.cpp"/>
+      <file name="rc_protocol.cpp" linked="false" uri="studio:/project/common/misc/rc_protocol.cpp"/>
+      <file name="sp_protocol.cpp" linked="false" uri="studio:/project/common/misc/sp_protocol.cpp"/>
+      <file name="sys_config.cpp" linked="false" uri="studio:/project/common/misc/sys_config.cpp"/>
+      <file name="time_task.cpp" linked="false" uri="studio:/project/common/misc/time_task.cpp"/>
+    </folder>
   </folder>
   <folder name="matter_2.5.2">
     <folder name="third_party">
@@ -214,31 +245,6 @@
               <file name="CHIPMem.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/support/CHIPMem.cpp"/>
               <file name="CHIPPlatformMemory.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/support/CHIPPlatformMemory.cpp"/>
             </folder>
-            <folder name="shell">
-              <folder name="commands">
-                <file name="Help.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Help.cpp"/>
-                <file name="Meta.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Meta.cpp"/>
-                <file name="Config.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Config.cpp"/>
-                <file name="Device.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Device.cpp"/>
-                <file name="Stat.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Stat.cpp"/>
-                <file name="OnboardingCodes.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/OnboardingCodes.cpp"/>
-                <file name="Dns.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Dns.cpp"/>
-                <file name="BLE.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/BLE.cpp"/>
-                <file name="Ota.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Ota.cpp"/>
-                <file name="Help.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Help.h"/>
-              </folder>
-              <file name="CommandSet.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/CommandSet.cpp"/>
-              <file name="Engine.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Engine.cpp"/>
-              <file name="streamer.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer.cpp"/>
-              <file name="streamer_silabs.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer_silabs.cpp"/>
-              <file name="MainLoopSilabs.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/MainLoopSilabs.cpp"/>
-              <file name="Engine.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Engine.h"/>
-              <file name="Command.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Command.h"/>
-              <file name="Commands.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Commands.h"/>
-              <file name="CommandSet.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/CommandSet.h"/>
-              <file name="streamer.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer.h"/>
-              <file name="SubShellCommand.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/SubShellCommand.h"/>
-            </folder>
           </folder>
           <folder name="app">
             <folder name="reporting">
@@ -380,13 +386,14 @@
                 <file name="basic-information.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/basic-information/basic-information.cpp"/>
                 <file name="basic-information.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/basic-information/basic-information.h"/>
               </folder>
+              <folder name="color-control-server">
+                <file name="color-control-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.cpp"/>
+                <file name="color-control-server.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.h"/>
+              </folder>
               <folder name="descriptor">
                 <file name="descriptor.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/descriptor/descriptor.cpp"/>
                 <file name="descriptor.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/descriptor/descriptor.h"/>
               </folder>
-              <folder name="ethernet-network-diagnostics-server">
-                <file name="ethernet-network-diagnostics-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/ethernet-network-diagnostics-server/ethernet-network-diagnostics-server.cpp"/>
-              </folder>
               <folder name="fixed-label-server">
                 <file name="fixed-label-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/fixed-label-server/fixed-label-server.cpp"/>
               </folder>
@@ -415,6 +422,10 @@
                 <file name="identify-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/identify-server/identify-server.cpp"/>
                 <file name="identify-server.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/identify-server/identify-server.h"/>
               </folder>
+              <folder name="level-control">
+                <file name="level-control.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/level-control/level-control.cpp"/>
+                <file name="level-control.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/level-control/level-control.h"/>
+              </folder>
               <folder name="localization-configuration-server">
                 <file name="localization-configuration-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/localization-configuration-server/localization-configuration-server.cpp"/>
               </folder>
@@ -422,6 +433,10 @@
                 <file name="network-commissioning.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/network-commissioning/network-commissioning.cpp"/>
                 <file name="network-commissioning.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/network-commissioning/network-commissioning.h"/>
               </folder>
+              <folder name="on-off-server">
+                <file name="on-off-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.cpp"/>
+                <file name="on-off-server.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.h"/>
+              </folder>
               <folder name="operational-credentials-server">
                 <file name="operational-credentials-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/operational-credentials-server/operational-credentials-server.cpp"/>
               </folder>
@@ -466,15 +481,15 @@
               <folder name="user-label-server">
                 <file name="user-label-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/user-label-server/user-label-server.cpp"/>
               </folder>
-              <folder name="wifi-network-diagnostics-server">
-                <file name="wifi-network-diagnostics-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/wifi-network-diagnostics-server/wifi-network-diagnostics-server.cpp"/>
-              </folder>
               <folder name="window-covering-server">
                 <file name="window-covering-server.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/window-covering-server/window-covering-server.cpp"/>
                 <file name="window-covering-delegate.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/window-covering-server/window-covering-delegate.h"/>
                 <file name="window-covering-server.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/window-covering-server/window-covering-server.h"/>
               </folder>
             </folder>
+            <folder name="cluster-building-blocks">
+              <file name="QuieterReporting.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/cluster-building-blocks/QuieterReporting.h"/>
+            </folder>
             <folder name="MessageDef">
               <file name="ArrayBuilder.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/MessageDef/ArrayBuilder.cpp"/>
               <file name="ArrayParser.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/MessageDef/ArrayParser.cpp"/>
@@ -1214,12 +1229,6 @@
                 <file name="ProvisionStorageDefault.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/provision/ProvisionStorageDefault.cpp"/>
                 <file name="ProvisionStorageCustom.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/provision/ProvisionStorageCustom.cpp"/>
               </folder>
-              <folder name="shell">
-                <folder name="icd">
-                  <file name="ICDShellCommands.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.cpp"/>
-                  <file name="ICDShellCommands.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.h"/>
-                </folder>
-              </folder>
               <file name="board_config.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/board_config.h"/>
               <file name="OTAConfig.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/OTAConfig.h"/>
               <file name="SoftwareFaultReports.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/SoftwareFaultReports.h"/>
@@ -1240,8 +1249,6 @@
               <file name="MatterConfig.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterConfig.cpp"/>
               <file name="SoftwareFaultReports.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/SoftwareFaultReports.cpp"/>
               <file name="LEDWidget.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/LEDWidget.cpp"/>
-              <file name="MatterShell.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterShell.cpp"/>
-              <file name="MatterShell.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterShell.h"/>
               <file name="syscalls_stubs.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/syscalls_stubs.cpp"/>
               <file name="SilabsTestEventTriggerDelegate.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/SilabsTestEventTriggerDelegate.cpp"/>
               <file name="uart.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/uart.cpp"/>
@@ -1252,17 +1259,6 @@
             <file name="DeviceInfoProviderImpl.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/providers/DeviceInfoProviderImpl.cpp"/>
             <file name="DeviceInfoProviderImpl.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/providers/DeviceInfoProviderImpl.h"/>
           </folder>
-          <folder name="shell">
-            <folder name="shell_common">
-              <folder name="include">
-                <file name="ChipShellCollection.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/include/ChipShellCollection.h"/>
-                <file name="Globals.h" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/include/Globals.h"/>
-              </folder>
-              <file name="cmd_misc.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/cmd_misc.cpp"/>
-              <file name="cmd_otcli.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/cmd_otcli.cpp"/>
-              <file name="globals.cpp" uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/globals.cpp"/>
-            </folder>
-          </folder>
         </folder>
       </folder>
       <folder name="nlassert">
@@ -2144,22 +2140,22 @@
           <folder name="gcc">
             <folder name="cortex-m33">
               <folder name="ble_host">
-                <folder name="ble_bgapi">
-                  <folder name="release">
-                    <file name="libble_bgapi_gatt_server.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_gatt_server.a"/>
-                    <file name="libble_bgapi.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi.a"/>
-                    <file name="libble_bgapi_stub_gatt_client.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_stub_gatt_client.a"/>
-                  </folder>
-                </folder>
                 <folder name="accept_list">
                   <folder name="release">
-                    <file name="libble_host_accept_list_stub.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list_stub.a"/>
+                    <file name="libble_host_accept_list.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list.a"/>
                   </folder>
                 </folder>
                 <folder name="bgstack">
                   <folder name="release">
+                    <file name="libbondingdb.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb.a"/>
                     <file name="libble_host.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libble_host.a"/>
-                    <file name="libbondingdb_stub.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb_stub.a"/>
+                  </folder>
+                </folder>
+                <folder name="ble_bgapi">
+                  <folder name="release">
+                    <file name="libble_bgapi_gatt_server.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_gatt_server.a"/>
+                    <file name="libble_bgapi.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi.a"/>
+                    <file name="libble_bgapi_stub_gatt_client.a" uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_stub_gatt_client.a"/>
                   </folder>
                 </folder>
                 <folder name="hal">
@@ -2193,10 +2189,20 @@
         </folder>
       </folder>
       <folder name="openthread">
+        <folder name="libs">
+          <file name="libsl_ot_stack_mtd_efr32mg24_gcc.a" uri="studio:/sdk/protocol/openthread/libs/libsl_ot_stack_mtd_efr32mg24_gcc.a"/>
+          <file name="libsl_openthread_cm33_gcc.a" uri="studio:/sdk/protocol/openthread/libs/libsl_openthread_cm33_gcc.a"/>
+        </folder>
         <folder name="src">
-          <folder name="cli">
-            <file name="bluetooth_cli.c" uri="studio:/sdk/protocol/openthread/src/cli/bluetooth_cli.c"/>
-            <file name="cli_utils.c" uri="studio:/sdk/protocol/openthread/src/cli/cli_utils.c"/>
+          <folder name="stubs">
+            <folder name="diag">
+              <file name="diag_stubs.c" uri="studio:/sdk/protocol/openthread/src/stubs/diag/diag_stubs.c"/>
+              <file name="diags_api_stubs.cpp" uri="studio:/sdk/protocol/openthread/src/stubs/diag/diags_api_stubs.cpp"/>
+              <file name="factory_diags_stubs.cpp" uri="studio:/sdk/protocol/openthread/src/stubs/diag/factory_diags_stubs.cpp"/>
+            </folder>
+            <folder name="tcp">
+              <file name="tcp_stubs.c" uri="studio:/sdk/protocol/openthread/src/stubs/tcp/tcp_stubs.c"/>
+            </folder>
           </folder>
         </folder>
         <folder name="platform-abstraction">
@@ -2221,7 +2227,6 @@
             <file name="sl_multipan.h" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/sl_multipan.h"/>
             <file name="soft_source_match_table.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/soft_source_match_table.c"/>
             <file name="alarm.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/alarm.c"/>
-            <file name="diag.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/diag.c"/>
             <file name="entropy.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/entropy.c"/>
             <file name="flash.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/flash.c"/>
             <file name="memory.c" uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32/memory.c"/>
@@ -2311,12 +2316,8 @@
             <file name="radio_power_manager.h" uri="studio:/sdk/protocol/openthread/platform-abstraction/include/radio_power_manager.h"/>
           </folder>
         </folder>
-        <folder name="libs">
-          <file name="libsl_openthread_cm33_gcc.a" uri="studio:/sdk/protocol/openthread/libs/libsl_openthread_cm33_gcc.a"/>
-        </folder>
         <folder name="include">
           <file name="sl_openthread_package_info.h" uri="studio:/sdk/protocol/openthread/include/sl_openthread_package_info.h"/>
-          <file name="sl_ot_custom_cli.h" uri="studio:/sdk/protocol/openthread/include/sl_ot_custom_cli.h"/>
         </folder>
       </folder>
     </folder>
@@ -2602,77 +2603,102 @@
           </folder>
         </folder>
         <folder name="openthread">
-          <folder name="examples">
-            <folder name="apps">
-              <folder name="cli">
-                <file name="cli_uart.cpp" uri="studio:/sdk/util/third_party/openthread/examples/apps/cli/cli_uart.cpp"/>
-              </folder>
-            </folder>
-            <folder name="platforms">
-              <folder name="utils">
-                <file name="code_utils.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/code_utils.h"/>
-                <file name="link_metrics.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/link_metrics.h"/>
-                <file name="mac_frame.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/mac_frame.h"/>
-                <file name="logging_rtt.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/logging_rtt.h"/>
-                <file name="settings.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/settings.h"/>
-                <file name="uart.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart.h"/>
-                <file name="uart_rtt.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart_rtt.h"/>
-                <file name="debug_uart.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/debug_uart.c"/>
-                <file name="link_metrics.cpp" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/link_metrics.cpp"/>
-                <file name="mac_frame.cpp" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/mac_frame.cpp"/>
-                <file name="settings_ram.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/settings_ram.c"/>
-                <file name="uart_rtt.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart_rtt.c"/>
+          <folder name="include">
+            <folder name="openthread">
+              <folder name="platform">
+                <file name="alarm-micro.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/alarm-micro.h"/>
+                <file name="alarm-milli.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/alarm-milli.h"/>
+                <file name="ble.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/ble.h"/>
+                <file name="border_routing.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/border_routing.h"/>
+                <file name="crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/crypto.h"/>
+                <file name="diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/diag.h"/>
+                <file name="dns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dns.h"/>
+                <file name="dnssd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dnssd.h"/>
+                <file name="dso_transport.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dso_transport.h"/>
+                <file name="entropy.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/entropy.h"/>
+                <file name="flash.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/flash.h"/>
+                <file name="infra_if.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/infra_if.h"/>
+                <file name="memory.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/memory.h"/>
+                <file name="misc.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/misc.h"/>
+                <file name="multipan.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/multipan.h"/>
+                <file name="logging.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/logging.h"/>
+                <file name="mdns_socket.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/mdns_socket.h"/>
+                <file name="otns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/otns.h"/>
+                <file name="radio.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/radio.h"/>
+                <file name="time.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/time.h"/>
+                <file name="udp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/udp.h"/>
+                <file name="spi-slave.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/spi-slave.h"/>
+                <file name="settings.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/settings.h"/>
+                <file name="messagepool.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/messagepool.h"/>
+                <file name="toolchain.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/toolchain.h"/>
+                <file name="trel.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/trel.h"/>
+                <file name="debug_uart.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/debug_uart.h"/>
               </folder>
-              <file name="openthread-system.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/openthread-system.h"/>
+              <file name="backbone_router.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/backbone_router.h"/>
+              <file name="backbone_router_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/backbone_router_ftd.h"/>
+              <file name="ble_secure.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ble_secure.h"/>
+              <file name="border_agent.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_agent.h"/>
+              <file name="border_router.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_router.h"/>
+              <file name="border_routing.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_routing.h"/>
+              <file name="channel_manager.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/channel_manager.h"/>
+              <file name="channel_monitor.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/channel_monitor.h"/>
+              <file name="child_supervision.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/child_supervision.h"/>
+              <file name="cli.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/cli.h"/>
+              <file name="coap_secure.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/coap_secure.h"/>
+              <file name="coap.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/coap.h"/>
+              <file name="commissioner.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/commissioner.h"/>
+              <file name="config.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/config.h"/>
+              <file name="crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/crypto.h"/>
+              <file name="dataset.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset.h"/>
+              <file name="dataset_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset_ftd.h"/>
+              <file name="dataset_updater.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset_updater.h"/>
+              <file name="diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/diag.h"/>
+              <file name="dns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dns.h"/>
+              <file name="dns_client.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dns_client.h"/>
+              <file name="dnssd_server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dnssd_server.h"/>
+              <file name="error.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/error.h"/>
+              <file name="heap.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/heap.h"/>
+              <file name="history_tracker.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/history_tracker.h"/>
+              <file name="icmp6.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/icmp6.h"/>
+              <file name="instance.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/instance.h"/>
+              <file name="ip6.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ip6.h"/>
+              <file name="jam_detection.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/jam_detection.h"/>
+              <file name="joiner.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/joiner.h"/>
+              <file name="link.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link.h"/>
+              <file name="link_metrics.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link_metrics.h"/>
+              <file name="link_raw.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link_raw.h"/>
+              <file name="logging.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/logging.h"/>
+              <file name="mdns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/mdns.h"/>
+              <file name="mesh_diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/mesh_diag.h"/>
+              <file name="message.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/message.h"/>
+              <file name="multi_radio.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/multi_radio.h"/>
+              <file name="nat64.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/nat64.h"/>
+              <file name="ncp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ncp.h"/>
+              <file name="netdata.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdata.h"/>
+              <file name="netdata_publisher.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdata_publisher.h"/>
+              <file name="netdiag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdiag.h"/>
+              <file name="network_time.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/network_time.h"/>
+              <file name="ping_sender.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ping_sender.h"/>
+              <file name="radio_stats.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/radio_stats.h"/>
+              <file name="random_crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/random_crypto.h"/>
+              <file name="random_noncrypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/random_noncrypto.h"/>
+              <file name="server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/server.h"/>
+              <file name="sntp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/sntp.h"/>
+              <file name="srp_client.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_client.h"/>
+              <file name="srp_client_buffers.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_client_buffers.h"/>
+              <file name="srp_server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_server.h"/>
+              <file name="tasklet.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tasklet.h"/>
+              <file name="tcat.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcat.h"/>
+              <file name="tcp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcp.h"/>
+              <file name="tcp_ext.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcp_ext.h"/>
+              <file name="thread.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/thread.h"/>
+              <file name="thread_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/thread_ftd.h"/>
+              <file name="trel.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/trel.h"/>
+              <file name="udp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/udp.h"/>
+              <file name="verhoeff_checksum.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/verhoeff_checksum.h"/>
             </folder>
           </folder>
           <folder name="src">
-            <folder name="cli">
-              <file name="cli.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli.cpp"/>
-              <file name="cli_bbr.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_bbr.cpp"/>
-              <file name="cli_br.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_br.cpp"/>
-              <file name="cli_coap.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_coap.cpp"/>
-              <file name="cli_coap_secure.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_coap_secure.cpp"/>
-              <file name="cli_commissioner.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_commissioner.cpp"/>
-              <file name="cli_dataset.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_dataset.cpp"/>
-              <file name="cli_dns.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_dns.cpp"/>
-              <file name="cli_history.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_history.cpp"/>
-              <file name="cli_joiner.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_joiner.cpp"/>
-              <file name="cli_link_metrics.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_link_metrics.cpp"/>
-              <file name="cli_mac_filter.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_mac_filter.cpp"/>
-              <file name="cli_mdns.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_mdns.cpp"/>
-              <file name="cli_network_data.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_network_data.cpp"/>
-              <file name="cli_ping.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_ping.cpp"/>
-              <file name="cli_srp_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_srp_client.cpp"/>
-              <file name="cli_srp_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_srp_server.cpp"/>
-              <file name="cli_tcat.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_tcat.cpp"/>
-              <file name="cli_tcp.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_tcp.cpp"/>
-              <file name="cli_udp.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_udp.cpp"/>
-              <file name="cli_utils.cpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_utils.cpp"/>
-              <file name="cli.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli.hpp"/>
-              <file name="cli_bbr.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_bbr.hpp"/>
-              <file name="cli_br.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_br.hpp"/>
-              <file name="cli_coap.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_coap.hpp"/>
-              <file name="cli_coap_secure.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_coap_secure.hpp"/>
-              <file name="cli_commissioner.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_commissioner.hpp"/>
-              <file name="cli_config.h" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_config.h"/>
-              <file name="cli_dataset.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_dataset.hpp"/>
-              <file name="cli_dns.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_dns.hpp"/>
-              <file name="cli_history.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_history.hpp"/>
-              <file name="cli_joiner.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_joiner.hpp"/>
-              <file name="cli_link_metrics.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_link_metrics.hpp"/>
-              <file name="cli_mac_filter.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_mac_filter.hpp"/>
-              <file name="cli_mdns.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_mdns.hpp"/>
-              <file name="cli_network_data.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_network_data.hpp"/>
-              <file name="cli_ping.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_ping.hpp"/>
-              <file name="cli_srp_client.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_srp_client.hpp"/>
-              <file name="cli_srp_server.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_srp_server.hpp"/>
-              <file name="cli_tcat.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_tcat.hpp"/>
-              <file name="cli_tcp.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_tcp.hpp"/>
-              <file name="cli_udp.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_udp.hpp"/>
-              <file name="cli_utils.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/cli_utils.hpp"/>
-              <file name="x509_cert_key.hpp" uri="studio:/sdk/util/third_party/openthread/src/cli/x509_cert_key.hpp"/>
-            </folder>
             <folder name="core">
               <folder name="backbone_router">
                 <file name="backbone_tmf.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/backbone_tmf.hpp"/>
@@ -2681,26 +2707,15 @@
                 <file name="bbr_manager.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/bbr_manager.hpp"/>
                 <file name="multicast_listeners_table.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.hpp"/>
                 <file name="ndproxy_table.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/ndproxy_table.hpp"/>
-                <file name="backbone_tmf.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/backbone_tmf.cpp"/>
-                <file name="bbr_leader.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/bbr_leader.cpp"/>
-                <file name="bbr_local.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/bbr_local.cpp"/>
-                <file name="bbr_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/bbr_manager.cpp"/>
-                <file name="multicast_listeners_table.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.cpp"/>
-                <file name="ndproxy_table.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/backbone_router/ndproxy_table.cpp"/>
               </folder>
               <folder name="border_router">
                 <file name="infra_if.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/border_router/infra_if.hpp"/>
                 <file name="routing_manager.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/border_router/routing_manager.hpp"/>
-                <file name="infra_if.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/border_router/infra_if.cpp"/>
-                <file name="routing_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/border_router/routing_manager.cpp"/>
               </folder>
               <folder name="coap">
                 <file name="coap.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap.hpp"/>
                 <file name="coap_message.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap_message.hpp"/>
                 <file name="coap_secure.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap_secure.hpp"/>
-                <file name="coap.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap.cpp"/>
-                <file name="coap_message.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap_message.cpp"/>
-                <file name="coap_secure.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/coap/coap_secure.cpp"/>
               </folder>
               <folder name="common">
                 <file name="appender.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/appender.hpp"/>
@@ -2757,30 +2772,6 @@
                 <file name="trickle_timer.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/trickle_timer.hpp"/>
                 <file name="type_traits.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/type_traits.hpp"/>
                 <file name="uptime.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/uptime.hpp"/>
-                <file name="binary_search.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/binary_search.cpp"/>
-                <file name="error.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/error.cpp"/>
-                <file name="frame_builder.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/frame_builder.cpp"/>
-                <file name="log.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/log.cpp"/>
-                <file name="random.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/random.cpp"/>
-                <file name="string.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/string.cpp"/>
-                <file name="tasklet.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/tasklet.cpp"/>
-                <file name="timer.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/timer.cpp"/>
-                <file name="uptime.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/uptime.cpp"/>
-                <file name="appender.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/appender.cpp"/>
-                <file name="crc16.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/crc16.cpp"/>
-                <file name="data.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/data.cpp"/>
-                <file name="frame_data.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/frame_data.cpp"/>
-                <file name="heap.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/heap.cpp"/>
-                <file name="heap_data.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/heap_data.cpp"/>
-                <file name="heap_string.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/heap_string.cpp"/>
-                <file name="message.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/message.cpp"/>
-                <file name="notifier.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/notifier.cpp"/>
-                <file name="offset_range.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/offset_range.cpp"/>
-                <file name="preference.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/preference.cpp"/>
-                <file name="settings.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/settings.cpp"/>
-                <file name="time_ticker.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/time_ticker.cpp"/>
-                <file name="tlvs.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/tlvs.cpp"/>
-                <file name="trickle_timer.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/common/trickle_timer.cpp"/>
               </folder>
               <folder name="config">
                 <file name="announce_sender.h" uri="studio:/sdk/util/third_party/openthread/src/core/config/announce_sender.h"/>
@@ -2842,23 +2833,13 @@
                 <file name="mbedtls.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/mbedtls.hpp"/>
                 <file name="sha256.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/sha256.hpp"/>
                 <file name="storage.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/storage.hpp"/>
-                <file name="aes_ccm.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/aes_ccm.cpp"/>
-                <file name="aes_ecb.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/aes_ecb.cpp"/>
-                <file name="crypto_platform.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/crypto_platform.cpp"/>
-                <file name="storage.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/storage.cpp"/>
-                <file name="hkdf_sha256.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/hkdf_sha256.cpp"/>
-                <file name="hmac_sha256.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/hmac_sha256.cpp"/>
-                <file name="mbedtls.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/mbedtls.cpp"/>
-                <file name="sha256.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/crypto/sha256.cpp"/>
               </folder>
               <folder name="diags">
                 <file name="factory_diags.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/diags/factory_diags.hpp"/>
-                <file name="factory_diags.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/diags/factory_diags.cpp"/>
               </folder>
               <folder name="instance">
                 <file name="extension.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/instance/extension.hpp"/>
                 <file name="instance.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/instance/instance.hpp"/>
-                <file name="instance.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/instance/instance.cpp"/>
               </folder>
               <folder name="mac">
                 <file name="channel_mask.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/channel_mask.hpp"/>
@@ -2873,21 +2854,6 @@
                 <file name="mac_types.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_types.hpp"/>
                 <file name="sub_mac.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/sub_mac.hpp"/>
                 <file name="wakeup_tx_scheduler.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.hpp"/>
-                <file name="link_raw.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/link_raw.cpp"/>
-                <file name="mac_frame.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_frame.cpp"/>
-                <file name="mac_header_ie.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_header_ie.cpp"/>
-                <file name="mac_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_types.cpp"/>
-                <file name="sub_mac.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/sub_mac.cpp"/>
-                <file name="sub_mac_callbacks.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/sub_mac_callbacks.cpp"/>
-                <file name="sub_mac_csl_receiver.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/sub_mac_csl_receiver.cpp"/>
-                <file name="channel_mask.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/channel_mask.cpp"/>
-                <file name="data_poll_handler.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/data_poll_handler.cpp"/>
-                <file name="data_poll_sender.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/data_poll_sender.cpp"/>
-                <file name="mac.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac.cpp"/>
-                <file name="mac_filter.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_filter.cpp"/>
-                <file name="mac_links.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/mac_links.cpp"/>
-                <file name="sub_mac_wed.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/sub_mac_wed.cpp"/>
-                <file name="wakeup_tx_scheduler.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.cpp"/>
               </folder>
               <folder name="meshcop">
                 <file name="announce_begin_client.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/announce_begin_client.hpp"/>
@@ -2908,25 +2874,6 @@
                 <file name="secure_transport.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/secure_transport.hpp"/>
                 <file name="tcat_agent.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/tcat_agent.hpp"/>
                 <file name="timestamp.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/timestamp.hpp"/>
-                <file name="announce_begin_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/announce_begin_client.cpp"/>
-                <file name="border_agent.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/border_agent.cpp"/>
-                <file name="commissioner.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/commissioner.cpp"/>
-                <file name="dataset.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/dataset.cpp"/>
-                <file name="dataset_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/dataset_manager.cpp"/>
-                <file name="dataset_manager_ftd.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/dataset_manager_ftd.cpp"/>
-                <file name="dataset_updater.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/dataset_updater.cpp"/>
-                <file name="energy_scan_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/energy_scan_client.cpp"/>
-                <file name="extended_panid.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/extended_panid.cpp"/>
-                <file name="joiner.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/joiner.cpp"/>
-                <file name="joiner_router.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/joiner_router.cpp"/>
-                <file name="meshcop.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/meshcop.cpp"/>
-                <file name="meshcop_leader.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/meshcop_leader.cpp"/>
-                <file name="meshcop_tlvs.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/meshcop_tlvs.cpp"/>
-                <file name="network_name.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/network_name.cpp"/>
-                <file name="panid_query_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/panid_query_client.cpp"/>
-                <file name="secure_transport.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/secure_transport.cpp"/>
-                <file name="tcat_agent.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/tcat_agent.cpp"/>
-                <file name="timestamp.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/meshcop/timestamp.cpp"/>
               </folder>
               <folder name="net">
                 <file name="checksum.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/checksum.hpp"/>
@@ -2959,35 +2906,6 @@
                 <file name="tcp6_ext.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/tcp6_ext.hpp"/>
                 <file name="tcp6.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/tcp6.hpp"/>
                 <file name="udp6.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/udp6.hpp"/>
-                <file name="checksum.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/checksum.cpp"/>
-                <file name="dhcp6_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dhcp6_client.cpp"/>
-                <file name="dhcp6_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dhcp6_server.cpp"/>
-                <file name="dns_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dns_client.cpp"/>
-                <file name="dns_dso.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dns_dso.cpp"/>
-                <file name="dns_platform.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dns_platform.cpp"/>
-                <file name="dns_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dns_types.cpp"/>
-                <file name="dnssd.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dnssd.cpp"/>
-                <file name="dnssd_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/dnssd_server.cpp"/>
-                <file name="icmp6.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/icmp6.cpp"/>
-                <file name="ip4_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip4_types.cpp"/>
-                <file name="ip6.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip6.cpp"/>
-                <file name="ip6_address.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip6_address.cpp"/>
-                <file name="ip6_filter.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip6_filter.cpp"/>
-                <file name="ip6_headers.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip6_headers.cpp"/>
-                <file name="ip6_mpl.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/ip6_mpl.cpp"/>
-                <file name="mdns.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/mdns.cpp"/>
-                <file name="nat64_translator.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/nat64_translator.cpp"/>
-                <file name="nd6.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/nd6.cpp"/>
-                <file name="nd_agent.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/nd_agent.cpp"/>
-                <file name="netif.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/netif.cpp"/>
-                <file name="sntp_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/sntp_client.cpp"/>
-                <file name="socket.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/socket.cpp"/>
-                <file name="srp_advertising_proxy.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/srp_advertising_proxy.cpp"/>
-                <file name="srp_client.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/srp_client.cpp"/>
-                <file name="srp_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/srp_server.cpp"/>
-                <file name="tcp6.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/tcp6.cpp"/>
-                <file name="tcp6_ext.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/tcp6_ext.cpp"/>
-                <file name="udp6.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/net/udp6.cpp"/>
               </folder>
               <folder name="radio">
                 <file name="ble_secure.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/ble_secure.hpp"/>
@@ -2996,13 +2914,6 @@
                 <file name="trel_interface.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_interface.hpp"/>
                 <file name="trel_link.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_link.hpp"/>
                 <file name="trel_packet.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_packet.hpp"/>
-                <file name="radio.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/radio.cpp"/>
-                <file name="radio_callbacks.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/radio_callbacks.cpp"/>
-                <file name="radio_platform.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/radio_platform.cpp"/>
-                <file name="ble_secure.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/ble_secure.cpp"/>
-                <file name="trel_interface.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_interface.cpp"/>
-                <file name="trel_link.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_link.cpp"/>
-                <file name="trel_packet.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/radio/trel_packet.cpp"/>
               </folder>
               <folder name="thread">
                 <file name="address_resolver.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/address_resolver.hpp"/>
@@ -3055,53 +2966,6 @@
                 <file name="tmf.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/tmf.hpp"/>
                 <file name="uri_paths.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/uri_paths.hpp"/>
                 <file name="version.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/version.hpp"/>
-                <file name="link_quality.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/link_quality.cpp"/>
-                <file name="address_resolver.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/address_resolver.cpp"/>
-                <file name="announce_begin_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/announce_begin_server.cpp"/>
-                <file name="announce_sender.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/announce_sender.cpp"/>
-                <file name="anycast_locator.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/anycast_locator.cpp"/>
-                <file name="child.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/child.cpp"/>
-                <file name="child_supervision.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/child_supervision.cpp"/>
-                <file name="child_table.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/child_table.cpp"/>
-                <file name="csl_tx_scheduler.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/csl_tx_scheduler.cpp"/>
-                <file name="discover_scanner.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/discover_scanner.cpp"/>
-                <file name="dua_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/dua_manager.cpp"/>
-                <file name="energy_scan_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/energy_scan_server.cpp"/>
-                <file name="indirect_sender.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/indirect_sender.cpp"/>
-                <file name="key_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/key_manager.cpp"/>
-                <file name="link_metrics.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/link_metrics.cpp"/>
-                <file name="link_metrics_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/link_metrics_types.cpp"/>
-                <file name="lowpan.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/lowpan.cpp"/>
-                <file name="mesh_forwarder.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mesh_forwarder.cpp"/>
-                <file name="mesh_forwarder_ftd.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mesh_forwarder_ftd.cpp"/>
-                <file name="mesh_forwarder_mtd.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mesh_forwarder_mtd.cpp"/>
-                <file name="mle.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mle.cpp"/>
-                <file name="mle_router.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mle_router.cpp"/>
-                <file name="mle_tlvs.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mle_tlvs.cpp"/>
-                <file name="mle_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mle_types.cpp"/>
-                <file name="mlr_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/mlr_manager.cpp"/>
-                <file name="neighbor.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/neighbor.cpp"/>
-                <file name="neighbor_table.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/neighbor_table.cpp"/>
-                <file name="network_data.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data.cpp"/>
-                <file name="network_data_leader.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_leader.cpp"/>
-                <file name="network_data_leader_ftd.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_leader_ftd.cpp"/>
-                <file name="network_data_local.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_local.cpp"/>
-                <file name="network_data_notifier.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_notifier.cpp"/>
-                <file name="network_data_publisher.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_publisher.cpp"/>
-                <file name="network_data_service.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_service.cpp"/>
-                <file name="network_data_tlvs.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_tlvs.cpp"/>
-                <file name="network_data_types.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_data_types.cpp"/>
-                <file name="network_diagnostic.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_diagnostic.cpp"/>
-                <file name="network_diagnostic_tlvs.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/network_diagnostic_tlvs.cpp"/>
-                <file name="panid_query_server.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/panid_query_server.cpp"/>
-                <file name="radio_selector.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/radio_selector.cpp"/>
-                <file name="router.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/router.cpp"/>
-                <file name="router_table.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/router_table.cpp"/>
-                <file name="src_match_controller.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/src_match_controller.cpp"/>
-                <file name="thread_netif.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/thread_netif.cpp"/>
-                <file name="time_sync_service.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/time_sync_service.cpp"/>
-                <file name="tmf.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/tmf.cpp"/>
-                <file name="uri_paths.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/thread/uri_paths.cpp"/>
               </folder>
               <folder name="utils">
                 <file name="channel_manager.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/channel_manager.hpp"/>
@@ -3120,80 +2984,6 @@
                 <file name="srp_client_buffers.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/srp_client_buffers.hpp"/>
                 <file name="static_counter.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/static_counter.hpp"/>
                 <file name="verhoeff_checksum.hpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/verhoeff_checksum.hpp"/>
-                <file name="parse_cmdline.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/parse_cmdline.cpp"/>
-                <file name="power_calibration.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/power_calibration.cpp"/>
-                <file name="channel_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/channel_manager.cpp"/>
-                <file name="channel_monitor.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/channel_monitor.cpp"/>
-                <file name="flash.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/flash.cpp"/>
-                <file name="heap.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/heap.cpp"/>
-                <file name="history_tracker.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/history_tracker.cpp"/>
-                <file name="jam_detector.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/jam_detector.cpp"/>
-                <file name="link_metrics_manager.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/link_metrics_manager.cpp"/>
-                <file name="mesh_diag.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/mesh_diag.cpp"/>
-                <file name="otns.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/otns.cpp"/>
-                <file name="ping_sender.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/ping_sender.cpp"/>
-                <file name="slaac_address.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/slaac_address.cpp"/>
-                <file name="srp_client_buffers.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/srp_client_buffers.cpp"/>
-                <file name="verhoeff_checksum.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/utils/verhoeff_checksum.cpp"/>
-              </folder>
-              <folder name="api">
-                <file name="diags_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/diags_api.cpp"/>
-                <file name="error_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/error_api.cpp"/>
-                <file name="instance_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/instance_api.cpp"/>
-                <file name="link_raw_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/link_raw_api.cpp"/>
-                <file name="logging_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/logging_api.cpp"/>
-                <file name="random_noncrypto_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/random_noncrypto_api.cpp"/>
-                <file name="tasklet_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/tasklet_api.cpp"/>
-                <file name="backbone_router_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/backbone_router_api.cpp"/>
-                <file name="backbone_router_ftd_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/backbone_router_ftd_api.cpp"/>
-                <file name="ble_secure_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/ble_secure_api.cpp"/>
-                <file name="border_agent_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/border_agent_api.cpp"/>
-                <file name="border_router_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/border_router_api.cpp"/>
-                <file name="border_routing_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/border_routing_api.cpp"/>
-                <file name="channel_manager_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/channel_manager_api.cpp"/>
-                <file name="channel_monitor_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/channel_monitor_api.cpp"/>
-                <file name="child_supervision_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/child_supervision_api.cpp"/>
-                <file name="coap_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/coap_api.cpp"/>
-                <file name="coap_secure_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/coap_secure_api.cpp"/>
-                <file name="commissioner_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/commissioner_api.cpp"/>
-                <file name="crypto_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/crypto_api.cpp"/>
-                <file name="dataset_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/dataset_api.cpp"/>
-                <file name="dataset_ftd_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/dataset_ftd_api.cpp"/>
-                <file name="dataset_updater_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/dataset_updater_api.cpp"/>
-                <file name="dns_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/dns_api.cpp"/>
-                <file name="dns_server_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/dns_server_api.cpp"/>
-                <file name="heap_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/heap_api.cpp"/>
-                <file name="history_tracker_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/history_tracker_api.cpp"/>
-                <file name="icmp6_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/icmp6_api.cpp"/>
-                <file name="ip6_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/ip6_api.cpp"/>
-                <file name="jam_detection_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/jam_detection_api.cpp"/>
-                <file name="joiner_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/joiner_api.cpp"/>
-                <file name="link_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/link_api.cpp"/>
-                <file name="link_metrics_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/link_metrics_api.cpp"/>
-                <file name="mesh_diag_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/mesh_diag_api.cpp"/>
-                <file name="message_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/message_api.cpp"/>
-                <file name="mdns_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/mdns_api.cpp"/>
-                <file name="multi_radio_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/multi_radio_api.cpp"/>
-                <file name="nat64_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/nat64_api.cpp"/>
-                <file name="netdata_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/netdata_api.cpp"/>
-                <file name="netdata_publisher_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/netdata_publisher_api.cpp"/>
-                <file name="netdiag_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/netdiag_api.cpp"/>
-                <file name="network_time_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/network_time_api.cpp"/>
-                <file name="ping_sender_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/ping_sender_api.cpp"/>
-                <file name="radio_stats_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/radio_stats_api.cpp"/>
-                <file name="random_crypto_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/random_crypto_api.cpp"/>
-                <file name="server_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/server_api.cpp"/>
-                <file name="sntp_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/sntp_api.cpp"/>
-                <file name="srp_client_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/srp_client_api.cpp"/>
-                <file name="srp_client_buffers_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/srp_client_buffers_api.cpp"/>
-                <file name="srp_server_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/srp_server_api.cpp"/>
-                <file name="tcp_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/tcp_api.cpp"/>
-                <file name="tcp_ext_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/tcp_ext_api.cpp"/>
-                <file name="thread_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/thread_api.cpp"/>
-                <file name="thread_ftd_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/thread_ftd_api.cpp"/>
-                <file name="trel_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/trel_api.cpp"/>
-                <file name="udp_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/udp_api.cpp"/>
-                <file name="verhoeff_checksum_api.cpp" uri="studio:/sdk/util/third_party/openthread/src/core/api/verhoeff_checksum_api.cpp"/>
               </folder>
               <file name="openthread-core-config.h" uri="studio:/sdk/util/third_party/openthread/src/core/openthread-core-config.h"/>
             </folder>
@@ -3203,99 +2993,23 @@
               </folder>
             </folder>
           </folder>
-          <folder name="include">
-            <folder name="openthread">
-              <folder name="platform">
-                <file name="alarm-micro.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/alarm-micro.h"/>
-                <file name="alarm-milli.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/alarm-milli.h"/>
-                <file name="ble.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/ble.h"/>
-                <file name="border_routing.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/border_routing.h"/>
-                <file name="crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/crypto.h"/>
-                <file name="diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/diag.h"/>
-                <file name="dns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dns.h"/>
-                <file name="dnssd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dnssd.h"/>
-                <file name="dso_transport.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/dso_transport.h"/>
-                <file name="entropy.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/entropy.h"/>
-                <file name="flash.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/flash.h"/>
-                <file name="infra_if.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/infra_if.h"/>
-                <file name="memory.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/memory.h"/>
-                <file name="misc.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/misc.h"/>
-                <file name="multipan.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/multipan.h"/>
-                <file name="logging.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/logging.h"/>
-                <file name="mdns_socket.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/mdns_socket.h"/>
-                <file name="otns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/otns.h"/>
-                <file name="radio.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/radio.h"/>
-                <file name="time.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/time.h"/>
-                <file name="udp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/udp.h"/>
-                <file name="spi-slave.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/spi-slave.h"/>
-                <file name="settings.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/settings.h"/>
-                <file name="messagepool.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/messagepool.h"/>
-                <file name="toolchain.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/toolchain.h"/>
-                <file name="trel.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/trel.h"/>
-                <file name="debug_uart.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/platform/debug_uart.h"/>
+          <folder name="examples">
+            <folder name="platforms">
+              <folder name="utils">
+                <file name="code_utils.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/code_utils.h"/>
+                <file name="link_metrics.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/link_metrics.h"/>
+                <file name="mac_frame.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/mac_frame.h"/>
+                <file name="logging_rtt.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/logging_rtt.h"/>
+                <file name="settings.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/settings.h"/>
+                <file name="uart.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart.h"/>
+                <file name="uart_rtt.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart_rtt.h"/>
+                <file name="debug_uart.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/debug_uart.c"/>
+                <file name="link_metrics.cpp" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/link_metrics.cpp"/>
+                <file name="mac_frame.cpp" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/mac_frame.cpp"/>
+                <file name="settings_ram.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/settings_ram.c"/>
+                <file name="uart_rtt.c" uri="studio:/sdk/util/third_party/openthread/examples/platforms/utils/uart_rtt.c"/>
               </folder>
-              <file name="backbone_router.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/backbone_router.h"/>
-              <file name="backbone_router_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/backbone_router_ftd.h"/>
-              <file name="ble_secure.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ble_secure.h"/>
-              <file name="border_agent.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_agent.h"/>
-              <file name="border_router.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_router.h"/>
-              <file name="border_routing.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/border_routing.h"/>
-              <file name="channel_manager.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/channel_manager.h"/>
-              <file name="channel_monitor.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/channel_monitor.h"/>
-              <file name="child_supervision.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/child_supervision.h"/>
-              <file name="cli.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/cli.h"/>
-              <file name="coap_secure.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/coap_secure.h"/>
-              <file name="coap.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/coap.h"/>
-              <file name="commissioner.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/commissioner.h"/>
-              <file name="config.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/config.h"/>
-              <file name="crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/crypto.h"/>
-              <file name="dataset.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset.h"/>
-              <file name="dataset_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset_ftd.h"/>
-              <file name="dataset_updater.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dataset_updater.h"/>
-              <file name="diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/diag.h"/>
-              <file name="dns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dns.h"/>
-              <file name="dns_client.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dns_client.h"/>
-              <file name="dnssd_server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/dnssd_server.h"/>
-              <file name="error.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/error.h"/>
-              <file name="heap.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/heap.h"/>
-              <file name="history_tracker.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/history_tracker.h"/>
-              <file name="icmp6.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/icmp6.h"/>
-              <file name="instance.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/instance.h"/>
-              <file name="ip6.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ip6.h"/>
-              <file name="jam_detection.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/jam_detection.h"/>
-              <file name="joiner.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/joiner.h"/>
-              <file name="link.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link.h"/>
-              <file name="link_metrics.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link_metrics.h"/>
-              <file name="link_raw.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/link_raw.h"/>
-              <file name="logging.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/logging.h"/>
-              <file name="mdns.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/mdns.h"/>
-              <file name="mesh_diag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/mesh_diag.h"/>
-              <file name="message.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/message.h"/>
-              <file name="multi_radio.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/multi_radio.h"/>
-              <file name="nat64.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/nat64.h"/>
-              <file name="ncp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ncp.h"/>
-              <file name="netdata.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdata.h"/>
-              <file name="netdata_publisher.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdata_publisher.h"/>
-              <file name="netdiag.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/netdiag.h"/>
-              <file name="network_time.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/network_time.h"/>
-              <file name="ping_sender.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/ping_sender.h"/>
-              <file name="radio_stats.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/radio_stats.h"/>
-              <file name="random_crypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/random_crypto.h"/>
-              <file name="random_noncrypto.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/random_noncrypto.h"/>
-              <file name="server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/server.h"/>
-              <file name="sntp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/sntp.h"/>
-              <file name="srp_client.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_client.h"/>
-              <file name="srp_client_buffers.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_client_buffers.h"/>
-              <file name="srp_server.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/srp_server.h"/>
-              <file name="tasklet.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tasklet.h"/>
-              <file name="tcat.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcat.h"/>
-              <file name="tcp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcp.h"/>
-              <file name="tcp_ext.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/tcp_ext.h"/>
-              <file name="thread.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/thread.h"/>
-              <file name="thread_ftd.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/thread_ftd.h"/>
-              <file name="trel.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/trel.h"/>
-              <file name="udp.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/udp.h"/>
-              <file name="verhoeff_checksum.h" uri="studio:/sdk/util/third_party/openthread/include/openthread/verhoeff_checksum.h"/>
+              <file name="openthread-system.h" uri="studio:/sdk/util/third_party/openthread/examples/platforms/openthread-system.h"/>
             </folder>
           </folder>
           <folder name="third_party">
@@ -3303,7 +3017,6 @@
               <folder name="bsdtcp">
                 <folder name="cc">
                   <file name="cc_module.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/cc/cc_module.h"/>
-                  <file name="cc_newreno.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/cc/cc_newreno.c"/>
                 </folder>
                 <folder name="sys">
                   <file name="queue.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/sys/queue.h"/>
@@ -3320,23 +3033,11 @@
                 <file name="tcp_timer.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.h"/>
                 <file name="tcp_var.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_var.h"/>
                 <file name="types.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/types.h"/>
-                <file name="tcp_fastopen.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_fastopen.c"/>
-                <file name="tcp_input.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_input.c"/>
-                <file name="tcp_output.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_output.c"/>
-                <file name="tcp_reass.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_reass.c"/>
-                <file name="tcp_sack.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_sack.c"/>
-                <file name="tcp_subr.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_subr.c"/>
-                <file name="tcp_timer.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.c"/>
-                <file name="tcp_timewait.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timewait.c"/>
-                <file name="tcp_usrreq.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_usrreq.c"/>
               </folder>
               <folder name="lib">
                 <file name="bitmap.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/bitmap.h"/>
                 <file name="cbuf.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/cbuf.h"/>
                 <file name="lbuf.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/lbuf.h"/>
-                <file name="bitmap.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/bitmap.c"/>
-                <file name="cbuf.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/cbuf.c"/>
-                <file name="lbuf.c" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/lib/lbuf.c"/>
               </folder>
               <file name="tcplp.h" uri="studio:/sdk/util/third_party/openthread/third_party/tcplp/tcplp.h"/>
             </folder>
@@ -3368,6 +3069,10 @@
   <excludedPath>simplicity_sdk_2024.12.2/protocol/bluetooth/api/sl_bt.xapi</excludedPath>
   <excludedPath>linker_options/ot-rtos-wrapper-options</excludedPath>
   <includePath uri="studio:/project/include"/>
+  <includePath uri="studio:/project/common/app"/>
+  <includePath uri="studio:/project/common/event_queue"/>
+  <includePath uri="studio:/project/common/hal"/>
+  <includePath uri="studio:/project/common/misc"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/include"/>
@@ -3426,6 +3131,8 @@
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/icd/server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/access-control-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/basic-information"/>
+  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/cluster-building-blocks"/>
+  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/color-control-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/descriptor"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/general-commissioning-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/general-diagnostics-server"/>
@@ -3433,16 +3140,14 @@
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/icd-management-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/identify-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/slc/inc"/>
+  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/level-control"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/network-commissioning"/>
+  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/on-off-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/controller"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/ota-requestor"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/power-source-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_support/provision"/>
   <includePath uri="studio:/sdk/extension/matter_extension/slc/component/sdk-content/simplicity-sdk/util/third_party/segger/systemview/SEGGER"/>
-  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell"/>
-  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands"/>
-  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/include"/>
-  <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/shell/icd"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/software-diagnostics-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/app/clusters/thread-network-diagnostics-server"/>
   <includePath uri="studio:/sdk/extension/matter_extension/third_party/matter_sdk/src/tracing"/>
@@ -3489,8 +3194,6 @@
   <includePath uri="studio:/sdk/platform/service/mpu/inc"/>
   <includePath uri="studio:/sdk/platform/emdrv/nvm3/inc"/>
   <includePath uri="studio:/sdk/platform/emdrv/nvm3/config"/>
-  <includePath uri="studio:/sdk/util/third_party/openthread/src"/>
-  <includePath uri="studio:/sdk/util/third_party/openthread/src/cli"/>
   <includePath uri="studio:/sdk/protocol/openthread/platform-abstraction/efr32"/>
   <includePath uri="studio:/sdk/util/third_party/openthread/include"/>
   <includePath uri="studio:/sdk/util/third_party/openthread/include/openthread"/>
@@ -3527,9 +3230,11 @@
   <includePath uri="studio:/sdk/platform/security/sl_component/sli_psec_osal/inc"/>
   <includePath uri="studio:/sdk/platform/emdrv/uartdrv/inc"/>
   <includePath uri="studio:/sdk/platform/service/udelay/inc"/>
+  <macroDefinition name="AOK02_MATTER_PROJECT" value="1"/>
   <macroDefinition name="CHIP_CRYPTO_PLATFORM" value="1"/>
   <macroDefinition name="NVM3_DEFAULT_MAX_OBJECT_SIZE" value="4092"/>
   <macroDefinition name="NVM3_DEFAULT_NVM_SIZE" value="40960"/>
+  <macroDefinition name="SL_OPENTHREAD_APPLICATION_CONFIG_FILE" value="&quot;sl_openthread_application_config.h&quot;"/>
   <macroDefinition name="_WANT_REENT_SMALL" value="1"/>
   <macroDefinition name="CHIP_ADDRESS_RESOLVE_IMPL_INCLUDE_HEADER" value="&lt;lib/address_resolve/AddressResolve_DefaultImpl.h>"/>
   <macroDefinition name="CHIP_HAVE_CONFIG_H" value="1"/>
@@ -3548,15 +3253,15 @@
   <macroDefinition name="NON_SPEC_COMPLIANT_OTA_ACTION_DELAY_FLOOR" value="-1"/>
   <macroDefinition name="SILABS_OTA_ENABLED"/>
   <macroDefinition name="RTT_USE_ASM" value="0"/>
-  <macroDefinition name="ENABLE_CHIP_SHELL"/>
-  <macroDefinition name="OPENTHREAD_CONFIG_CLI_TRANSPORT" value="OT_CLI_TRANSPORT_CONSOLE"/>
-  <macroDefinition name="SL_MATTER_CLI_ARG_PARSER" value="1"/>
   <macroDefinition name="SL_MATTER_TEST_EVENT_TRIGGER_ENABLED"/>
-  <macroDefinition name="CHIP_DEVICE_CONFIG_THREAD_ENABLE_CLI" value="1"/>
+  <macroDefinition name="OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE" value="0"/>
+  <macroDefinition name="OPENTHREAD_CONFIG_TCP_ENABLE" value="0"/>
+  <macroDefinition name="SL_OPENTHREAD_CERT_LIB" value="1"/>
   <macroDefinition name="CONFIG_ENABLE_EUART"/>
   <macroDefinition name="EFR32MG24"/>
   <macroDefinition name="EFR32MG24A410F1536IM40"/>
   <macroDefinition name="SL_CODE_COMPONENT_SYSTEM" value="system"/>
+  <macroDefinition name="RADIOAES_BLE_RPA_MAX_KEYS" value="8"/>
   <macroDefinition name="SL_APP_PROPERTIES"/>
   <macroDefinition name="SL_CODE_COMPONENT_CLOCK_MANAGER" value="clock_manager"/>
   <macroDefinition name="configNUM_SDK_THREAD_LOCAL_STORAGE_POINTERS" value="2"/>
@@ -3571,12 +3276,13 @@
   <macroDefinition name="CMSIS_NVIC_VIRTUAL"/>
   <macroDefinition name="CMSIS_NVIC_VIRTUAL_HEADER_FILE" value="&quot;cmsis_nvic_virtual.h&quot;"/>
   <macroDefinition name="MBEDTLS_CONFIG_FILE" value="&lt;sl_mbedtls_config.h>"/>
+  <macroDefinition name="OPENTHREAD_CONFIG_DIAG_ENABLE" value="1"/>
   <macroDefinition name="OPENTHREAD_CORE_CONFIG_PLATFORM_CHECK_FILE" value="&quot;openthread-core-efr32-config-check.h&quot;"/>
   <macroDefinition name="OPENTHREAD_PROJECT_CORE_CONFIG_FILE" value="&quot;openthread-core-efr32-config.h&quot;"/>
   <macroDefinition name="SL_CODE_COMPONENT_OT_PLATFORM_ABSTRACTION" value="ot_platform_abstraction"/>
   <macroDefinition name="OPENTHREAD_CONFIG_FILE" value="&quot;sl_openthread_package_info.h&quot;"/>
   <macroDefinition name="OPENTHREAD_MTD" value="1"/>
-  <macroDefinition name="SL_OPENTHREAD_STACK_FEATURES_CONFIG_FILE" value="&quot;sl_openthread_features_config.h&quot;"/>
+  <macroDefinition name="SL_OPENTHREAD_STACK_FEATURES_CONFIG_FILE" value="&quot;sl_openthread_features_mtd_cert_config.h&quot;"/>
   <macroDefinition name="SL_CODE_COMPONENT_POWER_MANAGER" value="power_manager"/>
   <macroDefinition name="MBEDTLS_PSA_CRYPTO_CONFIG_FILE" value="&lt;psa_crypto_config.h>"/>
   <macroDefinition name="SL_RAIL_LIB_MULTIPROTOCOL_SUPPORT" value="1"/>
@@ -3584,7 +3290,6 @@
   <macroDefinition name="SL_CODE_COMPONENT_SE_MANAGER" value="se_manager"/>
   <macroDefinition name="CIRCULAR_QUEUE_USE_LOCAL_CONFIG_HEADER" value="1"/>
   <macroDefinition name="SL_CODE_COMPONENT_CORE" value="core"/>
-  <macroDefinition name="SL_OPENTHREAD_CUSTOM_CLI_ENABLE" value="1"/>
   <macroDefinition name="SL_CODE_COMPONENT_SLEEPTIMER" value="sleeptimer"/>
   <macroDefinition name="SL_CODE_COMPONENT_SLI_CRYPTO" value="sli_crypto"/>
   <macroDefinition name="SLI_RADIOAES_REQUIRES_MASKING"/>
@@ -3594,17 +3299,18 @@
   <libraryFile uri="studio:/sdk/extension/matter_extension/third_party/matter_support/provision/libs/libProvision_efr32mg24.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/bgcommon/lib/build/gcc/cortex-m33/bgcommon/release/libbgcommon.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/bgstack/ll/build/gcc/xg24/release/liblinklayer.a"/>
+  <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list.a"/>
+  <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_gatt_server.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/bgapi_protocol/api3/release/libbgapi_core.a"/>
-  <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list_stub.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libble_host.a"/>
-  <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb_stub.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi_stub_gatt_client.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/hal/release/libble_host_hal_series2.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/hci/release/libble_host_hci.a"/>
   <libraryFile uri="studio:/sdk/protocol/bluetooth/build/gcc/cortex-m33/ble_host/system/release/libble_system.a"/>
   <libraryFile name="stdc++"/>
+  <libraryFile uri="studio:/sdk/protocol/openthread/libs/libsl_ot_stack_mtd_efr32mg24_gcc.a"/>
   <libraryFile uri="studio:/sdk/protocol/openthread/libs/libsl_openthread_cm33_gcc.a"/>
   <libraryFile uri="studio:/sdk/platform/radio/rail_lib/autogen/librail_release/librail_multiprotocol_efr32xg24_gcc_release.a"/>
   <libraryFile name="gcc"/>
@@ -3616,17 +3322,15 @@
   <toolOption toolId="toolOption.uc.toolchain" optionId="toolOption.uc.toolchain.fpu" value="fpv5-sp"/>
   <toolOption toolId="toolOption.uc.toolchain" optionId="toolOption.uc.toolchain.float_abi" value="hard"/>
   <toolOption toolId="toolOption.uc.compiler" optionId="toolOption.uc.compiler.secure_code" value="true"/>
+  <toolOption toolId="toolOption.uc.linker" optionId="toolOption.uc.linker.misc">
+    <toolListOption value="@$project/linker_options/ot-rtos-wrapper-options"/>
+  </toolOption>
   <toolOption toolId="toolOption.uc.compiler" optionId="toolOption.uc.compiler.preinclude">
-    <toolListOption value="sl_openthread_ble_cli_config.h"/>
     <toolListOption value="sl_gcc_preinclude.h"/>
   </toolOption>
   <toolOption toolId="toolOption.uc.assembler" optionId="toolOption.uc.assembler.preinclude">
-    <toolListOption value="sl_openthread_ble_cli_config.h"/>
     <toolListOption value="sl_gcc_preinclude.h"/>
   </toolOption>
-  <toolOption toolId="toolOption.uc.linker" optionId="toolOption.uc.linker.misc">
-    <toolListOption value="@$project/linker_options/ot-rtos-wrapper-options"/>
-  </toolOption>
   <toolOption toolId="toolOption.uc.linker" optionId="toolOption.uc.linker.linkerScript" value="$project/autogen/linkerfile.ld"/>
   <toolOption toolId="toolOption.uc.compiler" optionId="toolOption.uc.compiler.function_sections" value="true"/>
   <toolOption toolId="toolOption.uc.compiler" optionId="toolOption.uc.compiler.data_sections" value="true"/>
@@ -3654,15 +3358,12 @@
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.cpp.linker.base" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.cpp.linker.floatingpoint.enable" value="true"/>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.toolchain.exe" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.toolchain.debug.level" value="com.silabs.ide.si32.gcc.cdt.managedbuild.toolchain.debug.level.default"/>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.assembler.base" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.assembler.preinclude">
-    <toolListOption value="sl_openthread_ble_cli_config.h"/>
     <toolListOption value="sl_gcc_preinclude.h"/>
   </toolOption>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.c.compiler.base" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.c.compiler.preinclude">
-    <toolListOption value="sl_openthread_ble_cli_config.h"/>
     <toolListOption value="sl_gcc_preinclude.h"/>
   </toolOption>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.cpp.compiler.base" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.cpp.compiler.preinclude">
-    <toolListOption value="sl_openthread_ble_cli_config.h"/>
     <toolListOption value="sl_gcc_preinclude.h"/>
   </toolOption>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.c.compiler.base" optionId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.c.compiler.misc.dialect" value="gnu.c.compiler.dialect.c18"/>
@@ -3713,7 +3414,6 @@
     <toolListOption value="-Werror=unused-function"/>
     <toolListOption value="-Werror=unused-label"/>
     <toolListOption value="-Werror=unused-variable"/>
-    <toolListOption value="-Wno-sign-compare"/>
     <toolListOption value="-fno-lto"/>
     <toolListOption value="--specs=nano.specs"/>
   </toolOption>
@@ -3731,7 +3431,6 @@
     <toolListOption value="-Werror=unused-function"/>
     <toolListOption value="-Werror=unused-label"/>
     <toolListOption value="-Werror=unused-variable"/>
-    <toolListOption value="-Wno-sign-compare"/>
     <toolListOption value="--specs=nano.specs"/>
   </toolOption>
   <toolOption toolId="com.silabs.ide.si32.gcc.cdt.managedbuild.tool.gnu.c.compiler.base" optionId="com.silabs.gnu.c.compiler.option.misc.otherlist">
@@ -3748,7 +3447,6 @@
     <toolListOption value="-Werror=unused-function"/>
     <toolListOption value="-Werror=unused-label"/>
     <toolListOption value="-Werror=unused-variable"/>
-    <toolListOption value="-Wno-sign-compare"/>
     <toolListOption value="-fno-lto"/>
     <toolListOption value="--specs=nano.specs"/>
     <toolListOption value="-c"/>
@@ -3768,7 +3466,6 @@
     <toolListOption value="-Werror=unused-function"/>
     <toolListOption value="-Werror=unused-label"/>
     <toolListOption value="-Werror=unused-variable"/>
-    <toolListOption value="-Wno-sign-compare"/>
     <toolListOption value="-fno-lto"/>
     <toolListOption value="--specs=nano.specs"/>
     <toolListOption value="-c"/>
diff --git a/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj b/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
index 504dd83..37273f4 100644
--- a/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
+++ b/.pdm/uc.module.setup.ucConfig.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
@@ -33,9 +33,13 @@
     <file name="sl_matter_provision_config.h" generated="true" linked="false"/>
     <file name="SEGGER_RTT_Conf.h" generated="true" linked="false"/>
     <file name="sl_matter_test_event_trigger_config.h" generated="true" linked="false"/>
+    <file name="sl_bt_accept_list_config.h" generated="true" linked="false"/>
+    <file name="sl_bt_resolving_list_config.h" generated="true" linked="false"/>
     <file name="sl_clock_manager_oscillator_config.h" generated="true" linked="false"/>
     <file name="sl_clock_manager_tree_config.h" generated="true" linked="false"/>
     <file name="sl_rail_util_pti_config.h" generated="true" linked="false"/>
+    <file name="sl_uartdrv_eusart_serial_config.h" generated="true" linked="false"/>
+    <file name="sl_uartdrv_eusart_vcom_config.h" generated="true" linked="false"/>
     <file name="nvm3_default_config.h" generated="true" linked="false"/>
     <file name="psa_crypto_config.h" generated="true" linked="false"/>
     <file name="sl_device_init_dcdc_config.h" generated="true" linked="false"/>
@@ -48,14 +52,12 @@
     <file name="circular_queue_config.h" generated="true" linked="false"/>
     <file name="sl_bluetooth_config.h" generated="true" linked="false"/>
     <file name="sl_hfxo_manager_config.h" generated="true" linked="false"/>
-    <file name="sl_openthread_features_config.h" generated="true" linked="false"/>
+    <file name="sl_openthread_features_mtd_cert_config.h" generated="true" linked="false"/>
     <file name="sl_interrupt_manager_s2_config.h" generated="true" linked="false"/>
     <file name="uartdrv_config.h" generated="true" linked="false"/>
-    <file name="sl_openthread_ble_cli_config.h" generated="true" linked="false"/>
     <file name="sl_rail_util_sequencer_config.h" generated="true" linked="false"/>
     <file name="sl_802154_radio_priority_config.h" generated="true" linked="false"/>
     <file name="sl_bluetooth_connection_config.h" generated="true" linked="false"/>
-    <file name="sl_uartdrv_eusart_vcom_config.h" generated="true" linked="false"/>
     <file name="sl_core_config.h" generated="true" linked="false"/>
     <file name="sl_sleeptimer_config.h" generated="true" linked="false"/>
     <file name="sl_power_manager_config.h" generated="true" linked="false"/>
@@ -74,7 +76,7 @@
     <file name="emlib_core_debug_config.h" generated="true" linked="false"/>
     <file name="sl_mbedtls_config.h" generated="true" linked="false"/>
     <file name="sl_mbedtls_device_config.h" generated="true" linked="false"/>
-    <file name="sl_simple_led_inst0_config.h" generated="true" linked="false"/>
+    <file name="sl_simple_led_led0_config.h" generated="true" linked="false"/>
   </folder>
   <includePath uri="studio:/project/config"/>
   <includePath uri="studio:/project/config/app/icd/server"/>
diff --git a/.pdm/uc.module.setup.ucTemplate.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj b/.pdm/uc.module.setup.ucTemplate.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
index f9d1b22..a1749a6 100644
--- a/.pdm/uc.module.setup.ucTemplate.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
+++ b/.pdm/uc.module.setup.ucTemplate.com.silabs.ss.framework.project.toolchain.core.default#com.silabs.ss.tool.ide.arm.toolchain.gnu.cdt.12.2.1.20221205.gcc.slsproj
@@ -19,7 +19,6 @@
     <file name="sli_psa_builtin_config_autogen.h" builtin="true" generated="true"/>
     <file name="sl_simple_led_instances.c" builtin="true" generated="true"/>
     <file name="sl_simple_led_instances.h" builtin="true" generated="true"/>
-    <file name="sl_ot_custom_cli.c" builtin="true" generated="true"/>
     <file name="linkerfile.ld" builtin="true" generated="true"/>
     <file name="sl_uartdrv_init.c" builtin="true" generated="true"/>
     <file name="sl_uartdrv_instances.h" builtin="true" generated="true"/>
diff --git a/.project b/.project
index 6d426c9..f24755e 100644
--- a/.project
+++ b/.project
@@ -842,14 +842,14 @@
 			<locationURI>STUDIO_SDK_LOC/protocol/openthread/include/sl_openthread_package_info.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/openthread/include/sl_ot_custom_cli.h</name>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/libs/libsl_openthread_cm33_gcc.a</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/openthread/include/sl_ot_custom_cli.h</locationURI>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/libs/libsl_openthread_cm33_gcc.a</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/openthread/libs/libsl_openthread_cm33_gcc.a</name>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/libs/libsl_ot_stack_mtd_efr32mg24_gcc.a</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/openthread/libs/libsl_openthread_cm33_gcc.a</locationURI>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/libs/libsl_ot_stack_mtd_efr32mg24_gcc.a</locationURI>
 		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/plugin/security_manager/security_manager.c</name>
@@ -3261,11 +3261,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/protocol/openthread/platform-abstraction/efr32/crypto.c</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/openthread/platform-abstraction/efr32/diag.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/openthread/platform-abstraction/efr32/diag.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/protocol/openthread/platform-abstraction/efr32/diag.h</name>
 			<type>1</type>
@@ -3441,16 +3436,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/protocol/openthread/platform-abstraction/rtos/sl_ot_rtos_adaptation.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/cli/bluetooth_cli.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/cli/bluetooth_cli.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/cli/cli_utils.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/cli/cli_utils.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/silicon_labs/silabs_core/queue/circular_queue.c</name>
 			<type>1</type>
@@ -4101,16 +4086,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterConfig.h</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/platform/silabs/MatterShell.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterShell.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/platform/silabs/MatterShell.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/MatterShell.h</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/examples/platform/silabs/MemMonitoring.h</name>
 			<type>1</type>
@@ -4196,21 +4171,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/uart.h</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/shell/shell_common/cmd_misc.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/cmd_misc.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/shell/shell_common/cmd_otcli.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/cmd_otcli.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/shell/shell_common/globals.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/globals.cpp</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/access/examples/ExampleAccessControlDelegate.cpp</name>
 			<type>1</type>
@@ -4701,6 +4661,11 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/MessageDef/WriteResponseMessage.h</locationURI>
 		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/cluster-building-blocks/QuieterReporting.h</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/cluster-building-blocks/QuieterReporting.h</locationURI>
+		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/codegen-data-model-provider/Instance.h</name>
 			<type>1</type>
@@ -5821,61 +5786,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/dnssd/Types.h</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/Command.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Command.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/CommandSet.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/CommandSet.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/CommandSet.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/CommandSet.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/Commands.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Commands.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/Engine.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Engine.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/Engine.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/Engine.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/MainLoopSilabs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/MainLoopSilabs.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/SubShellCommand.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/SubShellCommand.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/streamer.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/streamer.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/streamer_silabs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/streamer_silabs.cpp</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/Base64.cpp</name>
 			<type>1</type>
@@ -8066,6 +7976,26 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/protocol/openthread/platform-abstraction/rtos/rtos-wrappers/verhoeff_checksum_wrapper.c</locationURI>
 		</link>
+		<link>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/stubs/diag/diag_stubs.c</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/stubs/diag/diag_stubs.c</locationURI>
+		</link>
+		<link>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/stubs/diag/diags_api_stubs.cpp</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/stubs/diag/diags_api_stubs.cpp</locationURI>
+		</link>
+		<link>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/stubs/diag/factory_diags_stubs.cpp</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/stubs/diag/factory_diags_stubs.cpp</locationURI>
+		</link>
+		<link>
+			<name>simplicity_sdk_2024.12.2/protocol/openthread/src/stubs/tcp/tcp_stubs.c</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/protocol/openthread/src/stubs/tcp/tcp_stubs.c</locationURI>
+		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/freertos/cmsis/Include/freertos_mpool.h</name>
 			<type>1</type>
@@ -8971,226 +8901,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/include/openthread/verhoeff_checksum.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_bbr.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_bbr.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_bbr.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_bbr.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_br.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_br.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_br.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_br.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_coap.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_coap.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_coap.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_coap.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_coap_secure.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_coap_secure.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_coap_secure.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_coap_secure.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_commissioner.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_commissioner.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_commissioner.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_commissioner.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_config.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_config.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_dataset.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_dataset.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_dataset.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_dataset.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_dns.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_dns.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_dns.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_dns.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_history.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_history.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_history.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_history.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_joiner.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_joiner.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_joiner.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_joiner.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_link_metrics.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_link_metrics.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_link_metrics.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_link_metrics.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_mac_filter.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_mac_filter.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_mac_filter.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_mac_filter.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_mdns.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_mdns.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_mdns.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_mdns.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_network_data.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_network_data.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_network_data.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_network_data.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_ping.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_ping.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_ping.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_ping.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_srp_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_srp_client.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_srp_client.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_srp_client.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_srp_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_srp_server.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_srp_server.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_srp_server.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_tcat.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_tcat.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_tcat.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_tcat.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_tcp.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_tcp.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_tcp.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_tcp.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_udp.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_udp.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_udp.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_udp.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_utils.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_utils.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/cli_utils.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/cli_utils.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/cli/x509_cert_key.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/cli/x509_cert_key.hpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/openthread-core-config.h</name>
 			<type>1</type>
@@ -9211,16 +8921,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/provision/ProvisionStorageDefault.cpp</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/shell/shell_common/include/ChipShellCollection.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/include/ChipShellCollection.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/shell/shell_common/include/Globals.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/shell/shell_common/include/Globals.h</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/access-control-server/ArlEncoder.cpp</name>
 			<type>1</type>
@@ -9251,6 +8951,16 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/basic-information/basic-information.h</locationURI>
 		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.cpp</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.cpp</locationURI>
+		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.h</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/color-control-server/color-control-server.h</locationURI>
+		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/descriptor/descriptor.cpp</name>
 			<type>1</type>
@@ -9261,11 +8971,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/descriptor/descriptor.h</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/ethernet-network-diagnostics-server/ethernet-network-diagnostics-server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/ethernet-network-diagnostics-server/ethernet-network-diagnostics-server.cpp</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/fixed-label-server/fixed-label-server.cpp</name>
 			<type>1</type>
@@ -9336,6 +9041,16 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/identify-server/identify-server.h</locationURI>
 		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/level-control/level-control.cpp</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/level-control/level-control.cpp</locationURI>
+		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/level-control/level-control.h</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/level-control/level-control.h</locationURI>
+		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/localization-configuration-server/localization-configuration-server.cpp</name>
 			<type>1</type>
@@ -9351,6 +9066,16 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/network-commissioning/network-commissioning.h</locationURI>
 		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.cpp</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.cpp</locationURI>
+		</link>
+		<link>
+			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.h</name>
+			<type>1</type>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/on-off-server/on-off-server.h</locationURI>
+		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/operational-credentials-server/operational-credentials-server.cpp</name>
 			<type>1</type>
@@ -9501,11 +9226,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/user-label-server/user-label-server.cpp</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/wifi-network-diagnostics-server/wifi-network-diagnostics-server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/app/clusters/wifi-network-diagnostics-server/wifi-network-diagnostics-server.cpp</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/app/clusters/window-covering-server/window-covering-delegate.h</name>
 			<type>1</type>
@@ -9737,99 +9457,49 @@
 			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/dnssd/platform/DnssdBrowseDelegate.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/BLE.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.cpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/BLE.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.cpp</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Config.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Config.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Device.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/CHIPLogging.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Device.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/CHIPLogging.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Dns.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/Constants.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Dns.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/Constants.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Help.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.cpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Help.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.cpp</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Help.h</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Help.h</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Meta.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.cpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Meta.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.cpp</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/OnboardingCodes.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/OnboardingCodes.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.h</locationURI>
 		</link>
 		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Ota.cpp</name>
+			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff10.cpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Ota.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/shell/commands/Stat.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/shell/commands/Stat.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/BinaryLogging.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/CHIPLogging.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/CHIPLogging.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/Constants.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/Constants.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/logging/TextOnlyLogging.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff.h</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff10.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff10.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/src/lib/support/verhoeff/Verhoeff10.cpp</locationURI>
 		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/platform/silabs/efr32/BLEManagerImpl.cpp</name>
@@ -10041,11 +9711,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/freertos/kernel/portable/SiliconLabs/tick_power_manager.c</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/examples/apps/cli/cli_uart.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/examples/apps/cli/cli_uart.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/examples/platforms/utils/code_utils.h</name>
 			<type>1</type>
@@ -10242,894 +9907,434 @@
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/include/openthread/platform/udp.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/backbone_router_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/backbone_tmf.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/backbone_router_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/backbone_tmf.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/backbone_router_ftd_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_leader.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/backbone_router_ftd_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_leader.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/ble_secure_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_local.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/ble_secure_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_local.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/border_agent_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_manager.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/border_agent_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_manager.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/border_router_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/border_router_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/border_routing_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/ndproxy_table.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/border_routing_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/ndproxy_table.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/channel_manager_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/infra_if.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/channel_manager_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/infra_if.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/channel_monitor_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/routing_manager.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/channel_monitor_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/routing_manager.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/child_supervision_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/child_supervision_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/coap_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_message.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/coap_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_message.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/coap_secure_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_secure.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/coap_secure_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_secure.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/commissioner_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/appender.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/commissioner_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/appender.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/crypto_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/arg_macros.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/crypto_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/arg_macros.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/dataset_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/array.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/dataset_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/array.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/dataset_ftd_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/as_core_type.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/dataset_ftd_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/as_core_type.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/dataset_updater_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/binary_search.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/dataset_updater_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/binary_search.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/diags_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/bit_set.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/diags_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/bit_set.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/dns_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/callback.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/dns_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/callback.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/dns_server_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/clearable.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/dns_server_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/clearable.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/error_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/code_utils.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/error_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/code_utils.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/heap_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/const_cast.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/heap_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/const_cast.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/history_tracker_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/crc16.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/history_tracker_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/crc16.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/icmp6_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/data.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/icmp6_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/data.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/instance_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/debug.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/instance_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/debug.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/ip6_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/encoding.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/ip6_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/encoding.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/jam_detection_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/equatable.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/jam_detection_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/equatable.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/joiner_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/error.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/joiner_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/error.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/link_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_builder.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/link_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_builder.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/link_metrics_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_data.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/link_metrics_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_data.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/link_raw_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/link_raw_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/logging_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_allocatable.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/logging_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_allocatable.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/mdns_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_array.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/mdns_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_array.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/mesh_diag_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_data.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/mesh_diag_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_data.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/message_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_string.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/message_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_string.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/multi_radio_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/iterator_utils.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/multi_radio_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/iterator_utils.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/nat64_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/linked_list.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/nat64_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/linked_list.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/netdata_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/locator.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/netdata_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/locator.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/netdata_publisher_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/log.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/netdata_publisher_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/log.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/netdiag_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/logging.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/netdiag_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/logging.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/network_time_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/message.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/network_time_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/message.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/ping_sender_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/new.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/ping_sender_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/new.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/radio_stats_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/non_copyable.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/radio_stats_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/non_copyable.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/random_crypto_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/notifier.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/random_crypto_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/notifier.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/random_noncrypto_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/num_utils.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/random_noncrypto_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/num_utils.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/server_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/numeric_limits.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/server_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/numeric_limits.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/sntp_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/offset_range.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/sntp_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/offset_range.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/srp_client_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/owned_ptr.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/srp_client_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/owned_ptr.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/srp_client_buffers_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/owning_list.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/srp_client_buffers_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/owning_list.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/srp_server_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/pool.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/srp_server_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/pool.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/tasklet_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/preference.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/tasklet_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/preference.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/tcp_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/ptr_wrapper.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/tcp_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/ptr_wrapper.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/tcp_ext_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/random.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/tcp_ext_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/random.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/thread_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/retain_ptr.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/thread_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/retain_ptr.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/thread_ftd_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/serial_number.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/thread_ftd_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/serial_number.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/trel_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/settings.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/trel_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/settings.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/udp_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/settings_driver.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/udp_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/settings_driver.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/api/verhoeff_checksum_api.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/string.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/api/verhoeff_checksum_api.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/string.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/backbone_tmf.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tasklet.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/backbone_tmf.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tasklet.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/backbone_tmf.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/time.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/backbone_tmf.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/time.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_leader.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/time_ticker.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_leader.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/time_ticker.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_leader.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/timer.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_leader.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/timer.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_local.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tlvs.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_local.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tlvs.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_local.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/trickle_timer.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_local.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/trickle_timer.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_manager.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/type_traits.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_manager.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/type_traits.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/bbr_manager.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/uptime.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/bbr_manager.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/uptime.hpp</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/announce_sender.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/announce_sender.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/backbone_router.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/multicast_listeners_table.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/backbone_router.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/ndproxy_table.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_agent.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/ndproxy_table.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_agent.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/backbone_router/ndproxy_table.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_router.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/backbone_router/ndproxy_table.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_router.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/infra_if.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_routing.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/infra_if.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_routing.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/infra_if.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/channel_manager.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/infra_if.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/channel_manager.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/routing_manager.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/channel_monitor.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/routing_manager.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/channel_monitor.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/border_router/routing_manager.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/child_supervision.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/border_router/routing_manager.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/child_supervision.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/coap.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/coap.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/commissioner.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/commissioner.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_message.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/crypto.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_message.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/crypto.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_message.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dataset_updater.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_message.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dataset_updater.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_secure.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dhcp6_client.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_secure.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dhcp6_client.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/coap/coap_secure.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dhcp6_server.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/coap/coap_secure.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dhcp6_server.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/appender.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/diag.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/appender.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/diag.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/appender.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dns_client.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/appender.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dns_client.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/arg_macros.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dns_dso.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/arg_macros.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dns_dso.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/array.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dnssd_server.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/array.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dnssd_server.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/as_core_type.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/history_tracker.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/as_core_type.hpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/history_tracker.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/binary_search.cpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/ip6.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/binary_search.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/ip6.h</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/binary_search.hpp</name>
+			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/joiner.h</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/binary_search.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/bit_set.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/bit_set.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/callback.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/callback.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/clearable.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/clearable.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/code_utils.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/code_utils.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/const_cast.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/const_cast.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/crc16.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/crc16.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/crc16.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/crc16.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/data.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/data.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/data.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/data.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/debug.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/debug.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/encoding.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/encoding.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/equatable.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/equatable.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/error.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/error.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/error.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/error.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_builder.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_builder.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_builder.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_builder.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_data.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_data.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/frame_data.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/frame_data.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_allocatable.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_allocatable.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_array.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_array.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_data.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_data.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_data.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_data.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_string.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_string.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/heap_string.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/heap_string.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/iterator_utils.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/iterator_utils.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/linked_list.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/linked_list.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/locator.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/locator.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/log.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/log.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/log.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/log.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/logging.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/logging.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/message.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/message.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/message.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/message.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/new.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/new.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/non_copyable.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/non_copyable.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/notifier.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/notifier.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/notifier.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/notifier.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/num_utils.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/num_utils.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/numeric_limits.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/numeric_limits.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/offset_range.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/offset_range.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/offset_range.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/offset_range.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/owned_ptr.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/owned_ptr.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/owning_list.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/owning_list.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/pool.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/pool.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/preference.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/preference.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/preference.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/preference.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/ptr_wrapper.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/ptr_wrapper.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/random.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/random.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/random.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/random.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/retain_ptr.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/retain_ptr.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/serial_number.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/serial_number.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/settings.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/settings.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/settings.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/settings.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/settings_driver.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/settings_driver.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/string.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/string.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/string.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/string.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tasklet.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tasklet.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tasklet.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tasklet.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/time.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/time.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/time_ticker.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/time_ticker.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/time_ticker.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/time_ticker.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/timer.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/timer.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/timer.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/timer.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tlvs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tlvs.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/tlvs.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/tlvs.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/trickle_timer.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/trickle_timer.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/trickle_timer.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/trickle_timer.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/type_traits.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/type_traits.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/uptime.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/uptime.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/common/uptime.hpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/common/uptime.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/announce_sender.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/announce_sender.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/backbone_router.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/backbone_router.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_agent.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_agent.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_router.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_router.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/border_routing.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/border_routing.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/channel_manager.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/channel_manager.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/channel_monitor.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/channel_monitor.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/child_supervision.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/child_supervision.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/coap.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/coap.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/commissioner.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/commissioner.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/crypto.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/crypto.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dataset_updater.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dataset_updater.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dhcp6_client.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dhcp6_client.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dhcp6_server.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dhcp6_server.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/diag.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/diag.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dns_client.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dns_client.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dns_dso.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dns_dso.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/dnssd_server.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/dnssd_server.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/history_tracker.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/history_tracker.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/ip6.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/ip6.h</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/joiner.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/joiner.h</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/joiner.h</locationURI>
 		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/config/link_metrics_manager.h</name>
@@ -11266,21 +10471,11 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/config/wakeup.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/aes_ccm.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/aes_ccm.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/aes_ccm.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/aes_ccm.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/aes_ecb.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/aes_ecb.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/aes_ecb.hpp</name>
 			<type>1</type>
@@ -11291,71 +10486,36 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/context_size.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/crypto_platform.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/crypto_platform.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/ecdsa.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/ecdsa.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/hkdf_sha256.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/hkdf_sha256.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/hkdf_sha256.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/hkdf_sha256.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/hmac_sha256.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/hmac_sha256.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/hmac_sha256.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/hmac_sha256.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/mbedtls.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/mbedtls.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/mbedtls.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/mbedtls.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/sha256.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/sha256.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/sha256.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/sha256.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/storage.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/storage.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/crypto/storage.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/crypto/storage.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/diags/factory_diags.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/diags/factory_diags.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/diags/factory_diags.hpp</name>
 			<type>1</type>
@@ -11366,341 +10526,161 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/instance/extension.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/instance/instance.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/instance/instance.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/instance/instance.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/instance/instance.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/channel_mask.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/channel_mask.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/channel_mask.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/channel_mask.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/data_poll_handler.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/data_poll_handler.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/data_poll_handler.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/data_poll_handler.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/data_poll_sender.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/data_poll_sender.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/data_poll_sender.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/data_poll_sender.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/link_raw.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/link_raw.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/link_raw.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/link_raw.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_filter.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_filter.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_filter.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_filter.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_frame.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_frame.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_frame.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_frame.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_header_ie.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_header_ie.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_header_ie.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_header_ie.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_links.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_links.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_links.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_links.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/mac_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/mac_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/sub_mac.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/sub_mac.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/sub_mac.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/sub_mac.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/sub_mac_callbacks.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/sub_mac_callbacks.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/sub_mac_csl_receiver.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/sub_mac_csl_receiver.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/sub_mac_wed.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/sub_mac_wed.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/mac/wakeup_tx_scheduler.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/announce_begin_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/announce_begin_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/announce_begin_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/announce_begin_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/border_agent.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/border_agent.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/border_agent.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/border_agent.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/commissioner.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/commissioner.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/commissioner.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/commissioner.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset_manager.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset_manager.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset_manager_ftd.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset_manager_ftd.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset_updater.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset_updater.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/dataset_updater.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/dataset_updater.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/energy_scan_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/energy_scan_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/energy_scan_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/energy_scan_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/extended_panid.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/extended_panid.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/extended_panid.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/extended_panid.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/joiner.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/joiner.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/joiner.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/joiner.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/joiner_router.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/joiner_router.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/joiner_router.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/joiner_router.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop_leader.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop_leader.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop_leader.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop_leader.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop_tlvs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop_tlvs.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/meshcop_tlvs.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/meshcop_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/network_name.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/network_name.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/network_name.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/network_name.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/panid_query_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/panid_query_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/panid_query_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/panid_query_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/secure_transport.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/secure_transport.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/secure_transport.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/secure_transport.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/tcat_agent.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/tcat_agent.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/tcat_agent.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/tcat_agent.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/timestamp.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/timestamp.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/meshcop/timestamp.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/meshcop/timestamp.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/checksum.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/checksum.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/checksum.hpp</name>
 			<type>1</type>
@@ -11711,146 +10691,71 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dhcp6.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dhcp6_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dhcp6_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dhcp6_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dhcp6_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dhcp6_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dhcp6_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dhcp6_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dhcp6_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_dso.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_dso.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_dso.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_dso.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_platform.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_platform.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dns_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dns_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dnssd.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dnssd.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dnssd.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dnssd.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dnssd_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dnssd_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/dnssd_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/dnssd_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/icmp6.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/icmp6.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/icmp6.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/icmp6.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip4_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip4_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip4_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip4_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_address.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_address.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_address.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_address.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_filter.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_filter.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_filter.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_filter.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_headers.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_headers.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_headers.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_headers.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_mpl.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_mpl.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/ip6_mpl.hpp</name>
 			<type>1</type>
@@ -11861,141 +10766,71 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/ip6_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/mdns.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/mdns.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/mdns.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/mdns.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nat64_translator.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nat64_translator.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nat64_translator.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nat64_translator.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nd6.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nd6.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nd6.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nd6.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nd_agent.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nd_agent.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/nd_agent.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/nd_agent.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/netif.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/netif.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/netif.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/netif.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/sntp_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/sntp_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/sntp_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/sntp_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/socket.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/socket.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/socket.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/socket.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_advertising_proxy.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_advertising_proxy.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_advertising_proxy.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_advertising_proxy.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_client.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_client.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_client.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_client.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/srp_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/srp_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/tcp6.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/tcp6.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/tcp6.hpp</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/tcp6.hpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/tcp6_ext.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/tcp6_ext.cpp</locationURI>
+			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/tcp6.hpp</locationURI>
 		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/tcp6_ext.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/tcp6_ext.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/udp6.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/udp6.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/net/udp6.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/net/udp6.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/ble_secure.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/ble_secure.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/ble_secure.hpp</name>
 			<type>1</type>
@@ -12006,101 +10841,46 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/max_power_table.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/radio.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/radio.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/radio.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/radio.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/radio_callbacks.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/radio_callbacks.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/radio_platform.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/radio_platform.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_interface.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_interface.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_interface.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_interface.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_link.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_link.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_link.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_link.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_packet.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_packet.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/radio/trel_packet.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/radio/trel_packet.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/address_resolver.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/address_resolver.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/address_resolver.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/address_resolver.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/announce_begin_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/announce_begin_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/announce_begin_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/announce_begin_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/announce_sender.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/announce_sender.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/announce_sender.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/announce_sender.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/anycast_locator.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/anycast_locator.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/anycast_locator.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/anycast_locator.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child.hpp</name>
 			<type>1</type>
@@ -12111,71 +10891,36 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child_mask.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child_supervision.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child_supervision.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child_supervision.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child_supervision.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child_table.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child_table.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/child_table.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/child_table.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/csl_tx_scheduler.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/csl_tx_scheduler.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/csl_tx_scheduler.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/csl_tx_scheduler.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/discover_scanner.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/discover_scanner.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/discover_scanner.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/discover_scanner.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/dua_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/dua_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/dua_manager.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/dua_manager.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/energy_scan_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/energy_scan_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/energy_scan_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/energy_scan_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/indirect_sender.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/indirect_sender.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/indirect_sender.hpp</name>
 			<type>1</type>
@@ -12186,21 +10931,11 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/indirect_sender_frame_context.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/key_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/key_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/key_manager.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/key_manager.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_metrics.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_metrics.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_metrics.hpp</name>
 			<type>1</type>
@@ -12211,101 +10946,46 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_metrics_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_metrics_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_metrics_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_metrics_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_metrics_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_quality.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_quality.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/link_quality.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/link_quality.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/lowpan.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/lowpan.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/lowpan.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/lowpan.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mesh_forwarder.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mesh_forwarder.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mesh_forwarder.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mesh_forwarder.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mesh_forwarder_ftd.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mesh_forwarder_ftd.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mesh_forwarder_mtd.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mesh_forwarder_mtd.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_router.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_router.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_router.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_router.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_tlvs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_tlvs.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_tlvs.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mle_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mle_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mlr_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mlr_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/mlr_manager.hpp</name>
 			<type>1</type>
@@ -12316,186 +10996,91 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/mlr_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/neighbor.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/neighbor.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/neighbor.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/neighbor.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/neighbor_table.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/neighbor_table.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/neighbor_table.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/neighbor_table.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_leader.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_leader.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_leader.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_leader.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_leader_ftd.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_leader_ftd.cpp</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_local.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_local.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_local.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_local.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_notifier.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_notifier.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_notifier.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_notifier.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_publisher.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_publisher.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_publisher.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_publisher.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_service.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_service.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_service.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_service.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_tlvs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_tlvs.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_tlvs.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_types.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_types.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_data_types.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_data_types.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_diagnostic.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_diagnostic.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_diagnostic.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_diagnostic.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_diagnostic_tlvs.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_diagnostic_tlvs.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/network_diagnostic_tlvs.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/network_diagnostic_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/panid_query_server.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/panid_query_server.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/panid_query_server.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/panid_query_server.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/radio_selector.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/radio_selector.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/radio_selector.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/radio_selector.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/router.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/router.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/router.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/router.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/router_table.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/router_table.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/router_table.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/router_table.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/src_match_controller.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/src_match_controller.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/src_match_controller.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/src_match_controller.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/thread_netif.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/thread_netif.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/thread_netif.hpp</name>
 			<type>1</type>
@@ -12506,31 +11091,16 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/thread_tlvs.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/time_sync_service.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/time_sync_service.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/time_sync_service.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/time_sync_service.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/tmf.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/tmf.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/tmf.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/tmf.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/uri_paths.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/uri_paths.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/thread/uri_paths.hpp</name>
 			<type>1</type>
@@ -12541,141 +11111,71 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/thread/version.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/channel_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/channel_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/channel_manager.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/channel_manager.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/channel_monitor.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/channel_monitor.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/channel_monitor.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/channel_monitor.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/flash.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/flash.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/flash.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/flash.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/heap.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/heap.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/heap.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/heap.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/history_tracker.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/history_tracker.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/history_tracker.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/history_tracker.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/jam_detector.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/jam_detector.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/jam_detector.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/jam_detector.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/link_metrics_manager.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/link_metrics_manager.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/link_metrics_manager.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/link_metrics_manager.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/mesh_diag.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/mesh_diag.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/mesh_diag.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/mesh_diag.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/otns.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/otns.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/otns.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/otns.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/parse_cmdline.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/parse_cmdline.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/parse_cmdline.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/parse_cmdline.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/ping_sender.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/ping_sender.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/ping_sender.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/ping_sender.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/power_calibration.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/power_calibration.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/power_calibration.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/power_calibration.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/slaac_address.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/slaac_address.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/slaac_address.hpp</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/slaac_address.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/srp_client_buffers.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/srp_client_buffers.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/srp_client_buffers.hpp</name>
 			<type>1</type>
@@ -12686,11 +11186,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/static_counter.hpp</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/verhoeff_checksum.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/src/core/utils/verhoeff_checksum.cpp</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/src/core/utils/verhoeff_checksum.hpp</name>
 			<type>1</type>
@@ -12731,11 +11226,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_const.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_fastopen.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_fastopen.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_fastopen.h</name>
 			<type>1</type>
@@ -12746,56 +11236,16 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_fsm.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_input.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_input.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_output.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_output.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_reass.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_reass.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_sack.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_sack.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_seq.h</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_seq.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_subr.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_subr.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.h</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timer.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timewait.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_timewait.c</locationURI>
-		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_usrreq.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_usrreq.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/tcp_var.h</name>
 			<type>1</type>
@@ -12806,46 +11256,21 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/types.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/bitmap.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/bitmap.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/bitmap.h</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/bitmap.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/cbuf.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/cbuf.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/cbuf.h</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/cbuf.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/lbuf.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/lbuf.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/lib/lbuf.h</name>
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/lib/lbuf.h</locationURI>
 		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.cpp</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.cpp</locationURI>
-		</link>
-		<link>
-			<name>matter_2.5.2/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.h</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/extension/matter_extension/third_party/matter_sdk/examples/platform/silabs/shell/icd/ICDShellCommands.h</locationURI>
-		</link>
 		<link>
 			<name>matter_2.5.2/third_party/matter_sdk/src/include/platform/internal/testing/ConfigUnitTest.h</name>
 			<type>1</type>
@@ -12856,11 +11281,6 @@
 			<type>1</type>
 			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/cc/cc_module.h</locationURI>
 		</link>
-		<link>
-			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/cc/cc_newreno.c</name>
-			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/util/third_party/openthread/third_party/tcplp/bsdtcp/cc/cc_newreno.c</locationURI>
-		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/util/third_party/openthread/third_party/tcplp/bsdtcp/sys/queue.h</name>
 			<type>1</type>
@@ -12877,9 +11297,9 @@
 			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/bgapi_protocol/api3/release/libbgapi_core.a</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list_stub.a</name>
+			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list.a</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list_stub.a</locationURI>
+			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/ble_host/accept_list/release/libble_host_accept_list.a</locationURI>
 		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libble_host.a</name>
@@ -12887,9 +11307,9 @@
 			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libble_host.a</locationURI>
 		</link>
 		<link>
-			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb_stub.a</name>
+			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb.a</name>
 			<type>1</type>
-			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb_stub.a</locationURI>
+			<locationURI>STUDIO_SDK_LOC/protocol/bluetooth/build/gcc/cortex-m33/ble_host/bgstack/release/libbondingdb.a</locationURI>
 		</link>
 		<link>
 			<name>simplicity_sdk_2024.12.2/protocol/bluetooth/build/gcc/cortex-m33/ble_host/ble_bgapi/release/libble_bgapi.a</name>
diff --git a/.vscode/settings.json b/.vscode/settings.json
new file mode 100644
index 0000000..5b9d860
--- /dev/null
+++ b/.vscode/settings.json
@@ -0,0 +1,43 @@
+{
+    "files.associations": {
+        "array": "cpp",
+        "istream": "cpp",
+        "ostream": "cpp",
+        "tuple": "cpp",
+        "type_traits": "cpp",
+        "utility": "cpp",
+        "fstream": "cpp",
+        "new": "cpp",
+        "optional": "cpp",
+        "system_error": "cpp",
+        "atomic": "cpp",
+        "cctype": "cpp",
+        "clocale": "cpp",
+        "cmath": "cpp",
+        "cstdarg": "cpp",
+        "cstddef": "cpp",
+        "cstdint": "cpp",
+        "cstdio": "cpp",
+        "cstdlib": "cpp",
+        "cstring": "cpp",
+        "cwchar": "cpp",
+        "cwctype": "cpp",
+        "deque": "cpp",
+        "list": "cpp",
+        "unordered_map": "cpp",
+        "vector": "cpp",
+        "exception": "cpp",
+        "algorithm": "cpp",
+        "memory": "cpp",
+        "memory_resource": "cpp",
+        "string": "cpp",
+        "string_view": "cpp",
+        "initializer_list": "cpp",
+        "iosfwd": "cpp",
+        "limits": "cpp",
+        "sstream": "cpp",
+        "stdexcept": "cpp",
+        "streambuf": "cpp",
+        "typeinfo": "cpp"
+    }
+}
\ No newline at end of file
diff --git a/aok02_matter_ac.pintool b/aok02_matter_ac.pintool
index e27cc54..0500ff5 100644
--- a/aok02_matter_ac.pintool
+++ b/aok02_matter_ac.pintool
@@ -1,7 +1,24 @@
 <?xml version="1.0" encoding="ASCII"?>
-<device:XMLDevice xmi:version="2.0" xmlns:xmi="http://www.omg.org/XMI" xmlns:device="http://www.silabs.com/ss/hwconfig/document/device.ecore" name="pin_tool.EFR32MG24A410F1536IM40" partId="mcu.arm.efr32.mg24.efr32mg24a410f1536im40" contextId="com.silabs.sdk.stack.sisdk:2024.12.2._-667083859">
+<device:XMLDevice xmi:version="2.0" xmlns:xmi="http://www.omg.org/XMI" xmlns:device="http://www.silabs.com/ss/hwconfig/document/device.ecore" name="pin_tool.EFR32MG24A410F1536IM40" partId="mcu.arm.efr32.mg24.efr32mg24a410f1536im40" contextId="com.silabs.sdk.stack.sisdk:2024.12.2._827188305">
   <mode name="DefaultMode">
     <property object="DefaultMode" propertyId="mode.diagramLocation" value="100, 100"/>
+    <property object="EUSART0" propertyId="ABModule.selectedRequirement" value="eusart%T%SL_UARTDRV_EUSART_SERIAL%T%sl_uartdrv_eusart_serial_config.h"/>
+    <property object="EUSART0" propertyId="ABPeripheral.included" value="true"/>
+    <property object="EUSART1" propertyId="ABModule.selectedRequirement" value="eusart%T%SL_UARTDRV_EUSART_VCOM%T%sl_uartdrv_eusart_vcom_config.h"/>
+    <property object="EUSART1" propertyId="ABPeripheral.included" value="true"/>
+    <property object="PA03" propertyId="ABModule.selectedRequirement" value="gpio%T%SL_SIMPLE_LED_LED0%T%sl_simple_led_led0_config.h"/>
+    <property object="PORTIO" propertyId="portio.eusart0.enable.rx" value="Enabled"/>
+    <property object="PORTIO" propertyId="portio.eusart0.enable.tx" value="Enabled"/>
+    <property object="PORTIO" propertyId="portio.eusart0.location.rx" value="18"/>
+    <property object="PORTIO" propertyId="portio.eusart0.location.tx" value="17"/>
+    <property object="PORTIO" propertyId="portio.eusart1.enable.rx" value="Enabled"/>
+    <property object="PORTIO" propertyId="portio.eusart1.enable.tx" value="Enabled"/>
+    <property object="PORTIO" propertyId="portio.eusart1.location.rx" value="8"/>
+    <property object="PORTIO" propertyId="portio.eusart1.location.tx" value="7"/>
+    <property object="PORTIO" propertyId="portio.pti.enable.dclk" value="Enabled"/>
+    <property object="PTI" propertyId="ABModule.selectedRequirement" value="pti%T%SL_RAIL_UTIL_PTI%T%sl_rail_util_pti_config.h"/>
+    <property object="PTI" propertyId="ABPeripheral.included" value="true"/>
+    <property object="PTI" propertyId="peripheral.name" value=""/>
   </mode>
   <modeTransition>
     <property object="RESET &#x2192; DefaultMode" propertyId="modeTransition.source" value="RESET"/>
diff --git a/aok02_matter_ac.slcp b/aok02_matter_ac.slcp
index 6e15f69..fb5fd67 100644
--- a/aok02_matter_ac.slcp
+++ b/aok02_matter_ac.slcp
@@ -9,18 +9,44 @@ readme:
 - {path: README.md}
 - {path: README.md}
 source:
-- {path: src/AppTask.cpp}
 - {path: src/main.cpp}
-- {path: src/WindowManager.cpp}
-- {path: src/ZclCallbacks.cpp}
+- {path: common/app/app_ble_mgr.cpp}
+- {path: common/app/app_colorlight_mgr.cpp}
+- {path: common/app/app_comm_mgr.cpp}
+- {path: common/app/app_endpoint_mgr.cpp}
+- {path: common/app/app_identify_mgr.cpp}
+- {path: common/app/app_msg_mgr.cpp}
+- {path: common/app/app_nwk_mgr.cpp}
+- {path: common/app/app_phone_mgr.cpp}
+- {path: common/app/app_spm_mgr.cpp}
+- {path: common/app/app_timetask_mgr.cpp}
+- {path: common/app/app_wdc_mgr.cpp}
+- {path: common/app/AppTask.cpp}
+- {path: common/app/color_format.cpp}
+- {path: common/app/rgb_light.cpp}
+- {path: common/app/ZclCallbacks.cpp}
+- {path: common/app/log_api.c}
+- {path: common/app/app_lockout_mgr.c}
+- {path: common/event_queue/event_handler.c}
+- {path: common/event_queue/event-queue.c}
+- {path: common/event_queue/hal_ticktimer.c}
+- {path: common/hal/hal_uart.cpp}
+- {path: common/hal/wdg_api.c}
+- {path: common/misc/ble_connection.cpp}
+- {path: common/misc/dev_mapping.cpp}
+- {path: common/misc/phone_nvm3_table.cpp}
+- {path: common/misc/phone_protocol.cpp}
+- {path: common/misc/rc_nvm3_table.cpp}
+- {path: common/misc/rc_protocol.cpp}
+- {path: common/misc/sp_protocol.cpp}
+- {path: common/misc/sys_config.cpp}
+- {path: common/misc/time_task.cpp}
 include:
-- path: include
-  file_list:
-  - {path: AppConfig.h}
-  - {path: CHIPProjectConfig.h}
-  - {path: WindowManager.h}
-  - {path: AppTask.h}
-  - {path: AppEvent.h}
+- {path: include}
+- {path: common/app}
+- {path: common/event_queue}
+- {path: common/hal}
+- {path: common/misc}
 sdk: {id: simplicity_sdk, version: 2024.12.2}
 toolchain_settings:
 - {value: gnu++17, option: cxx_standard}
@@ -32,11 +58,11 @@ component:
 - {from: matter, id: matter_basic_information}
 - {from: matter, id: matter_ble}
 - {from: matter, id: matter_buttons}
+- {from: matter, id: matter_color_control}
 - {from: matter, id: matter_configuration_over_swo}
 - {from: matter, id: matter_crypto}
 - {from: matter, id: matter_default_lcd_config}
 - {from: matter, id: matter_descriptor}
-- {from: matter, id: matter_ethernet_network_diagnostics}
 - {from: matter, id: matter_fixed_label}
 - {from: matter, id: matter_gatt}
 - {from: matter, id: matter_general_commissioning}
@@ -47,9 +73,11 @@ component:
 - {from: matter, id: matter_icd_management}
 - {from: matter, id: matter_identify}
 - {from: matter, id: matter_leds}
+- {from: matter, id: matter_level_control}
 - {from: matter, id: matter_localization_configuration}
 - {from: matter, id: matter_log_uart}
 - {from: matter, id: matter_network_commissioning}
+- {from: matter, id: matter_on_off}
 - {from: matter, id: matter_operational_credentials}
 - {from: matter, id: matter_ota_requestor}
 - {from: matter, id: matter_ota_support}
@@ -57,21 +85,28 @@ component:
 - {from: matter, id: matter_power_source}
 - {from: matter, id: matter_provision_default}
 - {from: matter, id: matter_segger_rtt}
-- {from: matter, id: matter_shell}
 - {from: matter, id: matter_software_diagnostics}
 - {from: matter, id: matter_test_event_trigger}
 - {from: matter, id: matter_thread}
 - {from: matter, id: matter_thread_network_diagnostics}
 - {from: matter, id: matter_time_format_localization}
 - {from: matter, id: matter_user_label}
-- {from: matter, id: matter_wifi_network_diagnostics}
 - {from: matter, id: matter_window}
 - {from: matter, id: matter_window_covering}
 - {id: EFR32MG24A410F1536IM40}
+- {id: bluetooth_feature_accept_list}
+- {id: bluetooth_feature_gatt_client_att_mtu_request_only}
+- {id: bluetooth_feature_resolving_list}
+- {id: bluetooth_feature_sm}
 - {id: clock_manager}
 - {id: device_init}
+- {id: ot_cert_libs}
 - {id: rail_util_pti}
+- instance: [led0]
+  id: simple_led
 - {id: sl_system}
+- instance: [serial, vcom]
+  id: uartdrv_eusart
 other_file:
 - {path: qr_code_img.png}
 define:
@@ -79,6 +114,8 @@ define:
 - {name: _WANT_REENT_SMALL, value: '1'}
 - {name: NVM3_DEFAULT_NVM_SIZE, value: '40960'}
 - {name: NVM3_DEFAULT_MAX_OBJECT_SIZE, value: '4092'}
+- {name: SL_OPENTHREAD_APPLICATION_CONFIG_FILE, value: '"sl_openthread_application_config.h"'}
+- {name: AOK02_MATTER_PROJECT, value: '1'}
 config_file:
 - {path: config/common/window-app.zap, directory: common}
 - {path: config/provision/provision.mattpconf, directory: provision}
diff --git a/aok02_matter_ac.slps b/aok02_matter_ac.slps
index 5899684..c89d5bc 100644
--- a/aok02_matter_ac.slps
+++ b/aok02_matter_ac.slps
@@ -1,9 +1,9 @@
 <?xml version="1.0" encoding="ASCII"?>
 <model:MDescriptors xmlns:model="http://www.silabs.com/ss/Studio.ecore">
   <descriptors name="aok02_matter_ac">
-    <properties key="projectCommon.sdkId" value="com.silabs.sdk.stack.sisdk:2024.12.2._-667083859"/>
+    <properties key="projectCommon.sdkId" value="com.silabs.sdk.stack.sisdk:2024.12.2._827188305"/>
     <properties key="universalConfig.relativeWorkspacePath" value="..\aok02-dc.slcw"/>
-    <properties key="universalConfig.generationDirectory" value="..\..\..\..\..\..\..\..\v5_aok\aok02_matter_ac"/>
+    <properties key="universalConfig.generationDirectory" value=""/>
     <properties key="universalConfig.toolchainCompatibility" value="gcc"/>
     <properties key="projectCommon.overwriteCopiedSources" value="false"/>
     <properties key="projectCommon.boardIds" value="com.silabs.board.none:0.0.0"/>
diff --git a/config/btconf/gatt_configuration.btconf b/config/btconf/gatt_configuration.btconf
index 4d1efd9..690c973 100644
--- a/config/btconf/gatt_configuration.btconf
+++ b/config/btconf/gatt_configuration.btconf
@@ -1,21 +1,20 @@
 <?xml version="1.0" encoding="UTF-8" standalone="no"?>
 <!--Custom BLE GATT-->
 <gatt gatt_caching="true" generic_attribute_service="true" header="gatt_db.h" name="Custom BLE GATT" out="gatt_db.c" prefix="gattdb_">
-  
+
   <!--Generic Access-->
   <service advertise="false" name="Generic Access" requirement="mandatory" sourceId="org.bluetooth.service.generic_access" type="primary" uuid="1800">
     <informativeText>Abstract: The generic_access service contains generic information about the device. All available Characteristics are readonly. </informativeText>
-    
+
     <!--Device Name-->
     <characteristic const="false" id="device_name" name="Device Name" sourceId="org.bluetooth.characteristic.gap.device_name" uuid="2A00">
-      <informativeText/>
-      <value length="13" type="utf-8" variable_length="false">Empty Example</value>
+      <value length="13" type="utf-8" variable_length="false">Matter</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
         <write authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
-    
+
     <!--Appearance-->
     <characteristic const="true" name="Appearance" sourceId="org.bluetooth.characteristic.gap.appearance" uuid="2A01">
       <informativeText>Abstract: The external appearance of this device. The values are composed of a category (10-bits) and sub-categories (6-bits). </informativeText>
@@ -24,57 +23,157 @@
         <read authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
+
+    <!--Central Address Resolution-->
+    <characteristic const="false" id="central_address_resolution_0" name="Central Address Resolution" sourceId="org.bluetooth.characteristic.gap.central_address_resolution" uuid="2AA6">
+      <value length="1" type="hex" variable_length="false"/>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
   </service>
-  
+
   <!--Device Information-->
   <service advertise="false" name="Device Information" requirement="mandatory" sourceId="org.bluetooth.service.device_information" type="primary" uuid="180A">
     <informativeText>Abstract: The Device Information Service exposes manufacturer and/or vendor information about a device. Summary: This service exposes manufacturer information about a device. The Device Information Service is instantiated as a Primary Service. Only one instance of the Device Information Service is exposed on a device. </informativeText>
-    
+
     <!--Manufacturer Name String-->
-    <characteristic const="true" name="Manufacturer Name String" sourceId="org.bluetooth.characteristic.manufacturer_name_string" uuid="2A29">
+    <characteristic const="false" id="manufacturer_name" name="Manufacturer Name String" sourceId="org.bluetooth.characteristic.manufacturer_name_string" uuid="2A29">
       <informativeText>Abstract: The value of this characteristic is a UTF-8 string representing the name of the manufacturer of the device. </informativeText>
-      <value length="12" type="utf-8" variable_length="false">Silicon Labs</value>
+      <value length="12" type="utf-8" variable_length="true">Silicon Labs</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
-    
+
     <!--Model Number String-->
-    <characteristic const="true" name="Model Number String" sourceId="org.bluetooth.characteristic.model_number_string" uuid="2A24">
+    <characteristic const="false" id="model_number" name="Model Number String" sourceId="org.bluetooth.characteristic.model_number_string" uuid="2A24">
       <informativeText>Abstract: The value of this characteristic is a UTF-8 string representing the model number assigned by the device vendor. </informativeText>
-      <value length="10" type="utf-8" variable_length="false">Blue Gecko</value>
+      <value length="20" type="utf-8" variable_length="true"/>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
-    
+
     <!--System ID-->
-    <characteristic const="true" name="System ID" sourceId="org.bluetooth.characteristic.system_id" uuid="2A23">
+    <characteristic const="false" id="system_id" name="System ID" sourceId="org.bluetooth.characteristic.system_id" uuid="2A23">
       <informativeText>Abstract: The SYSTEM ID characteristic consists of a structure with two fields. The first field are the LSOs and the second field contains the MSOs.       This is a 64-bit structure which consists of a 40-bit manufacturer-defined identifier concatenated with a 24 bit unique Organizationally Unique Identifier (OUI). The OUI is issued by the IEEE Registration Authority (http://standards.ieee.org/regauth/index.html) and is required to be used in accordance with IEEE Standard 802-2001.6 while the least significant 40 bits are manufacturer defined.       If System ID generated based on a Bluetooth Device Address, it is required to be done as follows. System ID and the Bluetooth Device Address have a very similar structure: a Bluetooth Device Address is 48 bits in length and consists of a 24 bit Company Assigned Identifier (manufacturer defined identifier) concatenated with a 24 bit Company Identifier (OUI). In order to encapsulate a Bluetooth Device Address as System ID, the Company Identifier is concatenated with 0xFFFE followed by the Company Assigned Identifier of the Bluetooth Address. For more guidelines related to EUI-64, refer to http://standards.ieee.org/develop/regauth/tut/eui64.pdf. Examples: If the system ID is based of a Bluetooth Device Address with a Company Identifier (OUI) is 0x123456 and the Company Assigned Identifier is 0x9ABCDE, then the System Identifier is required to be 0x123456FFFE9ABCDE. </informativeText>
-      <value length="6" type="hex" variable_length="false">000102030405</value>
+      <value length="8" type="hex" variable_length="true">000102030405</value>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--Serial Number String-->
+    <characteristic const="false" id="serial_number" name="Serial Number String" sourceId="org.bluetooth.characteristic.serial_number_string" uuid="2A25">
+      <value length="20" type="utf-8" variable_length="true"/>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--Hardware Revision String-->
+    <characteristic const="false" id="hardware_revision" name="Hardware Revision String" sourceId="org.bluetooth.characteristic.hardware_revision_string" uuid="2A27">
+      <value length="20" type="utf-8" variable_length="true">00</value>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--Firmware Revision String-->
+    <characteristic const="false" id="firmware_revision_string_0" name="Firmware Revision String" sourceId="org.bluetooth.characteristic.firmware_revision_string" uuid="2A26">
+      <value length="20" type="hex" variable_length="true"/>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--IEEE 11073-20601 Regulatory Certification Data List-->
+    <characteristic const="false" id="regulatory_cert_data" name="IEEE 11073-20601 Regulatory Certification Data List" sourceId="org.bluetooth.characteristic.ieee_11073-20601_regulatory_certification_data_list" uuid="2A2A">
+      <value length="20" type="hex" variable_length="true">00</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
+
+    <!--PnP ID-->
+    <characteristic const="false" id="pnp_id" name="PnP ID" sourceId="org.bluetooth.characteristic.pnp_id" uuid="2A50">
+      <value length="20" type="hex" variable_length="true">00</value>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+  </service>
+
+  <!--AOK Service-->
+  <service advertise="false" id="aok_service" name="AOK Service" requirement="mandatory" sourceId="custom.type" type="primary" uuid="6e40ff01-b5a3-f393-e0a9-e50e24dcca9e">
+    <informativeText>Custom service</informativeText>
+
+    <!--app2host-->
+    <characteristic const="false" id="app2host" name="app2host" sourceId="custom.type" uuid="6e40ff04-b5a3-f393-e0a9-e50e24dcca9e">
+      <informativeText>Custom characteristic</informativeText>
+      <value length="247" type="user" variable_length="true">00</value>
+      <properties>
+        <write authenticated="false" bonded="false" encrypted="false"/>
+        <write_no_response authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--remotectl_rx-->
+    <characteristic const="false" id="remotectl_rx" name="remotectl_rx" sourceId="custom.type" uuid="8e8ed52f-bd01-49c2-90e4-c875387b6fa3">
+      <informativeText>Custom characteristic</informativeText>
+      <value length="247" type="user" variable_length="true">00</value>
+      <properties>
+        <write authenticated="false" bonded="false" encrypted="false"/>
+        <write_no_response authenticated="false" bonded="false" encrypted="false"/>
+        <notify authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--remotectl_tx-->
+    <characteristic const="false" id="remotectl_tx" name="remotectl_tx" sourceId="custom.type" uuid="7f6abf15-03ce-49bc-b751-59ccdd8706fb">
+      <informativeText>Custom characteristic</informativeText>
+      <value length="512" type="user" variable_length="true">00</value>
+      <properties>
+        <indicate authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+
+    <!--host2app-->
+    <characteristic const="false" id="host2app" name="host2app" sourceId="custom.type" uuid="6e40ff03-b5a3-f393-e0a9-e50e24dcca9e">
+      <value length="250" type="hex" variable_length="true">00</value>
+      <properties>
+        <notify authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
   </service>
-  
+
+  <!--Generic Attribute-->
+  <service advertise="false" id="generic_attribute_0" name="Generic Attribute" requirement="mandatory" sourceId="org.bluetooth.service.generic_attribute" type="primary" uuid="1801">
+
+    <!--Service Changed-->
+    <characteristic const="false" id="service_changed" name="Service Changed" sourceId="2A05" uuid="2A05">
+      <value length="4" type="hex" variable_length="false">00</value>
+      <properties>
+        <indicate authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
+  </service>
+
   <!--CHIPoBLE-->
   <service advertise="false" name="CHIPoBLE" requirement="mandatory" sourceId="custom.type" type="primary" uuid="fff6">
-    <informativeText>Custom service</informativeText>
-    
+
     <!--CHIPoBLEChar_Rx-->
     <characteristic const="false" id="CHIPoBLEChar_Rx" name="CHIPoBLEChar_Rx" sourceId="custom.type" uuid="18EE2EF5-263D-4559-959F-4F9C429F9D11">
-      <informativeText>Custom characteristic</informativeText>
       <value length="247" type="hex" variable_length="true">00</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
         <write authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
-    
+
     <!--CHIPoBLEChar_Tx-->
     <characteristic const="false" id="CHIPoBLEChar_Tx" name="CHIPoBLEChar_Tx" sourceId="custom.type" uuid="18EE2EF5-263D-4559-959F-4F9C429F9D12">
-      <informativeText>Custom characteristic</informativeText>
       <value length="247" type="hex" variable_length="true">00</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
@@ -84,8 +183,8 @@
       </properties>
     </characteristic>
 
+    <!--CHIPoBLEChar_C3-->
     <characteristic const="false" id="CHIPoBLEChar_C3" name="CHIPoBLEChar_C3" sourceId="custom.type" uuid="64630238-8772-45F2-B87D-748A83218F04">
-      <informativeText>Custom characteristic</informativeText>
       <value length="512" type="hex" variable_length="true">00</value>
       <properties>
         <read authenticated="false" bonded="false" encrypted="false"/>
@@ -94,6 +193,18 @@
         <indicate authenticated="false" bonded="false" encrypted="false"/>
       </properties>
     </characteristic>
+  </service>
 
+  <!--Battery Service-->
+  <service advertise="false" id="battery_service_0" name="Battery Service" requirement="mandatory" sourceId="org.bluetooth.service.battery_service" type="primary" uuid="180F">
+
+    <!--Battery Level-->
+    <characteristic const="false" id="battery_level" name="Battery Level" sourceId="org.bluetooth.characteristic.battery_level" uuid="2A19">
+      <value length="0" type="hex" variable_length="true">00</value>
+      <properties>
+        <read authenticated="false" bonded="false" encrypted="false"/>
+        <notify authenticated="false" bonded="false" encrypted="false"/>
+      </properties>
+    </characteristic>
   </service>
 </gatt>
diff --git a/config/common/window-app.zap b/config/common/window-app.zap
index 3b46618..713b4b6 100644
--- a/config/common/window-app.zap
+++ b/config/common/window-app.zap
@@ -38,38 +38,47 @@
       "id": 1,
       "name": "MA-windowcovering",
       "deviceTypeRef": {
-        "code": 17,
+        "code": 22,
         "profileId": 259,
-        "label": "MA-powersource",
-        "name": "MA-powersource",
+        "label": "MA-rootdevice",
+        "name": "MA-rootdevice",
         "deviceTypeOrder": 0
       },
       "deviceTypes": [
+        {
+          "code": 22,
+          "profileId": 259,
+          "label": "MA-rootdevice",
+          "name": "MA-rootdevice",
+          "deviceTypeOrder": 0
+        },
         {
           "code": 17,
           "profileId": 259,
           "label": "MA-powersource",
           "name": "MA-powersource",
-          "deviceTypeOrder": 0
+          "deviceTypeOrder": 1
         },
         {
-          "code": 22,
+          "code": 18,
           "profileId": 259,
-          "label": "MA-rootdevice",
-          "name": "MA-rootdevice",
-          "deviceTypeOrder": 1
+          "label": "MA-otarequestor",
+          "name": "MA-otarequestor",
+          "deviceTypeOrder": 2
         }
       ],
       "deviceVersions": [
+        3,
         1,
         1
       ],
       "deviceIdentifiers": [
+        22,
         17,
-        22
+        18
       ],
-      "deviceTypeName": "MA-powersource",
-      "deviceTypeCode": 17,
+      "deviceTypeName": "MA-rootdevice",
+      "deviceTypeCode": 22,
       "deviceTypeProfileId": 259,
       "clusters": [
         {
@@ -266,22 +275,6 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
-            {
-              "name": "Extension",
-              "code": 1,
-              "mfgCode": null,
-              "side": "server",
-              "type": "array",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 1,
-              "maxInterval": 65534,
-              "reportableChange": 0
-            },
             {
               "name": "SubjectsPerAccessControlEntry",
               "code": 2,
@@ -434,13 +427,6 @@
               "mfgCode": null,
               "side": "server",
               "included": 1
-            },
-            {
-              "name": "AccessControlExtensionChanged",
-              "code": 1,
-              "mfgCode": null,
-              "side": "server",
-              "included": 1
             }
           ]
         },
@@ -878,7 +864,7 @@
               "storageOption": "RAM",
               "singleton": 1,
               "bounded": 0,
-              "defaultValue": "3",
+              "defaultValue": "4",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
@@ -1041,6 +1027,70 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "FeatureMap",
               "code": 65532,
@@ -1099,13 +1149,45 @@
           ]
         },
         {
-          "name": "Unit Localization",
-          "code": 45,
+          "name": "Localization Configuration",
+          "code": 43,
           "mfgCode": null,
-          "define": "UNIT_LOCALIZATION_CLUSTER",
+          "define": "LOCALIZATION_CONFIGURATION_CLUSTER",
           "side": "server",
           "enabled": 1,
           "attributes": [
+            {
+              "name": "ActiveLocale",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "char_string",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "en-US",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "SupportedLocales",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "GeneratedCommandList",
               "code": 65528,
@@ -1205,163 +1287,269 @@
           ]
         },
         {
-          "name": "Power Source",
-          "code": 47,
+          "name": "Unit Localization",
+          "code": 45,
           "mfgCode": null,
-          "define": "POWER_SOURCE_CLUSTER",
+          "define": "UNIT_LOCALIZATION_CLUSTER",
           "side": "server",
           "enabled": 1,
           "attributes": [
             {
-              "name": "Status",
+              "name": "TemperatureUnit",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "PowerSourceStatusEnum",
+              "type": "TempUnitEnum",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "Order",
-              "code": 1,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "int8u",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "Description",
-              "code": 2,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
-              "type": "char_string",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "BatVoltage",
-              "code": 11,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "BatPercentRemaining",
-              "code": 12,
+              "name": "AttributeList",
+              "code": 65531,
               "mfgCode": null,
               "side": "server",
-              "type": "int8u",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "BatTimeRemaining",
-              "code": 13,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "bitmap32",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": "1",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "BatChargeLevel",
-              "code": 14,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
               "side": "server",
-              "type": "BatChargeLevelEnum",
+              "type": "int16u",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": "1",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
-            },
+            }
+          ]
+        },
+        {
+          "name": "Power Source",
+          "code": 47,
+          "mfgCode": null,
+          "define": "POWER_SOURCE_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
             {
-              "name": "ActiveBatFaults",
-              "code": 18,
+              "name": "Status",
+              "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "PowerSourceStatusEnum",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
               "reportableChange": 0
             },
             {
-              "name": "BatChargeState",
-              "code": 26,
+              "name": "Order",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "BatChargeStateEnum",
+              "type": "int8u",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "",
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
               "reportableChange": 0
             },
             {
-              "name": "EndpointList",
-              "code": 31,
+              "name": "Description",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "char_string",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "Primary Battery",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "BatChargeLevel",
+              "code": 14,
+              "mfgCode": null,
+              "side": "server",
+              "type": "BatChargeLevelEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "BatReplacementNeeded",
+              "code": 15,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "BatReplaceability",
+              "code": 16,
+              "mfgCode": null,
+              "side": "server",
+              "type": "BatReplaceabilityEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "BatChargeState",
+              "code": 26,
+              "mfgCode": null,
+              "side": "server",
+              "type": "BatChargeStateEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "BatFunctionalWhileCharging",
+              "code": 28,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "EndpointList",
+              "code": 31,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -1446,7 +1634,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "6",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -1462,7 +1650,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "2",
+              "defaultValue": "3",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
@@ -1698,7 +1886,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": "2",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
@@ -1916,6 +2104,38 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "SupportedThreadFeatures",
+              "code": 9,
+              "mfgCode": null,
+              "side": "server",
+              "type": "ThreadCapabilitiesBitmap",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "4",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ThreadVersion",
+              "code": 10,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "GeneratedCommandList",
               "code": 65528,
@@ -2006,7 +2226,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": "2",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
@@ -3467,7 +3687,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "2",
+              "defaultValue": "3",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
@@ -3476,109 +3696,61 @@
           ]
         },
         {
-          "name": "Wi-Fi Network Diagnostics",
-          "code": 54,
+          "name": "Administrator Commissioning",
+          "code": 60,
           "mfgCode": null,
-          "define": "WIFI_NETWORK_DIAGNOSTICS_CLUSTER",
+          "define": "ADMINISTRATOR_COMMISSIONING_CLUSTER",
           "side": "server",
           "enabled": 1,
           "commands": [
             {
-              "name": "ResetCounts",
+              "name": "OpenCommissioningWindow",
               "code": 0,
               "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
               "isEnabled": 1
-            }
-          ],
-          "attributes": [
-            {
-              "name": "BSSID",
-              "code": 0,
-              "mfgCode": null,
-              "side": "server",
-              "type": "octet_string",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
-              "reportableChange": 0
             },
             {
-              "name": "SecurityType",
+              "name": "OpenBasicCommissioningWindow",
               "code": 1,
               "mfgCode": null,
-              "side": "server",
-              "type": "SecurityTypeEnum",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
-              "reportableChange": 0
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
             },
             {
-              "name": "WiFiVersion",
+              "name": "RevokeCommissioning",
               "code": 2,
               "mfgCode": null,
-              "side": "server",
-              "type": "WiFiVersionEnum",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
-              "reportableChange": 0
-            },
-            {
-              "name": "ChannelNumber",
-              "code": 3,
-              "mfgCode": null,
-              "side": "server",
-              "type": "int16u",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
-              "reportableChange": 0
-            },
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
             {
-              "name": "RSSI",
-              "code": 4,
+              "name": "WindowStatus",
+              "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "int8s",
+              "type": "CommissioningWindowStatusEnum",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "BeaconLostCount",
-              "code": 5,
+              "name": "AdminFabricIndex",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "fabric_idx",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3590,11 +3762,11 @@
               "reportableChange": 0
             },
             {
-              "name": "BeaconRxCount",
-              "code": 6,
+              "name": "AdminVendorId",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "vendor_id",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3606,11 +3778,11 @@
               "reportableChange": 0
             },
             {
-              "name": "PacketMulticastRxCount",
-              "code": 7,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3622,11 +3794,11 @@
               "reportableChange": 0
             },
             {
-              "name": "PacketMulticastTxCount",
-              "code": 8,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3638,11 +3810,11 @@
               "reportableChange": 0
             },
             {
-              "name": "PacketUnicastRxCount",
-              "code": 9,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3654,11 +3826,11 @@
               "reportableChange": 0
             },
             {
-              "name": "PacketUnicastTxCount",
-              "code": 10,
+              "name": "AttributeList",
+              "code": 65531,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3670,108 +3842,151 @@
               "reportableChange": 0
             },
             {
-              "name": "CurrentMaxRate",
-              "code": 11,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "bitmap32",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "OverrunCount",
-              "code": 12,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
-              "reportable": 1,
-              "minInterval": 1,
-              "maxInterval": 65534,
-              "reportableChange": 0
-            },
-            {
-              "name": "FeatureMap",
-              "code": 65532,
-              "mfgCode": null,
-              "side": "server",
-              "type": "bitmap32",
-              "included": 1,
-              "storageOption": "RAM",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": "3",
-              "reportable": 1,
-              "minInterval": 1,
-              "maxInterval": 65534,
-              "reportableChange": 0
-            },
-            {
-              "name": "ClusterRevision",
-              "code": 65533,
-              "mfgCode": null,
-              "side": "server",
-              "type": "int16u",
-              "included": 1,
-              "storageOption": "RAM",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 0,
               "maxInterval": 65344,
               "reportableChange": 0
             }
-          ],
-          "events": [
+          ]
+        },
+        {
+          "name": "Operational Credentials",
+          "code": 62,
+          "mfgCode": null,
+          "define": "OPERATIONAL_CREDENTIALS_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
             {
-              "name": "Disconnection",
+              "name": "AttestationRequest",
               "code": 0,
               "mfgCode": null,
-              "side": "server",
-              "included": 1
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
             },
             {
-              "name": "AssociationFailure",
+              "name": "AttestationResponse",
               "code": 1,
               "mfgCode": null,
-              "side": "server",
-              "included": 1
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
             },
             {
-              "name": "ConnectionStatus",
+              "name": "CertificateChainRequest",
               "code": 2,
               "mfgCode": null,
-              "side": "server",
-              "included": 1
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "CertificateChainResponse",
+              "code": 3,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "CSRRequest",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "CSRResponse",
+              "code": 5,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddNOC",
+              "code": 6,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "UpdateNOC",
+              "code": 7,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "NOCResponse",
+              "code": 8,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "UpdateFabricLabel",
+              "code": 9,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveFabric",
+              "code": 10,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddTrustedRootCertificate",
+              "code": 11,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
             }
-          ]
-        },
-        {
-          "name": "Ethernet Network Diagnostics",
-          "code": 55,
-          "mfgCode": null,
-          "define": "ETHERNET_NETWORK_DIAGNOSTICS_CLUSTER",
-          "side": "server",
-          "enabled": 1,
+          ],
           "attributes": [
             {
-              "name": "PHYRate",
+              "name": "NOCs",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "PHYRateEnum",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3783,27 +3998,27 @@
               "reportableChange": 0
             },
             {
-              "name": "FullDuplex",
+              "name": "Fabrics",
               "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "boolean",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 1,
-              "maxInterval": 65534,
+              "minInterval": 0,
+              "maxInterval": 65344,
               "reportableChange": 0
             },
             {
-              "name": "PacketRxCount",
+              "name": "SupportedFabrics",
               "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3815,11 +4030,11 @@
               "reportableChange": 0
             },
             {
-              "name": "PacketTxCount",
+              "name": "CommissionedFabrics",
               "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3831,11 +4046,11 @@
               "reportableChange": 0
             },
             {
-              "name": "TxErrCount",
+              "name": "TrustedRootCertificates",
               "code": 4,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3847,43 +4062,43 @@
               "reportableChange": 0
             },
             {
-              "name": "CollisionCount",
+              "name": "CurrentFabricIndex",
               "code": 5,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "OverrunCount",
-              "code": 6,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CarrierDetect",
-              "code": 7,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
-              "type": "boolean",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3895,11 +4110,27 @@
               "reportableChange": 0
             },
             {
-              "name": "TimeSinceReset",
-              "code": 8,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
-              "type": "int64u",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3920,7 +4151,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "3",
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -3945,15 +4176,15 @@
           ]
         },
         {
-          "name": "Administrator Commissioning",
-          "code": 60,
+          "name": "Group Key Management",
+          "code": 63,
           "mfgCode": null,
-          "define": "ADMINISTRATOR_COMMISSIONING_CLUSTER",
+          "define": "GROUP_KEY_MANAGEMENT_CLUSTER",
           "side": "server",
           "enabled": 1,
           "commands": [
             {
-              "name": "OpenCommissioningWindow",
+              "name": "KeySetWrite",
               "code": 0,
               "mfgCode": null,
               "source": "client",
@@ -3961,21 +4192,53 @@
               "isEnabled": 1
             },
             {
-              "name": "RevokeCommissioning",
+              "name": "KeySetRead",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "KeySetReadResponse",
               "code": 2,
               "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "KeySetRemove",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "KeySetReadAllIndices",
+              "code": 4,
+              "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
               "isEnabled": 1
+            },
+            {
+              "name": "KeySetReadAllIndicesResponse",
+              "code": 5,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
             }
           ],
           "attributes": [
             {
-              "name": "WindowStatus",
+              "name": "GroupKeyMap",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "CommissioningWindowStatusEnum",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -3987,11 +4250,11 @@
               "reportableChange": 0
             },
             {
-              "name": "AdminFabricIndex",
+              "name": "GroupTable",
               "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "fabric_idx",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -4003,11 +4266,27 @@
               "reportableChange": 0
             },
             {
-              "name": "AdminVendorId",
+              "name": "MaxGroupsPerFabric",
               "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "vendor_id",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "MaxGroupKeysPerFabric",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -4089,10 +4368,10 @@
               "side": "server",
               "type": "bitmap32",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": null,
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -4105,125 +4384,85 @@
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
         },
         {
-          "name": "Operational Credentials",
-          "code": 62,
+          "name": "Fixed Label",
+          "code": 64,
           "mfgCode": null,
-          "define": "OPERATIONAL_CREDENTIALS_CLUSTER",
+          "define": "FIXED_LABEL_CLUSTER",
           "side": "server",
           "enabled": 1,
-          "commands": [
+          "attributes": [
             {
-              "name": "AttestationRequest",
+              "name": "LabelList",
               "code": 0,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
-            },
-            {
-              "name": "AttestationResponse",
-              "code": 1,
-              "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
-            },
-            {
-              "name": "CertificateChainRequest",
-              "code": 2,
-              "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
-            },
-            {
-              "name": "CertificateChainResponse",
-              "code": 3,
-              "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
-            },
-            {
-              "name": "CSRRequest",
-              "code": 4,
-              "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
-            },
-            {
-              "name": "CSRResponse",
-              "code": 5,
-              "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
-            },
-            {
-              "name": "AddNOC",
-              "code": 6,
-              "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
-            },
-            {
-              "name": "UpdateNOC",
-              "code": 7,
-              "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
-            },
-            {
-              "name": "NOCResponse",
-              "code": 8,
-              "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
-            },
-            {
-              "name": "UpdateFabricLabel",
-              "code": 9,
-              "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "RemoveFabric",
-              "code": 10,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "AddTrustedRootCertificate",
-              "code": 11,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             }
-          ],
+          ]
+        },
+        {
+          "name": "User Label",
+          "code": 65,
+          "mfgCode": null,
+          "define": "USER_LABEL_CLUSTER",
+          "side": "server",
+          "enabled": 1,
           "attributes": [
             {
-              "name": "NOCs",
+              "name": "LabelList",
               "code": 0,
               "mfgCode": null,
               "side": "server",
@@ -4239,75 +4478,85 @@
               "reportableChange": 0
             },
             {
-              "name": "Fabrics",
-              "code": 1,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "bitmap32",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "SupportedFabrics",
-              "code": 2,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
               "side": "server",
-              "type": "int8u",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "1",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
-            },
+            }
+          ]
+        },
+        {
+          "name": "ICD Management",
+          "code": 70,
+          "mfgCode": null,
+          "define": "ICD_MANAGEMENT_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
             {
-              "name": "CommissionedFabrics",
-              "code": 3,
+              "name": "IdleModeDuration",
+              "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "int8u",
+              "type": "int32u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "TrustedRootCertificates",
-              "code": 4,
+              "name": "ActiveModeDuration",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int32u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentFabricIndex",
-              "code": 5,
+              "name": "ActiveModeThreshold",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int8u",
+              "type": "int16u",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -4392,7 +4641,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0x0000",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -4408,74 +4657,2737 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": "3",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
-        },
-        {
-          "name": "Group Key Management",
-          "code": 63,
-          "mfgCode": null,
-          "define": "GROUP_KEY_MANAGEMENT_CLUSTER",
-          "side": "server",
-          "enabled": 1,
-          "commands": [
-            {
-              "name": "KeySetWrite",
+        }
+      ]
+    },
+    {
+      "id": 2,
+      "name": "MA-windowcovering",
+      "deviceTypeRef": {
+        "code": 514,
+        "profileId": 259,
+        "label": "MA-windowcovering",
+        "name": "MA-windowcovering",
+        "deviceTypeOrder": 0
+      },
+      "deviceTypes": [
+        {
+          "code": 514,
+          "profileId": 259,
+          "label": "MA-windowcovering",
+          "name": "MA-windowcovering",
+          "deviceTypeOrder": 0
+        }
+      ],
+      "deviceVersions": [
+        3
+      ],
+      "deviceIdentifiers": [
+        514
+      ],
+      "deviceTypeName": "MA-windowcovering",
+      "deviceTypeCode": 514,
+      "deviceTypeProfileId": 259,
+      "clusters": [
+        {
+          "name": "Identify",
+          "code": 3,
+          "mfgCode": null,
+          "define": "IDENTIFY_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "Identify",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "TriggerEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "IdentifyTime",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "IdentifyType",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "IdentifyTypeEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x05",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Groups",
+          "code": 4,
+          "mfgCode": null,
+          "define": "GROUPS_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "AddGroup",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupResponse",
+              "code": 0,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroup",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroupResponse",
+              "code": 1,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembership",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembershipResponse",
+              "code": 2,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroup",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroupResponse",
+              "code": 3,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveAllGroups",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupIfIdentifying",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "NameSupport",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "NameSupportBitmap",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "4",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Descriptor",
+          "code": 29,
+          "mfgCode": null,
+          "define": "DESCRIPTOR_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
+            {
+              "name": "DeviceTypeList",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ServerList",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClientList",
+              "code": 2,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "PartsList",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Window Covering",
+          "code": 258,
+          "mfgCode": null,
+          "define": "WINDOW_COVERING_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "UpOrOpen",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "DownOrClose",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StopMotion",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GoToLiftValue",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GoToLiftPercentage",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "Type",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "Type",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x08",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "PhysicalClosedLimitLift",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFFFF",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65535,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLift",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "NumberOfActuationsLift",
+              "code": 5,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65535,
+              "reportableChange": 0
+            },
+            {
+              "name": "ConfigStatus",
+              "code": 7,
+              "mfgCode": null,
+              "side": "server",
+              "type": "ConfigStatus",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x01",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLiftPercentage",
+              "code": 8,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "OperationalStatus",
+              "code": 10,
+              "mfgCode": null,
+              "side": "server",
+              "type": "OperationalStatus",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "TargetPositionLiftPercent100ths",
+              "code": 11,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent100ths",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "EndProductType",
+              "code": 13,
+              "mfgCode": null,
+              "side": "server",
+              "type": "EndProductType",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLiftPercent100ths",
+              "code": 14,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent100ths",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "InstalledOpenLimitLift",
+              "code": 16,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "InstalledClosedLimitLift",
+              "code": 17,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFFFF",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "Mode",
+              "code": 23,
+              "mfgCode": null,
+              "side": "server",
+              "type": "Mode",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "SafetyStatus",
+              "code": 26,
+              "mfgCode": null,
+              "side": "server",
+              "type": "SafetyStatus",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x000D",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        }
+      ]
+    },
+    {
+      "id": 3,
+      "name": "MA-windowcovering",
+      "deviceTypeRef": {
+        "code": 514,
+        "profileId": 259,
+        "label": "MA-windowcovering",
+        "name": "MA-windowcovering",
+        "deviceTypeOrder": 0
+      },
+      "deviceTypes": [
+        {
+          "code": 514,
+          "profileId": 259,
+          "label": "MA-windowcovering",
+          "name": "MA-windowcovering",
+          "deviceTypeOrder": 0
+        }
+      ],
+      "deviceVersions": [
+        3
+      ],
+      "deviceIdentifiers": [
+        514
+      ],
+      "deviceTypeName": "MA-windowcovering",
+      "deviceTypeCode": 514,
+      "deviceTypeProfileId": 259,
+      "clusters": [
+        {
+          "name": "Identify",
+          "code": 3,
+          "mfgCode": null,
+          "define": "IDENTIFY_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "Identify",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "TriggerEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "IdentifyTime",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "IdentifyType",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "IdentifyTypeEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x05",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Groups",
+          "code": 4,
+          "mfgCode": null,
+          "define": "GROUPS_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "AddGroup",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupResponse",
+              "code": 0,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroupResponse",
+              "code": 1,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroup",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembership",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembershipResponse",
+              "code": 2,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroupResponse",
+              "code": 3,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroup",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveAllGroups",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupIfIdentifying",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "NameSupport",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "NameSupportBitmap",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "4",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Descriptor",
+          "code": 29,
+          "mfgCode": null,
+          "define": "DESCRIPTOR_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
+            {
+              "name": "DeviceTypeList",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ServerList",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClientList",
+              "code": 2,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "PartsList",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Window Covering",
+          "code": 258,
+          "mfgCode": null,
+          "define": "WINDOW_COVERING_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "UpOrOpen",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "DownOrClose",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StopMotion",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GoToLiftValue",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GoToLiftPercentage",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "Type",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "Type",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x08",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "PhysicalClosedLimitLift",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFFFF",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65535,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLift",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "NumberOfActuationsLift",
+              "code": 5,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65535,
+              "reportableChange": 0
+            },
+            {
+              "name": "ConfigStatus",
+              "code": 7,
+              "mfgCode": null,
+              "side": "server",
+              "type": "ConfigStatus",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x03",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLiftPercentage",
+              "code": 8,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "OperationalStatus",
+              "code": 10,
+              "mfgCode": null,
+              "side": "server",
+              "type": "OperationalStatus",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "TargetPositionLiftPercent100ths",
+              "code": 11,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent100ths",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "EndProductType",
+              "code": 13,
+              "mfgCode": null,
+              "side": "server",
+              "type": "EndProductType",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "CurrentPositionLiftPercent100ths",
+              "code": 14,
+              "mfgCode": null,
+              "side": "server",
+              "type": "percent100ths",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "InstalledOpenLimitLift",
+              "code": 16,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "InstalledClosedLimitLift",
+              "code": 17,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFFFF",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "Mode",
+              "code": 23,
+              "mfgCode": null,
+              "side": "server",
+              "type": "Mode",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "SafetyStatus",
+              "code": 26,
+              "mfgCode": null,
+              "side": "server",
+              "type": "SafetyStatus",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x000D",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 0,
+              "maxInterval": 65344,
+              "reportableChange": 0
+            }
+          ]
+        }
+      ]
+    },
+    {
+      "id": 4,
+      "name": "Anonymous Endpoint Type",
+      "deviceTypeRef": {
+        "code": 269,
+        "profileId": 259,
+        "label": "MA-extendedcolorlight",
+        "name": "MA-extendedcolorlight",
+        "deviceTypeOrder": 0
+      },
+      "deviceTypes": [
+        {
+          "code": 269,
+          "profileId": 259,
+          "label": "MA-extendedcolorlight",
+          "name": "MA-extendedcolorlight",
+          "deviceTypeOrder": 0
+        }
+      ],
+      "deviceVersions": [
+        4
+      ],
+      "deviceIdentifiers": [
+        269
+      ],
+      "deviceTypeName": "MA-extendedcolorlight",
+      "deviceTypeCode": 269,
+      "deviceTypeProfileId": 259,
+      "clusters": [
+        {
+          "name": "Identify",
+          "code": 3,
+          "mfgCode": null,
+          "define": "IDENTIFY_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "Identify",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "TriggerEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "IdentifyTime",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "IdentifyType",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "IdentifyTypeEnum",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "5",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Groups",
+          "code": 4,
+          "mfgCode": null,
+          "define": "GROUPS_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "AddGroup",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupResponse",
+              "code": 0,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroupResponse",
+              "code": 1,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "ViewGroup",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembership",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "GetGroupMembershipResponse",
+              "code": 2,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroup",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveGroupResponse",
+              "code": 3,
+              "mfgCode": null,
+              "source": "server",
+              "isIncoming": 0,
+              "isEnabled": 1
+            },
+            {
+              "name": "RemoveAllGroups",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "AddGroupIfIdentifying",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "NameSupport",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "NameSupportBitmap",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "4",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "On/Off",
+          "code": 6,
+          "mfgCode": null,
+          "define": "ON_OFF_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "Off",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "On",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Toggle",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OffWithEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithRecallGlobalScene",
+              "code": 65,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithTimedOff",
+              "code": 66,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "OnOff",
+              "code": 0,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 0,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GlobalSceneControl",
+              "code": 16384,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OnTime",
+              "code": 16385,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OffWaitTime",
+              "code": 16386,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "StartUpOnOff",
+              "code": 16387,
+              "mfgCode": null,
+              "side": "server",
+              "type": "StartUpOnOffEnum",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AcceptedCommandList",
+              "code": 65529,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "AttributeList",
+              "code": 65531,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "FeatureMap",
+              "code": 65532,
+              "mfgCode": null,
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "ClusterRevision",
+              "code": 65533,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "6",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            }
+          ]
+        },
+        {
+          "name": "Level Control",
+          "code": 8,
+          "mfgCode": null,
+          "define": "LEVEL_CONTROL_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "commands": [
+            {
+              "name": "MoveToLevel",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Move",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Step",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Stop",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveToLevelWithOnOff",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveWithOnOff",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StepWithOnOff",
+              "code": 6,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StopWithOnOff",
+              "code": 7,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
+          "attributes": [
+            {
+              "name": "CurrentLevel",
               "code": 0,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x01",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "RemainingTime",
+              "code": 1,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "MinLevel",
+              "code": 2,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x01",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "MaxLevel",
+              "code": 3,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFE",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "Options",
+              "code": 15,
+              "mfgCode": null,
+              "side": "server",
+              "type": "OptionsBitmap",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x00",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OnOffTransitionTime",
+              "code": 16,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0x0000",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OnLevel",
+              "code": 17,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFE",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OnTransitionTime",
+              "code": 18,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "OffTransitionTime",
+              "code": 19,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "DefaultMoveRate",
+              "code": 20,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "50",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "StartUpCurrentLevel",
+              "code": 16384,
+              "mfgCode": null,
+              "side": "server",
+              "type": "int8u",
+              "included": 1,
+              "storageOption": "NVM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "0xFE",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GeneratedCommandList",
+              "code": 65528,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "KeySetRead",
-              "code": 1,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "KeySetReadResponse",
-              "code": 2,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "KeySetRemove",
-              "code": 3,
+              "name": "AttributeList",
+              "code": 65531,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "KeySetReadAllIndices",
-              "code": 4,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
-              "source": "client",
-              "isIncoming": 1,
-              "isEnabled": 1
+              "side": "server",
+              "type": "bitmap32",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "3",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             },
             {
-              "name": "KeySetReadAllIndicesResponse",
-              "code": 5,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
-              "source": "server",
-              "isIncoming": 0,
-              "isEnabled": 1
+              "side": "server",
+              "type": "int16u",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "6",
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
             }
-          ],
+          ]
+        },
+        {
+          "name": "Descriptor",
+          "code": 29,
+          "mfgCode": null,
+          "define": "DESCRIPTOR_CLUSTER",
+          "side": "server",
+          "enabled": 1,
           "attributes": [
             {
-              "name": "GroupKeyMap",
+              "name": "DeviceTypeList",
               "code": 0,
               "mfgCode": null,
               "side": "server",
@@ -4491,7 +7403,7 @@
               "reportableChange": 0
             },
             {
-              "name": "GroupTable",
+              "name": "ServerList",
               "code": 1,
               "mfgCode": null,
               "side": "server",
@@ -4507,11 +7419,11 @@
               "reportableChange": 0
             },
             {
-              "name": "MaxGroupsPerFabric",
+              "name": "ClientList",
               "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -4523,11 +7435,11 @@
               "reportableChange": 0
             },
             {
-              "name": "MaxGroupKeysPerFabric",
+              "name": "PartsList",
               "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
               "storageOption": "External",
               "singleton": 0,
@@ -4637,48 +7549,114 @@
           ]
         },
         {
-          "name": "Fixed Label",
-          "code": 64,
+          "name": "Color Control",
+          "code": 768,
           "mfgCode": null,
-          "define": "FIXED_LABEL_CLUSTER",
+          "define": "COLOR_CONTROL_CLUSTER",
           "side": "server",
           "enabled": 1,
+          "commands": [
+            {
+              "name": "MoveToHue",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveHue",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StepHue",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveToSaturation",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveSaturation",
+              "code": 4,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StepSaturation",
+              "code": 5,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveToHueAndSaturation",
+              "code": 6,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "StopMoveStep",
+              "code": 71,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
           "attributes": [
             {
-              "name": "LabelList",
+              "name": "CurrentHue",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "FeatureMap",
-              "code": 65532,
+              "name": "CurrentSaturation",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "bitmap32",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ClusterRevision",
-              "code": 65533,
+              "name": "RemainingTime",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
               "type": "int16u",
@@ -4686,123 +7664,87 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
-              "reportable": 1,
-              "minInterval": 1,
-              "maxInterval": 65534,
-              "reportableChange": 0
-            }
-          ]
-        },
-        {
-          "name": "User Label",
-          "code": 65,
-          "mfgCode": null,
-          "define": "USER_LABEL_CLUSTER",
-          "side": "server",
-          "enabled": 1,
-          "attributes": [
-            {
-              "name": "LabelList",
-              "code": 0,
-              "mfgCode": null,
-              "side": "server",
-              "type": "array",
-              "included": 1,
-              "storageOption": "External",
-              "singleton": 0,
-              "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0x0000",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "FeatureMap",
-              "code": 65532,
+              "name": "ColorMode",
+              "code": 8,
               "mfgCode": null,
               "side": "server",
-              "type": "bitmap32",
+              "type": "ColorModeEnum",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ClusterRevision",
-              "code": 65533,
+              "name": "Options",
+              "code": 15,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "OptionsBitmap",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "1",
+              "defaultValue": "0x01",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
-            }
-          ]
-        },
-        {
-          "name": "ICD Management",
-          "code": 70,
-          "mfgCode": null,
-          "define": "ICD_MANAGEMENT_CLUSTER",
-          "side": "server",
-          "enabled": 1,
-          "attributes": [
+            },
             {
-              "name": "IdleModeDuration",
-              "code": 0,
+              "name": "NumberOfPrimaries",
+              "code": 16,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ActiveModeDuration",
-              "code": 1,
+              "name": "EnhancedColorMode",
+              "code": 16385,
               "mfgCode": null,
               "side": "server",
-              "type": "int32u",
+              "type": "EnhancedColorModeEnum",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ActiveModeThreshold",
-              "code": 2,
+              "name": "ColorCapabilities",
+              "code": 16394,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "ColorCapabilitiesBitmap",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0x01",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -4882,7 +7824,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": "0x01",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -4898,7 +7840,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "3",
+              "defaultValue": "7",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -4909,32 +7851,32 @@
       ]
     },
     {
-      "id": 2,
-      "name": "MA-windowcovering",
+      "id": 5,
+      "name": "Anonymous Endpoint Type",
       "deviceTypeRef": {
-        "code": 514,
+        "code": 257,
         "profileId": 259,
-        "label": "MA-windowcovering",
-        "name": "MA-windowcovering",
+        "label": "MA-dimmablelight",
+        "name": "MA-dimmablelight",
         "deviceTypeOrder": 0
       },
       "deviceTypes": [
         {
-          "code": 514,
+          "code": 257,
           "profileId": 259,
-          "label": "MA-windowcovering",
-          "name": "MA-windowcovering",
+          "label": "MA-dimmablelight",
+          "name": "MA-dimmablelight",
           "deviceTypeOrder": 0
         }
       ],
       "deviceVersions": [
-        2
+        1
       ],
       "deviceIdentifiers": [
-        514
+        257
       ],
-      "deviceTypeName": "MA-windowcovering",
-      "deviceTypeCode": 514,
+      "deviceTypeName": "MA-dimmablelight",
+      "deviceTypeCode": 257,
       "deviceTypeProfileId": 259,
       "clusters": [
         {
@@ -4989,7 +7931,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x05",
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -5027,6 +7969,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -5069,10 +8027,10 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "4",
+              "defaultValue": "5",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
@@ -5179,8 +8137,8 @@
               "bounded": 0,
               "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
@@ -5215,6 +8173,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -5241,7 +8215,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -5259,79 +8233,145 @@
               "bounded": 0,
               "defaultValue": "4",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
         },
         {
-          "name": "Descriptor",
-          "code": 29,
+          "name": "On/Off",
+          "code": 6,
           "mfgCode": null,
-          "define": "DESCRIPTOR_CLUSTER",
+          "define": "ON_OFF_CLUSTER",
           "side": "server",
           "enabled": 1,
+          "commands": [
+            {
+              "name": "Off",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "On",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Toggle",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OffWithEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithRecallGlobalScene",
+              "code": 65,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithTimedOff",
+              "code": 66,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
           "attributes": [
             {
-              "name": "DeviceTypeList",
+              "name": "OnOff",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "boolean",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
+              "reportable": 0,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GlobalSceneControl",
+              "code": 16384,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ServerList",
-              "code": 1,
+              "name": "OnTime",
+              "code": 16385,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ClientList",
-              "code": 2,
+              "name": "OffWaitTime",
+              "code": 16386,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PartsList",
-              "code": 3,
+              "name": "StartUpOnOff",
+              "code": 16387,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "StartUpOnOffEnum",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -5369,6 +8409,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -5392,10 +8448,10 @@
               "side": "server",
               "type": "bitmap32",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -5408,10 +8464,10 @@
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "6",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -5420,15 +8476,15 @@
           ]
         },
         {
-          "name": "Window Covering",
-          "code": 258,
+          "name": "Level Control",
+          "code": 8,
           "mfgCode": null,
-          "define": "WINDOW_COVERING_CLUSTER",
+          "define": "LEVEL_CONTROL_CLUSTER",
           "side": "server",
           "enabled": 1,
           "commands": [
             {
-              "name": "UpOrOpen",
+              "name": "MoveToLevel",
               "code": 0,
               "mfgCode": null,
               "source": "client",
@@ -5436,7 +8492,7 @@
               "isEnabled": 1
             },
             {
-              "name": "DownOrClose",
+              "name": "Move",
               "code": 1,
               "mfgCode": null,
               "source": "client",
@@ -5444,7 +8500,7 @@
               "isEnabled": 1
             },
             {
-              "name": "StopMotion",
+              "name": "Step",
               "code": 2,
               "mfgCode": null,
               "source": "client",
@@ -5452,7 +8508,15 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToLiftValue",
+              "name": "Stop",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveToLevelWithOnOff",
               "code": 4,
               "mfgCode": null,
               "source": "client",
@@ -5460,7 +8524,7 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToLiftPercentage",
+              "name": "MoveWithOnOff",
               "code": 5,
               "mfgCode": null,
               "source": "client",
@@ -5468,16 +8532,16 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToTiltValue",
-              "code": 7,
+              "name": "StepWithOnOff",
+              "code": 6,
               "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
               "isEnabled": 1
             },
             {
-              "name": "GoToTiltPercentage",
-              "code": 8,
+              "name": "StopWithOnOff",
+              "code": 7,
               "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
@@ -5486,23 +8550,23 @@
           ],
           "attributes": [
             {
-              "name": "Type",
+              "name": "CurrentLevel",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "Type",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x08",
+              "defaultValue": "0x01",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PhysicalClosedLimitLift",
+              "name": "RemainingTime",
               "code": 1,
               "mfgCode": null,
               "side": "server",
@@ -5511,335 +8575,345 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": "0x0000",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PhysicalClosedLimitTilt",
+              "name": "MinLevel",
               "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": "0x01",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLift",
+              "name": "MaxLevel",
               "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTilt",
-              "code": 4,
+              "name": "Options",
+              "code": 15,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "OptionsBitmap",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0x00",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "NumberOfActuationsLift",
-              "code": 5,
+              "name": "OnOffTransitionTime",
+              "code": 16,
               "mfgCode": null,
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": "0x0000",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "NumberOfActuationsTilt",
-              "code": 6,
+              "name": "OnLevel",
+              "code": 17,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ConfigStatus",
-              "code": 7,
+              "name": "OnTransitionTime",
+              "code": 18,
               "mfgCode": null,
               "side": "server",
-              "type": "ConfigStatus",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x03",
+              "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLiftPercentage",
-              "code": 8,
+              "name": "OffTransitionTime",
+              "code": 19,
               "mfgCode": null,
               "side": "server",
-              "type": "percent",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTiltPercentage",
-              "code": 9,
+              "name": "DefaultMoveRate",
+              "code": 20,
               "mfgCode": null,
               "side": "server",
-              "type": "percent",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "50",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "OperationalStatus",
-              "code": 10,
+              "name": "StartUpCurrentLevel",
+              "code": 16384,
               "mfgCode": null,
               "side": "server",
-              "type": "OperationalStatus",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x00",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "TargetPositionLiftPercent100ths",
-              "code": 11,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "TargetPositionTiltPercent100ths",
-              "code": 12,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "EndProductType",
-              "code": 13,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
-              "type": "EndProductType",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x00",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLiftPercent100ths",
-              "code": 14,
+              "name": "AttributeList",
+              "code": 65531,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTiltPercent100ths",
-              "code": 15,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "bitmap32",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "3",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledOpenLimitLift",
-              "code": 16,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": "6",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
-            },
+            }
+          ]
+        },
+        {
+          "name": "Descriptor",
+          "code": 29,
+          "mfgCode": null,
+          "define": "DESCRIPTOR_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
             {
-              "name": "InstalledClosedLimitLift",
-              "code": 17,
+              "name": "DeviceTypeList",
+              "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledOpenLimitTilt",
-              "code": 18,
+              "name": "ServerList",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledClosedLimitTilt",
-              "code": 19,
+              "name": "ClientList",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "Mode",
-              "code": 23,
+              "name": "PartsList",
+              "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "Mode",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "SafetyStatus",
-              "code": 26,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "SafetyStatus",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "GeneratedCommandList",
-              "code": 65528,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
               "type": "array",
@@ -5854,8 +8928,8 @@
               "reportableChange": 0
             },
             {
-              "name": "AcceptedCommandList",
-              "code": 65529,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
               "type": "array",
@@ -5892,13 +8966,13 @@
               "side": "server",
               "type": "bitmap32",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x001F",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
@@ -5908,13 +8982,13 @@
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "5",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
@@ -5922,32 +8996,32 @@
       ]
     },
     {
-      "id": 3,
-      "name": "MA-windowcovering",
+      "id": 6,
+      "name": "Anonymous Endpoint Type",
       "deviceTypeRef": {
-        "code": 514,
+        "code": 257,
         "profileId": 259,
-        "label": "MA-windowcovering",
-        "name": "MA-windowcovering",
+        "label": "MA-dimmablelight",
+        "name": "MA-dimmablelight",
         "deviceTypeOrder": 0
       },
       "deviceTypes": [
         {
-          "code": 514,
+          "code": 257,
           "profileId": 259,
-          "label": "MA-windowcovering",
-          "name": "MA-windowcovering",
+          "label": "MA-dimmablelight",
+          "name": "MA-dimmablelight",
           "deviceTypeOrder": 0
         }
       ],
       "deviceVersions": [
-        2
+        1
       ],
       "deviceIdentifiers": [
-        514
+        257
       ],
-      "deviceTypeName": "MA-windowcovering",
-      "deviceTypeCode": 514,
+      "deviceTypeName": "MA-dimmablelight",
+      "deviceTypeCode": 257,
       "deviceTypeProfileId": 259,
       "clusters": [
         {
@@ -5965,6 +9039,14 @@
               "source": "client",
               "isIncoming": 1,
               "isEnabled": 1
+            },
+            {
+              "name": "TriggerEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
             }
           ],
           "attributes": [
@@ -5994,7 +9076,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x05",
+              "defaultValue": "0x00",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -6032,6 +9114,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -6074,10 +9172,10 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "4",
+              "defaultValue": "5",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
@@ -6184,8 +9282,8 @@
               "bounded": 0,
               "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
@@ -6220,6 +9318,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -6246,7 +9360,7 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -6264,79 +9378,145 @@
               "bounded": 0,
               "defaultValue": "4",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
         },
         {
-          "name": "Descriptor",
-          "code": 29,
+          "name": "On/Off",
+          "code": 6,
           "mfgCode": null,
-          "define": "DESCRIPTOR_CLUSTER",
+          "define": "ON_OFF_CLUSTER",
           "side": "server",
           "enabled": 1,
+          "commands": [
+            {
+              "name": "Off",
+              "code": 0,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "On",
+              "code": 1,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "Toggle",
+              "code": 2,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OffWithEffect",
+              "code": 64,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithRecallGlobalScene",
+              "code": 65,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "OnWithTimedOff",
+              "code": 66,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            }
+          ],
           "attributes": [
             {
-              "name": "DeviceTypeList",
+              "name": "OnOff",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "boolean",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
+              "reportable": 0,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
+            {
+              "name": "GlobalSceneControl",
+              "code": 16384,
+              "mfgCode": null,
+              "side": "server",
+              "type": "boolean",
+              "included": 1,
+              "storageOption": "RAM",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ServerList",
-              "code": 1,
+              "name": "OnTime",
+              "code": 16385,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ClientList",
-              "code": 2,
+              "name": "OffWaitTime",
+              "code": 16386,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PartsList",
-              "code": 3,
+              "name": "StartUpOnOff",
+              "code": 16387,
               "mfgCode": null,
               "side": "server",
-              "type": "array",
+              "type": "StartUpOnOffEnum",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "0",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -6374,6 +9554,22 @@
               "maxInterval": 65534,
               "reportableChange": 0
             },
+            {
+              "name": "EventList",
+              "code": 65530,
+              "mfgCode": null,
+              "side": "server",
+              "type": "array",
+              "included": 1,
+              "storageOption": "External",
+              "singleton": 0,
+              "bounded": 0,
+              "defaultValue": null,
+              "reportable": 1,
+              "minInterval": 1,
+              "maxInterval": 65534,
+              "reportableChange": 0
+            },
             {
               "name": "AttributeList",
               "code": 65531,
@@ -6397,10 +9593,10 @@
               "side": "server",
               "type": "bitmap32",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "1",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -6413,10 +9609,10 @@
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "External",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": null,
+              "defaultValue": "6",
               "reportable": 1,
               "minInterval": 1,
               "maxInterval": 65534,
@@ -6425,15 +9621,15 @@
           ]
         },
         {
-          "name": "Window Covering",
-          "code": 258,
+          "name": "Level Control",
+          "code": 8,
           "mfgCode": null,
-          "define": "WINDOW_COVERING_CLUSTER",
+          "define": "LEVEL_CONTROL_CLUSTER",
           "side": "server",
           "enabled": 1,
           "commands": [
             {
-              "name": "UpOrOpen",
+              "name": "MoveToLevel",
               "code": 0,
               "mfgCode": null,
               "source": "client",
@@ -6441,7 +9637,7 @@
               "isEnabled": 1
             },
             {
-              "name": "DownOrClose",
+              "name": "Move",
               "code": 1,
               "mfgCode": null,
               "source": "client",
@@ -6449,7 +9645,7 @@
               "isEnabled": 1
             },
             {
-              "name": "StopMotion",
+              "name": "Step",
               "code": 2,
               "mfgCode": null,
               "source": "client",
@@ -6457,7 +9653,15 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToLiftValue",
+              "name": "Stop",
+              "code": 3,
+              "mfgCode": null,
+              "source": "client",
+              "isIncoming": 1,
+              "isEnabled": 1
+            },
+            {
+              "name": "MoveToLevelWithOnOff",
               "code": 4,
               "mfgCode": null,
               "source": "client",
@@ -6465,7 +9669,7 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToLiftPercentage",
+              "name": "MoveWithOnOff",
               "code": 5,
               "mfgCode": null,
               "source": "client",
@@ -6473,16 +9677,16 @@
               "isEnabled": 1
             },
             {
-              "name": "GoToTiltValue",
-              "code": 7,
+              "name": "StepWithOnOff",
+              "code": 6,
               "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
               "isEnabled": 1
             },
             {
-              "name": "GoToTiltPercentage",
-              "code": 8,
+              "name": "StopWithOnOff",
+              "code": 7,
               "mfgCode": null,
               "source": "client",
               "isIncoming": 1,
@@ -6491,23 +9695,23 @@
           ],
           "attributes": [
             {
-              "name": "Type",
+              "name": "CurrentLevel",
               "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "Type",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x08",
+              "defaultValue": "0x01",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PhysicalClosedLimitLift",
+              "name": "RemainingTime",
               "code": 1,
               "mfgCode": null,
               "side": "server",
@@ -6516,335 +9720,345 @@
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": "0x0000",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "PhysicalClosedLimitTilt",
+              "name": "MinLevel",
               "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": "0x01",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLift",
+              "name": "MaxLevel",
               "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTilt",
-              "code": 4,
+              "name": "Options",
+              "code": 15,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "OptionsBitmap",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "0x00",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "NumberOfActuationsLift",
-              "code": 5,
+              "name": "OnOffTransitionTime",
+              "code": 16,
               "mfgCode": null,
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": "0x0000",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "NumberOfActuationsTilt",
-              "code": 6,
+              "name": "OnLevel",
+              "code": 17,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "int8u",
               "included": 1,
               "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65535,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "ConfigStatus",
-              "code": 7,
+              "name": "OnTransitionTime",
+              "code": 18,
               "mfgCode": null,
               "side": "server",
-              "type": "ConfigStatus",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x03",
+              "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLiftPercentage",
-              "code": 8,
+              "name": "OffTransitionTime",
+              "code": 19,
               "mfgCode": null,
               "side": "server",
-              "type": "percent",
+              "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTiltPercentage",
-              "code": 9,
+              "name": "DefaultMoveRate",
+              "code": 20,
               "mfgCode": null,
               "side": "server",
-              "type": "percent",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "50",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "OperationalStatus",
-              "code": 10,
+              "name": "StartUpCurrentLevel",
+              "code": 16384,
               "mfgCode": null,
               "side": "server",
-              "type": "OperationalStatus",
+              "type": "int8u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "NVM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x00",
+              "defaultValue": "0xFE",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "TargetPositionLiftPercent100ths",
-              "code": 11,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "TargetPositionTiltPercent100ths",
-              "code": 12,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
               "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "EndProductType",
-              "code": 13,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
-              "type": "EndProductType",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x00",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionLiftPercent100ths",
-              "code": 14,
+              "name": "AttributeList",
+              "code": 65531,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "CurrentPositionTiltPercent100ths",
-              "code": 15,
+              "name": "FeatureMap",
+              "code": 65532,
               "mfgCode": null,
               "side": "server",
-              "type": "percent100ths",
+              "type": "bitmap32",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0",
+              "defaultValue": "3",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledOpenLimitLift",
-              "code": 16,
+              "name": "ClusterRevision",
+              "code": 65533,
               "mfgCode": null,
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "RAM",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": "6",
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
-            },
+            }
+          ]
+        },
+        {
+          "name": "Descriptor",
+          "code": 29,
+          "mfgCode": null,
+          "define": "DESCRIPTOR_CLUSTER",
+          "side": "server",
+          "enabled": 1,
+          "attributes": [
             {
-              "name": "InstalledClosedLimitLift",
-              "code": 17,
+              "name": "DeviceTypeList",
+              "code": 0,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledOpenLimitTilt",
-              "code": 18,
+              "name": "ServerList",
+              "code": 1,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "InstalledClosedLimitTilt",
-              "code": 19,
+              "name": "ClientList",
+              "code": 2,
               "mfgCode": null,
               "side": "server",
-              "type": "int16u",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0xFFFF",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "Mode",
-              "code": 23,
+              "name": "PartsList",
+              "code": 3,
               "mfgCode": null,
               "side": "server",
-              "type": "Mode",
+              "type": "array",
               "included": 1,
-              "storageOption": "NVM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x00",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "SafetyStatus",
-              "code": 26,
+              "name": "GeneratedCommandList",
+              "code": 65528,
               "mfgCode": null,
               "side": "server",
-              "type": "SafetyStatus",
+              "type": "array",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0000",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
-              "name": "GeneratedCommandList",
-              "code": 65528,
+              "name": "AcceptedCommandList",
+              "code": 65529,
               "mfgCode": null,
               "side": "server",
               "type": "array",
@@ -6859,8 +10073,8 @@
               "reportableChange": 0
             },
             {
-              "name": "AcceptedCommandList",
-              "code": 65529,
+              "name": "EventList",
+              "code": 65530,
               "mfgCode": null,
               "side": "server",
               "type": "array",
@@ -6897,13 +10111,13 @@
               "side": "server",
               "type": "bitmap32",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "0x0017",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             },
             {
@@ -6913,13 +10127,13 @@
               "side": "server",
               "type": "int16u",
               "included": 1,
-              "storageOption": "RAM",
+              "storageOption": "External",
               "singleton": 0,
               "bounded": 0,
-              "defaultValue": "5",
+              "defaultValue": null,
               "reportable": 1,
-              "minInterval": 0,
-              "maxInterval": 65344,
+              "minInterval": 1,
+              "maxInterval": 65534,
               "reportableChange": 0
             }
           ]
@@ -6951,6 +10165,30 @@
       "endpointId": 2,
       "networkId": 0,
       "parentEndpointIdentifier": null
+    },
+    {
+      "endpointTypeName": "Anonymous Endpoint Type",
+      "endpointTypeIndex": 3,
+      "profileId": 259,
+      "endpointId": 3,
+      "networkId": 0,
+      "parentEndpointIdentifier": null
+    },
+    {
+      "endpointTypeName": "Anonymous Endpoint Type",
+      "endpointTypeIndex": 4,
+      "profileId": 259,
+      "endpointId": 4,
+      "networkId": 0,
+      "parentEndpointIdentifier": null
+    },
+    {
+      "endpointTypeName": "Anonymous Endpoint Type",
+      "endpointTypeIndex": 5,
+      "profileId": 259,
+      "endpointId": 5,
+      "networkId": 0,
+      "parentEndpointIdentifier": null
     }
   ]
 }
\ No newline at end of file
diff --git a/config/pin_config.h b/config/pin_config.h
index c4805a1..1028f17 100644
--- a/config/pin_config.h
+++ b/config/pin_config.h
@@ -92,6 +92,22 @@
 // [I2C1]$
 
 // $[EUSART1]
+// EUSART1 RX on PA08
+#ifndef EUSART1_RX_PORT                         
+#define EUSART1_RX_PORT                          SL_GPIO_PORT_A
+#endif
+#ifndef EUSART1_RX_PIN                          
+#define EUSART1_RX_PIN                           8
+#endif
+
+// EUSART1 TX on PA07
+#ifndef EUSART1_TX_PORT                         
+#define EUSART1_TX_PORT                          SL_GPIO_PORT_A
+#endif
+#ifndef EUSART1_TX_PIN                          
+#define EUSART1_TX_PIN                           7
+#endif
+
 // [EUSART1]$
 
 // $[KEYSCAN]
@@ -125,41 +141,33 @@
 // [I2C0]$
 
 // $[EUSART0]
-// EUSART0 CTS on PA02
-#ifndef EUSART0_CTS_PORT                        
-#define EUSART0_CTS_PORT                         SL_GPIO_PORT_A
-#endif
-#ifndef EUSART0_CTS_PIN                         
-#define EUSART0_CTS_PIN                          2
-#endif
-
-// EUSART0 RTS on PA03
-#ifndef EUSART0_RTS_PORT                        
-#define EUSART0_RTS_PORT                         SL_GPIO_PORT_A
-#endif
-#ifndef EUSART0_RTS_PIN                         
-#define EUSART0_RTS_PIN                          3
-#endif
-
-// EUSART0 RX on PA01
+// EUSART0 RX on PB02
 #ifndef EUSART0_RX_PORT                         
-#define EUSART0_RX_PORT                          SL_GPIO_PORT_A
+#define EUSART0_RX_PORT                          SL_GPIO_PORT_B
 #endif
 #ifndef EUSART0_RX_PIN                          
-#define EUSART0_RX_PIN                           1
+#define EUSART0_RX_PIN                           2
 #endif
 
-// EUSART0 TX on PA00
+// EUSART0 TX on PB01
 #ifndef EUSART0_TX_PORT                         
-#define EUSART0_TX_PORT                          SL_GPIO_PORT_A
+#define EUSART0_TX_PORT                          SL_GPIO_PORT_B
 #endif
 #ifndef EUSART0_TX_PIN                          
-#define EUSART0_TX_PIN                           0
+#define EUSART0_TX_PIN                           1
 #endif
 
 // [EUSART0]$
 
 // $[PTI]
+// PTI DCLK on PC00
+#ifndef PTI_DCLK_PORT                           
+#define PTI_DCLK_PORT                            SL_GPIO_PORT_C
+#endif
+#ifndef PTI_DCLK_PIN                            
+#define PTI_DCLK_PIN                             0
+#endif
+
 // [PTI]$
 
 // $[MODEM]
diff --git a/config/sl_openthread_ble_cli_config.h b/config/sl_bt_accept_list_config.h
similarity index 56%
rename from config/sl_openthread_ble_cli_config.h
rename to config/sl_bt_accept_list_config.h
index 9657f16..afbf290 100644
--- a/config/sl_openthread_ble_cli_config.h
+++ b/config/sl_bt_accept_list_config.h
@@ -1,36 +1,47 @@
-/*******************************************************************************
- * @file
- * @brief OpenThread Bluetooth CLI configuration file.
- *******************************************************************************
- * # License
- * <b>Copyright 2024 Silicon Laboratories Inc. www.silabs.com</b>
- *******************************************************************************
- *
- * SPDX-License-Identifier: Zlib
- *
- * The licensor of this software is Silicon Laboratories Inc.
- *
- * This software is provided 'as-is', without any express or implied
- * warranty. In no event will the authors be held liable for any damages
- * arising from the use of this software.
- *
- * Permission is granted to anyone to use this software for any purpose,
- * including commercial applications, and to alter it and redistribute it
- * freely, subject to the following restrictions:
- *
- * 1. The origin of this software must not be misrepresented; you must not
- *    claim that you wrote the original software. If you use this software
- *    in a product, an acknowledgment in the product documentation would be
- *    appreciated but is not required.
- * 2. Altered source versions must be plainly marked as such, and must not be
- *    misrepresented as being the original software.
- * 3. This notice may not be removed or altered from any source distribution.
- *
- ******************************************************************************/
-
-//-------- <<< Use Configuration Wizard in Context Menu >>> -----------------
-//
-// <e>  Bluetooth CLI
-#define SL_OPENTHREAD_BLE_CLI_ENABLE                       1
-// </e>
-// <<< end of configuration section >>>
+/***************************************************************************//**
+ * @file
+ * @brief Bluetooth Accept List configuration
+ *******************************************************************************
+ * # License
+ * <b>Copyright 2023 Silicon Laboratories Inc. www.silabs.com</b>
+ *******************************************************************************
+ *
+ * SPDX-License-Identifier: Zlib
+ *
+ * The licensor of this software is Silicon Laboratories Inc.
+ *
+ * This software is provided 'as-is', without any express or implied warranty.
+ * In no event will the authors be held liable for any damages arising from the
+ * use of this software.
+ *
+ * Permission is granted to anyone to use this software for any purpose,
+ * including commercial applications, and to alter it and redistribute it
+ * freely, subject to the following restrictions:
+ *
+ * 1. The origin of this software must not be misrepresented; you must not
+ *    claim that you wrote the original software. If you use this software in a
+ *    product, an acknowledgment in the product documentation would be
+ *    appreciated but is not required.
+ * 2. Altered source versions must be plainly marked as such, and must not be
+ *    misrepresented as being the original software.
+ * 3. This notice may not be removed or altered from any source distribution.
+ *
+ ******************************************************************************/
+
+#ifndef SL_BT_ACCEPT_LIST_CONFIG_H
+#define SL_BT_ACCEPT_LIST_CONFIG_H
+
+// <<< Use Configuration Wizard in Context Menu >>>
+
+// <h> Bluetooth Controller Configuration
+
+// <o SL_BT_CONFIG_ACCEPT_LIST_SIZE> Bluetooth Controller Filter Accept List Size <0..127:1>
+// <i> Default: 2
+// <i> Define the number of Filter Accept List entries to be used in doing device address filtering when scanning
+#define SL_BT_CONFIG_ACCEPT_LIST_SIZE     (2)
+
+// </h> Bluetooth Controller Configuration
+
+// <<< end of configuration section >>>
+
+#endif // SL_BT_ACCEPT_LIST_CONFIG_H
diff --git a/config/sl_bt_resolving_list_config.h b/config/sl_bt_resolving_list_config.h
new file mode 100644
index 0000000..28d783d
--- /dev/null
+++ b/config/sl_bt_resolving_list_config.h
@@ -0,0 +1,52 @@
+/***************************************************************************//**
+ * @file
+ * @brief Bluetooth Resolving List configuration
+ *******************************************************************************
+ * # License
+ * <b>Copyright 2023 Silicon Laboratories Inc. www.silabs.com</b>
+ *******************************************************************************
+ *
+ * SPDX-License-Identifier: Zlib
+ *
+ * The licensor of this software is Silicon Laboratories Inc.
+ *
+ * This software is provided 'as-is', without any express or implied warranty.
+ * In no event will the authors be held liable for any damages arising from the
+ * use of this software.
+ *
+ * Permission is granted to anyone to use this software for any purpose,
+ * including commercial applications, and to alter it and redistribute it
+ * freely, subject to the following restrictions:
+ *
+ * 1. The origin of this software must not be misrepresented; you must not
+ *    claim that you wrote the original software. If you use this software in a
+ *    product, an acknowledgment in the product documentation would be
+ *    appreciated but is not required.
+ * 2. Altered source versions must be plainly marked as such, and must not be
+ *    misrepresented as being the original software.
+ * 3. This notice may not be removed or altered from any source distribution.
+ *
+ ******************************************************************************/
+
+#ifndef SL_BTCTRL_RESOLVING_LIST_CONFIG_H
+#define SL_BTCTRL_RESOLVING_LIST_CONFIG_H
+
+// <<< Use Configuration Wizard in Context Menu >>>
+
+// <h> Bluetooth Controller Configuration
+
+// <o SL_BT_CONFIG_RESOLVING_LIST_SIZE> Bluetooth Controller Resolving List Size
+// <0..8:1>
+// <i> Default: 2
+// <i> Define the number of resolving list entries to be used in linklayer privacy.
+#define SL_BT_CONFIG_RESOLVING_LIST_SIZE     (2)
+
+#if SL_BT_CONFIG_RESOLVING_LIST_SIZE > RADIOAES_BLE_RPA_MAX_KEYS
+#error "The configured resolving list size cannot be handled by the bluetooth stack/controller"
+#endif
+
+// </h> Bluetooth Controller Configuration
+
+// <<< end of configuration section >>>
+
+#endif // SL_BTCTRL_RESOLVING_LIST_CONFIG_H
diff --git a/config/sl_openthread_features_config.h b/config/sl_openthread_features_mtd_cert_config.h
similarity index 81%
rename from config/sl_openthread_features_config.h
rename to config/sl_openthread_features_mtd_cert_config.h
index 3e5ed67..165cd74 100644
--- a/config/sl_openthread_features_config.h
+++ b/config/sl_openthread_features_mtd_cert_config.h
@@ -1,405 +1,383 @@
-/*******************************************************************************
- * @file
- * @brief OpenThread stack configuration file.
- *******************************************************************************
- * # License
- * <b>Copyright 2024 Silicon Laboratories Inc. www.silabs.com</b>
- *******************************************************************************
- *
- * SPDX-License-Identifier: Zlib
- *
- * The licensor of this software is Silicon Laboratories Inc.
- *
- * This software is provided 'as-is', without any express or implied
- * warranty. In no event will the authors be held liable for any damages
- * arising from the use of this software.
- *
- * Permission is granted to anyone to use this software for any purpose,
- * including commercial applications, and to alter it and redistribute it
- * freely, subject to the following restrictions:
- *
- * 1. The origin of this software must not be misrepresented; you must not
- *    claim that you wrote the original software. If you use this software
- *    in a product, an acknowledgment in the product documentation would be
- *    appreciated but is not required.
- * 2. Altered source versions must be plainly marked as such, and must not be
- *    misrepresented as being the original software.
- * 3. This notice may not be removed or altered from any source distribution.
- *
- ******************************************************************************/
-
-#ifndef _SL_OPENTHREAD_FEATURES_CONFIG_H
-#define _SL_OPENTHREAD_FEATURES_CONFIG_H
-//-------- <<< Use Configuration Wizard in Context Menu >>> -----------------
-//
-// <h> Default OpenThread Stack Configuration
-
-// <h>  Thread Stack Protocol Version
-// <o   OPENTHREAD_CONFIG_THREAD_VERSION>
-//      <OT_THREAD_VERSION_1_1=> Thread 1.1
-//      <OT_THREAD_VERSION_1_2=> Thread 1.2
-//      <OT_THREAD_VERSION_1_3=> Thread 1.3
-//      <OT_THREAD_VERSION_1_4=> Thread 1.4
-// <i>  Current Default: OT_THREAD_VERSION_1_4
-#ifndef OPENTHREAD_CONFIG_THREAD_VERSION
-#define OPENTHREAD_CONFIG_THREAD_VERSION OT_THREAD_VERSION_1_4
-#endif
-// </h>
-
-#if (OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_2)
-// <h>  The following features require at least Thread Stack Protocol Version 1.2
-// <q>  Backbone Router
-#ifndef OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE
-#define OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE    0
-#endif
-// <q> CSL Auto Synchronization using data polling
-#ifndef OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE
-#define OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE  1
-#endif
-// <q>  CSL (Coordinated Sampled Listening) Debug
-#ifndef OPENTHREAD_CONFIG_MAC_CSL_DEBUG_ENABLE
-#define OPENTHREAD_CONFIG_MAC_CSL_DEBUG_ENABLE      0
-#endif
-// <q>  CSL (Coordinated Sampled Listening) Receiver
-#ifndef OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE
-#define OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE   1
-#endif
-// <o SL_OPENTHREAD_CSL_TX_UNCERTAINTY> CSL Scheduling Uncertainty (±10 us units) <12..999:1>
-#ifndef SL_OPENTHREAD_CSL_TX_UNCERTAINTY
-#if OPENTHREAD_RADIO
-  #define SL_OPENTHREAD_CSL_TX_UNCERTAINTY 175
-#elif OPENTHREAD_FTD
-  #define SL_OPENTHREAD_CSL_TX_UNCERTAINTY 20
-#else
-  #define SL_OPENTHREAD_CSL_TX_UNCERTAINTY 12
-#endif
-#endif
-// <q>  DUA (Domain Unicast Address)
-#ifndef OPENTHREAD_CONFIG_DUA_ENABLE
-#define OPENTHREAD_CONFIG_DUA_ENABLE                1
-#endif
-// <q>  Link Metrics Initiator
-#ifndef OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE
-#define OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE 1
-#endif
-// <q>  Link Metrics Subject
-#ifndef OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE
-#define OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE 1
-#endif
-// <q>  Multicast Listener Registration
-#ifndef OPENTHREAD_CONFIG_MLR_ENABLE
-#define OPENTHREAD_CONFIG_MLR_ENABLE                1
-#endif
-// </h>
-#endif // OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_2
-
-#if (OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_3)
-// <h>  The following features require at least Thread Stack Protocol Version 1.3
-// <q>  DNS Client
-#ifndef OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE
-#define OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE         1
-#endif
-// <q>  DNS-SD Server
-#ifndef OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE
-#define OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE       0
-#endif
-// <q>  Service Registration Protocol (SRP) Client
-#ifndef OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE
-#define OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE         1
-#endif
-// <q>  Service Registration Protocol (SRP) Server
-#ifndef OPENTHREAD_CONFIG_SRP_SERVER_ENABLE
-#define OPENTHREAD_CONFIG_SRP_SERVER_ENABLE         0
-#endif
-// <q>  TCP API
-#ifndef OPENTHREAD_CONFIG_TCP_ENABLE
-#define OPENTHREAD_CONFIG_TCP_ENABLE                0
-#endif
-// <q>  DNS Client over TCP
-#ifndef OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE
-#define OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE 0
-#endif
-// <q> Thread over Infrastructure (NCP only)
-#ifndef OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE
-#define OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE 0
-#endif
-// </h>
-#endif // OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_3
-
-// <e>  Border Agent
-#ifndef OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE
-#define OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE       0
-#endif
-// </e>
-// <e>  Border Router
-#ifndef OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE
-#define OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE      0
-#endif
-// </e>
-// <e>  Channel Manager
-#ifndef OPENTHREAD_CONFIG_CHANNEL_MANAGER_ENABLE
-#define OPENTHREAD_CONFIG_CHANNEL_MANAGER_ENABLE    0
-#endif
-// </e>
-// <e>  Channel Monitor
-#ifndef OPENTHREAD_CONFIG_CHANNEL_MONITOR_ENABLE
-#define OPENTHREAD_CONFIG_CHANNEL_MONITOR_ENABLE    0
-#endif
-// </e>
-
-// <e OPENTHREAD_CONFIG_COMMISSIONER_ENABLE>  Commissioner
-#ifndef OPENTHREAD_CONFIG_COMMISSIONER_ENABLE
-#define OPENTHREAD_CONFIG_COMMISSIONER_ENABLE       0
-#endif
-
-// <o OPENTHREAD_CONFIG_COMMISSIONER_MAX_JOINER_ENTRIES> Max Joiner Entries
-// <i> The maximum number of Joiner entries maintained by the Commissioner.
-// <d> 2
-#ifndef OPENTHREAD_CONFIG_COMMISSIONER_MAX_JOINER_ENTRIES
-#define OPENTHREAD_CONFIG_COMMISSIONER_MAX_JOINER_ENTRIES       2
-#endif
-// </e>
-
-// <e>  COAP API
-#ifndef OPENTHREAD_CONFIG_COAP_API_ENABLE
-#define OPENTHREAD_CONFIG_COAP_API_ENABLE           0
-#endif
-// </e>
-// <e>  COAP Observe (RFC7641) API
-#ifndef OPENTHREAD_CONFIG_COAP_OBSERVE_API_ENABLE
-#define OPENTHREAD_CONFIG_COAP_OBSERVE_API_ENABLE   0
-#endif
-// </e>
-// <e>  COAP Secure API
-#ifndef OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE
-#define OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE    0
-#endif
-// </e>
-// <e>  DHCP6 Client
-#ifndef OPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE
-#define OPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE       0
-#endif
-// </e>
-// <e>  DHCP6 Server
-#ifndef OPENTHREAD_CONFIG_DHCP6_SERVER_ENABLE
-#define OPENTHREAD_CONFIG_DHCP6_SERVER_ENABLE       0
-#endif
-// </e>
-// <e>  ECDSA (Elliptic Curve Digital Signature Algorithm) (Required for Matter support)
-#ifndef OPENTHREAD_CONFIG_ECDSA_ENABLE
-#define OPENTHREAD_CONFIG_ECDSA_ENABLE              1
-#endif
-// </e>
-// <e>  External Heap
-#ifndef OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE
-#define OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE      1
-#endif
-// </e>
-// <e>  IPv6 Fragmentation
-#ifndef OPENTHREAD_CONFIG_IP6_FRAGMENTATION_ENABLE
-#define OPENTHREAD_CONFIG_IP6_FRAGMENTATION_ENABLE  0
-#endif
-// </e>
-// <e>  Maximum number of IPv6 unicast addresses allowed to be externally added
-#ifndef OPENTHREAD_CONFIG_IP6_MAX_EXT_UCAST_ADDRS
-#define OPENTHREAD_CONFIG_IP6_MAX_EXT_UCAST_ADDRS   4
-#endif
-// </e>
-// <e>  Maximum number of IPv6 multicast addresses allowed to be externally added
-#ifndef OPENTHREAD_CONFIG_IP6_MAX_EXT_MCAST_ADDRS
-#define OPENTHREAD_CONFIG_IP6_MAX_EXT_MCAST_ADDRS   4
-#endif
-// </e>
-// <e>  Jam Detection
-#ifndef OPENTHREAD_CONFIG_JAM_DETECTION_ENABLE
-#define OPENTHREAD_CONFIG_JAM_DETECTION_ENABLE      0
-#endif
-// </e>
-// <e>  Joiner
-#ifndef OPENTHREAD_CONFIG_JOINER_ENABLE
-#define OPENTHREAD_CONFIG_JOINER_ENABLE             0
-#endif
-// </e>
-// <e>  Link Raw Service
-#ifndef OPENTHREAD_CONFIG_LINK_RAW_ENABLE
-#define OPENTHREAD_CONFIG_LINK_RAW_ENABLE           0
-#endif
-// </e>
-// <e>  MAC Filter
-#ifndef OPENTHREAD_CONFIG_MAC_FILTER_ENABLE
-#define OPENTHREAD_CONFIG_MAC_FILTER_ENABLE         0
-#endif
-// </e>
-// <e>  MLE Long Routes extension (experimental)
-#ifndef OPENTHREAD_CONFIG_MLE_LONG_ROUTES_ENABLE
-#define OPENTHREAD_CONFIG_MLE_LONG_ROUTES_ENABLE    0
-#endif
-// </e>
-// <e>  MultiPAN RCP
-#ifndef OPENTHREAD_CONFIG_MULTIPAN_RCP_ENABLE
-#define OPENTHREAD_CONFIG_MULTIPAN_RCP_ENABLE       0
-#endif
-// </e>
-// <e>  Multiple OpenThread Instances
-#ifndef OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE
-#define OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE      0
-#endif
-// </e>
-// <e>  Multiple Static Instance Support
-#ifndef OPENTHREAD_CONFIG_MULTIPLE_STATIC_INSTANCE_ENABLE
-#define OPENTHREAD_CONFIG_MULTIPLE_STATIC_INSTANCE_ENABLE      0
-#endif
-// </e>
-// <e>  Number of OpenThread Instances For Static Buffer Allocation
-#ifndef OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_NUM
-#define OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_NUM      2
-#endif
-// </e>
-// <e>  Define broadcast IID for spinel frames dedicated to all hosts in multipan configuration
-#ifndef OPENTHREAD_SPINEL_CONFIG_BROADCAST_IID
-#define OPENTHREAD_SPINEL_CONFIG_BROADCAST_IID      0
-#endif
-// </e>
-// <e>  OTNS (OpenThread Network Simulator)
-#ifndef OPENTHREAD_CONFIG_OTNS_ENABLE
-#define OPENTHREAD_CONFIG_OTNS_ENABLE               0
-#endif
-// </e>
-// <e>  Ping Sender Module
-#ifndef OPENTHREAD_CONFIG_PING_SENDER_ENABLE
-#define OPENTHREAD_CONFIG_PING_SENDER_ENABLE        1
-#endif
-
-// </e>
-// <e>  Power Calibration Module  (RCP only configuration)
-#ifndef OPENTHREAD_CONFIG_POWER_CALIBRATION_ENABLE
-#define OPENTHREAD_CONFIG_POWER_CALIBRATION_ENABLE  0
-#endif
-
-// </e>
-// <e>  Platform UDP
-#ifndef OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE
-#define OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE       0
-#endif
-// </e>
-// <e>  Reference Device for Thread Test Harness
-#ifndef OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE
-#define OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE   0
-#endif
-// </e>
-// <e>  Service Entries in Thread Network Data
-#ifndef OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE
-#define OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE    0
-#endif
-// </e>
-// <e>  RAM (volatile-only storage)
-#ifndef OPENTHREAD_SETTINGS_RAM
-#define OPENTHREAD_SETTINGS_RAM                     0
-#endif
-// </e>
-// <e>  SLAAC Addresses
-#ifndef OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE
-#define OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE          1
-#endif
-// </e>
-// <e>  SNTP Client
-#ifndef OPENTHREAD_CONFIG_SNTP_CLIENT_ENABLE
-#define OPENTHREAD_CONFIG_SNTP_CLIENT_ENABLE        0
-#endif
-// </e>
-// <e>  TMF Network Diagnostic client API
-#ifndef OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE
-#define OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE   1
-#endif
-// </e>
-// <e>  Time Synchronization Service
-#define OPENTHREAD_CONFIG_TIME_SYNC_ENABLE          0
-// </e>
-// <e>  UDP Forward
-#ifndef OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE
-#define OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE        0
-#endif
-// </e>
-// <e>  Enable Mac beacon payload parsing support
-#ifndef OPENTHREAD_CONFIG_MAC_BEACON_PAYLOAD_PARSING_ENABLE
-#define OPENTHREAD_CONFIG_MAC_BEACON_PAYLOAD_PARSING_ENABLE      1
-#endif
-// </e>
-// <e>  Max raw power calibration length.
-#ifndef SL_OPENTHREAD_RAW_POWER_CALIBRATION_LENGTH
-#define SL_OPENTHREAD_RAW_POWER_CALIBRATION_LENGTH  4
-#endif
-// </e>
-// <e>  Max FEM config setting length.
-#ifndef SL_OPENTHREAD_FEM_SETTING_LENGTH
-#define SL_OPENTHREAD_FEM_SETTING_LENGTH            4
-#endif
-// </e>
-// <i> The maximum number of RX buffers to use in the radio driver.
-// <d> 16
-#ifndef SL_OPENTHREAD_RADIO_RX_BUFFER_COUNT
-#define SL_OPENTHREAD_RADIO_RX_BUFFER_COUNT       16
-#endif
-// </h>
-// <h>  Logging
-// <o   OPENTHREAD_CONFIG_LOG_OUTPUT> LOG_OUTPUT
-//      <OPENTHREAD_CONFIG_LOG_OUTPUT_NONE             => NONE
-//      <OPENTHREAD_CONFIG_LOG_OUTPUT_APP              => APP
-//      <OPENTHREAD_CONFIG_LOG_OUTPUT_PLATFORM_DEFINED => PLATFORM_DEFINED
-// <i>  Default: OPENTHREAD_CONFIG_LOG_OUTPUT_PLATFORM_DEFINED
-#ifndef OPENTHREAD_CONFIG_LOG_OUTPUT
-#define OPENTHREAD_CONFIG_LOG_OUTPUT OPENTHREAD_CONFIG_LOG_OUTPUT_APP
-#endif
-
-// <q>  DYNAMIC_LOG_LEVEL
-#ifndef OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE
-#define OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE  0
-#endif
-
-// <e>  Enable Logging
-#define OPENTHREAD_FULL_LOGS_ENABLE                 0
-#if     OPENTHREAD_FULL_LOGS_ENABLE
-
-// <h>  Note: Enabling higher log levels, which include logging packet details, can cause delays which may result in join failures.
-// <o   OPENTHREAD_CONFIG_LOG_LEVEL> LOG_LEVEL
-//      <OT_LOG_LEVEL_NONE       => NONE
-//      <OT_LOG_LEVEL_CRIT       => CRIT
-//      <OT_LOG_LEVEL_WARN       => WARN
-//      <OT_LOG_LEVEL_NOTE       => NOTE
-//      <OT_LOG_LEVEL_INFO       => INFO
-//      <OT_LOG_LEVEL_DEBG       => DEBG
-// <i>  Default: OT_LOG_LEVEL_DEBG
-#ifndef OPENTHREAD_CONFIG_LOG_LEVEL
-#define OPENTHREAD_CONFIG_LOG_LEVEL OT_LOG_LEVEL_DEBG
-#endif
-// <q>  CLI
-#ifndef OPENTHREAD_CONFIG_LOG_CLI
-#define OPENTHREAD_CONFIG_LOG_CLI                   1
-#endif
-// <q>  PKT_DUMP
-#ifndef OPENTHREAD_CONFIG_LOG_PKT_DUMP
-#define OPENTHREAD_CONFIG_LOG_PKT_DUMP              1
-#endif
-// <q>  PLATFORM
-#ifndef OPENTHREAD_CONFIG_LOG_PLATFORM
-#define OPENTHREAD_CONFIG_LOG_PLATFORM              1
-#endif
-// <q>  PREPEND_LEVEL
-#ifndef OPENTHREAD_CONFIG_LOG_PREPEND_LEVEL
-#define OPENTHREAD_CONFIG_LOG_PREPEND_LEVEL         1
-#endif
-
-#endif // OPENTHREAD_FULL_LOGS_ENABLE
-
-// <e> Log crash dump after initialization
-#ifndef OPENTHREAD_CONFIG_PLATFORM_LOG_CRASH_DUMP_ENABLE
-#define OPENTHREAD_CONFIG_PLATFORM_LOG_CRASH_DUMP_ENABLE 0
-#endif
-// </e>
-
-// </h>
-// </e>
-// </h>
-
-// <<< end of configuration section >>>
-#endif // _SL_OPENTHREAD_FEATURES_CONFIG_H
+/*******************************************************************************
+ * @file
+ * @brief OpenThread MTD certification configuration file.
+ *******************************************************************************
+ * # License
+ * <b>Copyright 2024 Silicon Laboratories Inc. www.silabs.com</b>
+ *******************************************************************************
+ *
+ * SPDX-License-Identifier: Zlib
+ *
+ * The licensor of this software is Silicon Laboratories Inc.
+ *
+ * This software is provided 'as-is', without any express or implied
+ * warranty. In no event will the authors be held liable for any damages
+ * arising from the use of this software.
+ *
+ * Permission is granted to anyone to use this software for any purpose,
+ * including commercial applications, and to alter it and redistribute it
+ * freely, subject to the following restrictions:
+ *
+ * 1. The origin of this software must not be misrepresented; you must not
+ *    claim that you wrote the original software. If you use this software
+ *    in a product, an acknowledgment in the product documentation would be
+ *    appreciated but is not required.
+ * 2. Altered source versions must be plainly marked as such, and must not be
+ *    misrepresented as being the original software.
+ * 3. This notice may not be removed or altered from any source distribution.
+ *
+ ******************************************************************************/
+
+#ifndef _SL_OPENTHREAD_FEATURES_CONFIG_H
+#define _SL_OPENTHREAD_FEATURES_CONFIG_H
+//-------- <<< Use Configuration Wizard in Context Menu >>> -----------------
+//
+// <h> OpenThread Stack Configuration for MTD Certification
+
+// <h> WARNING:
+// </h>
+// <h> Changing configuration values here will have ramifications on inheriting Thread certification using pre-built MTD certification libraries. If you must change any of these values, note that it requires rebuilding the MTD certification libraries.
+// </h>
+// <h>
+// </h>
+// <h> Note: If you have selected the "OpenThread CoAP Certification configuration" component, then the CoAP API options will be automatically enabled for the project and will not be affected by the settings here.
+// </h>
+// <h>
+// </h>
+
+// <h>  Thread Stack Protocol Version
+// <o   OPENTHREAD_CONFIG_THREAD_VERSION>
+//      <OT_THREAD_VERSION_1_1=> Thread 1.1
+//      <OT_THREAD_VERSION_1_2=> Thread 1.2
+//      <OT_THREAD_VERSION_1_3=> Thread 1.3
+//      <OT_THREAD_VERSION_1_4=> Thread 1.4
+// <i>  Current Default: OT_THREAD_VERSION_1_4
+#ifndef OPENTHREAD_CONFIG_THREAD_VERSION
+#define OPENTHREAD_CONFIG_THREAD_VERSION OT_THREAD_VERSION_1_4
+#endif
+// </h>
+
+#if (OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_2)
+// <h>  The following features require at least Thread Stack Protocol Version 1.2
+// <q>  Backbone Router
+#ifndef OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE
+#define OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE    0
+#endif
+// <q> CSL Auto Synchronization using data polling
+#ifndef OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE
+#define OPENTHREAD_CONFIG_MAC_CSL_AUTO_SYNC_ENABLE  1
+#endif
+// <q>  CSL (Coordinated Sampled Listening) Debug
+#ifndef OPENTHREAD_CONFIG_MAC_CSL_DEBUG_ENABLE
+#define OPENTHREAD_CONFIG_MAC_CSL_DEBUG_ENABLE      0
+#endif
+// <q>  CSL (Coordinated Sampled Listening) Receiver
+#ifndef OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE
+#define OPENTHREAD_CONFIG_MAC_CSL_RECEIVER_ENABLE   1
+#endif
+// <o SL_OPENTHREAD_CSL_TX_UNCERTAINTY> CSL Scheduling Uncertainty (±10 us units) <12..999:1>
+#ifndef SL_OPENTHREAD_CSL_TX_UNCERTAINTY
+#define SL_OPENTHREAD_CSL_TX_UNCERTAINTY            200
+#endif
+// <o OPENTHREAD_CONFIG_CSL_RECEIVE_TIME_AHEAD> Reception ramp up time for CSL receiver (us.) <600..2000:1>
+#ifndef OPENTHREAD_CONFIG_CSL_RECEIVE_TIME_AHEAD
+#define OPENTHREAD_CONFIG_CSL_RECEIVE_TIME_AHEAD    750
+#endif
+// <q>  DUA (Domain Unicast Address)
+#ifndef OPENTHREAD_CONFIG_DUA_ENABLE
+#define OPENTHREAD_CONFIG_DUA_ENABLE                1
+#endif
+// <q>  Link Metrics Initiator
+#ifndef OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE
+#define OPENTHREAD_CONFIG_MLE_LINK_METRICS_INITIATOR_ENABLE 1
+#endif
+// <q>  Link Metrics Subject
+#ifndef OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE
+#define OPENTHREAD_CONFIG_MLE_LINK_METRICS_SUBJECT_ENABLE 0
+#endif
+// <q>  Multicast Listener Registration
+#ifndef OPENTHREAD_CONFIG_MLR_ENABLE
+#define OPENTHREAD_CONFIG_MLR_ENABLE                1
+#endif
+// </h>
+#endif // OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_2
+
+#if (OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_3)
+// <h>  The following features require at least Thread Stack Protocol Version 1.3
+// <q>  DNS Client
+#ifndef OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE
+#define OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE         1
+#endif
+// <q>  DNS-SD Server
+#ifndef OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE
+#define OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE       0
+#endif
+// <q>  Service Registration Protocol (SRP) Client
+#ifndef OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE
+#define OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE         1
+#endif
+// <q>  Service Registration Protocol (SRP) Server
+#ifndef OPENTHREAD_CONFIG_SRP_SERVER_ENABLE
+#define OPENTHREAD_CONFIG_SRP_SERVER_ENABLE         0
+#endif
+// <q>  TCP API
+#ifndef OPENTHREAD_CONFIG_TCP_ENABLE
+#define OPENTHREAD_CONFIG_TCP_ENABLE                1
+#endif
+// <q>  DNS Client over TCP
+#ifndef OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE
+#define OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE 1
+#endif
+// <q> Thread over Infrastructure (NCP only)
+#ifndef OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE
+#define OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE 0
+#endif
+// </h>
+#endif // OPENTHREAD_CONFIG_THREAD_VERSION >= OT_THREAD_VERSION_1_3
+
+// <e>  Border Agent
+#ifndef OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE
+#define OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE       0
+#endif
+// </e>
+// <e>  Border Router
+#ifndef OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE
+#define OPENTHREAD_CONFIG_BORDER_ROUTER_ENABLE      0
+#endif
+// </e>
+// <e>  Channel Manager
+#ifndef OPENTHREAD_CONFIG_CHANNEL_MANAGER_ENABLE
+#define OPENTHREAD_CONFIG_CHANNEL_MANAGER_ENABLE    0
+#endif
+// </e>
+// <e>  Channel Monitor
+#ifndef OPENTHREAD_CONFIG_CHANNEL_MONITOR_ENABLE
+#define OPENTHREAD_CONFIG_CHANNEL_MONITOR_ENABLE    0
+#endif
+// </e>
+// <e>  Commissioner
+#ifndef OPENTHREAD_CONFIG_COMMISSIONER_ENABLE
+#define OPENTHREAD_CONFIG_COMMISSIONER_ENABLE       0
+#endif
+// </e>
+// <e>  COAP API
+#ifndef OPENTHREAD_CONFIG_COAP_API_ENABLE
+#define OPENTHREAD_CONFIG_COAP_API_ENABLE           0
+#endif
+// </e>
+// <e>  COAP Observe (RFC7641) API
+#ifndef OPENTHREAD_CONFIG_COAP_OBSERVE_API_ENABLE
+#define OPENTHREAD_CONFIG_COAP_OBSERVE_API_ENABLE   0
+#endif
+// </e>
+// <e>  COAP Secure API
+#ifndef OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE
+#define OPENTHREAD_CONFIG_COAP_SECURE_API_ENABLE    0
+#endif
+// </e>
+// <e>  DHCP6 Client
+#ifndef OPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE
+#define OPENTHREAD_CONFIG_DHCP6_CLIENT_ENABLE       1
+#endif
+// </e>
+// <e>  DHCP6 Server
+#ifndef OPENTHREAD_CONFIG_DHCP6_SERVER_ENABLE
+#define OPENTHREAD_CONFIG_DHCP6_SERVER_ENABLE       0
+#endif
+// </e>
+// <e>  ECDSA (Elliptic Curve Digital Signature Algorithm) (Required for Matter support)
+#ifndef OPENTHREAD_CONFIG_ECDSA_ENABLE
+#define OPENTHREAD_CONFIG_ECDSA_ENABLE              1
+#endif
+// </e>
+// <e>  External Heap
+#ifndef OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE
+#define OPENTHREAD_CONFIG_HEAP_EXTERNAL_ENABLE      1
+#endif
+// </e>
+// <e>  IPv6 Fragmentation
+#ifndef OPENTHREAD_CONFIG_IP6_FRAGMENTATION_ENABLE
+#define OPENTHREAD_CONFIG_IP6_FRAGMENTATION_ENABLE  0
+#endif
+// </e>
+// <e>  Maximum number of IPv6 unicast addresses allowed to be externally added
+#ifndef OPENTHREAD_CONFIG_IP6_MAX_EXT_UCAST_ADDRS
+#define OPENTHREAD_CONFIG_IP6_MAX_EXT_UCAST_ADDRS   4
+#endif
+// </e>
+// <e>  Maximum number of IPv6 multicast addresses allowed to be externally added
+#ifndef OPENTHREAD_CONFIG_IP6_MAX_EXT_MCAST_ADDRS
+#define OPENTHREAD_CONFIG_IP6_MAX_EXT_MCAST_ADDRS   4
+#endif
+// </e>
+// <e>  Jam Detection
+#ifndef OPENTHREAD_CONFIG_JAM_DETECTION_ENABLE
+#define OPENTHREAD_CONFIG_JAM_DETECTION_ENABLE      0
+#endif
+// </e>
+// <e>  Joiner
+#ifndef OPENTHREAD_CONFIG_JOINER_ENABLE
+#define OPENTHREAD_CONFIG_JOINER_ENABLE             0
+#endif
+// </e>
+// <e>  Link Raw Service
+#ifndef OPENTHREAD_CONFIG_LINK_RAW_ENABLE
+#define OPENTHREAD_CONFIG_LINK_RAW_ENABLE           0
+#endif
+// </e>
+// <e>  MAC Filter
+#ifndef OPENTHREAD_CONFIG_MAC_FILTER_ENABLE
+#define OPENTHREAD_CONFIG_MAC_FILTER_ENABLE         0
+#endif
+// </e>
+// <e>  MLE Long Routes extension (experimental)
+#ifndef OPENTHREAD_CONFIG_MLE_LONG_ROUTES_ENABLE
+#define OPENTHREAD_CONFIG_MLE_LONG_ROUTES_ENABLE    0
+#endif
+// </e>
+// <e>  MultiPAN RCP
+#ifndef OPENTHREAD_CONFIG_MULTIPAN_RCP_ENABLE
+#define OPENTHREAD_CONFIG_MULTIPAN_RCP_ENABLE       0
+#endif
+// </e>
+// <e>  Multiple OpenThread Instances
+#ifndef OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE
+#define OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE      0
+#endif
+// </e>
+// <e>  OTNS (OpenThread Network Simulator)
+#ifndef OPENTHREAD_CONFIG_OTNS_ENABLE
+#define OPENTHREAD_CONFIG_OTNS_ENABLE               0
+#endif
+// </e>
+// <e>  Ping Sender Module
+#ifndef OPENTHREAD_CONFIG_PING_SENDER_ENABLE
+#define OPENTHREAD_CONFIG_PING_SENDER_ENABLE        1
+#endif
+// </e>
+// <e>  Platform UDP
+#ifndef OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE
+#define OPENTHREAD_CONFIG_PLATFORM_UDP_ENABLE       0
+#endif
+// </e>
+// <e>  Reference Device for Thread Test Harness
+#ifndef OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE
+#define OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE   0
+#endif
+// </e>
+// <e>  Service Entries in Thread Network Data
+#ifndef OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE
+#define OPENTHREAD_CONFIG_TMF_NETDATA_SERVICE_ENABLE    1
+#endif
+// </e>
+// <e>  RAM (volatile-only storage)
+#ifndef OPENTHREAD_SETTINGS_RAM
+#define OPENTHREAD_SETTINGS_RAM                     0
+#endif
+// </e>
+// <e>  SLAAC Addresses
+#ifndef OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE
+#define OPENTHREAD_CONFIG_IP6_SLAAC_ENABLE          1
+#endif
+// </e>
+// <e>  SNTP Client
+#ifndef OPENTHREAD_CONFIG_SNTP_CLIENT_ENABLE
+#define OPENTHREAD_CONFIG_SNTP_CLIENT_ENABLE        0
+#endif
+// </e>
+// <e>  TMF Network Diagnostic client API
+#ifndef OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE
+#define OPENTHREAD_CONFIG_TMF_NETDIAG_CLIENT_ENABLE   1
+#endif
+// </e>
+// <e>  Run-time configuration of Vendor Info
+#ifndef OPENTHREAD_CONFIG_NET_DIAG_VENDOR_INFO_SET_API_ENABLE
+#define OPENTHREAD_CONFIG_NET_DIAG_VENDOR_INFO_SET_API_ENABLE   1
+#endif
+// </e>
+// <e>  Uptime of OpenThread instance
+#ifndef OPENTHREAD_CONFIG_UPTIME_ENABLE
+#define OPENTHREAD_CONFIG_UPTIME_ENABLE             1
+#endif
+// </e>
+// <e>  Time Synchronization Service
+#define OPENTHREAD_CONFIG_TIME_SYNC_ENABLE          0
+// </e>
+// <e>  UDP Forward
+#ifndef OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE
+#define OPENTHREAD_CONFIG_UDP_FORWARD_ENABLE        0
+#endif
+// </e>
+// <e>  Enable Mac beacon payload parsing support
+#ifndef OPENTHREAD_CONFIG_MAC_BEACON_PAYLOAD_PARSING_ENABLE
+#define OPENTHREAD_CONFIG_MAC_BEACON_PAYLOAD_PARSING_ENABLE      1
+#endif
+// </e>
+// <e>  Stay awake between fragments
+// <i>  Required for Matter SVE use cases
+#ifndef OPENTHREAD_CONFIG_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS
+#define OPENTHREAD_CONFIG_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS 1
+#endif
+// </e>
+// </h>
+// <h>  Logging
+// <o   OPENTHREAD_CONFIG_LOG_OUTPUT> LOG_OUTPUT
+//      <OPENTHREAD_CONFIG_LOG_OUTPUT_NONE             => NONE
+//      <OPENTHREAD_CONFIG_LOG_OUTPUT_APP              => APP
+//      <OPENTHREAD_CONFIG_LOG_OUTPUT_PLATFORM_DEFINED => PLATFORM_DEFINED
+// <i>  Default: OPENTHREAD_CONFIG_LOG_OUTPUT_PLATFORM_DEFINED
+#ifndef OPENTHREAD_CONFIG_LOG_OUTPUT
+#define OPENTHREAD_CONFIG_LOG_OUTPUT OPENTHREAD_CONFIG_LOG_OUTPUT_APP
+#endif
+
+// <q>  DYNAMIC_LOG_LEVEL
+#ifndef OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE
+#define OPENTHREAD_CONFIG_LOG_LEVEL_DYNAMIC_ENABLE  0
+#endif
+
+// <i> The maximum number of RX buffers to use in the radio driver.
+// <d> 16
+#ifndef SL_OPENTHREAD_RADIO_RX_BUFFER_COUNT
+#define SL_OPENTHREAD_RADIO_RX_BUFFER_COUNT       16
+#endif
+
+// <e>  Enable Logging
+#define OPENTHREAD_FULL_LOGS_ENABLE                 0
+#if     OPENTHREAD_FULL_LOGS_ENABLE
+
+// <h>  Note: Enabling higher log levels, which include logging packet details, can cause delays which may result in join failures.
+// <o   OPENTHREAD_CONFIG_LOG_LEVEL> LOG_LEVEL
+//      <OT_LOG_LEVEL_NONE       => NONE
+//      <OT_LOG_LEVEL_CRIT       => CRIT
+//      <OT_LOG_LEVEL_WARN       => WARN
+//      <OT_LOG_LEVEL_NOTE       => NOTE
+//      <OT_LOG_LEVEL_INFO       => INFO
+//      <OT_LOG_LEVEL_DEBG       => DEBG
+// <i>  Default: OT_LOG_LEVEL_DEBG
+#ifndef OPENTHREAD_CONFIG_LOG_LEVEL
+#define OPENTHREAD_CONFIG_LOG_LEVEL OT_LOG_LEVEL_DEBG
+#endif
+// <q>  CLI
+#ifndef OPENTHREAD_CONFIG_LOG_CLI
+#define OPENTHREAD_CONFIG_LOG_CLI                   1
+#endif
+// <q>  PKT_DUMP
+#ifndef OPENTHREAD_CONFIG_LOG_PKT_DUMP
+#define OPENTHREAD_CONFIG_LOG_PKT_DUMP              1
+#endif
+// <q>  PLATFORM
+#ifndef OPENTHREAD_CONFIG_LOG_PLATFORM
+#define OPENTHREAD_CONFIG_LOG_PLATFORM              1
+#endif
+// <q>  PREPEND_LEVEL
+#ifndef OPENTHREAD_CONFIG_LOG_PREPEND_LEVEL
+#define OPENTHREAD_CONFIG_LOG_PREPEND_LEVEL         1
+#endif
+
+#endif
+// </h>
+// </e>
+// </h>
+
+// <<< end of configuration section >>>
+#endif // _SL_OPENTHREAD_FEATURES_CONFIG_H
diff --git a/config/sl_rail_util_pti_config.h b/config/sl_rail_util_pti_config.h
index 0595cae..a098246 100644
--- a/config/sl_rail_util_pti_config.h
+++ b/config/sl_rail_util_pti_config.h
@@ -59,6 +59,13 @@
 #define SL_RAIL_UTIL_PTI_PERIPHERAL              PTI
 #endif
 
+// PTI DCLK on PC00
+#ifndef SL_RAIL_UTIL_PTI_DCLK_PORT              
+#define SL_RAIL_UTIL_PTI_DCLK_PORT               SL_GPIO_PORT_C
+#endif
+#ifndef SL_RAIL_UTIL_PTI_DCLK_PIN               
+#define SL_RAIL_UTIL_PTI_DCLK_PIN                0
+#endif
 // [PTI_SL_RAIL_UTIL_PTI]$
 
 // <<< sl:end pin_tool >>>
diff --git a/config/sl_simple_led_inst0_config.h b/config/sl_simple_led_led0_config.h
similarity index 77%
rename from config/sl_simple_led_inst0_config.h
rename to config/sl_simple_led_led0_config.h
index 53449fe..8bbbc9a 100644
--- a/config/sl_simple_led_inst0_config.h
+++ b/config/sl_simple_led_led0_config.h
@@ -1,57 +1,60 @@
-/***************************************************************************//**
- * @file
- * @brief Simple Led Driver Configuration
- *******************************************************************************
- * # License
- * <b>Copyright 2019 Silicon Laboratories Inc. www.silabs.com</b>
- *******************************************************************************
- *
- * SPDX-License-Identifier: Zlib
- *
- * The licensor of this software is Silicon Laboratories Inc.
- *
- * This software is provided 'as-is', without any express or implied
- * warranty. In no event will the authors be held liable for any damages
- * arising from the use of this software.
- *
- * Permission is granted to anyone to use this software for any purpose,
- * including commercial applications, and to alter it and redistribute it
- * freely, subject to the following restrictions:
- *
- * 1. The origin of this software must not be misrepresented; you must not
- *    claim that you wrote the original software. If you use this software
- *    in a product, an acknowledgment in the product documentation would be
- *    appreciated but is not required.
- * 2. Altered source versions must be plainly marked as such, and must not be
- *    misrepresented as being the original software.
- * 3. This notice may not be removed or altered from any source distribution.
- *
- ******************************************************************************/
-
-#ifndef SL_SIMPLE_LED_INST0_CONFIG_H
-#define SL_SIMPLE_LED_INST0_CONFIG_H
-
-// <<< Use Configuration Wizard in Context Menu >>>
-
-// <h> Simple LED configuration
-// <o SL_SIMPLE_LED_INST0_POLARITY>
-// <SL_SIMPLE_LED_POLARITY_ACTIVE_LOW=> Active low
-// <SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH=> Active high
-// <i> Default: SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH
-#define SL_SIMPLE_LED_INST0_POLARITY SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH
-// </h> end led configuration
-
-// <<< end of configuration section >>>
-
-// <<< sl:start pin_tool >>>
-
-// <gpio> SL_SIMPLE_LED_INST0
-// $[GPIO_SL_SIMPLE_LED_INST0]
-#warning "Simple LED Driver GPIO pin not configured"
-// #define SL_SIMPLE_LED_INST0_PORT            SL_GPIO_PORT_A
-// #define SL_SIMPLE_LED_INST0_PIN             1
-// [GPIO_SL_SIMPLE_LED_INST0]$
-
-// <<< sl:end pin_tool >>>
-
-#endif // SL_SIMPLE_LED_INST0_CONFIG_H
+/***************************************************************************//**
+ * @file
+ * @brief Simple Led Driver Configuration
+ *******************************************************************************
+ * # License
+ * <b>Copyright 2019 Silicon Laboratories Inc. www.silabs.com</b>
+ *******************************************************************************
+ *
+ * SPDX-License-Identifier: Zlib
+ *
+ * The licensor of this software is Silicon Laboratories Inc.
+ *
+ * This software is provided 'as-is', without any express or implied
+ * warranty. In no event will the authors be held liable for any damages
+ * arising from the use of this software.
+ *
+ * Permission is granted to anyone to use this software for any purpose,
+ * including commercial applications, and to alter it and redistribute it
+ * freely, subject to the following restrictions:
+ *
+ * 1. The origin of this software must not be misrepresented; you must not
+ *    claim that you wrote the original software. If you use this software
+ *    in a product, an acknowledgment in the product documentation would be
+ *    appreciated but is not required.
+ * 2. Altered source versions must be plainly marked as such, and must not be
+ *    misrepresented as being the original software.
+ * 3. This notice may not be removed or altered from any source distribution.
+ *
+ ******************************************************************************/
+
+#ifndef SL_SIMPLE_LED_LED0_CONFIG_H
+#define SL_SIMPLE_LED_LED0_CONFIG_H
+
+// <<< Use Configuration Wizard in Context Menu >>>
+
+// <h> Simple LED configuration
+// <o SL_SIMPLE_LED_LED0_POLARITY>
+// <SL_SIMPLE_LED_POLARITY_ACTIVE_LOW=> Active low
+// <SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH=> Active high
+// <i> Default: SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH
+#define SL_SIMPLE_LED_LED0_POLARITY SL_SIMPLE_LED_POLARITY_ACTIVE_HIGH
+// </h> end led configuration
+
+// <<< end of configuration section >>>
+
+// <<< sl:start pin_tool >>>
+
+// <gpio> SL_SIMPLE_LED_LED0
+// $[GPIO_SL_SIMPLE_LED_LED0]
+#ifndef SL_SIMPLE_LED_LED0_PORT                 
+#define SL_SIMPLE_LED_LED0_PORT                  SL_GPIO_PORT_A
+#endif
+#ifndef SL_SIMPLE_LED_LED0_PIN                  
+#define SL_SIMPLE_LED_LED0_PIN                   3
+#endif
+// [GPIO_SL_SIMPLE_LED_LED0]$
+
+// <<< sl:end pin_tool >>>
+
+#endif // SL_SIMPLE_LED_LED0_CONFIG_H
diff --git a/config/sl_uartdrv_eusart_serial_config.h b/config/sl_uartdrv_eusart_serial_config.h
new file mode 100644
index 0000000..929ab27
--- /dev/null
+++ b/config/sl_uartdrv_eusart_serial_config.h
@@ -0,0 +1,123 @@
+/***************************************************************************//**
+ * @file
+ * @brief UARTDRV_EUSART Config
+ *******************************************************************************
+ * # License
+ * <b>Copyright 2019 Silicon Laboratories Inc. www.silabs.com</b>
+ *******************************************************************************
+ *
+ * SPDX-License-Identifier: Zlib
+ *
+ * The licensor of this software is Silicon Laboratories Inc.
+ *
+ * This software is provided 'as-is', without any express or implied
+ * warranty. In no event will the authors be held liable for any damages
+ * arising from the use of this software.
+ *
+ * Permission is granted to anyone to use this software for any purpose,
+ * including commercial applications, and to alter it and redistribute it
+ * freely, subject to the following restrictions:
+ *
+ * 1. The origin of this software must not be misrepresented; you must not
+ *    claim that you wrote the original software. If you use this software
+ *    in a product, an acknowledgment in the product documentation would be
+ *    appreciated but is not required.
+ * 2. Altered source versions must be plainly marked as such, and must not be
+ *    misrepresented as being the original software.
+ * 3. This notice may not be removed or altered from any source distribution.
+ *
+ ******************************************************************************/
+
+#ifndef SL_UARTDRV_EUSART_SERIAL_CONFIG_H
+#define SL_UARTDRV_EUSART_SERIAL_CONFIG_H
+
+#include "em_eusart.h"
+// <<< Use Configuration Wizard in Context Menu >>>
+
+// <h> EUSART settings
+// <o SL_UARTDRV_EUSART_SERIAL_BAUDRATE> Baud rate
+// <i> Default: 115200
+#define SL_UARTDRV_EUSART_SERIAL_BAUDRATE        9600
+
+// <o SL_UARTDRV_EUSART_SERIAL_LF_MODE> Low frequency mode
+// <true=> True
+// <false=> False
+#define SL_UARTDRV_EUSART_SERIAL_LF_MODE         false
+
+// <o SL_UARTDRV_EUSART_SERIAL_PARITY> Parity mode to use
+// <eusartNoParity=> No Parity
+// <eusartEvenParity=> Even parity
+// <eusartOddParity=> Odd parity
+// <i> Default: eusartNoParity
+#define SL_UARTDRV_EUSART_SERIAL_PARITY          eusartNoParity
+
+// <o SL_UARTDRV_EUSART_SERIAL_STOP_BITS> Number of stop bits to use.
+// <eusartStopbits0p5=> 0.5 stop bits
+// <eusartStopbits1=> 1 stop bits
+// <eusartStopbits1p5=> 1.5 stop bits
+// <eusartStopbits2=> 2 stop bits
+// <i> Default: eusartStopbits1
+#define SL_UARTDRV_EUSART_SERIAL_STOP_BITS       eusartStopbits1
+
+// <o SL_UARTDRV_EUSART_SERIAL_FLOW_CONTROL_TYPE> Flow control method
+// <uartdrvFlowControlNone=> None
+// <uartdrvFlowControlSw=> Software XON/XOFF
+// <uartdrvFlowControlHw=> nRTS/nCTS hardware handshake
+// <uartdrvFlowControlHwUart=> UART peripheral controls nRTS/nCTS
+// <i> Default: uartdrvFlowControlHwUart
+#define SL_UARTDRV_EUSART_SERIAL_FLOW_CONTROL_TYPE uartdrvFlowControlNone
+
+// <o SL_UARTDRV_EUSART_SERIAL_OVERSAMPLING> Oversampling selection
+// <eusartOVS16=> 16x oversampling
+// <eusartOVS8=> 8x oversampling
+// <eusartOVS6=> 6x oversampling
+// <eusartOVS4=> 4x oversampling
+// <eusartOVS0=> Oversampling disabled
+// <i> Default: eusartOVS16
+#define SL_UARTDRV_EUSART_SERIAL_OVERSAMPLING      eusartOVS0
+
+// <o SL_UARTDRV_EUSART_SERIAL_MVDIS> Majority vote disable for 16x, 8x and 6x oversampling modes
+// <eusartMajorityVoteEnable=> False
+// <eusartMajorityVoteDisable=> True
+// <i> Default: eusartMajorityVoteEnable
+#define SL_UARTDRV_EUSART_SERIAL_MVDIS             eusartMajorityVoteEnable
+
+// <o SL_UARTDRV_EUSART_SERIAL_RX_BUFFER_SIZE> Size of the receive operation queue
+// <i> Default: 6
+#define SL_UARTDRV_EUSART_SERIAL_RX_BUFFER_SIZE  6
+
+// <o SL_UARTDRV_EUSART_SERIAL_TX_BUFFER_SIZE> Size of the transmit operation queue
+// <i> Default: 6
+#define SL_UARTDRV_EUSART_SERIAL_TX_BUFFER_SIZE 6
+// </h>
+// <<< end of configuration section >>>
+
+// <<< sl:start pin_tool >>>
+// <eusart signal=TX,RX,(CTS),(RTS)> SL_UARTDRV_EUSART_SERIAL
+// $[EUSART_SL_UARTDRV_EUSART_SERIAL]
+#ifndef SL_UARTDRV_EUSART_SERIAL_PERIPHERAL     
+#define SL_UARTDRV_EUSART_SERIAL_PERIPHERAL      EUSART0
+#endif
+#ifndef SL_UARTDRV_EUSART_SERIAL_PERIPHERAL_NO  
+#define SL_UARTDRV_EUSART_SERIAL_PERIPHERAL_NO   0
+#endif
+
+// EUSART0 TX on PB01
+#ifndef SL_UARTDRV_EUSART_SERIAL_TX_PORT        
+#define SL_UARTDRV_EUSART_SERIAL_TX_PORT         SL_GPIO_PORT_B
+#endif
+#ifndef SL_UARTDRV_EUSART_SERIAL_TX_PIN         
+#define SL_UARTDRV_EUSART_SERIAL_TX_PIN          1
+#endif
+
+// EUSART0 RX on PB02
+#ifndef SL_UARTDRV_EUSART_SERIAL_RX_PORT        
+#define SL_UARTDRV_EUSART_SERIAL_RX_PORT         SL_GPIO_PORT_B
+#endif
+#ifndef SL_UARTDRV_EUSART_SERIAL_RX_PIN         
+#define SL_UARTDRV_EUSART_SERIAL_RX_PIN          2
+#endif
+
+// [EUSART_SL_UARTDRV_EUSART_SERIAL]$
+// <<< sl:end pin_tool >>>
+#endif // SL_UARTDRV_EUSART_SERIAL_CONFIG_H
diff --git a/config/sl_uartdrv_eusart_vcom_config.h b/config/sl_uartdrv_eusart_vcom_config.h
index d27c2b0..3c57435 100644
--- a/config/sl_uartdrv_eusart_vcom_config.h
+++ b/config/sl_uartdrv_eusart_vcom_config.h
@@ -37,7 +37,7 @@
 // <h> EUSART settings
 // <o SL_UARTDRV_EUSART_VCOM_BAUDRATE> Baud rate
 // <i> Default: 115200
-#define SL_UARTDRV_EUSART_VCOM_BAUDRATE        115200
+#define SL_UARTDRV_EUSART_VCOM_BAUDRATE        921600
 
 // <o SL_UARTDRV_EUSART_VCOM_LF_MODE> Low frequency mode
 // <true=> True
@@ -65,7 +65,7 @@
 // <uartdrvFlowControlHw=> nRTS/nCTS hardware handshake
 // <uartdrvFlowControlHwUart=> UART peripheral controls nRTS/nCTS
 // <i> Default: uartdrvFlowControlHwUart
-#define SL_UARTDRV_EUSART_VCOM_FLOW_CONTROL_TYPE uartdrvFlowControlHwUart
+#define SL_UARTDRV_EUSART_VCOM_FLOW_CONTROL_TYPE uartdrvFlowControlNone
 
 // <o SL_UARTDRV_EUSART_VCOM_OVERSAMPLING> Oversampling selection
 // <eusartOVS16=> 16x oversampling
@@ -74,7 +74,7 @@
 // <eusartOVS4=> 4x oversampling
 // <eusartOVS0=> Oversampling disabled
 // <i> Default: eusartOVS16
-#define SL_UARTDRV_EUSART_VCOM_OVERSAMPLING      eusartOVS16
+#define SL_UARTDRV_EUSART_VCOM_OVERSAMPLING      eusartOVS0
 
 // <o SL_UARTDRV_EUSART_VCOM_MVDIS> Majority vote disable for 16x, 8x and 6x oversampling modes
 // <eusartMajorityVoteEnable=> False
@@ -96,43 +96,28 @@
 // <eusart signal=TX,RX,(CTS),(RTS)> SL_UARTDRV_EUSART_VCOM
 // $[EUSART_SL_UARTDRV_EUSART_VCOM]
 #ifndef SL_UARTDRV_EUSART_VCOM_PERIPHERAL       
-#define SL_UARTDRV_EUSART_VCOM_PERIPHERAL        EUSART0
+#define SL_UARTDRV_EUSART_VCOM_PERIPHERAL        EUSART1
 #endif
 #ifndef SL_UARTDRV_EUSART_VCOM_PERIPHERAL_NO    
-#define SL_UARTDRV_EUSART_VCOM_PERIPHERAL_NO     0
+#define SL_UARTDRV_EUSART_VCOM_PERIPHERAL_NO     1
 #endif
 
-// EUSART0 TX on PA00
+// EUSART1 TX on PA07
 #ifndef SL_UARTDRV_EUSART_VCOM_TX_PORT          
 #define SL_UARTDRV_EUSART_VCOM_TX_PORT           SL_GPIO_PORT_A
 #endif
 #ifndef SL_UARTDRV_EUSART_VCOM_TX_PIN           
-#define SL_UARTDRV_EUSART_VCOM_TX_PIN            0
+#define SL_UARTDRV_EUSART_VCOM_TX_PIN            7
 #endif
 
-// EUSART0 RX on PA01
+// EUSART1 RX on PA08
 #ifndef SL_UARTDRV_EUSART_VCOM_RX_PORT          
 #define SL_UARTDRV_EUSART_VCOM_RX_PORT           SL_GPIO_PORT_A
 #endif
 #ifndef SL_UARTDRV_EUSART_VCOM_RX_PIN           
-#define SL_UARTDRV_EUSART_VCOM_RX_PIN            1
+#define SL_UARTDRV_EUSART_VCOM_RX_PIN            8
 #endif
 
-// EUSART0 CTS on PA02
-#ifndef SL_UARTDRV_EUSART_VCOM_CTS_PORT         
-#define SL_UARTDRV_EUSART_VCOM_CTS_PORT          SL_GPIO_PORT_A
-#endif
-#ifndef SL_UARTDRV_EUSART_VCOM_CTS_PIN          
-#define SL_UARTDRV_EUSART_VCOM_CTS_PIN           2
-#endif
-
-// EUSART0 RTS on PA03
-#ifndef SL_UARTDRV_EUSART_VCOM_RTS_PORT         
-#define SL_UARTDRV_EUSART_VCOM_RTS_PORT          SL_GPIO_PORT_A
-#endif
-#ifndef SL_UARTDRV_EUSART_VCOM_RTS_PIN          
-#define SL_UARTDRV_EUSART_VCOM_RTS_PIN           3
-#endif
 // [EUSART_SL_UARTDRV_EUSART_VCOM]$
 // <<< sl:end pin_tool >>>
 #endif // SL_UARTDRV_EUSART_VCOM_CONFIG_H
diff --git a/imported_project_report.html b/imported_project_report.html
new file mode 100644
index 0000000..e80d40b
--- /dev/null
+++ b/imported_project_report.html
@@ -0,0 +1,45 @@
+<?xml version="1.0" encoding="utf-8"?>
+<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
+<html>
+<head>
+<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
+<title>
+Project Import Report for aok02_matter_ac</title>
+</head>
+<body>
+<h1>
+Project Import Summary</h1>
+<table style="border:1px solid">
+<tr style="border:1px solid">
+<td style="border:1px solid">
+Import time</td>
+<td style="border:1px solid">
+2025年10月20日 18:35:19</td>
+</tr>
+<tr style="border:1px solid">
+<td style="border:1px solid">
+Original location</td>
+<td style="border:1px solid">
+C:\Users\DELL\Desktop\AOk Project\AOK Code\aok02_matter_ac\.cproject</td>
+</tr>
+<tr style="border:1px solid">
+<td style="border:1px solid">
+Original project name</td>
+<td style="border:1px solid">
+aok02_matter_ac</td>
+</tr>
+<tr style="border:1px solid">
+<td style="border:1px solid">
+Original project type</td>
+<td style="border:1px solid">
+Simplicity Studio (.sls)</td>
+</tr>
+<tr style="border:1px solid">
+<td style="border:1px solid">
+Import mode</td>
+<td style="border:1px solid">
+Copy contents</td>
+</tr>
+</table>
+</body>
+</html>
diff --git a/include/AppConfig.h b/include/AppConfig.h
deleted file mode 100644
index 578861f..0000000
--- a/include/AppConfig.h
+++ /dev/null
@@ -1,57 +0,0 @@
-/*
- *
- *    Copyright (c) 2020 Project CHIP Authors
- *    Copyright (c) 2019 Google LLC.
- *    All rights reserved.
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#pragma once
-
-#include "silabs_utils.h"
-
-// ---- Window Example App Config ----
-#define APP_TASK_NAME "APP"
-#define APP_EVENT_QUEUE_SIZE 20
-#define BLE_DEV_NAME "SiLabs-Window"
-
-#define LCD_SIZE 128
-#define LCD_MARGIN_SIZE 1
-#define LCD_BORDER_SIZE 2
-#define LCD_FRAME_SIZE (2 * LCD_MARGIN_SIZE + LCD_BORDER_SIZE)
-#define LCD_COVER_SIZE (LCD_SIZE - 2 * LCD_FRAME_SIZE)
-#define LIFT_OPEN_LIMIT 0
-#define LIFT_CLOSED_LIMIT (LCD_COVER_SIZE - 1)
-#define LIFT_DELTA 1000 // 10%
-#define TILT_OPEN_LIMIT 0
-#define TILT_CLOSED_LIMIT (LCD_COVER_SIZE / 10 - 1)
-#define TILT_DELTA 1000 // 10%
-
-#define WINDOW_COVER_COUNT 2
-
-#ifndef WINDOW_COVER_ENDPOINT1
-#define WINDOW_COVER_ENDPOINT1 1
-#endif
-
-#ifndef WINDOW_COVER_ENDPOINT2
-#define WINDOW_COVER_ENDPOINT2 2
-#endif
-
-#ifndef LONG_PRESS_TIMEOUT
-#define LONG_PRESS_TIMEOUT 3000
-#endif
-
-#ifndef COVER_LIFT_TILT_TIMEOUT
-#define COVER_LIFT_TILT_TIMEOUT 500
-#endif
diff --git a/include/AppEvent.h b/include/AppEvent.h
deleted file mode 100644
index 16db1d9..0000000
--- a/include/AppEvent.h
+++ /dev/null
@@ -1,84 +0,0 @@
-/*
- *
- *    Copyright (c) 2020 Project CHIP Authors
- *    All rights reserved.
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#pragma once
-
-#ifdef DISPLAY_ENABLED
-#include "lcd.h"
-#endif
-
-struct AppEvent;
-typedef void (*EventHandler)(AppEvent *);
-
-#include <app/clusters/window-covering-server/window-covering-server.h>
-#include <lib/core/CHIPError.h>
-
-using namespace chip::app::Clusters::WindowCovering;
-
-struct AppEvent
-{
-    enum AppEventTypes
-    {
-        kEventType_Button = 0,
-        kEventType_LCD,
-        kEventType_Timer,
-        kEventType_ResetWarning,
-        kEventType_ResetCanceled,
-        // Button events
-        kEventType_UpPressed,
-        kEventType_UpReleased,
-        kEventType_DownPressed,
-        kEventType_DownReleased,
-        // Cover events
-        kEventType_CoverChange,
-        kEventType_CoverTypeChange,
-        kEventType_TiltModeChange,
-
-        // Cover Attribute update events
-        kEventType_AttributeChange,
-    };
-
-    uint16_t Type;
-    chip::EndpointId mEndpoint = 0;
-    chip::AttributeId mAttributeId;
-
-    union
-    {
-        struct
-        {
-            uint8_t Action;
-        } ButtonEvent;
-#ifdef DISPLAY_ENABLED
-        struct
-        {
-            SilabsLCD::Screen_e screen;
-        } LCDEvent;
-#endif
-        struct
-        {
-            void * Context;
-        } TimerEvent;
-
-        struct
-        {
-            void * Context;
-        } WindowEvent;
-    };
-
-    EventHandler Handler;
-};
diff --git a/include/AppTask.h b/include/AppTask.h
deleted file mode 100644
index ea9f6e5..0000000
--- a/include/AppTask.h
+++ /dev/null
@@ -1,67 +0,0 @@
-/*
- *
- *    Copyright (c) 2020 Project CHIP Authors
- *    Copyright (c) 2019 Google LLC.
- *    All rights reserved.
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#pragma once
-
-/**********************************************************
- * Includes
- *********************************************************/
-
-#include <stdbool.h>
-#include <stdint.h>
-
-#include "BaseApplication.h"
-#include <ble/Ble.h>
-#include <cmsis_os2.h>
-#include <lib/core/CHIPError.h>
-#include <platform/CHIPDeviceLayer.h>
-
-/**********************************************************
- * AppTask Declaration
- *********************************************************/
-
-class AppTask : public BaseApplication
-{
-
-public:
-    AppTask() = default;
-
-    static AppTask & GetAppTask() { return sAppTask; }
-
-    /**
-     * @brief AppTask task main loop function
-     *
-     * @param pvParameter FreeRTOS task parameter
-     */
-    static void AppTaskMain(void * pvParameter);
-
-    CHIP_ERROR StartAppTask();
-
-    static void ButtonEventHandler(uint8_t button, uint8_t btnAction);
-
-private:
-    static AppTask sAppTask;
-
-    /**
-     * @brief AppTask initialisation function
-     *
-     * @return CHIP_ERROR
-     */
-    CHIP_ERROR Init();
-};
diff --git a/include/CHIPProjectConfig.h b/include/CHIPProjectConfig.h
index 2ee5e87..4d68b62 100644
--- a/include/CHIPProjectConfig.h
+++ b/include/CHIPProjectConfig.h
@@ -129,3 +129,49 @@
  *
  */
 #define CHIP_CONFIG_MRP_LOCAL_ACTIVE_RETRY_INTERVAL (2000_ms32)
+
+#define BLE_LAYER_NUM_BLE_ENDPOINTS 10
+
+/**
+ * CHIP_DEVICE_CONFIG_ENABLE_PAIRING_AUTOSTART
+ *
+ * manually opening pairing window after device power-up.
+ *
+ */
+#define CHIP_DEVICE_CONFIG_ENABLE_PAIRING_AUTOSTART 0
+
+/**
+ * CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART
+ *
+ * Enable CHIPoBLE advertising start automatically after device power-up.
+ *
+ * CHIP's device may start advertising automatically only if its all primary device
+ * functions are within a CHIP network. Device providing unrelated to CHIP functionalities
+ * should not start advertising automatically after power-up.
+ *
+ * TODO: Default value should be changed to 0, after all platforms will implement enabling
+ *       advertisement in their own way.
+ */
+#define CHIP_DEVICE_CONFIG_CHIPOBLE_ENABLE_ADVERTISING_AUTOSTART 0
+
+/**
+ * CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS
+ *
+ * Time in seconds that a factory new device will advertise commissionable node discovery.
+ */
+#define CHIP_DEVICE_CONFIG_DISCOVERY_TIMEOUT_SECS (5 * 60)
+
+/**
+ * CHIP_DEVICE_CONFIG_BLE_SLOW_ADVERTISING_INTERVAL_MIN
+ *
+ * The minimum interval (in units of 0.625ms) at which the device will send BLE advertisements while
+ * in slow advertising mode. The minimum interval should be greater and not equal to the
+ * CHIP_DEVICE_CONFIG_BLE_SLOW_ADVERTISING_INTERVAL_MAX.
+ *
+ * Defaults 200 ms
+ */
+#define CHIP_DEVICE_CONFIG_BLE_SLOW_ADVERTISING_INTERVAL_MIN 320
+
+#define CHIP_CONFIG_MAX_GROUP_ENDPOINTS_PER_FABRIC 3
+
+#define IGNORE_ON_OFF_CLUSTER_START_UP_ON_OFF
\ No newline at end of file
diff --git a/include/WindowManager.h b/include/WindowManager.h
deleted file mode 100644
index ce70834..0000000
--- a/include/WindowManager.h
+++ /dev/null
@@ -1,166 +0,0 @@
-/*
- *
- *    Copyright (c) 2021 Project CHIP Authors
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#pragma once
-
-#include <app/clusters/window-covering-server/window-covering-server.h>
-#include <lib/core/CHIPError.h>
-
-#include "AppEvent.h"
-
-#include "LEDWidget.h"
-#include <cmsis_os2.h>
-#include <string>
-#ifdef DISPLAY_ENABLED
-#include <LcdPainter.h>
-#endif
-
-using namespace chip::app::Clusters::WindowCovering;
-
-class WindowManager
-{
-public:
-    static WindowManager sWindow;
-    struct Timer
-    {
-        typedef void (*Callback)(Timer & timer);
-
-        Timer(uint32_t timeoutInMs, Callback callback, void * context);
-        ~Timer();
-
-        void Start();
-        void Stop();
-        void Timeout();
-
-        Callback mCallback = nullptr;
-        void * mContext    = nullptr;
-        bool mIsActive     = false;
-
-        osTimerId_t mHandler = nullptr;
-
-    private:
-        static void TimerCallback(void * timerCbArg);
-    };
-
-    struct Cover
-    {
-        enum ControlAction : uint8_t
-        {
-            Lift = 0,
-            Tilt = 1
-        };
-
-        void Init(chip::EndpointId endpoint);
-
-        /**
-         * @brief Schedule a lift or a tilt related attribute transition on the ChipEvent queue
-         * **This function allocates a CoverWorkData which needs to be freed by the Worker callback**
-         *
-         * @param action : ControlAction::Lift will ScheduleWork LiftUpdateWorker, while ControlAction::Tilt will ScheduleWork
-         * TilitUpdateWorker
-         * @param setNewTarget : True will stop any ongoing transition and start a new one. False will continue the active
-         * transition updates
-         */
-        void ScheduleControlAction(ControlAction action, bool setNewTarget);
-        // Helper functions that schedule Lift transitions
-        inline void LiftGoToTarget() { ScheduleControlAction(ControlAction::Lift, true); }
-        inline void LiftContinueToTarget() { ScheduleControlAction(ControlAction::Lift, false); }
-        // Helper functions that schedule Tilt transitions
-        inline void TiltGoToTarget() { ScheduleControlAction(ControlAction::Tilt, true); }
-        inline void TiltContinueToTarget() { ScheduleControlAction(ControlAction::Tilt, false); }
-
-        void PositionSet(chip::EndpointId endpointId, chip::Percent100ths position, ControlAction action);
-        void UpdateTargetPosition(OperationalState direction, ControlAction action);
-
-        Type CycleType();
-
-        static void OnLiftTimeout(Timer & timer);
-        static void OnTiltTimeout(Timer & timer);
-
-        chip::EndpointId mEndpoint = 0;
-
-        Timer * mLiftTimer = nullptr;
-        Timer * mTiltTimer = nullptr;
-
-        OperationalState mLiftOpState = OperationalState::Stall;
-        OperationalState mTiltOpState = OperationalState::Stall;
-
-        /**
-         * @brief Worker callbacks for the ScheduleControlAction.
-         * Those functions compute the operational state, and transititon movement based on the current and target positions
-         * for the cover.
-         * @param arg Context passed to the schedule worker. In this case, a CoverWorkData pointer
-         * The referenced CoverWorkData was allocated by ScheduleControlAction and must be freed by the worker.
-         */
-        static void LiftUpdateWorker(intptr_t arg);
-        static void TiltUpdateWorker(intptr_t arg);
-    };
-
-    struct CoverWorkData
-    {
-        Cover * cover     = nullptr;
-        bool setNewTarget = false;
-        CoverWorkData(Cover * c, bool t) : cover(c), setNewTarget(t) {}
-        ~CoverWorkData() { cover = nullptr; }
-    };
-
-    static WindowManager & Instance();
-
-    WindowManager();
-
-    CHIP_ERROR Init();
-    void PostAttributeChange(chip::EndpointId endpoint, chip::AttributeId attributeId);
-
-    static void ButtonEventHandler(uint8_t button, uint8_t btnAction);
-    void UpdateLED();
-
-#ifdef DISPLAY_ENABLED
-    static void DrawUI(GLIB_Context_t * glibContext);
-    void UpdateLCD();
-#endif // DISPLAY_ENABLED
-
-    static void GeneralEventHandler(AppEvent * aEvent);
-
-    static void OnIconTimeout(WindowManager::Timer & timer);
-
-protected:
-    Cover & GetCover();
-    Cover * GetCover(chip::EndpointId endpoint);
-
-    static void OnLongPressTimeout(Timer & timer);
-
-    Timer * mLongPressTimer = nullptr;
-    bool mTiltMode          = false;
-    bool mUpPressed         = false;
-    bool mDownPressed       = false;
-    bool mUpSuppressed      = false;
-    bool mDownSuppressed    = false;
-    bool mResetWarning      = false;
-
-private:
-    void HandleLongPress();
-    void DispatchEventAttributeChange(chip::EndpointId endpoint, chip::AttributeId attribute);
-
-    Cover mCoverList[WINDOW_COVER_COUNT];
-    uint8_t mCurrentCover = 0;
-
-    LEDWidget mActionLED;
-#ifdef DISPLAY_ENABLED
-    Timer * mIconTimer = nullptr;
-    LcdIcon mIcon      = LcdIcon::None;
-#endif
-};
diff --git a/include/device_config.h b/include/device_config.h
new file mode 100644
index 0000000..f6cb996
--- /dev/null
+++ b/include/device_config.h
@@ -0,0 +1,8 @@
+#ifndef _DEVICE_CONFIG_H_INCLUDE_
+#define _DEVICE_CONFIG_H_INCLUDE_
+
+#define MATTER_MAX_CURTAIN_NUM 2    /* 最大的窗帘数量 */
+#define MATTER_MAX_LIGHT_NUM 3      /* 最大的灯光数据 */
+#define CURTAIN_MAX_TIME_TASK_NUM 4 /* 每个窗帘最大的定时任务数量 */
+
+#endif /* _DEVICE_CONFIG_H_INCLUDE_ */
\ No newline at end of file
diff --git a/include/sl_openthread_application_config.h b/include/sl_openthread_application_config.h
new file mode 100644
index 0000000..bc59dc4
--- /dev/null
+++ b/include/sl_openthread_application_config.h
@@ -0,0 +1,24 @@
+/*
+ * sl_openthread-application-config.h
+ *
+ *  Created on: 2024年4月27日
+ *      Author: Zhenhua.Liang
+ *
+ *
+ *  Note: Define marco SL_OPENTHREAD_APPLICATION_CONFIG_FILE="sl_openthread-application-config.h" in project C/C++ setting to enable this feature
+ */
+
+#ifndef INCLUDE_SL_OPENTHREAD_APPLICATION_CONFIG_H_
+#define INCLUDE_SL_OPENTHREAD_APPLICATION_CONFIG_H_
+
+
+/**
+ * @def OPENTHREAD_CONFIG_DEFAULT_TRANSMIT_POWER
+ *
+ * The default IEEE 802.15.4 transmit power (dBm).
+ *
+ */
+#define OPENTHREAD_CONFIG_DEFAULT_TRANSMIT_POWER 10
+
+
+#endif /* INCLUDE_SL_OPENTHREAD_APPLICATION_CONFIG_H_ */
diff --git a/src/AppTask.cpp b/src/AppTask.cpp
deleted file mode 100644
index e7c12ce..0000000
--- a/src/AppTask.cpp
+++ /dev/null
@@ -1,113 +0,0 @@
-/*
- *
- *    Copyright (c) 2020 Project CHIP Authors
- *    Copyright (c) 2019 Google LLC.
- *    All rights reserved.
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#include "AppTask.h"
-#include "AppConfig.h"
-#include "AppEvent.h"
-
-#include "WindowManager.h"
-
-#include <app/server/OnboardingCodesUtil.h>
-#include <app/server/Server.h>
-#include <app/util/attribute-storage.h>
-
-#include <assert.h>
-
-#include <platform/silabs/platformAbstraction/SilabsPlatform.h>
-
-#include <setup_payload/QRCodeSetupPayloadGenerator.h>
-#include <setup_payload/SetupPayload.h>
-
-#include <lib/support/CodeUtils.h>
-
-using namespace chip;
-using namespace ::chip::DeviceLayer;
-using namespace ::chip::DeviceLayer::Silabs;
-
-using namespace chip::TLV;
-using namespace ::chip::DeviceLayer;
-
-AppTask AppTask::sAppTask;
-
-CHIP_ERROR AppTask::Init()
-{
-    CHIP_ERROR err = CHIP_NO_ERROR;
-    chip::DeviceLayer::Silabs::GetPlatform().SetButtonsCb(WindowManager::ButtonEventHandler);
-
-#ifdef DISPLAY_ENABLED
-    GetLCD().Init((uint8_t *) "Window-App");
-    GetLCD().SetCustomUI(WindowManager::DrawUI);
-#endif
-
-    err = BaseApplication::Init();
-    if (err != CHIP_NO_ERROR)
-    {
-        SILABS_LOG("BaseApplication::Init() failed");
-        appError(err);
-    }
-
-    err = WindowManager::sWindow.Init();
-
-    if (err != CHIP_NO_ERROR)
-    {
-        SILABS_LOG("WindowMgr::Init() failed");
-        appError(err);
-    }
-
-    return err;
-}
-
-CHIP_ERROR AppTask::StartAppTask()
-{
-    return BaseApplication::StartAppTask(AppTaskMain);
-}
-
-void AppTask::AppTaskMain(void * pvParameter)
-{
-    AppEvent event;
-    osMessageQueueId_t sAppEventQueue = *(static_cast<osMessageQueueId_t *>(pvParameter));
-
-    CHIP_ERROR err = sAppTask.Init();
-    if (err != CHIP_NO_ERROR)
-    {
-        SILABS_LOG("AppTask.Init() failed");
-        appError(err);
-    }
-
-#if !(defined(CHIP_CONFIG_ENABLE_ICD_SERVER) && CHIP_CONFIG_ENABLE_ICD_SERVER)
-    sAppTask.StartStatusLEDTimer();
-#endif
-
-    SILABS_LOG("App Task started");
-
-    WindowManager::sWindow.UpdateLED();
-#ifdef DISPLAY_ENABLED
-    WindowManager::sWindow.UpdateLCD();
-#endif // DISPLAY_ENABLED
-
-    while (true)
-    {
-        osStatus_t eventReceived = osMessageQueueGet(sAppEventQueue, &event, NULL, osWaitForever);
-        while (eventReceived == osOK)
-        {
-            sAppTask.DispatchEvent(&event);
-            eventReceived = osMessageQueueGet(sAppEventQueue, &event, NULL, 0);
-        }
-    }
-}
diff --git a/src/WindowManager.cpp b/src/WindowManager.cpp
deleted file mode 100644
index df32812..0000000
--- a/src/WindowManager.cpp
+++ /dev/null
@@ -1,807 +0,0 @@
-/*
- *
- *    Copyright (c) 2021 Project CHIP Authors
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-#include "AppEvent.h"
-#include "AppTask.h"
-#include <AppConfig.h>
-#include <app-common/zap-generated/attributes/Accessors.h>
-#include <app/server/Server.h>
-
-#include <lib/support/CodeUtils.h>
-#include <platform/CHIPDeviceLayer.h>
-
-#include <WindowManager.h>
-
-#include <app/clusters/window-covering-server/window-covering-server.h>
-#include <app/server/OnboardingCodesUtil.h>
-#include <cmsis_os2.h>
-#include <lib/core/CHIPError.h>
-#include <lib/dnssd/Advertiser.h>
-#include <lib/support/CodeUtils.h>
-#include <platform/CHIPDeviceLayer.h>
-
-#ifdef SL_WIFI
-#include <app/clusters/network-commissioning/network-commissioning.h>
-#include <platform/silabs/NetworkCommissioningWiFiDriver.h>
-#include <platform/silabs/wifi/WifiInterfaceAbstraction.h>
-#endif
-
-#ifdef DISPLAY_ENABLED
-#include <LcdPainter.h>
-#endif
-
-#include <platform/silabs/platformAbstraction/SilabsPlatform.h>
-
-#define LCD_ICON_TIMEOUT 1000
-
-using namespace chip::app::Clusters::WindowCovering;
-using namespace chip;
-using namespace ::chip::DeviceLayer;
-using namespace ::chip::DeviceLayer::Silabs;
-#define APP_ACTION_LED 1
-
-#ifdef DIC_ENABLE
-#define DECIMAL 10
-#define MSG_SIZE 6
-#include "dic.h"
-#endif // DIC_ENABLE
-
-using namespace ::chip::Credentials;
-using namespace ::chip::DeviceLayer;
-using namespace chip::app::Clusters::WindowCovering;
-
-WindowManager WindowManager::sWindow;
-
-AppEvent CreateNewEvent(AppEvent::AppEventTypes type)
-{
-    AppEvent aEvent;
-    aEvent.Type                = type;
-    aEvent.Handler             = WindowManager::GeneralEventHandler;
-    WindowManager * window     = static_cast<WindowManager *>(&WindowManager::sWindow);
-    aEvent.WindowEvent.Context = window;
-    return aEvent;
-}
-
-void WindowManager::Timer::Start()
-{
-    // Starts or restarts the function timer
-    if (osTimerStart(mHandler, pdMS_TO_TICKS(100)) != osOK)
-    {
-        SILABS_LOG("Timer start() failed");
-        appError(CHIP_ERROR_INTERNAL);
-    }
-
-    mIsActive = true;
-}
-
-void WindowManager::Timer::Timeout()
-{
-    mIsActive = false;
-    if (mCallback)
-    {
-        mCallback(*this);
-    }
-}
-
-WindowManager::Cover & WindowManager::GetCover()
-{
-    return mCoverList[mCurrentCover];
-}
-
-WindowManager::Cover * WindowManager::GetCover(chip::EndpointId endpoint)
-{
-    for (uint16_t i = 0; i < WINDOW_COVER_COUNT; ++i)
-    {
-        if (mCoverList[i].mEndpoint == endpoint)
-        {
-            return &mCoverList[i];
-        }
-    }
-    return nullptr;
-}
-
-void WindowManager::DispatchEventAttributeChange(chip::EndpointId endpoint, chip::AttributeId attribute)
-{
-    Cover * cover = GetCover(endpoint);
-    chip::BitMask<Mode> mode;
-    chip::BitMask<ConfigStatus> configStatus;
-    chip::BitMask<OperationalStatus> opStatus;
-
-    if (nullptr == cover)
-    {
-        ChipLogProgress(Zcl, "Ep[%u] not supported AttributeId=%u\n", endpoint, (unsigned int) attribute);
-        return;
-    }
-
-    switch (attribute)
-    {
-    /* For a device supporting Position Awareness : Changing the Target triggers motions on the real or simulated device */
-    case Attributes::TargetPositionLiftPercent100ths::Id:
-        cover->LiftGoToTarget();
-        break;
-    /* For a device supporting Position Awareness : Changing the Target triggers motions on the real or simulated device */
-    case Attributes::TargetPositionTiltPercent100ths::Id:
-        cover->TiltGoToTarget();
-        break;
-    /* RO OperationalStatus */
-    case Attributes::OperationalStatus::Id:
-        chip::DeviceLayer::PlatformMgr().LockChipStack();
-        opStatus = OperationalStatusGet(endpoint);
-        OperationalStatusPrint(opStatus);
-        chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-        UpdateLED();
-        break;
-    /* RW Mode */
-    case Attributes::Mode::Id:
-        chip::DeviceLayer::PlatformMgr().LockChipStack();
-        mode = ModeGet(endpoint);
-        ModePrint(mode);
-        ModeSet(endpoint, mode); // refilter mode if needed
-        chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-        break;
-    /* RO ConfigStatus: set by WC server */
-    case Attributes::ConfigStatus::Id:
-        chip::DeviceLayer::PlatformMgr().LockChipStack();
-        configStatus = ConfigStatusGet(endpoint);
-        ConfigStatusPrint(configStatus);
-        chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-        break;
-    /* ### ATTRIBUTEs CHANGEs IGNORED ### */
-    /* RO Type: not supposed to dynamically change */
-    case Attributes::Type::Id:
-    /* RO EndProductType: not supposed to dynamically change */
-    case Attributes::EndProductType::Id:
-    /* RO SafetyStatus: set by WC server */
-    case Attributes::SafetyStatus::Id:
-    /* ============= Positions for Position Aware ============= */
-    case Attributes::CurrentPositionLiftPercent100ths::Id:
-    case Attributes::CurrentPositionTiltPercent100ths::Id:
-        UpdateLED();
-#ifdef DISPLAY_ENABLED
-        UpdateLCD();
-#endif // DISPLAY_ENABLED
-        break;
-    default:
-        break;
-    }
-}
-
-void WindowManager::HandleLongPress()
-{
-
-    AppEvent event;
-    event.Handler             = GeneralEventHandler;
-    WindowManager * window    = static_cast<WindowManager *>(&WindowManager::sWindow);
-    event.WindowEvent.Context = window;
-
-    if (mUpPressed && mDownPressed)
-    {
-        // Long press both buttons: Cycle between window coverings
-        mUpSuppressed = mDownSuppressed = true;
-        mCurrentCover                   = mCurrentCover < WINDOW_COVER_COUNT - 1 ? mCurrentCover + 1 : 0;
-        event.Type                      = AppEvent::kEventType_CoverChange;
-        AppTask::GetAppTask().PostEvent(&event);
-        ChipLogDetail(AppServer, "App controls set to cover %d", mCurrentCover + 1);
-    }
-    else if (mUpPressed)
-    {
-        mUpSuppressed = true;
-        if (!mResetWarning)
-        {
-            // Long press button up: Reset warning!
-            event.Type = AppEvent::kEventType_ResetWarning;
-            AppTask::GetAppTask().PostEvent(&event);
-        }
-    }
-    else if (mDownPressed)
-    {
-        // Long press button down: Cycle between covering types
-        mDownSuppressed = true;
-        Type type       = GetCover().CycleType();
-        mTiltMode       = mTiltMode && (Type::kTiltBlindLiftAndTilt == type);
-        ChipLogDetail(AppServer, "Cover type changed to %d", to_underlying(type));
-    }
-}
-
-void WindowManager::OnLongPressTimeout(WindowManager::Timer & timer)
-{
-    WindowManager * app = static_cast<WindowManager *>(timer.mContext);
-    if (app)
-    {
-        app->HandleLongPress();
-    }
-}
-
-void WindowManager::Cover::Init(chip::EndpointId endpoint)
-{
-    mEndpoint  = endpoint;
-    mLiftTimer = new Timer(COVER_LIFT_TILT_TIMEOUT, OnLiftTimeout, this);
-    mTiltTimer = new Timer(COVER_LIFT_TILT_TIMEOUT, OnTiltTimeout, this);
-
-    // Preset Lift attributes
-    Attributes::InstalledOpenLimitLift::Set(endpoint, LIFT_OPEN_LIMIT);
-    Attributes::InstalledClosedLimitLift::Set(endpoint, LIFT_CLOSED_LIMIT);
-
-    // Preset Tilt attributes
-    Attributes::InstalledOpenLimitTilt::Set(endpoint, TILT_OPEN_LIMIT);
-    Attributes::InstalledClosedLimitTilt::Set(endpoint, TILT_CLOSED_LIMIT);
-
-    // Note: All Current Positions are preset via Zap config and kept across reboot via NVM: no need to init them
-
-    // Attribute: Id  0 Type
-    TypeSet(endpoint, Type::kTiltBlindLiftAndTilt);
-
-    // Attribute: Id  7 ConfigStatus
-    chip::BitMask<ConfigStatus> configStatus = ConfigStatusGet(endpoint);
-    configStatus.Set(ConfigStatus::kLiftEncoderControlled);
-    configStatus.Set(ConfigStatus::kTiltEncoderControlled);
-    ConfigStatusSet(endpoint, configStatus);
-
-    chip::app::Clusters::WindowCovering::ConfigStatusUpdateFeatures(endpoint);
-
-    // Attribute: Id 13 EndProductType
-    EndProductTypeSet(endpoint, EndProductType::kInteriorBlind);
-
-    // Attribute: Id 24 Mode
-    chip::BitMask<Mode> mode;
-    mode.Clear(Mode::kMotorDirectionReversed);
-    mode.Clear(Mode::kMaintenanceMode);
-    mode.Clear(Mode::kCalibrationMode);
-    mode.Set(Mode::kLedFeedback);
-
-    /* Mode also update ConfigStatus accordingly */
-    ModeSet(endpoint, mode);
-
-    // Attribute: Id 27 SafetyStatus (Optional)
-    chip::BitFlags<SafetyStatus> safetyStatus(0x00); // 0 is no issues;
-}
-
-void WindowManager::Cover::ScheduleControlAction(ControlAction action, bool setNewTarget)
-{
-    VerifyOrReturn(action <= ControlAction::Tilt);
-    // Allocate a CoverWorkData. It will be freed by the Worker callback
-    CoverWorkData * data = new CoverWorkData(this, setNewTarget);
-    VerifyOrDie(data != nullptr);
-
-    AsyncWorkFunct workFunct = (action == ControlAction::Lift) ? LiftUpdateWorker : TiltUpdateWorker;
-    if (PlatformMgr().ScheduleWork(workFunct, reinterpret_cast<intptr_t>(data)) != CHIP_NO_ERROR)
-    {
-        ChipLogError(AppServer, "Failed to schedule cover control action");
-        delete data;
-    }
-}
-
-void WindowManager::Cover::LiftUpdateWorker(intptr_t arg)
-{
-    // Use a unique_prt so it's freed when leaving this context
-    std::unique_ptr<CoverWorkData> data(reinterpret_cast<CoverWorkData *>(arg));
-    Cover * cover = data->cover;
-
-    NPercent100ths current, target;
-
-    VerifyOrReturn(Attributes::TargetPositionLiftPercent100ths::Get(cover->mEndpoint, target) ==
-                   Protocols::InteractionModel::Status::Success);
-    VerifyOrReturn(Attributes::CurrentPositionLiftPercent100ths::Get(cover->mEndpoint, current) ==
-                   Protocols::InteractionModel::Status::Success);
-
-    OperationalState opState = ComputeOperationalState(target, current);
-
-    // If Triggered by a TARGET update
-    if (data->setNewTarget)
-    {
-        cover->mLiftTimer->Stop(); // Cancel previous motion if any
-        cover->mLiftOpState = opState;
-    }
-
-    if (cover->mLiftOpState == opState)
-    {
-        // Actuator still needs to move, has not reached/crossed Target yet
-        chip::Percent100ths percent100ths;
-
-        if (!current.IsNull())
-        {
-            percent100ths = ComputePercent100thsStep(cover->mLiftOpState, current.Value(), LIFT_DELTA);
-        }
-        else
-        {
-            percent100ths = WC_PERCENT100THS_MIDDLE; // set at middle by default
-        }
-
-        cover->PositionSet(cover->mEndpoint, percent100ths, ControlAction::Lift);
-    }
-    else // CURRENT reached TARGET or crossed it
-    {
-        // Actuator finalize the movement AND CURRENT Must be equal to TARGET at the end
-        if (!target.IsNull())
-            cover->PositionSet(cover->mEndpoint, target.Value(), ControlAction::Lift);
-
-        cover->mLiftOpState = OperationalState::Stall;
-    }
-
-    OperationalStateSet(cover->mEndpoint, OperationalStatus::kLift, cover->mLiftOpState);
-
-    if ((OperationalState::Stall != cover->mLiftOpState) && cover->mLiftTimer)
-    {
-        cover->mLiftTimer->Start();
-    }
-}
-
-void WindowManager::Cover::TiltUpdateWorker(intptr_t arg)
-{
-    // Use a unique_prt so it's freed when leaving this context
-    std::unique_ptr<CoverWorkData> data(reinterpret_cast<CoverWorkData *>(arg));
-    Cover * cover = data->cover;
-
-    NPercent100ths current, target;
-    VerifyOrReturn(Attributes::TargetPositionTiltPercent100ths::Get(cover->mEndpoint, target) ==
-                   Protocols::InteractionModel::Status::Success);
-    VerifyOrReturn(Attributes::CurrentPositionTiltPercent100ths::Get(cover->mEndpoint, current) ==
-                   Protocols::InteractionModel::Status::Success);
-
-    OperationalState opState = ComputeOperationalState(target, current);
-
-    // If Triggered by a TARGET update
-    if (data->setNewTarget)
-    {
-        cover->mTiltTimer->Stop(); // Cancel previous motion if any
-        cover->mTiltOpState = opState;
-    }
-
-    if (cover->mTiltOpState == opState)
-    {
-        // Actuator still needs to move, has not reached/crossed Target yet
-        chip::Percent100ths percent100ths;
-
-        if (!current.IsNull())
-        {
-            percent100ths = ComputePercent100thsStep(cover->mTiltOpState, current.Value(), TILT_DELTA);
-        }
-        else
-        {
-            percent100ths = WC_PERCENT100THS_MIDDLE; // set at middle by default
-        }
-
-        cover->PositionSet(cover->mEndpoint, percent100ths, ControlAction::Tilt);
-    }
-    else // CURRENT reached TARGET or crossed it
-    {
-        // Actuator finalize the movement AND CURRENT Must be equal to TARGET at the end
-        if (!target.IsNull())
-            cover->PositionSet(cover->mEndpoint, target.Value(), ControlAction::Tilt);
-
-        cover->mTiltOpState = OperationalState::Stall;
-    }
-
-    OperationalStateSet(cover->mEndpoint, OperationalStatus::kTilt, cover->mTiltOpState);
-
-    if ((OperationalState::Stall != cover->mTiltOpState) && cover->mTiltTimer)
-    {
-        cover->mTiltTimer->Start();
-    }
-}
-
-void WindowManager::Cover::UpdateTargetPosition(OperationalState direction, ControlAction action)
-{
-    Protocols::InteractionModel::Status status;
-    NPercent100ths current;
-    chip::Percent100ths target;
-
-    chip::DeviceLayer::PlatformMgr().LockChipStack();
-
-    if (action == ControlAction::Tilt)
-    {
-        status = Attributes::CurrentPositionTiltPercent100ths::Get(mEndpoint, current);
-        if ((status == Protocols::InteractionModel::Status::Success) && !current.IsNull())
-        {
-            target = ComputePercent100thsStep(direction, current.Value(), TILT_DELTA);
-            (void) Attributes::TargetPositionTiltPercent100ths::Set(mEndpoint, target);
-        }
-    }
-    else
-    {
-        status = Attributes::CurrentPositionLiftPercent100ths::Get(mEndpoint, current);
-        if ((status == Protocols::InteractionModel::Status::Success) && !current.IsNull())
-        {
-            target = ComputePercent100thsStep(direction, current.Value(), LIFT_DELTA);
-            (void) Attributes::TargetPositionLiftPercent100ths::Set(mEndpoint, target);
-        }
-    }
-    chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-}
-
-Type WindowManager::Cover::CycleType()
-{
-    chip::DeviceLayer::PlatformMgr().LockChipStack();
-    Type type = TypeGet(mEndpoint);
-    chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-
-    switch (type)
-    {
-    case Type::kRollerShade:
-        type = Type::kDrapery;
-        // tilt = false;
-        break;
-    case Type::kDrapery:
-        type = Type::kTiltBlindLiftAndTilt;
-        break;
-    case Type::kTiltBlindLiftAndTilt:
-        type = Type::kRollerShade;
-        // tilt = false;
-        break;
-    default:
-        type = Type::kTiltBlindLiftAndTilt;
-    }
-
-    chip::DeviceLayer::PlatformMgr().LockChipStack();
-    TypeSet(mEndpoint, type);
-    chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-
-    return type;
-}
-
-void WindowManager::Cover::OnLiftTimeout(WindowManager::Timer & timer)
-{
-    WindowManager::Cover * cover = static_cast<WindowManager::Cover *>(timer.mContext);
-    if (cover)
-    {
-        cover->LiftContinueToTarget();
-    }
-}
-
-void WindowManager::Cover::OnTiltTimeout(WindowManager::Timer & timer)
-{
-    WindowManager::Cover * cover = static_cast<WindowManager::Cover *>(timer.mContext);
-    if (cover)
-    {
-        cover->TiltContinueToTarget();
-    }
-}
-
-void WindowManager::Cover::PositionSet(chip::EndpointId endpointId, chip::Percent100ths position, ControlAction action)
-{
-    NPercent100ths nullablePosition;
-    nullablePosition.SetNonNull(position);
-    if (action == ControlAction::Tilt)
-    {
-        TiltPositionSet(endpointId, nullablePosition);
-#ifdef DIC_ENABLE
-        uint16_t value = position;
-        char buffer[MSG_SIZE];
-        itoa(value, buffer, DECIMAL);
-        dic_sendmsg("tilt/position set", (const char *) (buffer));
-#endif // DIC_ENABLE
-    }
-    else
-    {
-        LiftPositionSet(endpointId, nullablePosition);
-#ifdef DIC_ENABLE
-        uint16_t value = position;
-        char buffer[MSG_SIZE];
-        itoa(value, buffer, DECIMAL);
-        dic_sendmsg("lift/position set", (const char *) (buffer));
-#endif // DIC_ENABLE
-    }
-}
-
-//------------------------------------------------------------------------------
-// Timers
-//------------------------------------------------------------------------------
-
-WindowManager::Timer::Timer(uint32_t timeoutInMs, Callback callback, void * context) : mCallback(callback), mContext(context)
-{
-    mHandler = osTimerNew(TimerCallback, // timer callback handler
-                          osTimerOnce,   // no timer reload (one-shot timer)
-                          this,          // pass the app task obj context
-                          NULL           // No osTimerAttr_t to provide.
-    );
-
-    if (mHandler == NULL)
-    {
-        SILABS_LOG("Timer create failed");
-        appError(CHIP_ERROR_INTERNAL);
-    }
-}
-
-WindowManager::Timer::~Timer()
-{
-    if (mHandler)
-    {
-        osTimerDelete(mHandler);
-        mHandler = nullptr;
-    }
-}
-
-void WindowManager::Timer::Stop()
-{
-    mIsActive = false;
-    if (osTimerStop(mHandler) == osError)
-    {
-        SILABS_LOG("Timer stop() failed");
-        appError(CHIP_ERROR_INTERNAL);
-    }
-}
-
-void WindowManager::Timer::TimerCallback(void * timerCbArg)
-{
-    Timer * timer = static_cast<Timer *>(timerCbArg);
-    if (timer)
-    {
-        timer->Timeout();
-    }
-}
-
-WindowManager & WindowManager::Instance()
-{
-    return WindowManager::sWindow;
-}
-
-WindowManager::WindowManager() {}
-
-void WindowManager::OnIconTimeout(WindowManager::Timer & timer)
-{
-#ifdef DISPLAY_ENABLED
-    sWindow.mIcon = LcdIcon::None;
-    sWindow.UpdateLCD();
-#endif // DISPLAY_ENABLED
-}
-
-CHIP_ERROR WindowManager::Init()
-{
-    chip::DeviceLayer::PlatformMgr().LockChipStack();
-
-#ifdef DISPLAY_ENABLED
-    mIconTimer = new Timer(LCD_ICON_TIMEOUT, OnIconTimeout, this);
-#endif
-    // Timers
-    mLongPressTimer = new Timer(LONG_PRESS_TIMEOUT, OnLongPressTimeout, this);
-
-    // Coverings
-    mCoverList[0].Init(WINDOW_COVER_ENDPOINT1);
-    mCoverList[1].Init(WINDOW_COVER_ENDPOINT2);
-
-    // Initialize LEDs
-    LEDWidget::InitGpio();
-    mActionLED.Init(APP_ACTION_LED);
-    AppTask::GetAppTask().LinkAppLed(&mActionLED);
-
-    chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-
-    return CHIP_NO_ERROR;
-}
-
-void WindowManager::PostAttributeChange(chip::EndpointId endpoint, chip::AttributeId attributeId)
-{
-    AppEvent event     = CreateNewEvent(AppEvent::kEventType_AttributeChange);
-    event.mEndpoint    = endpoint;
-    event.mAttributeId = attributeId;
-    AppTask::GetAppTask().PostEvent(&event);
-}
-
-void WindowManager::UpdateLED()
-{
-    Cover & cover = GetCover();
-    if (mResetWarning)
-    {
-        mActionLED.Set(false);
-        mActionLED.Blink(500);
-    }
-    else
-    {
-        // Action LED
-        NPercent100ths current;
-        LimitStatus liftLimit = LimitStatus::Intermediate;
-
-        chip::DeviceLayer::PlatformMgr().LockChipStack();
-        Attributes::CurrentPositionLiftPercent100ths::Get(cover.mEndpoint, current);
-        chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-
-        if (!current.IsNull())
-        {
-            AbsoluteLimits limits = { .open = WC_PERCENT100THS_MIN_OPEN, .closed = WC_PERCENT100THS_MAX_CLOSED };
-            liftLimit             = CheckLimitState(current.Value(), limits);
-        }
-
-        if (OperationalState::Stall != cover.mLiftOpState)
-        {
-            mActionLED.Blink(100);
-        }
-        else if (LimitStatus::IsUpOrOpen == liftLimit)
-        {
-            mActionLED.Set(true);
-        }
-        else if (LimitStatus::IsDownOrClose == liftLimit)
-        {
-            mActionLED.Set(false);
-        }
-        else
-        {
-            mActionLED.Blink(1000);
-        }
-    }
-}
-
-#ifdef DISPLAY_ENABLED
-void WindowManager::DrawUI(GLIB_Context_t * glibContext)
-{
-    sWindow.UpdateLCD();
-}
-
-void WindowManager::UpdateLCD()
-{
-    // Update LCD
-    if (BaseApplication::GetProvisionStatus())
-    {
-        Cover & cover = GetCover();
-        chip::app::DataModel::Nullable<uint16_t> lift;
-        chip::app::DataModel::Nullable<uint16_t> tilt;
-
-        chip::DeviceLayer::PlatformMgr().LockChipStack();
-        Type type = TypeGet(cover.mEndpoint);
-
-        Attributes::CurrentPositionLift::Get(cover.mEndpoint, lift);
-        Attributes::CurrentPositionTilt::Get(cover.mEndpoint, tilt);
-        chip::DeviceLayer::PlatformMgr().UnlockChipStack();
-
-        if (!tilt.IsNull() && !lift.IsNull())
-        {
-            LcdPainter::Paint(AppTask::GetAppTask().GetLCD(), type, lift.Value(), tilt.Value(), mIcon);
-        }
-    }
-}
-#endif // DISPLAY_ENABLED
-
-// Silabs button callback from button event ISR
-void WindowManager::ButtonEventHandler(uint8_t button, uint8_t btnAction)
-{
-    AppEvent event;
-
-    if (btnAction == static_cast<uint8_t>(SilabsPlatform::ButtonAction::ButtonPressed))
-    {
-        event = CreateNewEvent(button ? AppEvent::kEventType_DownPressed : AppEvent::kEventType_UpPressed);
-    }
-    else
-    {
-        event = CreateNewEvent(button ? AppEvent::kEventType_DownReleased : AppEvent::kEventType_UpReleased);
-    }
-
-    AppTask::GetAppTask().PostEvent(&event);
-}
-
-void WindowManager::GeneralEventHandler(AppEvent * aEvent)
-{
-    WindowManager * window = static_cast<WindowManager *>(aEvent->WindowEvent.Context);
-
-    switch (aEvent->Type)
-    {
-    case AppEvent::kEventType_ResetWarning:
-        window->mResetWarning = true;
-        AppTask::GetAppTask().StartFactoryResetSequence();
-        window->UpdateLED();
-        break;
-
-    case AppEvent::kEventType_ResetCanceled:
-        window->mResetWarning = false;
-        AppTask::GetAppTask().CancelFactoryResetSequence();
-        window->UpdateLED();
-        break;
-
-    case AppEvent::kEventType_UpPressed:
-        window->mUpPressed = true;
-        if (window->mLongPressTimer)
-        {
-            window->mLongPressTimer->Start();
-        }
-        break;
-
-    case AppEvent::kEventType_UpReleased:
-        window->mUpPressed = false;
-        if (window->mLongPressTimer)
-        {
-            window->mLongPressTimer->Stop();
-        }
-        if (window->mResetWarning)
-        {
-            aEvent->Type = AppEvent::kEventType_ResetCanceled;
-            AppTask::GetAppTask().PostEvent(aEvent);
-        }
-        if (window->mUpSuppressed)
-        {
-            window->mUpSuppressed = false;
-        }
-        else if (window->mDownPressed)
-        {
-            window->mTiltMode       = !(window->mTiltMode);
-            window->mDownSuppressed = true;
-            aEvent->Type            = AppEvent::kEventType_TiltModeChange;
-            AppTask::GetAppTask().PostEvent(aEvent);
-        }
-        else
-        {
-            window->GetCover().UpdateTargetPosition(
-                OperationalState::MovingUpOrOpen, ((window->mTiltMode) ? Cover::ControlAction::Tilt : Cover::ControlAction::Lift));
-        }
-        break;
-
-    case AppEvent::kEventType_DownPressed:
-        window->mDownPressed = true;
-        if (window->mLongPressTimer)
-        {
-            window->mLongPressTimer->Start();
-        }
-        break;
-
-    case AppEvent::kEventType_DownReleased:
-        window->mDownPressed = false;
-        if (window->mLongPressTimer)
-        {
-            window->mLongPressTimer->Stop();
-        }
-        if (window->mResetWarning)
-        {
-            aEvent->Type = AppEvent::kEventType_ResetCanceled;
-            AppTask::GetAppTask().PostEvent(aEvent);
-        }
-        if (window->mDownSuppressed)
-        {
-            window->mDownSuppressed = false;
-        }
-        else if (window->mUpPressed)
-        {
-            window->mTiltMode     = !(window->mTiltMode);
-            window->mUpSuppressed = true;
-            aEvent->Type          = AppEvent::kEventType_TiltModeChange;
-            AppTask::GetAppTask().PostEvent(aEvent);
-        }
-        else
-        {
-            window->GetCover().UpdateTargetPosition(
-                OperationalState::MovingDownOrClose,
-                ((window->mTiltMode) ? Cover::ControlAction::Tilt : Cover::ControlAction::Lift));
-        }
-        break;
-
-    case AppEvent::kEventType_AttributeChange:
-        window->DispatchEventAttributeChange(aEvent->mEndpoint, aEvent->mAttributeId);
-        break;
-
-#ifdef DISPLAY_ENABLED
-    case AppEvent::kEventType_CoverTypeChange:
-        window->UpdateLCD();
-        break;
-    case AppEvent::kEventType_CoverChange:
-        if (window->mIconTimer != nullptr)
-        {
-            window->mIconTimer->Start();
-        }
-        window->mIcon = (window->GetCover().mEndpoint == 1) ? LcdIcon::One : LcdIcon::Two;
-        window->UpdateLCD();
-        break;
-    case AppEvent::kEventType_TiltModeChange:
-        ChipLogDetail(AppServer, "App control mode changed to %s", window->mTiltMode ? "Tilt" : "Lift");
-        if (window->mIconTimer != nullptr)
-        {
-            window->mIconTimer->Start();
-        }
-        window->mIcon = window->mTiltMode ? LcdIcon::Tilt : LcdIcon::Lift;
-        window->UpdateLCD();
-        break;
-#endif // DISPLAY_ENABLED
-
-    default:
-        break;
-    }
-}
diff --git a/src/ZclCallbacks.cpp b/src/ZclCallbacks.cpp
deleted file mode 100644
index f658a45..0000000
--- a/src/ZclCallbacks.cpp
+++ /dev/null
@@ -1,57 +0,0 @@
-/*
- *
- *    Copyright (c) 2021 Project CHIP Authors
- *
- *    Licensed under the Apache License, Version 2.0 (the "License");
- *    you may not use this file except in compliance with the License.
- *    You may obtain a copy of the License at
- *
- *        http://www.apache.org/licenses/LICENSE-2.0
- *
- *    Unless required by applicable law or agreed to in writing, software
- *    distributed under the License is distributed on an "AS IS" BASIS,
- *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
- *    See the License for the specific language governing permissions and
- *    limitations under the License.
- */
-
-/**
- * @file
- *   This file implements the handler for data model messages.
- */
-
-#include <AppConfig.h>
-#include <WindowManager.h>
-
-#include <app-common/zap-generated/attributes/Accessors.h>
-#include <app-common/zap-generated/callback.h>
-#include <app-common/zap-generated/cluster-objects.h>
-#include <app-common/zap-generated/ids/Attributes.h>
-#include <app-common/zap-generated/ids/Clusters.h>
-#include <app/CommandHandler.h>
-#include <app/ConcreteAttributePath.h>
-#include <app/ConcreteCommandPath.h>
-#include <app/clusters/window-covering-server/window-covering-server.h>
-
-using namespace ::chip;
-using namespace ::chip::app::Clusters::WindowCovering;
-
-void MatterPostAttributeChangeCallback(const app::ConcreteAttributePath & attributePath, uint8_t type, uint16_t size,
-                                       uint8_t * value)
-{
-    switch (attributePath.mClusterId)
-    {
-    case app::Clusters::Identify::Id:
-        ChipLogProgress(Zcl, "Identify cluster ID: " ChipLogFormatMEI " Type: %u Value: %u, length %u",
-                        ChipLogValueMEI(attributePath.mAttributeId), type, *value, size);
-        break;
-    default:
-        break;
-    }
-}
-
-/* Forwards all attributes changes */
-void MatterWindowCoveringClusterServerAttributeChangedCallback(const app::ConcreteAttributePath & attributePath)
-{
-    WindowManager::Instance().PostAttributeChange(attributePath.mEndpointId, attributePath.mAttributeId);
-}
```