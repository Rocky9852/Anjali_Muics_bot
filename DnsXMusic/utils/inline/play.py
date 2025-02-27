#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#
import math 

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DnsXMusic.utils.formatters import time_to_seconds

def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        return "⚪─────────"
    elif 10 < umm <= 20:
        return "━⚪────────"
    elif 20 < umm <= 30:
        return "━━⚪───────"
    elif 30 < umm <= 40:
        return "━━━⚪──────"
    elif 40 < umm <= 50:
        return "━━━━⚪─────"
    elif 50 < umm <= 60:
        return "━━━━━⚪────"
    elif 60 < umm <= 70:
        return "━━━━━━⚪───"
    elif 70 < umm <= 80:
        return "━━━━━━━⚪──"
    elif 80 < umm <= 90:
        return "━━━━━━━━⚪─"
    elif 90 < umm <= 100:
        return "━━━━━━━━━⚪"
    else:
        return "───────────"
        
