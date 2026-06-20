import time

from retrieval.retriever import Retriever

from llm.groq_client import GroqLLM

from rag.prompt_template import SYSTEM_PROMPT


class RAGPipeline:

    def __init__(self):

        print("Loading Retriever...")
        self.retriever = Retriever()

        print("Loading LLM...")
        self.llm = GroqLLM()

        print("RAG Pipeline Ready")

    def build_context(self, chunks):

        context_parts = []

        for chunk in chunks:

            context_parts.append(
                f"""
SOURCE:
{chunk['pdf_name']}

PAGE:
{chunk['page_number']}

CONTENT:
{chunk['text']}
"""
            )

        return "\n\n".join(context_parts)

    def ask(self, query):

        start_time = time.time()

        # Retrieve
        retrieved = self.retriever.retrieve(
            query,
            top_k=20
        )

        # Use top 5 chunks
        context_chunks = retrieved[:8]

        # Build context
        context = self.build_context(
            context_chunks
        )

        prompt = f"""
{SYSTEM_PROMPT}

CONTEXT:

{context}

QUESTION:

{query}

ANSWER:
"""

        answer = self.llm.generate(
            prompt
        )

        latency = (
            time.time()
            - start_time
        )

        return {

            "query":
                query,

            "answer":
                answer,

            "sources":
                context_chunks,

            "retrieved":
                retrieved,

            "latency":
                latency
        }
    
    def deduplicate_sources(self,chunks):

        seen = set()

        unique = []

        for chunk in chunks:

            key = (
                chunk["pdf_name"],
                chunk["page_number"]
            )

            if key not in seen:

                seen.add(key)

                unique.append(chunk)

        return unique