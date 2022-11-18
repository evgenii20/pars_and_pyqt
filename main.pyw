# -*- coding: utf-8 -*-
# стр. 403
# Подклюяаем модуль QtWidgets содержит классы компонентов
from PyQt5 import QtWidgets
import sys

# создаём объект приложения(только один), принимаем параметры ком. строки "argv":
app = QtWidgets.QApplication(sys.argv)
# вывод списка параметров преданных в командной строке, можно так:
# print(QtWidgets.qApp.argv())
# создаём объект окна
window = QtWidgets.QWidget()
# текст в заголовке окна
window.setWindowTitle("Первая программа на PyQt")
# рекомендуемые параметры окна, окно будет увеличено если компоненты ">" окна
window.resize(300, 150)
# также можно вывести таблицу или картинку в строке с помощью HTML и CSS
label = QtWidgets.QLabel("<center>Привет, мир!</center>")
btnQuit = QtWidgets.QPushButton("&Закрыть окно")
# создаём вертикальный контейнер для выстраивания компонентов сверху вниз в порядке
# добавления:
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
# Добавляем контейнер в основное окно
window.setLayout(vbox)
# назначаем обрабочик сигнала "clicked" при нажатии кнопки
btnQuit.clicked.connect(app.quit)
# вывод окна и всех компонентов
window.show()
# запускает бесконечный цикл обработки событий в приложении.
# Завершаем выполнение программы "exit()"
sys.exit(app.exec_())
