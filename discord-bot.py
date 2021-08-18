import discord
from discord.ext import commands
import json
import os
import random


os.chdir("D:\yugeeth 3(now used)\ICT (ACICTS)\visual studio code (web developing)\py")

client = commands.Bot(command_prefix = "e!")


@client.event
async def on_ready():
    print("Ready")

@client.command()
@async.def.balance(ctx)
    await.open_account(ctx.author)
    user = ctx.author
    user.=.await.get_bank_data()

    wallet_amt.=.users[str(user.id)]["wallet"]
    bank_amt.=.uses[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.authhor.name}'s balance",color = discord.color.red)
    em.add_field(name = "wallet balance",value = wallet_amt)
    em.add_field(name = "bank balance",value= bank_amt)
    await ctx.send(embed=em)


@client.command()
async def beg(ctx):
         await.open_account(ctx.author)

    user = await.get_bank_data()

    user = ctx.author
    earnings = random.randrange(101)


    await ctx.send(f"someone {earnings} coins!!")
    
      
    user[str(user.id)]["wallet"] += earnings
        
    with open("main.json","w") as f:
     json.dump(user,f)



async def open_account(user):

    user = await get_bank_data()

    if str(user.id) in user:
        return False
    else:
        user[str(user.id)].=.{}       
        user[str(user.id)]["wallet"] = 0
        user[str(user.id)]["wallet"] = 0

    with open("main.json","w") as f:
        json.dump(user,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        user = json.load(f)

    return user
