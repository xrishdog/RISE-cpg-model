from imports import *

c = constants()

# kappa = 0.006
# t1 = np.array([101481, 113740, 123684, 120589, 124019, 124095, 122019, 121988, 121984, 123926, 123944])
# t2 = np.array([64674, 100779, 127328, 123572, 123687, 122619, 122643, 122647, 122639, 123485, 128260])

# kappa = 10.0, c = 0.005
# t1 = np.array([101481, 113599, 123771, 120781, 120837, 124180, 124216, 122191, 133423, 124447, 132608])
# t2 = np.array([64674, 100780, 127444, 123690, 123799, 122683, 122665, 122670, 122742, 122952, 133792])

# kappa = 10.0, c = 0.0001
t1 = np.array([101481, 113363, 123193, 112993, 121781, 110786, 113132, 120706, 113173, 121829, 110806, 113147])
t2 = np.array([64674, 100782, 127254, 112170, 111727, 123135, 117246, 124025, 112493, 111803, 123161, 117260])

# kappa = 0.0, c = 1.0
# t1 = np.array([56254, 30508, 63356, 119736, 129720, 125726, 131534])
# t2 = np.array([20147.0, 14841.0, 49712.0, 72168.0, 72992.0, 80355.0, 80866.0])

t1 = t1 * c.scale
t2 = t2 * c.scale

plt.figure()

plt.plot(t1-t2, linewidth=0.5, color="black")
plt.title("Difference in Bursting Times of Coupled HR Neurons")
plt.xlabel("burst number")
plt.ylabel("difference in ms")
plt.savefig("difference.png", dpi = 300)
plt.show()