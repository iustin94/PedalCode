#!/usr/bin/env python3
import serial
from evdev import UInput, AbsInfo, ecodes

capabilities = {
    ecodes.EV_ABS: [
        (ecodes.ABS_Z,  AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0)),
        (ecodes.ABS_RZ, AbsInfo(value=0, min=0, max=255, fuzz=0, flat=0, resolution=0)),
    ],
    ecodes.EV_KEY: [
        ecodes.BTN_JOYSTICK,
    ],
}

device = UInput(
    events=capabilities,
    name="Arduino Foot Pedal",
    vendor=0x0001,
    product=0x0001,
    bustype=ecodes.BUS_USB,
)

print(f"Created virtual joystick: {device.device.path}")
print("Use this event device path in your Steam launch options:")
print(f'  SDL_JOYSTICK_DEVICE={device.device.path} WINEDLLOVERRIDES="dinput8=n,b" %command%')

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

prev_a = False
prev_b = False

while True:
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    if len(line) != 2:
        continue

    a = line[0] == "1"
    b = line[1] == "1"

    if a != prev_a:
        device.write(ecodes.EV_ABS, ecodes.ABS_Z, 255 if a else 0)
        device.syn()
        prev_a = a
    if b != prev_b:
        device.write(ecodes.EV_ABS, ecodes.ABS_RZ, 255 if b else 0)
        device.syn()
        prev_b = b
