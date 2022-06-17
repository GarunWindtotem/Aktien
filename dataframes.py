import pandas as pd
# import openpyxl
# import datetime as dt

def dataframes(query_string, today, bezeichnung_aktie):
    # print(f'dataframes = {bezeichnung_aktie}')  # debug
    df = pd.read_csv(query_string)
    df['Kurs'] = (1/2) * ( df["Low"]+df["High"])
    length = len(df["Kurs"])
    #print(f'length = 5%={int(length*0.05)}, 25%={int(length*0.25)}')

    # rolling_window1 = int(length*0.10)
    # rolling_window2 = int(length*0.25)
    # rolling_window3 = int(length*0.50)

    # für michi
    rolling_window1 = 30
    rolling_window2 = 200
    rolling_window3 = 600

    df['Kurs_mean_1'] = df['Kurs'].rolling(window=rolling_window1, min_periods=1, center=True).mean()
    df['Kurs_mean_2'] = df['Kurs'].rolling(window=rolling_window2, min_periods=1, center=True).mean()
    df['Kurs_mean_3'] = df['Kurs'].rolling(window=rolling_window3, min_periods=1, center=True).mean()

    df['Kurs_std+'] = df['Kurs_mean_1'] + df['Kurs'].rolling(window=rolling_window1, min_periods=1, center=True).std()
    df['Kurs_std-'] = df['Kurs_mean_1'] - df['Kurs'].rolling(window=rolling_window1, min_periods=1, center=True).std()

    # df['Kurs_mean_1'] = df['Kurs'].rolling(window=rolling_window1, min_periods=rolling_window1, center=False).mean()
    # df['Kurs_mean_2'] = df['Kurs'].rolling(window=rolling_window2, min_periods=rolling_window2, center=False).mean()
    # df["Steigung"] = 1
    df = df.drop(columns=['Open', 'High', 'Low', 'Close', 'Adj Close'])
    df.loc[df['Kurs_mean_1'] <= 6.3, 'smaller_6_3'] = 'smaller'
    # df["Steigung"] = df["Kurs_mean_1"] - df["Kurs_mean_1"].shift(periods=2)
    df['Date'] = pd.to_datetime(df.Date, utc=True)
    df['Date'] = df['Date'].dt.tz_localize(None)
    
    # df.to_csv(f'D:\\Github\\Aktien\\Output\\Daten\{today} {bezeichnung_aktie}.csv')
    return df, rolling_window1, rolling_window2, rolling_window3

