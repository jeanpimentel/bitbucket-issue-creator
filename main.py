#!/usr/bin/env python3
import argparse
import configparser
import csv
import json

import requests


def load_config():
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    return conf


def get_url(configs):
    return f"https://api.bitbucket.org/2.0/repositories/{configs.get('username')}/{configs.get('repo_slug')}/issues"


def create_issue(configs, data):
    url = get_url(configs)
    auth = (configs.get('username'), configs.get('password'))

    headers = {
        'user-agent': 'bitbucket-issue-creator',
        'content-type': 'application/json',
    }

    result = requests.post(url, headers=headers, data=data, auth=auth)

    if result.status_code != 201:
        raise Exception(result.json())


def create_json_payload(row):
    row['content'] = {'raw': row.get('content')}

    if row.get('component'):
        row['component'] = {'name': row.get('component')}
    else:
        del row['component']

    return json.dumps(row)


if __name__ == '__main__':

    configs = load_config()

    parser = argparse.ArgumentParser(description='Create issues on Bitbucket')
    parser.add_argument('repo', type=str, choices=configs.sections(), help='Repository where issues will be created')
    parser.add_argument('source', type=argparse.FileType('r'), help='CSV file with issues content')

    args = parser.parse_args()

    configs = dict(configs.items(args.repo))

    reader = csv.DictReader(args.source)
    for line, row in enumerate(reader):
        payload = create_json_payload(row)

        try:
            create_issue(configs, payload)
        except Exception as e:
            print(f'Error on line {line}', row, e, sep='|')

    print('Done!')
