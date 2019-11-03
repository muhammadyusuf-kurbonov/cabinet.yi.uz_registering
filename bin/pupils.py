from bin import ClassesLib, core
from bin.Consts import PUPILS_FILE_PATH


def start():
    core.login()

    infos = open(PUPILS_FILE_PATH, mode="r", encoding="utf-8")
    try:
        for line in infos:
            parts = line.split('\t')
            if line.startswith("#") or len(parts) < 5:
                continue

            pupil = ClassesLib.Pupil()

            name = parts[1]

            split = name.split(' ')
            pupil.name = split[1].lstrip().rstrip()
            pupil.lastName = split[0].lstrip().rstrip()
            pupil.surname = name[len(split[0]) + len(split[1]) + 1 + 1:].lstrip().rstrip()

            if parts[2].__contains__("fema"):
                pupil.gender = "female"
            else:
                pupil.gender = "male"

            pupil.birthday = parts[3].lstrip().rstrip()

            pupil.school_region = '12'
            pupil.school_tuman = '172'
            pupil.school_id = str(3282 + int(parts[4].lstrip().rstrip()))  # maktab

            pupil.course = parts[5].lstrip().rstrip()

            doc = parts[6].lstrip().rstrip()
            doc = doc.replace('А', 'A').replace("С", "C").replace('В', 'B')

            if doc.startswith("I"):
                pupil.document_type = "certificate"
                pupil.series = doc[:-7].lstrip().rstrip()
                pupil.number = doc[-7:].lstrip().rstrip()
            elif doc.startswith("A"):
                pupil.document_type = "pasport"
                pupil.series = doc[:2].lstrip().rstrip()
                pupil.number = doc[-7:].lstrip().rstrip()

            pupil.region = '12'
            pupil.tuman = '172'
            pupil.mahalla = parts[7].lstrip().rstrip()
            pupil.address = parts[8].lstrip().rstrip()

            pupil.phone = parts[9].lstrip().rstrip().replace('(', '').replace(')', '').replace(' ', '').replace('\n',
                                                                                                                '')

            print(pupil.json())

            try:
                core.addPupil(pupil)
            except Exception as ex:
                print('Error' + str(ex))

        infos.close()
        core.close()
    except Exception as e:
        print(f"Error on main {str(e)}")
