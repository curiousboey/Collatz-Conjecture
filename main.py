import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

points = 100
start = 100
stop = 500

# randintegers = np.random.randint(start,stop,points)
randintegers = np.array(range(10,50))
Integers = np.size(randintegers)

fig = plt.figure(figsize=(10, 10))
ax1 = plt.subplot2grid((4, 2), (0, 0), colspan=1, rowspan=2)
ax2 = plt.subplot2grid((4, 2), (0, 1), colspan=1, rowspan=1)
ax3 = plt.subplot2grid((4, 2), (1, 1), colspan=1, rowspan=1)
ax4 = plt.subplot2grid((4, 2), (2, 1), colspan=1, rowspan=1)
ax5 = plt.subplot2grid((4, 2), (3, 1), colspan=1, rowspan=1)
ax6 = plt.subplot2grid((4, 2), (2, 0), colspan=1, rowspan=2)

ax_val_final = []
ax_len = []
y_max = []
for y in range(Integers):
    y_axis=[]
    val = randintegers[y]
    ax_val= val
    ax_val_final.append(ax_val)
    if val > 1:
        y_axis.append(val)
        cal1=val; cal2=val
        while cal1 > 1 and cal2 > 1:
            if val%2 == 0:
                cal1= val/2
                y_axis.append(cal1)
                val=cal1
            else:
                cal2= 3*val + 1
                y_axis.append(cal2)
                val= cal2
    else:
        pass
    x_axis = np.array(range(np.size(y_axis)))
    ax_len.append(len(x_axis)-1)
    y_max.append(max(y_axis))

    ax1.plot(x_axis, y_axis, color='red', linestyle='solid', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=5)
    ax2.vlines(x=ax_val, ymin=0, ymax=(len(x_axis)-1), colors='green', lw=2)
    ax3.vlines(x=ax_val, ymin=0, ymax=max(y_axis), colors='blue', lw=2)
    ax6.plot([ax_val, ax_val],[(len(x_axis)-1),max(y_axis)], color='green', linestyle='solid', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=5)

ax4.scatter(ax_val_final, ax_len, color='blue')
ax5.scatter(ax_val_final, y_max, color='red')
ax6.plot(ax_val_final,np.array(y_max)-np.array(ax_len), linestyle= 'dashed')
ax1.grid()
# ax1.set_xlabel('common xlabel')
ax2.grid()
ax3.grid()
plt.show()











