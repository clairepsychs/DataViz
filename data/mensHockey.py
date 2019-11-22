import csv
import matplotlib.pyplot as plt

#pie chart for men's hockey medal colours (gold, silver, bronze)
#arrays for each colour

golds = []
silvers = []
bronzes = []

catagories = []

with open('mensHockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

	for row in reader:
		if line_count is 0:
			#parse that first row of text data out of the file
			catagories.append(row)
			line_count += 1 

	else: 
		if row[7] =="Gold":
			print("Won Gold!!")
			golds.append(row[7])

		elif row[7] == "Silver":
			print("Won Silver")
			silvers.append(row[7])

		if row[7] == "Bronze":
			print("Won Bronze. Is that even winning?")
			bronzes.append(row[7])

		line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silvers))
print("bronze medals: ", len(bronzes))

# plot pie chart

labels = ("Gold", "Silver", "Bronze")
# sizes are how many and how large the slices of the pie chart will be
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Gold Medals for Men's Hockey")
plt.xlabel("Medals since 1924")
plt.show()