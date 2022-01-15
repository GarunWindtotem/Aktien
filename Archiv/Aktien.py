# import modules
from datetime import datetime
from datetime import date
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
# import numpy as np
# import matplotlib.dates as mdates
# from matplotlib.ticker import FuncFormatter

today = date.today().strftime("%d.%m.%Y")
minticks = 5
maxticks = None

dict_Depot = {
    "1": "BYW.DE",  ## Baywa
    "2": "HOC.DE",  ## Holidaycheck
    "3": "INR.DE",  ## Intern Cons Airline
    "4": "JAL.F",  ## Japan Airlines
    "5": "LHA.DE",  ## Lufthansa
    "6": "MSF.DE",  ## Microsoft
    "7": "PAH3.DE",  ## Porsche
    "8": "RY4C.F",  ## Ryanair
    "9": "XY6.DE"  ## Xylem
}

dict_Depot_EP = {
    "1": "52.500",  ## Baywa
    "2": "3.280",  ## Holidaycheck
    "3": "2.333",  ## Intern Cons Airline
    "4": "19.948",  ## Japan Airlines
    "5": "10.674",  ## Lufthansa
    "6": "202.800",  ## Microsoft
    "7": "97.460",  ## Porsche
    "8": "16.860",  ## Ryanair
    "9": "98.140"  ## Xylem
}

dict_Depot_name = {
    "BYW.DE": "Baywa",  ## Baywa
    "HOC.DE": "Holidaycheck",  ## Holidaycheck
    "INR.DE": "Intern. Cons. Airline",  ## Intern Cons Airline
    "JAL.F": "Japan Airlines",  ## Japan Airlines
    "LHA.DE": "Lufthansa",  ## Lufthansa
    "MSF.DE": "Microsoft",  ## Microsoft
    "PAH3.DE": "Porsche",  ## Porsche
    "RY4C.F": "Ryanair",  ## Ryanair
    "XY6.DE": "Xylem"  ## Xylem
}

# print(dict_Depot_EP["5"])
# print(dict_Depot["2"])


def create_df(i):
    # initialize parameters
    start_date = datetime(2021, 6, 1)
    end_date = datetime(2021, 7, 8)
    name_aktie = str(dict_Depot[i])
    name_aktie_depot = str(dict_Depot_name[name_aktie])
    # get the data
    df = yf.download(name_aktie, start=start_date, end=end_date)
    df = df.reset_index(level=0)
    df.index=list(range(0, len(df["Low"])))
    df["EP"] = float(dict_Depot_EP[i])
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    win_loss = round(df["Low"].iloc[-1] - df["EP"].max(), 2)
    chart(df, name_aktie, name_aktie_depot, win_loss)
    return (df, name_aktie, name_aktie_depot, win_loss)


def chart(df, name_aktie, name_aktie_depot, win_loss):
    # display
    size = 20
    plt.style.use('seaborn')
    #     fig, ax = plt.subplots(figsize=(16, 9))
    plt.figure(figsize=(20, 10))
    plt.plot(df["Date"], df['Low'], linestyle="solid", linewidth=size * 0.2, marker=".", color="black", label="Low")
    plt.plot(df["Date"], df['EP'], linestyle="--", linewidth=size * 0.2, marker="", color="black", label="EP")
    plt.title(f'{name_aktie_depot}, {win_loss} € \n', fontsize=size * 1.5)
    plt.suptitle(today + ' PW', fontsize=size, y=0.91)
    plt.fill_between(df["Date"], df["Low"], df["EP"], color="green", interpolate=True, alpha=0.5,
                     where=df["Low"] > df["EP"], label="Gewinn")
    plt.fill_between(df["Date"], df["Low"], df["EP"], color="red", interpolate=True, alpha=0.5,
                     where=df["Low"] < df["EP"], label="Verlust")
    #     plt.fill_between(df["Date"], df['change_1_MW'], df['R1'], label = "Erhöhung Neuinfektionen",
    #                  color='red',alpha=0.5, interpolate=True, where = df['change_1_MW'] > 0 )
    plt.legend(loc='upper center',
               bbox_to_anchor=(0.5, -0.20),
               fancybox=True,
               shadow=True,
               ncol=2,
               fontsize=size)

    plt.xticks(fontsize=size, rotation=45)
    plt.yticks(fontsize=size)
    plt.ylabel('Wert [€]', fontsize=size)
    plt.xlabel('Zeit', fontsize=size)
    plt.savefig(f'D:\\Github\\Aktien\\Output\\{name_aktie_depot}.png', dpi=100, bbox_inches='tight')

for i in dict_Depot:
    create_df(i)
