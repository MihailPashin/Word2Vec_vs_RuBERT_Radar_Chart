from Loading_DataSet.load import DataProcessor
from Topics.topics_themes import dict_for_razmetka
def print_group_names():
    for key, value in dict_for_razmetka.items():
        print(f'Тематика отзывов {key+1} {value["name_group"]}')
print_group_names()
    # Our main program.
Ready_DataFrame = DataProcessor('Loading_DataSet/data/New_coordinates_titles.csv')
Ready_DataFrame.drop_columns()
Ready_DataFrame.reset_index()
Ready_DataFrame.set_index('title')
Ready_DataFrame.remove_row_by_index()
Ready_DataFrame.reset_index()
Ready_DataFrame.split_coordinates_column('coord')
Ready_DataFrame.convert_to_float(['coord_X', 'coord_Y'])
