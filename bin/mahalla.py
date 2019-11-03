import bin.core as core
from bin import ClassesLib
from bin.Consts import *


def start():
    core.login()

    mahalla_poeples = open(TEENAGERS_FILE_PATH, mode="r", encoding="utf-8")
    try:
        for line in mahalla_poeples:

            parts = line.split('\t')
            if line.startswith("#") or len(parts) < 5:
                continue
            teenager = ClassesLib.Teenager()

            name = parts[1]

            split = name.split(' ')
            teenager.name = split[1].lstrip().rstrip()
            teenager.lastName = split[0].lstrip().rstrip()
            teenager.surname = name[len(split[0]) + len(split[1]) + 1 + 1:].lstrip().rstrip()

            if parts[2].__contains__("fema"):
                teenager.gender = "female"
            else:
                teenager.gender = "male"

            teenager.birthday = parts[3].lstrip().rstrip()

            state = parts[4].lstrip().rstrip()

            if state.__contains__("0"):
                teenager.status = TeenagerStatus.JOBLESS
            elif state.__contains__("1"):
                teenager.status = TeenagerStatus.WORKER

            teenager.info = parts[5].lstrip().rstrip()

            doc = parts[6].lstrip().rstrip()
            doc = doc.replace('А', 'A').replace("С", "C").replace('В', 'B')

            if doc.startswith("I"):
                teenager.document_type = "certificate"
                teenager.series = doc[:-7].lstrip().rstrip()
                teenager.number = doc[-7:].lstrip().rstrip()
            elif doc.startswith("A"):
                teenager.document_type = "pasport"
                teenager.series = doc[:2].lstrip().rstrip()
                teenager.number = doc[-7:].lstrip().rstrip()

            teenager.region = '12'
            teenager.tuman = '172'
            teenager.mahalla = parts[7].lstrip().rstrip()
            teenager.address = parts[8].lstrip().rstrip()

            teenager.phone = parts[9].lstrip().rstrip().replace('(', '').replace(')', '').replace(' ', '').replace('\n',
                                                                                                                   '')

            print(teenager.json)

            try:
                core.addTeenager(teenager)
            except Exception as ex:
                print('Error' + str(ex))

        mahalla_poeples.close()
        core.close()
    except Exception as e:
        print(f"Error on main {str(e)}")
