from MyMockInterface.tomcatReader import gzReader
from MyLibs.logParser import logParser
from domain.patternLog import patternLog
import yaml


def main():

    with open("Configs/Config.yaml", "r") as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    i = 0
    for arr, all in logParser.Parse(gzReader("tomcat.log.gz"), 
                                    patternLog(cfg['markers'], cfg['re'])):
        print(arr, all)
        i += 1

    print(i)


if __name__ == '__main__':
    main()
