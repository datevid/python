### Pandas, library of Python:
install:
```
pip install pandas
```

importar:
```
import pandas as pd
```

abrir un archivo:
```
df = pd.read_excel('E:\\descargas\\ab1.xlsx', sheet_name='Hoja1', dtype=str)
print(df)
```
### recorrer dataframe mediante bucles:
recorrer sólo una columna de un dataframe con el encabezado 'name':
```
for row in df['name']:
    print(row)
```

recorrer todos los items de un dataframe con el encabezado 'name':
```
for i, row in df.iterrows():
    print(row['name'])
```
### Agrupaciones:
group by filtro_estado:
```
df = df.reset_index().groupby(
    ['dependencia_destino', 'cemp_nu_dni', 'cemp_codemp', 'empleado_destino', 'filtro_estado']
)['cantidad_por_estado'].aggregate('first').unstack()
```

reset hierarchical index pandas
```
df = df.reset_index()
```

replace null or empty with the number zero:
```
df['RECIBIDO'].fillna(0, inplace=True)
df['PENDIENTE'].fillna(0, inplace=True)
```

agrupar por algun campo y sumar las columnas no agrupadas:
df = df.groupby(['dependencia_destino']).agg('sum')

### Adicionar una columna al Dataframe
```
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
```

### check value in Dataframe:
```
# check 'Ankit' exist in dataframe or not
if 'Ankit' in df.values :
    print("\nThis value exists in Dataframe")
 
else :
    print("\nThis value does not exists in Dataframe")
``` 

### check value in especific column of Dataframe:
```
# check 'Ankit' exist in dataframe or not
if 'Ankit' in df['columZ'].values :
    print("\nThis value exists in Dataframe")
 
else :
    print("\nThis value does not exists in Dataframe")
```

### Change the Data Type of Columns
Changet datatype to numeric:
```
df[['RECIBIDO', 'PENDIENTE']] = df[['RECIBIDO', 'PENDIENTE']].apply(pd.to_numeric)
```

Create a new column type int:

```
df['Total general'] = df['RECIBIDO'].astype(int) + df['PENDIENTE'].astype(int)
```
more in this [blog](https://www.geeksforgeeks.org/create-a-new-column-in-pandas-dataframe-based-on-the-existing-columns/)

### Add colum type object:
```
import pandas as pd
#creacion de dataframe
df = pd.DataFrame(data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
print(df)
"""
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
"""


#adicionando una nueva columna que permita almacenar objetos de cualquier tipo
df['id_archivo']=''
df['id_archivo'].astype('object')

#adicionando datos a la nueva columna de tipo object
lista1 = ['row1','row2']
#df.loc[0][3]=lista1
df['id_archivo']=[1,[1,2],3]
print(df)
"""
   A  B  C id_archivo
0  1  4  7          1
1  2  5  8     [1, 2]
2  3  6  9          3
"""
```

### remove a column
eliminamos la columna cemp_codemp del reporte
```
df = df.drop(columns=['cemp_codemp'])
```


### convertir a lista
convertir a lista una columna de un dataframe con el encabezado 'name':
```
nameList = df['name'].tolist()
```

### reemplazar valores
Replace NaN Values with Zeros in Pandas DataFrame:
```
df['DataFrame Column'] = df['DataFrame Column'].fillna(0)
```

### save to file
save file to excel:
```
df.to_excel("example"+getDatetimeStr()+".xlsx",merge_cells=False, index=False)
```

### Get values consolidados
get total rows from dataframe
```
num_rows = df.shape[0]
```

### Get Dias transcurridos desde una fecha determinada
```
today = datetime.now()

df = pd.read_csv('/home/doctor/dbresult/DocsPendientesYRecibidos_202210241240_1.csv')

#adicionando a la columna 'fe_emi_with_format' con formato datetime
df['fe_emi_with_format']=pd.to_datetime(df['fe_emi'],format="%Y-%m-%d %H:%M:%S.%f")

#restamos y el resultado lo adicionamos a la columna dias_transcurridos
df["dias_transcurridos"]=(today-df['fe_emi_with_format']).dt.days
print(df)
```
