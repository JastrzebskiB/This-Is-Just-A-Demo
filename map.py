#import necessary for the constructor to work
from tile import*
from charsheet import*

#initialise map and hero object; cannot be in initials.py, since
#both files would have to import each other
#has to be initialised before class itself, otherwise it does not run
map1 = [["S","S","S","S","S","S","S","S","S","S","S","S","M","M","M"],\
 ["S","S","S","S","S","S","S","S","S","S","b","b","t28","M","M"],\
 ["S","S","t33","b","W","t36","t37","r","W","b","b","_","_","_","T"],\
 ["S","S","b","b","W","t51","t52","r","W","_","_","_","_","_","T"],\
 ["S","S","b","b","W","r","r","r","W","_","_","_","_","T","T"],\
 ["S","b","b","_","W","t81","r","t83","W","_","T","_","_","T","T"],\
 ["S","b","_","_","W","W","r","W","W","_","_","_","_","T","S"],\
 ["S","b","_","_","_","_","r","_","_","_","_","_","T","T","S"],\
 ["M","T","_","_","_","_","r","r","r","r","r","r","r","t134","S"],\
 ["M","T","T","_","T","_","r","_","_","_","_","_","T","T","S"],\
 ["M","M","T","_","_","_","r","_","_","_","_","_","_","T","T"],\
 ["M","M","T","T","_","_","r","_","_","_","_","_","_","T","T"],\
 ["M","M","T","T","_","_","r","r","r","r","_","_","_","_","T"],\
 ["M","M","T","T","T","_","r","T","T","r","_","_","_","_","T"],\
 ["M","M","T","T","T","_","r","T","T","r","_","T","_","_","T"],\
 ["M","M","T","t229","r","r","r","T","T","r","_","_","_","_","T"],\
 ["M","M","T","T","T","T","T","T","T","r","_","_","_","_","T"],\
 ["M","M","M","T","T","T","T","T","T","r","_","_","_","T","T"],\
 ["M","M","M","M","M","M","T","T","T","r","_","_","T","T","T"],\
 ["M","M","M","M","M","M","M","T","T","t295","T","T","T","T","T"]]
firstbattles = [False, False, False]

def firstmap_tiles(map):
    tilelist = []
    pos = [-40, -40]
    counter = 0
    for row in map:
        pos[0] += 40
        pos[1] = -40
        for tile in row:
            counter += 1
            name = "t" + str(counter)
            pos[1] += 40
            if tile == "S":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "sea.png")
                tilelist.append(name)
            elif tile == "T":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "tree.png")
                tilelist.append(name)
            elif tile == "W":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "wall.png")
                tilelist.append(name)
            elif tile == "M":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "mountain.png")
                tilelist.append(name)
            elif tile == "b":
                name = Tile(name, tile_width, tile_height, pos, False, \
                False, "beach.png")
                tilelist.append(name)
            elif tile == "_":
                name = Tile(name, tile_width, tile_height, pos, False, \
                False, "grass.png")
                tilelist.append(name)
            elif tile == "r":
                name = Tile(name, tile_width, tile_height, pos, False, \
                False, "road.png")
                tilelist.append(name)
            elif tile == "t28":
                name = T28(name, tile_width, tile_height, pos, False, \
                True, "beach.png")
                tilelist.append(name)
            elif tile == "t33":
                name = T33(name, tile_width, tile_height, pos, False, \
                True, "beach.png")
                tilelist.append(name)                
            elif tile == "t36":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "castle1.png")
                tilelist.append(name)
            elif tile == "t37":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "castle3.png")
                tilelist.append(name)
            elif tile == "t51":
                name = Tile(name, tile_width, tile_height, pos, True, \
                False, "castle2.png")
                tilelist.append(name)
            elif tile == "t52":
                name = T52(name, tile_width, tile_height, pos, False, \
                True, "castle4.png")
                tilelist.append(name)
            elif tile == "t81":
                name = T81(name, tile_width, tile_height, pos, False, \
                True, "master_at_arms.png")
                tilelist.append(name)
            elif tile == "t83":
                name = T83(name, tile_width, tile_height, pos, False, \
                True, "blacksmith.png")
                tilelist.append(name)
            elif tile == "t134":
                name = T134(name, tile_width, tile_height, pos, False, \
                True, "fishermen.png")
                tilelist.append(name)
            elif tile == "t229":
                name = T229(name, tile_width, tile_height, pos, False, \
                True, "lumbermill.png")
                tilelist.append(name)
            elif tile == "t295":
                name = T295(name, tile_width, tile_height, pos, False, \
                True, "road.png")
                tilelist.append(name)
            else:
                name = Tile(name, tile_width, tile_height, pos, False, \
                False, "empty.png")
                tilelist.append(name)
    return tilelist

class Map():

    """
    The map is to be 20 x 15 tiles; so it will be a 2d list having 20 rows, 15
    columns each as this is a demo, the maps are hardcoded into the main file;
    they can easily be made to load from a pickled file.
    """    


    #list of 20 lists, each one consisting of 15 elements (S=sea, b=beach, 
    #g=grass, W=wall, r=road, M=mountain, T=tree, Txx=building/action tile)
    #list of bools
    def __init__(self, map, battlelist, tilestrategy=firstmap_tiles):
        self.map = map
        self.tilelist = []
        self.blocklist = []
        self.actionlist = []
        self.battlelist = battlelist
        
        self.tilelist_constructor(tilestrategy)
        self.blocklist_constructor()
        self.actionlist_constructor()
        
    def tilelist_constructor(self, tilestrategy):
        self.tilelist = tilestrategy(self.map)    
        
    def blocklist_constructor(self):
        for tile in self.tilelist:
            if tile.get_block():
                self.blocklist.append(tile)
                
    def actionlist_constructor(self):
        for tile in self.tilelist:
            if tile.action:
                self.actionlist.append(tile)
            
    def fought_battle(self, which_battle):
        self.battlelist[which_battle] = True
        
    def get_battle(self, which_battle):
        return self.battlelist[which_battle]
        
    def show_map(self):
        for tile in self.tilelist:
            tile.show_tile()

    #currently not in use; included to be able to reuse and modify map objects
    def map_modify(self, map):  
        self.map = map
        self.tilelist_constructor()
        self.blocklist_constructor()
        self.actionlist_constructor()        
        
    def perform_actions(self, hero, locmap):
        for tile in self.actionlist:
            tile.act(hero, self)
    
    #main method    
    def play_map(self, hero):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit("Closed in play_map.")
                if event.type == KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not hero.checkleft(self.blocklist):
                            hero.ifleft(True)
                    if event.key == pygame.K_RIGHT:
                        if not hero.checkright(self.blocklist):
                            hero.ifright(True)
                    if event.key == pygame.K_UP:
                        if not hero.checkup(self.blocklist):
                            hero.ifup(True)
                    if event.key == pygame.K_DOWN:
                        if not hero.checkdown(self.blocklist):
                            hero.ifdown(True)
                if event.type == KEYUP:
                    if event.key == pygame.K_LEFT:
                        hero.ifleft(False)
                    if event.key == pygame.K_RIGHT:
                        hero.ifright(False)
                    if event.key == pygame.K_UP:
                        hero.ifup(False)
                    if event.key == pygame.K_DOWN:
                        hero.ifdown(False)
                if event.type == MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    if (mousepos[0] > hero.rect.left and\
                            mousepos[0] < hero.rect.right and\
                            mousepos[1] > hero.rect.top and\
                            mousepos[1] < hero.rect.bottom):
                        hero.reset_movement()
                        charsheet(army)

            screen.fill(BLACK)

            #ordered like that so that hero shows on the map and textbox
            #displays over hero
            self.show_map()
            hero.move(self.blocklist)
            hero.show_tile()
            self.perform_actions(hero, self.map)

            #short wait time due to tremendous performance loss after 
            #changing tile graphics from solid colour
            pygame.time.wait(10)
            pygame.display.update()

firstmap = Map(map1, firstbattles)
hero = Hero(10, 10, [160, 200], False, "hero_l.png", "hero_r.png")