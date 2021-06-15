import discord
import os
import random
from discord.ext import commands

client = discord.Client()
from keep_alive import keep_alive

client = commands.Bot(command_prefix='>')

swears = [
    "fuck", "fucking", "shit", "shitty", "retard", "Fuck", "Shit", "bitch",
    "Bitch", "stfu", "faggot", "fag", "bainchod", "nigga", "nigger", "gay",
    "screw you", "Screw you"
]

sad_words = [
    "sad", "unhappy", "depressed", "anxiety", "anxious", "pessimistic",
    "disappointing"
]
responses = [
    "Before you diagnose yourself with depression or low self esteem, first make sure that you are not in fact, just surrounding yourself with assholes.",
    "Sometimes the appropriate response to reality is to go insane.",
    "Cheer up when the night comes, because mornings always give you another chance",
    "Depression brings people closer to the church, but so do funerals.",
    "Life is too short for us to dwell on sadness. Cheer up and live life to the fullest",
    "In the middle of difficulty lies opportunity.",
    "Let your smile change the world. But don’t let the world change your smile",
    "Someday, everything will make perfect sense. So for now, laugh at the confusion, smile through the tears, and keep reminding yourself that everything happens for a reason",
    "You don’t always need a plan. Sometimes you just need to breathe, trust, let go and see what happens",
    "Life is not a problem to be solved but a gift to be enjoyed",
    "Fly high, do or die, dare to dream, cheer to the extreme!"
]

greetings = [
    "hi pepper", "Hey Pepper", "Hello Pepper", "Hi", "Hi Pepper", "Hi pepper",
    "Hello pepper", "hello pepper"
]

greetings_responses = [
    "Howdy ", "Hey there", "Hello!", "How are you", "Konichiwa", "Hiya"
]

thanks = ["Thanks Pepper","Thank you pepper","thanks pepper","thank you pepper","thank you so much pepper","I needed to hear that"]

thanks_responses = ["Anytime chief :)","Anytime :)","Don't mention it!","Always here to help!","You're most welcome 🤗","🙏 ","Happy to help out!"]

#Messsage on startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="Fayaz"))#Status of the bot
    print('We have logged in as {0.user}'.format(client))

#Messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(
            'Hi there!{0.author.mention}'.format(message))
#reaction
    if "nice" in message.content:
        await message.add_reaction("👍")
#commands only i can use
    valid_users = ["fintasticツ#4854"]
    if str(message.author) in valid_users:
        if message.content.startswith('Right Pepper?'):
            await message.channel.send(
                'Your wish is my command {0.author.mention}'.format(message))
#listen and response from arrays
    if any(word in message.content for word in greetings):
        await message.channel.send(random.choice(greetings_responses))

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(responses))

    if any(word in message.content for word in thanks):
        await message.channel.send(random.choice(thanks_responses))

        if any(word in message.content for word in swears):
            await message.channel.send(
                'Please watch ur  language {0.author.mention}'.format(message))

#Counts the no. of members in my server
    id = client.get_guild(804156381842243584)
    valid_users = ["fintasticツ#4854"]
    if str(message.author) in valid_users:
        if message.content == ">users":
            await message.channel.send(
                f"""No. of members = {id.member_count}""")

#Welcome message to anyone who joins my server
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "welcome":
            await client.send_message(
                f""" Welcome to the A-Team, {member.mention}! Please choose any character you'd like to have as a role. It can be any hero or villain. We hope you enjoy your stay!"""
            )

#keeps the bot alive by hosting it from Replit servers
keep_alive()
client.run(os.environ['TOKEN'])
