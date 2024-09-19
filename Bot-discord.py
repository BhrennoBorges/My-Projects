import discord
import requests
import json
import random

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/jokes/random/250')
    json_data = json.loads(response.text)
    joke = json_data[0] if json_data else {'setup': 'No joke found', 'punchline': ''}
    return f"{joke['setup']} \n{joke['punchline']}"

def play_gamble():
    symbols = ['🍒', '🍇', '🍉', '7️⃣']
    results = random.choices(symbols, k=3)
    result_string = ' | '.join(results)
    if results.count('7️⃣') == 3:
        return f"{result_string}\nJackpot! 💰"
    else:
        return f"{result_string}\nThanks for playing!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$meme'):
            meme_url = get_meme()
            await message.channel.send(meme_url)
        
        elif message.content.startswith('$gamble'):
            result_message = play_gamble()
            await message.channel.send(result_message)
        
        elif message.content.startswith('$jokes'):
            joke = get_joke()
            await message.channel.send(joke)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Your Token Here')
