from telethon import events



import asyncio



from userbot.utils import admin_cmd











@borg.on(admin_cmd("tauba"))



async def _(event):



    if event.fwd_from:



        return



    animation_interval = 1.5

    



    animation_ttl = range(0, 9)



    await event.edit("Abey Saale!")



    animation_chars = [

            "Tauba",

            "Tauba",

            "sara",

            "mood" ,

            "kharab",

            "kar",

            "diya",

            "**Tauba Tauba Sara Mood Kharab Kardiya**"

        ]



    for i in animation_ttl:





        await event.edit(animation_chars[i % 9])

        await asyncio.sleep(animation_interval)

            
