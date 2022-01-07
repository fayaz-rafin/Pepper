import discord
import os
import random
from discord import embeds
from discord.ext import commands
import aiohttp
import json
import pprint
from keep_alive import keep_alive

client = commands.Bot(description="test", command_prefix="!")
bot = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                                 )  #Status of the bot
    print('We have logged in as {0.user}'.format(client))


#Need's work
@client.event
async def on_member_join(member):
    print(f'{member} just joined the server')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 0000:  #change the id to whoever you wanna annoy
        await message.channel.send('Stfu')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await client.process_commands(message)
    if any(word in message.content for word in greetings):
        await message.channel.send(random.choice(greetings_responses))

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(responses))

    if any(word in message.content for word in thanks):
        await message.channel.send(random.choice(thanks_responses))

    valid_users = ["fintasticツ#4854", "mehri#7476","dinnerbone#2187"]
    if str(message.author) not in valid_users:
        if any(word in message.content for word in swears):
            await message.channel.send(
                'Please, be family friendly {0.author.mention}'.format(message))

    if message.content.startswith('Bye'):
        await message.channel.send('Bye! {0.author.mention}'.format(message))

    if "nice" in message.content:
        await message.add_reaction("👍")

    #Commands i can use
    valid_users = ["fintasticツ#4854"]
    if str(message.author) in valid_users:
        if message.content.startswith('Right Pepper?'):
            await message.channel.send(
                'Your wish is my command {0.author.mention}'.format(message))

    #Counts how many users
    id = client.get_guild(
        804156381842243584)  #Change get_guild to ur server id
    valid_users = ["fintasticツ#4854"]  #Your username
    if str(message.author) in valid_users:
        if message.content == ">users":
            await message.channel.send(
                f"""No. of members = {id.member_count}""")


#Bot Commands
@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json?sort=hot") as r:
            res = await r.json()
            #pprint.pprint(res)
            data = res['data']['children'][random.randint(0,
                                                          25)]['data']['url']
            await ctx.send(data)


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "welcome":
            await client.send_message(
                f""" Welcome to the A-Team, {member.mention}! Please choose any character you'd like to have as a role. It can be any hero or villain. We hope you enjoy your stay!"""
            )


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
    "Howdy ", "Hey there", "Hello!", "How are you", "Konichiwa", "Hiya",
    "Selam", "salam aleykum", "Bonjour mon amie"
]

thanks = [
    "Thanks Pepper", "Thank you pepper", "thanks pepper", "thank you pepper",
    "thank you so much pepper", "I needed to hear that"
]

thanks_responses = ["Anytime chief :)", "Anytime :)", "Don't mention it!"]

swears = [
    "Bitch", "stfu", "faggot", "fag", "bainchod", "nigga", "nigger",
    "screw you", "Screw you", "FUCK", "F U C K", "BITCH", "SHIT", "shit",
    "fuck", "f u c k", "sh.it", "Sh.it", "SHlT"
]

keep_alive()

client.run(os.environ['TOKEN'])
