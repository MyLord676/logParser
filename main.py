import yaml
from datetime import datetime
from re import sub

from MyMockInterface.tomcatReader import gzReader
from MyLibs.logParser import logParser
from DataBase.mysqllib import mysqllib
from domain.dataBase import MyWarning


def main():

    with open("Configs/Config.yaml", "r") as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    myBase = mysqllib(cfg['host'],
                      cfg['port'],
                      cfg['user'],
                      cfg['password'],
                      cfg['database'])

    insert = 0
    notInsert = 0
    for arr, all in logParser.Parse(gzReader("tomcat.log.gz"),
                                    cfg['markers'], cfg['re']):
        print(arr, all)
        if all:
            war = MyWarning()
            war.date_time = datetime.strptime(arr[0], "%d-%b-%Y %H:%M:%S.%f")
            war.port = arr[1]
            war.answer_time = sub("ms", "", arr[2], 1)
            myBase.insertLog(war)
            insert += 1
        else:
            notInsert += 1

    print("insert: ", insert)
    print("notInsert: ", notInsert)


if __name__ == '__main__':
    main()
