from die import Die
import pygal
import matplotlib.pyplot as plt
# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()
# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()+die_3.roll()
    results.append(result)
    plt.scatter(roll_num, result)
print(results)
# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
hist = pygal.Bar()
hist.title = "Results of rolling a 3-x D6 50,000 times."
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16','17','18']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
plt.show()




