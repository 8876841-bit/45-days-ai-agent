import numpy as np


np.set_printoptions(precision=3, suppress=True)


def softmax(x: np.ndarray) -> np.ndarray:
    x = x - np.max(x, axis=-1, keepdims=True)
    exp = np.exp(x)
    return exp / np.sum(exp, axis=-1, keepdims=True)


def self_attention(x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    d_k = x.shape[-1]

    # For this first demo, use x directly as Q, K, and V.
    # Later models learn separate Wq, Wk, and Wv projection matrices.
    q = x
    k = x
    v = x

    scores = q @ k.T / np.sqrt(d_k)
    weights = softmax(scores)
    output = weights @ v

    return scores, weights, output


def print_matrix(title: str, matrix: np.ndarray, labels: list[str]) -> None:
    print(f"\n{title}")
    print(" " * 12 + " ".join(f"{label:>10}" for label in labels))
    for label, row in zip(labels, matrix):
        values = " ".join(f"{value:>10.3f}" for value in row)
        print(f"{label:>10}  {values}")


def run_case(title: str, tokens: list[str], vectors: np.ndarray) -> None:
    print(f"\n{'=' * 80}")
    print(title)
    print("=" * 80)

    print("\nInput token vectors:")
    for token, vector in zip(tokens, vectors):
        print(f"{token:>10}: {vector}")

    scores, weights, output = self_attention(vectors)

    print_matrix("Attention scores = QK^T / sqrt(d_k)", scores, tokens)
    print_matrix("Attention weights = softmax(scores)", weights, tokens)

    print("\nOutput vectors = attention_weights @ V")
    for token, vector in zip(tokens, output):
        print(f"{token:>10}: {vector}")


def main() -> None:
    tokens = ["我", "喜欢", "AI"]

    base_vectors = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.8, 0.2, 0.0],
            [0.0, 0.1, 1.0],
        ]
    )

    run_case("Case 1: '我' and '喜欢' are similar, 'AI' is different", tokens, base_vectors)

    changed_vectors = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.1, 0.0, 0.9],
            [0.0, 0.1, 1.0],
        ]
    )

    run_case("Case 2: make '喜欢' more similar to 'AI'", tokens, changed_vectors)

    print("\nKey idea:")
    print("A token does not understand itself alone.")
    print("It builds a new representation by looking at other tokens with different weights.")


if __name__ == "__main__":
    main()
