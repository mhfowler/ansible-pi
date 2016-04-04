import socket

from pi_utilities.slack_helper import slack_notify_message


def announce_ip():
    print '++ attempting to announce ip'
    slack_notify_message('its pi')
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(("gmail.com",80))
    # ip_address = s.getsockname()[0]
    # s.close()


if __name__ == '__main__':
    announce_ip()