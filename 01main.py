import time
import datetime
import pandas as pd
from matplotlib import pyplot as plt

from diagramme import diagramme
from dataframes import dataframes
from daten import daten
from settings import f_settings
# from PDF import pdf_erstellen
from image import image_resize_append

import sys
import subprocess

# Settings
# bool_EP, bool_rolling = f_settings()

from datetime import date
today = date.today().strftime("%d.%m.%Y")

current_year = date.today().year
current_month = date.today().month
current_day = date.today().day
# print(f'{current_year} {current_month} {current_day}')

# Einstellungen
AnzahlJahre, bool_WochenTrend, bool_KurzzeitTrend, bool_MittelTrend, bool_LangzeitTrend, bool_costprice, bool_Streuung = f_settings()

# Datum Filter
period1 = int(time.mktime(datetime.datetime(current_year-AnzahlJahre, current_month, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(current_year, current_month, current_day, 23, 59).timetuple()))

# erstes bis zweites halving BTC
# period1 = int(time.mktime(datetime.datetime(2014, 6, 30, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2016, 7, 9, 23, 59).timetuple()))

# zweites bis drittes halving BTC
# period1 = int(time.mktime(datetime.datetime(2016, 7, 9, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2020, 5, 11, 23, 59).timetuple()))

# # # nach zweitem halving BTC
# period1 = int(time.mktime(datetime.datetime(2020, 5, 11, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2024, 12, 31, 23, 59).timetuple()))

interval = '1d'
# interval = '1wk'
# interval = '1m'


dict_aktien, dict_bezeichnung_aktien, image_paths, dict_y_aktien, pfad_output = daten()

# main loop
for key in dict_aktien:
    aktie=dict_aktien[key]
    bezeichnung_aktie = dict_bezeichnung_aktien[aktie]
    y_aktie = dict_y_aktien[aktie]
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{aktie}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    print(f'01main() bezeichnung_aktie= {bezeichnung_aktie}')

    # function Dataframes
    df, rolling_window0, rolling_window1, rolling_window2, rolling_window3 = dataframes(query_string, today, bezeichnung_aktie)

    # function Diagramme
    diagramme(df, rolling_window0, rolling_window1, rolling_window2, rolling_window3,today, bezeichnung_aktie, bool_WochenTrend, bool_KurzzeitTrend, bool_MittelTrend, bool_LangzeitTrend, y_aktie, bool_costprice, bool_Streuung, AnzahlJahre, pfad_output)

# pdf_erstellen()

image_resize_append(image_paths, pfad_output)

path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(path)
subprocess.Popen('explorer "D:\OneDrive\Github Output"')

print('fertig :-)')