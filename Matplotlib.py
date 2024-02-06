# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:17:49 2023

@author: de
"""

                             #MATPLOTLIB#
#Used to generate graphs                             
#Do not execute the code line by line
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show() 

#______________________________________________________________________________

#Multiline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x, [xi*1.5 for xi in x])
plt.plot(x, [xi*3.0 for xi in x])
plt.plot(x, [xi/3.0 for xi in x])
plt.show()

#______________________________________________________________________________

'''
NOTE:Matplotlib automatically chooses colours for each line-green for the first
line ,blue for the second line and red for the third line(from top to bottom)
'''
#Grid ,axes,and labels
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()

#______________________________________________________________________________

#Handling axes
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5,x,x*3.0,x,x/3.0)

plt.axis()            #Shows the current axis limits values

plt.axis([0,5,-1,13])  #Set new axes limits
#[xmin,xmax,ymin,ymax]
#[0,5,-1,13]
plt.show()

#______________________________________________________________________________

#Adding labels
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.xlabel('This is the Xaxis')
plt.ylabel('This is the Yaxis')
plt.show()

#______________________________________________________________________________

#Adding a title
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.title('Simple plot')
plt.show()

#______________________________________________________________________________

#Adding a legend
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*3.0,label='Fast')

plt.plot(x,x*3.0,label='Slow')
plt.legend()
plt.show()

#______________________________________________________________________________

'''
Color abbreviation
Color Name
b- blue
c- cyon
g- green
k- black
m- magenta
r- red
w- white
y- yellow
'''
#Control colors
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y, 'y');
plt.plot(y+1,'m');
plt.plot(y+2, 'c');
plt.show()

#______________________________________________________________________________

#Control lines style
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y, '--',y+1,'-,',y+2,':')
plt.show()

#______________________________________________________________________________

'''
Style abbreviation Style
solid line 
dashed line
dashed-dot line
dotted line
'''
#______________________________________________________________________________

'''
Marker abbreviation Marker styles

'''
#______________________________________________________________________________

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s');
plt.show()

#______________________________________________________________________________

#Histogram charts
import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y);  #Should be remembered
plt.show()

#______________________________________________________________________________

#BARplot
#Imp to understand trend of data
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()

'''
BAR fun is used to generate charts in Matplotlib
'''
#______________________________________________________________________________

#Scatter plots
#Imp in regression (to check linearity,polarity)
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

#_____________________________________________________________________________

#To change size
size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y, s=size, c=colors);
plt.show()

#______________________________________________________________________________

#To add text inside graph
#For Adding text some packages are imp
import matplotlib.pyplot as plt
import numpy as np
X=np.linspace(-4,4,1024)
Y=.25*(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25,'Brackmard minimun')
plt.plot(X,Y,c='k')
plt.show()

#____________________________________________________________________________

#SEABORN
#pip install seaborn

import seaborn as sns 
import pandas
import matplotlib.pyplot as plt

#SEABORN has 18 in-built datasets that can be found using foll commands

sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

#______________________________________________________________________________

#COUNT plot
'''
Used to plot frequency of different categories
'''
#to display how many male and female were ther in titanic
sns.countplot(x='sex',data=df)
#x= The name of the column
#data=The dataframe
#hue is the name of categorical column
#Here palette is used for set of colors
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

#______________________________________________________________________________

#KDE PLOT   (Kernel Density Estimate)
#Exact measurement of data
#To plot the data distribution of continuous data
#bins:The no of bars


sns.kdeplot(x='age',data=df,color='black')

#_____________________________________________________________________________

#DISTRIBUTION PLOT 
#More helpful than histogram bcoz it is alongwith KDE Plot
sns.displot(x='age',kde=True,bins=6,data=df)
sns.displot(x='age',kde=True,bins=5,
hue=df['survived'],palette='Set1',data=df)

#Here also we can plot Scatter plot
#First we will need to load the iris dataset.
df=sns.load_dataset('iris')
df.head()

#______________________________________________________________________________
#Joint Plot
#It is also used to plot the corelation of the data
sns.jointplot(x='sepal_length',y='petal_length',
              data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',
              data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',
              data=df,kind='kde')

#_____________________________________________________________________________

#PAIR Plot
sns.pairplot(df)

#_____________________________________________________________________________

#HEAT MAP
#It is used to visualize confusion,matrices and corelation
corr=df.corr()
sns.heatmap(corr)



























