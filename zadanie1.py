import matplotlib.pyplot as plt 
plt.plot([1,5], [1,1], color='g', marker='.', ms=10)
plt.plot([1,1], [1,5], color='g', marker='.', ms=10)
plt.plot([5,5], [5,1], color='g', marker='.', ms=10)
plt.plot([1,5], [5,5], color='g', marker='.', ms=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('square')
plt.show()

plt.plot([1,], [1,1], color='g', marker='.', ms=10)
