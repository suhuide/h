import sys
from markitdown import MarkItDown

def main():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("用法: python script.py <输入文件> [输出文件]")
        print("示例: python script.py sample.pdf          # 输出到 output.md")
        print("示例: python script.py sample.docx out.md  # 输出到 out.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else "output.md"

    # 转换文档
    md = MarkItDown()
    result = md.convert(input_file)

    # 保存到文件（UTF-8编码）
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result.text_content)

    print(f"转换完成！Markdown 内容已保存到: {output_file}")

if __name__ == "__main__":
    main()