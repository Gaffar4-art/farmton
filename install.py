import subprocess
import sys

# قائمة المكاتب المطلوبة
required_libraries = [
    "requests",
    "colorama",
    "backoff",
    "rich"
]

# تثبيت كل مكتبة إن لم تكن مثبتة بالفعل
for lib in required_libraries:
    try:
        __import__(lib)
        print(f"[✓] Library '{lib}' is already installed.")
    except ImportError:
        print(f"[!] Installing '{lib}'...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])