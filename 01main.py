import time
import datetime
import pandas as pd
from matplotlib import pyplot as plt

from diagramme import diagramme
from dataframes import dataframes
from daten import daten
from settings import f_settings

# Settings
bool_EP, bool_rolling = f_settings()

titel_beschreibung = ""

# Datum Filter
period1 = int(time.mktime(datetime.datetime(2021, 10, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 12, 30, 23, 59).timetuple()))

# erstes bis zweites halving BTC
# period1 = int(time.mktime(datetime.datetime(2014, 6, 30, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2016, 7, 9, 23, 59).timetuple()))

# zweites bis drittes halving BTC
# period1 = int(time.mktime(datetime.datetime(2016, 7, 9, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2020, 5, 11, 23, 59).timetuple()))

# # # nach zweitem halving BTC
# period1 = int(time.mktime(datetime.datetime(2020, 5, 11, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2024, 12, 31, 23, 59).timetuple()))

interval = '1d' # 1d, 1wk, 1m 

from datetime import date
today = date.today().strftime("%d.%m.%Y")

dict_aktien, dict_bezeichnung_aktien, dict_n_aktien, dict_EP_aktien = daten()

# main loop
for key in dict_aktien:
    aktie=dict_aktien[key]
    n_aktie=dict_n_aktien[aktie]
    EP_Aktie=dict_EP_aktien[aktie]
    bezeichnung_aktie = dict_bezeichnung_aktien[aktie]
    Einstandswert = round(EP_Aktie * n_aktie, 1)
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{aktie}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    # function Dataframes
    df, aktueller_Wert, rolling_window1, rolling_window2, rolling_window3 = dataframes(query_string, EP_Aktie, n_aktie, today, bezeichnung_aktie)

    # function Diagramme
    diagramme(df, rolling_window1, rolling_window2, rolling_window3, aktie, interval, today, Einstandswert, aktueller_Wert, bezeichnung_aktie, bool_EP, titel_beschreibung)

print('fertig')