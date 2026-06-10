import pandas as pd
student = {"name": ["Eva", "Polina", "Sanek"], "point": [194, 191, 185]}
df = pd.DataFrame(student)
print("Кількість набраних балів НМТ:")
print(df)
average_point = df["point"].mean()
print("Середнє значення:", average_point)
print("Це середній бал НМТ моїх студентів")