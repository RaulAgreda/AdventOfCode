

"""
d/a a a a/b
d         b
d         b
d/c c c c/b
"""

def part1():

    allTiles = open("20_Input.txt").read().split("\n\n")

    # print(allTiles)

    def getTiles(tilesList):
        tiles = {}

        for tile in tilesList:
            id = int(tile[5:tile.index(":")])
            splitTile = tile.split("\n")
            tiles[id] = {"a":"","b":"","c":"","d":""}
            tiles[id]["a"] = splitTile[1]
            tiles[id]["c"] = splitTile[-1]
            for i in range(1,len(splitTile)):
                tiles[id]["b"] += splitTile[i][-1]
                tiles[id]["d"] += splitTile[i][0]

        return tiles

    def doesMatch(tiles:dict,id1,id2):

        for key1 in tiles[id1].keys():
            for key2 in tiles[id2].keys():
                if tiles[id1][key1] == tiles[id2][key2]:
                    return True
        return False

    def nOfMatch(tiles:dict,id):
        total = 0

        for id2 in tiles.keys():
            if id2 != id:
                if doesMatch(tiles,id,id2):
                    total+=1
        
        return total

    tiles = getTiles(allTiles)

    total = 1

    for id in tiles.keys():

        if nOfMatch(tiles,id) == 2:
            total*=id
            print(id)
    
    return total

    

    # asociations = ("bd","ac")


    




print(part1())


