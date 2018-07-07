import importlib
import os
import shutil
import subprocess
import sys
import time
import zipfile

# Prepare zip files
uploads = []
for upload_file in os.listdir("./uploads"):
    if upload_file.endswith(".zip"):
        uploads.append(upload_file)

# Prepare screenshots
screenshots = []
for screenshot in os.listdir("./pictures"):
    if screenshot.endswith(".png"):
        screenshots.append(screenshot)

# Loop over every student
for upload_file in uploads:
    with zipfile.ZipFile("./uploads/" + upload_file, "r") as zip_ref:
        zip_ref.extractall(".")

    # Check file structure
    student_id = upload_file[:upload_file.index('.')]
    if os.path.isdir('./' + student_id + '/python'):
        lang = 'python'
        work_dir = './' + student_id + '/python'
    elif os.path.isdir('./' + student_id + '/matlab'):
        lang = 'matlab'
        work_dir = './' + student_id + '/matlab'
    elif os.path.isdir('./' + student_id + '/cpp'):
        lang = 'cpp'
        work_dir = './' + student_id + '/cpp'
    else:
        print('Broken upload structure! Exiting...')
        exit()

    # Check test platform
    platform = sys.platform
    if platform != "win32" and platform != "darwin":
        print("Unsupported platform. Exiting...")
        exit()

    # Check source files
    engine = None
    if lang == "matlab":
        if not os.path.isfile(work_dir + '/jumper.m'):
            print('Source code does not exist! Exiting...')
            exit()
        import matlab.engine
        engine = matlab.engine.start_matlab()
        engine.addpath(work_dir)
    elif lang == "python":
        if not os.path.isfile(work_dir + '/jumper.py'):
            print('Source code does not exist! Exiting...')
            exit()
        for f in os.listdir(work_dir):
            shutil.copy(work_dir + '/' + f, './' + student_id)
        jumper = importlib.import_module(student_id + '.jumper')
    else:
        if platform == "win32":
            if not os.path.isfile(work_dir + '/jumper.exe'):
                print('Executable file does not exist! Exiting...')
                exit()
        if platform == "darwin":
            if not os.path.isfile(work_dir + '/jumper'):
                print('Executable file does not exist! Exiting...')
                exit()

    # Begin test
    start_time = time.time()
    error_in_total = 0
    for screenshot in screenshots:
        shutil.copy2('./pictures/' + screenshot, work_dir + '/autojump.png')
        original_distance = screenshot.split('_')[2]
        calculated_distance = 0
        if lang == "python":
            os.chdir(work_dir)
            calculated_distance = jumper.jumper()
            os.chdir('../../')
        elif lang == "cpp":
            if platform == "win32":
                calculated_distance = subprocess.getoutput(
                    'cd ' + work_dir + ' && jumper.exe')
            if platform == "darwin":
                calculated_distance = subprocess.getoutput(
                    'cd ' + work_dir + ' && ./jumper')
        else:
            calculated_distance = engine.jumper()

        error = abs(int(calculated_distance) - int(original_distance))
        error_in_total = error_in_total + error

    # Print mean error
    mean_error = error_in_total / len(screenshots)
    print(student_id + ' mean distance error ' + str(mean_error) +
          ' executed in ' + str(round(time.time() - start_time, 2)) + 's')

    # Remove temp dir
    shutil.rmtree(student_id)
