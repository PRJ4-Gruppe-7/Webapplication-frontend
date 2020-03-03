import random

file = open("GeneratedjsonData.txt", "w+");

file.write('[')

for i in range(10):
    for j in range(10):
        file.write("""
        {
        "x": """ + str(i) + """,
        "y": """ + str(j) + """,
        "value": """ + str(random.random()) + """
        },
        """)

file.write(']')
