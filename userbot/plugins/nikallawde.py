from telethon import events



import asyncio



from userbot.utils import admin_cmd











@borg.on(admin_cmd("nikal"))



async def _(event):



    if event.fwd_from:



        return



    animation_interval = 0.5

    



    animation_ttl = range(0, 9)



    await event.edit("**Madarchod**")



    animation_chars = [

            "**Nikal**",

            "**Lawde**",

            "**Pehli**",

            "**Fursat**" ,

            "**Mai**",

            "**Nikal**",

            "**Nikal Lawde Pehli Fursat Mai Nikal**"

        ]



    for i in animation_ttl:





        await event.edit(animation_chars[i % 9])

        await asyncio.sleep(animation_interval)

            
