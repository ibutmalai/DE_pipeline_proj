from connector import Connector
from loader import Loader
from transfrormer import Transformer
import json
from pandas import DataFrame 

#importam fisierul de configurare
config_file = open('./connection/config_file.json')
data = json.load(config_file)

#cream conexiunea cu baza de date
connection = Connector(driver=data['driver'], server=data['server'], database=data['database'])
#cream cursorul pentru a-l executa ulterior
cursor = connection.createCursor()
print('cursor created')
cursor.execute('''select count(*) as nums, gender
                from AdventureWorks2022.HumanResources.Employee
                group by gender''')

#citim totul din cursor
data = cursor.fetchall()

columns = []
for col in cursor.description:
    columns.append(col[0])

#transmitem datele fetched de cursor catre Transformer
df = Transformer(data=data)
#La moment Transformer nu are careva methods de transformare
df.data.columns = columns
#trimitem datele care ar trebui sa fie transformate catre Loader
#iar acesta ulterior le va  
loader_obj = Loader(data=df.data)

print(loader_obj.data)
loader_obj.save_csv('./connection/file.csv')

