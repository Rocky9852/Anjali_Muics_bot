import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from DnsXMusic.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        return "─▷─────────"
    elif 10 < umm <= 20:
        return "──▷────────"
    elif 20 < umm <= 30:
        return "───▷───────"
    elif 30 < umm <= 40:
        return "────▷──────"
    elif 40 < umm <= 50:
        return "─────▷─────"
    elif 50 < umm <= 60:
        return "──────▷────"
    elif 60 < umm <= 70:
        return "───────▷───"
    elif 70 < umm <= 80:
        return "────────▷──"
    elif 80 < umm <= 90:
        return "─────────▷─"
    elif 90 < umm <= 100:
        return "──────────▷"
    else:
        return "───────────"

#bar of wynk---------------------------------------
    if 0 < umm <= 1:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄 𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 1 <= umm < 2:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 2 <= umm < 3:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 3 <= umm < 4:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 4 <= umm < 5:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 5 <= umm < 6:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 6 <= umm < 7:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 7 <= umm < 8:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 8 <= umm < 9:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 9 <= umm < 10:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 10 <= umm < 11:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 11 <= umm < 12:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 12 <= umm < 13:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 13 <= umm < 14:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 14 <= umm < 15:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 15 <= umm < 16:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 16 <= umm < 17:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 17 <= umm < 18:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 18 <= umm < 19:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 19 <= umm < 20:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 20 <= umm < 21:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 21 <= umm < 22:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 22 <= umm < 23:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 23 <= umm < 24:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 24 <= umm < 25:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 25 <= umm < 26:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 26 <= umm < 27:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 27 <= umm < 28:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 28 <= umm < 29:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 29 <= umm < 30:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 30 <= umm < 31:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 31 <= umm < 32:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 32 <= umm < 33:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 33 <= umm < 34:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 34 <= umm < 35:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 35 <= umm < 36:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 36 <= umm < 37:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 37 <= umm < 38:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 38 <= umm < 39:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 39 <= umm < 40:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 40 <= umm < 41:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 41 <= umm < 42:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 42 <= umm < 43:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 43 <= umm < 44:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 44 <= umm < 45:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 45 <= umm < 46:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 46 <= umm < 47:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 47 <= umm < 48:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 48 <= umm < 49:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"
    elif 49 <= umm < 50:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 50 <= umm < 51:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 51 <= umm < 52:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 52 <= umm < 53:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 53 <= umm < 54:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 54 <= umm < 55:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 55 <= umm < 56:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 56<= umm < 57:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 57 <= umm < 58:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 58 <= umm < 59:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 59 <= umm < 60:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 60 <= umm < 61:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 61 <= umm < 62:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝑴𝒖𝒔𝒊𝒄"
    elif 62 <= umm < 63:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 63 <= umm < 64:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 64 <= umm < 65:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 65 <= umm < 66:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 66 <= umm < 67:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 67 <= umm < 68:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 68 <= umm < 69:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 69 <= umm < 70:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 70 <= umm < 71:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 71 <= umm < 72:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 72 <= umm < 73:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 73 <= umm < 74:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 74 <= umm < 75:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ"
    elif 75 <= umm < 76:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 76 <= umm < 77:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 77 <= umm < 78:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 78 <= umm < 79:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣"
    elif 79 <= umm < 80:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 80 <= umm < 81:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 81 <= umm < 82:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 82 <= umm < 83:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 83 <= umm < 84:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐒𝗍υᑯ𝗂ⱺ"
    elif 84 <= umm < 85:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 85 <= umm < 86:
        bar = "𝐌𝗂ᥣᥣ𝗂ⱺ𐓣 𝐒ⱺ𐓣𝗀𝗌"
    elif 86 <= umm < 87:
        bar = "𝐄α𝗌𝗂ᥣ𝗒 𝐒𝗍𝗋𝖾αꭑ "
    elif 87 <= umm < 88:
        bar = "𝐋ⱺω-𝐒ρ𝖾𝖾ᑯ 𝐒𝗍𝗋𝖾αꭑ𝗂𐓣𝗀"
    elif 88 <= umm < 89:
        bar = "𝐁𝗂𝗀 𝐃α𝗍αᑲα𝗌ɦ"
    elif 89 <= umm < 90:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 90 <= umm < 91:
        bar = "𝐋α𝗀 𝐅𝗋𝖾𝖾 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 "
    elif 91 <= umm < 92:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ"
    elif 92 <= umm < 93:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐅α𝗏ⱺ𝗋𝗂𝗍𝖾 ρᥣα𝗒ᥣ𝗂𝗌𝗍"
    elif 93 <= umm < 94:
        bar = "𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐌υ𝗌𝗂𝖼"
    elif 94 <= umm < 95:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    elif 95 <= umm < 96:
        bar = "𝐁𝖾𝗌𝗍 𝐅𝖾α𝗍υ𝗋𝖾𝗌"
    elif 96 <= umm < 97:
        bar = "𝐅𝗋𝖾𝖾 𝐃ⱺω𐓣ᥣⱺαᑯ 𝐌υ𝗌𝗂𝖼"
    elif 97 <= umm < 98:
        bar = "𝐄𐓣𝗃ⱺ𝗒 𝐉𝗂ⱺ 𝐒αα𝗏𐓣 𝐀ρρ 𝐎𐓣 𝐓𝖾ᥣ𝖾𝗀𝗋αꭑ"
    elif 98 <= umm < 99:
        bar = "𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐀ᑲⱺυ𝗍 𝐓ⱺ 𝐄𐓣ᑯ"
    else:
        bar = "𝐓ɦ𝖾 𝐒ⱺ𐓣𝗀 𝚰𝗌 𝐎𝗏𝖾𝗋"


   
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾")],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾")],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bar = get_progress_bar(percentage)  # using for getting the bar
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾"),
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾"),
        ],
    ]
    return buttons


## By umm
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="〆 𝖢𝗅𝗈𝗌𝖾 〆", callback_data="𝖢𝗅𝗈𝗌𝖾")]]
)

## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DnsPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DnsPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")],
    ]
    return buttons
