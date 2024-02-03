import os
import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA


os.environ["OPENAI_API_KEY"] = 'sk-KEY'

# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = ''

# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

# print(docs)
# exit()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# print(splits[0])
# exit()

# Index the chunks using OpenAI's embeddings.
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()

# docs = retriever.get_relevant_documents("Task Decomposition", top_k=3)
# print(docs[0])
# exit()


###
# Set up the prompt for the question-answering model.
# 
# You are an assistant for question-answering tasks. Use the following pieces of 
# retrieved context to answer the question. If you don't know the answer, 
# just say that you don't know. Use three sentences maximum and keep the answer concise.
# Question: {question} 
# Context: {context} 
# Answer:
###
prompt = hub.pull("rlm/rag-prompt")


# OpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


# RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)
question = "What are the approaches to Task Decomposition?"
result = qa_chain({"query": question})

print(result["result"])


# cleanup
vectorstore.delete_collection()