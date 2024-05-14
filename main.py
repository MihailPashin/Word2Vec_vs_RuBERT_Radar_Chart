from Word2Vec.distributive_semantics import Word2VecModel
from Loading_DataSet.load import DataProcessor
from Topics.topics_themes import dict_for_razmetka

# My main.py
if __name__ == "__main__" :
    def print_group_names():
        for key, value in dict_for_razmetka.items():
            print(f'Тематика отзывов {key+1} {value["name_group"]}')
    print_group_names()
    # Our main program.
    df = DataProcessor('Loading_DataSet/data/New_coordinates_titles.csv')
    df.drop_columns()
    df.reset_index()
    df.set_index('title')
    df.remove_row_by_index()
    df.reset_index()
    df.split_coordinates_column('coord')
    df.convert_to_float(['coord_X', 'coord_Y'])
    keywords = df.extract_keywords()
    print(len(keywords))
    print(keywords[0:3])
    full_dataset = df.view_reviews()
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
