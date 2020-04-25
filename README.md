# PieStats
a simple implementation of multivariate distribution using nothing more an uniform distribution primitive.

## an example
```python
import matplotlib.pyplot as plt
plt.style.use("ggplot")

x1, x2 = Multivariate_Normal()
plt.hist2d(x1, x2, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
```

## why do things the easy way when you can do things the hard way?
computers don't know what a gaussian distribution looks like. the only thing they know is a uniform distribution, which relies on psuedo random numbers and nothing else. so how do libraries like (numpy.random.multivariate_normal)[https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.multivariate_normal.html] draw from multivariate distributions?

## how dey do dat
piestats is a bare bones library that simulates a multivariate normal distribution. 

first, it draws floats from a uniform distribution between 0 and 1. all computers know how to do this so we start from here.

then, we convert samples drawn from a uniform distribution into a 1d normal distribution through a box muller transformation. 

finally, we reshape samples by its covariance matrix. in this setting, the covariance matrix can be interpreted as a transformation matrix that reshapes samples. 