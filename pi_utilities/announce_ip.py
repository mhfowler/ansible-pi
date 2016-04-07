import socket
import time
import subprocess
import re

from pi_utilities.slack_helper import slack_notify_message


def announce_ip():
    index = 0
    while index < 200:
        print '++ attempting to announce ip: {}'.format(index)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("gmail.com",80))
            ip_address = s.getsockname()[0]
            s.close()
            slack_notify_message('@channel: its pi: {}'.format(ip_address))
            iwget = subprocess.check_output('iwgetid', shell=True)
            slack_notify_message('iwget: {}'.format(iwget))
            return
        except Exception as e:
            pass
        index += 1
        time.sleep(1)



if __name__ == '__main__':
    announce_ip()