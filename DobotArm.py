from serial.tools import list_ports
import pydobot

def control_dobot(port_name="COM4", num_iterations=2):
    available_ports = list_ports.comports(port_name)
    print(f'Available ports: {[x.device for x in available_ports]}')

    if not available_ports:
        raise Exception("No Dobot found on the specified port.")

    port = available_ports[0].device
    device = pydobot.Dobot(port=port, verbose=True)

    (x, y, z, r, j1, j2, j3, j4) = device.pose()
    print(f'x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

    for _ in range(num_iterations):
        device.move_to(x + 70, y, z, r, wait=True)
        device.wait(1000)
        device.move_to(x, y, z, r, wait=True)
        device.wait(1000)

    device.close()
