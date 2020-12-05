reaction_config = {
    784585338122272768: { # verification channel
        "✅": [784579235200237618] # moneybag and relevant role
    },
    784599049969205268: {
        "🎓": [784599110393004073], # alumni role
        "🐝": [784564632782241802], # CO25 role
        "🕐": [784600043008950292], # pending decision
        "👴": [782057745804296212], # boomer
    },
    784601720248074240: {
        "♂️": [784568874758045726],  # he/him,
        "♀️": [784568897202159637], # she/her,
        "☮️": [784568921633587221], # they/them,
        "🌈": [784602983450148865], # lgbtq+
    },
    784604476429697056: {
        "🍑": [784604492708053056], # in-state
        "🇺🇸": [784604570084704327], # out of state
        "🗺️": [784604587331420200], # intl
    }
}

async def handler(ctx, payload, state):
    print(payload)
    m_id = payload.message_id
    if m_id not in reaction_config:
        return

    e_name = payload.emoji.name
    if e_name not in reaction_config[m_id]:
        return

    g_id = payload.guild_id
    u_id = payload.user_id
    guild = ctx.get_guild(g_id)
    member = await guild.fetch_member(u_id)

    print(g_id, u_id, guild, member)

    print(f"Assigning {member}")

    for r_id in reaction_config[m_id][e_name]:
        role = guild.get_role(r_id)
        if state == "add":
            await member.add_roles(role, reason="Reaction request fulfillment.")
        else:
            await member.remove_roles(role, reason="Reaction request fulfillment.")