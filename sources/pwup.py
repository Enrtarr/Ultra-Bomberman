import ursina as urs

if __name__ == '__main__':
    app = urs.Ursina()

lst_pwup_tex = {
    'fire':'./textures/pwup_fire',
    'roller':'./textures/pwup_roller',
    'bomb_up':'./textures/pwup_bombup'
    }

class PowerUp(urs.Entity):
    def __init__(self, type, power_ups:urs.Entity, **kwargs): 
        super().__init__()
        """Initialisation du power-up et de ses attributs
            - rotation_x : permet de faire en sorte que la bombe fasse face à la caméra
            - scale : la déformation du power-up
            - type : le type de power-up (ex: fire, roller, etc...)
            - __anims : les animations du power-up
            """

        self.rotation_x = -90
        # self.model = 'plane'
        self.parent = power_ups
        self.scale = .8
        self.type = type
        self.collider = 'box'
        self.collected = False
        # self.texture = lst_pwup_tex[self.type]
        
        # print(self)
        
        # self.murs_incassables = murs_incassables
        # self.murs_cassables = murs_cassables
        # self.bombes = bombes

        self.__anims = urs.SpriteSheetAnimation(
            texture=f'./textures/pwup_sheet.png',
            tileset_size=(10,5),
            fps=12,
            model='plane',
            animations={
                'fire':((6,4),(8,4)),
                'roller':((6,3),(8,3)),
                'bombup':((6,2),(8,2)),
            }
        )
        self.__anims.parent = self
        self.__anims.play_animation(self.type)
        
        for key, value in kwargs.items(): 
            setattr(self, key, value)
    
    def recuperer(self):
        self.rotation_x = 90
        self.z = -5
        # print(self.__anims.animations)
        # for i in self.__anims.animations:
        #     self.__anims.animations[i].finish()
        #     self.__anims.animations[i].kill()
        #     print(self.__anims.animations[i])
        # urs.destroy(self)
    
    def stat_change(self):
        stats = {
            'fire':'bomb_size',
            'roller':'speed',
            'bombup': 'max_bomb',
        }
        return stats[self.type]

class PwupSpawner(urs.Entity):
    def __init__(self, **kwargs): 
        super().__init__()

        self.model='quad'
        self.texture='./textures/vide'
        
        self.t = 0
        
        for key, value in kwargs.items(): 
            setattr(self, key, value)
    
    def apparaitre(self):
        self.t += 1
        print(self.t)
        new_pwup = PowerUp(type='fire',power_ups=self)
    
    def input(self,key):
        if key=='b':
            self.demarrer()
        elif key=='n':
            self.arreter()
    
    def demarrer(self):
        self.sequence = urs.Sequence(
            urs.Func(self.apparaitre),
            urs.Wait(.1),
            loop=True
            )
        self.sequence.start()
    
    def arreter(self):
        self.sequence.kill()
    
    # def update(self):
    #     self.t += urs.time.dt
    #     if self.t > .5:  # do every half second
    #         self.t = 0
    #         print('sus')


if __name__ == '__main__':
    app.run()