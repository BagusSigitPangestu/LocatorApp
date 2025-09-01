import os
import sys
import subprocess
import shutil
from pathlib import Path

def clean_previous_build():
    """Hapus build sebelumnya"""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Cleaned {dir_name} directory")

def build_executable():
    """Build executable dengan PyInstaller"""
    # Pindah ke root directory (parent dari build_scripts)
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print(f"Building dari directory: {project_root}")
    print("🔨 Memulai build executable...")
    
    # Perintah PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # Tanpa console window
        "--name=LocatorApp",           # Nama executable
        "--clean",                      # Bersihkan cache
        
        # Hidden imports untuk modules Anda
        "--hidden-import=modules.calculate_locator",
        "--hidden-import=modules.gui_controller", 
        "--hidden-import=modules.interface",
        "--hidden-import=modules.serial_process",
        
        # Main script
        "main.py"
    ]
    
    try:
        # Jalankan PyInstaller
        print("Menjalankan PyInstaller...")
        result = subprocess.run(cmd, check=True)
        
        print("\n✅ Build berhasil!")
        print(f"📁 Executable tersimpan di: {project_root}/dist/LocatorApp.exe")
        
        # Tampilkan ukuran file
        exe_path = project_root / "dist" / "LocatorApp.exe"
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"📊 Ukuran file: {size_mb:.1f} MB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build gagal: {e}")
        print("\nTroubleshooting:")
        print("1. Pastikan semua dependencies terinstall")
        print("2. Pastikan main.py ada di root directory")
        print("3. Check apakah ada error di aplikasi")
        return False

def test_imports():
    """Test apakah semua modules bisa diimport"""
    print("🔍 Testing imports...")
    
    # Pindah ke project root directory dan tambahkan ke Python path
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    sys.path.insert(0, str(project_root))
    
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"📁 Project root: {project_root}")
    
    modules_to_test = [
        "PySide6.QtWidgets",
        "modules.calculate_locator", 
        "modules.gui_controller",
        "modules.interface",
        "modules.serial_process"
    ]
    
    failed_imports = []
    
    for module in modules_to_test:
        try:
            __import__(module)
            print(f"✓ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️  {len(failed_imports)} module(s) gagal diimport")
        print("Perbaiki import errors sebelum build")
        return False
    else:
        print("✅ Semua imports berhasil!")
        return True

def main():
    print("🚀 LocatorApp Build Script")
    print("=" * 40)
    
    # Test imports dulu
    if not test_imports():
        return
    
    # Konfirmasi build
    # print(f"\nProject directory: {Path(__file__).parent.parent}")
    # confirm = input("Mulai build? (y/n): ").lower().strip()
    
    # if confirm != 'y':
    #     print("Build dibatalkan.")
    #     return
    
    # Bersihkan build sebelumnya
    clean_previous_build()
    
    # Build executable
    success = build_executable()
    
    if success:
        print("\n🎉 Build selesai!")
        # print("\n📋 Langkah selanjutnya:")
        # print("1. Test executable di folder dist/")
        # print("2. Test di komputer lain (tanpa Python)")
        # print("3. Buat installer jika diperlukan")
    else:
        print("\n❌ Build gagal. Periksa error di atas.")

if __name__ == "__main__":
    main()