import pytest
import os
import json
from mindcode_sync import MindcodeSync, ArchitectureWizardConfig

def test_register_command():
    sync = MindcodeSync('/tmp/workspace')
    assert sync.register_command() == 'mindcode.sync.architecture'

def test_open_wizard():
    sync = MindcodeSync('/tmp/workspace')
    ui_config = sync.open_wizard()
    assert ui_config['title'] == 'Architecture Wizard'
    assert len(ui_config['fields']) == 2

def test_persist_selections(tmp_path):
    workspace_folder = str(tmp_path)
    sync = MindcodeSync(workspace_folder)
    selections = {'field1': 'value1', 'field2': 'value2'}
    sync.persist_selections(selections)
    assert os.path.exists(os.path.join(workspace_folder, 'mindcode_sync_config.json'))
    with open(os.path.join(workspace_folder, 'mindcode_sync_config.json'), 'r') as f:
        config = json.load(f)
    assert config['selections'] == selections

def test_load_selections(tmp_path):
    workspace_folder = str(tmp_path)
    sync = MindcodeSync(workspace_folder)
    selections = {'field1': 'value1', 'field2': 'value2'}
    with open(os.path.join(workspace_folder, 'mindcode_sync_config.json'), 'w') as f:
        json.dump({'selections': selections}, f)
    loaded_selections = sync.load_selections()
    assert loaded_selections == selections

def test_load_selections_empty(tmp_path):
    workspace_folder = str(tmp_path)
    sync = MindcodeSync(workspace_folder)
    assert sync.load_selections() == {}
