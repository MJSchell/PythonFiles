import subprocess
import sys

installs = ["gspread", "gspread-formatting",
            "qrcode", "Pillow", "opencv-python"]


for i in installs:
    subprocess.check_call([sys.executable, "-m", "pip", "install", i])
subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "-U", "numpy"])
subprocess.check_call(
    [sys.executable, "sudo", "apt-get", "install", "libatlas-base-dev"])