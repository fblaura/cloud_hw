from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws=Workspace.from_config(path='./.azureml', _file_name='config.json')

experiment=Experiment(workspace=ws, name='day1-initial-testing-workspace')

run_config=ScriptRunConfig(source_directory='./src', script='test-ws.py', compute_target='cpu-hw')

run=experiment.submit(run_config)

aml_url=run.get_portal_url()

print(aml_url)