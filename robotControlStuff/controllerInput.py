import bluetooth
import keyboard #Using module keyboard
import serial
import pygame
from pygame.locals import *
import time

decices = bluetooth.discover_devices()
ser = serial.Serial("/dev/rfcomm0", 9600)

pygame.init()
screen = pygame.display.set_mode((600,400))

Lspeed = 0
Rspeed = 0

while True:
	time.sleep(1./25)
	ser.write('<L,' + str(Lspeed) + '>')
	ser.write('<R,' + str(Rspeed) + '>')
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				Lspeed += 255
				Rspeed += 255
			if event.key == K_a:
				Lspeed -= 255
			if event.key == K_d:
				Rspeed -= 255
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				Lspeed -= 255
				Rspeed -= 255
			if event.key == K_a:
				Lspeed += 255
			if event.key == K_d:
				Rspeed += 255
				
		if event.type == pygame.QUIT:
			Lspeed = 0
			Rspeed = 0
			pygame.quit()
			exit(0)