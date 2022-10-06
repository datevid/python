### Diferencia entre fechas:
```
import datetime
import pandas as pd

def getDiasOfFechas(fechaIni,fechaFin):
    """
    obtiene las fechas de cada día en un rango de fechas indicado como parámetro
    :param fechaIni: formato 2022-02-15
    :param fechaFin: formato 2022-03-02
    :return: ['2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18]
    """
    start = datetime.datetime.strptime(fechaIni, "%Y-%m-%d")
    end = datetime.datetime.strptime(fechaFin, "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    #print(date_generated.strftime("%d-%m-%Y"))
    diasList=[]
    for i in date_generated:
        diasList.append(i.strftime("%Y-%m-%d"))
    return diasList;


diasList=getDiasOfFechas("2022-02-15","2022-03-02")
print(diasList)
```

### Obtención de datetime año-hora-minuto-segundo
```
import datetime

def getDatetimeStr():
    # Converting datetime object to string
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%m-%d.%H.%M.%S")
    return timestampStr;
```
