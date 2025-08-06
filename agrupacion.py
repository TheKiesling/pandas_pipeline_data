import pandas as pd

class DataGrouper:
    def __init__(self, dataframe):
        self.df = dataframe

    def group_by_column_count(self, column_name):
        grouped = self.df.groupby(column_name).size().reset_index(name='count')
        return grouped