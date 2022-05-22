import sys
import subprocess
import time

iterations = 100     # by conditions
timeFlag = time.time()  # epoch time

for _ in range(iterations):
    subprocess.Popen([sys.executable, 'D:\\PyCharm 2021.2\\PycharmProjects'
                                      '\\pythonProject\\uni_programs\\yaml_to_xml\\main\\mainCode.py'])
print(time.time() - timeFlag)
timeFlag = time.time()

for _ in range(iterations):
    subprocess.Popen([sys.executable, 'D:\\PyCharm 2021.2\\PycharmProjects'
                                      '\\pythonProject\\uni_programs\\yaml_to_xml\\lib_with\\libCode.py'])
print(time.time() - timeFlag)
timeFlag = time.time()

for _ in range(iterations):
    subprocess.Popen([sys.executable, 'D:\\PyCharm 2021.2\\PycharmProjects'
                                      '\\pythonProject\\uni_programs\\yaml_to_xml\\reg_with\\regCode.py'])
print(time.time() - timeFlag)
