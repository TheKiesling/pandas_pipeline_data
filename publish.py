class Publisher:
    def __init__(self, file_type):
        self.file_type = file_type
        
    def publish(self, dataframe, file_name):
        if self.file_type == 'csv':
            dataframe.to_csv(file_name, index=False)
        elif self.file_type == 'excel':
            dataframe.to_excel(file_name, index=False)
        elif self.file_type == 'json':
            dataframe.to_json(file_name, orient='records', lines=True)
