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

# Get values consolidados
get total rows from dataframe
```
num_rows = df.shape[0]
```

