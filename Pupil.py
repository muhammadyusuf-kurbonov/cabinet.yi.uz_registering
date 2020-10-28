import json.decoder
import json.encoder


class Tumanlar:
    qoshtepa = range(7615, 7664 + 1)
    qoshtepa_code = '158'

    toshloq = range(7958, 8008 + 1)
    toshloq_code = '164'

    margilon = range(8386, 8489 + 1)
    margilon_code = '172'

    fargona = range(8218, 8287 + 1)
    fargona_code = '169'


class Pupil:
    name: str
    lastName: str
    surname: str
    gender: str
    birthday: str

    pupil_type: str = "pupil"

    course: str
    school_region: str
    school_tuman: str
    school_id: str

    document_type: str
    series: str
    number: str

    region: str
    tuman: str
    mahalla: str
    address: str

    phone: str

    success: bool = True

    def check(self):
        try:
            if int(self.mahalla) > 0:
                self.success = True
            if self.surname == '':
                self.success = False
            if self.document_type == "certificate":
                if self.series.__contains__('R'):
                    while not self.series.endswith('R'):
                        self.series = self.series[:-1]
                else:
                    self.success = False
            mahalla_code = int(self.mahalla)
            if mahalla_code in Tumanlar.margilon:
                self.tuman = Tumanlar.margilon_code
            elif mahalla_code in Tumanlar.toshloq:
                self.tuman = Tumanlar.toshloq_code
            elif mahalla_code in Tumanlar.qoshtepa:
                self.tuman = Tumanlar.qoshtepa_code
            elif mahalla_code in Tumanlar.fargona:
                self.tuman = Tumanlar.fargona_code

            if len(self.phone) < 7:
                self.phone = '901234567'
            else:
                self.phone = self.phone
        except Exception as e:
            print(e, self.json())
            self.success = False

    def json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    @staticmethod
    def fromJSON(string):
        return json.decoder.JSONDecoder().decode(string)
