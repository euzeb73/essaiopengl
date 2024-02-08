
class Scene:
    def __init__(self,model_list=[]):
        self.models = model_list

    def add_model(self, model):
        self.models.append(model)
    
    def update(self):
        for model in self.models:
            model.update()

    def render(self):
        for model in self.models:
            model.render()

    def destroy(self):
        for model in self.models:
            model.destroy()