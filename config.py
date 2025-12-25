import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# =========================================================
# HELPERS
# =========================================================
def get_int(name, default=0):
    try:
        return int(getenv(name, default))
    except (TypeError, ValueError):
        return default


def get_bool(name, default=False):
    return str(getenv(name, default)).lower() in (
        "true", "1", "yes", "on"
    )


# =========================================================
# REQUIRED (BOT WILL STOP IF MISSING)
# =========================================================
API_ID = get_int("API_ID")
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise SystemExit(
        "❌ ERROR: API_ID / API_HASH / BOT_TOKEN missing"
    )


# =========================================================
# OWNER / LOG
# =========================================================
OWNER_ID = get_int("OWNER_ID")
LOGGER_ID = get_int("LOGGER_ID", -1003530337097)
LOG = get_bool("LOG", True)


# =========================================================
# DATABASE
# =========================================================
MONGO_DB_URI = getenv("MONGO_DB_URI", "")


# =========================================================
# BOT SETTINGS
# =========================================================
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "MusicBot")
PRIVATE_BOT_MODE = get_bool("PRIVATE_BOT_MODE", False)

DURATION_LIMIT_MIN = get_int("DURATION_LIMIT", 999999)


# =========================================================
# HEROKU
# =========================================================
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")


# =========================================================
# API
# =========================================================
API_URL = getenv(
    "API_URL",
    "https://api.thequickearn.xyz"
)
VIDEO_API_URL = getenv(
    "VIDEO_API_URL",
    "https://api.video.thequickearn.xyz"
)
API_KEY = getenv(
    "API_KEY",
    "30DxNexGenBotsfcfad8"
)


# =========================================================
# GIT
# =========================================================
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/krishbharti3404-source/Oxcy"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")


# =========================================================
# SUPPORT
# =========================================================
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/veron_bots"
)
SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/adult_town"
)


# =========================================================
# AUTO FEATURES
# =========================================================
AUTO_LEAVING_ASSISTANT = get_bool(
    "AUTO_LEAVING_ASSISTANT", False
)
AUTO_GCAST = get_bool("AUTO_GCAST", False)
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")


# =========================================================
# SPOTIFY
# =========================================================
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", ""
)


# =========================================================
# LIMITS
# =========================================================
SERVER_PLAYLIST_LIMIT = get_int(
    "SERVER_PLAYLIST_LIMIT", 999
)
PLAYLIST_FETCH_LIMIT = get_int(
    "PLAYLIST_FETCH_LIMIT", 999
)

SONG_DOWNLOAD_DURATION_LIMIT = get_int(
    "SONG_DOWNLOAD_DURATION_LIMIT", 999999
)

TG_AUDIO_FILESIZE_LIMIT = get_int(
    "TG_AUDIO_FILESIZE_LIMIT", 104857600
)
TG_VIDEO_FILESIZE_LIMIT = get_int(
    "TG_VIDEO_FILESIZE_LIMIT", 1073741824
)


# =========================================================
# STRING SESSIONS
# =========================================================
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")


# =========================================================
# RUNTIME DATA (NO ERRORS)
# =========================================================
BANNED_USERS = filters.user([])
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


# =========================================================
# IMAGES
# =========================================================
DEFAULT_IMG = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"

START_IMG_URL = getenv("START_IMG_URL", DEFAULT_IMG)
PING_IMG_URL = getenv("PING_IMG_URL", DEFAULT_IMG)

PLAYLIST_IMG_URL = "https://files.catbox.moe/owu6ir.jpg"

STATS_IMG_URL = START_IMG_URL
TELEGRAM_AUDIO_URL = START_IMG_URL
TELEGRAM_VIDEO_URL = START_IMG_URL
STREAM_IMG_URL = PLAYLIST_IMG_URL
SOUNCLOUD_IMG_URL = START_IMG_URL
YOUTUBE_IMG_URL = PLAYLIST_IMG_URL
SPOTIFY_ARTIST_IMG_URL = START_IMG_URL
SPOTIFY_ALBUM_IMG_URL = START_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = START_IMG_URL


# =========================================================
# UTIL
# =========================================================
def time_to_seconds(time):
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(
            reversed(str(time).split(":"))
        )
    )


DURATION_LIMIT = time_to_seconds(
    f"{DURATION_LIMIT_MIN}:6000"
)


# =========================================================
# URL VALIDATION
# =========================================================
for url, name in [
    (SUPPORT_CHANNEL, "SUPPORT_CHANNEL"),
    (SUPPORT_CHAT, "SUPPORT_CHAT"),
]:
    if url and not re.match(r"^https?://", url):
        raise SystemExit(
            f"❌ ERROR: {name} must start with https://"
        )
