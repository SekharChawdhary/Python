import pandas as pd
mydatasets={
    'Name':["Kiran", "Anil", "Sekhar"],
    'Age':[27, 30, 25],
    'College':['A', 'B', 'C']
}
myvar=pd.DataFrame(mydatasets)
print(myvar)