import click
import random
import socket
import time

ROUTER_HOST = "localhost"
ROUTER_PORT = 9340


def random_mac_address():
    mac_addresss = "01:00:00"
    choices = "0123456789abcdef"
    for _ in range(3):
        mac_addresss += ":{}{}".format(*random.choices(choices, k=2))
    return mac_addresss

def random_client_ip():
    ip_addresss = ''
    for _ in range(4):
        ip_addresss += f"{(random.randint(0, 254))}."
    return ip_addresss[:-1]


@click.command()
@click.option("--ip-addr", help="IP address")
@click.option("--mac-addr", help="MAC address")
def main(ip_addr, mac_addr):
    if not mac_addr:
        mac_addr = random_mac_address()
    if not ip_addr:
        ip_addr = random_client_ip()

    click.echo(f"Using MAC address: {mac_addr}")
    click.echo(f"Using IP address: {ip_addr}")

    router = (ROUTER_HOST, ROUTER_PORT)
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(random.randint(1, 3))
    client1.connect(router)

if __name__ == "__main__":
    main()