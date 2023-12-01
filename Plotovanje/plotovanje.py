import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', sep=',')
a = df.iloc[:, 0].to_numpy()
b = df.iloc[:, 1].to_numpy()
c = df.iloc[:, 2].to_numpy()


plt.figure()
plt.subplot(211)

plt.ylabel('[a]')
plt.plot(c, a)
plt.subplot(212)
plt.xlabel('[c]')
plt.plot(c, b, color='red')
plt.ylabel('[b]')


plt.show()
