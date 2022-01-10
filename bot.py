import os
from discord.ext import commands
from datetime import datetime
import time

def main():

    TOKEN_JON = "ODcwMDU5NTM4NDk2MjI5NDE3.YQHQFg." + "lzmsM9PMEVM7kY4bHCdOUNCkeq8"

    token = os.getenv("DISCORD_TOKEN")
    client = commands.Bot(command_prefix="?")

    @client.event
    async def on_ready():
        print(f"{client.user.name} is connected to Discord")

    @client.event
    async def on_message(ctx):
        if(ctx.content.startswith("hello")):
            current_time = datetime.now.strftime("%H:%M:%S")          
            await ctx.channel.send("hi -" + + current_time)
            
    client.run(TOKEN_JON)


# entry point
if __name__ == '__main__':
    main()