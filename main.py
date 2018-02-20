#!/usr/bin/python
# -*- coding: utf-8 -*-

from slackclient import SlackClient
import os
import logging

from schokotron import SchokotronCaralho

if __name__ == "__main__":
    # Inject this has a dependency
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    slack_username = os.getenv("SLACK_API_USERNAME", "")
    slack_token = os.getenv("SLACK_API_TOKEN", 0)

    if slack_token is 0 or slack_username is "":
        exit("Error, couldn't connect to Slack")

    slack_client = SlackClient(slack_token)

    sc = SchokotronCaralho(logger, slack_client, slack_username)
    sc.run()
