import pygame, pickle, os, random, copy

#Класс описывающий локацию
class Location:
    def __init__(self):
        self.id = 0 #Id локации
        self.name = '' #Название локации
        self.matrix = list() #Матрица локации
        self.previousPos = (0, 0)
        pass
    def loadArena(self, previousPos):
        self.previousPos = previousPos
        self.name = 'Arena'
        mappings = open('Assets/DataBase/Arena.txt'.format(self.id), 'r').read().split('\n')
        self.matrix.clear()
        for line in mappings:
            self.matrix.append(line.split(' '))
            pass
        return (2, 5)
    def unloadArena(self):
        self.setLocation(self.id)
        return self.previousPos
    def setLocation(self, id):
        spawnPos = (0, 0)
        if (id == 0): #Main Village
            if (self.id == 1):
                spawnPos = (5, 0)
            elif (self.id == 3):
                spawnPos = (20, 7)
            else:
                spawnPos = (8, 6)
            self.id = 0
            self.name = 'Main Village'

        elif (id == 1): #Path to the Light Soul 1
            if (self.id == 0): 
                spawnPos = (5, 10)
            elif (self.id == 2):
                spawnPos = (14, 0)
            self.id = 1
            self.name = 'Path to the Light Soul 1'

        elif (id == 2): #Path to the Light Soul 2
            if (self.id == 1):
                spawnPos = (14, 10)
            elif (self.id == 5):
                spawnPos = (20, 6)
            self.id = 2
            self.name = 'Path to the Light Soul 2'

        elif (id == 3): #Path to the Dark Soul 1
            if (self.id == 0):
                spawnPos = (0, 7)
            elif (self.id == 8):
                spawnPos = (20, 9)
            self.id = 3
            self.name = 'Path to the Dark Soul 1'

        elif (id == 4): #Gray Soul
            if (self.id == 5):
                spawnPos = (10, 0)
            elif (self.id == 6):
                spawnPos = (19, 1)
            elif (self.id == 7):
                spawnPos = (20, 6)
            self.id = 4
            self.name = 'Gray Soul'

        elif (id == 5): #Light Soul
            if (self.id == 2):
                spawnPos = (0, 6)
            elif (self.id == 4):
                spawnPos = (10, 10)
            self.id = 5
            self.name = 'Light Soul'

        elif (id == 6): #Soul King
            spawnPos = (1, 9)
            self.id = 6
            self.name = 'Soul King'

        elif (id == 7): #Dark Soul
            if (self.id == 4):
                spawnPos = (0, 6)
            elif (self.id == 8):
                spawnPos = (5, 10)
            self.id = 7
            self.name = 'Dark Soul'
        
        elif (id == 8): #Path to the Dark Soul 2
            if (self.id == 3):
                spawnPos = (0, 9)
            elif (self.id == 7):
                spawnPos = (5, 0)
            self.id = 8
            self.name = 'Path to the Dark Soul 2'
        mappings = open('Assets/DataBase/Location{0}.txt'.format(self.id), 'r').read().split('\n')
        self.matrix.clear()
        for line in mappings:
            self.matrix.append(line.split(' '))
            pass
        return spawnPos
    pass

#Объект для наследования
class Object:
    def __init__(self):
        self.name = ''
        self.speed = 1
        self.position = (0, 0)
        self.health = 100
        self.maxHealth = self.health
        self.armor = 1
        self.damage = 1
        self.isalive = True
        pass
    pass

#Класс описывающй героя
class Hero(Object):
    def __init__(self, name):
        self.name = name
        self.locations = list()
        
        
        self.weapon = 1
        self.xpweapon = 25

        self.armor = 1
        self.xparmor = 25
        
        self.speed = 2
        self.xpspeed = 500

        self.health = 100
        self.xphealth = 50

        self.damage = 8
        self.soul = 0
        self.maxHealth = self.health
        self.coolDown = 0
        self.currentXP = 0
        pass
    pass

#LightSoul
class LightSoul(Object):
    def __init__(self):
        self.name = 'Light Soul'
        self.speed = 2
        self.position = (10, 9)
        self.armor = 25
        self.damage = 35
        self.health = 850
        self.maxHealth = self.health
        self.isalive = True
    pass

#DarkSoul
class DarkSoul(Object):
    def __init__(self):
        self.name = 'Dark Soul'
        self.speed = 2
        self.position = (1, 6)
        self.armor = 20
        self.damage = 62
        self.health = 600
        self.maxHealth = self.health
        self.isalive = True
    pass

#GraySoul
class GraySoul(Object):
    def __init__(self):
        self.name = 'Gray Soul'
        self.speed = 3
        self.position = (19, 1)
        self.damage = 100
        self.armor = 30
        self.health = 1500
        self.maxHealth = self.health
        self.isalive = True
    pass

#Soul King
class SoulKing(Object):
    def __init__(self):
        self.name = '2.0'
        self.speed = 4
        self.armor = 50
        self.damage = 200
        self.health = 3500
        self.position = (9, 5)
        self.maxHealth = self.health
        self.isalive = True
    pass

#Models
class Models:
    def __init__(self):
        self.heroModel = None
        self.locationModel = None
        self.soulModel = pygame.image.load('Assets/Sprites/Soul King.png')
        self.grayModel = pygame.image.load('Assets/Sprites/Gray Soul.png')
        self.darkModel = pygame.image.load('Assets/Sprites/Dark Soul.png')
        self.lightModel = pygame.image.load('Assets/Sprites/Light Soul.png')
        self.enemyModel = None
        pass
    def SetEnemyModel(self, id):
        if (id == 1 or id == 2):
            self.enemyModel = pygame.image.load('Assets/Sprites/Enemy.png')
        elif (id == 4):
            self.enemyModel = self.lightModel
        elif (id == 5):
            self.enemyModel = self.darkModel
        elif (id == 6):
            self.enemyModel = self.grayModel
        elif (id == 7):
            self.enemyModel = self.soulModel
        pass
    def SetHeroModel(self, id):
        if (id < 4):
            self.heroModel = pygame.image.load('Assets/Sprites/Hero{0}.png'.format(id))
        pass
    def SetLocationModel(self, id):
        if (id != -1):
            self.locationModel = pygame.image.load('Assets/Sprites/Location{0}.png'.format(id))
        else:
            self.locationModel = pygame.image.load('Assets/Sprites/Arena.png'.format(id))
        pass
    pass

#Данные для сохранения
class SavingData:
    def __init__(self):
        self.currentHero = None #Текущий герой
        self.currentLocation = None #Текущая локация
        self.lightsoul = None #Белая душа
        self.darksoul = None #Черная душа
        self.graysoul = None #Серая душа
        self.soulking = None #Король душ

        self.moves = 0 #Сколько шагов
        pass
    pass

#Класс работы с игрой
class GameControl:
    def __init__(self):
        pygame.init()
        self.running = True #Игра идет
        self.screen = None #Экран
        self.screenSize = (1344, 704 + 150) #Размер экрана
        self.FPS = 30 #Кол-во кадров в секунду
        self.objects = list() #Лист объектов

        self.currentHero = None #Текущий герой
        self.currentLocation = None #Текущая локация
        self.currentEnemy = Object() #Текущий противник
        self.data = SavingData() #То, что сохранять
        self.lightsoul = LightSoul() #Белая душа
        self.darksoul = DarkSoul() #Черная душа
        self.graysoul = GraySoul() #Серая душа
        self.soulking = SoulKing() #Король душ
        self.models = Models() #Модельки

        self.keypressed = 0 #Кол-во нажатий
        self.moves = 0 #Сколько шагов
        self.win = False #Победа
        self.openWorld = True #Бегает по открытому миру
        self.event = 'Ничего'
        self.hmove = 0
        self.emove = 0
        self.status = [0, 0]
        self.statusTime = 0
        self.hdmg = 0
        self.edmg = 0
        pass

    #Загрузить игру
    def loadGame(self):
        with open('Assets/DataBase/Database.txt', 'rb') as file:
            if (os.stat(file.fileno()).st_size != 0):
                self.data = pickle.load(file)
                self.currentHero = self.data.currentHero
                self.currentLocation = self.data.currentLocation
                self.darksoul = self.data.darksoul
                self.lightsoul = self.data.lightsoul
                self.graysoul = self.data.graysoul
                self.soulking = self.data.soulking
                self.moves = self.data.moves

                self.models.SetHeroModel(self.currentHero.soul)
                self.models.SetLocationModel(self.currentLocation.id)
                self.startGame()
        pass

    #Сохранить игру
    def saveGame(self):
        self.data.currentHero = self.currentHero
        self.data.currentLocation = self.currentLocation
        self.data.darksoul = self.darksoul
        self.data.lightsoul = self.lightsoul
        self.data.graysoul = self.graysoul
        self.data.soulking = self.soulking
        self.data.moves = self.moves
        pickle.dump(self.data, open('Assets/DataBase/Database.txt', 'wb'))
        self.event = 'Сохранение'
        pass

    #Установить режим игры
    def setGameMode(self, mode):
        if (mode == 0): #Новая игра
            self.currentHero = Hero(input('Введите имя героя: '))
            self.currentLocation = Location()
            self.currentHero.position = self.currentLocation.setLocation(6)
            self.currentHero.locations.extend(['0', '1', '2', '3', '5', '7', '8'])
            self.models.SetHeroModel(self.currentHero.soul)
            self.models.SetLocationModel(self.currentLocation.id)

            self.saveGame()
            self.startGame()
            pass
        elif (mode == 1): #Продолжить
            self.loadGame()
        self.event = 'Ничего'
        pass

    #Тернарный оператор
    def ternar(self, condition, true, false):
        if (condition): return true
        return false

    #В радиусе
    def inRadius(self, pos1, pos2):
        m = copy.deepcopy(self.currentLocation.matrix)
        m[pos2[1]][pos2[0]] = 'A'
        j, i = pos1
        return (m[i - 1][j - 1] == 'A') or (m[i - 1][j] == 'A') or (m[i - 1][j + 1] == 'A') or (m[i][j - 1] == 'A') or (m[i][j + 1] == 'A') or (m[i + 1][j - 1] == 'A') or (m[i + 1][j] == 'A') or (m[i + 1][j + 1] == 'A')

    #Вернуть объект текста для вывода на экран
    def returnText(self, text, size, color):
        font = pygame.font.SysFont('Verdana', size)
        return font.render(text, False, color)

    #Перемещение игрока
    def PlayerMove(self, newCoords):
        try:
            if (self.currentHero.position != newCoords):
                willFight = random.choice([True, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
                temp = self.currentLocation.matrix[newCoords[1]][newCoords[0]]
                if (willFight):
                    self.openWorld = False
                    self.currentHero.position = self.currentLocation.loadArena(self.currentHero.position)
                    self.models.SetLocationModel(-1)
                    self.setEnemy(1)
                    self.event = 'Бой!'
                    pass
                else:
                    if (temp[0] == '1' or (temp[0] == '4' and not self.lightsoul.isalive) or (temp[0] == '5' and not self.darksoul.isalive) or (temp[0] == '6' and not self.graysoul.isalive) or (temp[0] == '7' and not self.soulking.isalive)): #Перемещение
                        self.event = 'Перемещение: {0} --> {1}'.format(self.currentHero.position, newCoords)
                        self.currentHero.position = newCoords
                    elif (temp[0] == '3' and temp[1:] in self.currentHero.locations): #Переход на следующую локацию
                        self.currentHero.position = self.currentLocation.setLocation(int(temp[1:]))
                        self.models.SetLocationModel(self.currentLocation.id)
                        self.event = 'Переход на другую локацию'
                    elif (temp[0] == '8'): #Princess, WIN!
                        self.win = True
                        self.event = 'Победа!'
                    elif (temp[0] in '4567'):
                        self.openWorld = False
                        self.currentHero.position = self.currentLocation.loadArena(self.currentHero.position)
                        self.models.SetLocationModel(-1)
                        self.setEnemy(int(temp[0]))
                        self.event = 'Бой!'
                        pass
                    self.moves += 1
                    self.updateStatuses()
                    pass
                pass #if (self.currentHero.position != newCoords):
            pass
        except Exception as ex: 
            print(ex)
            pass
        pass

    #Установить врага
    def setEnemy(self, id):
        if (id == 1 or id == 2): #Random Enemy
            self.currentEnemy = Object()
            self.currentEnemy.name = 'Enemy'
            self.currentEnemy.health = random.randrange(self.currentHero.health // 2, self.currentHero.health, 10)
            self.currentEnemy.maxHealth = self.currentEnemy.health
            self.currentEnemy.armor = random.randint(self.currentHero.armor // 2, self.currentHero.armor)
            self.currentEnemy.speed = random.randint(self.currentHero.speed // 2, self.currentHero.speed)
            dmg = self.currentHero.damage * self.currentHero.weapon + 1
            self.currentEnemy.damage = random.randint(dmg // 1.5, dmg)
        elif (id == 4): #Light Soul boss
            self.currentEnemy = self.lightsoul
        elif (id == 5): #Dark Soul boss
            self.currentEnemy = self.darksoul
        elif (id == 6): #Gray Soul boss
            self.currentEnemy = self.graysoul
        elif (id == 7): #Soul King boss
            self.currentEnemy = self.soulking

        self.models.SetEnemyModel(id)
        self.currentEnemy.position = (18, 5)
        pass

    #Обновить статусы
    def updateStatuses(self):
        if (self.currentHero.coolDown != 0):
            self.currentHero.coolDown -= 1
        if (self.statusTime != 0):
            self.statusTime -= 1
        else:
            self.status = [0, 0]
        pass

    #Действия игрока
    def playerActions(self):
        keys = pygame.key.get_pressed()
        temp = list(filter(lambda x: x == 1, keys))
        if (len(temp) == 0):
            self.keypressed = 0
        else:
            self.keypressed += len(temp)
        if (self.keypressed == 0):
            return False
        elif (self.keypressed == 1):
            rad = self.inRadius(self.currentHero.position, self.currentEnemy.position)
            if (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_w] or keys[pygame.K_s]): #Перемещение
                newCoords = self.currentHero.position
                newCoords = (self.ternar(keys[pygame.K_a], newCoords[0] - 1, newCoords[0]), newCoords[1])
                newCoords = (self.ternar(keys[pygame.K_d], newCoords[0] + 1, newCoords[0]), newCoords[1])
                newCoords = (newCoords[0], self.ternar(keys[pygame.K_w], newCoords[1] - 1, newCoords[1]))
                newCoords = (newCoords[0], self.ternar(keys[pygame.K_s], newCoords[1] + 1, newCoords[1]))
                if (self.currentLocation.matrix[newCoords[1]][newCoords[0]] == '1' and newCoords != self.currentEnemy.position):
                    self.currentHero.position = newCoords
                    self.hmove += 1
                    self.event = 'Перемещение!'
                    return True
                pass
            elif (keys[pygame.K_1] and self.currentHero.coolDown == 0): #Ярость
                self.hmove = self.currentHero.speed
                self.currentHero.coolDown = 6
                self.status[0] += int(self.currentHero.damage * 0.20)
                self.status[1] += int(self.currentHero.armor * 0.20)
                self.statusTime = 10
                self.event = 'Ярость!'
                pass
            elif (keys[pygame.K_2] and self.currentHero.coolDown == 0): #Баф хп
                self.hmove = self.currentHero.speed
                self.currentHero.coolDown = 6
                self.currentHero.health += int(self.currentHero.maxHealth * 0.20)
                self.event = 'Баф здоровья!'
                return True
            elif (keys[pygame.K_3] and self.currentHero.coolDown == 0 and rad): #Крит атака
                self.hmove = self.currentHero.speed
                self.currentHero.coolDown = 4
                self.status[0] -= int(self.currentHero.damage * 0.20)
                self.statusTime = 3
                dmg = ((self.currentHero.damage + self.status[0]) * self.currentHero.weapon) + 1
                dmg = dmg - ((dmg * self.currentEnemy.armor) // 100)
                dmg = random.randint(dmg // 1.5, dmg)
                dmg *= 3
                self.hdmg = dmg
                self.currentEnemy.health -= dmg
                self.event = 'Крит!'
                return True
            elif (keys[pygame.K_4] and rad): #Атака
                self.hmove += 2
                dmg = ((self.currentHero.damage + self.status[0]) * self.currentHero.weapon) + 1
                dmg = dmg - ((dmg * self.currentEnemy.armor) // 100)
                dmg = random.randint(dmg // 1.5, dmg)
                self.hdmg = dmg
                self.currentEnemy.health -= dmg
                self.event = 'Атака!'
                return True
            pass #Elif keypressed == 1
        return False

    #Действия AI
    def aiActions(self):
        if (self.inRadius(self.currentEnemy.position, self.currentHero.position)): #Атака
            self.emove += 2
            dmg = self.currentEnemy.damage
            dmg = dmg - ((dmg * (self.currentHero.armor + self.status[1])) // 100)
            dmg = random.randint(dmg // 1.5, dmg)
            self.edmg = dmg
            self.currentHero.health -= dmg
            return True
        else:
            p = self.currentEnemy.position
            p1 = self.currentHero.position
            if (p[1] > p1[1]):
                self.currentEnemy.position = (p[0], p[1] - 1)
            elif (p[1] < p1[1]):
                self.currentEnemy.position = (p[0], p[1] + 1)
            elif (p[0] > p1[0]):
                self.currentEnemy.position = (p[0] - 1, p[1])
            elif (p[0] < p1[0]):
                self.currentEnemy.position = (p[0] + 1, p[1])
            self.emove += 1
            return True
        return False

    #Какие-либо действия в игре
    def actions(self):
        keys = pygame.key.get_pressed()

        if (self.openWorld):
            if (keys[pygame.K_LCTRL] and keys[pygame.K_s]):
                self.saveGame();
            else:
                temp = list(filter(lambda x: x == 1, keys))
                if (len(temp) == 0):
                    self.keypressed = 0
                else:
                    self.keypressed += len(temp)

                if (self.keypressed == 1 and (keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d])):
                    newCoords = self.currentHero.position
                    newCoords = (self.ternar(keys[pygame.K_a], newCoords[0] - 1, newCoords[0]), newCoords[1])
                    newCoords = (self.ternar(keys[pygame.K_d], newCoords[0] + 1, newCoords[0]), newCoords[1])
                    newCoords = (newCoords[0], self.ternar(keys[pygame.K_w], newCoords[1] - 1, newCoords[1]))
                    newCoords = (newCoords[0], self.ternar(keys[pygame.K_s], newCoords[1] + 1, newCoords[1]))
                    self.PlayerMove(newCoords)
                    pass
                elif (keys[pygame.K_1]):
                    pygame.display.iconify()
                    os.system('cls')
                    print('Улучшения:\n1)Здоровье: {0} --> {1}, нужно {2}xp'.format(self.currentHero.maxHealth, self.currentHero.maxHealth + 50, self.currentHero.xphealth))
                    print('2)Броня: {0} --> {1}, нужно {2}xp'.format(self.currentHero.armor, self.currentHero.armor + 1, self.currentHero.xparmor))
                    print('3)Оружие: {0} --> {1}, нужно {2}xp'.format(self.currentHero.weapon, self.currentHero.weapon + 1, self.currentHero.xpweapon))
                    print('4)Скорость: {0} --> {1}, нужно {2}xp'.format(self.currentHero.speed, self.currentHero.speed + 1, self.currentHero.xpspeed))
                    res = input('У вас {0}xp: '.format(self.currentHero.currentXP))
                    if (res == '1'):
                        if (self.currentHero.currentXP >= self.currentHero.xphealth):
                            self.currentHero.maxHealth += 50
                            self.currentHero.health = self.currentHero.maxHealth
                            self.currentHero.currentXP -= self.currentHero.xphealth
                            self.currentHero.xphealth *= 2
                            print('Успешно')
                        else:
                            print('Недостаточно опыта')
                        pass
                    elif (res == '2'):
                        if (self.currentHero.currentXP >= self.currentHero.xparmor):
                            self.currentHero.armor += 1
                            self.currentHero.currentXP -= self.currentHero.xparmor
                            self.currentHero.xparmor *= 2
                            print('Успешно')
                        else:
                            print('Недостаточно опыта')
                        pass
                    elif (res == '3'):
                        if (self.currentHero.currentXP >= self.currentHero.xpweapon):
                            self.currentHero.weapon += 1
                            self.currentHero.currentXP -= self.currentHero.xpweapon
                            self.currentHero.xpweapon *= 2
                            print('Успешно')
                        else:
                            print('Недостаточно опыта')
                        pass
                    elif (res == '4'):
                        if (self.currentHero.currentXP >= self.currentHero.xpspeed):
                            self.currentHero.speed += 1
                            self.currentHero.currentXP -= self.currentHero.xpspeed
                            self.currentHero.xpspeed *= 2
                            print('Успешно')
                        else:
                            print('Недостаточно опыта')
                        pass
                    pass
                pass
            
            pass # if (self.openWorld)
        else: #Fighting
            if (self.currentEnemy.health <= 0 or keys[pygame.K_0]):
                self.openWorld = True
                self.currentHero.position = self.currentLocation.unloadArena()
                self.models.SetLocationModel(self.currentLocation.id)
                self.currentHero.health = self.currentHero.maxHealth
                #Получение опыта
                XP = self.currentEnemy.speed * 10 + self.currentEnemy.armor + self.currentEnemy.damage + self.currentEnemy.maxHealth // 100
                self.event = 'Победа!'
                self.edmg = 0
                self.hdmg = 0
                if (self.currentEnemy.name == 'Light Soul'):
                    self.lightsoul.isalive = False
                    self.currentHero.soul += 1
                    XP *= 2.5
                    if (not self.lightsoul.isalive and not self.darksoul.isalive):
                        self.currentHero.locations.append('4')
                    pass
                elif (self.currentEnemy.name == 'Dark Soul'):
                    self.darksoul.isalive = False
                    self.currentHero.soul += 1
                    XP *= 2.5
                    if (not self.lightsoul.isalive and not self.darksoul.isalive):
                        self.currentHero.locations.append('4')
                    pass
                elif (self.currentEnemy.name == 'Gray Soul'):
                    self.graysoul.isalive = False
                    self.currentHero.soul += 1
                    self.currentHero.locations.append('6')
                    XP *= 3
                    pass
                elif (self.currentEnemy.name == '2.0'):
                    self.soulking.isalive = False
                    self.currentHero.soul += 1
                    XP *= 3.5
                    pass
                self.currentHero.currentXP += int(XP)
                self.models.SetHeroModel(self.currentHero.soul)
                pass
            if (self.currentHero.speed > self.hmove): #Действия игрока
                if(self.playerActions() == True): pygame.time.delay(150)
            elif (self.currentEnemy.speed > self.emove): #Действия AI
                if (self.aiActions() == True): pygame.time.delay(150)
            else:
                self.event += ' | --> {0}, <-- {1} | Ход завершен'.format(self.hdmg, self.edmg)
                self.emove = 0
                self.hmove = 0
                self.moves += 1
                self.updateStatuses()
            pass
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (keys[pygame.K_LALT] and keys[pygame.K_F4])): 
                self.running = False
                self.saveGame()
            pass
        pass

    #Обновить фрейм
    def drawFrame(self):
        self.screen.fill((0, 0, 0))

        for obj in self.objects:
            self.screen.blit(obj[0], obj[1])
            pass
        self.objects.clear()

        pygame.display.update()
        pass

    #Начать игру
    def startGame(self):
        pygame.display.set_caption('Save Your Princess')
        self.screen = pygame.display.set_mode(self.screenSize)

        while self.running:
            pygame.time.Clock().tick(self.FPS)
            self.actions()

            if (self.win):
                self.running = False
                print('You Win\nTHE END')
                with open('Assets/DataBase/Database.txt', 'w') as file:
                    file.write('')
                pass

            self.objects.append((pygame.image.load('Assets/Sprites/UI.png'), (0, 704)))
            self.objects.append((self.returnText('Герой: {0} | Ход: {1}'.format(self.currentHero.name, self.moves), 20, (0, 200, 0)), (22, 714)))
            self.objects.append((self.returnText('Здоровье: {0}/{1} | КД: {2}'.format(self.currentHero.health, self.currentHero.maxHealth, self.currentHero.coolDown), 20, (0, 200, 0)), (22, 736)))
            self.objects.append((self.returnText('Урон: {0} | Защита: {1}'.format(self.currentHero.damage * self.currentHero.weapon, self.currentHero.armor), 20, (0, 200, 0)), (22, 758)))
            self.objects.append((self.returnText('Опыт: {0} | Локация: {1}'.format(self.currentHero.currentXP, self.currentLocation.name), 20, (0, 200, 0)), (22, 802)))

            self.objects.append((self.returnText('Событие: {0}'.format(self.event), 20, (0, 200, 0)), (640, 714)))

            if (self.currentHero.health > 0):
                if (self.openWorld): #Open World
                    self.objects.append((self.returnText('1 - Улучшения', 20, (0, 200, 0)), (340, 714)))
                    self.objects.append((self.models.locationModel, (0, 0))) #Location
                    bpos = (0, 0)
                    if (self.currentLocation.id == 5 and self.lightsoul.isalive):
                        bpos = self.lightsoul.position[0] * 64, self.lightsoul.position[1] * 64
                        self.objects.append((self.models.lightModel, bpos)) #Light Boss
                    elif (self.currentLocation.id == 4 and self.graysoul.isalive):
                        bpos = self.graysoul.position[0] * 64, self.graysoul.position[1] * 64
                        self.objects.append((self.models.grayModel, bpos)) #Gray Boss
                    elif (self.currentLocation.id == 7 and self.darksoul.isalive):
                        bpos = self.darksoul.position[0] * 64, self.darksoul.position[1] * 64
                        self.objects.append((self.models.darkModel, bpos)) #Dark Boss
                    elif (self.currentLocation.id == 6 and self.soulking.isalive):
                        bpos = self.soulking.position[0] * 64, self.soulking.position[1] * 64
                        self.objects.append((self.models.soulModel, bpos)) #King Boss
                        self.objects.append((pygame.image.load('Assets/Sprites/Princess.png'), (15 * 64, 5 * 64)))
                    elif (self.currentLocation.id == 6 and not self.soulking.isalive):
                        self.objects.append((pygame.image.load('Assets/Sprites/Princess.png'), (15 * 64, 5 * 64)))

                    hpos = self.currentHero.position[0] * 64, self.currentHero.position[1] * 64
                    self.objects.append((self.models.heroModel, hpos)) #Hero
                    pass
                else: #Fighting
                    self.objects.append((self.returnText('1 - Ярость', 20, (0, 200, 0)), (340, 714)))
                    self.objects.append((self.returnText('2 - Божественная ладонь', 20, (0, 200, 0)), (340, 714 + 22)))
                    self.objects.append((self.returnText('3 - Критический удар', 20, (0, 200, 0)), (340, 714 + 22 + 22)))
                    self.objects.append((self.returnText('4 - Обычная атака', 20, (0, 200, 0)), (340, 714 + 22 + 22 + 22)))
                    self.objects.append((self.models.locationModel, (0, 0))) #Location

                    self.objects.append((self.returnText('Враг: {0} | {1}/{2} HP'.format(self.currentEnemy.name, self.currentEnemy.health, self.currentEnemy.maxHealth), 20, (0, 200, 0)), (640, 714 + 45)))
                    self.objects.append((self.returnText('Статусы: {0} к урону, {1} к броне на {2} ходов'.format(self.status[0], self.status[1], self.statusTime), 20, (0, 200, 0)), (640, 714 + 45 + 22)))

                    epos = self.currentEnemy.position[0] * 64, self.currentEnemy.position[1] * 64
                    self.objects.append((self.models.enemyModel, epos)) #Enemy

                    hpos = self.currentHero.position[0] * 64, self.currentHero.position[1] * 64
                    self.objects.append((self.models.heroModel, hpos)) #Hero
                    pass
                pass #Hero is alive
            else:
                print('You died...')
                self.running = False;
                with open('Assets/DataBase/Database.txt', 'w') as file:
                    file.write('')
                pass
            self.drawFrame()
            pass
        pygame.quit()
        pass
    pass
