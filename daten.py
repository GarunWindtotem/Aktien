def daten():

    # Aktien Shortcuts
    dict_aktien = {
        '1': 'LHA.DE',      # Aktie Lufthansa
        '2': 'H4ZJ.DE',     # ETF HSBC MSCI World
        '3': 'TDIV.AS',     # ETF VanEck Morningstar Developed Markets Dividend
        '4': 'ISPA.DE',     # ETF iShares STOXX Global Select Dividend 100 UCITS
        '5': 'GLDV.L',      # ETF SPDR S&P Global Dividend Aristocrats UCITS
        '6': 'BTC-EUR',     # Rohstoff Bitcoin-EUR
       # '7': 'PAH3.F',
        # '8': '9201.T',
        # '9': 'IAG.L',
       # '10': 'RYA.IR',
        '11': 'E127.DE',

        # '7': 'CL=F'
        #'5': 'EURUSD=X',
       # '6': 'GC=F'
       }

    # Aktien Bezeichnung
    dict_bezeichnung_aktien = {
        'LHA.DE': 'Aktie Lufthansa',
        'H4ZJ.DE': 'ETF HSBC MSCI World',
        'E127.DE': 'ETF Lyxor MSCI Emerging Markets',
        'TDIV.AS': 'ETF VanEck Morningstar Developed Markets Dividend',
        'ISPA.DE': 'ETF iShares STOXX Global Select Dividend 100 UCITS',
        'GLDV.L': 'ETF SPDR S&P Global Dividend Aristocrats UCITS',
        'BTC-EUR': 'Bitcoin-EUR',
        #'PAH3.F': 'Aktie Porsche Holding',
        # '9201.T': 'Aktie Japan Cons. Airline',
        # 'IAG.L': 'Aktie Internation Cons. Airline',
       # 'RYA.IR': 'Aktie Ryanair Holding',
        
        # 'CL=F': 'crude oil'
      # 'EURUSD=X': 'EURO to USD',
      # 'GC=F': 'Gold'
        }
   
    dict_y_aktien = {
        'LHA.DE': 6.379,        # Aktie Lufthansa
        'H4ZJ.DE': 27.023,      # ETF HSBC MSCI World
        'TDIV.AS': 33.100,      # ETF VanEck Morningstar Developed Markets Dividend
        'ISPA.DE': 28.497,      # ETF iShares STOXX Global Select Dividend 100 UCITS
        'GLDV.L': 31.265,       # ETF SPDR S&P Global Dividend Aristocrats UCITS
        'BTC-EUR': 27041.9219,  # Rohstoff Bitcoin-EUR
       # 'PAH3.F': 97.460,
        # '9201.T': '',
        # 'IAG.L': '',
       # 'RYA.IR': 16.860,
        'E127.DE': 47.942,
        # 'CL=F': 'crude oil'
      # 'EURUSD=X': 'EURO to USD',
      # 'GC=F': 'Gold'
        }

    # Liste mit den Pfaden der Output Daten
    pfad_output= f'D:\\OneDrive\\Github Output\\Aktien\\'
    image_paths = [
        f'{pfad_output}Bitcoin-EUR.png', 
        f'{pfad_output}ETF HSBC MSCI World.png',
        f'{pfad_output}ETF Lyxor MSCI Emerging Markets.png',
        # 'D:\\Github\\Aktien\\Output\\crude oil.png',
        f'{pfad_output}ETF VanEck Morningstar Developed Markets Dividend.png',
        f'{pfad_output}ETF iShares STOXX Global Select Dividend 100 UCITS.png',
        f'{pfad_output}ETF SPDR S&P Global Dividend Aristocrats UCITS.png',
        f'{pfad_output}Aktie Lufthansa.png',
       # 'D:\\Github\\Aktien\\Output\\Aktie Ryanair Holding.png',
       # 'D:\\Github\\Aktien\\Output\\Aktie Porsche Holding.png',
        # 'D:\\Github\\Aktien\\Output\\Aktie Japan Cons. Airline.png',
        # 'D:\\Github\\Aktien\\Output\\Aktie Internation Cons. Airline.png',
        ]
     


    return dict_aktien, dict_bezeichnung_aktien, image_paths, dict_y_aktien, pfad_output