import pandas as pd

data = {
    'name': ['John', 'Jane', 'Bob', 'Alice'],
    'usia': [25, 20, 17, 18],
    'pekerjaan': ['Engineer', 'Teacher', 'Desginer', 'Doctor']
  }  

df = pd.DataFrame(data)
print(df)