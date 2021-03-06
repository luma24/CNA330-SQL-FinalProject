import pandas as pd
from matplotlib import pyplot as plt
from sqlalchemy import create_engine


hostname = "18.217.178.166"
uname = "pythoneverything"
pwd = "python123"
dbname = "googleplaystore"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))


df = pd.read_sql('googleplaystore',engine)
connection = engine.connect()

# Ploting
# Luma's part
# Plots the quantity of Apps that have Free Type with their Rating level.
# ( We can see here that this Database have 3667 FREE Apps and have a rate between 4.2 and 4.6)
plt.title("Free Apps")
df[df["Type"] == "Free"]["Rating"].plot(kind='hist')
plt.ylabel("Quantity")
plt.xlabel("Rating")
plt.show()


# Hasan's part
# Plots the quantity of Apps that have Paid Type with their Rating level.
# ( We can see here that this Database have 245 PAID Apps and have a highest rate between 4.2 and 4.6)

plt.title("Paid Apps")
df[df["Type"] == "Paid"]["Rating"].plot(kind="hist")
plt.ylabel(" Quantity")
plt.xlabel("Rating")
plt.show()

# Pie Plot of Apps by Type
plt.title('Free and Paid Apps')
df.Type.value_counts().plot(kind="pie")
plt.xlabel("Type")
plt.show()

# Luma's part
# Find the number of Rate for a specific category(BUSINESS)
# (We can see that the database has 96 apps with a highest rate for business category is between 4.2nd 4.6)
plt.title("Number of apps under the BUSINESS Category")
df[df["Category"] == "BUSINESS"]['Rating'].plot(kind="hist")
plt.ylabel("Quantity")
plt.xlabel("Rating")
plt.show()





# Mohamad's part
# Bar Plot of quantity of apps for each Category (we can see the FAMILY Category has the most numbers of apps)
plt.title('Number of Apps For Each Category')
df.Category.value_counts().plot(kind="bar")
plt.xlabel("Category")
plt.show()


# Plot the Category type with the level of Reviews for only 1000 rows.

df = pd.read_csv(r'C:\Users\Luma\PycharmProjects\GroupProject\googleplaystore.csv',index_col='App',  nrows=1000)
plt.title('Category')
plt.plot(df['Category'], df['Reviews'])
plt.xlabel('Category')
plt.ylabel('Reviews')
plt.xticks(rotation=90)
plt.show()

connection.close()





