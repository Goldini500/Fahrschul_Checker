from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from PyQt5.QtWidgets import QApplication, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget, QMainWindow
from win10toast import ToastNotifier
import time, sys


toaster = ToastNotifier()
# app = QApplication(sys.argv)

# tableWidget = QTableWidget()
# tableWidget.setColumnCount(2)
# tableWidget.setRowCount(15)
# tableWidget.setFixedSize(500,500)
# header_one = QTableWidgetItem()
# header_two = QTableWidgetItem()
# tableWidget.setStyleSheet("background-color:lightgray;")
# tableWidget.setHorizontalHeaderItem(0,header_one)
# tableWidget.setHorizontalHeaderItem(1,header_two)
# tableWidget.horizontalHeaderItem(0).setText("Thema")
# tableWidget.horizontalHeaderItem(1).setText("Freie Slots")
# tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
# tableWidget.show()


options=Options()
options.add_argument('--headless')
urlpage = 'https://app.cituro.com/booking/fuehrerscheinmacher#show=11eb407e83a50918807c919a9ae8b05a'
driver = webdriver.Firefox(options=options)




driver.get(urlpage)
time.sleep(1)
driver.find_element_by_xpath("(//*[contains(@class, 'add-toggle')])[last()-2]").click()
time.sleep(1)
row = 0

themen = driver.find_elements_by_xpath("//*[contains(@class, 'title')]")
for item in themen:

    if item.text == "":
        pass
    else:
        all_content = item.text
        a,b = (all_content.split("\n"))
        #tableWidget.setItem(row, 0, QTableWidgetItem(a))
        #tableWidget.setItem(row, 1, QTableWidgetItem(b))
        row = row +1
        if a[-7:] == "Thema 4" or all_content.find("Thema 13") != -1 :
            toaster.show_toast("Schnell reservieren!",a + " ist verfügbar" )

        else:
            pass
driver.quit()
#app.exec()
