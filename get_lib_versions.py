import importlib.metadata

packages = [
    "langgraph",
    "langchain_community",
    "langchain_core",
    "langchain_groq",
    "langchain_cohere",
    "tavily_python",
    "wikipedia",
    "ipykernel"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}: {version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg}: Not installed")
