import pandas as pd
url = "https://raw.githubusercontent.com/RakeshSanthapuri/internship-test2/master/input/question-3/main.csv"
df = pd.read_csv(url)
df = df[["Team","Yellow Cards","Red Cards"]]
result = df.sort_values(by = ["Yellow Cards"],ascending=False)
result = df.sort_values(by = ["Red Cards"],ascending=False)
result.to_csv("C:\\Users\\santh\\AppData\\Local\\Programs\\Python\\Python37\\main.csv",index=True)
