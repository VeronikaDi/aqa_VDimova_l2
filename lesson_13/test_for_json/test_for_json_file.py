import json
from pathlib import Path

folder_path = Path('ideas_for_test/work_with_json')
log_file = Path('lesson_13/test_for_json/json_result_after_test_2.log')

for json_file in folder_path.glob('*.json'):
    try:
        with json_file.open('r') as f:
            json.load(f)
    except json.JSONDecodeError:
        with log_file.open('a') as log:
            log.write(f"Error: {json_file.name} is not a valid JSON file.\n")
