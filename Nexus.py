import asyncio
import discord
import aiohttp
#from discord.ext.commands import Bot
from discord.ext import commands
import random
from bs4 import BeautifulSoup as soup

bot = commands.Bot(command_prefix='!')

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


def userornah():
    proxy = ""
    while proxy == "":
        proxy = random_line("proxies.txt")

    try:
        proxytest = proxy.split(":")[2]
        userpass = True
    except IndexError:
        userpass = False
    if userpass == True:
        ip = proxy.split(":")[0]
        port = proxy.split(":")[1]
        userpassproxy = ip + ":" + port
        proxyuser = proxy.split(":")[2].rstrip()
        proxypass = proxy.split(":")[3].rstrip()

    if userpass:
        proxies = {'http': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy,
                   'https': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy}

        proxies = "http://" + proxyuser + ':' + proxypass + '@' + userpassproxy
    if not userpass:
        proxies = "http://{}".format(proxy)

    return proxies


def page_content(page):
    page_soup = soup(page, 'html.parser')
    watch_link = page_soup.find('a', {'class': ' '})
    return watch_link['href']


def page_content2(page):
    page_soup = soup(page, 'html.parser')
    if 'ADDEDTO' in page_soup.text:
        print('added to watch list')

    else:
        print('no idiot')
        #print(page_soup)

# def page_content3(page):
#     page_soup = soup(page, 'html.parser')
#     print(page_soup)

firstname = ["Jackson", "Aiden", "Sophia", "Emma", "Olivia", "Lucas", "Ava", "Liam", "Mia", "Noah", "Ethan", "Isabella", "Riley", "Caden", "Aria", "Mason", "Elijah", "Zoe", "Lily", "Michael", "Benjamin", "Emily", "James", "Chloe", "Abigail", "Avery", "Evelyn", "Daniel", "Jack", "Madison", "Caleb", "Alexander", "Daniel", "Jack", "Evelyn", "Isaac", "Cameron", "Julian", "Eli", "Peyton", "Mackenzie", "Maria", "Camilla", "John", "Lincoln", "Brayden", "Victoria"]
lastname = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
     "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Lewis", "Hall", "Allen",
     "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzales", "Nelson",
     "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Stewart",
     "Sanchez", "Morris"]

def loopityloop(itemlink, numberofwatchers):
    loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.gather(*(create_account(itemlink) for x in range(int(numberofwatchers)))))
    asyncio.gather(*(create_account(itemlink) for x in range(numberofwatchers)))

def loopityloop2(itemlink, numberofviews):
    asyncio.gather(*(viewthis(itemlink) for x in range(int(numberofviews))))

async def create_account(itemlink):

    first = random.choice(firstname)
    last = random.choice(lastname)
    email = first + last + str(random.randint(00000,10000)) + '@gmail.com'
    url = 'https://reg.ebay.com/reg/PartialReg'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        # "Content-Length": "1295",
        "Content-Type": "application/x-www-form-urlencoded",
        #"DNT": "1",
        "Host": "reg.ebay.com",
        "Origin": "https://reg.ebay.com",
        #ORIGINAL "Referer": "https://reg.ebay.com/reg/PartialReg?siteid=0&co_partnerId=0&UsingSSL=1&rv4=1&pageType=3984&ru=https%3A%2F%2Fmy.ebay.com%2Fws%2FeBayISAPI.dll%3FMyEbayBeta%26MyEbay%3D%26gbh%3D1%26guest%3D1&signInUrl=https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1%26pageType%3D3984%26ru%3Dhttps%253A%252F%252Fmy.ebay.com%252Fws%252FeBayISAPI.dll%253FMyEbayBeta%2526MyEbay%253D%2526gbh%253D1%2526guest%253D1",
        "Referer": "https://reg.ebay.com/reg/PartialReg?ru=https%3A%2F%2Fwww.ebay.com%2F",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        #"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36" #CHANGED 9/25

    }

    data = {

        "isSug": "false",
        "countryId": "1",
        "userid": "",
        "ru": "https://www.ebay.com",
        "firstname": first,
        "lastname": last,
        "email": email,
        "PASSWORD": 'sadCheetah69',
        "promotion": "true",
        "iframeMigration1": "true",
        "mode": "1",
        "frmaction": "submit",
        "tagInfo":"",
        #"tagInfo": 'ht5%3DAQAAAWXfrUENAAUxNjYwZjM2M2IwYi5hYWQ3NjdhLjJiZDE5LmZmZmNmZmU5y63XnpR95RLU8Mv3KuFYGy%252Fr3u0*%7Cht5new%3Dfalse%26usid%3D4c14777b1660aade1c10690afffd1462', #original TagInfo
        #"tagInfo": 'ht5%3DAQAAAWXfrUENAAUxNjYwZjYxYTlmNi5hYmM2NjFiLjQ1ZmJhLmZmZmM4OWU1rp13lY%252FhVto1tsEk5Z19OLKmx4U*%7Cht5new%3Dtrue%26usid%3D0f61a9f61660abc661b45fbafffc89e4', #changed 9/25
        # "tagInfo": 'ht5%3DAQAAAWWsLakOAAUxNjViN2Y4MmE2NC5hNDgyMmZjLjczNTU3LmZmZmZlYmNkutBiUPfY5KE9GOep8hH5mfnR7xI*%7Cht5new%3Dfalse%26usid%3D' + str(
        # tmxSessionId),
        "hmvb": "",
        "isGuest": "0",
        "idlstate": "",
        "profilePicture": "",
        "agreement": "Terms and conditions",
        "signInUrl": "https%3A%2F%2Fsignin.ebay.com%2Fws%2FeBayISAPI.dll%3FSignIn%26regUrl%3Dhttps%253A%252F%252Freg.ebay.com%252Freg%252FPartialReg", #ORIGINAL
        #'signInUrl': 'https%3A%2F%2Fsignin.ebay.com%2Fws%2FeBayISAPI.dll%3FSignIn%26ru%3Dhttps%253A%252F%252Fwww.ebay.com%252F%26regUrl%3Dhttps%253A%252F%252Freg.ebay.com%252Freg%252FPartialReg%253Fru%253Dhttps%25253A%25252F%25252Fwww.ebay.com%25252F', #CHANGED 9/25
        "personalFlag": "true",
        "isMobilePhone": "",
        "_trksid": "p2052190",
        # "_trksid": trksid,
        #"ets": "AQADAAAAEIqCgeCg9oW5tDS30Hfl7Aw", #original ets
        "ets": "AQADAAAAEPwtodbFg38It4o27gMyZL4" #changed 9/25
        # "ets": ets
    }

    # "https": proxy1


    print('creating account with {}'.format(email))

    headers3 = {
        "authority": "www.ebay.com",
        "method": "GET",
        "path": itemlink[20::],
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

    }


    proxy1 = userornah()
    #print(proxy1)
    #proxy1 = "http://{}".format(proxy1)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data, proxy=proxy1) as resp:
            #page_content3(await resp.text())
            async with session.get(itemlink, headers=headers3, proxy=proxy1) as resp1:
                watch_link = page_content(await resp1.text())
                async with session.get(watch_link, headers=headers3, proxy=proxy1) as resp2:
                    page_content2(await resp2.text())

global count
async def viewthis(itemlink):
    count = 0
    headers3 = {
        "authority": "www.ebay.com",
        "method": "GET",
        "path": itemlink[20::],
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

    }

    proxy2 = userornah()
    # proxy2 = random_line('proxies.txt')
    # proxy2 = "http://{}".format(proxy2)


    async with aiohttp.ClientSession() as session1:
        try:
            async with session1.get(itemlink, headers=headers3, proxy=proxy2) as resp1:
                print('item viewed')
        except aiohttp.client_exceptions.ClientHttpProxyError:
            print('item not viewed')
        except aiohttp.client_exceptions.ClientConnectorSSLError:
            print('item not viewed')
        except aiohttp.client_exceptions.ServerDisconnectedError:
            print('item not viewed')
# @bot.event
# async def on_command_error(error, ctx):
#     if isinstance(error, commands.CommandOnCooldown):
#         await bot.send_message(ctx.message.channel, content='This command is on a %.2fs cooldown' % error.retry_after)
#     raise error

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        error_time = error.retry_after/60.0/60.0
        embed = discord.Embed(title='You cannot use this command for the next %.2f hours' % error_time)
        await bot.send_message(ctx.message.channel, embed=embed)

    raise error

@bot.command(pass_context = True)
@commands.cooldown(3, 86400, commands.BucketType.user)
async def watch(ctx, *args):
    mesg = ' '.join(args)
    mesg = mesg.split(' ')
    itemlink = mesg[0]
    if 'www.ebay.com' in itemlink:
        try:
            number_of_watchers = mesg[1]
            number_of_watchers = int(number_of_watchers)
            if number_of_watchers > 10:
                embed = discord.Embed(title='Cannot send over 10 watchers at a time')
                await bot.send_message(ctx.message.channel, embed=embed)
                return
        except IndexError:
            embed = discord.Embed(title="You need to add the number of watchers after the link!", color=0xe74c3c)
            embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
            await bot.send_message(ctx.message.channel, embed=embed)
            return

        embed = discord.Embed(title="Sending {} Watchers...".format(number_of_watchers), color=0xc27c0e)
        embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
        await bot.send_message(ctx.message.channel, embed=embed)
        bot.send_message(ctx.message.channel, embed=embed)

    else:
        embed = discord.Embed(title="Incorrect Link! Link needs to start with www.ebay.com", color=0xe74c3c)
        embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
        await bot.send_message(ctx.message.channel, embed=embed)
        bot.send_message(ctx.message.channel, embed=embed)
        return

    loopityloop(itemlink, number_of_watchers)
    embed = discord.Embed(title="Successfully Sent {} Watchers!".format(number_of_watchers), color=0x2ecc71)
    embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
    await bot.send_message(ctx.message.channel, embed=embed)
    #await Mike.delete_message(ctx.message)
    #return await bot.say(mesg[0])

@bot.command(pass_context = True)
@commands.cooldown(3, 86400, commands.BucketType.user)
async def view(ctx, *args):
    mesg = ' '.join(args)
    mesg = mesg.split(' ')
    itemlink = mesg[0]
    if 'www.ebay.com' in itemlink:
        try:
            number_of_views = mesg[1]
            number_of_views = int(number_of_views)
            if number_of_views > 200:
                embed = discord.Embed(title='Cannot send over 200 views at a time')
                await bot.send_message(ctx.message.channel, embed=embed)
                return
        except IndexError:
            embed = discord.Embed(title="You need to add the number of views after the link!", color=0xe74c3c)
            embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
            await bot.send_message(ctx.message.channel, embed=embed)
            return
        embed = discord.Embed(title="Sending {} Views...".format(number_of_views), color=0xc27c0e)
        embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
        await bot.send_message(ctx.message.channel, embed=embed)
        bot.send_message(ctx.message.channel, embed=embed)
    else:
        embed = discord.Embed(title="Incorrect Link! Link needs to start with www.ebay.com", color=0xe74c3c)
        embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
        await bot.send_message(ctx.message.channel, embed=embed)
        bot.send_message(ctx.message.channel, embed=embed)
        return

    loopityloop2(itemlink, number_of_views)
    embed = discord.Embed(title="Successfully Sent {} Views!".format(number_of_views), color=0x2ecc71)
    embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def format(ctx):
    embed = discord.Embed(title='Format:\n\n`!view <ebay link> <# of views desired>` \n`!watch <ebay link> <# of watchers desired>\n\n You are allowed 2 watch commands and 2 view commands per day!`', color=0x3498db)
    embed.set_footer(text='Nexus Retro - @k0rnsyrup', icon_url='https://cdn.discordapp.com/attachments/499432680870641674/499432749216563201/nexus.png')
    await bot.send_message(ctx.message.channel, embed=embed)
    bot.send_message(ctx.message.channel, embed=embed)


@bot.event
async def on_ready():
    print('------')
    print('Logged in as ' + bot.user.name)
    print(bot.user.id)
    print('------')
    print('Made by k0rndawg')
    print('ready when you are, dude')
    print('------')







if __name__ == '__main__':
    bot.run('NDk5NDMzMzI2NTE2MzcxNDY5.Dp8NKA.j4rU9m_IJtcpIa9k4Woudnc2uyY')







