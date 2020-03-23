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
         if(not self.end):
            #Calculate Time
            self.total_time = time.time() - self.time_start
 
            #Calculate Accuracy
            count = 0
            for i,c in enumerate(self.word):
               try:
                  if self.input_text[i] == c:
                     count += 1
               except:
                  pass
            self.accuracy = count/len(self.word)*100
            
            #Calculate WPM
            self.WPM = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time:'+str(round(self.total_time)) +" secs Accuracy:"+ str(round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))
            
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
         self.screen.blit(self.open_img, (0,0))

         pygame.display.update()
         time.sleep(1)

         self.reset=False
         self.end=False

         self.input_text=''
         self.word = ''
         self.word_start = 0 
         self.total_time = 0
         self.wpm = 0

         self.word = self.get_sentence()
         if (not self.word) : self.reset_game()

         self.screen.fill((0,0,0))
         self.screen.blit(self.background,(0,0))
         msg = ""
         self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)

         pygame.draw.rect(self.screen,(255,192,25),(50,250,650,50),2)

         self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C)

         pygame.display.update()



Game().run()
