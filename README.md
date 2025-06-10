# Discord to Discord Relay
## Link two discord channels with one another

## How does it work?
It uses the bot (not webhooks because they get rate limited easier) to transfer over messages with embeds. The embeds support embedded links, images and other bots embeds. The embeds contain the profile and name of the person with the sidebar being the color of the highest role that, that person has. 

Here is how it looks in action
![1000057279](https://github.com/user-attachments/assets/246324a3-2f07-4787-98e8-2b490c43979a)
![1000057281](https://github.com/user-attachments/assets/83d2b3e2-d234-4d15-9a88-7f15c32d943e)

# How to install/use (python needs to be installed)

Open your desired terminal and run:
`git clone https://github.com/MasterCraft6969/Discord-Discord_Relay/ && cd Discord-Discord_Relay/ && pip install discord.py`

Then open relay.py and change YOUR_BOT_TOKEN to your bot token, SOURCE_SERVER_ID to the first server (doesn't matter which is the first or second) ID, SOURCE_CHANNEL_ID to the channel ID of that first server, DESTINATION_SERVER_ID to the second server ID, DESTINATION_CHANNEL_ID to the channel ID of that second server and then in your terminal run:
`python relay.py` (whilst being in the directory of the file)
