async def new_member_welcome_dm(member, GUILD):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello there {member.name}, welcome to {GUILD}!'
    )