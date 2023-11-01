import sys
import subprocess

def die(exit_code, msg):
    if msg:
        if not msg.endswith("\n"):
            msg += "\n"
        sys.stderr.write(msg)
        sys.stderr.flush()
    sys.exit(exit_code)


def run_command(cmd, die_if_fail=False):
    try:
        subprocess.check_call(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True)
    except:
        if die_if_fail:
            die(-1, None)
