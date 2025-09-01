from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QButtonGroup,
    QListView,
) 
from PySide6.QtCore import QThread, Signal, Qt, QTimer, QObject
from PySide6.QtGui import QPixmap, QImage
from modules.interface import Ui_MainWindow
from modules.serial_process import SerialProcess
from modules.calculate_locator import CalculateLocator


class SerialSignal(QObject):
    data_received = Signal(str)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("🚀 Initializing App...")

        # setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create signal object
        self.signal_handler = SerialSignal()
        self.signal_handler.data_received.connect(self.handle_serial_data)

        # setup proces
        self.system = SerialProcess(callback=self.handle_serial_data)
        
        #setup calculate
        self.calc = CalculateLocator()

        # variabel
        self.port = None
        self.lida_state = True
        self.kclka_state = False
        self.locator_lida = {
            1: [0,0,0],
            2: [0,0,0],
            3: [0,0,0],
            4: [0,0,0],
            5: [0,0,0],
            6: [0,0,0]
        }
        
        self.locator_kclka = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        # setup
        self.setup_connections()
        self.get_port()
        self.ui.stackedWidget.setCurrentIndex(0)

    def setup_connections(self):
        try:
            self.ui.pb_refresh.clicked.connect(self.get_port)
            self.ui.pb_connect.clicked.connect(self.toggle_connection)
            self.ui.pb_KCLKA.clicked.connect(self.goto_page_kclka)
            self.ui.pb_LIDA.clicked.connect(self.goto_page_lida)
            self.ui.pb_lokator1.clicked.connect(self.handle_btn_input1)
            self.ui.pb_lokator2.clicked.connect(self.handle_btn_input2)
            
            
        except Exception as e:
            print(f"⚠️  Connection setup error: {e}")

    def get_port(self):
        self.port = self.system.get_serial_ports()
        print(f"port detek = {self.port}")

        if not self.port:
            print("⚠️ Tidak ada port terdeteksi atau fungsi return None")
            self.port = []

        self.ui.select_port.clear()
        self.ui.select_port.setMaxVisibleItems(6)
        self.ui.select_port.addItems(self.port)

    def toggle_connection(self):
        """Connect/Disconnect toggle button"""
        if not self.system.is_connected():
            # Connect
            selected_port = self.ui.select_port.currentText()
            if not selected_port:
                print("Please select a port")
                return

            if self.system.connect_serial(selected_port, baudrate=115200):
                self.system.start_reading()
                self.ui.pb_connect.setText("Disconnect")
                self.ui.pb_connect.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                self.ui.select_port.setEnabled(False)  # Disable port selection
            else:
                print("❌ Connection failed")
        else:
            # Disconnect
            current_port = self.system.get_current_port()
            self.system.disconnect_serial()
            self.ui.pb_connect.setText("Connect")
            self.ui.pb_connect.setStyleSheet("background-color: green; color: white; font-weight: bold;")
            print(f"Disconnected from {current_port}")
            self.ui.select_port.setEnabled(True)  # Enable port selection

    def goto_page_kclka(self):
        """Pindah ke page dengan index tertentu"""
        try:
            self.lida_state = False
            self.kclka_state = True
            self.ui.stackedWidget.setCurrentIndex(1)
            print(f"Switched to page kclka")

        except Exception as e:
            print(f"Error switching page: {e}")

    def goto_page_lida(self):
        """Pindah ke page dengan index tertentu"""
        try:
            self.lida_state = True
            self.kclka_state = False
            self.ui.stackedWidget.setCurrentIndex(0)
            print(f"Switched to page lida")

        except Exception as e:
            print(f"Error switching page: {e}")
    
    def get_locator_lida(self):
        
        locator_lida = {
            1: [self.ui.Input_X2L_P1_LIDA, self.ui.Input_X1L_P1_LIDA, self.ui.Input_X1R_P1_LIDA],
            2: [self.ui.Input_X2L_P2_LIDA, self.ui.Input_X1L_P2_LIDA, self.ui.Input_X1R_P2_LIDA],
            3: [self.ui.Input_X2L_P3_LIDA, self.ui.Input_X1L_P3_LIDA, self.ui.Input_X1R_P3_LIDA],
            4: [self.ui.Input_X2L_P4_LIDA, self.ui.Input_X1L_P4_LIDA, self.ui.Input_X1R_P4_LIDA],
            5: [self.ui.Input_X2L_P5_LIDA, self.ui.Input_X1L_P5_LIDA, self.ui.Input_X1R_P5_LIDA],
            6: [self.ui.Input_X2L_P6_LIDA, self.ui.Input_X1L_P6_LIDA, self.ui.Input_X1R_P6_LIDA]
        }
        
        for nomor, edits in locator_lida.items():
            self.locator_lida[nomor] = [int(edit.text())*10 for edit in edits]  # ambil semua nilai di baris
        # print(self.locator_lida)  # contoh: {1: ['0', '0', '0'], 2: [...], ...}
        result = self.calc.lida_locator(self.locator_lida)
        return result
        
    
    def get_locator_kclka(self):
        locator_kclka = {
            1: self.ui.Input_X1_P1_KCLKA,
            2: self.ui.Input_X1_P2_KCLKA,
            3: self.ui.Input_X1_P3_KCLKA,
            4: self.ui.Input_X1_P4_KCLKA,
            5: self.ui.Input_X1_P5_KCLKA,
            6: self.ui.Input_X1_P6_KCLKA,
        }
        
        for nomor, edit in locator_kclka.items():
            self.locator_kclka[nomor] = int(edit.text())  # ambil semua nilai di baris
        # print(self.locator_kclka)  # contoh: {1: ['0', '0', '0'], 2: [...], ...}
        result = self.calc.kclka_locator(self.locator_kclka)
        # print(result)
        return result
        
                
    def emit_signal(self, data):
        """Emit signal dari thread (thread-safe)"""
        self.signal_handler.data_received.emit(data)

    def handle_serial_data(self, data):
        """Callback function untuk handle data dari serial (dipanggil dari thread)"""
        print(f"data = {data}")

        try:
            if "#" in data:
                values = data.split("#")

                if len(values) == 3:
                    self.ui.encoder_value.setText(values[0].strip())
                    self.ui.kondisi_value.setText(values[1].strip())
                    self.ui.dac_value.setText(values[2].strip())

        except Exception as e:
            print(f"❌ Parsing error: {e}")
    def handle_btn_input1(self):
        if self.lida_state:
            data = self.get_locator_lida().strip()
            print(data)
            self.send_data("update_all", data)
        elif self.kclka_state:
            data = self.get_locator_kclka().strip()
            print(data)
            self.send_data("update_all",data)
            
    def handle_btn_input2(self):
        data = self.ui.locator_value.text()
        if not data:
            return
        print(f"data terinput {data}")
        self.send_data("e", data)

    def send_data(self,action, data):
        """Send data ke serial port"""
        # data = self.ui.locator_value.text().strip()
        if not data:
            return
        if self.system.send_data(f"{action} {data}\n"):  # Add newline
            print(f"Sent: {data}")
        else:
            print("❌ Send failed - not connected")

    def closeEvent(self, event):
        """Cleanup saat aplikasi ditutup"""
        if self.system.is_connected():
            self.system.disconnect_serial()
        event.accept()
