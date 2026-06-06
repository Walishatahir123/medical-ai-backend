# # # step 1:create memoery for llm (by using ml model=mini)
# # # step 2:Connect llm with faiss and create chain

# # import os
# # from dotenv import load_dotenv

# # # LangChain core
# # from langchain import hub
# # from langchain.chains import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain

# # # Groq LLM
# # from langchain_groq import ChatGroq

# # # HuggingFace embeddings (new package, not langchain_community)
# # from langchain_huggingface import HuggingFaceEmbeddings

# # # Vector database
# # from langchain_community.vectorstores import FAISS

# # # Load environment variables
# # load_dotenv()

# # # Step 1: Setup LLM (Groq)
# # GROK_API_KEY = os.getenv("GROK_API_KEY")  # <-- fixed typo (was GROK_APKI_KEY)
# # GROK_MODEL_NAME = "llama-3.1-8b-instant"

# # llm = ChatGroq(
# #     model=GROK_MODEL_NAME,
# #     temperature=0.5,
# #     max_tokens=512,
# #     api_key=GROK_API_KEY,
# # )

# # # Step 2: Connect LLM with FAISS and Embeddings
# # DB_FAISS_PATH = "vectorstore/db_faiss"
# # embedding_model = HuggingFaceEmbeddings(
# #     model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )

# # db = FAISS.load_local(
# #     DB_FAISS_PATH,
# #     embedding_model,
# #     allow_dangerous_deserialization=True
# # )

# # # Step 3: Build RAG chain
# # retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

# # combine_docs_chain = create_stuff_documents_chain(
# #     llm, retrieval_qa_chat_prompt
# # )

# # rag_chain = create_retrieval_chain(
# #     db.as_retriever(search_kwargs={'k': 3}),  # answer how many doc
# #     combine_docs_chain
# # )

# # # Step 4: Run Query
# # user_query = input("Write Query Here: ")
# # response = rag_chain.invoke({'input': user_query})

# # print("RESULT: ", response["answer"])
# # print("SOURCE DOCUMENTS:")
# # for doc in response["context"]:
# #     print(f"- {doc.metadata} -> {doc.page_content[:200]}...")
# # import os
# # <<<<<<< Updated upstream

# # from langchain_groq import ChatGroq
# # from langchain_community.vectorstores import FAISS
# # from langchain_huggingface import HuggingFaceEmbeddings

# # from langchain import hub
# # from langchain.chains import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain

# # =======
# # >>>>>>> Stashed changes
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # <<<<<<< Updated upstream
# # # Step 1: Setup Groq LLM
# # GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# # GROQ_MODEL_NAME = "llama-3.1-8b-instant"  # Change to any supported Groq model


# # llm = ChatGroq(
# #     model=GROQ_MODEL_NAME,
# #     temperature=0.5,
# #     max_tokens=512,
# #     api_key=GROQ_API_KEY,
# # )

# # =======
# # # =========================
# # # LangChain Imports
# # # =========================

# # from langchain.chains import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain

# # from langchain_core.prompts import ChatPromptTemplate

# # # Groq
# # from langchain_groq import ChatGroq
# # >>>>>>> Stashed changes

# # # Embeddings
# # from langchain_huggingface import HuggingFaceEmbeddings

# # <<<<<<< Updated upstream
# # # Load Database
# # DB_FAISS_PATH = "vectorstore/db_faiss"
# # embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# # db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

# # # Step 3: Build RAG chain
# # retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

# # # Document combiner chain (stuff documents into prompt)
# # combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

# # # Retrieval chain (retriever + doc combiner)
# # rag_chain = create_retrieval_chain(db.as_retriever(search_kwargs={'k': 3}), combine_docs_chain)



# # # Now invoke with a single query
# # user_query=input("Write Query Here: ")
# # response=rag_chain.invoke({'input': user_query})
# # print("RESULT: ", response["answer"])
# # print("\nSOURCE DOCUMENTS:")
# # for doc in response["context"]:
# #     print(f"- {doc.metadata} -> {doc.page_content[:200]}...")
# # =======
# # # Vector Store
# # from langchain_community.vectorstores import FAISS


# # # =========================
# # # STEP 1: Setup LLM
# # # =========================

# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # if not GROQ_API_KEY:
# #     raise ValueError("GROQ_API_KEY not found in .env file")


# # llm = ChatGroq(
# #     groq_api_key=GROQ_API_KEY,
# #     model_name="llama-3.1-8b-instant",
# #     temperature=0.5,
# #     max_tokens=512
# # )

# # print("LLM Loaded Successfully")


# # # =========================
# # # STEP 2: Load Embedding Model
# # # =========================

# # embedding_model = HuggingFaceEmbeddings(
# #     model_name="sentence-transformers/all-MiniLM-L6-v2"
# # )

# # print("Embedding Model Loaded")


# # # =========================
# # # STEP 3: Load FAISS DB
# # # =========================

# # DB_FAISS_PATH = "vectorstore/db_faiss"

# # db = FAISS.load_local(
# #     DB_FAISS_PATH,
# #     embedding_model,
# #     allow_dangerous_deserialization=True
# # )

# # print("FAISS Database Loaded")


# # # =========================
# # # STEP 4: Create Retriever
# # # =========================

# # retriever = db.as_retriever(
# #     search_type="similarity",
# #     search_kwargs={"k": 3}
# # )


# # # =========================
# # # STEP 5: Create Prompt
# # # =========================

# # prompt = ChatPromptTemplate.from_template(
# #     """
# #     Answer the user's question using only the provided context.

# #     Context:
# #     {context}

# #     Question:
# #     {input}

# #     Answer:
# #     """
# # )


# # # =========================
# # # STEP 6: Create Chain
# # # =========================

# # combine_docs_chain = create_stuff_documents_chain(
# #     llm,
# #     prompt
# # )

# # rag_chain = create_retrieval_chain(
# #     retriever,
# #     combine_docs_chain
# # )

# # print("RAG Chain Created Successfully")


# # # =========================
# # # STEP 7: Chat Loop
# # # =========================

# # while True:

# #     user_query = input("\nWrite Query Here: ")

# #     if user_query.lower() == "exit":
# #         break

# #     response = rag_chain.invoke({
# #         "input": user_query
# #     })

# #     print("\nRESULT:")
# #     print(response["answer"])

# #     print("\nSOURCE DOCUMENTS:")
    
# #     for doc in response["context"]:
# #         print(f"\nSOURCE: {doc.metadata}")
# #         print(doc.page_content[:200])
# # >>>>>>> Stashed changes

# import os
# os.environ["TRANSFORMERS_OFFLINE"] = "1"
# os.environ["HF_DATASETS_OFFLINE"] = "1"
# os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# from dotenv import load_dotenv
# load_dotenv()

# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# # =========================
# # STEP 1: Setup LLM
# # =========================

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY not found in .env file")

# llm = ChatGroq(
#     groq_api_key=GROQ_API_KEY,
#     model_name="llama-3.1-8b-instant",
#     temperature=0.5,
#     max_tokens=512
# )
# print("LLM loaded")


# # =========================
# # STEP 2: Embedding Model
# # =========================

# embedding_model = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2",
#     model_kwargs={"device": "cpu"},
#     encode_kwargs={"normalize_embeddings": True}
# )
# print("Embedding model loaded")


# # =========================
# # STEP 3: Load FAISS DB
# # =========================

# DB_FAISS_PATH = "vectorstore/db_faiss"
# db = FAISS.load_local(
#     DB_FAISS_PATH,
#     embedding_model,
#     allow_dangerous_deserialization=True
# )
# print("FAISS database loaded")


# # =========================
# # STEP 4: Retriever
# # =========================

# retriever = db.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 5}
# )


# # =========================
# # STEP 5: Prompt
# # =========================

# prompt = ChatPromptTemplate.from_template("""
# You are a helpful medical assistant with access to two knowledge sources:

# 1. MEDICAL ENCYCLOPEDIA — Gale Encyclopedia of Medicine with detailed
#    information about diseases, symptoms, treatments, and medications.

# 2. LAHORE DOCTOR DIRECTORY — A list of specialist doctors in Lahore,
#    Pakistan, including their names, specializations, clinics, and
#    contact information.

# Use the context below to answer the user's question accurately.

# Rules:
# - If the user asks about a disease, symptom, treatment, or medication
#   answer from the medical encyclopedia.
# - If the user asks about a doctor, specialist, clinic, or hospital
#   in Lahore answer from the doctor directory.
# - If the user asks about both (e.g. "I have diabetes, which doctor
#   should I see in Lahore?") answer both parts.
# - If the answer is not in the context, say:
#   "I don't have enough information in my documents to answer that."
# - Never make up doctor names, phone numbers, or addresses.

# Context:
# {context}

# Question:
# {input}

# Answer:
# """)


# # =========================
# # STEP 6: RAG Chain
# # =========================

# combine_docs_chain = create_stuff_documents_chain(llm, prompt)
# rag_chain          = create_retrieval_chain(retriever, combine_docs_chain)
# print("RAG chain ready\n")


# # =========================
# # STEP 7: Chat Loop
# # =========================

# print("=" * 55)
# print("Medical AI Assistant")
# print("Sources: Gale Encyclopedia + Lahore Specialist Doctors")
# print("Type 'exit' to quit")
# print("=" * 55)

# while True:
#     user_query = input("\nYou: ").strip()

#     if not user_query:
#         continue

#     if user_query.lower() in ["exit", "quit", "q"]:
#         print("Goodbye!")
#         break

#     try:
#         response = rag_chain.invoke({"input": user_query})

#         print("\nAssistant:")
#         print(response["answer"])

#         print("\nSources used:")
#         seen = set()
#         for doc in response["context"]:
#             source      = doc.metadata.get("source", "Unknown")
#             page        = doc.metadata.get("page", "?")
#             source_type = doc.metadata.get("source_type", "unknown")
#             key         = f"{source}-{page}"
#             if key not in seen:
#                 seen.add(key)
#                 icon = "📚" if source_type == "medical_encyclopedia" else "👨‍⚕️"
#                 print(f"  {icon} {source} (page {page})")

#     except Exception as e:
#         print(f"Error: {e}")

import os
import sys
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from dotenv import load_dotenv
load_dotenv()

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# =========================================================
# EMERGENCY DETECTION
# =========================================================

EMERGENCY_KEYWORDS = {
    "suicide": [
        "i want to die", "kill myself", "killing myself",
        "end my life", "suicide", "suicidal", "self harm",
        "self-harm", "hurt myself", "no reason to live",
        "don't want to live", "want to end it", "take my life",
        "better off dead", "can't go on", "give up on life",
        "rather be dead", "overdose on purpose",
    ],
    "heart_attack": [
        "chest pain", "chest pressure", "chest tightness",
        "left arm pain", "jaw pain", "heart attack",
        "shortness of breath", "heart is racing",
        "pain in chest", "crushing chest",
    ],
    "stroke": [
        "face drooping", "face numb", "slurred speech",
        "can't speak", "weakness on one side", "arm weakness",
        "sudden headache", "blurred vision", "stroke",
        "face falling",
    ],
    "severe_bleeding": [
        "bleeding badly", "won't stop bleeding", "blood everywhere",
        "severe bleeding", "cut myself badly", "bleeding out",
    ],
    "unconscious": [
        "not breathing", "unconscious", "passed out",
        "not waking up", "fainted", "collapsed",
        "no pulse", "not responding",
    ],
}

HELPLINE_MESSAGES = {
    "suicide": """
╔══════════════════════════════════════════════════════╗
║           YOU ARE NOT ALONE                         ║
╚══════════════════════════════════════════════════════╝

It sounds like you are going through an incredibly
difficult time. Your life has value and people care
about you deeply.

PAKISTAN MENTAL HEALTH HELPLINES:
--------------------------------------------------
  Umang Helpline        : 0317-4288665  (24/7)
  Rozan Counseling      : 051-2890505
  Umang Mental Health   : 0311-7786264
  Rescue Emergency      : 1122
  Edhi Foundation       : 115
--------------------------------------------------

Please reach out to someone you trust RIGHT NOW:
a family member, friend, or the helplines above.

This chatbot session is now closing so you can
get the real human support you deserve.
""",
    "heart_attack": """
╔══════════════════════════════════════════════════════╗
║         POSSIBLE HEART ATTACK DETECTED              ║
╚══════════════════════════════════════════════════════╝

Your symptoms may indicate a MEDICAL EMERGENCY.

CALL IMMEDIATELY:
--------------------------------------------------
  Rescue / Ambulance    : 1122
  Edhi Ambulance        : 115
  Health Helpline       : 1166
--------------------------------------------------

While waiting for help:
  - Sit or lie down and stay calm
  - Chew an aspirin if available and not allergic
  - Loosen tight clothing
  - Do NOT drive yourself to hospital

Go to the nearest Emergency Room NOW.
""",
    "stroke": """
╔══════════════════════════════════════════════════════╗
║           POSSIBLE STROKE DETECTED                  ║
╚══════════════════════════════════════════════════════╝

Your symptoms may indicate a STROKE. Time is critical.

CALL IMMEDIATELY:
--------------------------------------------------
  Rescue / Ambulance    : 1122
  Edhi Ambulance        : 115
  Health Helpline       : 1166
--------------------------------------------------

Remember FAST:
  F - Face drooping?
  A - Arm weakness?
  S - Speech difficulty?
  T - Time to call 1122 NOW

Every minute counts. Go to hospital IMMEDIATELY.
""",
    "severe_bleeding": """
╔══════════════════════════════════════════════════════╗
║         SEVERE BLEEDING EMERGENCY                   ║
╚══════════════════════════════════════════════════════╝

CALL IMMEDIATELY:
--------------------------------------------------
  Rescue / Ambulance    : 1122
  Edhi Ambulance        : 115
--------------------------------------------------

While waiting:
  - Press firmly on the wound with a clean cloth
  - Keep pressure constant, do not lift to check
  - Lay the person down and keep them warm

Go to the nearest Emergency Room NOW.
""",
    "unconscious": """
╔══════════════════════════════════════════════════════╗
║         UNCONSCIOUS PERSON DETECTED                 ║
╚══════════════════════════════════════════════════════╝

CALL IMMEDIATELY:
--------------------------------------------------
  Rescue / Ambulance    : 1122
  Edhi Ambulance        : 115
--------------------------------------------------

While waiting:
  - Check if they are breathing
  - If not breathing, start CPR if you know how
  - Place in recovery position if breathing
  - Do not leave them alone

This is a medical emergency. Call 1122 NOW.
""",
}


def detect_emergency(text: str):
    text_lower = text.lower()
    for category, keywords in EMERGENCY_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return category
    return None


def handle_emergency(category: str):
    print(HELPLINE_MESSAGES[category])
    if category == "suicide":
        print("Closing chatbot. Please call a helpline now.\n")
        sys.exit(0)
    else:
        print("-" * 55)
        print("After calling emergency services you may continue.\n")


# =========================================================
# STEP 1: Setup LLM
# =========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0.5,
    max_tokens=512
)
print("LLM loaded")


# =========================================================
# STEP 2: Embedding Model
# =========================================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)
print("Embedding model loaded")


# =========================================================
# STEP 3: Load FAISS DB
# =========================================================

DB_FAISS_PATH = "vectorstore/db_faiss"
db = FAISS.load_local(
    DB_FAISS_PATH,
    embedding_model,
    allow_dangerous_deserialization=True
)
print("FAISS database loaded")


# =========================================================
# STEP 4: Retriever
# =========================================================

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


# =========================================================
# STEP 5: Prompt
# =========================================================

prompt = ChatPromptTemplate.from_template("""
You are a helpful medical assistant with access to two knowledge sources:

1. MEDICAL ENCYCLOPEDIA - Gale Encyclopedia of Medicine with detailed
   information about diseases, symptoms, treatments, and medications.

2. LAHORE DOCTOR DIRECTORY - A list of specialist doctors in Lahore,
   Pakistan, including their names, specializations, clinics, and
   contact information.

Rules:
- If the user asks about a disease, symptom, treatment, or medication
  answer from the medical encyclopedia.
- If the user asks about a doctor, specialist, clinic, or hospital
  in Lahore answer from the doctor directory.
- If the user asks about both answer both parts.
- If the answer is not in the context, say:
  "I don't have enough information in my documents to answer that."
- Never make up doctor names, phone numbers, or addresses.

Context:
{context}

Question:
{input}

Answer:
""")


# =========================================================
# STEP 6: RAG Chain
# =========================================================

combine_docs_chain = create_stuff_documents_chain(llm, prompt)
rag_chain          = create_retrieval_chain(retriever, combine_docs_chain)
print("RAG chain ready\n")


# =========================================================
# STEP 7: Chat Loop
# =========================================================

print("=" * 55)
print("Medical AI Assistant")
print("Sources : Gale Encyclopedia + Lahore Specialist Doctors")
print("Safety  : Emergency detection ON")
print("Type 'exit' to quit")
print("=" * 55)

while True:
    user_query = input("\nYou: ").strip()

    if not user_query:
        continue

    if user_query.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    # ── Emergency check BEFORE sending to LLM ──────────
    emergency = detect_emergency(user_query)
    if emergency:
        handle_emergency(emergency)
        continue
    # ────────────────────────────────────────────────────

    try:
        response = rag_chain.invoke({"input": user_query})

        print("\nAssistant:")
        print(response["answer"])

        print("\nSources used:")
        seen = set()
        for doc in response["context"]:
            source      = doc.metadata.get("source", "Unknown")
            page        = doc.metadata.get("page", "?")
            source_type = doc.metadata.get("source_type", "unknown")
            key         = f"{source}-{page}"
            if key not in seen:
                seen.add(key)
                icon = "📚" if source_type == "medical_encyclopedia" else "👨‍⚕️"
                print(f"  {icon} {source} (page {page})")

    except Exception as e:
        print(f"Error: {e}")