
### Restar fechas y retornar los días involucrados en formato YYYY-MM-DD:
```
import datetime
import pandas as pd

def restarFechasReturnDaysYYYYMMDD(fechaIni,fechaFin):
    """
    obtiene las fechas de cada día en un rango de fechas indicado como parámetro
    :param fechaIni: formato 2022-02-15
    :param fechaFin: formato 2022-03-02
    :return: retorna las fechas por día en un array
    ['2022-02-15', '2022-02-16', '2022-02-17', '2022-02-18]
    """
    start = datetime.datetime.strptime(fechaIni, "%Y-%m-%d")
    end = datetime.datetime.strptime(fechaFin, "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    #print(date_generated.strftime("%d-%m-%Y"))
    diasList=[]
    for i in date_generated:
        diasList.append(i.strftime("%Y-%m-%d"))
    return diasList;
```
### Restar fechas y retornar los años involucrados en formato YYYY:

```
import datetime
import pandas as pd

def restarFechasReturnYearsYY(fechaIni,fechaFin):
    """
    obtiene las fechas de cada día en un rango de fechas indicado como parámetro
    :param fechaIni: formato 2021-12-30
    :param fechaFin: formato 2022-01-02
    :return: retorna sólo los años años en un array
    [2021, 2022]
    Notice: years no repeat

    """
    start = datetime.datetime.strptime(fechaIni, "%Y-%m-%d")
    end = datetime.datetime.strptime(fechaFin, "%Y-%m-%d")
    date_generated = pd.date_range(start, end)

    anios=date_generated.year;

    #remove duplicates:
    anios = [*set(anios)]

    return anios


diasList=restarFechasReturnYearsYY("2021-12-30","2022-01-02")
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
### Obtención de datetime año-hora-minuto-segundo formato YYYYmmdd.hh.mm.ss
```
import datetime
def getDatetimeStrYYMMDD():
    """
    return datetime in string with format YYYYmmdd.hh.mm.ss
    :return:
    """
    # Converting datetime object to string
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y%m%d.%H.%M.%S")
    return timestampStr;
```
        
