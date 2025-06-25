<img src="schematic/v1.svg" alt="filament dry box v1 schematic"/>

# Components

- Intake Fan with Heater:
    - 12V DC (8.33A)
    - PTC: 12V AC/DC
    - POWER: 100W
    - SKU: JYA01663
- Microcontroller:
    - ESP32 WROOM with OLED
- Dual Channel Relay:
    - HL-52S
- H-Bridge DC Speed Controller:
    - L298N
- Environment sensor:
    - SHT21 
- Heat Bed:
    - 24V DC
    - POWER: 260W
- DC/DC Converter:
    - 24V to 12V 10A
- Power Supply AC to DC:
    - LRS 350 24

# Control


The heat bed and fan heat and powered via relays and thus primary can be turned on or off.
Esphome "slow pwm" has been used to allow control of the heating elements via a pwm signal.

The intake fan speed is controlled with half of an H-bridge and there for is controlled via a PWM signal.

All of these devices are controlled together with a PID controller to control the interior temperature according to the enviroment sensor.


# Wish List

- external environment sensor
- power mosfets or suitable device to control fan heat and bed heat with a pwm signal
- second fan diagonal opposite the existing intake fan
- use full H-bridge to control intake fan
- hot bed temperature sensor
- lid open/close sensor
