# Welcome to the CobbKit repository!

CobbKit is a desktop app used to as a base for tools I find helpful. The repo currently contains a single app that connects to GitHub and retrieves pull requests with pending reviewers.

To use this app you will need to create a GitHub personal access token. You can do this by going to your GitHub account settings and selecting "Developer settings" from the sidebar. Then select "Personal access tokens" and click "Generate new token". You will need to select the "repo" scope to allow the app to access your repositories.

Once you have your token you will be able to enter that token in the settings menu. This will create a .env file in the root of the project that will store your token. You can also enter your token in the .env file manually.


## Installation

To install the required dependencies for the app, run the following command in the root of the project:

```bash
pip install -r requirements.txt -t .
```

### Sqlite3

The app uses sqlite3 to store data. To install sqlite3, run the following command:

```bash
/bin/bash -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install sqlite3
```

### Troubleshooting

If you run into any issues with the installation you may need to run one of the commands found on [this](https://bobbyhadz.com/blog/python-no-module-named-tkinter) article.


## Running the app

```bash
/usr/local/bin/python3.9 main.py
``````


We hope you find this package useful, and we welcome any feedback or contributions to improve it!
