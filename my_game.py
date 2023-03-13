"""Game"""
class Street():
    """streets of game"""
    def __init__(self, name):
        """Work with class"""
        self.name = name
        self.description = ''
        self.side = []
        self.character = None
        self.items = None
        self.end = False

    def set_description(self, description):
        """Description of street"""
        self.description = description

    def get_details(self):
        """Print details of street"""
        print(self.name)
        print("--------------------")
        print(self.description)
        for street in self.side:
            print(f'{street[0].name} {street[1]}')

    def link_street(self, other_street, side):
        """Information of linked street"""
        self.side.append([other_street, side])

    def set_character(self, character):
        """Is someone in street"""
        self.character = character

    def get_character(self):
        """Return Enemy street"""
        return self.character

    def move(self, where):
        """Move in other street"""
        for street in self.side:
            if street[1]== where:
                return street[0]

    def get_item(self):
        """Return item in street"""
        return self.items

    def set_item(self, items):
        """Add item in street"""
        self.items = items

    def end_street(self):
        """End street"""
        self.end = True

class Character:
    """Class Character for characters in streets"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        """Print information of character"""
        print(f'{self.name} тут')
        print(self.description)

    def set_conversation(self, conversation):
        """Add conversation"""
        self.conversation = conversation

    def talk(self):
        """Character talk"""
        if self.conversation is not None:
            print(self.name + " сказав: " + self.conversation)
        else:
            print(self.name + " не хоче говорити")
    def give_money(self):
        """Give money to enemy"""
        print('Ви дали гроші')

class Enemy(Character):
    """Class of enemy of streets"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.conversation = None

    def fight(self):
        """Fight with enemy"""
        print("Ви вдарили його в пах, а він навзаєм вдарив у обличчя")

    def shout(self):
        """Shout"""
        print('Ви закричали та привернули увагу людей')

    def run(self):
        """Run"""
        print('Ви втікли')

class DangerousEnemy(Enemy):
    """Class of dangerous enemy(killers, maniac)"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.conversation = None

    def call_police(self):
        """Call to police"""
        print('Ви подзвонили в поліцію')

class Friend(Character):
    """Class of friends"""
    def __init__(self, name, description):
        super().__init__(name, description)
        self.conversation = None

    def hug(self):
        """Hug"""
        print(self.name + " обняла тебе навзаєм")

class Item():
    """Class Item for items in street"""
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        """Add description of item"""
        self.description = description

    def describe(self):
        """Print description of item"""
        print(f"На цій вулиці є {self.name}, а саме {self.description}")

    def get_name(self):
        """Return name of item"""
        return self.name

kozelnytska = Street("вул. Козельницька")
kozelnytska.set_description("Вулиця у Сихівському районі міста Львова, у місцевості Персенківка.")

ivana_franka = Street("вул. Івана Франка")
ivana_franka.set_description("Сучасна вулиця Івана Франка простягається\
 від площі Соборної повз Стрийський базар аж до вулиці Панаса Мирного.")

yaroslava_stetska = Street("вул. Ярослава Стецька")
yaroslava_stetska.set_description("Вулиця Ярослава Стецька забудована \
переважно у стилях історизм, конструктивізм, сецесія. Більшість будинків\
 внесені до реєстру пам'яток архітектури місцевого значення.")
shevchenka = Street('вул. Шевченка')
shevchenka.set_description('Вулиця у Львові, одна із семи важливих\
 транспортних магістралей Львова.')

ave = Street('Площа')
ave.set_description("Площа Ринок - це серце та головна визначна пам'ятка Львова,\
 сукупність архітектурних пам'ятників Середньовіччя.")
ave.end_street()

kozelnytska.link_street(ivana_franka, "спереду")
ivana_franka.link_street(kozelnytska, "позаду")
ivana_franka.link_street(yaroslava_stetska, "спереду")
yaroslava_stetska.link_street(ivana_franka, "позаду")
yaroslava_stetska.link_street(shevchenka, 'спереду')
shevchenka.link_street(yaroslava_stetska, "позаду")
shevchenka.link_street(ave, 'спереду')

misha = Enemy("Міша", "Алкоголік, що мріє вступити в УКУ")
misha.set_conversation("Я завжди мріяв вступити сюди, але таке місце займають такі як ти")
kozelnytska.set_character(misha)

tolik = Enemy("Толік", "Високий чоловік, одягнений в темне, \
сонцезахисні окуляри та підозріла усмішка на обличчі")
tolik.set_conversation("Віддавай гроші та всі коштовності поки не \
пізно і усміхайся інакше пошкодуєш")
ivana_franka.set_character(tolik)

jenya = DangerousEnemy("Женя", "Низький та товстий чоловік з великою собакою та шрамом на обличчі")
jenya.set_conversation("Я зроблю так, що ти пошкодуєш що народилась на цей світ")
yaroslava_stetska.set_character(jenya)

alina = Friend("Аліна", "Дівчинка десь 12 років, що грається з маленьким кошенням")
alina.set_conversation("Як би я хотіла забрати це кошення додому, шкода що мама не дозволить")
shevchenka.set_character(alina)

gryvnias = Item("Гроші")
gryvnias.set_description("100 гривень, що лежать на асфальті")
kozelnytska.set_item(gryvnias)

drink = Item("Напій")
drink.set_description("невідомий напій, що стоїть на лавці")
shevchenka.set_item(drink)

current_street = kozelnytska
backpack = []

dead = False
done = False

while not dead and not done:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()
  
    if current_street.end:
        done = True
        print('Ви прибули до місця призначення. Вітаю!')
        break

    command = input("> ")

    if command == "вперед":
        if inhabitant is None or isinstance(inhabitant, Friend):
            current_street = current_street.move('спереду')
        else:
            print('Ви неможете піти через небезпеку')
    elif command == "назад":
        current_street = current_street.move('позаду')
    elif command == "поговорити":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('Немає з ким говорити')
    elif command == 'дати гроші':
        if inhabitant is not None:
            if 'Гроші' in backpack:
                inhabitant.give_money()
                backpack.pop(backpack.index('Гроші'))
                if isinstance(inhabitant, Enemy) or isinstance(inhabitant, DangerousEnemy):
                    print('Злодій пішов')
                    current_street.character = None
            else:
                print('Ви не маєте грошей :(')
        else:
            print('Немає кому дати грошей')
    elif command == "обійняти":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print('Ця людина небезпечна, тому не варто обійматись')
        else:
            print('Немає кого обійняти.')
    elif command == 'втікти':
        if inhabitant is not None and isinstance(inhabitant, Enemy) \
            or isinstance(inhabitant, DangerousEnemy):
            inhabitant.run()
            current_street.character = None
            current_street = current_street.move('спереду')
        else:
            print('Немає причини біжати, бо немає небезпеки')
    elif command == 'закричати':
        if inhabitant is not None and isinstance(inhabitant, Enemy) \
            or isinstance(inhabitant, DangerousEnemy):
            inhabitant.shout()
            print('Злодій злякався та втік.')
            current_street.character = None
        else:
            print('Немає причини кричати, бо немає небезпеки')
    elif command == 'подзвонити в поліцію':
        if inhabitant is not None and isinstance(inhabitant, DangerousEnemy):
            inhabitant.call_police()
            print('Злодій злякався та втік.')
            current_street.character = None
        else:
            print('Поліція не зможе приїхати, бо не бачить небезпеки')
    elif command == "побитись":
        if inhabitant is not None and not isinstance(inhabitant, Friend):
            inhabitant.fight()
            print('Ви померли')
            dead = True
        else:
            print("Немає причини битись")
    elif command == "взяти":
        if item is not None:
            print("Ти взяв " + item.get_name() + " у свій рюкзак")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("Немає, що брати")
    else:
        print("Я не знаю як виконати команду " + command)
