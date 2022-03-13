from matplotlib import pyplot as plt

def diagramme(df, rolling_window1, rolling_window2, aktie, interval, today, Einstandswert, aktueller_Wert, bezeichnung_aktie):
   
    plt.figure(figsize=(24,9))
    plt.style.use('seaborn')
    plt.grid(True)

    # Kurzzeittrend
    plt.plot(df["Date"], df["Kurs_mean_1"], marker='', linestyle='-', alpha = 0.7,
        color="blue", linewidth=5, label = f'Kurzzeittrend ({rolling_window1} Tage)', markersize=10)

    # Langzeittrend
    plt.plot(df["Date"], df["Kurs_mean_2"], marker='', linestyle='-', alpha = 0.7,
        color="black", linewidth=7, label = f'Langzeittrend ({rolling_window2} Tage)', markersize=10)

    plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='green', alpha=0.7,
        label=f'positiver Kurzzeittrend', interpolate=True,  where=(df["Kurs_mean_1"] > df["Kurs_mean_2"]))

    plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='red', alpha=1,
        label=f'negativer Kurzzeittrend', interpolate=True, where=(df["Kurs_mean_1"] < df["Kurs_mean_2"]))

    plt.plot(df["Date"], df["Einstandspreis"], marker='', linestyle='-', alpha = 0.7,
        color="grey", linewidth=1.5, label = f'Einstandspreis', markersize=10)

    plt.plot(df["Date"], df["Kurs"], marker='.', linestyle='-', alpha=0.4,
        color="black", linewidth=3, label = "Tageskurs", markersize=15)

    plt.legend(loc='upper center',
        bbox_to_anchor=(0.5, -0.2),
        fancybox=True,
        shadow=True,
        ncol=3,
        fontsize=20)

    # plt.title(f'Kurswert: {bezeichnung_aktie}, ({interval})\n', fontsize=25)
    plt.title(f'{bezeichnung_aktie} \n', fontsize=25)
    plt.suptitle(f'{today}, Einstandswert = {Einstandswert} €, aktueller Wert = {aktueller_Wert} €', fontsize=20, y=0.92)

    plt.xticks(fontsize=15, rotation=0)
    plt.yticks(fontsize=15)

    plt.ylabel("Euro", fontsize=25)
    plt.xlabel("Zeit", fontsize=25)

    plt.savefig(f'D:\\Github\\Aktien\\Output\\{today} {bezeichnung_aktie}.png', dpi=300, bbox_inches='tight')
    return