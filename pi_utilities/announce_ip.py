import socket
import time
import subprocess

from pi_utilities.slack_helper import slack_notify_message


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


def announce_ip():
    index = 0
    while index < 200:
        print '++ attempting to announce ip: {}'.format(index)
        try:
            ip_address = get_ip()
            slack_notify_message('@channel: its pi: {}'.format(ip_address))
            while index < 200:
                try:
                    iwget = subprocess.check_output('iwgetid', shell=True)
                    slack_notify_message('iwget: {} | {}'.format(iwget, get_ip()))
                    return
                except Exception as e:
                    index += 1
                    time.sleep(1)
            return
        except Exception as e:
            pass
        index += 1
        time.sleep(1)



if __name__ == '__main__':
    announce_ip()