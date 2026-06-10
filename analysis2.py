import pandas as pd
student = {"name": ["Eva", "Polina", "Sanek"], "point": [194, 191, 185]}
df = pd.DataFrame(student)
print("Кількість набраних балів НМТ (тимчасова версія):")
print(df)
print("Середнє значення:", df["point"].mean())
