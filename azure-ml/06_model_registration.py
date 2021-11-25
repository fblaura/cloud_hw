from azureml.core import Workspace
from azureml.core import Model
if __name__ == "__main__":
    ws = Workspace.from_config(path='./.azureml',_file_name='config.json')
    
    model = Model.register(model_name='Train_electrical',
                            tags={'Varianza explicada':  1,'MAE' : 0.077},
                            model_path='output\Electrical_model.pkl',
                            workspace = ws)
    print(model.name, model.id, model.version, sep='\t')