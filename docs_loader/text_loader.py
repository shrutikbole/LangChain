from langchain_community.document_loaders import TextLoader

loader = TextLoader('.\public\cricket.txt', encoding= 'utf-8')

docs = loader.load()

print(type(docs))
print(docs[0])