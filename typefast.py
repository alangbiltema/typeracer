import pygame
from pygame.locals import *
import time
import random
import sys


class Game:

     def __init__(self):
        self.w=750
        self.h=500
        self.reset=True
        self.active = False
        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)

        pygame.init():
        



        def draw_text(self,screen,msg,y,fsize,color):
           font = pygame.font.Font(None, fsize)
           text = font.render(msg,i,color)
           text_rect = text.get_rect(center=(self.w/2,y))
           screen.blit(text, text_rect)
           pygame.display.update()
