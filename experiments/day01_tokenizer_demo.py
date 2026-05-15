from rich.console import Console
from rich.table import Table
import tiktoken


SAMPLES = {
    "中文目标": "我要在45天内掌握AI Agent",
    "英文目标": "I want to master AI agents in 45 days.",
    "中英混合": "我想用 Python 写一个 AI Agent。",
    "代码": "def greet(name):\n    return f\"Hello, {name}!\"",
    "Markdown": "## Day 1\n- Tokenizer\n- Embedding\n- Attention",
    "符号": "今天状态很好 rocket fire",
}


def preview_tokens(enc: tiktoken.Encoding, text: str, limit: int = 12) -> str:
    token_ids = enc.encode(text)
    pieces = []

    for token_id in token_ids[:limit]:
        raw = enc.decode_single_token_bytes(token_id)
        try:
            piece = raw.decode("utf-8")
        except UnicodeDecodeError:
            piece = repr(raw)
        pieces.append(f"{token_id}:{piece!r}")

    if len(token_ids) > limit:
        pieces.append("...")

    return " | ".join(pieces)


def main() -> None:
    console = Console()
    enc = tiktoken.encoding_for_model("gpt-4o-mini")

    table = Table(title="Day 1 Tokenizer Demo")
    table.add_column("样本", style="cyan", no_wrap=True)
    table.add_column("文本")
    table.add_column("字符数", justify="right")
    table.add_column("Token数", justify="right", style="green")
    table.add_column("Token预览")

    for name, text in SAMPLES.items():
        token_ids = enc.encode(text)
        table.add_row(
            name,
            text.replace("\n", "\\n"),
            str(len(text)),
            str(len(token_ids)),
            preview_tokens(enc, text),
        )

    console.print(table)
    console.print()
    console.print("[bold]观察问题：[/bold]")
    console.print("1. 为什么中文字符数和 token 数不是一一对应？")
    console.print("2. 为什么代码里的空格、换行和符号也会占 token？")
    console.print("3. 为什么 prompt 越长，成本和延迟通常越高？")


if __name__ == "__main__":
    main()
