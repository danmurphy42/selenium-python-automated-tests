import sys
import os
import shutil
import subprocess
from dotenv import load_dotenv
load_dotenv()


# Run this file with the directory name of your suite (e.g. "editortests") as a command line argument to run an indivudal
# suite, or "all" to run all suites in the repo. e.g. "python3 helpers/suite_runner.py all"

def gather_env_vars():
    if os.getenv('SANDBOX') is None or os.getenv('EDITOR_USERNAME') is None or os.getenv('EDITOR_PW') is None:
        sandbox_input = input('Which sandbox are you testing in? (qa1, qa2, qa3, etc.)\n')
        os.environ['SANDBOX'] = sandbox_input
        editor_username = input('Editor username:\n')
        os.environ['EDITOR_USERNAME'] = editor_username
        editor_pw = input('Editor password:\n')
        os.environ['EDITOR_PW'] = editor_pw


def clear_existing_screenshots():
    if os.path.exists('./tmp/screenshots') is True:
        shutil.rmtree('./tmp/screenshots')


test_suite = sys.argv[1]


def suite_runner():
    if test_suite == 'all':
        clear_existing_screenshots()
        gather_env_vars()
        subprocess.run(['python3', '-m', 'pytest', 'testcases/', '--junitxml=junitreport.xml'])
    else:
        gather_env_vars()
        subprocess.run(['python3', '-m', 'pytest', 'testcases/' + test_suite, '--junitxml=junitreport.xml'])


suite_runner()
