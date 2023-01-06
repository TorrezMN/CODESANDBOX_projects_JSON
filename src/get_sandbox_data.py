#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

import json
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def get_repos():
    """Gets a full list of my sandboxes."""
    sandboxes_url = "https://codesandbox.io/api/v1/users/TorrezMN/sandboxes?sort_by=view_count&direction=desc&page=all"
    data = requests.get(sandboxes_url, headers=HEADERS)

    global new_data

    new_data = json.loads(data.text)


#  GETTING REPOS DATA
get_repos()


#  SAVE DATA TO JSON FILE
with open("sandboxes.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=4)
