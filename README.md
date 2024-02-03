# Retrieval-Augmented Generation (RAG) Project

## Introduction

Retrieval-Augmented Generation (RAG) is an innovative approach that enhances the capabilities of Large Language Models (LLMs) by integrating external knowledge bases during the generation process. This method allows models to produce more accurate, relevant, and contextually appropriate responses by referencing authoritative sources outside their original training data.

## Benefits of RAG
- Enhanced Accuracy: By consulting external knowledge bases, RAG ensures the information provided is up-to-date and accurate.
- Domain Specificity: Tailors LLM output to specific domains or organizational knowledge, making it highly relevant.
- Cost Efficiency: Eliminates the need for costly retraining of models for new data or domains.
- Scalability: Easily integrates with existing LLMs, allowing for scalable solutions across various applications.

## How RAG Works
RAG operates by first querying an external database or knowledge base to retrieve relevant information based on the input query. This information is then combined with the LLM's internal knowledge to generate a response that is both informed by the model's training and the latest data from the external source.

## Getting Started

### Installation

1. Clone the Repository
```
git clone https://github.com/varun-coditas/rag-example.git
```

2. Install the Requirements
```
pip install -r requirements.txt
```

3. Configure your OPENAI API Key in `app.py`

4. Run app.py to get the answer
```
python app.py
```


## Have Questions? 
You can reach out to me on [LinkedIn](https://www.linkedin.com/in/varun1505/) 