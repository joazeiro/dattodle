import pandas as pd
import os
import csv
import json 

test = pd.read_csv('C:\\Users\\maria.gomes\\Desktop\\Work\\dattodle\\dattodle\\deviceInfo\\devices.csv')
test.to_json('C:\\Users\\maria.gomes\\Desktop\\Work\\dattodle\\dattodle\\deviceInfo\\test.json', orient='records', lines=True)