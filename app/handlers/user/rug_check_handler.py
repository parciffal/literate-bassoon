from aiogram import Router, Bot, F
from aiogram.types import Message, ContentType


import logging


from app.config import Config
from app.tools.token_analitic import gopluslabs_manager
from app.tools.token_analitic.gopluslabs import get_link_keyboard

router = Router()


@router.message(F.content_type.in_({ContentType.TEXT}))
async def token_cmd_handler(message: Message, config: Config, bot: Bot):
    try:
        if message.text:
            if len(message.text) == 42 and message.text.startswith("0"):
                address = message.text
                msg, keyboard = await gopluslabs_manager.get_token_security(
                    address, bot
                )
                if keyboard is None:
                    await message.answer(msg, parse_mode="html")
                else:
                    keyb = await get_link_keyboard(keyboard)
                    await message.answer(msg, parse_mode="html", reply_markup=keyb)
            elif message.text.startswith("0") and (
                len(message.text) < 42 or len(message.text) > 42
            ):
                await message.answer(
                    "📵 <b> We're sorry, but the token you provided appears to be invalid.</b>"
                )
            elif message.text == "🫂 Social Media":
                msg = (
                    f"🕊️ X: \nhttps://twitter.com/zeroxsai\n\n"
                    f"🌐 Website: \nhttps://0xs.ai\n\n"
                    f"✈️ Telegram: \nhttps://t.me/zeroxsai\n\n"
                )
                await message.answer(msg)
            elif message.text == "💎 Advertisement":
                msg = f"🗞️Looking got good advertisement?🗞️\n🚀Get in touch with @Botindeed! 🚀"
                await message.answer(msg)
            elif message.text == "⛓️ Chain Support":
                msg = (
                    f"⛓️ <b>Supported Chains</b> ⛓️\n\n"
                    f"1. <b>Shibarium (SHIB) 🔗</b>\n"
                    f"2. <b>Ethereum (ETH) 🔗</b>\n"
                    f"3. <b>Binance Smart Chain (BSC) 🔗</b>\n"
                    f"4. <b>Optimism (OL) 🔗</b>\n"
                    f"5. <b>Cronos (CRONOS) 🔗</b>\n"
                    f"6. <b>OKExChain (OKC) 🔗</b>\n"
                    f"7. <b>Gnosis (GNOSIS) 🔗</b>\n"
                    f"8. <b>Polygon (MATIC) 🔗</b>\n"
                    f"9. <b>Fantom Opera (FTM) 🔗</b>\n"
                    f"10. <b>zkSync (zkSYNC) 🔗</b>\n"
                    f"11. <b>KCC (KCC) 🔗</b>\n"
                    f"12. <b>Avalanche (AVAX) 🔗</b>\n"
                    f"13. <b>Arbitrum (ARBITRUM) 🔗</b>\n"
                    f"14. <b>Base (BASE) 🔗</b>\n"
                    f"15. <b>Harmony (HARMONY) 🔗</b>\n"
                    f"16. <b>Ethereum Wanchain (ETHW) 🔗</b>\n"
                    f"16. <b>Ethereum Wanchain (ETHW) 🔗</b>\n"
                    f"18. <b>Tron (TRON) 🔗</b>\n"
                )
                await message.answer(msg)
    except Exception as e:
        await message.answer(
            "📵 <b> We're sorry, but the token you provided appears to be invalid or error appeared.\n Please try again later. </b>"
        )
        logging.error(e)
