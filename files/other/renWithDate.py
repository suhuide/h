import os
import datetime
import argparse
from pathlib import Path

def get_file_modification_time(filepath):
    """
    获取文件的修改时间
    
    Args:
        filepath: 文件路径
    
    Returns:
        修改时间的datetime对象
    """
    # 获取文件修改时间戳
    timestamp = os.path.getmtime(filepath)
    # 转换为datetime对象
    return datetime.datetime.fromtimestamp(timestamp)

def add_timestamp_to_filename(filepath, timestamp_format="%Y%m%d%H%M", separator="-", use_modify_time=True):
    """
    给文件名添加时间戳
    
    Args:
        filepath: 文件路径
        timestamp_format: 时间戳格式，默认：年月日时分
        separator: 分隔符，默认为"-"
        use_modify_time: 是否使用修改时间，True使用修改时间，False使用当前时间
    
    Returns:
        添加时间戳后的文件名（不包含路径）
    """
    # 获取文件名和路径
    path = Path(filepath)
    filename = path.name
    directory = path.parent
    
    # 分离文件名和扩展名
    name, ext = os.path.splitext(filename)
    
    # 获取时间
    if use_modify_time and os.path.exists(filepath):
        # 使用文件的修改时间
        file_time = get_file_modification_time(filepath)
        timestamp = file_time.strftime(timestamp_format)
    else:
        # 使用当前时间
        now = datetime.datetime.now()
        timestamp = now.strftime(timestamp_format)
    
    # 添加时间戳
    new_filename = f"{name}{separator}{timestamp}{ext}"
    
    return new_filename

def get_file_info(filepath):
    """
    获取文件的详细信息
    
    Args:
        filepath: 文件路径
    
    Returns:
        包含文件信息的字典
    """
    stat = os.stat(filepath)
    modify_time = datetime.datetime.fromtimestamp(stat.st_mtime)
    create_time = datetime.datetime.fromtimestamp(stat.st_ctime)
    
    return {
        'modify_time': modify_time,
        'create_time': create_time,
        'size': stat.st_size
    }

def batch_rename_files(file_list, timestamp_format="%Y%m%d%H%M", separator="-", 
                       use_modify_time=True, dry_run=True):
    """
    批量重命名文件
    
    Args:
        file_list: 文件名列表
        timestamp_format: 时间戳格式
        separator: 分隔符
        use_modify_time: 是否使用修改时间
        dry_run: 是否只预览不实际重命名
    
    Returns:
        重命名结果列表
    """
    results = []
    
    for filepath in file_list:
        if os.path.exists(filepath):
            # 获取文件信息用于显示
            file_info = get_file_info(filepath)
            modify_time_str = file_info['modify_time'].strftime("%Y-%m-%d %H:%M:%S")
            
            # 生成新文件名
            new_filename = add_timestamp_to_filename(
                filepath, timestamp_format, separator, use_modify_time
            )
            
            # 构建完整的新文件路径
            directory = os.path.dirname(filepath)
            if directory:
                new_filepath = os.path.join(directory, new_filename)
            else:
                new_filepath = new_filename
            
            if dry_run:
                print(f"文件: {os.path.basename(filepath)}")
                print(f"  修改时间: {modify_time_str}")
                print(f"  新文件名: {new_filename}")
                print()
            else:
                # 检查目标文件是否已存在
                if os.path.exists(new_filepath):
                    print(f"警告: 目标文件已存在，跳过: {new_filepath}")
                    continue
                
                os.rename(filepath, new_filepath)
                print(f"已重命名: {os.path.basename(filepath)} -> {new_filename}")
            
            results.append((filepath, new_filepath))
        else:
            print(f"文件不存在: {filepath}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='给文件名添加文件修改时间戳')
    parser.add_argument('files', nargs='+', help='要重命名的文件')
    parser.add_argument('--format', '-f', default='%Y%m%d%H%M', 
                       help='时间戳格式，默认：%%Y%%m%%d%%H%%M (例如：202602270945)')
    parser.add_argument('--separator', '-s', default='-', 
                       help='分隔符，默认为"-"')
    parser.add_argument('--current-time', '-c', action='store_true', 
                       help='使用当前时间而不是文件修改时间')
    parser.add_argument('--execute', '-e', action='store_true', 
                       help='实际执行重命名（默认只预览）')
    
    args = parser.parse_args()
    
    # 确定使用什么时间
    use_modify_time = not args.current_time
    time_source = "文件修改时间" if use_modify_time else "当前系统时间"
    
    print(f"时间戳格式: {args.format}")
    print(f"分隔符: '{args.separator}'")
    print(f"时间来源: {time_source}")
    print(f"模式: {'实际执行' if args.execute else '预览模式'}\n")
    
    batch_rename_files(
        args.files, 
        args.format, 
        args.separator, 
        use_modify_time,
        not args.execute
    )

if __name__ == "__main__":
    main()