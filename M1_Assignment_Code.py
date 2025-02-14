import pandas as pd
import matplotlib.pyplot as plt


file_path = "megaGymDataset.csv"
df = pd.read_csv(file_path)

df = df.drop(columns='RatingDesc',)
df = df.drop(columns='Desc')

# print(df.head())

#BEGINNER

best_exercises_beginner = (df[(df['Type'] == 'Strength') & (df['Level'] == 'Beginner')]
                  .sort_values('Rating', ascending=False)
                  .groupby('BodyPart', as_index=False)
                  .first()
                  .sort_values('Rating', ascending=False))
# print(best_exercises_beginner)

# New column for better plot label
best_exercises_beginner['Exercise_Label'] = best_exercises_beginner['BodyPart'] + " - " + best_exercises_beginner['Title']

best_exercises_beginner = best_exercises_beginner.sort_values(by="Rating", ascending=False)

# Beginner Plot
# plt.figure(figsize=(12, 6))
# plt.barh(best_exercises_beginner['Exercise_Label'], best_exercises_beginner['Rating'], color='skyblue')
# plt.xlabel("Rating")
# plt.ylabel("Exercise")
# plt.title("Top-Rated Exercises for Each Muscle Group - Beginner")
# plt.gca().invert_yaxis()
# plt.show()

#INTERMEDIATE

best_exercises_intermediate = (df[(df['Type'] == 'Strength') & (df['Level'] == 'Intermediate')]
                  .sort_values('Rating', ascending=False)
                  .groupby('BodyPart', as_index=False)
                  .first()
                  .sort_values('Rating', ascending=False))
print(best_exercises_intermediate)

best_exercises_intermediate['Exercise_Label'] = best_exercises_intermediate['BodyPart'] + " - " + best_exercises_intermediate['Title']


best_exercises_intermediate = best_exercises_intermediate.sort_values(by="Rating", ascending=False)

# Plot
plt.figure(figsize=(12, 6))
plt.barh(best_exercises_intermediate['Exercise_Label'], best_exercises_intermediate['Rating'], color='skyblue')
plt.xlabel("Rating")
plt.ylabel("Exercise")
plt.title("Top-Rated Exercises for Each Muscle Group - Intermediate")
plt.gca().invert_yaxis()
plt.show()