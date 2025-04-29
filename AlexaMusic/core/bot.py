AlexaMusic/core/bot.py

import asyncio from ..logging import LOGGER

class AlexaBot: def init(self): self.name = "Alexa" self.running = False

async def start(self):
    self.running = True
    LOGGER(__name__).info(f"{self.name} botu başlatıldı.")
    try:
        while self.running:
            LOGGER(__name__).info(f"{self.name} çalışıyor...")
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        LOGGER(__name__).info("Bot durduruldu.")

async def stop(self):
    self.running = False
    LOGGER(__name__).info(f"{self.name} botu durduruldu.")

Eğer doğrudan çalıştırılırsa

if name == "main": bot = AlexaBot() loop = asyncio.get_event_loop() try: loop.run_until_complete(bot.start()) except KeyboardInterrupt: loop.run_until_complete(bot.stop())

