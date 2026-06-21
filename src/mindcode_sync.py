import json
import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class ArchitectureWizardConfig:
    selections: Dict[str, str]

class MindcodeSync:
    def __init__(self, workspace_folder: str):
        self.workspace_folder = workspace_folder
        self.config_file = os.path.join(workspace_folder, 'mindcode_sync_config.json')

    def register_command(self):
        return 'mindcode.sync.architecture'

    def open_wizard(self):
        # Render wizard UI in VSCode webview
        # For simplicity, assume the UI is a simple JSON object
        ui_config = {
            'title': 'Architecture Wizard',
            'fields': [
                {'name': 'field1', 'type': 'text'},
                {'name': 'field2', 'type': 'checkbox'}
            ]
        }
        return ui_config

    def persist_selections(self, selections: Dict[str, str]):
        config = ArchitectureWizardConfig(selections)
        with open(self.config_file, 'w') as f:
            json.dump({'selections': config.selections}, f)

    def load_selections(self) -> Dict[str, str]:
        if not os.path.exists(self.config_file):
            return {}
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        return config.get('selections', {})
