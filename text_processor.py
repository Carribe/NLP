import spacy

# Загрузка модели для русского языка
nlp = spacy.load("ru_core_news_sm")

# Функции для обработки текста и получения списка лемм (начальных форм слов) по каждой части речи
def process_nouns(text):
    doc = nlp(text)
    lemmatized_nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN" and token.lemma_ not in stop_words and len(token.lemma_) >= 3]
    return lemmatized_nouns

def process_adjectives(text):
    doc = nlp(text)
    lemmatized_adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ" and token.lemma_ not in stop_words and len(token.lemma_) >= 3]
    return lemmatized_adjectives

def process_verbs(text):
    doc = nlp(text)
    lemmatized_verbs = [token.lemma_ for token in doc if token.pos_ == "VERB" and token.lemma_ not in stop_words and len(token.lemma_) >= 3]
    return lemmatized_verbs

# Разделение текстов на пакеты для параллельной обработки
batch_size = 1024
stop_words = spacy.lang.ru.stop_words.STOP_WORDS.union("-")
