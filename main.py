#!/usr/bin/python
# -*- coding: utf-8 -*-

from slackclient import SlackClient

import os
import time
import re
import logging

class SchokotronCaralho(object):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self.slack_username = os.getenv("SLACK_API_USERNAME", "")
        self.slack_token = os.getenv("SLACK_API_TOKEN", 0)
        self.slack_client = SlackClient(self.slack_token)

        if self.slack_token is 0 or self.slack_username is "":
            exit("Error, couldn't connect to Slack")

        self.listen()

    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            self.logger.info("Successfully connected, listening for commands")
            while True:
                events = self.slack_client.rtm_read()

                if events and len(events) > 0:
                    for event in events:
                        self.parse_event(event)
                 
                time.sleep(1)
        else:
            exit("Error, Connection Failed")

    def parse_event(self, event):
        if event and "text" in event and "user" in event:
            if not self.self_sent(event["user"]):
                channel_id = event["channel"]
                
                user_details = self.slack_client.api_call(
                    "users.info",
                    user=event['user']
                )

                if re.match( r'(ajuda).*(caralho)', event["text"], re.M|re.I):
                    self.send_message("Quié caralho?", channel_id)
                    self.send_message("Podes enviar-me:", channel_id)
                    self.send_message("`Dá-me um chocolate, caralho!`", channel_id)
                    self.send_message("`Dá-me a puta de um chocolate seu filho da puta, caralho!`", channel_id)
                    return

                if re.match( r'(dá-me|quero).*(chocolate).*(caralho)', event["text"].encode('utf-8'), re.M|re.I):
                    self.send_message("Toma o teu chocolate gordo(a).", channel_id)
                    self.send_message("O(A) gordo(a) do(a) @" + user_details["user"]["name"] + " acabou de comer mais um chocolate!", "#random")
                    return

                self.send_message("Vai chatear o caralho! :middle_finger:", channel_id)

    def self_sent(self, user_id):
        users = self.slack_client.api_call(
            "users.list"
        )

        if users and "ok" in users:
            for user in users["members"]:
                if user["name"] == self.slack_username and user["id"] == user_id:
                    return True

        return False

    def send_message(self, message, channel):
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            link_names=True,
            parse="full",
            text=message
        )

if __name__ == "__main__":
    sc = SchokotronCaralho()
