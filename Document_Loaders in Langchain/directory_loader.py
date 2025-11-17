from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='ANN',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load() # load (minimum pdf), lazy_load(when maximum number of pdf file)

for document in docs:
    print(document.metadata)
