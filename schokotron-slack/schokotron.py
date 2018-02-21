#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import re
import urllib

class SchokotronCaralho(object):
    ROBOT_ADDRESS = "http://127.0.0.1:5000"
    API_ADDRESS = ""

    def __init__(self, logger, slack_client, slack_username):
        self.logger = logger
        self.slack_client = slack_client
        self.slack_username = slack_username


    def run(self):
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
                user_info = self.parse_user_info(event['user'])

                self.logger.info("Recebi uma mensagem do " + user_info["username"])

                if re.match( r'(ajuda).*(caralho)', event["text"], re.M|re.I):
                    self.send_message("Quié caralho?", channel_id)
                    self.send_message("Podes enviar-me:", channel_id)
                    self.send_message("`Dá-me um chocolate, caralho!`", channel_id)
                    self.send_message("`Dá-me a puta de um chocolate seu filho da puta, caralho!`", channel_id)
                    return

                if re.match( r'(dá-me|quero).*(chocolate).*(caralho)', event["text"], re.M|re.I):
                    self.perform_action("serve_chocolat", channel_id)
                    #self.send_message("O(A) gordo(a) do(a) @" + user_details["username"] + " acabou de comer mais um chocolate!", "#random")
                    return

                self.send_message("Vai chatear o caralho! :middle_finger:", channel_id)


    def self_sent(self, user_id):
        users = self.slack_client.api_call(
            "users.list"
        )

        if users and "ok" in users and "members" in users:
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


    def parse_user_info(self, user_id):
        user_data = {}

        user_details = self.slack_client.api_call(
            "users.info",
            user=user_id
        )

        user_data["provider_id"] = user_details["user"]["id"]
        user_data["username"] = user_details["user"]["name"]
        user_data["full_name"] = user_details["user"]["real_name"]
        user_data["email"] = user_details["user"]["profile"]["email"]

        return user_data


    def perform_action(self, action, channel_id):
        return {
            'serve_chocolat': self.serve_chocolat(channel_id),
        }[action]
    

    def serve_chocolat(self, channel_id):
        try:
            urllib.request.urlopen(self.ROBOT_ADDRESS + "/candies").read()
            self.send_message("Toma o teu chocolate gordo(a).", channel_id)
        except Exception as description:
            self.logger.error("Something went wrong! Here are some details:")
            self.logger.error(description)
            self.send_message("Ocorreu um erro! :cry: Contacta os Super Administradores desta merda.", channel_id)
