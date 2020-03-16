import pygame, time, random, sys
from pygame.locals import *

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

      pygame.init()
      self.screen = pygame.display.set_mode((self.w,self.h))
      pygame.display.set_caption('typefast')

      def draw_text(self,screen,msg,y,fsize,color):
         font = pygame.font.Font(None, fsize)
         text = font.render(msg,i,color)
         text_rect = text.get_rect(center=(self.w/2,y))
         screen.blit(text, text_rect)
         pygame.display.update()

      def get_sentence(self):
         f = open('meningar.txt').read()
         sentences = f.split('\n')
         sentence = random.choice(sentences)
         return sentence

      def show_results(self, screen):
         #Calculate Time
         #Calculate Accuracy
         #Calculate WPM


      def run(self):
         self.reset_game()

         self.running=True
         while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0),(50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C,(50,250,650,50), 2)

            self.draw_text(self.screen, self.input_text, 274, 26, (250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
               if event.type == QUIT:
                  self.running = False
                  sys.exit()
               elif event.type == pygame.MOUSEBUTTONUP:
                  x,y = pygame.mouse.get_pos()
        
      def reset_game():
         
