import glm
import pygame as pg
FOV = 45
NEAR = 0.1
FAR = 100
SENSITIVITY = 7e-3
SPEED = 5e-3

class Camera:
    def __init__(self,app) -> None:
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(-0.1,0.1,3) #par défaut
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.m_proj = glm.perspective(glm.radians(FOV),self.aspect_ratio,NEAR,FAR)
        self.m_view = self.get_m_view()

    def rotate(self,delta_lacet,delta_tangage):
        #lacet
        self.up=glm.rotate(self.up,delta_lacet,self.up)
        self.right=glm.rotate(self.right,delta_lacet,self.up)
        self.forward=glm.rotate(self.forward,delta_lacet,self.up)
        #Tangage
        self.right=glm.rotate(self.right,delta_tangage,self.right)
        self.up=glm.rotate(self.up,delta_tangage,self.right)
        self.forward=glm.rotate(self.forward,delta_tangage,self.right)

        # print(self.up,self.forward)

    def move(self,delta_position):
        self.position += delta_position

    def update(self):
        #Rotation
        rel_x, rel_y = pg.mouse.get_rel()
        delta_lacet = -rel_x * SENSITIVITY
        delta_tangage = -rel_y * SENSITIVITY
        self.rotate(delta_lacet,delta_tangage)
        #Translation
        velocity = SPEED * self.app.delta_time
        delta_position = glm.vec3(0)
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            delta_position += self.forward * velocity
        if keys[pg.K_s]:
            delta_position -= self.forward * velocity
        if keys[pg.K_q]:
            delta_position -= self.right * velocity
        if keys[pg.K_d]:
            delta_position += self.right * velocity
        if keys[pg.K_r]:
            delta_position += self.up * velocity
        if keys[pg.K_f]:
            delta_position -= self.up * velocity
        self.move(delta_position)
        self.m_view = self.get_m_view()

    def get_m_view(self):
        return glm.lookAt(self.position,self.position + self.forward,self.up)
    