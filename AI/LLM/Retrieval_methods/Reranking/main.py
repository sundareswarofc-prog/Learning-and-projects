from flashrank import Ranker, RerankRequest

ranker = Ranker()

query = "What is FastAPI?"

documents = [
    {"id": 1, "text": "React is a frontend library."},
    {"id": 2, "text": "FastAPI is a Python framework for building APIs."},
    {"id": 3, "text": "Python is a programming language."}
]

request = RerankRequest(
    query=query,
    passages=documents
)
print("request",request)

results = ranker.rerank(request)

print("results",results)


for result in results:
    print(result["score"], result["text"])