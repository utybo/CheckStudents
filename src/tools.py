import discord


class Tools:
    @staticmethod
    def convert(role: str):
        try:
            return int(role.replace(" ", "").lstrip("<@&").rstrip(">"))
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def got_the_role(role, user: discord.Member):
        """
        Check if a user got at least one role in author list
        """
        if isinstance(role, list):
            for i in role:
                if i in [y.id for y in user.roles]:
                    return True
        elif isinstance(role, int):
            return role in [y.id for y in user.roles]

    @staticmethod
    def name(member):
        """
        Return server nickname of a user, and if he doesn't have one, return his pseudo
        """
        if member.nick is not None:
            return member.nick
        else:
            return member.name

    @staticmethod
    async def embedError(channel, message):
        embed = discord.Embed(color=discord.Color.red(), title=message)
        embed.set_author(name="CheckStudents", url="https://github.com/Renaud-Dov/CheckStudents",
                         icon_url="https://raw.githubusercontent.com/Renaud-Dov/CheckStudents/master/img/logo.png")
        # embed.add_field(name="Permission Denied",value=message)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Renaud-Dov/CheckStudents/master/img/remove.png")
        await channel.send(embed=embed)
