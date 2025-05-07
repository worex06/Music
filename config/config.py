# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "24127278"))
API_HASH = getenv("API_HASH", "ad3ac8bc4d7f5c9b9b650588a2411d2e")

BOT_TOKEN = getenv("BOT_TOKEN", "7703499597:AAEGYvHB1XjLuRiVDuXLRlvTq8kNAJU0ox0")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://turan:ramoben200@cluster0.mllmbuy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG = True  # veya False
LOG_GROUP_ID = -1001903631091 # Telegram grup ID'si

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "TURAN MÜZİK")



# Eğer birden fazla OWNER_ID varsa, bunları liste olarak tanımlayın
OWNER_ID = int(getenv("OWNER_ID", "8119547604"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID", "7703499597")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ramowlf/turan")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TurkUserBotKanali")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/TurkUserBotKanali")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3400"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/ramowlf/turan")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "16c87464675546abae618d6a218d4448")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "d0b5cb52cc5844b7b8bf092ad301532e")


VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes


STRING1 = getenv("STRING_SESSION", "BAFwJy4ALlhf4I6q3LdH1QZ-23ZlaPpwN2Q_mdseaBabsifeRKj2BX4Iog3HC8ktiZA_bpEYA6VaVx0nmICC0EB6t9jhMeDTJJ7nMiQMpHGYQcrrI1T3oRNk_MWk1c85-Cg_3yfWSxGC_2pcCPdCDog6a4rMBgFlVrUG1CwOd694p4Ebw33wgKtdB2fEaFARlc25fq2Kf_JpNL6dtFwiC4Fv3_Ykx-ecoB8cr1RCd7nZqi1M4_8IqMWE7S_Dr6bUd9B1Z4Ng_ulOnM_WEXEZ0Dr7EtDtFPoXSfdrakbbWBl2OeYnlw-genAhh3PlGSvXbOejhx4N-dMp1LDpilM2AZimJHuC2AAAAAFv_XsgAA")
STRING2 = getenv("STRING_SESSION2", None)

STRING3 = getenv("STRING_SESSION3", None)

STRING4 = getenv("STRING_SESSION4", None)

STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)


SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://i.hizliresim.com/hyjkuec.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
            
