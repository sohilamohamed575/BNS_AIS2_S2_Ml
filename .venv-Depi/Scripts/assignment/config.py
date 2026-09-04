DROP_CLO = ['PassengerId', 'Name', 'Ticket']

def drop_columns(df, columns):
    return df.drop(columns=columns, errors='ignore')