from pathlib import Path
from markitdown import MarkItDown


def convert_pdfs_to_markdown(src: str, dest: str):
    """
    PDFファイルを指定したディレクトリ内でMarkdown形式に変換し、出力先ディレクトリに保存する。

    Args:
        src (str): 入力PDFファイルが格納されているディレクトリ。
        dest (str): 変換したMarkdownファイルの出力先ディレクトリ。
    """
    # 入力ディレクトリと出力ディレクトリのパスを設定
    src_dir = Path(src)
    dest_dir = Path(dest)

    # 出力先ディレクトリが存在しない場合は作成
    dest_dir.mkdir(parents=True, exist_ok=True)

    # PDFファイルを探索してMarkdownに変換
    for pdf_file in src_dir.glob("*.pdf"):
        mid = MarkItDown()
        result = mid.convert(str(pdf_file))

        # 出力先ファイル名を設定
        md_file = dest_dir / (pdf_file.stem + ".md")

        # Markdownファイルとして保存
        with open(md_file, "w", encoding="utf8") as f:
            f.write(result.text_content)
        print(f"{pdf_file.name} -> {md_file.name} に変換完了")


# 使用例
if __name__ == "__main__":
    src_dir = "./src"  # 入力元ディレクトリ
    dest_dir = "./dest"  # 出力先ディレクトリ
    convert_pdfs_to_markdown(src=src_dir, dest=dest_dir)
