# Analyzing-Text-of-Rights-Abuse-Testimony

# Topic Modeling Arabic Human Rights Texts

This project implements natural language processing methods to analyze and classify human rights abuse testimonies in Arabic text. The goal is to develop an automated pipeline for processing unstructured testimony data to identify patterns of abuse and streamline documentation efforts.

## Background

In Egypt, widespread arrests and security service impunity have led to extensive human rights violations, including:
- Politically motivated arbitrary detentions
- Due process violations
- Extended pre-trial detentions
- Substandard detention conditions
- Physical and mental abuse

With an estimated 65,000 political prisoners and minimal judicial transparency, proper documentation of abuse is crucial for accountability and long-term transitional justice. This project aims to make the documentation process more efficient through NLP techniques.

## Data

The dataset consists of approximately 1,100 individual testimonies from cases of various human rights abuses. Key characteristics:
- Documents range from several sentences to multiple paragraphs
- All data has been anonymized
- Contains unlabeled text data only
- Source: Compilation of case files and testimonies from researchers and human rights lawyers

### Challenges in Arabic Text Processing

The project addresses several unique challenges in processing Arabic text:
- Orthographic Ambiguity: Character forms and word spellings vary by context
- Morphological Richness: Multiple forms for the same verb
- Dialectal Variation: Vocabulary differences across dialects
- Orthographic Inconsistency: Multiple valid spellings for the same word

## Methods

### Feature Selection and Preprocessing
- Consolidated data from multiple Excel workbooks
- Removed punctuation and diacritics
- Normalized text to handle spelling inconsistencies
- Removed duplicates and stop words
- Implemented lemmatization for root word forms

### Topic Modeling
- Utilized BERTopic for enhanced topic coherence
- Tested two Arabic language embeddings:
  - AraVec (trained on 1.16B tokens from tweets and Wikipedia)
  - AraBERT (trained on 2B+ tokens from online Arabic corpora)
- Applied TF-IDF vectorization with:
  - n-gram range: (1,2)
  - min_df: 5
  - max_df: 0.8

## Results

The model successfully identified several distinct topic clusters:
1. Prison and prosecution related
2. Bodily harm/ailments
3. Interrogations
4. Denial of family visitation
5. Mistreatment
6. Sexual violence
7. Location-specific information
8. Torture-related content

Key findings:
- AraBERT embeddings performed significantly better than AraVec
- Topics showed high correlation in abuse patterns
- Two main cluster groups emerged:
  - Physical abuse
  - Psychological abuse and non-physical rights violations

## Model Card

| Aspect | Description |
|--------|-------------|
| Model Type | Unsupervised topic model using AraBERT embeddings |
| Use Case | Assist human rights practitioners in abuse documentation |
| Training Data | ~1,100 testimonies ranging from sentences to paragraphs |
| Limitations | Specific to human rights documentation domain |
| Evaluation | Based on topic interpretability |
| Ethical Considerations | Requires careful data anonymization to protect subjects |

## Future Work

Planned improvements include:
- Applying the model to prison letter corpus
- Implementing quantitative coherence metrics
- Real-world deployment in documentation work


DAGSHUB with DVC pipeline: https://dagshub.com/yousufabdelfatah/Analyzing-Text-of-Rights-Abuse-Testimony 
