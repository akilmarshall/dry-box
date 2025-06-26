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
- power mosfets or suitable solid state device to control fan heat and bed heat with a pwm signal
- second intake fan
- use full H-bridge to control intake fan:
    - bi-directional airflow control
- hot bed temperature sensor
- lid open/close sensor
- insulated box

## Components

2 heated fans + heat bed = 460W

- [SHT31-D](https://www.adafruit.com/product/2857):
    - i2c address can be changed so two devices can be on one i2c bus
- Intake Fan with Heater:
    - 12V DC (8.33A)
    - PTC: 12V AC/DC
    - POWER: 100W
    - SKU: JYA01663
- H-Bridge DC Speed Controller:
    - L298N
- Heat Bed:
    - 24V DC
    - POWER: 260W
- [N-channel power MOSFET](https://www.adafruit.com/product/355):
    - switch 30V/60A
- ATX power supply:
    - 500W
- 12V to 24V Dc Dc Converter

## Future Schematic

<img src="schematic/v2.svg" alt="filament dry box v1 schematic"/>

