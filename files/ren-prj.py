#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from pathlib import Path

def walk_and_replace(target_dir, old_str, new_str):
    """
    递归遍历目录并替换文件名和文件内容
    """
    target_path = Path(target_dir).resolve()
    
    if not target_path.exists() or not target_path.is_dir():
        print(f"错误: 无效的目录 - {target_dir}")
        return False
    
    print(f"处理目录: {target_path}")
    print(f"替换规则: '{old_str}' -> '{new_str}'")
    
    renamed_files = 0
    modified_files = 0
    script_name = os.path.basename(__file__)
    
    for root, dirs, files in os.walk(target_path):
        root_path = Path(root)
        
        for file in files:
            file_path = root_path / file
            
            # 跳过脚本本身
            if file_path.name == script_name:
                continue
            
            # 处理文件内容
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                if old_str.encode('utf-8') in content:
                    new_content = content.replace(old_str.encode('utf-8'), new_str.encode('utf-8'))
                    with open(file_path, 'wb') as f:
                        f.write(new_content)
                    print(f"已修改内容: {file_path}")
                    modified_files += 1
                    
            except Exception as e:
                print(f"处理内容失败 {file_path}: {e}")
            
            # 处理文件名
            if old_str in file_path.name:
                new_name = file_path.name.replace(old_str, new_str)
                new_path = file_path.parent / new_name
                try:
                    file_path.rename(new_path)
                    print(f"已重命名: {file_path} -> {new_path}")
                    renamed_files += 1
                except Exception as e:
                    print(f"重命名失败 {file_path}: {e}")
    
    print(f"\n处理完成!")
    print(f"修改内容的文件数: {modified_files}")
    print(f"重命名的文件数: {renamed_files}")
    return True

def main():
    parser = argparse.ArgumentParser(description='批量替换文件内容和文件名中的字符串')
    parser.add_argument('target_dir', nargs='?', help='要处理的目录路径')
    parser.add_argument('-o', '--old', default='aok04_matter_dc', help='要替换的旧字符串 (默认: aok04_matter_dc)')
    parser.add_argument('-n', '--new', default='bk01_matter_dc', help='替换后的新字符串 (默认: bk01_matter_dc)')
    parser.add_argument('-y', '--yes', action='store_true', help='自动确认，不提示')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("文件批量替换工具")
    print(f"将 '{args.old}' 替换为 '{args.new}'")
    print("=" * 60)
    print("注意：此操作不可撤销！")
    
    # 获取目标目录
    target_dir = args.target_dir
    if not target_dir:
        target_dir = input("\n请输入要处理的目录路径: ").strip()
        if not target_dir:
            print("未指定目录，退出程序")
            return
    
    print(f"\n目标目录: {target_dir}")
    print(f"替换规则: '{args.old}' -> '{args.new}'")
    
    # 确认操作
    if not args.yes:
        response = input("\n确认继续？(y/n): ")
        if response.lower() != 'y':
            print("操作已取消")
            return
    
    walk_and_replace(target_dir, args.old, args.new)

if __name__ == "__main__":
    main()