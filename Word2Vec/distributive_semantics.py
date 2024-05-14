import gensim
import pandas as pd
import re
import numpy as np
from nltk.stem.snowball import SnowballStemmer
from operator import itemgetter
from collections import Counter
import itertools


class Word2VecModel:

    def __init__(self, model_path=None):
        if model_path:
            try:
                self.model = gensim.models.Word2Vec.load(model_path)
            except:
                print('Путь к файлу некорректный')
                self.model = None
        else:
            self.model = None

    def creating_word2vec_model(self, train_tokens, vector_size=30, window=4, min_count=5, workers=6, sg=2, epochs=20):
        self.model = gensim.models.Word2Vec(sentences=train_tokens, vector_size=vector_size, window=window,
                                             min_count=min_count, workers=workers, sg=sg, epochs=epochs)


    def tokenize_text_simple_regex(txt, min_token_size=4):
        #print(txt)
        TOKEN_RE = re.compile(r'[\w\d]+')
        txt = txt.lower()
        all_tokens = TOKEN_RE.findall(txt)
        return [token for token in all_tokens if len(token) >= min_token_size]

    def tokenize_corpus(self,texts, tokenizer=tokenize_text_simple_regex):
        #print(texts[0:4])
        return [tokenizer(text) for text in texts]
    # Поиск соседей
    # My class Word2VecModel:
    def get_neighbor(self,word,neighbor_counts=20):

        try:
            # Derive the vector for the word "парковка" in our model
            vector = self.model.wv[word]

            normal_neighbors = self.model.wv.most_similar([vector], topn=neighbor_counts)
            aggregated_sosedi=[]

            for neighbor in normal_neighbors[0:50]:
                aggregated_sosedi.append(neighbor[0])
            #print(aggregated_sosedi)
            return aggregated_sosedi
        except KeyError:
            print(f"Слово {word} не найдено в обученной модели")
            pass

            #raise
    # Поиск соседи по списку list
    def save_neigbor(self, lists):
        sosedi = []
        try:
          for el in lists:
              print(f'{el} s')
              sosedis=self.get_neighbor(el)
              if sosedis:
                sosedi.extend(sosedis)
                print(f'sosedis - {sosedis}')
              else:
                print(f"Ненайденное слово пропущенное")

          return sosedi
        except TypeError:
            pass

    def stemmer_and_regex(self,neighbors):
        stemmer = SnowballStemmer("russian")
        answer =  [ [stemmer.stem(word).lower()+'\w{0,}' if i < len(item.split()) - 1
                    else stemmer.stem(word).lower()
                    for i, word in enumerate(item.split())]\
           for item in neighbors ]
           #for item in neighbors # deleted row - for item in neighbors
            # deleted row - for item in neighbors
        united_list = [(' '.join(sublist)).strip().lower() for sublist in answer]
        rst_without_dublicates = list(set(itertools.chain(united_list)))
        #print(f'without_dublicates {rst_without_dublicates}')
        return rst_without_dublicates

    def filter(self,my_dict):
        list_by_groups=[]
      # Распаковка вложенного словаря
        name_groups = []
        candidates = []
        for item in my_dict.values():
            name_groups.append(item['name_group'])
            candidates.append(item['candidates'])
        print(name_groups)
        print(candidates)
        for key, value in enumerate(candidates):
            rst_without_dublicates = []
          #print(f'item - {value}')
            print(f'value - {value}')
            print(f'kostroma - {self}')
            embed_finding=self.save_neigbor(value)
            print(f' word2vec - {embed_finding}, candidates - {value} ')

            result=self.stemmer_and_regex(embed_finding)
  
            list_by_groups.append(result) #result_for_one_group
        return  list_by_groups
