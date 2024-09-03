from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


dp = Dispatcher()
router = Router()
bot = Bot(token="YOUR_BOT_TOKEN",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp.include_router(router=router)