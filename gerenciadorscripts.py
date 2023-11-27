import subprocess
import time
import threading


def executar_script(script):
    subprocess.run(["python", script])

scripts = ["gerador_dados.py", "extrator_dados.py", "movearq.py"]


while True:
    theads = []

    for script in scripts:
        thread = threading.Thread(target=executar_script, args=(script,))
        theads.append(thread)
        thread.start()

    for thread in theads:
        thread.join()
    
    time.sleep(1)