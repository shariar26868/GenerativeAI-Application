# PDF Question & Answer Generation App

This application extracts content from PDF files, generates 10 questions and answers using a large language model (LLM), stores them in a vector database for efficient querying, and serves them via a FastAPI-based web application.

## Features

- **PDF Text Extraction**: Extracts the text from uploaded PDF files.
- **Question & Answer Generation**: Uses an LLM (e.g., OpenAI GPT) to generate questions and answers based on the extracted text.
- **Vector Database**: Stores document embeddings for quick retrieval using a vector database (FAISS).
- **FastAPI Backend**: A simple RESTful API to upload PDFs and retrieve generated questions and answers.

## Technologies Used

- **Python 3.12.6**
- **FastAPI**: Web framework for creating the REST API.
- **PyPDF**: PDF extraction libraries.
- **OpenAI**: For generating questions and answers with an LLM.
- **FAISS**: For storing and retrieving document embeddings.

## Prerequisites

- Python 3.12.6
- pip (Python package installer)
Need OpenAI API Key.


