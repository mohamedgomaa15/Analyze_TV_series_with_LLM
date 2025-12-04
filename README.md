# Anime Character Analytics: Multi-Model NLP Pipeline


A comprehensive NLP and machine learning project that analyzes the Naruto anime series through multiple analytical lenses. The project combines web scraping, data preprocessing, natural language processing, network analysis, and generative AI to provide deep insights into the series.

## 🎯 Project Overview

This project implements an end-to-end pipeline from data collection to interactive visualization, featuring four distinct machine learning modules integrated into a unified Gradio web application.

## 🏗️ Architecture

### 1. Data Collection Pipeline
- **Web Scraper**: Custom Scrapy spider that crawls the Naruto Fandom Wiki
  - Extracts jutsu names, types, and descriptions
  
- **Subtitle Parser**: Processes `.ass` subtitle files
  - Extracts episode scripts and dialogue
  - Cleans and structures text data for downstream tasks
  - Handles batch processing of multiple episodes
 
### 2. Machine Learning Modules

#### Theme Classifier (Zero-Shot Classification)
- Implements BART-large-mnli for theme detection without training data
- Processes scripts in sentence-level batches for memory efficiency
- Supports multi-label classification across custom theme taxonomies
- Aggregates scores across episodes for series-wide theme analysis

#### Character Network Analysis
- **Named Entity Recognition**: Uses spaCy's transformer model (`en_core_web_trf`)
  - Extracts the character's name mentions from dialogue 
  
- **Network Generation**: Creates character relationship graphs
  - Sliding window co-occurrence analysis (configurable window size)
  - Interactive visualization using NetworkX and PyVis

**Output**: Interactive HTML network graph  

#### Text Classifier
- Fine-tuned DistilBERT for 3-class classification (Ninjutsu, Genjutsu, Taijutsu)
- Custom training pipeline with class imbalance handling
- Implements weighted cross-entropy loss via custom Trainer

**Pipeline:**
1. Text cleaning and preprocessing
2. Label encoding and stratified train/test split
3. Tokenization 
4. Fine-tuning with custom loss weighting
5. Automatic model versioning to HuggingFace Hub

#### Character Chatbot
- QLoRA-adapted Llama 3.1-8B on Colab for character roleplay
- Fine-tuned on Naruto's dialogue patterns from episode scripts

**Implementation:**
- 4-bit quantization for efficient inference
- Parameter-efficient fine-tuning with LoRA (r=64, alpha=16)
- Custom data preparation: filters meaningful dialogue 
- Contextual prompt engineering with conversation history
- Temperature and top-p sampling for response diversity

### 3. Gradio Web Application

Unified interface integrating all four modules:

**Features:**
- **Theme Analysis Tab**: Upload scripts, define themes, visualize distribution
- **Character Network Tab**: Generate interactive relationship graphs
- **Classifier Tab**: Real-time classification of user-input text
- **Chatbot Tab**: Conversational interface with character AI

## 🛠️ Technologies

**Core LLM/NLP:**
- PyTorch, Transformers (HuggingFace)
- PEFT (LoRA), TRL (SFTTrainer)
- spaCy, NLTK

**Data & Web:**
- Scrapy, pandas
- NetworkX, PyVis

**Deployment:**
- Gradio, HuggingFace Hub
- BitsAndBytes (quantization)

**Development:**
- scikit-learn, python-dotenv
- Custom training utilities

## 🚀 Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Set HuggingFace token
export HUGGINGFACE_TOKEN="your_token_here"

# Run Gradio app
python gradio_app.py
```

## 🎓 Learning Outcomes

- End-to-end ML pipeline development
- Multi-model integration and orchestration
- Parameter-efficient fine-tuning (LoRA/QLoRA)
- Custom loss functions for imbalanced data
- Interactive visualization techniques
- Production ML deployment with Gradio
