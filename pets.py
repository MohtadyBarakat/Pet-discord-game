import random
from time import time
from time_calc import time_min_f,time_hour_f, time_second_f, last_feed_f, last_play_f, age_f, genesis_f


class Pet:
    def __init__(self, name, spec, gender, hunger='100%', joy='bored'):
        self.name = name
        self.age = 0
        self.spec = spec
        self.hunger = hunger
        self.joy = joy
        self.genesis = int(time())
        self.gender = gender

    def Stat (self):
        print('name:',self.name)
        print('age:',round (self.age)) 
        print('type:',self.spec)
        print('hunger:',self.hunger)
        
        return f"name: {self.name}\n\
                age: {round(self.age)}\n\
                type: {self.spec}\n\
                hunger: {self.hunger}\n\
                Joy: {self.joy}\n\
                "


    def Age (self):
        age = age_f(self)
        print (age)
        return (age)

    
    def Check_age (self):
        age = age_f(self)
        print (age)
        return f'{age}'
        
    
    def Check_hunger (self):
        time_hour = time_hour_f(self)
        if int(time_hour) == 0 or int(time_hour) == 1:
            self.hunger = '0%'
            print (self.hunger)
        elif int(time_hour)%5 == 0:
            self.hunger = '100%'
            print (self.hunger)
        elif int(time_hour)%4 == 0:
            self.hunger = '75%'
            print (self.hunger)
        elif int(time_hour)%3 == 0:
            self.hunger = '50%'
            print (self.hunger)
        elif int(time_hour)%2 == 0:
            self.hunger = '25%'
            print (self.hunger)
        
        return self.hunger

    def Feed (self):
        last_feed = last_feed_f(self)
        self.hunger = '0%'
        print ('Hunger:',self.hunger)
        return f'Hunger: {self.hunger}'

    def Check_joy (self):
        time_hour = time_hour_f(self)
        if int(time_hour) == 0 or int(time_hour) == 1 :
            self.joy = 'Joyfull'
        elif int(time_hour)%3 == 0 :
            self.joy = 'Bored'
        elif int(time_hour)%2 == 0 :
            self.joy = 'Started to get bored'
        print(self.joy)
        return self.joy
        

    def Play (self):
        last_play = last_play_f(self)
        self.joy = 'Joyfull'
        print ('Joy:',self.joy)
        return f'Joy: {self.joy}'

    def Marry (self,second_pet):
        age = age_f(self)
        if self.gender == 'm' and second_pet.gender == 'f' or self.gender == 'f' and second_pet.gender == 'm':
            if age == 0 or age > 0 :
                print('done')
                self.married_to = second_pet
                second_pet.married_to = self
                if self == second_pet:
                    return "you can't fuck yourself"
                return f'{self.name} is married to {second_pet.name}'
            else:
                print (f"your pet's age is {self.age}. it's too young for marriege")
                return f"your pet's age is {self.age}. it's too young for marriege. that's child abuse you son of a bird"
        else:
            return "pets must have diffrent genders to get married"

    def Give_birth (self,second_pet,name):
        print('IN')
        age = age_f(self)
        print('age')
        if self.age and second_pet.age > 0 or self.age == 0 :
            if self.married_to == second_pet:
                new_pet = all_pets[self.spec](name=name, spec=self.spec)
                return f'{name} has been born', new_pet
            else:
                return "what about a wedding first huh?"
        else :
            print ("Oh really!!? HAHAHA. BITCH go raise your pet's first they are too young UGH!")
            return "Oh really!!? HAHAHA. BITCH go raise your pet's first they are too young UGH!"


    def __call__(self, stat, *arg, **kwargs):
        stat = stat.capitalize()
        return getattr(self, stat)(*arg, **kwargs)

class Dog (Pet):
    def Bark (self):
        print('Woooof')
        return('Woooof')

class Cat (Pet):
    def Meow (self):
        print('Meow')
        return('Meow')

class Dragon (Pet):
    def Growl (self):
        print('Growl')
        return('GROWWWWWWL')

class Pokemon (Pet):
    def Fire_blast (self):
        print('Fire')
        return('FIIIIRRRREEEE')

class Bird (Pet):
    def Sing (self):
        print('Sing')
        return('Seow Seow Seow')



all_pets = {"pet":Pet, "dog":Dog, "cat":Cat, "pokemon":Pokemon, "dragon":Dragon, 'bird':Bird}  


def test_pet():
    hunger = '100%'

    print ("Welcome to Tady's game. first of all you need to select a pet species from the following: Dragon, Cat, Dog, Pokemon and Dolphen")


    spec = ['dragon', 'cat', 'dog', 'pokemon']
    spec_choice = input ("choose yor pet species: ")



    print ("Perfect choice!!! Now choose your pet's name")
    
    name = input ('input the pet name: ')
    if not spec_choice in all_pets: 
        print("WRONG species mother lover")
        return 
    print(all_pets[spec_choice])
    pet = all_pets[spec_choice](name = name, spec = spec_choice, hunger = hunger)

    print ("Awww that's a cute name! now you will need to take care of it first of all let's walk through orders")
    print ("first of all you can check the status of your pet by typing 'stat'")
    print ("to feed your pet type 'feed' and to check on it's hunger type 'check hunger'")
    print ("your pet will get hungry every 5 minutes. Take care to feed it!!")
    print ("every 5 mins your et get's one year older and to chek it's age type 'check age'")




    while True:
        stat = input ("type your order:")
        # pet.(stat)
        pet(stat)
        


if __name__ == "__main__":
    test_pet()