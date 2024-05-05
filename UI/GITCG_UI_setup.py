from UI.ICON import *
from UI.GeniusInvokationTCG_UI_ui import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QByteArray
import sys

class UI_Setup(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Win = Ui_MainWindow()
        self.Win.setupUi(self)
        self.content_setup()
    
    def content_setup(self):
        for i in self.Win.frame.findChildren(QPushButton):
            # i.setText('◇☼')
            # i.setIcon(self.icon_setup(ICON.SETTING_Normal, ICON.SETTING_Active))
            i.setIcon(self.icon_setup(ICON.SETTING_Normal))
            # print(i)
    
    def icon_setup(self, icon_normal, icon_active=None):
        pixmap_normal = QPixmap()
        pixmap_normal.loadFromData(QByteArray(icon_normal.encode()))
        icon = QIcon()
        icon.addPixmap(pixmap_normal, QIcon.Normal)
        if icon_active == None:
            icon_active = self.svg_change_color(icon_normal, "#00AAAA")
        if icon_active:
            pixmap_active = QPixmap()
            pixmap_active.loadFromData(QByteArray(icon_active.encode()))
            icon.addPixmap(pixmap_active, QIcon.Active)
        return icon
    
    def svg_change_color(self, old_svg, new_color):
        old_color = old_svg.split('fill="')[1].split('"')[0]
        # print(old_color)
        return old_svg.replace(f'fill="{old_color}"', f'fill="{new_color}"')
    