import pandas as pd
from wordcloud import WordCloud
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from collections import Counter
from text_processor import process_nouns, process_adjectives, process_verbs
from text_generator import text_generator
import spacy
import os
import datetime

def create_output_directory():
    # Получаем текущую дату
    current_date = datetime.date.today()
    # Преобразуем дату в строку в формате "год_месяц_день"
    folder_name = current_date.strftime("%Y_%m_%d")
    # Путь к папке с текущей датой
    output_directory = os.path.join(os.getcwd(), folder_name)

    # Создаем папку, если её нет
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    return output_directory

def process_texts_parallel(process_func, df, csv_file, batch_size, num_cores):
    result_freq = Counter()
    with Pool(num_cores) as pool, tqdm(total=len(df)//batch_size) as pbar:
        for lemmas in pool.imap_unordered(process_func, text_generator(csv_file, batch_size)):
            result_freq.update(lemmas)
            pbar.update(1)
    return result_freq

def save_wordcloud_to_file(wordcloud, output_directory, filename):
    wordcloud.to_file(os.path.join(output_directory, filename))

def save_frequency_to_csv(freq_data, output_directory, filename):
    # Преобразуем словарь в объект Counter
    freq_counter = Counter(freq_data)
    df = pd.DataFrame(freq_counter.most_common(), columns=["Word", "Frequency"])
    df.to_csv(os.path.join(output_directory, filename), index=False)

def main():
    # Создаем папку с текущей датой и временем
    output_directory = create_output_directory()

    # Загрузка данных из CSV файла
    csv_file = "/Users/artem/Downloads/Chuv_22.07.2023-24.07.2023_csv - Chuv_22.07.2023-24.07.2023_64bfa133556c525cf518f633.csv.csv"

    df = pd.read_csv(csv_file, sep=",", encoding="utf-8", skiprows=4)

    # Обработка текстов параллельно для каждой части речи
    batch_size = 1024
    num_cores = cpu_count()

    def filter_low_frequency_words(word_freq, min_frequency=10):
        filtered_word_freq = {word: freq for word, freq in word_freq.items() if freq >= min_frequency}
        return filtered_word_freq

    # Обработка существительных
    noun_freq = process_texts_parallel(process_nouns, df, csv_file, batch_size, num_cores)
    noun_freq = filter_low_frequency_words(noun_freq, min_frequency=10)
    save_wordcloud_to_file(WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(noun_freq),
                           output_directory, "wordcloud_nouns.png")
    save_frequency_to_csv(noun_freq, output_directory, "nouns_frequency.csv")

    # Обработка прилагательных
    adj_freq = process_texts_parallel(process_adjectives, df, csv_file, batch_size, num_cores)
    adj_freq = filter_low_frequency_words(adj_freq, min_frequency=10)
    save_wordcloud_to_file(WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(adj_freq),
                           output_directory, "wordcloud_adj.png")
    save_frequency_to_csv(adj_freq, output_directory, "adjectives_frequency.csv")

    # Обработка глаголов
    verb_freq = process_texts_parallel(process_verbs, df, csv_file, batch_size, num_cores)
    verb_freq = filter_low_frequency_words(verb_freq, min_frequency=10)
    save_wordcloud_to_file(WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(verb_freq),
                           output_directory, "wordcloud_verbs.png")
    save_frequency_to_csv(verb_freq, output_directory, "verbs_frequency.csv")


if __name__ == "__main__":
    main()
