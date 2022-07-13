#abrir archivo 
import pandas as pd
import datetime

def getDatetimeStr():
    # Converting datetime object to string
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%m-%d.%H.%M.%S")
    return timestampStr;


df = pd.read_excel('E:\\descargas\\sinsaltolinea.xlsx', sheet_name='Hoja1', dtype=str)
#print(df)

#recorrer sólo una columna de un dataframe con el encabezado 'name':
rownew=[];
for row in df['Columna1']:
    print(row)
    new_string = row.replace(';', "\n")
    new_string=new_string.strip();
    rownew.append(new_string)

print(rownew)

df['newcolum']=rownew
print(df)
df.to_excel("example"+getDatetimeStr()+".xlsx",merge_cells=False, index=False)
