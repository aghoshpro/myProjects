# Environment Setup

### Important Pkgs

- [Gensim](https://radimrehurek.com/gensim/)
- [map()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)

### NLTK

```
import nltk
print('NLTK Version: %s' % (nltk.__version__))
#nltk.download('stopwords') # Run if using nltk for the first time ever
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
```

### SpaCy

```
import spacy
print('spaCy Version: %s' % (spacy.__version__))
```

### Text Cleaning and Processing

input_text = "Diego went back to UniverSity"

- **_Normalize_** - [e.g., diego went back to university]
- **_Tokenize_** - [e.g., 'deigo', 'went', 'back', 'to', 'university']
- **_Stop Words Removal_** - [e.g., 'deigo', 'went', 'university']
- **_Lematazialtion_** - [e.g., 'deigo', 'go', 'university']
- **_Stemming_** [e.g., 'deigo', 'go', 'univers']

#### Preparing Stopwords

```
nlp = spacy.load('en_core_web_sm')
stopwordsSpacy = nlp.Defaults.stop_words
#stopwordsSpacy = spacy.lang.en.stop_words.STOP_WORDS

print("SPACY Stopwords # = ",len(stopwordsSpacy))

stopwordsNLTK = stopwords.words("english")
print("NLTK Stopwords # = ",len(stopwordsNLTK))
```

### Combine nltk & spacy stopwords

**Resources :** [StopWords](https://medium.com/@makcedward/nlp-pipeline-stop-words-part-5-d6770df8a936)

## Projects

### 1. Topic Modelling

### 2. Sentiment Analysis
