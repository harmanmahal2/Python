import matplotlib.pyplot as plt
plt.style.available

input_values = [1,5,10,15,20,25,30]
squares = [each**2 for each in input_values]


plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(input_values,squares,c='blue',linewidth=3)

#set chart title and label axes

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=14)


plt.show()