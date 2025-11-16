# Indonesian-Language Bot Detection on Social Media X Using Transformer and RNN Models

This repository contains the implementation of a research study titled:

**“Identifying Indonesian-Language Bot Accounts on Social Media X Using Transformer and Recurrent Neural Network (RNN) Models.”**

The project evaluates multiple NLP architectures — including **LSTM, GRU, IndoBERT, mBERT, and hybrid Transformer-RNN models** — for detecting Indonesian-language bot accounts based on tweet text and numerical metadata.

---
## 🚀 Features

- Bot detection using:
  - **LSTM**
  - **GRU**
  - **IndoBERT**
  - **mBERT**
  - **IndoBERT + LSTM**
  - **IndoBERT + GRU**
  - **mBERT + LSTM**
  - **mBERT + GRU**
- Manual text preprocessing for RNN models
- Transformer tokenizer preprocessing for IndoBERT & mBERT
- Numerical features:
  - `favorite_count`, `retweet_count`, `reply_count`, `quote_count`, `tweet_per_day`
- Training & evaluation with:
  - Accuracy, Precision, Recall, F1-score
  - ROC AUC
  - Confusion matrix
  - 10-Fold Cross Validation
- Statistical analysis:
  - **Friedman Test**
  - **Nemenyi Post-Hoc Test**
- Deployment using **Gradio + HuggingFace Spaces**
