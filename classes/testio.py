import socket


def available_port(host_ip='127.0.0.1', port=80):
    """
    Check if a given port is open on a host.

    :param host_ip: host to check
    :param port: port to check
    :return: True if port is open
    """

    s = socket.socket()
    try:
        s.connect((host_ip, int(port)))
        s.close()
        return False
    except socket.error, e:
        return True


