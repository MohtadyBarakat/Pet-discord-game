age = 0
hunger = '100%'
import discord
from pets import all_pets
import pickle
import os
import users


current_pets = {}
all_user = {}


if 'data_base.bb' in os.listdir ('./'):
    file_open = open("data_base.bb", "rb")
    current_pets = pickle.load(file_open)
    file_open.close()
    print (current_pets)

async def start_game(msg):
    await msg.channel.send (f'''Welcome {msg.author.id}, This is Wonder land. in wonder land you can creat, raise, sell, buy pets and a lot more...
let's start with species, you can choose Dragon, Cat, Dog and Bird. each animal have a special sound and they can marry each other to creat a new animal
Dragon can growl, pokemon can creat a fire blast, cat can mewo, dog can bark and bird can sing. to creat a pet you will need to type:
!pet creat 'your pet's species without the"' 'your pet's name without the"''
REMEMBER you can't give two pet's the same name. be creative you mo**** f*****....sorry that was rude just be creative OK???''')

def pet_name_creat (msg):
    name = msg.content.split(' ')[-1]
    return name

async def congrats_new_pet(msg, name, specs):
    await msg.channel.send (f'''Awww {name}, that's a cute name! now you will need to take care of your new {specs}.
let's start by explaining how to write a command:
!pet 'your order' 'your pet's name' now let's walk through orders:
feed: is to feed your {specs}. remember your {specs} needs to be fed every 5 mins
check hunger: is to check on your {specs}'s hunger
check age: to check how old is your {specs} now
play: to play with your {specs}
check_joy: is to check if your {specs} id joyfull  or need your attention. remeber your {specs} will get bored after 3 hours''')

    if specs == 'cat':
        await msg.channel.send("meow: to make your cat meow")
    if specs == 'dog':
        await msg.channel.send("bark: to make your dog bark")
    if specs == 'dragon':
        await msg.channel.send("growl: to make your dragon growl")
    if specs == 'bird':
        await msg.channel.send("sing: to make your bird sing")
    if specs == 'pokemon':
        await msg.channel.send("fire_blast: to make your pokemon blast a fire")

async def Call (msg):
    order = msg.content.split(" ")[1]
    name = pet_name_creat (msg)
    if not msg.author.id in all_user:
        new_user = users.User(user_id = msg.author.id)
        all_user[msg.author.id]=new_user
    elif msg.author.id in all_user:
        new_user = all_user[msg.author.id]
    if order == "start":
        await start_game(msg)
    elif order == "creat":
        ###!prt creat specs gender name 
        specs = msg.content.split(" ")[2]
        gender = msg.content.split(" ")[-2]
        output,con = new_user.Buy()
        await msg.channel.send(output)
        try:
            if con == 0:
                if gender == 'm' or gender == 'f':
                    new_pet = all_pets[specs](name=name, spec=specs, gender=gender)
                    await congrats_new_pet(msg, name, specs)
                    if not msg.author.id in current_pets: 
                        all_user[msg.author.id]={}
                    current_pets[msg.author.id][name] = new_pet
        except: pass

    elif order == "marry":
        second_pet = msg.content.split(" ")[-1]
        first_pet = msg.content.split(" ")[2]
        first_pet = current_pets[msg.author.id][first_pet]
        second_pet = current_pets[msg.author.id][second_pet]
        output = first_pet.Marry(second_pet)
        await msg.channel.send(output)



    elif order == "give_birth":
        ####!pet give_birth (name) from first_pet secon_pet
        second_pet = msg.content.split(" ")[-1]
        first_pet = msg.content.split(" ")[-2]
        name = msg.content.split(" ")[2]
        first_pet = current_pets[msg.author.id][first_pet]
        second_pet = current_pets[msg.author.id][second_pet]
        output, new_pet = first_pet.Give_birth(second_pet,name)
        print('1')
        await msg.channel.send(output)
        if not msg.author.id in current_pets: 
            current_pets[msg.author.id]={}
            print('2')
        current_pets[msg.author.id][name] = new_pet
        print('3')

    elif order == "ls":
        if not msg.author.id in current_pets:
            await msg.channel.send(f"You ain't got nothing...really nothing broke bitch")
            return
        await msg.channel.send("your pets are: " + ", ".join(current_pets[msg.author.id].keys()))
    else:
        if not msg.author.id in current_pets or not name in current_pets[msg.author.id]:
            await msg.channel.send(f"You don't own {name}")
            return
        

        output = current_pets[msg.author.id][name](order)
        await msg.channel.send(output)

    file_open = open("data_base.bb", "wb")
    pickle.dump(current_pets, file_open)
    file_open.close()
        

        
        


client = discord.Client()


@client.event
async def on_message(message):
    
    inp = message.content
    if message.author.bot: 
        return
    
    if message.content.startswith('!pet'):
        try: await Call(message)
        except Exception as exc:
            print('the error is:',exc)
            await message.channel.send("PLAY FAIR YOU *******")

    elif message.content.startswith('!repeat_me'):
        await message.channel.send(inp)


print("client running, open discord ...")
client.run('OTI3MjgzMjkyMjcxNzA2MTMz.YdH93A.xOfPXdFqrOlmsw_DCsWWqi0c5iQ')