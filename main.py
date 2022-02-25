import discum, random, time
bot = discum.Client(token="token-goes-here", log=False)

members = []
guilds = input("Guild ID: ")
channels = input("Channel ID: ")
times = input("Seconds between messages: ")

@bot.gateway.command
def higuy(resp): # sending messages will be started after typing "higuy"
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guilds, channels)
    if bot.gateway.finishedMemberFetching(guilds):
        bot.gateway.removeCommand(higuy)
        bot.gateway.close()
bot.gateway.run()
print("Starting add members.")
for memberID in bot.gateway.session.guild(guilds).members:
    members.append(memberID)
print("Starting to DM.")
for x in members:
    try:
        rand = random.randint(0,15)
        if rand == 15:
            print(f'Sleeping for 45 seconds.')
            time.sleep(45)
            print(f'Done sleeping!')
        print(f"Preparing to DM {x}.")
        messages = open("message.txt")
        time.sleep(int(times))
        newDM = bot.createDM([f"{x}"]).json()["id"]
        bot.sendMessage(newDM, f"{messages.read()}")
        print(f'DMed {x}.')
        messages.close()
    except Exception as E:
        print(E)
        print(f'Couldn\'t DM {x}.')
