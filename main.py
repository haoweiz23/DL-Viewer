from PyQt5.Qt import *
import sys
import os
import matplotlib.pyplot as plt
from ui import Ui_MainWindow
from qt_material import apply_stylesheet


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionView.triggered.connect(self.call_back_action_actionView)
        # self.actionView.setIcon(QIcon('icons/image_view.png'))
        self.actionDraw_Fig.triggered.connect(self.call_back_action_actionDraw_Fig)
        # self.actionDraw_Fig.setIcon(QIcon('icons/figure_paint.png'))
        self.pushButton_load_table.clicked.connect(self.call_back_push_button_load_table)
        self.pushButton_build.clicked.connect(self.call_back_push_button_build)

        self.H_Max, self.W_Max = 960, 960
        # self.additem('./imgs/0181723.jpg', self.page1_imglistWidget)
        # self.page2_x_column.setText('1')
        self.page1_imglistWidget.dropEvent = self.dropEvent
        self.page1_imglistWidget.dragEnterEvent = self.dragEnterEvent
        self.page1_imglistWidget.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(125, 125, 125);')
        self.page1_result_listwidget.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(125, 125, 125);')
        self.page1_text_outputs.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(125, 125, 125);')

        # self.setMouseTracking(True)
        self.mousePosX,  self.mousePosY = 120, 38
        self.mousePosX_gap,  self.mousePosY_gap = 0, 0
        self.mousePosX_Flag,  self.mousePosY_Flag = False, False


        # self.toolBar.setStyleSheet("QToolBar{spacing:8px;}")
        # self.actionView.icon.setStyleSheet("QToolBar{spacing:8px;}")

        # for i in self.children():
        #     # 根据实际情况去过滤一些不带焦点功能的子组件
        #     if isinstance(i, QVBoxLayout) or isinstance(i, QHBoxLayout) \
        #             or isinstance(i, QLayout) or isinstance(i, QAction):
        #         pass
        #     else:
        #         i.setFocusPolicy(Qt.NoFocus)

    def eventFilter(self, objwatched, event):
        eventType = event.type()

        for i in self.children():
            if isinstance(i, QVBoxLayout) or isinstance(i, QHBoxLayout) \
                    or isinstance(i, QLayout) or isinstance(i, QAction):
                # if not isinstance(i, QListWidget) and not isinstance(i, QListWidgetItem):
                self.is_focus_keyboard_event(objwatched, eventType, i)

        return super().eventFilter(objwatched, event)

    def is_focus_keyboard_event(self, watched, event, obj):
        if watched == obj:
            if event == QEvent.FocusIn:
                obj.grabKeyboard()
            elif event == QEvent.FocusIn:
                obj.releaseKeyboard()

    def call_back_action_actionView(self):
        self.stackedWidget.setCurrentIndex(0)

    def call_back_action_actionDraw_Fig(self):
        self.stackedWidget.setCurrentIndex(1)

    def call_back_push_button_load_table(self):
        file, filetype = QFileDialog.getOpenFileName(self, "Select file", "",
                                                     "All Files (*);;Txt Files (*.txt)")

        try:
            log = open(file, 'r', encoding='utf-8').readlines()
            spliter = self.comboBox_spliter.currentText()
            gap_line = self.spinBox_gap_line.value()
            import re

            n = self.page2_tableWidget.columnCount()

            self.page2_tableWidget.setRowCount(len(list(range(0, len(log), gap_line))))

            for i in range(0, len(log), gap_line):
                pattern = re.compile(r"\d+\.?\d*")
                res = re.findall(pattern, log[i].strip())
                self.page2_tableWidget.setColumnCount(n + len(res))
                for j in range(len(res)):
                    row_item = QTableWidgetItem(res[j])
                    self.page2_tableWidget.setItem(i, n + j, row_item)

        except Exception as e:
            print(e)

    def call_back_push_button_build(self):
        try:
            x = int(self.page2_x_column.toPlainText()) - 1
            y = [int(i) - 1 for i in self.page2_y_column.toPlainText().split(';')]

            x_s = [float(self.page2_tableWidget.item(i, x).text())
                   for i in range(self.page2_tableWidget.rowCount())]

            y_s = []
            for i in y:
                y_s.append([float(self.page2_tableWidget.item(j, i).text())
                            for j in range(self.page2_tableWidget.rowCount())])

            fig = plt.figure()
            color = ['green', 'blue', 'red', 'pink', 'black', 'darkblue']
            titles = [x for x in self.page2_y_title.toPlainText().split(';')]
            for i in range(len(y_s)):
                plt.plot(x_s, y_s[i], color=color[i], label=titles[i])
            plt.legend()
            plt.show()
            plt.title(self.page2_fig_title.toPlainText())

            # w, h, c = img.shape
            # frame = QImage(img, w, h, QImage.Format_RGB888)
            # pix = QPixmap.fromImage(frame)
            # item = QGraphicsPixmapItem(pix)
            # scene = QGraphicsScene()
            # scene.addItem(item)
            # self.page2_graphicsView.setScene(scene)
        except Exception as e:
            print(e)

    def additem(self, img_path, obj):
        pix1 = QPixmap(img_path).scaled(self.page1_imglistWidget.iconSize())
        item = QListWidgetItem()
        item.setIcon(QIcon(pix1.scaled(self.H_Max, self.W_Max, Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        # item.setCheckState(Qt.CheckState.Unchecked)
        obj.addItem(item)

    def keyReleaseEvent(self, e: QKeyEvent):  # sometimes keyPressEvent not work, switch to keyReleaseEvent
        try:
            if e.key() == Qt.Key_Delete:
                items = self.page1_imglistWidget.selectedItems()
                for i in items:
                    self.page1_imglistWidget.takeItem(self.page1_imglistWidget.indexFromItem(i).row())

                selected_items = self.page2_tableWidget.selectedItems()

                if len(selected_items) == self.page2_tableWidget.rowCount():
                    Columns = set([x.column() for x in selected_items])
                    for i in Columns:
                        self.page2_tableWidget.removeColumn(i)
                elif len(selected_items) == self.page2_tableWidget.columnCount():
                    Rows = set([x.row() for x in selected_items])
                    for i in Rows:
                        self.page2_tableWidget.removeRow(i)

            elif e.key() == Qt.Key_Minus:
                self.page1_imglistWidget.setIconSize(self.page1_imglistWidget.iconSize() * 0.9)
            elif e.key() == Qt.Key_Plus:
                if not self.page1_imglistWidget.iconSize().height() >= self.H_Max:
                    self.page1_imglistWidget.setIconSize(self.page1_imglistWidget.iconSize() * 1.1)
            elif e.key() == Qt.Key_Left:
                items = self.page1_imglistWidget.selectedItems()  # 获取所有的拖入item

                for i in items:
                    current_row = self.page1_imglistWidget.indexFromItem(i).row()
                    self.page1_imglistWidget.takeItem(self.page1_imglistWidget.indexFromItem(i).row())  # 实时移除来源item
                    self.page1_imglistWidget.insertItem(current_row - 1, i)
                    self.page1_imglistWidget.item(current_row - 1).setSelected(True)
            elif e.key() == Qt.Key_Right:
                items = self.page1_imglistWidget.selectedItems()  # 获取所有的拖入item
                for i in items:
                    current_row = self.page1_imglistWidget.indexFromItem(i).row()
                    self.page1_imglistWidget.takeItem(self.page1_imglistWidget.indexFromItem(i).row())  # 实时移除来源item
                    self.page1_imglistWidget.insertItem(current_row + 1, i)
                    self.page1_imglistWidget.item(current_row + 1).setSelected(True)
        except Exception as e:
            print(e)

    def dragEnterEvent(self, e: QDragEnterEvent):
        e.accept()

    def dropEvent(self, e: QDropEvent):
        try:
            img_paths = [x.toLocalFile() for x in e.mimeData().urls()]
            import glob

            for path in img_paths:
                if os.path.isdir(path):
                    files = glob.glob(path + '/*')
                    for file in files:
                        if file.endswith('.jpg') or file.endswith('.png'):
                            self.additem(file, self.page1_imglistWidget)
                else:
                    self.additem(path, self.page1_imglistWidget)

            e.accept()
        except:
            pass

        # TODO: fix the move item problem
        try:
            pos = e.pos()  # 获取拖入事件的坐标
            current_item = self.page1_imglistWidget.itemAt(pos)  # 获取当前坐标下的item
            current_index = self.page1_imglistWidget.indexFromItem(current_item)  # 获取该item的index
            current_row = current_index.row()  # 获取行数
            items = self.page1_imglistWidget.selectedItems()  # 获取所有的拖入item

            for i in items:
                self.page1_imglistWidget.takeItem(self.page1_imglistWidget.indexFromItem(i).row())  # 实时移除来源item
                self.page1_imglistWidget.insertItem(current_row, i)

            e.accept()
        except:
            pass

        e.ignore()

    def mousePressEvent(self, event):
        n = event.button()

        # print(event.x(), event.y())     # (465, 298)
        #
        # print(self.page1_imglistWidget.geometry().x(), self.page1_imglistWidget.geometry().x() + self.page1_imglistWidget.geometry().width())  # 9 376
        # print(self.page1_imglistWidget.geometry().y(), self.page1_imglistWidget.geometry().y() + self.page1_imglistWidget.geometry().height()) # 9 267

        # TODO: fix different style
        relative_pos_x, relative_pos_y = event.x() - self.mousePosX_gap - self.page1_imglistWidget.geometry().x(), \
                                         event.y() - self.mousePosY_gap - self.page1_imglistWidget.geometry().y()
        if relative_pos_x < self.page1_imglistWidget.geometry().width() + 20 and relative_pos_x > self.page1_imglistWidget.geometry().width() - 20:
            self.mousePosX = event.x()
            self.mousePosX_Flag = True
        if relative_pos_y < self.page1_imglistWidget.geometry().height() + 20 and relative_pos_y > self.page1_imglistWidget.geometry().height() - 20:
            self.mousePosY = event.y()
            self.mousePosY_Flag = True

    def mouseDoubleClickEvent(self, event):
        self.mousePosX_gap = event.x() - self.page1_imglistWidget.geometry().x() - self.page1_imglistWidget.geometry().width()
        self.mousePosY_gap = event.y() - self.page1_imglistWidget.geometry().y() - self.page1_imglistWidget.geometry().height()
        # print(self.mousePosX_gap, self.mousePosY_gap)

    def mouseReleaseEvent(self, event):
        self.mousePosX_Flag = False
        self.mousePosY_Flag = False

    def mouseMoveEvent(self, event):
        if self.mousePosX_Flag:
            xChanged = event.x() - self.mousePosX
            self.page1_imglistWidget.resize(self.page1_imglistWidget.geometry().width() + xChanged,
                                            self.page1_imglistWidget.geometry().height())
            self.page1_result_listwidget.setGeometry(self.page1_result_listwidget.geometry().x() + xChanged,
                                                     self.page1_result_listwidget.geometry().y() ,
                                                     self.page1_result_listwidget.geometry().width() - xChanged,
                                            self.page1_result_listwidget.geometry().height())
            self.mousePosX = event.x()
        if self.mousePosY_Flag:
            yChanged = event.y() - self.mousePosY
            self.page1_imglistWidget.resize(self.page1_imglistWidget.geometry().width(),
                                            self.page1_imglistWidget.geometry().height() + yChanged)
            self.page1_result_listwidget.setGeometry(self.page1_result_listwidget.geometry().x(),
                                                     self.page1_result_listwidget.geometry().y(),
                                                     self.page1_result_listwidget.geometry().width(),
                                                     self.page1_result_listwidget.geometry().height() + yChanged)
            self.page1_text_outputs.setGeometry(self.page1_text_outputs.geometry().x(),
                                                     self.page1_text_outputs.geometry().y() + yChanged,
                                                     self.page1_text_outputs.geometry().width(),
                                                     self.page1_text_outputs.geometry().height() - yChanged)
            self.mousePosY = event.y()


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    apply_stylesheet(app, theme='default_light.xml')
    myWin.show()
    app.installEventFilter(myWin)
    sys.exit(app.exec_())
