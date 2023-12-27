import numpy as np

class Triangle:
    def __init__(self,app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.vertex_data = self.get_vertex_data()
        self.text_data = self.get_text_data() 
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
        vao = self.ctx.vertex_array(self.shader_prgm,[(self.vbo,'2f 3f','text_coord','position')])
        return vao

    def get_vertex_data(self):
        vertex_data = [(-0.5,-0.5,0.0),(0.5,-0.8,0.0),(0.0,0.8,0.0),(-0.9,-0.9,0.0),(-0.55,-0.95,0.0),(-0.6,-0.6,0.0)]
        # vertex_data = [(-0.6,-0.8,0.0),(0.6,-0.8,0.0),(0.0,0.8,0.0)]
        vertex_data = np.array(vertex_data, dtype= 'f4')
        return vertex_data
    
    def get_text_data(self):
        vertex_data = [(0,0),(1,0),(1,1)]
        vertex_data = np.array(vertex_data, dtype= 'f4')
        return vertex_data

    def get_vbo(self):
        vbo = self.ctx.buffer(np.hstack([self.text_data, self.vertex_data]))
        return vbo
    
    def get_shader_prgm(self,shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        return self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader )
    
class Cube(Triangle):
    def __init__(self,app):
        super().__init__(app)
        
    def get_vertex_data(self):
        #Sommets
        S1 = (0,0.5,0)
        S2 = (0,0,0)
        S3 = (0.5,0,0)
        S4 = (0.5,0.5,0)
        S5 = (0,0.5,0.5)
        S6 = (0,0,0.5)
        S7 = (0.5,0,0.5)
        S8 = (0.5,0.5,0.5)
        vertex_data = [S1,S2,S3]#,
                        # S1,S3,S4,
                        # S4,S3,S7,
                        # S4,S7,S8,
                        # S1,S6,S2,
                        # S1,S5,S6,
                        # S5,S8,S7,
                        # S5,S7,S6,
                        # S2,S6,S7,
                        # S2,S7,S3,
                        # S3,S2,S6,
                        # S3,S6,S7]
        return np.array(vertex_data, dtype= 'f4')
    
    def get_text_data(self):
        #Sommets
        S1 = (0,1)
        S2 = (0,0) 
        S3 = (1,0)
        S4 = (1,1)
        vertex_data = [S1,S2,S3]#,
                    #    S1,S3,S4,
                    #    S1,S2,S3,
                    #    S1,S3,S4,
                    #    S4,S2,S3,
                    #    S4,S1,S2,
                    #    S4,S2,S3,
                    #    S4,S1,S2,
                    #    S1,S2,S3,
                    #    S1,S3,S4,
                    #    S1,S2,S3,
                    #    S1,S3,S4]
        vertex_data = np.array(vertex_data, dtype= 'f4')
        return vertex_data