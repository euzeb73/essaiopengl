import numpy as np

class Triangle:
    def __init__(self,app,vertex_data = None) -> None:
        self.app = app
        self.ctx = app.ctx
        if vertex_data is None:
            self.vertex_data = self.get_vertex_data()
        self.vbo = self.get_vbo()
        self.shader_prgm = self.get_shader_prgm('defaut')
        self.vao = self.get_vao()
        self.shader_prgm['m_proj'].write(self.app.camera.m_proj)

    def update(self):

        self.shader_prgm['m_view'].write(self.app.camera.m_view)

    def render(self):
        self.update()
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_prgm.release()
        self.vbo.release()

    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_prgm,[(self.vbo,'3f','position')])
        return vao

    def get_vertex_data(self):
        vertex_data = [(-0.5,-0.5,0.0),(0.5,-0.8,0.0),(0.0,0.8,0.0),(-0.9,-0.9,0.0),(-0.55,-0.95,0.0),(-0.6,-0.6,0.0)]
        # vertex_data = [(-0.6,-0.8,0.0),(0.6,-0.8,0.0),(0.0,0.8,0.0)]
        self.vertex_data = np.array(vertex_data, dtype= 'f4')
        return self.vertex_data
    
    def get_vbo(self):
        vbo = self.ctx.buffer(self.vertex_data)
        return vbo
    
    def get_shader_prgm(self,shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        return self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader )
    
class Cube(Triangle):
    def __init__(self,app,vertex_data = None):
        if vertex_data is None:
            #Sommets
            S1 = (0,0.5,0)
            S2 = (0,0,0)
            S3 = (0.5,0,0)
            S4 = (0.5,0.5,0)
            S5 = (0,0.5,0.5)
            S6 = (0,0,0.5)
            S7 = (0.5,0,0.5)
            S8 = (0.5,0.5,0.5)
            vertex_data = [S1,S2,S3,
                           S1,S3,S4,
                           S4,S3,S7,
                           S4,S7,S8,
                           S1,S6,S2,
                           S1,S5,S6,
                           S5,S8,S7,
                           S5,S7,S6]
            self.vertex_data = np.array(vertex_data, dtype= 'f4')
        super().__init__(app,self.vertex_data)