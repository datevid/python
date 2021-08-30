#recorrer sólo una columna de un dataframe con el encabezado 'name':
for row in df['name']:
    print(row)

#recorrer todos los items de un dataframe con el encabezado 'name':
for i, row in df.iterrows():
    print(row['name'])

# group by filtro_estado
df = df.reset_index().groupby(
    ['dependencia_destino', 'cemp_nu_dni', 'cemp_codemp', 'empleado_destino', 'filtro_estado']
)['cantidad_por_estado'].aggregate('first').unstack()

# reset hierarchical index pandas
df = df.reset_index()

# replace null or empty with the number zero
df['RECIBIDO'].fillna(0, inplace=True)
df['PENDIENTE'].fillna(0, inplace=True)

# Change the Data Type of Columns
df[['RECIBIDO', 'PENDIENTE']] = df[['RECIBIDO', 'PENDIENTE']].apply(pd.to_numeric)

# create a new column type int
# https://www.geeksforgeeks.org/create-a-new-column-in-pandas-dataframe-based-on-the-existing-columns/
df['Total general'] = df['RECIBIDO'].astype(int) + df['PENDIENTE'].astype(int)

# eliminamos la columna cemp_codemp del reporte
df = df.drop(columns=['cemp_codemp'])

# convertir a lista una columna de un dataframe con el encabezado 'name':
nameList = df['name'].tolist()
