class Stationery:
    title = 'Title'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовка маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
