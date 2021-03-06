
# CNA330 12/2/2020
# This script is to migrate the resulting of the database(googleplaystore) from this project into a cloud(I used AWS).

import pandas as pd
from sqlalchemy import create_engine


hostname = "18.217.178.166"
uname = "pythoneverything"
pwd = "python123"
dbname = "googleplaystore"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_csv(r'C:\Users\Luma\PycharmProjects\GroupProject\googleplaystore.csv', index_col='App', nrows=1000)

connection = engine.connect()

df.to_sql('googleplaystore', con=engine, if_exists='append')


engine.execute('CREATE TABLE googleplaystore_temp Like googleplaystore')
engine.execute('INSERT INTO googleplaystore_temp SELECT DISTINCT App, Category,Rating, Reviews,  Size,Installs, Type, Price, ContentRating, Genres, LastUpdated, CurrentVer, AndroidVer FROM googleplaystore ')
engine.execute('DROP TABLE googleplaystore')
engine.execute('ALTER TABLE googleplaystore_temp RENAME TO googleplaystore')

connection.close()














