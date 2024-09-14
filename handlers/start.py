from aiogram.types import Message
from aiogram.filters import CommandStart
from loader import router
from googletrans import Translator

# Tarjima funksiyasi
async def translate_text(text):
    try:
        translator = Translator()
        detected_lang = translator.detect(text).lang  # Matnning tilini aniqlash
        
        # Agar til o'zbekcha bo'lsa, inglizchaga tarjima qilish
        # Aks holda, o'zbek tiliga tarjima qilish
        target_lang = 'en' if detected_lang == 'uz' else 'uz'
        translated = translator.translate(text, dest=target_lang)
        
        return translated.text
    except Exception as e:
        return f"Xatolik yuz berdi: {e}"

@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer_sticker('CAACAgIAAxkBAAMDZtcpgyJiPVJSrWchsGesCx3nHxwAAm4AA0G1VgzQpYRy5txaiDUE')
    await msg.answer("Assalomu aleykum rahmatulloh!😊")
    await msg.answer("Matn yoki so'z yuboring!")

@router.message(lambda msg: msg.text is not None)
async def handle_translation(msg: Message):
    text = msg.text
    # Matnni tarjima qilish
    translated_text = await translate_text(text)
    await msg.answer(translated_text)
