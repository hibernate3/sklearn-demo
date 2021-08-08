import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl


if __name__ == '__main__':
    starbucks = pd.read_csv('starbucks_directory.csv')
    count = starbucks.groupby(['Country']).count()

    count['Brand'].plot(kind='bar', figsize=(20, 8))
    plt.show()

    print(starbucks.groupby(['Country', 'State/Province']).count())
    pass


