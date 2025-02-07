# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    name = "ALL-IN-ONE-PRO-BOT"
    APP_ID = int(os.environ.get("APP_ID", 268451200685))
    API_HASH = os.environ.get("API_HASH", "5a2684512006853f2e48aca9652d83ea")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5457463964:AAFQgKp5KgOVO_PYbbcekMT9R-PhsQVevVI")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5798143340").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["True", "true"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
