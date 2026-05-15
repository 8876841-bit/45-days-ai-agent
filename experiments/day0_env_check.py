import anthropic
import dotenv
import numpy
import openai
import pandas
import rich
import tiktoken


def main() -> None:
    enc = tiktoken.encoding_for_model("gpt-4o-mini")
    sample = "我要在45天内掌握AI Agent"
    tokens = enc.encode(sample)

    print("AI dev env OK")
    print(f"openai: {openai.__version__}")
    print(f"anthropic: {anthropic.__version__}")
    print(f"numpy: {numpy.__version__}")
    print(f"pandas: {pandas.__version__}")
    print(f"tiktoken sample tokens: {len(tokens)}")


if __name__ == "__main__":
    main()
