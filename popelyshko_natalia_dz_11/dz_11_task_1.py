class Data:
    def __init__(self, params):
        self.day_month_year = str(params)

    @classmethod
    def extract(cls, date):
        try:
            result = [int(element) for element in date.split('-')]
            return result
        except ValueError:
            print('Ожидается формат dd-mm-yyyy')
            return False

    @staticmethod
    def data_valid(data):
        if int(data[0: 2]) > 31:
            print('Ошибка в дне. Ожидается формат dd-mm-yyyy')
            return False
        if int(data[3: 5]) > 12:
            print('Ошибка в месяце. Ожидается формат dd-mm-yyyy')
            return False
        if int(data[6: 10]) < 1000 or len(data[6:]) != 4:
            print('Ошибка в годе. Ожидается формат dd-mm-yyyy')
            return False
        return True


today = Data('20-07-2022')
print(today.extract('21-07-2022'))
print(today.data_valid('21-07-2022'))