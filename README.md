# Bitbucket Issue Creator

This script reads a CSV file and then, create issues on a Bitbucket project.

![Issues on Bitbucket](.github/sample.png?raw=true "Issues on Bitbucket")


## Installation

```
git clone https://github.com/jeanpimentel/bitbucket-issue-creator.git && cd bitbucket-issue-creator
pip install -r requirements.txt
chmod +x ./main.py
```

## Configuration

If you use 2FA (or even if you don't), you should create an app password to use that script.

> App passwords allow two-step verification users to access their Bitbucket account through apps such as Sourcetree. We'll generate the app passwords for you, and you won't need to remember them.

To create an app password, go to: https://bitbucket.org/account/user/YOUR-USERNAME-HERE/app-passwords/new

⚠️ Do not forget to mark **Issues (Read/Write)**

---

Edit [config.ini](./config.ini) to use your credentials and repositories

```ini
[DEFAULT]
username = your_username
password = your_password

[my-repo]
repo_slug = my-repository

[studies]
repo_slug = studies
```

---

Check [issues.csv](./issues.csv) to understand how the file is structured

## Usage

```
./main.py -h
usage: main.py [-h] {my-repo,studies} source

Create issues on Bitbucket

positional arguments:
  {my-repo,studies}  Repository where issues will be created
  source             CSV file with issues content

optional arguments:
  -h, --help         show this help message and exit
```

Sample: 
```
./main.py my-repo issues.csv
done!
```
