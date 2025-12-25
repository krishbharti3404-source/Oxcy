import os
import re
import random
import aiofiles
import aiohttp

from PIL import (
    Image,
    ImageDraw,
    ImageEnhance,
    ImageFilter,
    ImageFont,
    ImageOps,
)

from unidecode import unidecode
from py_yt import VideosSearch

from BrandrdXMusic import app
from config import YOUTUBE_IMG_URL


# ================= UTILITIES ================= #

def changeImageSize(max_w, max_h, img):
    ratio = min(max_w / img.width, max_h / img.height)
    size = (int(img.width * ratio), int(img.height * ratio))
    return img.resize(size, Image.LANCZOS)


def clean_title(text, limit=60):
    text = re.sub(r"\W+", " ", text)
    words = text.split()
    out = ""
    for w in words:
        if len(out) + len(w) <= limit:
            out += " " + w
    return out.strip()


# ================= MAIN FUNCTION ================= #

async def get_thumb(videoid):
    os.makedirs("cache", exist_ok=True)

    final_path = f"cache/{videoid}.png"
    temp_path = f"cache/temp_{videoid}.png"

    if os.path.isfile(final_path):
        return final_path

    try:
        search = VideosSearch(
            f"https://www.youtube.com/watch?v={videoid}", limit=1
        )
        data = (await search.next())["result"][0]

        title = clean_title(data.get("title", "Unsupported Title").title())
        duration = data.get("duration", "Unknown")
        views = data.get("viewCount", {}).get("short", "Unknown Views")
        channel = data.get("channel", {}).get("name", "Unknown Channel")
        thumb_url = data["thumbnails"][0]["url"].split("?")[0]

        # -------- Download Thumbnail -------- #
        async with aiohttp.ClientSession() as session:
            async with session.get(thumb_url) as resp:
                if resp.status != 200:
                    return YOUTUBE_IMG_URL
                async with aiofiles.open(temp_path, "wb") as f:
                    await f.write(await resp.read())

        # -------- Image Processing -------- #
        base = Image.open(temp_path).convert("RGB")
        base = changeImageSize(1280, 720, base)

        # Blur Background
        background = base.filter(ImageFilter.GaussianBlur(10))
        background = ImageEnhance.Brightness(background).enhance(0.85)
        background = ImageEnhance.Contrast(background).enhance(1.2)

        # Neon Border
        neon_colors = ["cyan", "magenta", "blue", "red", "green", "yellow"]
        background = ImageOps.expand(
            background, border=6, fill=random.choice(neon_colors)
        )
        background = changeImageSize(1280, 720, background)

        draw = ImageDraw.Draw(background)

        # -------- Fonts -------- #
        title_font = ImageFont.truetype(
            "BrandrdXMusic/assets/font.ttf", 42
        )
        small_font = ImageFont.truetype(
            "BrandrdXMusic/assets/font2.ttf", 28
        )

        # -------- Text Drawing -------- #
        draw.text((40, 35), title, fill="white", font=title_font)
        draw.text(
            (40, 95),
            f"{channel} • {views}",
            fill="white",
            font=small_font,
        )
        draw.text(
            (1100, 20),
            unidecode(app.name),
            fill="white",
            font=small_font,
        )
        draw.text(
            (40, 650),
            duration,
            fill="white",
            font=small_font,
        )

        # -------- Save -------- #
        os.remove(temp_path)
        background.save(final_path, "PNG")

        return final_path

    except Exception as e:
        print("[THUMB ERROR]", e)
        return YOUTUBE_IMG_URL
