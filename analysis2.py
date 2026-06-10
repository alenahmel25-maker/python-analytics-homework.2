import pandas as pd
student = {"name": ["Eva", "Polina", "Sanek"], "point": [194, 191, 180]}
df = pd.DataFrame(student)
print("Кількість набраних балів НМТ:")
print(df)
print("Середнє значення:", df["point"].mean())
