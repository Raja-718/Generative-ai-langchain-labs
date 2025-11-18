from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='sample_data_100.csv')

data = loader.load()

print(data[0])