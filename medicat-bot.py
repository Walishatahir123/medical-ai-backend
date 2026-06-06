# import os
# import streamlit as st

# from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain.chains import RetrievalQA

# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import PromptTemplate
# # from langchain_huggingface import HuggingFaceEndpoint
# from langchain_groq import ChatGroq
# # LangChain core
# from langchain import hub
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain

# from dotenv import load_dotenv
# load_dotenv()

# DB_FAISS_PATH="vectorstore/db_faiss"

# @st.cache_resource
# def get_vectorstore():
#     embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
#     db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
#     return db

# def set_custom_prompt(custom_prompt_template):
#     prompt=PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
#     return prompt

# GROK_MODEL_NAME="llama-3.1-8b-instant"
# GROK_API_KEY=os.getenv("GROK_API_KEY") 

# llm = ChatGroq(
#     model=GROK_MODEL_NAME,
#     temperature=0.5,
#     max_tokens=512,
#     api_key=GROK_API_KEY,
# )

# """def load_llm(huggingface_repo_id, HF_TOKEN):
#     llm=HuggingFaceEndpoint(
#         repo_id=huggingface_repo_id,
#         temperature=0.5,
#         model_kwargs={"token":HF_TOKEN,
#                       "max_length":"512"}
#     )
#     return llm"""

# def main():
#     st.title("Ask Chatbot!")

#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         st.chat_message(message['role']).markdown(message['content'])

#     prompt=st.chat_input("Pass your prompt here")

#     if prompt:
#         st.chat_message('user').markdown(prompt)
#         st.session_state.messages.append({'role':'user', 'content': prompt})

#         CUSTOM_PROMPT_TEMPLATE = """
#                 Use the pieces of information provided in the context to answer user's question.
#                 If you dont know the answer, just say that you dont know, dont try to make up an answer. 
#                 Dont provide anything out of the given context

#                 Context: {context}
#                 Question: {question}

#                 Start the answer directly. No small talk please.
#                 """
        
#         #HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3" # PAID
#         #HF_TOKEN=os.environ.get("HF_TOKEN")  

#         #TODO: Create a Groq API key and add it to .env file
        
#         try: 
#             vectorstore=get_vectorstore()
#             #vectorstore=get_vectorstore_hf_api(hf_token=os.environ.get("HF_TOKEN"))
#             if vectorstore is None:
#                 st.error("Failed to load the vector store")

#             # qa_chain = RetrievalQA.from_chain_type(
#             #     llm=ChatGroq(
#             #         model_name="meta-llama/llama-4-maverick-17b-128e-instruct",  # free, fast Groq-hosted model
#             #         temperature=0.0,
#             #         groq_api_key=os.environ["GROQ_API_KEY"],
#             #     ),
#             #     chain_type="stuff",
#             #     retriever=vectorstore.as_retriever(search_kwargs={'k':3}),
#             #     return_source_documents=True,
#             #     chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
#             # )
#          # Step 3: Build RAG chain
# retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

import os
import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

load_dotenv()

DB_FAISS_PATH = "vectorstore/db_faiss"

# =========================================================
# 🔴 EMERGENCY DETECTION (HEART ATTACK, STROKE, SUICIDE)
# =========================================================

EMERGENCY_KEYWORDS = {
    "heart_attack": [
        "chest pain", "left arm pain", "jaw pain",
        "tight chest", "shortness of breath"
    ],
    "stroke": [
        "face drooping", "slurred speech",
        "weakness on one side", "can't speak",
        "blurred vision"
    ],
    "suicide": [
        "i want to die", "kill myself",
        "end my life", "suicide",
        "self harm", "no reason to live"
    ]
}

def detect_emergency(text: str):
    text = text.lower()
    for category, keywords in EMERGENCY_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return category
    return None


PAKISTAN_EMERGENCY_MESSAGE = """
🚨 **MEDICAL EMERGENCY DETECTED**

Your message suggests a **serious or life-threatening condition**.

📞 **Please seek immediate help in Pakistan:**
- 🚑 **Rescue / Ambulance / Fire:** **1122**
- 🚑 **Edhi Ambulance:** **115**
- 🏥 **Health Helpline:** **1166**

⚠️ **Do NOT rely on this chatbot in emergencies.**
Go to the nearest hospital or call emergency services immediately.
"""

# =========================================================
# VECTOR STORE LOADING
# =========================================================

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    try:
        db = FAISS.load_local(
            DB_FAISS_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )
        return db
    except Exception as e:
        st.error("FAISS index corrupted or embedding mismatch. Rebuild the index.")
        st.error(str(e))
        return None


# =========================================================
# LLM CONFIGURATION (GROQ)
# =========================================================

GROQ_MODEL_NAME = "llama-3.1-8b-instant"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model=GROQ_MODEL_NAME,
    temperature=0.5,
    max_tokens=512,
    api_key=GROQ_API_KEY,
)

# =========================================================
# PROMPT TEMPLATE (no hub dependency)
# =========================================================

retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Use the following context to answer the user's medical question.\n"
        "If you don't know the answer, say you don't know. "
        "Do NOT make up information.\n\n"
        "Context:\n{context}"
    ),
    ("human", "{input}"),
])

# =========================================================
# STREAMLIT PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Medical A.I Chatbot",
    page_icon="🩺",
    layout="centered"
)


def main():
    st.title("Medical A.I Chatbot 🩺")

    st.info(
        "⚕️ **Medical Disclaimer:** This chatbot provides general medical information only. "
        "It is NOT a substitute for professional medical advice, diagnosis, or treatment."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message["role"]).markdown(message["content"])

    prompt = st.chat_input("Enter your medical question here...")

    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # =================================================
        # 🔴 EMERGENCY CHECK (BEFORE RAG & LLM)
        # =================================================
        emergency_type = detect_emergency(prompt)

        if emergency_type:
            st.chat_message("assistant").markdown(PAKISTAN_EMERGENCY_MESSAGE)
            st.session_state.messages.append(
                {"role": "assistant", "content": PAKISTAN_EMERGENCY_MESSAGE}
            )
            return

        try:
            vectorstore = get_vectorstore()
            if vectorstore is None:
                st.error("Failed to load the vector store")
                return

            combine_docs_chain = create_stuff_documents_chain(
                llm,
                retrieval_qa_chat_prompt
            )

            rag_chain = create_retrieval_chain(
                vectorstore.as_retriever(search_kwargs={'k': 3}),
                combine_docs_chain
            )

            response = rag_chain.invoke({'input': prompt})
            result = response["answer"]

            result += (
                "\n\n⚠️ *This information is for educational purposes only "
                "and does not replace professional medical advice.*"
            )

            st.chat_message("assistant").markdown(result)
            st.session_state.messages.append(
                {"role": "assistant", "content": result}
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()