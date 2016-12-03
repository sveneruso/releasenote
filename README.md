# Release Note
***ReleaseNote*** is a project to automatically generate the release notes from git tags or branch.

## Install
- Download the project
- Creat the config file using config_template.json example
- Run to generate the release note

		python3 releaseNote.py <start> <end>


Example:

To have the commits on developemnt but not on master
		
		python3 releaseNote.py master development

### How to contribute
Fell free to make a pull request or open an issue if you found some bugs or have new features.

## Next
- Generate config file with a wizard
- Add compact and group mode
- Config file as parameter
