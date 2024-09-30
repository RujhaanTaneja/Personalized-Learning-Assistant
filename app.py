import logging
import os

import pandas as pd

import pathway as pw
from pathway.stdlib.indexing import default_vector_document_index
from pathway.xpacks.llm.embedders import GeminiEmbedder
from pathway.xpacks.llm.llms import LiteLLMChat
from pathway.xpacks.llm.question_answering import (
    answer_with_geometric_rag_strategy_from_index,
)

logging.basicConfig(level=logging.CRITICAL)


from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

embedder_locator: str = "models/text-embedding-004"
embedding_dimension: int = 768
chat_locator: str = "gemini/gemini-pro"
max_tokens: int = 120
temperature: float = 0.0

embedder = GeminiEmbedder(
    api_key=api_key,
    model=embedder_locator,
    retry_strategy=pw.udfs.FixedDelayRetryStrategy(),
    cache_strategy=pw.udfs.DefaultCache(),
)
model = LiteLLMChat(
    api_key=api_key,
    model=chat_locator,
    temperature=temperature,
    max_tokens=max_tokens,
    retry_strategy=pw.udfs.FixedDelayRetryStrategy(),
    cache_strategy=pw.udfs.DefaultCache(),
)
import sys

#logging.basicConfig(stream=sys.stderr, level=logging.INFO, force=True)
class InputSchema(pw.Schema):
    doc: str
documents = pw.io.fs.read(
    "output.jsonl",
    format="json",
    schema=InputSchema,
    json_field_paths={"doc": "/context"},
    mode="static",
)

index = default_vector_document_index(
    documents.doc, documents, embedder=embedder, dimensions=embedding_dimension
)
#t=True
while True:
    question=str(input("Enter the question: "))
    df = pd.DataFrame(
        {
            "query": [
                 question,
            ],
            "__time__": [  # Queries need to be processed after documents, this sets arbitrarily high processing time
                2723124827240,
        ],
    }
)
    query = pw.debug.table_from_pandas(df)

    result = query.select(
        question=query.query,
        result=answer_with_geometric_rag_strategy_from_index(
            query.query,
            index,
            documents.doc,
            model,
            n_starting_documents=2,
            factor=2,
            max_iterations=5,
        ),
    )
#    print(result)
    pw.run()
    pw.debug.compute_and_print(result,include_id=False)