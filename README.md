# Business-Plan-Generator

## Setup Instructions
### Dependencies
To run this code locally, you need a virtual environment with the necessary dependencies.
Run the commands below to create and open a virtual environment (for Windows machines)
```
# Go into your project folder
cd Business-Plan-Generator
# Create a virtual env (only run this once!!)
python -m venv env\
# Activate the virtual env (run this everytime you want to work on this project)
env\Scripts\activate
```
Run the commands below to install the packages
```
# This installs OpenAI, run only once
pip install openai
```
### API Key
The Openai API Key is stored in `constants.json`. Follow the steps below to set it up:

1. Create a copy of the provided `constants_template.json` 
2. Rename the copied file to `constants.json`
3. Modify `constants.json` to include the OpenAI API Key

This is a safe way to store the key. The file `.gitignore` is set up to automatically ignore the file storing the API key when uploading things to Github.

### Useful Github Commands
To view the status of your local code compared to the main branch (this repo)
```
git status
```
To update your local code (so it's the same as what's in the online repo), run the command below
```
git pull
```
To add your local changes to this repo
```
git add .
git commit -m "a short messages about your changes"
git push
```
