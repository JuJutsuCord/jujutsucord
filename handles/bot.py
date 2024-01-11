# bot.py
from JuJutsuCord import JuJutsuCord, jjcord
from embeds import Embeds
from customcommands import CustomCommands

bot = JuJutsuCord(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@jjcord.command(name='serverinfo')
async def server_info(ctx):
    # Implement serverinfo command logic with embeds
    guild_info = GuildsInfo.get_server_info(ctx.guild)
    embed = Embeds.create_embed(title='Server Information', description=guild_info, color=discord.Color.blue())
    await ctx.send(embed=embed)

@jjcord.command(name='userinfo')
async def user_info(ctx):
    # Implement userinfo command logic with embeds
    user_info = UserInfo.get_user_info(ctx.author)
    embed = Embeds.create_embed(title='User Information', description=user_info, color=discord.Color.green())
    await ctx.send(embed=embed)

@jjcord.command(name='customcommand')
async def custom_command(ctx, *args):
    # Implement custom command logic with embeds
    result = CustomCommands.execute_command(ctx, *args)
    embed = Embeds.create_embed(title='Custom Command Result', description=result, color=discord.Color.gold())
    await ctx.send(embed=embed)

@jjcord.command(name='createcommand')
async def create_command(ctx, command_name, *args):
    # Implement custom command creation logic with embeds
    result = CustomCommands.create_command(ctx, command_name, *args)
    embed = Embeds.create_embed(title='Create Command Result', description=result, color=discord.Color.purple())
    await ctx.send(embed=embed)

# Add other @jjcord.command implementations

# Start the bot and keep it running
if __name__ == '__main__':
    bot_token = 'YOUR_BOT_TOKEN'
    bot.run(bot_token)
