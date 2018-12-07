import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
#url = up.urlparse(os.environ["postgres://czarbatm:A81rAFWJD2-ve8BYtNd-6uMGQMrV-iSE@elmer.db.elephantsql.com:5432/czarbatm"])
conn = psycopg2.connect(database="azcsmrbb",
                        user="azcsmrbb",
                        password="iAjNxyhiU0SpLAtmn6UoLU5-l-DHVQGm",
                        host="elmer.db.elephantsql.com",
                        port="5432"
                        )

cur = conn.cursor()

#cur.execute("Create table test(id integer primary key,name varchar(25))")
#cur.execute("INSERT INTO test(id,name) Values(13,'ravi');")
cur.execute('SELECT * FROM "public"."MDTouch_administrator" LIMIT 100')
#cur.execute("select * from test")
l = cur.fetchall()
print(l)
#conn.commit()
conn.close()