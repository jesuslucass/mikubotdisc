import os
import random
import discord

pontos = 0 


p1 = "Pergunta1"
p2 = "Pergunta2"
p3 = "Pergunta3"
p4 = "Pergunta4"
p5 = "Pergunta5"

a= ["miku gif.gif","Miku.png","miku img 2.jpg"]

client = discord.Client()

@client.event

async def on_ready():
  print("We have logged in as {0.user}".format(client))
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$start"):
    await message.channel.send("\nO que você deseja fazer?\n \nOpções:\n \n1 Informações Gerais do Bot\n \n2 Sobre o Livro\n \n3 Resumo\n \n4 Quiz\n \n Se quiser todos os comandos:$help\n")
  
  if message.content.startswith("$1"):
    await message.channel.send("Informações Gerais do Bot")
    await message.channel.send(file=discord.File(random.choice(a)))
    await message.add_reaction('\N{THUMBS UP SIGN}')
    
  
  if message.content.startswith("$2"):
    await message.add_reaction('\N{THUMBS UP SIGN}')
    await message.channel.send("Sobre o Livro")
    
  
  if message.content.startswith("$3"):
    await message.add_reaction('\N{THUMBS UP SIGN}')
    await message.channel.send("Qual tema você quer resumo?")
    await message.channel.send("\nTema1\n \nTema2\n \nTema3\n")

  if message.content.startswith("$tema1"):
    await message.channel.send("tema 1")

  elif message.content.startswith("$tema2"):
    await message.channel.send("tema2")
    
  elif message.content.startswith("$tema3"):
    await message.channel.send("tema3")
    
  elif message.content.startswith("$todos"):
    await message.channel.send("Todos os temas \nTema1\n \nTema2\n \nTema3\n")
  
  if message.content.startswith("$4"):
    await message.add_reaction('\N{THUMBS UP SIGN}')
    await message.channel.send("Quiz")

    await message.channel.send(p1)
    await message.channel.send(p2)
    await message.channel.send(p3)
    await message.channel.send(p4)
    await message.channel.send(p5)
    

  if message.content.startswith("$help"): 
    
    await message.author.send('Comandos do bot')


        
client.run(os.environ['Token'])



