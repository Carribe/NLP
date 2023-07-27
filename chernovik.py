# import pandas as pd
# from wordcloud import WordCloud
# from multiprocessing import Pool, cpu_count
# from tqdm import tqdm
# from collections import Counter
# from text_processor import process_nouns, process_adjectives, process_verbs
# from text_generator import text_generator
# import spacy
# import os
# import datetime
#
# def create_output_directory():
#     # Получаем текущую дату и время
#     current_datetime = datetime.datetime.now()
#     # Преобразуем дату в строку в формате "год_месяц_день_час_минута_секунда"
#     folder_name = current_datetime.strftime("%Y_%m_%d_%H_%M_%S")
#     # Путь к папке с текущей датой и временем
#     output_directory = os.path.join(os.getcwd(), folder_name)
#
#     # Создаем папку, если её нет
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)
#
#     return output_directory
# def main():
#     # Создаем папку с текущей датой и временем
#     output_directory = create_output_directory()
#
#     # Загрузка модели для русского языка
#     nlp = spacy.load("ru_core_news_sm")
#
#     # Загрузка данных из CSV файла
#     csv_file = "/Users/artem/Downloads/Chuv_22.07.2023-24.07.2023_csv - Chuv_22.07.2023-24.07.2023_64bfa133556c525cf518f633.csv.csv"
#
#     df = pd.read_csv(csv_file, sep=",", encoding="utf-8", skiprows=4)
#     noun_freq = Counter()
#     adj_freq = Counter()
#     verb_freq = Counter()
#
#     # Обработка текстов параллельно для каждой части речи
#     batch_size = 1024
#     num_cores = cpu_count()
#     with Pool(num_cores) as pool, tqdm(total=len(df)//batch_size) as pbar:
#         for lemmas in pool.imap_unordered(process_nouns, text_generator(csv_file, batch_size)):
#             noun_freq.update(lemmas)
#             pbar.update(1)
#
#     with Pool(num_cores) as pool, tqdm(total=len(df)//batch_size) as pbar:
#         for lemmas in pool.imap_unordered(process_adjectives, text_generator(csv_file, batch_size)):
#             adj_freq.update(lemmas)
#             pbar.update(1)
#
#     with Pool(num_cores) as pool, tqdm(total=len(df)//batch_size) as pbar:
#         for lemmas in pool.imap_unordered(process_verbs, text_generator(csv_file, batch_size)):
#             verb_freq.update(lemmas)
#             pbar.update(1)
#
#         # Сохранение облаков слов в папку с текущей датой и временем
#         wordcloud_nouns = WordCloud(width=800,
#                                     height=400,
#                                     background_color="white").generate_from_frequencies(noun_freq)
#         wordcloud_adj = WordCloud(width=800,
#                                   height=400,
#                                   background_color="white").generate_from_frequencies(adj_freq)
#         wordcloud_verbs = WordCloud(width=800,
#                                     height=400,
#                                     background_color="white").generate_from_frequencies(verb_freq)
#
#         wordcloud_nouns.to_file(os.path.join(output_directory, "wordcloud_nouns.png"))
#         wordcloud_adj.to_file(os.path.join(output_directory, "wordcloud_adj.png"))
#         wordcloud_verbs.to_file(os.path.join(output_directory, "wordcloud_verbs.png"))
#
#         # Сохранение частотности в CSV файлы в папке с текущей датой и временем
#         df_nouns = pd.DataFrame(noun_freq.most_common(), columns=["Word", "Frequency"])
#         df_adj = pd.DataFrame(adj_freq.most_common(), columns=["Word", "Frequency"])
#         df_verbs = pd.DataFrame(verb_freq.most_common(), columns=["Word", "Frequency"])
#
#         df_nouns.to_csv(os.path.join(output_directory, "nouns_frequency.csv"), index=False)
#         df_adj.to_csv(os.path.join(output_directory, "adjectives_frequency.csv"), index=False)
#         df_verbs.to_csv(os.path.join(output_directory, "verbs_frequency.csv"), index=False)
#
#
# if __name__ == "__main__":
#     main()
#
# +++++++++++++++++++
#
#
# import pandas as pd
#
# def text_generator(filename, batch_size):
#     for chunk in pd.read_csv(filename, sep=",", encoding="utf-8", skiprows=4, chunksize=batch_size):
#         texts = chunk["Текст"].dropna()
#         for text in texts:
#             yield text
#
# +++++++++++++++++++
#
#
# import spacy
#
# # Загрузка модели для русского языка
# nlp = spacy.load("ru_core_news_sm")
#
# # Функции для обработки текста и получения списка лемм (начальных форм слов) по каждой части речи
# def process_nouns(text):
#     doc = nlp(text)
#     lemmatized_nouns = [token.lemma_ for token in doc if token.pos_ == "NOUN" and token.lemma_ not in stop_words]
#     return lemmatized_nouns
#
# def process_adjectives(text):
#     doc = nlp(text)
#     lemmatized_adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ" and token.lemma_ not in stop_words]
#     return lemmatized_adjectives
#
# def process_verbs(text):
#     doc = nlp(text)
#     lemmatized_verbs = [token.lemma_ for token in doc if token.pos_ == "VERB" and token.lemma_ not in stop_words]
#     return lemmatized_verbs
#
# # Разделение текстов на пакеты для параллельной обработки
# batch_size = 1024
# stop_words = spacy.lang.ru.stop_words.STOP_WORDS.union("-")
