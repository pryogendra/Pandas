import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
values=np.random.randn(100)
s=pd.Series(values)
s.plot(kind='hist',title="Normaly Distributed Random Values") 
plt.show()
s.describe()