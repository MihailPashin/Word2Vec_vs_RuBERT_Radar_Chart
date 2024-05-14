import pandas as pd
import yake

class DataProcessor:
    columns_for_deletion = ['web-scraper-start-url', 'review_link-href', 'review_link'];
    except_raion = 'АвтоТехСтрой'
    column_for_extracting = 'message'
    def __init__(self, filename):
        self.df = pd.read_csv(filename, index_col=0)
        self.yake_extractor = yake.KeywordExtractor(lan="ru", n=5, dedupLim=0.65, dedupFunc='seqm', windowsSize=1, top=15)

    def drop_columns(self, columns=columns_for_deletion):
        self.df.drop(columns, axis=1, inplace=True)

    def reset_index(self):
        self.df.reset_index(drop=True, inplace=True)

    def set_index(self, index_column):
        self.df.set_index(index_column, inplace=True)

    def remove_row_by_index(self, index_value=except_raion):
        self.df.drop(index_value, inplace=True)

    def split_coordinates_column(self, coordinates_column):
        self.df[['coord_X', 'coord_Y']] = self.df[coordinates_column].str.split(',', expand=True)

    def convert_to_float(self, columns):
        for column in columns:
            self.df[column] = pd.to_numeric(self.df[column])

    def display_info(self):
        print(self.df.info())

    def extract_keywords(self, message_column=column_for_extracting):
        print('Началось выделение ключевых фраз')        
        def extract_keywords_for_row(row):
            keywords = self.yake_extractor.extract_keywords(row[message_column])
            return [keyword[0] for keyword in keywords]
        self.df['new_Yake'] = self.df.apply(extract_keywords_for_row, axis=1)
        return list(self.df['new_Yake'])

    def view_reviews(self):
        return list(self.df['message'].dropna())





