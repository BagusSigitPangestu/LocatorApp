import serial
import serial.tools.list_ports
from threading import Thread
import time

class SerialProcess:
    def __init__(self, callback=None):
        self.ser = None
        self.thread = None
        self.is_reading = False
        self.callback = callback  # Callback function untuk mengirim data ke UI
        
    # Fungsi mendapatkan daftar port serial yang tersedia
    def get_serial_ports(self):
        try:
            ports = serial.tools.list_ports.comports()
            return [port.device for port in ports]
        except Exception as e:
            print(f"Error getting serial ports: {e}")
            return []
    
    # Fungsi menghubungkan ke port serial
    def connect_serial(self, port, baudrate=115200, timeout=1):
        try:
            if self.ser and self.ser.is_open:
                self.disconnect_serial()
            
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
            print(f"Connected to {port} at {baudrate} baud")
            return True
            
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    # Fungsi memutuskan koneksi serial
    def disconnect_serial(self):
        try:
            self.stop_reading()
            if self.ser and self.ser.is_open:
                self.ser.close()
                print("Serial connection closed")
                return True
        except Exception as e:
            print(f"Disconnect error: {e}")
            return False
    
    # Fungsi mengirim data ke serial
    def send_data(self, data):
        try:
            if self.ser and self.ser.is_open:
                if isinstance(data, str):
                    data = data.encode('utf-8')
                    print(f"data terkirim = {data}")
                self.ser.write(data)
                return True
            else:
                print("Serial port not connected")
                return False
        except Exception as e:
            print(f"Send error: {e}")
            return False
    
    # Fungsi membaca data dari serial
    def read_serial(self):
        while self.is_reading:
            try:
                if self.ser and self.ser.is_open and self.ser.in_waiting:
                    data = self.ser.readline().decode('utf-8').strip()
                    if data and self.callback:
                        self.callback(data)  # Kirim data ke callback function
                        
                time.sleep(0.01)  # Small delay to prevent excessive CPU usage
                
            except Exception as e:
                print(f"Read error: {e}")
                if self.callback:
                    self.callback(f"Error: {e}")
                break
    
    # Fungsi menjalankan pembacaan serial dalam thread terpisah
    def start_reading(self):
        if not self.is_reading:
            self.is_reading = True
            self.thread = Thread(target=self.read_serial, daemon=True)
            self.thread.start()
            print("Started reading serial data")
    
    # Fungsi menghentikan pembacaan serial
    def stop_reading(self):
        self.is_reading = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1)  # Wait max 1 second for thread to finish
            print("Stopped reading serial data")
    
    # Fungsi mengecek status koneksi
    def is_connected(self):
        return self.ser and self.ser.is_open
    
    # Fungsi mendapatkan info port yang sedang digunakan
    def get_current_port(self):
        if self.ser and self.ser.is_open:
            return self.ser.port
        return None
    
    # Destruktor untuk cleanup
    def __del__(self):
        self.disconnect_serial()


# Example usage (untuk testing):
if __name__ == "__main__":
    def test_callback(data):
        print(f"Callback received: {data}")
    
    # Create serial instance
    serial_comm = SerialProcess(callback=test_callback)
    
    # Test get ports
    ports = serial_comm.get_serial_ports()
    print(f"Available ports: {ports}")
    
    # Test connection (uncomment to test with actual hardware)
    # if ports:
    #     success = serial_comm.connect_serial(ports[0])
    #     if success:
    #         serial_comm.start_reading()
    #         # Test send data
    #         serial_comm.send_data("Hello Serial!")
    #         time.sleep(5)  # Read for 5 seconds
    #         serial_comm.disconnect_serial()