import atomicpi
import gpio as GPIO
from time import sleep

# Control by signal ID
GPIO_0=atomicpi.signals.ISH_GPIO_0.global_idx # Enable A
GPIO.setup(GPIO_0, GPIO.OUT)
GPIO_1=atomicpi.signals.ISH_GPIO_1.global_idx # Enable B
GPIO.setup(GPIO_1, GPIO.OUT)
GPIO_2=atomicpi.signals.ISH_GPIO_2.global_idx # INPUT 1
GPIO.setup(GPIO_2, GPIO.OUT)
GPIO_3=atomicpi.signals.ISH_GPIO_3.global_idx # INPUT 2
GPIO.setup(GPIO_3, GPIO.OUT)
GPIO_4=atomicpi.signals.ISH_GPIO_4.global_idx # INPUT 3
GPIO.setup(GPIO_4, GPIO.OUT)
GPIO_7=atomicpi.signals.ISH_GPIO_7.global_idx # INPUT 4
GPIO.setup(GPIO_7, GPIO.OUT)

INPUT_1=GPIO_2
INPUT_2=GPIO_3
INPUT_3=GPIO_4
INPUT_4=GPIO_7
ENABLE_A=GPIO_0
ENABLE_B=GPIO_1

GPIO.output(GPIO_0, True)
GPIO.output(GPIO_1, True)
GPIO.output(GPIO_2, True)
GPIO.output(GPIO_3, True)
GPIO.output(GPIO_4, True)
GPIO.output(GPIO_7, True)