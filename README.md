# PieStats
piestats is a bare bones library that samples from a multivariate normal distribution. 

## usage
```python
from Random import Multivariate_Normal
import matplotlib.pyplot as plt
plt.style.use("ggplot")

cov = np.array([[1, 3], [2, 1]])

x1, x2 = Multivariate_Normal(size=10000, cov=cov)
plt.hist2d(x1, x2, bins=50, cmap='Blues')  # https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
cb = plt.colorbar()
cb.set_label('counts in bin')
```

## why do things the easy way when you can do things the hard way?
computers don't know anything about gaussian distributions. they only know uniform distributions, which can be generated from psuedo random numbers. so how do libraries like [numpy.random.multivariate_normal](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.multivariate_normal.html) emit samples from multivariate distributions?

## how dey do dat
first, piestats draws from a uniform distribution. this is a primitive operation that all computers know how to perform. then, it converts these samples into a 1d normal distribution through box muller transformation. finally, it reshapes these normally distribution samples by the specified covariance. 