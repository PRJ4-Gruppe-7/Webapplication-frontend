import random

file = open("GeneratedjsonData.txt", "w+");

file.write('[')

for i in range(100):
    for j in range(100):
        file.write("""
        {
        "x": """ + str(i) + """,
        "y": """ + str(j) + """,
        "value": """ + str(random.random()) + """
        },
        """)

file.write(']')
