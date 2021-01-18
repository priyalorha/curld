import json

import pandas as pd
import os

from models.stocks import TickerData


def save_data(data: dict) -> bool:
    try:
        TickerData(
            **data).save()
        return True
    except Exception as err:
        print(err)
        return False


def read_json_and_store(filename: str, filepath: str = '/') :
    file = os.path.join(filepath, filename)
    if os.path.exists(file):
        try:
            df = pd.read_json(file, orient='index')
            df = pd.read_json('fetchTicker.json', orient='index')
            df.apply(save_data, axis=1)
            return True
        except FileNotFoundError:
            return pd.DataFrame()

        except Exception as err:
            print(err)
            return pd.DataFrame()




