from Word2Vec.distributive_semantics import Word2VecModel
from RuBERT.load_bert import ruBERT
from RuBERT.using_ruBERT import BERT_Process
from Topics.topics_themes import dict_for_razmetka
from Loading_DataSet.load import DataProcessor
from Loading_DataSet.ready_dataframe import Ready_DataFrame

if __name__ == "__main__" :

    print(f'ready df - {Ready_DataFrame.df}')
    
    keywords = Ready_DataFrame.extract_keywords()
    print(f' type of keywords = {type(keywords)}')
    print(keywords[0:3])
    
    full_dataset = list(Ready_DataFrame.df['message'])
    print(full_dataset[0:3])
    print(f' type of full_dataset = {type(full_dataset)}')
    
    word2vec_model_tiny = Word2VecModel()
    word2vec_model_large = Word2VecModel('Word2Vec/preloaded_model/14cities.model')
    train_tokens = word2vec_model_tiny.tokenize_corpus(full_dataset)

    result=[]
    for wv_model in [word2vec_model_tiny,word2vec_model_large]:
        if wv_model.model is None:
            print('Создаём схему')
            wv_model.creating_word2vec_model(train_tokens)
        result.append(wv_model.filter(dict_for_razmetka))
    print(f'len {len(result)}')
    print(f'len {len(result[0])}')
    print(f'len {len(result[1])}')
   
    model_ruBERT = BERT_Process()
    model_ruBERT.preprocess_yake_phrases(keywords)
    print(f'Эмбединги извлечены. Активируем скрипт')    
    result.append(model_ruBERT.summarization_indexes(dict_for_razmetka))
    
    print(f'len {len(result)}')
    print(f'len {len(result[0])}')
    print(f'len {len(result[1])}')
    print(f'len {len(result[2])}')
    print(f'result from bolnichka {result[2][0]}')
