import numpy as np

class Triangle:
    def __init__(self,app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_prgm = self.get_shader_prgm('defaut')

    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_prgm,[(self.vbo,'3f','in_position')])
        return vao

    def get_vertex_data(self):
        vertex_data = [(-0.5,0.5,0),(0.5,-0.8,0),(0,0.8,0)]
        vertex_data = np.array(vertex_data, dtype= 'f4')
        return vertex_data
    
    def get_vbo(self):
        vertex_data=self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def get_shader_prgm(self,shader_name):
        with open(f'shaders/{shader_name}.vert') as file
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file
            vertex_shader = file.read()
