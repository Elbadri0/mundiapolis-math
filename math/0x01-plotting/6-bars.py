
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

fruit_names = ['apples', 'bananas', 'oranges', 'peaches']
person_names = ('Farrah', 'Fred', 'Felicia')
colors = ('red', 'yellow', '#ff8000', '#ffe5b4')
y_pos = np.arange(len(person_names))

y_offset = [0, 0, 0]

for row in range(len(fruit)):
    plt.bar(y_pos, fruit[row],
            0.5,
            bottom=y_offset,
            color=colors[row],
            label=fruit_names[row])
    y_offset = y_offset + fruit[row]

plt.xticks(y_pos, person_names)
plt.yticks(np.arange(0, 90, 10))
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()

plt.show()
