file = open("/home/students/jimenezls/git_repos/luke-jimenez.github.io/projects/weather-data.txt")
years = []
temps = []
for line in file:
    year, temp = line.split()
    index = 0
    years.append(year)
    temps.append(temp)
    index += 1
file.close()

for i in range(0, len(years)):
    years[i] = float(years[i]) - 1900

    
x_sum = 0
for i in range(0, len(years)):
    x_sum += float(years[i])

y_sum = 0
for i in range(0, len(temps)):
    y_sum += float(temps[i])

x_bar = x_sum/ len(years)
y_bar = y_sum/ len(temps)

top_slope = 0
for i in range(0, len(temps)):
    top_slope += (float(temps[i]) - y_bar)*(float(years[i]) - x_bar)

bottom_slope = 0
for i in range(0, len(years)):
    bottom_slope += (float(years[i]) - x_bar)**2

slope = top_slope/bottom_slope
intercept = y_bar - slope*x_bar

print("Computing the best fitting line for the weather dataset.\nm = %.6f" % round(slope, 6) + "\nc = %.6f" % round(intercept, 6))

