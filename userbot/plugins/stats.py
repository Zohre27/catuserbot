import time

from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User


@bot.on(admin_cmd(pattern="stat$"))
@bot.on(sudo_cmd(pattern="stat$", allow_sudo=True))
async def stats(event):
    cat = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📌 **Stats for {full_name}** \n\n"
    response += f"**Private Chats:** {private_chats} \n"
    response += f"   ★ `Users: {private_chats - bots}` \n"
    response += f"   ★ `Bots: {bots}` \n"
    response += f"**Groups:** {groups} \n"
    response += f"**Channels:** {broadcast_channels} \n"
    response += f"**Admin in Groups:** {admin_in_groups} \n"
    response += f"   ★ `Creator: {creator_in_groups}` \n"
    response += f"   ★ `Admin Rights: {admin_in_groups - creator_in_groups}` \n"
    response += f"**Admin in Channels:** {admin_in_broadcast_channels} \n"
    response += f"   ★ `Creator: {creator_in_channels}` \n"
    response += (
        f"   ★ `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n"
    )
    response += f"**Unread:** {unread} \n"
    response += f"**Unread Mentions:** {unread_mentions} \n\n"
    response += f"📌 __It Took:__ {stop_time:.02f}s \n"
    await cat.edit(response)


@bot.on(admin_cmd(pattern="stat c$"))
@bot.on(sudo_cmd(pattern="stat c$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            hi.append([entity.title, entity.id])
    output = "**The channels you are in are: **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of channels in which you are",
        )


@bot.on(admin_cmd(pattern="stat ca$"))
@bot.on(sudo_cmd(pattern="stat ca$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            if entity.creator or entity.admin_rights:
                hi.append([entity.title, entity.id])
    output = "**The channels in which you are admin are : **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of channels in which you are admin ",
        )


@bot.on(admin_cmd(pattern="stat co$"))
@bot.on(sudo_cmd(pattern="stat co$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            if entity.creator:
                hi.append([entity.title, entity.id])
    output = "**The channels in which you are owner are : **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of channels in which you are owner ",
        )


@bot.on(admin_cmd(pattern="stat g$"))
@bot.on(sudo_cmd(pattern="stat g$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            hi.append([entity.title, entity.id])
    output = "**The groups you are in are: **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of groups in which you are",
        )


@bot.on(admin_cmd(pattern="stat ga$"))
@bot.on(sudo_cmd(pattern="stat ga$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            if entity.creator or entity.admin_rights:
                hi.append([entity.title, entity.id])
    output = "**The groups in which you are admin are: **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of groups in which you admin ",
        )


@bot.on(admin_cmd(pattern="stat go$"))
@bot.on(sudo_cmd(pattern="stat go$", allow_sudo=True))
async def stats(event):
    catevent = await edit_or_reply(event, "`Collecting stats, Wait man`")
    start_time = time.time()
    hi = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            if entity.creator:
                hi.append([entity.title, entity.id])
    output = "**The groups in which you are owmer are: **\n\n"
    for k, i in enumerate(hi, start=1):
        output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
    stop_time = time.time() - start_time
    output += f"\n**Time Taken : ** {stop_time:.02f}s"
    try:
        await catevent.edit(output)
    except:
        await edit_or_reply(
            catevent,
            output,
            caption="The list of groups in which you owner ",
        )


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CMD_HELP.update(
    {
        "stats": "**Plugin : **`stats`\
    \n\n**Syntax : **`.stats`\
    \n**Function : **Shows you the count of  your groups, channels, private chats...etc"
    }
)
