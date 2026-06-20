import time
from retrieval.retriever import (
    Retriever
)

from retrieval.reranker import (
    Reranker
)
print("start")

def main():

    start = time.time()
    retriever = Retriever()

    query = input(
        "\nQuestion: "
    )

    print(
        "\nRetrieving..."
    )

    # reranker = Reranker()

    results = retriever.retrieve(
        query,
        top_k=20
    )

    print(
        f"\nRetrieved "
        f"{len(results)} chunks"
    )

    final_chunks = results[:5]
    end = time.time()

    print(
        f"\nLatency: "
        f"{end-start:.2f}s"
)

    print(
        "\nTop Results:\n"
    )

    for i, chunk in enumerate(
        final_chunks,
        start=1
    ):

        print("=" * 80)

        print(
            f"Rank: {i}"
        )

        print(
            f"PDF: "
            f"{chunk['pdf_name']}"
        )

        print(
            f"Page: "
            f"{chunk['page_number']}"
        )

        if "rerank_score" in chunk:
            print(
                f"Rerank Score: "
                f"{chunk['rerank_score']:.4f}"
            )

        elif "score" in chunk:
            print(
                f"Vector Score: "
                f"{chunk['score']:.4f}"
            )

        print()

        print(
            chunk["text"][:1000]
        )

        print("\n")


if __name__ == "__main__":

    main()