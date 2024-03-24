from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def build_films_keyboard(films: list):
    keyboard = []
    for film in films:
        button = InlineKeyboardButton(text=film.get("title"), callback_data=f"film_{films.index(film)}")
        keyboard.append([button])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def build_films_details_keyboard(url, video_link, video_tg_link):
    keyboard = [
        [InlineKeyboardButton(text="Open the IMDb link", url=url)],
        [InlineKeyboardButton(text="Open Google Drive link", url=video_link)] if video_link else [],
        [InlineKeyboardButton(text="Open link from Telegram", url=video_tg_link)] if video_tg_link else [],
        [InlineKeyboardButton(text="Go back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def build_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Go back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


