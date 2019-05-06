import Pupil
import graphics

graphics.login()

pupils = list()

infos = open("infos.txt", mode="r", encoding="utf-8")
try:
    for line in infos:
        if line.startswith("#"):
            continue

        parts = line.split('\t')
        pupil = Pupil.Pupil()

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

        pupil.phone = parts[9].lstrip().rstrip().replace('(', '').replace(')', '').replace(' ', '').replace('\n', '')

        pupils.append(pupil)

        print(pupil.json())

        try:
            graphics.add(pupil)

            pupils.remove(pupil)

            file = open("success.txt", 'a')
            file.write(pupil.json()+"\n")
            file.close()
        except Exception as ex:
            print('Error' + str(ex))

    error = open("error.txt", "w")
    for p in pupils:
        error.write(p.json())
    error.close()
    infos.close()
    graphics.close()
except Exception as e:
    print(f"Error on main {str(e)}")
