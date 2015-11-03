from PyQt4 import QtCore
from PyQt4 import QtGui


class TableWithPaste(QtGui.QTableWidget):

    itemDropped = QtCore.pyqtSignal(object)
    itemUrlPasted = QtCore.pyqtSignal(object)
    itemImagePasted = QtCore.pyqtSignal(object)


    def __init__(self, parent):
        QtGui.QTableWidget.__init__(self, parent)
        # super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        quitAction = QtGui.QAction("Quit", self)
        quitAction.triggered.connect(QtGui.qApp.quit)

        pasteAction = QtGui.QAction("Paste", self)
        pasteAction.triggered.connect(self.getPastin)
        self.addAction(pasteAction)
        self.addAction(quitAction)



    def dragEnterEvent(self, event):
        # if e.mimeData().hasFormat('text/plain'):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:  # hasFormat('text/plain'):
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            self.itemDropped.emit(event)
            # new_row_number = self.rowCount()
            # self.insertRow(new_row_number)
            # col = 0
            # print(event.mimeData().urls()[0].toString())
            # self.item = QtGui.QTableWidgetItem(event.mimeData().urls()[0].path()[1:])
            # self.item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            # self.setItem(new_row_number, col, self.item)
            # col = 1
            # col_width = self.columnWidth(col)
            # row_height = self.rowHeight(new_row_number)
            # image = QtGui.QImage(event.mimeData().imageData)
            # if image.isNull():
            #     print("Image is Null :(")
            # else:
            #     image_scaled = image.scaled(col_width, row_height, QtCore.Qt.KeepAspectRatio)
            #     pixmap = QtGui.QPixmap.fromImage(image_scaled)
            #     self.item = QtGui.QTableWidgetItem()
            #     self.item.setData(QtCore.Qt.DecorationRole, pixmap)
            #     self.item.setTextAlignment(QtCore.Qt.AlignCenter)
            #     self.item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            #     self.setItem(new_row_number, col, self.item)
            # print("finish")
        else:
            event.ignore()

    def getPastin(self):
        cboard = QtGui.qApp.clipboard().mimeData()
        if cboard.hasUrls:
            self.itemUrlPasted.emit(cboard)
        # elif cboard.hasImage():
        elif cboard.hasImage:
            self.itemImagePasted.emit(cboard)
            # print("Business!!!")
            # new_row_number = self.rowCount()
            # row_height = self.rowHeight(new_row_number-1)
            # self.insertRow(new_row_number)
            # self.setRowHeight(new_row_number, row_height)
            # col = 1
            # col_width = self.columnWidth(col)
            # image = QtGui.QImage(cboard.imageData())
            # if image.isNull():
            #     print("Image is Null :(")
            # else:
            #     image_scaled = image.scaled(col_width, row_height, QtCore.Qt.KeepAspectRatio)
            #     pixmap = QtGui.QPixmap.fromImage(image_scaled)
            #     self.item = QtGui.QTableWidgetItem()
            #     self.item.setData(QtCore.Qt.DecorationRole, pixmap)
            #     self.item.setTextAlignment(QtCore.Qt.AlignCenter)
            #     self.item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            #     self.setItem(new_row_number, col, self.item)
