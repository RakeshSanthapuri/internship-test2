import pandas as pd
url = "https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-2/main.csv"
df = pd.read_csv(url)
final = df.groupby('occupation')
final = final.agg({'age':['min','max']})
final.to_csv("C:\\Users\\santh\\AppData\\Local\\Programs\\Python\\Python37\\newfile1.csv",index=True)
