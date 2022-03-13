import time
import datetime
import pandas as pd
from matplotlib import pyplot as plt

# Datum Filter
period1 = int(time.mktime(datetime.datetime(2021, 10, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 12, 30, 23, 59).timetuple()))
interval = '1d' # 1d, 1wk, 1m 

# Aktien Daten
dict_aktien = {
    '1': 'LHA.DE',
    '2': 'H4ZJ.DE',
    '3': 'E127.MI'}

# Anzahl Aktien
dict_n_aktien = {
    'LHA.DE': 148,
    'H4ZJ.DE': 133.636,
    'E127.MI': 6.258}

# Einstandspreis
dict_EP_aktien = {
    'LHA.DE': 6.379,
    'H4ZJ.DE': 27.451,
    'E127.MI': 47.942}


aktie = 'LHA.DE'
n_aktie = 148
EP_Aktie = 6.379

# Datenimport
query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{aktie}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
df = pd.read_csv(query_string)

df['Kurs'] = (1/2)*( df["Low"]+df["High"] )


length = len(df["Kurs"])
rolling_window1 = int(length*0.05)
rolling_window2 = int(length*0.25)

print(length)
print(rolling_window1)
print(rolling_window2)
print(period1)
print(period2)

df['Kurs_mean_1'] = df['Kurs'].rolling(window=rolling_window1, min_periods=1, center=True).mean()
df['Kurs_mean_2'] = df['Kurs'].rolling(window=rolling_window2, min_periods=1, center=True).mean()
df['Einstandspreis'] = EP_Aktie 
df["Steigung"] = 1
df = df.drop(columns=['Open', 'High', 'Low', 'Close', 'Adj Close'])
# a = df["Kurs_mean_1"].iloc[-3]
# a = df["Kurs_mean_1"].iloc[-2]
# a = df["Kurs_mean_1"].iloc[-1]

df.loc[df['Kurs_mean_1'] <= 6.3, 'smaller_6_3'] = 'smaller'

df["Steigung"] = df["Kurs_mean_1"] - df["Kurs_mean_1"].shift(periods=2)

aktueller_Kurs = df["Kurs"].iloc[-1]

Einstandswert = round(EP_Aktie*n_aktie,1)
aktueller_Wert = round(aktueller_Kurs*n_aktie,1)


# from datetime import datetime, timedelta
from datetime import date

today = date.today().strftime("%d.%m.%Y")
print(today)

df['Date'] = pd.to_datetime(df.Date, utc=True)

plt.figure(figsize=(24,9))
plt.style.use('seaborn')
plt.grid(True)


plt.plot(df["Date"], df["Kurs"], marker='.', linestyle='-', alpha=0.4,
    color="black", linewidth=3, label = "Tageskurs", markersize=15)


plt.plot(df["Date"], df["Kurs_mean_1"], marker='', linestyle='-',
    color="blue", linewidth=5, label = f'Kurzzeittrend ({rolling_window1} Tage)', markersize=10)

plt.plot(df["Date"], df["Kurs_mean_2"], marker='', linestyle='-',
    color="black", linewidth=7, label = f'Langzeittrend ({rolling_window2} Tage)', markersize=10)


plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='green', alpha=0.7,
    label=f'positiver Kurzzeittrend', interpolate=True,  where=(df["Kurs_mean_1"] > df["Kurs_mean_2"]))

plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='red', alpha=1,
    label=f'negativer Kurzzeittrend', interpolate=True, where=(df["Kurs_mean_1"] < df["Kurs_mean_2"]))

# Einstandspreis
plt.plot(df["Date"], df["Einstandspreis"], marker='', linestyle='-', alpha = 0.7,
    color="grey", linewidth=1.5, label = f'Einstandspreis', markersize=10)


# Legende
plt.legend(loc='upper center',
    bbox_to_anchor=(0.5, -0.2),
    fancybox=True,
    shadow=True,
    ncol=4,
    fontsize=20)

# Titel
plt.title(f'Kurswert {aktie}, ({interval})\n', fontsize=25)
plt.suptitle(f'{today}, Einstandswert = {Einstandswert} €, aktueller Wert = {aktueller_Wert} €', fontsize=20, y=0.92)

# Schriftgrößen x und y achsenwerte
plt.xticks(fontsize=15, rotation=0)
plt.yticks(fontsize=15)

plt.ylabel("Euro", fontsize=25)
plt.xlabel("Zeit", fontsize=25)

plt.savefig(f'D:\\Github\\Aktien\\Output\\{today} {aktie}.png', dpi=300, bbox_inches='tight')
