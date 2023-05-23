import json


def read_json(file_path):
    with open(file_path, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            decription = item['description'].split(' ')
            description_words.extend(decription)

if __name__ == '__main__':
    read_json('newsafr.json')