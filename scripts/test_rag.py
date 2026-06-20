print("rag starting....")
import time

from rag.pipeline import (
    RAGPipeline
)


def main():
    print("creating pipeline")

    rag = RAGPipeline()
    print("pipeline created")

    while True:

        query = input(
            "\nAsk Question: "
        )

        if query.lower() == "exit":
            break
        print("Calling RAG...")

        start = time.time()

        result = rag.ask(query)

        end = time.time()

        print("\n")
        print("=" * 100)
        print("ANSWER")
        print("=" * 100)

        print(
            result["answer"]
        )

        print("\n")
        print("=" * 100)
        print("SOURCES")
        print("=" * 100)

        for source in result[
            "sources"
        ]:

            print(
                f"{source['pdf_name']} "
                f"(Page {source['page_number']})"
            )

        print(
            f"\nLatency: "
            f"{end-start:.2f}s"
        )
if __name__ == "__main__":
    print("Executing main()")
    main()