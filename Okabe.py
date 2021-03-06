import discord
from os import getenv
from random import *
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

bot = commands.Bot(command_prefix = "!", description = "Bot by Vic")

@bot.event
async def on_ready():
    print("Ready !")


#HOW TO PLAY  
@bot.command()
async def how(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="HELP ⚙️")
    embed.add_field(name="!drop", value="Pour drop une réponse d'Okabe!", inline=False)
    embed.add_field(name="!reward", value="Pour voir les récompenses de drop de réponses de différentes rareté", inline=False)
    embed.add_field(name="!pack", value="Pour récupérer un Gift d'Okabe", inline=False)
    embed.add_field(name="!collection[numéro]", value="Pour voir votre collection de mesages(numéro de joueur épinglé)", inline=False)
    embed.add_field(name="!top", value="Pour voir le classement et score des meilleurs joueurs", inline=False)
    await ctx.send(embed=embed)

#REWARD
@bot.command()
async def reward(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="REWARD 🏆")
    embed.add_field(name="🟡 Légendaire", value="Pour 1 légendaire: ⚙️ + 3🎟️ + 10,000,000💰", inline=False)
    embed.add_field(name="🟣 Epique", value="Pour 5 épiques: 1🎟️ + 5,000,000💰", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Pour 40 très rares: 1🎟️ + 2,500,000💰", inline=False)
    embed.add_field(name="🟠 Rare", value="Pour 200 rares: 1🎟️ + 1,000,000💰", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Pour 800 peu commun: 1,000,000💰", inline=False)
    await ctx.send(embed=embed)

#NAME
#vic
tl1=0
te1=0
ttr1=17
tr1=64
tpc1=297
s1=tpc1*1+tr1*10+ttr1*100+te1*1000+tl1*25000
#theo
tl2=0
te2=0
ttr2=7
tr2=75
tpc2=307
s2=tpc2*1+tr2*10+ttr2*100+te2*1000+tl2*25000
#doud
tl3=0
te3=0
ttr3=0
tr3=4
tpc3=12
s3=tpc3*1+tr3*10+ttr3*100+te3*1000+tl3*25000
#loujok
tl4=0
te4=0
ttr4=7
tr4=37
tpc4=163
s4=tpc4*1+tr4*10+ttr4*100+te4*1000+tl4*25000


#COLLECTION
@bot.command()
async def collection1(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COLLECTION - Vic 📚")
    embed.add_field(name="🟡 Légendaire", value="Total:" f"{tl1}" " Différents:0/2", inline=False)
    embed.add_field(name="🟣 Epique", value="Total:" f"{te1}" " Différents:0/3", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Total:" f"{ttr1}" " Différents:[5/5]", inline=False)
    embed.add_field(name="🟠 Rare", value="Total:" f"{tr1}" " Différents:[7/7]", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Total:" f"{tpc1}" " Différents:[12/12]", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def collection2(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COLLECTION - Theo 📚")
    embed.add_field(name="🟡 Légendaire", value="Total:" f"{tl2}" " Différents:0/2", inline=False)
    embed.add_field(name="🟣 Epique", value="Total:" f"{te2}" " Différents:0/3", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Total:" f"{ttr2}" " Différents:4/5", inline=False)
    embed.add_field(name="🟠 Rare", value="Total:" f"{tr2}" " Différents:[7/7]", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Total:" f"{tpc2}" " Différents:[12/12]", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def collection3(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COLLECTION - Doud' 📚")
    embed.add_field(name="🟡 Légendaire", value="Total:" f"{tl3}" " Différents:0/2", inline=False)
    embed.add_field(name="🟣 Epique", value="Total:" f"{te3}" " Différents:0/3", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Total:" f"{ttr3}" " Différents:0/5", inline=False)
    embed.add_field(name="🟠 Rare", value="Total:" f"{tr3}" " Différents:1/7", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Total:" f"{tpc3}" " Différents:3/12", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def collection4(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x636363)
    embed.set_author(name="COLLECTION - Loujok 📚")
    embed.add_field(name="🟡 Légendaire", value="Total:" f"{tl4}" " Différents:0/2", inline=False)
    embed.add_field(name="🟣 Epique", value="Total:" f"{te4}" " Différents:0/3", inline=False)
    embed.add_field(name="🟢 Très Rare", value="Total:" f"{ttr4}" " Différents:3/5", inline=False)
    embed.add_field(name="🟠 Rare", value="Total:" f"{tr4}" " Différents:6/7", inline=False)
    embed.add_field(name="🔵 Peu commun", value="Total:" f"{tpc4}" " Différents:[12/12]", inline=False)
    await ctx.send(embed=embed)

#TOP
classement=[s1,s2,s3,s4]
classement.sort()
n1=classement[3]
n2=classement[2]
n3=classement[1]
n4=classement[0]
if n1==s1:
    name1="Vic"
elif n1==s2:
    name1="Theo"
elif n1==s3:
    name1="Doud"
elif n1==s4:
    name1="Loujok"
if n2==s1:
    name2="Vic"
elif n2==s2:
    name2="Theo"
elif n2==s3:
    name2="Doud"
elif n2==s4:
    name2="Loujok"
if n3==s1:
    name3="Vic"
elif n3==s2:
    name3="Theo"
elif n3==s3:
    name3="Doud"
elif n3==s4:
    name3="Loujok"
if n4==s1:
    name4="Vic"
elif n4==s2:
    name4="Theo"
elif n4==s3:
    name4="Doud"
elif n4==s4:
    name4="Loujok"

@bot.command()
async def top(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━", color=0x636363)
    embed.set_author(name="TOP 🏆")
    embed.add_field(name="#1 " f"{name1}", value=f"{n1}" " pts", inline=False)
    embed.add_field(name="#2 " f"{name2}", value=f"{n2}" " pts", inline=False)
    embed.add_field(name="#3 " f"{name3}", value=f"{n3}" " pts", inline=False)
    embed.add_field(name="#4 " f"{name4}", value=f"{n4}" " pts", inline=False)
    await ctx.send(embed=embed)   

#PROBA
liste = (range(1000000))
liste0 = (range(1000))
debut = ["Hey!", "Hi!", "Hello there"]
commun = ["Hmmmmm", "Still here?", "Pfff...", "2929831831...", "The people are like garbage", "I have to go on @channel", "No way...", "I hate that Alpacaman...", "I'm tired", "Are you serious?", "drop? haha", "Not today", "Don't disturb me", "...", "What are you waiting for?", "Stop doing that", "My name is Hououin Kyouma"]
peucommun = ["Mission complete!", "Okey-Dokey !", "it's time to send a D-Mail...", "I'm the man who will destroy your ambitions.", "Butterfly Effect", "Gel-Banana...", "Oh-ha~! ♫", "The drink of the chosen ones, Dr Pepper !", "Daru, my Super Hacker!", "The Organization is chasing me after all.", "Future Gadget #1: The Bit Particle Gun!", "Future Gadget #2: The Bamboo Helicam!"]
rare = ["Future Gadget #6: the Cyalume Saber!", "Human is dead, mismatch", "The Time Leap Machine!", "the IBN 5100!", "Metal Upa!", "The Divergence Meter!", "Christina, my assistant !"]
tresrare = ["Fuahahahaha", "Huh? Mayushii's watch has stopped...", "The Reading Steiner!", "Future Gadget #8: the Phone Microwave!", "Tuturu! ♫"]
épique = ["I am the great mad scientist, HOUOUIN KYOUMA!", "Space has a beginning, but it has no end - infinite", "Stars too have a beginning, but are by their own power destroyed - finite"]
légendaire = ["El Psy Kongroo...", "This is the choice of Steins;Gate..."]
rec = (range(10000))


#DROP
hey=0
ope=0
opi=0
@bot.command()
async def drop(ctx):
    global hey
    global ope
    global opi
    opi = opi+0
    ope = ope+0
    hey = hey+1
    nb = choice(rec)
    a = choice(debut)
    b = choice(liste)
    c = choice(commun)
    d = choice(peucommun)
    e = choice(rare)
    f = choice(tresrare)
    g = choice(épique)
    h = choice(légendaire)
    if b==144078:
        print(b, ": légendaire")
        embed=discord.Embed(title=h, color=0xfff829)
        await ctx.send(embed=embed)
        await ctx.send("tag @Vic pour avoir ce message dans ta collection ! (légendaire)")
        if nb==500:
            print("-> giftx3!")
            embed=discord.Embed(title="🎁 Gift x3 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+3
    elif 20<=b<=35:
        print(b, ": épique")
        embed=discord.Embed(title=g, color=0xc955d8)
        await ctx.send(embed=embed)
        await ctx.send("tag @Vic pour avoir ce message dans ta collection ! épique)")
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 1400<=b<=1600:
        print(b, ": très rare")
        embed=discord.Embed(title=f, color=0x35d070)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 45033<=b<=46533:
        print(b, ": rare")
        embed=discord.Embed(title=e, color=0xf4911f)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif 345500<=b<=355550:
        print(b, ": peu commun")
        embed=discord.Embed(title=d, color=0x5aa7ce)
        await ctx.send(embed=embed)
        if nb==500:
            print("-> gift!")
            embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+1
    elif b==0 or b==1000000:
        print("-> mega gift!")
        embed=discord.Embed(title="🎁 MEGA Gift ! (fais vite la commande `!pack`)", color=0xffffff)
        await ctx.send(embed=embed)
        opi=opi+1
    else:
        if hey==1:
            await ctx.send("**🆕 Your collection has been uptaded!**" )
            await ctx.send(a)
        else:
            await ctx.send(c)
            if 500<=nb<=600:
                print("-> gift!", nb)
                embed=discord.Embed(title="🎁 Gift ! (fais vite la commande `!pack`)", color=0xffffff)
                await ctx.send(embed=embed)
                ope=ope+1
            if 0<=nb<=10 or nb==1000:
                print("-> gift!x3")
                embed=discord.Embed(title="🎁 Gift x3 (fais vite la commande `!pack`)", color=0xffffff)
                await ctx.send(embed=embed)
                ope=ope+3
#GIFT
@bot.command()
async def pack(ctx):
    global ope
    global opi
    a = choice(debut)
    b = choice(liste)
    c = choice(commun)
    d = choice(peucommun)
    e = choice(rare)
    f = choice(tresrare)
    g = choice(épique)
    h = choice(légendaire)
    if ope>=1:
        await ctx.send("All I want to say is...")
        nb = choice(rec)
        ope=ope-1
        if 0<=nb<=1000:
            print("-> giftx3!")
            embed=discord.Embed(title="🎁 Gift x3 (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+3
        if 1000<nb<=2500:
            print("-> giftx2!")
            embed=discord.Embed(title="🎁 Gift x2 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+2
        elif 2500<nb<8400:
            print("gift : peu commun")
            embed=discord.Embed(title=d, color=0x5aa7ce)
            await ctx.send(embed=embed)
        elif 8400<=nb<=9835:
            print("gift : rare")
            embed=discord.Embed(title=e, color=0xf4911f)
            await ctx.send(embed=embed)
        elif 9835<nb<=9993:
            print("gift : très rare")
            embed=discord.Embed(title=f, color=0x35d070)
            await ctx.send(embed=embed)
        elif 9993<nb<10000:
            print(b, ": épique")
            embed=discord.Embed(title=g, color=0xc955d8)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! (épique)")
        elif nb==10000:
            print("-> giftx10!")
            embed=discord.Embed(title="🎁 Gift x10 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+10
    elif opi>=1:
        await ctx.send("Lucky...")
        nb = choice(rec)
        opi=opi-1
        if nb<6000:
            print("mega gift : très rare")
            embed=discord.Embed(title=f, color=0x35d070)
            await ctx.send(embed=embed)
        
        elif 6000<=nb<8000:
            print("-> giftx10!")
            embed=discord.Embed(title="🎁 Gift x10 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+10
        elif 8000<=nb<=9800:
            print("mega gift : épique")
            embed=discord.Embed(title=g, color=0xc955d8)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! épique)")
        elif 9800<nb<9900:
            print("mega gift : légendaire")
            embed=discord.Embed(title=h, color=0xfff829)
            await ctx.send(embed=embed)
            await ctx.send("tag @Vic pour avoir ce message dans ta collection ! (légendaire)")
        elif 9900<=nb<=10000:
            print("-> giftx30!")
            embed=discord.Embed(title="🎁 Gift x30 ! (fais vite la commande `!pack`)", color=0xffffff)
            await ctx.send(embed=embed)
            ope=ope+30
    else:
        embed=discord.Embed(title="❌ There isn't any gift ❌", color=0x636363)
        await ctx.send(embed=embed)
    
#DR0P
@bot.command()
@cooldown(1, 3600, BucketType.user)
async def dr0p(ctx):
    z = choice(liste0)
    if 743<=z<=747:
        print(z, ": Hououin Kyoumaaaa ``aka Mad Scientist``")
        embed=discord.Embed(title="Hououin Kyoumaaaa ``aka Mad Scientist``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Kyouma_Hououin.png'))
    elif 358<=z<=378:
        print(z, ": Makise Kurisu ``aka Christina``")
        embed=discord.Embed(title="Makise Kurisu ``aka Christina``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Kurisu_Makise.jpg'))
    elif 888<=z<=908:
        print(z, ": Okabe Rintaro ``aka Okarin``")
        embed=discord.Embed(title="Okabe Rintaro ``aka Okarin``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Rintarou_Okabe.jpg'))
    elif 220<=z<=270:
        print(z, ": Hashida Daru ``aka Supah Hakah``")
        embed=discord.Embed(title="Hashida Daru ``aka Supah Hakah``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Daru_Hashida.jpg'))
    elif 510<=z<=560:
        print(z, ": Shiina Mayuri ``aka Mayushii``")
        embed=discord.Embed(title="Shiina Mayuri ``aka Mayushii``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Mayuri_Shiina.jpg'))
    elif 150<=z<=200:
        print(z, ": Amane Suzuha ``aka Working Warrior``")
        embed=discord.Embed(title="Amane Suzuha ``aka Working Warrior``", color=0xfff829)
        await ctx.send(embed=embed, file=discord.File('Suzuha_Amane.jpg'))
    else:
        embed=discord.Embed(title="Nothing here...", color=0x8b8989)
        await ctx.send(embed=embed)
@dr0p.error
async def command_dr0p_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Pas de ``dr0p`` disponible!",description=f"Try again in {error.retry_after:.2f}s.", color=0x575757)
        await ctx.send(embed=em)

#C0LLECTI0N
@bot.command()
async def c0llecti0n1(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━", color=0x575757)
    embed.set_author(name="C0LLECTI0N - Vic 🧪")
    embed.add_field(name="Lab Member 001", value="???????", inline=False)
    embed.add_field(name="Lab Member 002", value="???????", inline=False)
    embed.add_field(name="Lab Member 003", value="???????", inline=False)
    embed.add_field(name="Lab Member 004", value="???????", inline=False)
    embed.add_field(name="Lab Member 005", value="???????", inline=False)
    embed.add_field(name="Lab Member 006", value="???????", inline=False)
    embed.add_field(name="Lab Member 007", value="???????", inline=False)
    embed.add_field(name="Lab Member 008", value="???????", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def c0llecti0n2(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━", color=0x575757)
    embed.set_author(name="C0LLECTI0N - Theo 🧪")
    embed.add_field(name="Lab Member 001", value="???????", inline=False)
    embed.add_field(name="Lab Member 002", value="???????", inline=False)
    embed.add_field(name="Lab Member 003", value="???????", inline=False)
    embed.add_field(name="Lab Member 004", value="???????", inline=False)
    embed.add_field(name="Lab Member 005", value="???????", inline=False)
    embed.add_field(name="Lab Member 006", value="???????", inline=False)
    embed.add_field(name="Lab Member 007", value="???????", inline=False)
    embed.add_field(name="Lab Member 008", value="???????", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def c0llecti0n3(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━", color=0x575757)
    embed.set_author(name="C0LLECTI0N - Doud' 🧪")
    embed.add_field(name="Lab Member 001", value="???????", inline=False)
    embed.add_field(name="Lab Member 002", value="???????", inline=False)
    embed.add_field(name="Lab Member 003", value="???????", inline=False)
    embed.add_field(name="Lab Member 004", value="???????", inline=False)
    embed.add_field(name="Lab Member 005", value="???????", inline=False)
    embed.add_field(name="Lab Member 006", value="???????", inline=False)
    embed.add_field(name="Lab Member 007", value="???????", inline=False)
    embed.add_field(name="Lab Member 008", value="???????", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def c0llecti0n4(ctx):
    embed=discord.Embed(title=" ━━━━━━━━━━━━━━━━━━━━━", color=0x575757)
    embed.set_author(name="C0LLECTI0N - Loujok 🧪")
    embed.add_field(name="Lab Member 001", value="???????", inline=False)
    embed.add_field(name="Lab Member 002", value="???????", inline=False)
    embed.add_field(name="Lab Member 003", value="???????", inline=False)
    embed.add_field(name="Lab Member 004", value="???????", inline=False)
    embed.add_field(name="Lab Member 005", value="???????", inline=False)
    embed.add_field(name="Lab Member 006", value="???????", inline=False)
    embed.add_field(name="Lab Member 007", value="???????", inline=False)
    embed.add_field(name="Lab Member 008", value="???????", inline=False)
    await ctx.send(embed=embed)


bot.run(getenv('TOKEN'))

