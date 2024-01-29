import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values_bar = [10, 20, 30, 40]
values_line = [15, 25, 35, 45]
colors=['#276BFF','#EC3A7B','#FFBC42','#1DB52C']
# Create a bar chart
plt.bar(categories, values_bar, color=colors)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Colorized Bar Chart')
plt.show()