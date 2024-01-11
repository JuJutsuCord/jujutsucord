# embeds.py
import discord

class Embeds:
    @staticmethod
    def create_embed(title, description, color, image_url=None, thumbnail_url=None):
        embed = discord.Embed(title=title, description=description, color=color)
        
        if image_url:
            embed.set_image(url=image_url)
        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)

        return embed
