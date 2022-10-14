from bs4 import BeautifulSoup
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

print('Put some skills that you are not familiar with - ')
unfamiliar_skill = input('<')
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')  # _all
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(published_date)
            # print(skills)  print(company_name)
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f'More Info: {more_info}')
            print('')

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle("Web scarpping")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("For Company Name:")
        self.label.move(150, 150)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("For Required Skills:")
        self.label1.move(150, 250)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("For More Info:")
        self.label2.move(150, 350)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText(f"Company Name: {company_name.strip()}")
        self.label1.setText(f"Required Skills: {skills.strip()}")
        self.label2.setText(f'More Info: {more_info}')
        self.update()

    def update(self):
        self.label.adjustSize()
        self.label1.adjustSize()
        self.label2.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()