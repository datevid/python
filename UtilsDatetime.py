import datetime
import pandas as pd


class UtilsDatetime():

    def getDatetimeStr(self):
        """
        return datetime in string with format YYYY-mm-dd.hh.mm.ss
        :return:
        """
        # Converting datetime object to string
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%Y-%m-%d.%H.%M.%S")
        return timestampStr;

    def restarFechasReturnDaysYYYYMMDD(self, fechaIni, fechaFin):
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
        # print(date_generated.strftime("%d-%m-%Y"))
        diasList = []
        for i in date_generated:
            diasList.append(i.strftime("%Y-%m-%d"))
        return diasList;

    def restarFechasReturnYearsYY(self, fechaIni, fechaFin):
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

        anios = date_generated.year;

        # remove duplicates:
        anios = [*set(anios)]

        return anios


if __name__ == "__main__":
    utils = UtilsDatetime()
    diasList = utils.restarFechasReturnYearsYY("2021-12-30", "2022-01-02")
    print(diasList)
