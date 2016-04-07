import socket
import time
import subprocess
from wireless import Wireless

from pi_utilities.slack_helper import slack_notify_message
from hello_settings import SECRETS_DICT


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


def announce_ip():
    index = 0
    wireless = Wireless()
    while index < 200:
        print '++ attempting to announce ip: {}'.format(index)
        try:
            current_connection = wireless.current()
            if current_connection:
                slack_notify_message('warning: was already connected to network: {}'.format(current_connection))
            connected = wireless.connect(ssid=SECRETS_DICT['WIFI_SSID'], password=SECRETS_DICT['WIFI_PASSWORD'])
            if not connected:
                raise Exception('failed to connect')
            else:
                ip_address = get_ip()
                current_connection = wireless.current()
                slack_notify_message('@channel: its pi: {} | {}'.format(ip_address, current_connection))
            try:
                slack_notify_message('++ logging  info')
                ifconfig = subprocess.check_output('ifconfig', shell=True)
                slack_notify_message('ifconfig: {}'.format(ifconfig))
                iwget = subprocess.check_output('iwgetid', shell=True)
                slack_notify_message('iwget: {} | {}'.format(iwget, get_ip()))
                return
            except Exception as e:
                slack_notify_message('warning: failed to log all detailed info')
            return
        except Exception as e:
            pass
        index += 1
        time.sleep(1)



if __name__ == '__main__':
    announce_ip()