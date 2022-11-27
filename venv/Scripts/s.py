import pygame
from main import *
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
 
 
# class Button:
#     """Create a button, then blit the surface in the while loop"""
 
#     def __init__(self, text,  pos, font, bg="black", feedback=""):
#         self.x, self.y = pos
#         self.font = pygame.font.SysFont("Arial", font)
#         if feedback == "":
#             self.feedback = "text"
#         else:
#             self.feedback = feedback
#         self.change_text(text, bg)
 
#     def change_text(self, text, bg="black"):
#         """Change the text whe you click"""
#         self.text = self.font.render(text, 1, pygame.Color("White"))
#         self.size = self.text.get_size()
#         self.surface = pygame.Surface(self.size)
#         self.surface.fill(bg)
#         self.surface.blit(self.text, (0, 0))
#         self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
#     def show(self):
#         screen.blit(button1.surface, (self.x, self.y))
 
#     def click(self, event):
#         x, y = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pressed()[0]:
#                 if self.rect.collidepoint(x, y):
#                     self.change_text(self.feedback, bg="red")
 




base=Base()
def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #     button1.click(event)
        # button1.show()

        base.drawBase()
        # for event in pygame.event.get():
            # base.slide()
            # if pygame.BUTTON_RIGHT or event==pygame.K_DOWN:
        base.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and base.rect.left > 0:
            base.x -= base.speed
            base.direction = -1
        if key[pygame.K_1] and base.rect.right < windowWidth:
            base.x += base.speed
            base.direction = 1





        clock.tick(30)
        pygame.display.update()
 
 
# button1 = Button(
#     "Click here",
#     (100, 100),
#     font=30,
#     bg="navy",
#     feedback="You clicked me")
if __name__=="__main__":
    mainloop()