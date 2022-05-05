import matplotlib.pyplot as plt

a = [1,2,3,4,5]
b = [each**2 for each in a]

#plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(a,b, c=b, cmap=plt.cm.Reds, s=20)

ax.set_title("Multiple of 2")
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Multiplied by 2", fontsize = 14)

ax.tick_params(axis = 'both', labelsize = 14)


#set the range
ax.axis([0,6, 0, 30])

plt.show()