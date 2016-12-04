# Release Note [![Code Climate](https://codeclimate.com/github/sveneruso/releasenote/badges/gpa.svg)](https://codeclimate.com/github/sveneruso/releasenote)
***ReleaseNote*** is a project to generate automatically the release notes from git tags or branch.

## Install
- Download the project
- Create the config file using config_template.json example
	- Add the path to the repo
	- Add the regex to identity your commit (For example this is the rule for trello URLs ***?:https://trello.com/c/[a-z A-Z 0-9 \/]{8}***)
- To generate the release note:

		python3 releaseNote.py <start> <end>

For example, to include commits from the _development_ branch but not on master
		
		python3 releaseNote.py master development

### How to contribute
Feel free to make a pull request or open an issue if you find bugs or you want to propose new features.

## Next
- Generate config file with a wizard
- Add compact and group mode
- Config file as parameter
