import socket
import time
import subprocess
from wireless import Wireless

from pi_utilities.slack_helper import slack_notify_message
from hello_settings import SECRETS_DICT


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except:
        return None


def announce_ip():
    index = 0
    wireless = Wireless()
    while index < 200:
        print '++ attempting to announce ip: {}'.format(index)
        try:
            ip_address = get_ip()
            print '++ found ip_address: {}'.format(str(ip_address))
            if ip_address:
                current_connection = wireless.current()
                print '++ found current_connection: {}'.format(current_connection)
                slack_notify_message('@channel: its pi: {} | {}'.format(str(ip_address), str(current_connection)))
                break
            # else try to connect
            print '++ trying to connect'
            connected = wireless.connect(ssid=SECRETS_DICT['WIFI_SSID'], password=SECRETS_DICT['WIFI_PASSWORD'])
            if not connected:
                print ':-( failed to connect'
            else:
                print ':) connected'
        except Exception as e:
            print ':/ error: {}'.format(str(e.message))
            pass
        index += 1
        time.sleep(1)
    # after we have connected, log some info about the connection
    LOG_DETAILED_INFO = True
    if LOG_DETAILED_INFO:
        try:
            slack_notify_message('++ logging detailed info')
            ifconfig = subprocess.check_output('ifconfig', shell=True)
            slack_notify_message('ifconfig: {}'.format(ifconfig))
            iwget = subprocess.check_output('iwgetid', shell=True)
            slack_notify_message('iwget: {} | {}'.format(iwget, get_ip()))
            return
        except Exception as e:
            slack_notify_message('warning: failed to log all detailed info')


if __name__ == '__main__':
    announce_ip()