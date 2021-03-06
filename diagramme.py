from matplotlib import pyplot as plt

def diagramme(df, rolling_window0, rolling_window1, rolling_window2, rolling_window3, today, bezeichnung_aktie, bool_WochenTrend, bool_KurzzeitTrend, bool_MittelTrend, bool_LangzeitTrend):
   
    # print(f'diagramme() bezeichnung_aktie= {bezeichnung_aktie}')
    plt.figure(figsize=(24,9))
    plt.style.use('seaborn')
    plt.grid(True)

    # Wochentrend
    if bool_WochenTrend == True:
        plt.plot(df["Date"], df["Kurs_mean_0"], marker='', linestyle='-', alpha = 1,
            color="grey", linewidth=3, label = f'weekly trend ({rolling_window0} days)', markersize=10)

    # Kurzzeittrend
    if bool_KurzzeitTrend == True:
        plt.plot(df["Date"], df["Kurs_mean_1"], marker='', linestyle='-', alpha = 1,
            color="blue", linewidth=3, label = f'monthly trend ({rolling_window1} days)', markersize=10)

    # mittlerer Trend
    if bool_MittelTrend == True:
        plt.plot(df["Date"], df["Kurs_mean_2"], marker='', linestyle='-', alpha = 1,
            color="orange", linewidth=4, label = f'mid time trend ({rolling_window2} days)', markersize=10)
    
    # Langzeit Trend
    if bool_LangzeitTrend == True:
        plt.plot(df["Date"], df["Kurs_mean_3"], marker='', linestyle='-', alpha = 1,
            color="black", linewidth=5, label = f'long time trend ({rolling_window3} days)', markersize=10)

    # # std+
    # plt.plot(df["Date"], df["Kurs_std+"], marker='', linestyle='--', alpha = 0.3,
    #     color="black", linewidth=1, label = f'±1 sigma ({rolling_window1} Tage)', markersize=10)
    # # std+
    # plt.plot(df["Date"], df["Kurs_std-"], marker='', linestyle='--', alpha = 0.3,
    #     color="blue", linewidth=1, markersize=10)

    # FILL BETWEEN std
    plt.fill_between(df["Date"], df["Kurs_std-"], df["Kurs_std+"], color='grey', alpha=0.2,
        label=f'±1 sigma {rolling_window1}', interpolate=True)

    # FILL BETWEEN rot/grün
    # plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='green', alpha=0.3,
    #     label=f'positiver Kurzzeittrend', interpolate=True,  where=(df["Kurs_mean_1"] > df["Kurs_mean_2"]))

    # plt.fill_between(df["Date"], df["Kurs_mean_1"], df["Kurs_mean_2"], color='red', alpha=0.3,
    #     label=f'negativer Kurzzeittrend', interpolate=True, where=(df["Kurs_mean_1"] < df["Kurs_mean_2"]))

    plt.plot(df["Date"], df["Kurs"], marker='.', linestyle='', alpha=0.2,
        color="black", linewidth=3, label = "daily value", markersize=15)

    plt.legend(loc='upper center',
        bbox_to_anchor=(0.5, -0.2),
        fancybox=True,
        shadow=True,
        ncol=3,
        fontsize=25)

    plt.title(f'{bezeichnung_aktie}\n', fontsize=40)
    plt.suptitle(f'{today} PW', fontsize=25, y=0.92)

    plt.xticks(fontsize=25, rotation=0)
    plt.yticks(fontsize=25)

    plt.ylabel("Euro", fontsize=35)
    plt.xlabel("Zeit", fontsize=35)

    plt.savefig(f'D:\\Github\\Aktien\\Output\\{bezeichnung_aktie}.png', dpi=300, bbox_inches='tight')
    return