import subprocess

broken = subprocess.run(['pip', 'check'], capture_output=True)
with open('broken.txt', 'wb') as f:
    f.write(broken.stdout)
    f.write(broken.stderr)


installed = subprocess.check_output(['pip', 'list'])
with open('installed.txt', 'wb') as f:
    f.write(installed)

requirements = subprocess.check_output(['pip', 'freeze'])
with open('requirements.txt', 'wb') as f:
    f.write(requirements)

sklearninfo=subprocess.check_output(['pip', 'show', 'scikit-learn'])
with open('sklearninfo.txt', 'wb') as f:
    f.write(sklearninfo)

