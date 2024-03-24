from aiogram.fsm.state import State, StatesGroup

class FilmCreateForm(StatesGroup):
    title = State()
    desc = State()
    url = State()
    photo = State()
    rating = State()
    video_link = State()
    video_tg_link = State()