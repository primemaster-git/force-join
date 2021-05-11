import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1708956109:AAFyBaXSks8SCDVHoXmZ5fvTMx4dH2RPUok"
    DATABASE_URL = ""
    APP_ID = "3025747"
    API_HASH = "6330a7c3059cac3b85286bff7e053e9a"


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribers**\nForce group members to join a specific channel before sending messages in the group.\n\n**Setup**\n**Step 1.** __Add me in a group(in which you are creator of the group) as admin.__\n**Step 2.** __Send__ `/ForceSubscribe {your channel username}`\n**Step 3.** __Add me to your channel as admin.__\n\n`All set ! I mute users who didn't joined your channel and ask them to join channel and unmute themself.`\n\n**Commands**\n\n/ForceSubscribe { off / no / disable} - To stop force subscriber\n\n/ForceSubscribe {Channel Username} - Set the Channel\n\n/ForceSubscribe - Get current Status",
        
        "**Developed by @MaxxRider**\n\nPowered by @MaxxPrivate\nThanks to - @PyroGram @HasibulKobir"
      ]

      START_MSG = "Hey [{}](tg://user?id={})\nI am a multifunctional group manager bot.\nLearn more at /help"
      
