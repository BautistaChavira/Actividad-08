from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from Particulas import Particula
from Listas import Lista

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.click_agregar)
        self.ui.pushButton.clicked.connect(self.click_final)
        self.ui.pushButton_3.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)
        self.ui.mostrarTabla_pushButton.clicked.connect(self.mostrarTabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscarId)
    
    @Slot()
    def buscarId(self):
        idBusqueda = self.ui.buscar_lineEdit.text()
        identificado = False
        for Particula in self.lista:
            if idBusqueda == (str(Particula.id)):
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem (str(Particula.id))
                origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
                red_widget = QTableWidgetItem(str(Particula.red))
                blue_widget = QTableWidgetItem(str(Particula.blue))
                green_widget = QTableWidgetItem(str(Particula.green))
                distancia_widget = QTableWidgetItem(str(Particula.distancia))
                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_x_widget)
                self.ui.tabla.setItem(0,2,origen_y_widget)
                self.ui.tabla.setItem(0,3,destino_x_widget)
                self.ui.tabla.setItem(0,4,destino_y_widget)
                self.ui.tabla.setItem(0,5,velocidad_widget)
                self.ui.tabla.setItem(0,6,red_widget)
                self.ui.tabla.setItem(0,7,blue_widget)
                self.ui.tabla.setItem(0,8,green_widget)
                self.ui.tabla.setItem(0,9,distancia_widget)
                identificado = True
                return 
        if not identificado:
            QMessageBox.warning(self, "Error", f'La particula con el id "{idBusqueda}" no fue encontrada')


    @Slot()
    def mostrarTabla(self):
        self.ui.tabla.clear()
        self.ui.tabla.setColumnCount(10)
        headers = ["Id", "Origen X", "Origen Y", "Destino X", "Destino Y", "Velocidad", "Rojo", "Verde", "Azul", "Destino"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.lista))

        row = 0
        for Particula in self.lista:
            id_widget = QTableWidgetItem (str(Particula.id))
            origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            green_widget = QTableWidgetItem(str(Particula.green))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_x_widget)
            self.ui.tabla.setItem(row,2,origen_y_widget)
            self.ui.tabla.setItem(row,3,destino_x_widget)
            self.ui.tabla.setItem(row,4,destino_y_widget)
            self.ui.tabla.setItem(row,5,velocidad_widget)
            self.ui.tabla.setItem(row,6,red_widget)
            self.ui.tabla.setItem(row,7,blue_widget)
            self.ui.tabla.setItem(row,8,green_widget)
            self.ui.tabla.setItem(row,9,distancia_widget)
            row += 1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)' )[0]
        if self.lista.abrir_archivo(ubicacion):
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.insertPlainText("Lista cargada\n")
            self.ui.plainTextEdit.insertPlainText(str(self.lista))
            QMessageBox.information(
                self,
                "Carga completada",
                "Se cargaron los datos contenidos en :" + ubicacion
            )
        else:
                QMessageBox.critical(
                    self,
                    "Error",
                    "Error al abrir el archivo" + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
      ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON (*.json)'
        )[0]
      print(ubicacion)
      if self.lista.guardar_archivo(ubicacion):
        QMessageBox.information(
            self,
            "Guardado completado",
            "Se pudo crear el archivo en la direccion : " + ubicacion,
            
        )

      else :
        QMessageBox.critical(
            self,
            "Error",
            "No se pudo crear el archivo" + ubicacion
        )

    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.lista))

    @Slot()
    def click_agregar(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_inicio(particula)

    @Slot()
    def click_final(self):
        id = self.ui.spinBox.value()
        origen_x = self.ui.spinBox_2.value()
        origen_y = self.ui.spinBox_3.value()
        destino_x = self.ui.spinBox_4.value()
        destino_y = self.ui.spinBox_5.value()
        velocidad = self.ui.spinBox_6.value()
        rojo = self.ui.spinBox_7.value()
        verde = self.ui.spinBox_8.value()
        azul = self.ui.spinBox_9.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.insertar_final(particula)