# # from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# # from langchain_huggingface import HuggingFaceEmbeddings
# # from langchain_community.vectorstores import FAISS

# # # # Uncomment the following files if you're not using pipenv as your virtual environment manager
# # from dotenv import load_dotenv
# # load_dotenv()

# # # Step 1: Load raw PDF(s)
# # DATA_PATH = "data/"

# # def load_pdf_files(data):
# #     loader = DirectoryLoader(data,
# #                              glob='*.pdf',
# #                              loader_cls=PyPDFLoader)
    
# #     documents = loader.load()
# #     return documents

# # documents = load_pdf_files(data=DATA_PATH)
# # # print("Length of PDF pages: ", len(documents))

# # # Step 2: Create Chunks
# # # def create_chunks(extracted_data):
# # #     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
# # #                                                  chunk_overlap=50)
# # #    text_chunks = text_splitter.split_documents(extracted_data)
# # #     return text_chunks

# # # text_chunks = create_chunks(extracted_data=documents)
# # # Step 2: Create Chunks
# # def create_chunks(extracted_data):
# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )
    
# #     text_chunks = text_splitter.split_documents(extracted_data)
# #     return text_chunks

# # text_chunks = create_chunks(extracted_data=documents)

# # # print("Length of Text Chunks: ", len(text_chunks))

# # # Step 3: Create Vector Embeddings 

# # def get_embedding_model():
# #     embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # used for semantic seacrh
# #     return embedding_model

# # embedding_model = get_embedding_model()

# # # Step 4: Store embeddings in FAISS ->facebook ai similarity search
# # DB_FAISS_PATH = "vectorstore/db_faiss"
# # db = FAISS.from_documents(text_chunks, embedding_model)
# # db.save_local(DB_FAISS_PATH)
# # import os
# # os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
# # os.environ["TRANSFORMERS_OFFLINE"] = "1"      # ← don't contact HuggingFace
# # os.environ["HF_DATASETS_OFFLINE"] = "1"       # ← use local cache only
# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS

# # # Uncomment the following files if you're not using pipenv as your virtual environment manager
# # from dotenv import load_dotenv, find_dotenv
# # load_dotenv(find_dotenv())

# # Step 1: Load raw PDF(s)
# DATA_PATH = "data/"


# def load_pdf_files(data):
#     loader = DirectoryLoader(data,
#                              glob='*.pdf',
#                              loader_cls=PyPDFLoader)
    
#     documents = loader.load()
#     return documents


# documents = load_pdf_files(data=DATA_PATH)
# # print("Length of PDF pages: ", len(documents))


# # Step 2: Create Chunks
# def create_chunks(extracted_data):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
#                                                  chunk_overlap=50)
#     text_chunks = text_splitter.split_documents(extracted_data)
#     return text_chunks


# text_chunks = create_chunks(extracted_data=documents)
# # print("Length of Text Chunks: ", len(text_chunks))

# # Step 3: Create Vector Embeddings 


# def get_embedding_model():
#     embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     return embedding_model


# embedding_model = get_embedding_model()

# # Step 4: Store embeddings in FAISS
# DB_FAISS_PATH = "vectorstore/db_faiss"
# db = FAISS.from_documents(text_chunks, embedding_model)
# db.save_local(DB_FAISS_PATH)

# from langchain_community.document_loaders import (
#     PyPDFLoader,
#     DirectoryLoader
# )

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# from langchain_huggingface import HuggingFaceEmbeddings

# from langchain_community.vectorstores import FAISS

# import os


# # ======================
# # STEP 1: LOAD PDF FILES
# # ======================

# DATA_PATH = "data/"


# def load_pdf_files(data_path):

#     print("Loading PDF files...")

#     loader = DirectoryLoader(
#         data_path,
#         glob="*.pdf",
#         loader_cls=PyPDFLoader
#     )

#     documents = loader.load()

#     print(f"Loaded {len(documents)} pages")

#     return documents
# documents=load_pdf_files(data=DATA_PATH)
# #print("Length of PDF pages: ", len(documents))


# # documents = load_pdf_files(DATA_PATH)



# # # ======================
# # # STEP 2: CREATE CHUNKS
# # # ======================

# # def create_chunks(extracted_data):

# #     print("Creating text chunks...")

# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=500,
# #         chunk_overlap=50
# #     )

# #     text_chunks = text_splitter.split_documents(extracted_data)

# #     print(f"Created {len(text_chunks)} chunks")

# #     return text_chunks


# # text_chunks = create_chunks(documents)


# # # ======================
# # # STEP 3: LOAD EMBEDDING MODEL
# # # ======================

# # def get_embedding_model():

# #     print("Loading embedding model...")

# #     embedding_model = HuggingFaceEmbeddings(
# #         model_name="sentence-transformers/all-MiniLM-L6-v2"
# #     )

# #     print("Embedding model loaded")

# #     return embedding_model


# # # Step 4: Store embeddings in FAISS
# # DB_FAISS_PATH="vectorstore/db_faiss"
# # db=FAISS.from_documents(text_chunks, embedding_model)
# # db.save_local(DB_FAISS_PATH)

# # embedding_model = get_embedding_model()


# # # ======================
# # # STEP 4: CREATE FAISS DB
# # # ======================

# # print("Creating FAISS vector database...")

# # DB_FAISS_PATH = "vectorstore/db_faiss"

# # os.makedirs(DB_FAISS_PATH, exist_ok=True)

# # db = FAISS.from_documents(
# #     text_chunks,
# #     embedding_model
# # )

# # print("Saving FAISS database...")

# # db.save_local(DB_FAISS_PATH)

# # print("DONE")


# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# import os

# # ======================
# # STEP 1: LOAD PDF FILES
# # ======================
# DATA_PATH = "data/"

# def load_pdf_files(data_path):
#     print("Loading PDF files...")

#     loader = DirectoryLoader(
#         data_path,
#         glob="*.pdf",
#         loader_cls=PyPDFLoader
#     )

#     documents = loader.load()
#     print(f"Loaded {len(documents)} pages")

#     return documents


# documents = load_pdf_files(DATA_PATH)


# # ======================
# # STEP 2: CREATE CHUNKS
# # ======================
# def create_chunks(extracted_data):
#     print("Creating text chunks...")

#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     text_chunks = text_splitter.split_documents(extracted_data)

#     print(f"Created {len(text_chunks)} chunks")

#     return text_chunks


# text_chunks = create_chunks(documents)


# # ======================
# # STEP 3: LOAD EMBEDDING MODEL
# # ======================
# def get_embedding_model():
#     print("Loading embedding model...")

#     embedding_model = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     print("Embedding model loaded")
#     return embedding_model


# embedding_model = get_embedding_model()


# # ======================
# # STEP 4: CREATE + SAVE FAISS DB
# # ======================
# DB_FAISS_PATH = "vectorstore/db_faiss"
# os.makedirs(DB_FAISS_PATH, exist_ok=True)

# print("Creating FAISS vector database...")

# db = FAISS.from_documents(text_chunks, embedding_model)

# print("Saving FAISS database...")

# db.save_local(DB_FAISS_PATH)

# print("DONE")

import os
import time
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


DATA_PATH     = "data/"
SPECIALIST_PDF = "Specialistdr.pdf"   # <-- exact filename in your project root
DB_FAISS_PATH = "vectorstore/db_faiss"


# =============================================================
# STEP 1: Load Gale Encyclopedia PDFs  (from data/ folder)
# =============================================================

print("=" * 55)
print("STEP 1: Loading Gale Encyclopedia PDFs from data/...")
print("=" * 55)

medical_loader = DirectoryLoader(
    DATA_PATH,
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
medical_docs = medical_loader.load()

# Tag every page so we know it came from the encyclopedia
for doc in medical_docs:
    doc.metadata["source_type"] = "medical_encyclopedia"
    doc.metadata["category"]    = "Medical Knowledge"

print(f"Loaded {len(medical_docs)} pages from encyclopedia")


# =============================================================
# STEP 2: Load Specialistdr.pdf  (doctors in Lahore)
# =============================================================

print("\n" + "=" * 55)
print("STEP 2: Loading Specialistdr.pdf (Lahore doctors)...")
print("=" * 55)

if os.path.exists(SPECIALIST_PDF):
    specialist_loader = PyPDFLoader(SPECIALIST_PDF)
    specialist_docs   = specialist_loader.load()

    # Tag every page so we know it came from the doctor directory
    for doc in specialist_docs:
        doc.metadata["source_type"] = "doctor_directory"
        doc.metadata["category"]    = "Lahore Specialist Doctors"

    print(f"Loaded {len(specialist_docs)} pages from Specialistdr.pdf")
else:
    specialist_docs = []
    print(f"WARNING: '{SPECIALIST_PDF}' not found — skipping doctor directory")
    print(f"Make sure it's in: {os.path.abspath(SPECIALIST_PDF)}")


# =============================================================
# STEP 3: Combine both sources
# =============================================================

all_docs = medical_docs + specialist_docs
print(f"\nTotal pages combined: {len(all_docs)}")
print(f"  Medical encyclopedia : {len(medical_docs)} pages")
print(f"  Doctor directory     : {len(specialist_docs)} pages")


# =============================================================
# STEP 4: Split into chunks
# (use smaller chunks for doctor directory — it has structured data)
# =============================================================

print("\n" + "=" * 55)
print("STEP 3: Splitting into chunks...")
print("=" * 55)

# Larger chunks for encyclopedia prose
medical_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

# Smaller chunks for doctor directory (each entry is short)
specialist_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

medical_chunks    = medical_splitter.split_documents(medical_docs)
specialist_chunks = specialist_splitter.split_documents(specialist_docs)

all_chunks = medical_chunks + specialist_chunks

print(f"Encyclopedia chunks : {len(medical_chunks)}")
print(f"Doctor dir chunks   : {len(specialist_chunks)}")
print(f"Total chunks        : {len(all_chunks)}")


# =============================================================
# STEP 5: Load embedding model
# =============================================================

print("\n" + "=" * 55)
print("STEP 4: Loading embedding model...")
print("=" * 55)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={
        "normalize_embeddings": True,
        "batch_size": 64
    }
)
print("Embedding model ready")


# =============================================================
# STEP 6: Build FAISS in batches
# =============================================================

print("\n" + "=" * 55)
print("STEP 5: Building FAISS vector database...")
print("=" * 55)

os.makedirs("vectorstore", exist_ok=True)

BATCH         = 300
total_batches = (len(all_chunks) - 1) // BATCH + 1
db            = None
start         = time.time()

for i in range(0, len(all_chunks), BATCH):
    batch     = all_chunks[i : i + BATCH]
    batch_num = i // BATCH + 1
    elapsed   = time.time() - start

    if batch_num > 1:
        avg_per_batch = elapsed / (batch_num - 1)
        remaining     = avg_per_batch * (total_batches - batch_num + 1)
        print(f"  Batch {batch_num}/{total_batches} "
              f"({len(batch)} chunks) — ~{int(remaining)}s remaining...")
    else:
        print(f"  Batch {batch_num}/{total_batches} "
              f"({len(batch)} chunks) — estimating time...")

    if db is None:
        db = FAISS.from_documents(batch, embedding_model)
    else:
        db.merge_from(FAISS.from_documents(batch, embedding_model))

db.save_local(DB_FAISS_PATH)
total_time = int(time.time() - start)
print(f"\nDone! FAISS saved to '{DB_FAISS_PATH}'")
print(f"Total time: {total_time // 60}m {total_time % 60}s")
print(f"Total vectors indexed: {len(all_chunks)}")