#You are given the average monthly temperatures for four major cities in Pakistan: Islamabad, Lahore,
#Karachi, and Quetta. Your job is to calculate some basic statistics and create simple charts to show
#temperature trends.
#Use the following data for the temperatures (in Celsius) for each city:
#Islamabad: [7, 9, 15, 22, 28, 33, 31, 30, 27, 21, 15, 9]
#Lahore: [10, 12, 18, 26, 33, 37, 36, 35, 31, 25, 19, 12]
#Karachi: [18, 19, 22, 26, 29, 32, 31, 31, 29, 27, 23, 20]
#Quetta: [5, 7, 12, 18, 24, 28, 27, 26, 23, 17, 11, 6]
#• Create a NumPy array with this data, where each row is a city, and each column is a month
#(January to December).
#• Find the average temperature for each month across all cities (January to December).
#• Create a line plot for each city’s temperatures over the year.
#• Create a bar chart showing the average temperature for each month across all cities.

import numpy as np
import matplotlib.pyplot as plt

# Data for each city
temps = np.array([
    [7, 9, 15, 22, 28, 33, 31, 30, 27, 21, 15, 9],
    [10, 12, 18, 26, 33, 37, 36, 35, 31, 25, 19, 12],
    [18, 19, 22, 26, 29, 32, 31, 31, 29, 27, 23, 20],
    [5, 7, 12, 18, 24, 28, 27, 26, 23, 17, 11, 6]
])

cities = ["Islamabad", "Lahore", "Karachi", "Quetta"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#  the average temperature for each month across all cities
avg_temps = np.mean(temps, axis=0)

# Plot each city's temperature data
plt.figure(figsize=(10, 6))

for i, city in enumerate(cities):
    plt.plot(months, temps[i], label=city, marker='o')

plt.title('Monthly Temperatures for Each City (2024)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart for average monthly temperature across all cities
plt.figure(figsize=(10, 6))

plt.bar(months, avg_temps, color='skyblue')
plt.title('Average Monthly Temperature Across All Cities (2024)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
