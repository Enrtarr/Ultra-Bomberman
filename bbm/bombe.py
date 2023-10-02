import ursina as urs

if __name__ == '__main__':
    app = urs.Ursina()


class Bomb(urs.Entity):
    def __init__(self, murs_incassables, murs_cassables, bombes, **kwargs): 
        super().__init__()     

        # self.model="quad"
        # self.texture="./textures/vide"
        self.rotation_x = -90
        self.scale=1
        self.__tex_folder = './textures/explosion/'
        self.longueur = 3
        
        self.murs_incassables = murs_incassables
        self.murs_cassables = murs_cassables
        self.bombes = bombes

        self.__anims = urs.SpriteSheetAnimation(
            texture='./textures/bomb_flash.png',
            tileset_size=(6,1),
            fps=6,
            model='plane',
            animations={
                'flash': ((0,0), (5,0)),
            }
        )
        self.__anims.parent = self
        self.__anims.play_animation('flash')
        
        for key, value in kwargs.items(): 
            setattr(self, key, value)
    
    def explode(self):
        # les différentes durées entres les animations
        duration = .3
        wt1 = duration/3
        wt2 = 2 * duration/3
        wt3 = duration
        wt4 = duration + duration/3
        
        # créeation, animation et destruction du cube central
        m1 = urs.Entity(scale=self.scale,model='quad',position=self.position,collider='box') ; m1.texture = self.__tex_folder + 'm11'
        urs.invoke(setattr, m1, 'texture', self.__tex_folder+'m21', delay=wt1)
        urs.invoke(setattr, m1, 'texture', self.__tex_folder+'m31', delay=wt2)
        urs.invoke(setattr, m1, 'texture', self.__tex_folder+'m41', delay=wt3)
        urs.destroy(m1, delay=wt4)
        
        # on créer des parents pour chaque branche
        bombe_d = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        bombe_g = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        bombe_h = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        bombe_b = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        
        # on appelle la création des quatres branches
        # self.branche(bombe_d,'d',wt1,wt2,wt3,wt4)
        # self.branche(bombe_g,'g',wt1,wt2,wt3,wt4)
        # self.branche(bombe_h,'h',wt1,wt2,wt3,wt4)
        # self.branche(bombe_b,'b',wt1,wt2,wt3,wt4)
        for i in range(self.longueur):
            hit_UnWall = urs.raycast(bombe_d.position, (1,0), traverse_target=self.murs_incassables, distance=i+1, debug=False)
            hit_BrWall = urs.raycast(bombe_d.position, (1,0), traverse_target=self.murs_cassables, distance=i+1, debug=False)
            if hit_UnWall:
                break
            elif hit_BrWall:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_d) ; new_sprite.x += i+1
                new_sprite.texture = self.__tex_folder + 'd12'
                new_sprite.name = 'bout'
                urs.destroy(hit_BrWall.entity)
                break
            else:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_d) ; new_sprite.x += i+1 ; new_sprite.texture = self.__tex_folder + 'd11'
                if i+1 == self.longueur:
                    new_sprite.texture = self.__tex_folder + 'd12'
                    new_sprite.name = 'bout'
        for sprite in bombe_d.children:
            if sprite.name != 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d21', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d31', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d41', delay=wt3)
                urs.destroy(sprite, delay=wt4)
            elif sprite.name == 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d22', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d32', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'d42', delay=wt3)
                urs.destroy(sprite, delay=wt4)
        
        bombe_g = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        for i in range(self.longueur):
            hit_UnWall = urs.raycast(bombe_g.position, (-1,0), traverse_target=self.murs_incassables, distance=i+1, debug=False)
            hit_BrWall = urs.raycast(bombe_g.position, (-1,0), traverse_target=self.murs_cassables, distance=i+1, debug=False)
            if hit_UnWall:
                break
            elif hit_BrWall:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_g) ; new_sprite.x -= i+1
                new_sprite.texture = self.__tex_folder + 'g12'
                new_sprite.name = 'bout'
                urs.destroy(hit_BrWall.entity)
                break
            else:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_g) ; new_sprite.x -= i+1 ; new_sprite.texture = self.__tex_folder + 'g11'
                if i+1 == self.longueur:
                    new_sprite.texture = self.__tex_folder + 'g12'
                    new_sprite.name = 'bout'
        for sprite in bombe_g.children:
            if sprite.name != 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g21', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g31', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g41', delay=wt3)
                urs.destroy(sprite, delay=wt4)
            elif sprite.name == 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g22', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g32', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'g42', delay=wt3)
                urs.destroy(sprite, delay=wt4)
        
        bombe_h = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        for i in range(self.longueur):
            hit_UnWall = urs.raycast(bombe_h.position, (0,1), traverse_target=self.murs_incassables, distance=i+1, debug=False)
            hit_BrWall = urs.raycast(bombe_h.position, (0,1), traverse_target=self.murs_cassables, distance=i+1, debug=False)
            if hit_UnWall:
                break
            elif hit_BrWall:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_h) ; new_sprite.y += i+1
                new_sprite.texture = self.__tex_folder + 'h12'
                new_sprite.name = 'bout'
                urs.destroy(hit_BrWall.entity)
                break
            else:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_h) ; new_sprite.y += i+1 ; new_sprite.texture = self.__tex_folder + 'h11'
                if i+1 == self.longueur:
                    new_sprite.texture = self.__tex_folder + 'h12'
                    new_sprite.name = 'bout'
        for sprite in bombe_h.children:
            if sprite.name != 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h21', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h31', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h41', delay=wt3)
                urs.destroy(sprite, delay=wt4)
            elif sprite.name == 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h22', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h32', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'h42', delay=wt3)
                urs.destroy(sprite, delay=wt4)
        
        bombe_b = urs.Entity(model='quad', texture='./textures/vide',position=self.position)
        for i in range(self.longueur):
            hit_UnWall = urs.raycast(bombe_b.position, (0,-1), traverse_target=self.murs_incassables, distance=i+1, debug=False)
            hit_BrWall = urs.raycast(bombe_b.position, (0,-1), traverse_target=self.murs_cassables, distance=i+1, debug=False)
            if hit_UnWall:
                break
            elif hit_BrWall:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_b) ; new_sprite.y -= i+1
                new_sprite.texture = self.__tex_folder + 'b12'
                new_sprite.name = 'bout'
                urs.destroy(hit_BrWall.entity)
                break
            else:
                new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=bombe_b) ; new_sprite.y -= i+1 ; new_sprite.texture = self.__tex_folder + 'b11'
                if i+1 == self.longueur:
                    new_sprite.texture = self.__tex_folder + 'b12'
                    new_sprite.name = 'bout'
        for sprite in bombe_b.children:
            if sprite.name != 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b21', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b31', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b41', delay=wt3)
                urs.destroy(sprite, delay=wt4)
            elif sprite.name == 'bout':
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b22', delay=wt1)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b32', delay=wt2)
                urs.invoke(setattr, sprite, 'texture', self.__tex_folder+'b42', delay=wt3)
                urs.destroy(sprite, delay=wt4)
        
        # on change le parent pour le milieu et chaque branche
        m1.parent = self.bombes
        bombe_d.parent = self.bombes
        bombe_g.parent = self.bombes
        bombe_h.parent = self.bombes
        bombe_b.parent = self.bombes

        # on supprime les bombes (cause du bug, à modifier)
        for i in urs.scene.entities:
            if type(i) == urs.SpriteSheetAnimation:
                if 'flash' in i.animations:
                    i.disable()
    
    # fonction pour chaque branche de l'explosion
    # def branche(self,b_cote:urs.Entity,cote:str,wt1,wt2,wt3,wt4):
    #     for i in range(self.longueur):
    #         # raycast pour les deux types de mur
    #         hit_UnWall = urs.raycast(b_cote.position, (1,0), traverse_target=murs_incassables, distance=i+1, debug=False)
    #         hit_BrWall = urs.raycast(b_cote.position, (1,0), traverse_target=murs_cassables, distance=i+1, debug=False)
    #         # mur incassable : on stoppe le rayon
    #         if hit_UnWall:
    #             break
    #         # mur cassable : on le casse et on créer un bout, puis on stoppe le rayon
    #         elif hit_BrWall:
    #             new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=b_cote)
    #             if cote == 'd':
    #                 new_sprite.x += i+1
    #             elif cote == 'g':
    #                 new_sprite.x -= i+1
    #             elif cote == 'h':
    #                 new_sprite.y += i+1
    #             elif cote == 'b':
    #                 new_sprite.y -= i+1
    #             new_sprite.texture = self.__tex_folder+cote+'12'
    #             new_sprite.name = 'bout'
    #             print(cote)
    #             urs.destroy(hit_BrWall.entity)
    #             break
    #         # si aucun mur :
    #         else:
    #             # on créer un nouveau bout
    #             new_sprite = urs.Entity(scale=self.scale,model='quad',collider='box',parent=b_cote)
    #             if cote == 'd':
    #                 new_sprite.x += i+1
    #             elif cote == 'g':
    #                 new_sprite.x -= i+1
    #             elif cote == 'h':
    #                 new_sprite.y += i+1
    #             elif cote == 'b':
    #                 new_sprite.y -= i+1
    #             new_sprite.texture = self.__tex_folder+cote+'11'
    #             # si on est à la fin de la branche, on transforme le cube en bout
    #             if i+1 == self.longueur:
    #                 new_sprite.texture = self.__tex_folder+cote+'12'
    #                 new_sprite.name = 'bout'
    #     # mise à jour des textures au fil du temps :
    #     for sprite in b_cote.children:
    #         # si ce n'est pas un bout
    #         if sprite.name != 'bout':
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'21', delay=wt1)
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'31', delay=wt2)
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'41', delay=wt3)
    #             urs.destroy(sprite, delay=wt4)
    #         # si c'est un bout
    #         elif sprite.name == 'bout':
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'22', delay=wt1)
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'32', delay=wt2)
    #             urs.invoke(setattr, sprite, 'texture', self.__tex_folder+cote+'42', delay=wt3)
    #             urs.destroy(sprite, delay=wt4)

if __name__ == '__main__':
    app.run()