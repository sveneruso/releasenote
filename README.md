# Release Note
This project is for generate release note from git branches and/or tag

## Install
- Download the project
- Creat the config file using config_template.json example
- Run to generate the release note

		python3 releaseNote.py <start> <end>


Example:

To have the commits on developemnt but not on master
		
		python3 releaseNote.py master development

## Next
- Generate config file with a wizard
- Add compact and group mode
- Config file as parameter