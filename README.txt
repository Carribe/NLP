1. Описание:
Данный скрипт представляет собой программу для обработки текстовых данных, анализа частоты встречаемости слов различных частей речи (существительные, прилагательные, глаголы)
и создания wordcloud (облака слов) из наиболее часто встречающихся слов. Обработка текстов происходит параллельно с использованием многопроцессорности для повышения производительности.

2. Зависимости:
Перед запуском кода убедитесь, что в вашем виртуальном окружении установлены следующие библиотеки:
pandas: для работы с таблицами данных.
wordcloud: для создания wordcloud.
multiprocessing: для параллельной обработки текстов.
tqdm: для отображения прогресса обработки.
spacy: для обработки текстов на русском языке.

Также перед первым запуском кода нужно загрузить и установить модель ru_core_news_sm для обработки текстов на русском языке с помощью команды python -m spacy download ru_core_news_sm.

3. Входные данные:
Входные данные представляют собой CSV-файл с текстами для анализа. Путь к CSV-файлу указывается в переменной csv_file.
CSV-файл должен содержать столбец с текстами, помеченными меткой "Текст".

4. Обработка текстов:
Тексты из CSV-файла обрабатываются параллельно с использованием многопроцессорности.
Обработка происходит для каждой части речи (существительные, прилагательные, глаголы) отдельно.

5. Ограничения обработки:
В коде реализованы два ограничения обработки:
Ограничение длины слов: слова, содержащие менее трех символов, не учитываются при анализе.
Удаление низкочастотных слов: слова, встречающиеся менее 10 раз, также не учитываются при анализе.

6. Результаты анализа:
После обработки текстов для каждой части речи, код создает wordcloud на основе частоты встречаемости слов и сохраняет его в папке с текущей датой,
которая автоматически создается в директории исполнения скрипта. Также создается CSV-файл с результатами анализа частоты встречаемости слов для каждой части речи.

7. Запуск скрипта:
Для запуска скрипта убедитесь, что ваше виртуальное окружение активировано, а также выполнены все требования к зависимостям.
Затем запустите скрипт командой python main.py или python3 main.py в командной строке (терминале).

8. Примечание:
Перед первым запуском скрипта убедитесь, что путь к CSV-файлу в переменной csv_file указан правильно и содержит данные для анализа.
Также убедитесь, что модель ru_core_news_sm загружена и доступна для обработки текстов на русском языке.
Если модель еще не установлена, выполните команду python -m spacy download ru_core_news_sm для загрузки и установки модели.


1. Description:
This script is a program for processing text data, analyzing the frequency of occurrence of words of different parts of speech (nouns, adjectives, verbs),
and creating wordclouds from the most frequently occurring words. Text processing is performed in parallel using multiprocessing to improve performance.

2. Dependencies:
Before running the code, make sure you have the following libraries installed in your virtual environment:
pandas: for working with data tables.
wordcloud: for creating wordclouds.
multiprocessing: for parallel text processing.
tqdm: for displaying the processing progress.
spacy: for text processing in Russian language.

Additionally, before the first run, you need to download and install the ru_core_news_sm model
for text processing in Russian using the command python -m spacy download ru_core_news_sm.

3. Input Data:
The input data is a CSV file with texts for analysis. The path to the CSV file is specified in the csv_file variable.
The CSV file should contain a column with texts labeled as "Text".

4. Text Processing:
Texts from the CSV file are processed in parallel using multiprocessing.
The processing is performed separately for each part of speech (nouns, adjectives, verbs).

5. Processing Constraints:
The code implements two processing constraints:
Word Length Limit: Words containing less than three characters are not considered during the analysis.
Low-Frequency Word Removal: Words that occur less than 10 times are also not considered during the analysis.

6. Analysis Results:
After processing texts for each part of speech, the code creates wordclouds based on the frequency of word occurrences
and saves them in a folder with the current date, which is automatically created in the script's execution directory.
Additionally, CSV files are created with the results of the word frequency analysis for each part of speech.

7. Running the Script:
To run the script, ensure that your virtual environment is activated, and all dependencies are met.
Then, execute the script using the command python main.py or python3 main.py in the command prompt (terminal).

8. Note:
Before the first run of the script,ensure that the path to the CSV file in the csv_file variable is correctly specified and contains the data for analysis.
Also, make sure that the ru_core_news_sm model is downloaded and available for text processing in Russian.
If the model is not installed yet, run the command python -m spacy download ru_core_news_sm to download and install the model.