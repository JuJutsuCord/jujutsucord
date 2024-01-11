# guilds.py
class GuildsInfo:
    @staticmethod
    def get_server_info(guild):
        # Implement detailed logic to retrieve server information
        member_count = sum(1 for member in guild.members if not member.bot)
        bot_count = sum(1 for member in guild.members if member.bot)
        channels_info = f'Text Channels: {len(guild.text_channels)}\nVoice Channels: {len(guild.voice_channels)}'
        owner = guild.owner.name if guild.owner else 'Not available'
        created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S')
        
        return f'Server Info: {guild.name}, {guild.id}\n' \
               f'Members: {member_count} (Bots: {bot_count})\n' \
               f'Owner: {owner}\n' \
               f'Channels: {channels_info}\n' \
               f'Created at: {created_at}'
