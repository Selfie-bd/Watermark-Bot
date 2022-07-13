# (c) @AbirHasan2005

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN","5162389780:AAGXy1dBTsj6CpzPt6bAM_XVc3hHiL-OFQo")
	API_ID = int(os.environ.get("API_ID", 1976680))
	API_HASH = os.environ.get("API_HASH","9073255ce64a6072a59099803493f97d")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "JkqQxXVQZzuj3DM")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "5e4f1b21f9638094a8cf")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001611517455"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001576695301")
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "veryfast")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1940030638))
	CAPTION = "By @GroupDcBots"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "WatermarkDcBot")
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", True))
	USAGE_WATERMARK_ADDER = """
**Hi, I am Video Watermark Adder Bot!**

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at **[Support Group](https://t.me/Groupdc)**__
"""
	PROGRESS = """
Percentage 🚸 : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
