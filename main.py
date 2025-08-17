import os
import streamlit as st
import time
import requests
import asyncio
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS


try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

st.title("News search tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9)
main_placefolder = st.empty()


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

if process_url_clicked:
    main_placefolder.text("Data Loading...Started...✅✅✅")
    documents = []

    for url in urls:
        if not url.strip():
            continue
        try:
            resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
            text = "\n".join(paragraphs)

            documents.append(Document(
                page_content=text,
                metadata={"source": url}
            ))
            print(f"✅ Loaded {len(text)} characters from {url}")

        except Exception as e:
            print(f"❌ Error fetching {url}: {e}")


    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placefolder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(documents)

    
    vectorindex = FAISS.from_documents(docs, embeddings)
    main_placefolder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    vectorindex.save_local("faiss_index_gemini")


query = st.text_input("Question:")
if query:
    if os.path.exists("faiss_index_gemini"):
        vectorstore = FAISS.load_local(
            folder_path="faiss_index_gemini",
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever()
        )
        result = chain.invoke({"question": query})
        
        st.header("Answer")
        st.write(result["answer"])
        st.write(f"**Sources:** {result.get('sources', 'No sources found')}")
