# # Capstone Project

## Project Overview

This repository contains three modules developed as part of the capstone project:

1. Data Pipeline
2. Analytics
3. Support Assistant

Each module is organized in its own folder with the required code, documentation, and supporting files.

---

## Repository Structure

```
capstone-project/
│
├── README.md
├── data_pipeline/
├── analytics/
└── support_assistant/
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
cd capstone-project
```

### 2. Install dependencies

Install the required Python packages.

If using one requirements file:

```bash
pip install -r requirements.txt
```

If using module-wise requirements:

```bash
pip install -r data_pipeline/requirements.txt
pip install -r analytics/requirements.txt
pip install -r support_assistant/requirements.txt
```

---

## How to Run Each Module

### Data Pipeline

1. Open the `data_pipeline` folder.
2. Run the notebook or Python script.
3. The pipeline loads data, processes it, and saves the cleaned output.

---

### Analytics

1. Open the `analytics` folder.
2. Run the notebook or Python script.
3. The module trains the machine learning model, evaluates performance, and saves the trained model.

---

### Support Assistant

1. Open the `support_assistant` folder.
2. Install the required packages.
3. Run the application.
4. The assistant loads the knowledge base and answers user questions using Retrieval-Augmented Generation (RAG).

---

## Design Decisions

### Data Pipeline

- Data cleaning and preprocessing were performed before analysis.
- SQL and Pandas were used for data transformation.

### Analytics

- Machine learning models were trained and evaluated.
- The best-performing model was selected and saved.

### Support Assistant

- ChromaDB was used as the vector database.
- Sentence Transformers were used for embeddings.
- Retrieval-Augmented Generation (RAG) was implemented to answer user queries.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SQLite
- ChromaDB
- Sentence Transformers
- Jupyter Notebook

---

## Author

Ramya Korrapati
Final repository update
