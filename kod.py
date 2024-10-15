import requests
import os

import discord
import random
from discord.ext import commands
 
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command() 
async def pomoc(ctx):
    await ctx.send("Oto lista komend:")

    await ctx.send("Pomoc - lista komend i sposób działania bota")
    await ctx.send("!segregacja - informacje dotyczące segregacji śmieci")
    await ctx.send("!rozkład - informacje dotyczące rozkładu śmieci")
    await ctx.send("!palenie - porady odnośnie palenia")

@bot.command() 
async def segregacja(ctx):
    await ctx.send("Co wrzucać do jakiego kosza?")

    await ctx.send("Odpady plastikowe i metalowe (np: butelki plastikowe i puszki) - żółty kosz")
    await ctx.send("Odpady bio (np: resztki jedzenia i skórki owoców) - brązowy kosz")
    await ctx.send("Odpady zmieszane (np: odchody zwierząt, zawartość odkurzacza i porozbijane naczynia) - czarny kosz")
    await ctx.send("Odpady papierowe (np: stare papiery i kartony) - niebieski kosz")
    await ctx.send("Odpady szklane (np: butelki i słoiki bez uszkodzeń) - zielony kosz")

@bot.command() 
async def palenie(ctx):
    await ctx.send("Serio weź nie pal (chyba że w kominku/piecu z użyciem drewna bądź papieru)")  


@bot.command() 
async def rozkład(ctx):
    await ctx.send("Oto lista wybranych odpadów i ich przewidywany czas rozkładu:")

    await ctx.send("Opona gumowa - średnio 80 lat")
    await ctx.send("kubek styropianowy - 50 la")
    await ctx.send("niedopalony papieros - 5 lat")
    await ctx.send("guma do żucia - 5 lat")
    await ctx.send("drewniane krzesło - 20 lat")
    await ctx.send("materiał bawełniany - 1-5 miesięcy")

