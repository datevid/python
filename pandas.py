#recorrer sólo una columna de un dataframe con el encabezado 'name':
for row in df['name']:
    print(row)

#recorrer todos los items de un dataframe con el encabezado 'name':
for i, row in df.iterrows():
    print(row['name'])
