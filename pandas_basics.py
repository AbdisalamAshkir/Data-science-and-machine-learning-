import pandas as pd


data={
    'name':['Ahmed',"Ali","Ashkir"],
    'age':[30,25,40]
}


df=pd.DataFrame(data)



print(df)

#average
print("Average age:", df["age"].mean())