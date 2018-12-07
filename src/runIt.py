import subprocess

script = ["python2.7", "PrintQRCode.py"]
process = subprocess.Popen(" ".join(script),
                                        shell=True,
                                        env={"PYTHONPATH": "."})