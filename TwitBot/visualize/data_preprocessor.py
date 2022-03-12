from datetime import datetime

import pandas as pd


def convert_ukraine_stats_to_df(ukraine_stats):
    df = pd.DataFrame(ukraine_stats.get('data'))
    date_list = []
    for datetime_iso in df['end']:
        date_list.append(datetime.strptime(datetime_iso, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d-%m"))
    df['date'] = date_list
    return df.drop(['end', 'start'], axis=1)
