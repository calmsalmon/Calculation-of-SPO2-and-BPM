import pandas as pd

df = pd.read_xml('export.xml')

df.to_csv('test.csv', index=False)