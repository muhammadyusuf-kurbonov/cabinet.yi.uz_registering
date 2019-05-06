import Pupil
import graphics

graphics.login()

pupils = list()

infos = open("infos.txt", mode="r", encoding="utf-8")

count = 0
for line in infos:
    part_number = 0
    parts = line.split('\t')
    pupil = Pupil.Pupil()

    name = parts[1]

    split = name.split(' ')
    pupil.name = split[1]
    pupil.lastName = split[0]
    pupil.surname = name[len(split[0])+len(split[1])+1+1:]


    if parts[2].__contains__("fema"):
        pupil.gender = "female"
    else:
        pupil.gender = "male"

    pupil.birthday = parts[3]

    pupil.school_region = '12'
    pupil.school_tuman = '172'
    pupil.school_id = str(3282 + int(parts[4]))  # maktab

    pupil.course = parts[5]

    doc = parts[6]
    doc = doc.replace('А', 'A').replace("С", "C").replace('В','B')

    if doc.startswith("I"):
        pupil.document_type = "certificate"
        pupil.series = doc[:-7]
        pupil.number = doc[-7:]
    elif doc.startswith("A"):
        pupil.document_type = "pasport"
        pupil.series = doc[:2]
        pupil.number = doc[-7:]

    pupil.region = '12'
    pupil.tuman = '158'
    pupil.mahalla = parts[7]
    pupil.address = parts[8]

    pupil.phone = parts[9].replace('(', '').replace(')', '').replace(' ', '').replace('\n', '')

    pupils.append(pupil)

    try:
        graphics.add(pupil)

        pupils.remove(pupil)

        file = open("success.txt", 'a')
        file.write(pupil.json())
        file.close()
    except Exception as ex:
        print('Error' + str(ex))


    count = count + 1

error = open("error.txt", "w")
for p in pupils:
    error.write(p.json())
error.close()
infos.close()
graphics.close()
