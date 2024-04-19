from refined.inference.processor import Refined
from trial import make_news_data
import pandas as pd
from collections import defaultdict
import re


url = "https://www.thehindu.com/news/national/"
# news = make_news_data(url)
# path = 'news.csv'

refined = Refined.from_pretrained(model_name='wikipedia_model',
                                  entity_set="wikipedia")


class FreqFinder:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.freq_map = {}
        self.sorted_entity = []

    def check_match(self, file_path, term):
        print(f"Checking for term {term} in wikipedia dump")
        with open(file_path, 'r') as file:
            for line in file:
                if re.fullmatch(term, re.escape(line.strip())):
                    return True

        return False


    def find_freq(self):
        for index, row in self.df.iterrows():
            results = refined.process_text(row['content'])
            date = row['publish_date']
            url = row['url']
            title = row['headline']
            curr_news_entity = defaultdict(bool)
            
            print(index)
            print('\n')
            # print(dir(results[0]))
            for result in results:
                print(result)
                entity = result.text
                wp_page = result.predicted_entity.wikipedia_entity_title

                if wp_page == None:
                    # if self.check_match('combined_titles.txt', entity):
                    if entity in self.freq_map and not curr_news_entity[entity]:
                        self.freq_map[entity][0] += 1
                        self.freq_map[entity][1].append([title, date, url])

                    else:
                        self.freq_map[entity] = [1, [[title, date, url]]]
                        curr_news_entity[entity] = True

        # for key in self.freq_map:
        #     if self.freq_map[key][0] > 1:
        #         print(key)
        #         print(self.freq_map[key])

        self.sorted_entity = sorted(self.freq_map, key = lambda x: self.freq_map[x][0], reverse=True)

if __name__ == '__main__':
    path = 'combined.csv'
    f = FreqFinder(path)
    f.find_freq()
#    for entity in self.sorted_entity:
#        st.write(entity)
