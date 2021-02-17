import discord
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
from random import choice
import os
from keepalive import keep_alive



intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client=commands.Bot(command_prefix= "!",intents=intents)

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("Köleniz emrinize hazırdır"))
    change_status.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member :discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f"Banned {member.mention}")
@ban.error
async def ban_error(ctx,error):
    await ctx.channel.send('Geçersiz Komut.')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*, member):
    banned_users= await ctx.guild.bans()
    member_name,member_discriminator=member.split('#')

    for ban_entry in banned_users:
        user=ban_entry.user

        if(user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
@unban.error
async def unban_error(ctx,error):
    await ctx.channel.send('Geçersiz Komut.')



@client.command()
async def darbe(ctx):
    user = ctx.message.author
    if user.id != 376390237867343921:
        return 
    for i in range(0,20):
        i +=1 
        await ctx.channel.send("Darbe Yapıom")

    
@client.command()
@commands.has_permissions(manage_messages=True)
async def temizle(ctx,amount : int):
    message_list=[]
    await ctx.channel.purge(limit=amount+1)
    sent_message =await ctx.channel.send(f"**{amount}** adet mesaj sildim. ")
    message_list.append(sent_message)
    await asyncio.sleep(3)
    await ctx.channel.delete_messages(message_list)

@temizle.error
async def clear_error(ctx,error):
    await ctx.channel.send('Geçersiz Komut.')



@client.command()
@commands.has_permissions(ban_members=True)
async def sustur(ctx,victim: discord.Member):
    user = ctx.message.author
    role =get(user.guild.roles,name='Banned')

    if role in victim.roles:
        return

    else:
        await victim.add_roles(role)
        await ctx.channel.send('https://tenor.com/view/spongebob-ban-pubg-lite-banned-rainbow-gif-16212382')


@client.command(name="ping")
async def ping(ctx):
    await  ctx.send(f"Gecmikmen:  {round(client.latency*1000)}ms")
    if client.latency*1000 > 100:
        await ctx.send("Abu senin internet galiba kaçak")
    else:
         await  ctx.send("İnternetin iyi")

@client.command(name="selam")
async def selam(ctx):
    geridonus = ["As Ciğerim", "Sen kimsin birader", "Napim.", "??????", "Ben türkçe bilmiyor", "هل تعرف اللغة العربية","Ne oldu gene", "Beni mi çağırmıştınız uwu", "Maaşımı öde", "Geleceğin tony sparkıyım","sınavlara çalışıyorum konuşma benle"]
    await ctx.send(choice(geridonus))
@client.command()
@commands.has_permissions(ban_members=True)
async def susturmakaldir(ctx,victim: discord.Member):
    user= ctx.message.author
    role =get(user.guild.roles,name='Banned')

    if role not in victim.roles:
        return

    else:
        await victim.remove_roles(role)
    

@client.command()
async def gununsozu(ctx):
    user = ctx.message.author

    await ctx.channel.send(f"{user.mention} Doğum Günüm!!!!")

@client.command()
async def gununvideosu(ctx):
    user = ctx.message.author
    await ctx.channel.send(f"{user.mention} https://www.youtube.com/watch?v=pTmiCUob4cU&ab_channel=IsmetYavuz ")

status = ["Konser veriyor", "Yemek yiyom.", "Uyuyom","Sınavlara çalışıyorum!", "Signed by serhan", "Spordayım","Yeni Özellik Gelecek"]
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


keep_alive()
client.run(os.getenv("token"))

""" Banned adında bir rol oluşturulacak """