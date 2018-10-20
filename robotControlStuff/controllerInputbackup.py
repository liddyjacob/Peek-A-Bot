import bluetooth
import keyboard #Using module keyboard
import serial
import pygame
from pygame.locals import *

decices = bluetooth.discover_devices()
ser = serial.Serial("/dev/rfcomm0", 9600)

pygame.init()
screen = pygame.display.set_mode((600,400))

speed = 0;

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				ser.write('<L,255>')
				ser.write('<R,255>')
			elif event.key == K_a:
				ser.write('<L,-188>')
				ser.write('<R,188>')
			elif event.key == K_d:
				ser.write('<L,188>')
				ser.write('<R,-188>')
			elif event.key == K_s:
				ser.write('<L,-255>')
				ser.write('<R,-255>')
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				ser.write('<L,0>')
				ser.write('<R,0>')
			elif event.key == K_a:
				ser.write('<L,0>')
				ser.write('<R,0>')
			elif event.key == K_s:
				ser.write('<L,0>')
				ser.write('<R,0>')
			elif event.key == K_d:
				ser.write('<L,0>')
				ser.write('<R,0>')
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)