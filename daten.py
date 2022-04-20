def daten():

    # Aktien Shortcuts
    dict_aktien = {
        '1': 'LHA.DE',
        '2': 'H4ZJ.DE',
        # '3': 'E127.MI',
        '4': 'BTC-EUR'}

    # Aktien Bezeichnung
    dict_bezeichnung_aktien = {
        'LHA.DE': 'Lufthansa',
        'H4ZJ.DE': 'HSBC MSCI World ETF',
        # 'E127.MI': 'Lyxor MSCI Emerging Markets ETF',
        'BTC-EUR': 'Bitcoin-EUR'}

    # Anzahl Aktien
    dict_n_aktien = {
        'LHA.DE': 148,
        'H4ZJ.DE': 137.195,     # HSBC MSCI World
        # 'E127.MI': 6.258,
        'BTC-EUR': 0}

    # Einstandspreis
    dict_EP_aktien = {
        'LHA.DE': 6.379,
        'H4ZJ.DE': 27.468,
        # 'E127.MI': 47.942,
        'BTC-EUR': 37_000}
    return dict_aktien, dict_bezeichnung_aktien, dict_n_aktien, dict_EP_aktien