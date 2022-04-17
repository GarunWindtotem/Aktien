import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("Sankey.xlsx",
    engine = 'openpyxl')

# Listen erzeugen aus Excel

list_label = list(df.Unterkategorie)
cleaned_label = [x for x in list_label if str(x) != 'nan'] 
 
list_x = list(df.x)
cleaned_x = [x for x in list_x if str(x) != 'nan']

list_y = list(df.y)
cleaned_y = [x for x in list_y if str(x) != 'nan']

list_Source = list(df.Source)
cleaned_Source = [x for x in list_Source if str(x) != 'nan']
print(cleaned_Source)

list_Target = list(df.Target)
cleaned_Target = [x for x in list_Target if str(x) != 'nan']

list_value = list(df.value)
cleaned_value = [x for x in list_value if str(x) != 'nan']


fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node = {
        "label": cleaned_label,
        "x": cleaned_x,
        "y": cleaned_y,
        'pad':10},  # 1 Pixels Abstand
    link = {
        "source": list_Source,
        "target": list_Target,
        "value": list_value
        }))

fig.show()

