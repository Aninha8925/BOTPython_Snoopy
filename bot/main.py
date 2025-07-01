import discord #importando biblioteca
from discord.ext import commands, tasks
from datetime import time
import os

token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all() #criando var que contém as permissões pro bot
bot = commands.Bot(".", intents=intents) #representa o bot

#criar eventos
@bot.event #evento disparado quando bot liga
async def on_ready():
    sincs= await bot.tree.sync()
    print(f"{len(sincs)} comandos sincronizados!")
    DarBomDia.start()
    print("Bot inicializado com sucesso")

@bot.event
async def on_message(msg:discord.message):
    if msg.author.bot:
        return
    await bot.process_commands(msg)
    #await msg.reply(f"O usuário {msg.author.mention} enviou uma mensagem no canal {msg.channel.name}")



@bot.event #tenha em mente o id, 
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1387263016034242673)
    await canal.send(f"{membro.mention} entrou no servidor! seja bem vindo!")

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f"O membro {membro.name} reagiu a messagem com {reacao.emoji}")


#criar comandos
@bot.command()
async def ola(ctx:commands.Context):#não pode espaço
    nome =ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?") #ctx é uma abreviação de contexto que guarda todas as informações importantes

@bot.command()
async def repita(ctx:commands.Context, *,texto):
   await ctx.send(texto)

@bot.command()
async def repita2(ctx:commands.Context, texto, argumento_2):
   await ctx.send(texto)
   await ctx.send(argumento_2)

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
   resultado = num1 + num2
   await ctx.send(f"A soma entre {num1} e {num2} é igual {resultado}")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = "Título da embed"
    minha_embed.description = "Descrição da embed"

    imagem = discord.File("bot/imagens/bomdia.jpeg", "bom_dia.jpeg")
    minha_embed.set_image(url="attachment://bom_dia.jpeg")
    minha_embed.set_thumbnail(url="attachment://bom_dia.jpeg")

    minha_embed.set_footer(text="banana")

    minha_embed.set_author(name="Goku", icon_url="https://imgs.search.brave.com/1NmwPqr2SEXICzlcw7fxuM1OKgMAocBbsOio-yV7lqs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtd2l4bXAtZWQz/MGE4NmI4YzRjYTg4/Nzc3MzU5NGMyLndp/eG1wLmNvbS9mL2Vl/NTBiYjM3LWIxNDYt/NGE4Yy05Y2EwLWU4/Nzg2ZWUzMTZlNS9k/OWQzbmtzLTc2NGU3/NjI4LWRmZDEtNDNj/NS05MmZmLTRlZGZh/MTY5YjA5ZS5qcGcv/djEvZmlsbC93XzEw/MjQsaF82MzYscV83/NSxzdHJwL2RyYWdv/bmJhbGxfc3VwZXJf/X2dva3VfcGljdHVy/ZV8xX19mcm9tX2lu/dHJvX19ieV9hbnRo/b255am1vX2Q5ZDNu/a3MtZnVsbHZpZXcu/anBnP3Rva2VuPWV5/SjBlWEFpT2lKS1Yx/UWlMQ0poYkdjaU9p/SklVekkxTmlKOS5l/eUp6ZFdJaU9pSjFj/bTQ2WVhCd09qZGxN/R1F4T0RnNU9ESXlO/alF6TnpOaE5XWXda/RFF4TldWaE1HUXlO/bVV3SWl3aWFYTnpJ/am9pZFhKdU9tRndj/RG8zWlRCa01UZzRP/VGd5TWpZME16Y3pZ/VFZtTUdRME1UVmxZ/VEJrTWpabE1DSXNJ/bTlpYWlJNlcxdDdJ/bkJoZEdnaU9pSmNM/MlpjTDJWbE5UQmlZ/ak0zTFdJeE5EWXRO/R0U0WXkwNVkyRXdM/V1U0TnpnMlpXVXpN/VFpsTlZ3dlpEbGtN/MjVyY3kwM05qUmxO/ell5T0Mxa1ptUXhM/VFF6WXpVdE9USm1a/aTAwWldSbVlURTJP/V0l3T1dVdWFuQm5J/aXdpYUdWcFoyaDBJ/am9pUEQwMk16WWlM/Q0ozYVdSMGFDSTZJ/anc5TVRBeU5DSjlY/VjBzSW1GMVpDSTZX/eUoxY200NmMyVnlk/bWxqWlRwcGJXRm5a/UzUzWVhSbGNtMWhj/bXNpWFN3aWQyMXJJ/anA3SW5CaGRHZ2lP/aUpjTDNkdFhDOWxa/VFV3WW1Jek55MWlN/VFEyTFRSaE9HTXRP/V05oTUMxbE9EYzRO/bVZsTXpFMlpUVmNM/MkZ1ZEdodmJubHFi/Vzh0TkM1d2JtY2lM/Q0p2Y0dGamFYUjVJ/am81TlN3aWNISnZj/Rzl5ZEdsdmJuTWlP/akF1TkRVc0ltZHlZ/WFpwZEhraU9pSmpa/VzUwWlhJaWZYMC54/aGRLTHk2R1hsRWdK/dFA5NUFHMl9jWVhz/dGlKTVR0bml0Rnhy/cmMzZnZZ", url="https://www.youtube.com/@ColoniaContraAtaca")

    await ctx.reply(embed=minha_embed,file=imagem)



@tasks.loop(time=time(8, 30))
async def DarBomDia():
    canal= bot.get_channel(1387263016034242673)
    await canal.send("Bom dia seus lindos")

@bot.tree.command()
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f"Olá {interact.user.name}!")
    await interact.followup.send(f"Comando utilizado co  sucesso")
    #ephemeral=True

#defer deixa o bot em standby

@bot.tree.command()
async def falar(interact:discord.Interaction, texto:str):
    await interact.response.send_message(texto)

#bot run tem que está em último no código
bot.run("token")#id do bot