# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.view_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.page1_result_listwidget = QtWidgets.QListWidget(self.view_page)
        self.page1_result_listwidget.setObjectName("page1_result_listwidget")
        self.gridLayout_3.addWidget(self.page1_result_listwidget, 0, 1, 1, 1)
        self.page1_text_outputs = QtWidgets.QPlainTextEdit(self.view_page)
        self.page1_text_outputs.setObjectName("page1_text_outputs")
        self.gridLayout_3.addWidget(self.page1_text_outputs, 1, 0, 1, 2)
        self.page1_imglistWidget = QtWidgets.QListWidget(self.view_page)
        self.page1_imglistWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.page1_imglistWidget.setAcceptDrops(True)
        self.page1_imglistWidget.setDragEnabled(False)
        self.page1_imglistWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.page1_imglistWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.page1_imglistWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.page1_imglistWidget.setIconSize(QtCore.QSize(224, 224))
        self.page1_imglistWidget.setMovement(QtWidgets.QListView.Free)
        self.page1_imglistWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.page1_imglistWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.page1_imglistWidget.setSelectionRectVisible(False)
        self.page1_imglistWidget.setObjectName("page1_imglistWidget")
        self.gridLayout_3.addWidget(self.page1_imglistWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.view_page)
        self.paint_page = QtWidgets.QWidget()
        self.paint_page.setObjectName("paint_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.paint_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.page2_tableWidget = QtWidgets.QTableWidget(self.paint_page)
        self.page2_tableWidget.setRowCount(5)
        self.page2_tableWidget.setColumnCount(0)
        self.page2_tableWidget.setObjectName("page2_tableWidget")
        self.page2_tableWidget.horizontalHeader().setVisible(False)
        self.page2_tableWidget.horizontalHeader().setDefaultSectionSize(81)
        self.page2_tableWidget.verticalHeader().setDefaultSectionSize(29)
        self.page2_tableWidget.verticalHeader().setMinimumSectionSize(26)
        self.gridLayout_2.addWidget(self.page2_tableWidget, 1, 0, 3, 3)
        self.pushButton_load_table = QtWidgets.QPushButton(self.paint_page)
        self.pushButton_load_table.setObjectName("pushButton_load_table")
        self.gridLayout_2.addWidget(self.pushButton_load_table, 0, 0, 1, 1)
        self.pushButton_build = QtWidgets.QPushButton(self.paint_page)
        self.pushButton_build.setObjectName("pushButton_build")
        self.gridLayout_2.addWidget(self.pushButton_build, 0, 1, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.paint_page)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.paint_page)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.page2_x_column = QtWidgets.QTextEdit(self.tab_2)
        self.page2_x_column.setMaximumSize(QtCore.QSize(16777215, 35))
        self.page2_x_column.setObjectName("page2_x_column")
        self.gridLayout.addWidget(self.page2_x_column, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.page2_y_column = QtWidgets.QTextEdit(self.tab_2)
        self.page2_y_column.setMaximumSize(QtCore.QSize(16777215, 35))
        self.page2_y_column.setObjectName("page2_y_column")
        self.gridLayout.addWidget(self.page2_y_column, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.page2_x_title = QtWidgets.QTextEdit(self.tab_2)
        self.page2_x_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.page2_x_title.setObjectName("page2_x_title")
        self.gridLayout.addWidget(self.page2_x_title, 0, 3, 1, 1)
        self.page2_y_title = QtWidgets.QTextEdit(self.tab_2)
        self.page2_y_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.page2_y_title.setObjectName("page2_y_title")
        self.gridLayout.addWidget(self.page2_y_title, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.page2_fig_title = QtWidgets.QTextEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_fig_title.sizePolicy().hasHeightForWidth())
        self.page2_fig_title.setSizePolicy(sizePolicy)
        self.page2_fig_title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.page2_fig_title.setObjectName("page2_fig_title")
        self.gridLayout.addWidget(self.page2_fig_title, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.page2_fig_style = QtWidgets.QComboBox(self.tab_2)
        self.page2_fig_style.setMinimumSize(QtCore.QSize(0, 35))
        self.page2_fig_style.setObjectName("page2_fig_style")
        self.gridLayout.addWidget(self.page2_fig_style, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 49, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_spliter = QtWidgets.QComboBox(self.tab)
        self.comboBox_spliter.setGeometry(QtCore.QRect(70, 20, 111, 35))
        self.comboBox_spliter.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_spliter.setBaseSize(QtCore.QSize(0, 35))
        self.comboBox_spliter.setObjectName("comboBox_spliter")
        self.comboBox_spliter.addItem("")
        self.comboBox_spliter.addItem("")
        self.comboBox_spliter.addItem("")
        self.comboBox_spliter.addItem("")
        self.comboBox_spliter.addItem("")
        self.spinBox_gap_line = QtWidgets.QSpinBox(self.tab)
        self.spinBox_gap_line.setGeometry(QtCore.QRect(70, 70, 111, 35))
        self.spinBox_gap_line.setMinimumSize(QtCore.QSize(0, 35))
        self.spinBox_gap_line.setMinimum(1)
        self.spinBox_gap_line.setObjectName("spinBox_gap_line")
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 3, 1, 1)
        self.page2_zoom = QtWidgets.QSlider(self.paint_page)
        self.page2_zoom.setOrientation(QtCore.Qt.Vertical)
        self.page2_zoom.setObjectName("page2_zoom")
        self.gridLayout_2.addWidget(self.page2_zoom, 3, 4, 1, 1)
        self.page2_graphicsView = QtWidgets.QGraphicsView(self.paint_page)
        self.page2_graphicsView.setObjectName("page2_graphicsView")
        self.gridLayout_2.addWidget(self.page2_graphicsView, 3, 3, 1, 1)
        self.stackedWidget.addWidget(self.paint_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.page3_heatmap = QtWidgets.QCheckBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_heatmap.sizePolicy().hasHeightForWidth())
        self.page3_heatmap.setSizePolicy(sizePolicy)
        self.page3_heatmap.setMaximumSize(QtCore.QSize(150, 16777215))
        self.page3_heatmap.setObjectName("page3_heatmap")
        self.gridLayout_4.addWidget(self.page3_heatmap, 0, 0, 1, 3)
        self.page3_bbox = QtWidgets.QCheckBox(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_bbox.sizePolicy().hasHeightForWidth())
        self.page3_bbox.setSizePolicy(sizePolicy)
        self.page3_bbox.setObjectName("page3_bbox")
        self.gridLayout_4.addWidget(self.page3_bbox, 0, 3, 1, 3)
        self.page3_target_img = QtWidgets.QLabel(self.page)
        self.page3_target_img.setText("")
        self.page3_target_img.setScaledContents(False)
        self.page3_target_img.setObjectName("page3_target_img")
        self.gridLayout_4.addWidget(self.page3_target_img, 1, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 6, 1, 1)
        self.page3_result_img = QtWidgets.QLabel(self.page)
        self.page3_result_img.setText("")
        self.page3_result_img.setScaledContents(False)
        self.page3_result_img.setObjectName("page3_result_img")
        self.gridLayout_4.addWidget(self.page3_result_img, 1, 7, 1, 1)
        self.page3_open_file = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_open_file.sizePolicy().hasHeightForWidth())
        self.page3_open_file.setSizePolicy(sizePolicy)
        self.page3_open_file.setObjectName("page3_open_file")
        self.gridLayout_4.addWidget(self.page3_open_file, 2, 0, 1, 1)
        self.page3_open_dir = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_open_dir.sizePolicy().hasHeightForWidth())
        self.page3_open_dir.setSizePolicy(sizePolicy)
        self.page3_open_dir.setText("")
        self.page3_open_dir.setObjectName("page3_open_dir")
        self.gridLayout_4.addWidget(self.page3_open_dir, 2, 1, 1, 1)
        self.page3_build = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_build.sizePolicy().hasHeightForWidth())
        self.page3_build.setSizePolicy(sizePolicy)
        self.page3_build.setObjectName("page3_build")
        self.gridLayout_4.addWidget(self.page3_build, 2, 2, 1, 1)
        self.page3_save = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_save.sizePolicy().hasHeightForWidth())
        self.page3_save.setSizePolicy(sizePolicy)
        self.page3_save.setObjectName("page3_save")
        self.gridLayout_4.addWidget(self.page3_save, 2, 3, 1, 1)
        self.page3_clear = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_clear.sizePolicy().hasHeightForWidth())
        self.page3_clear.setSizePolicy(sizePolicy)
        self.page3_clear.setText("")
        self.page3_clear.setObjectName("page3_clear")
        self.gridLayout_4.addWidget(self.page3_clear, 2, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(482, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 5, 1, 3)
        self.page3_img_list_widget = QtWidgets.QListWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page3_img_list_widget.sizePolicy().hasHeightForWidth())
        self.page3_img_list_widget.setSizePolicy(sizePolicy)
        self.page3_img_list_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.page3_img_list_widget.setIconSize(QtCore.QSize(70, 70))
        self.page3_img_list_widget.setMovement(QtWidgets.QListView.Static)
        self.page3_img_list_widget.setFlow(QtWidgets.QListView.TopToBottom)
        self.page3_img_list_widget.setViewMode(QtWidgets.QListView.IconMode)
        self.page3_img_list_widget.setObjectName("page3_img_list_widget")
        self.gridLayout_4.addWidget(self.page3_img_list_widget, 3, 0, 1, 8)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 857, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMouseTracking(False)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionLoad_Files = QtWidgets.QAction(MainWindow)
        self.actionLoad_Files.setObjectName("actionLoad_Files")
        self.actionLoad_Dir = QtWidgets.QAction(MainWindow)
        self.actionLoad_Dir.setObjectName("actionLoad_Dir")
        self.actionLoad_from_TxT = QtWidgets.QAction(MainWindow)
        self.actionLoad_from_TxT.setObjectName("actionLoad_from_TxT")
        self.actionView = QtWidgets.QAction(MainWindow)
        self.actionView.setCheckable(False)
        self.actionView.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/image_view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView.setIcon(icon)
        self.actionView.setText("")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionView.setFont(font)
        self.actionView.setShortcutVisibleInContextMenu(True)
        self.actionView.setObjectName("actionView")
        self.actionDraw_Fig = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/figure_paint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDraw_Fig.setIcon(icon1)
        self.actionDraw_Fig.setText("")
        self.actionDraw_Fig.setObjectName("actionDraw_Fig")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/edit-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon2)
        self.actionEdit.setObjectName("actionEdit")
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionView)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDraw_Fig)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_load_table.setText(_translate("MainWindow", "Load Table"))
        self.pushButton_build.setText(_translate("MainWindow", "Build"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Y Colum (s)*"))
        self.label_6.setText(_translate("MainWindow", "X Title*"))
        self.label_3.setText(_translate("MainWindow", "X Colum*"))
        self.label_7.setText(_translate("MainWindow", "Y Title*"))
        self.label_8.setText(_translate("MainWindow", "Fig Title*"))
        self.label_5.setText(_translate("MainWindow", "Fig Style"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Figure Setting"))
        self.label.setText(_translate("MainWindow", "Spliter"))
        self.label_2.setText(_translate("MainWindow", "Gap Line"))
        self.comboBox_spliter.setItemText(0, _translate("MainWindow", "auto"))
        self.comboBox_spliter.setItemText(1, _translate("MainWindow", ";"))
        self.comboBox_spliter.setItemText(2, _translate("MainWindow", "\\n"))
        self.comboBox_spliter.setItemText(3, _translate("MainWindow", ":"))
        self.comboBox_spliter.setItemText(4, _translate("MainWindow", ","))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Table Setting"))
        self.page3_heatmap.setText(_translate("MainWindow", "Heatmap mode"))
        self.page3_bbox.setText(_translate("MainWindow", "Boudingbox mode"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad_Files.setText(_translate("MainWindow", "Open File(s)"))
        self.actionLoad_Dir.setText(_translate("MainWindow", "Open Dir"))
        self.actionLoad_from_TxT.setText(_translate("MainWindow", "Open from Txt"))
        self.actionEdit.setText(_translate("MainWindow", "edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
