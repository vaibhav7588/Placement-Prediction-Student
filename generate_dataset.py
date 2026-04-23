import pandas as pd
import random

data = []

for i in range(10000):
    cgpa = round(random.uniform(5.0, 9.8), 2)
    ssc = random.randint(50, 95)
    hsc = random.randint(50, 95)
    internships = random.randint(0, 3)
    projects = random.randint(0, 5)
    aptitude = random.randint(40, 100)
    communication = random.randint(1, 10)
    training = random.randint(0, 1)

    # 🎯 Smart logic (important for accuracy)
    score = (
        cgpa * 10 +
        aptitude +
        communication * 5 +
        internships * 10 +
        projects * 5 +
        training * 10
    )

    # Placement decision
    placed = 1 if score > 180 else 0

    data.append([
        cgpa, ssc, hsc, internships,
        projects, aptitude, communication,
        training, placed
    ])

columns = [
    'cgpa','ssc','hsc','internships',
    'projects','aptitude','communication',
    'training','placed'
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("placement.csv", index=False)

print("✅ placement.csv with 10,000 records created!")