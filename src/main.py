import pandas as pd
from pathlib import Path
from tabulate import tabulate

def read_tags(csv_file):
    tag_file = Path(csv_file)
    if tag_file.is_file() is False:
        raise Exception('Tag file specified is not a file')
    return pd.read_csv(csv_file)

def get_data_filenames():
    csv_files = Path(__file__).parent.parent.joinpath("data").glob('**/*.csv')
    files = [filename for filename in csv_files if filename.is_file()]
    return files

def data_files_to_display(data_files):
    data = []
    for data_file in data_files:
        data.append([data_file.name, str(data_file.absolute())])
    print(tabulate(data, tablefmt='psql', headers=['Name', 'Path']))

if __name__ == '__main__':
    data_files = get_data_filenames()
    data_files_to_display(data_files)
    tags_frame = read_tags(next(filter(lambda x: x.name.endswith('Tag.csv'), data_files), None))
    # row_count = len(tags_frame.index)
    tags_frame = tags_frame[tags_frame['Type'] == 'INVENTORY']
    history_frame = read_tags(next(filter(lambda x: x.name.endswith('HistoryLog.csv'), data_files), None))
    merged = history_frame.merge(tags_frame, how='inner', left_on='HistoryLogID', right_on='TagHistoryLogID')
    customer_records = pd.DataFrame(merged, columns=['CustomerID', 'Type', 'Tag', 'CreationDateTime'])
    by_id = customer_records.groupby("CustomerID")
    for customer_id, frame in by_id:
        with pd.option_context('mode.chained_assignment', None):
            customer_records_by_id = customer_records[customer_records["CustomerID"] == customer_id]
            customer_records_by_id['CreationDateTime'] = pd.to_datetime(customer_records_by_id['CreationDateTime'])
            customer_records_by_id.sort_values(by=['CreationDateTime'], inplace=True, ascending=False)
            print(tabulate(customer_records_by_id, headers='keys', tablefmt='psql'))