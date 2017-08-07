from abc import *

class Character(metaclass = ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.HP = hp
        self.power = power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.HP)

class Player(Character):
    def __init__(self, name = 'player', hp = 100, power = 10, *attack_kinds):
        super().__init__(name, hp, power)

        self.skills = []
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        '''
        만약 공격 종류가
        플레이어의 기술 중 하나라면
        데미지를 입지 않습니다. 
        '''
        if attack_kind in self.skills:
            return
        
        self.HP -= power
        
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind = 'None'

    def attack(self, other, attack_kind):
        if self.attack_kind == attack_kind:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        '''
        몬스터는 자신과 타입이 같은 공격을 당하면
        오히려 체력이 늘어납니다.
        조심해서 공격하세요.
        '''
        if self.attack_kind == attack_kind:
            self.HP += power
        else:
            self.HP -= power

class IceMonster(Monster):
    def __init__(self, name = 'Ice monster', hp = 50, power = 10):
        super().__init__(name, hp, power)
        self.attack_kind = 'ICE'

class FireMonster(Monster):
    def __init__(self, name = 'Fire monster', hp = 50, power = 20):
        super().__init__(name, hp, power)
        self.attack_kind = 'FIRE'

if __name__ == "__main__":
    player = Player('sword master',100, 30, 'ICE', 'FIRE')
    monsters = []
    monsters.append(IceMonster())
    monsters.append(FireMonster())
    
    for monster in monsters:
        print(monster)

    for monster in monsters:
        player.attack(monster, 'ICE')

    print('after the player attacked')

    for monster in monsters:
        print(monster)
    
            
        
