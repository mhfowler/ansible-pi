import socket
import time
import subprocess
from wireless import Wireless

from pi_utilities.slack_helper import slack_notify_message
from hello_settings import SECRETS_DICT


USE_PYTHON_TO_CONNECT = False
LOG_DETAILED_INFO = True


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
            current_connection = wireless.current()
            print '++ found ip_address: {}'.format(str(ip_address))
            print '++ found current_connection: {}'.format(str(current_connection))
            routes = subprocess.check_output('route -n', shell=True)
            print '++ routes'
            print routes
            print '++ endroutes'
            if ip_address:
                slack_notify_message('@channel: its pi: {} | {}'.format(str(ip_address), str(current_connection)))
                break
            # else try to connect
            if USE_PYTHON_TO_CONNECT:
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
    if LOG_DETAILED_INFO:
        try:
            print '++++ logging detailed info'
            ifconfig = subprocess.check_output('ifconfig', shell=True)
            print 'ifconfig: {}'.format(ifconfig)
            iwget = subprocess.check_output('iwgetid', shell=True)
            print 'iwget: {} | {}'.format(iwget, get_ip())
        except Exception as e:
            print 'warning: failed to log detailed info: {}'.format(e.message)


if __name__ == '__main__':
    announce_ip()