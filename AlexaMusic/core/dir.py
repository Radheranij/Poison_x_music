# Copyright (C) 2024 by krishna_Help @ Github, < https://github.com/Radharanij >
# Subscribe On YT < official_radhe_krishna_1 >. All rights reserved. © Poasion © Yukki.

""""
Krishna is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Krishna <https://github.com/Radharanij>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import os
import sys
import logging
from os import listdir, mkdir


def dirr():
    assets_folder = "assets"
    downloads_folder = "downloads"
    cache_folder = "cache"

    if assets_folder not in listdir():
        logging.warning(
            f"{assets_folder} Folder not Found. Please clone repository again."
        )
        sys.exit()

    for file in os.listdir():
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            os.remove(file)

    if downloads_folder not in listdir():
        mkdir(downloads_folder)

    if cache_folder not in listdir():
        mkdir(cache_folder)

    logging.info("Directories Updated.")


if __name__ == "__main__":
    dirr()
