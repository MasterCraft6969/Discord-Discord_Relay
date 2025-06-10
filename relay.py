import discord

BOT_TOKEN = "YOUR_BOT_TOKEN"


SOURCE_SERVER_ID = 0000000000000000  
SOURCE_CHANNEL_ID = 000000000000000000
DESTINATION_SERVER_ID = 000000000000000  
DESTINATION_CHANNEL_ID = 0000000000000000


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


async def relay_message(message, destination_channel_id):
    if message.author == client.user:
        return

    try:
        destination_channel = client.get_channel(destination_channel_id)
        if not destination_channel:
            print("Destination channel not found.")
            return

        member = message.author  
        
        embed = discord.Embed() 
        if message.embeds: 
             embed = message.embeds[0].copy() 

        embed.set_author(name=member.name, icon_url=member.display_avatar.url) 

        embed_color = member.color
        if embed_color.value != 0:  
            embed.color = embed_color
            
        if not embed.description: 
            embed.description = message.content or "*No message content*"

        if not message.embeds:
             embed.description = message.content or "*No message content*" 

        if message.attachments:
            embed.set_image(url=message.attachments[0].url) 


        await destination_channel.send(embed=embed)  


    except discord.HTTPException as e:
        print(f"Error relaying message: {e}")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == SOURCE_CHANNEL_ID:
        await relay_message(message, DESTINATION_CHANNEL_ID)
    elif message.channel.id == DESTINATION_CHANNEL_ID:
        await relay_message(message, SOURCE_CHANNEL_ID)


client.run(BOT_TOKEN)
