# Copyright (C) 2024 by Krishna_Help @ Github, < https://github.com/Radheranij/Poison_x_music >
# Subscribe On YT < official_radhe_krishna_1 >. All rights reserved. © Krishna © Yukki.

"""
official_radhe_krishna_1 is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Krishna <https://github.com/Radheranij/Poison_x_music>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import re
from os import path

from yt_dlp import YoutubeDL

from AlexaMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        if "soundcloud" in link:
            return True
        else:
            return False

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
