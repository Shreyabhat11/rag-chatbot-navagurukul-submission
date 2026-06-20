import time

from rag.pipeline import RAGPipeline

queries = [

    "What is consistent hashing?",

    "Explain CAP theorem",

    "How does Kafka work?",

    "Design URL Shortener",

    "Explain sharding"
]

rag = RAGPipeline()

latencies = []

for q in queries:

    start = time.time()

    rag.ask(q)

    latency = (
        time.time() - start
    )

    latencies.append(
        latency
    )

    print(
        q,
        latency
    )

print(
    "\nAverage:",
    sum(latencies) /
    len(latencies)
)