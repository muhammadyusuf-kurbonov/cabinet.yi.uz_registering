answer = ""

while not (answer.__contains__("1") or answer.__contains__("2")):
    answer = input("Quydagi qaysi ma\'lumotlarni kiritish lozim?\n"
                   "[1] o'quvchilar\n"
                   "[2] mahalla yoshlari\n"
                   ">   ")

from bin import pupils, mahalla

if answer == "1":
    pupils.start()
elif answer == "2":
    mahalla.start()
