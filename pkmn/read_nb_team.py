with open(r"team1.pnb", "rb") as f:
    team = f.read()

versionstr = team[1:7]
curbyte = 7

print(versionstr)


def chr2bin(string):
    res = ''
    for c in string:
        res += bin(c)[2:].zfill(8)
    return res



def read_mon_str(mon_str):
    curbyte = 0
    nickname = mon_str[curbyte:curbyte+15]
    curbyte += 15

    print("Nickname: %s" % nickname)

    b_mon_str = chr2bin(mon_str[curbyte:])
    curbyte = 0

    print(b_mon_str)

    species_no = int(b_mon_str[curbyte:curbyte+9], 2)
    curbyte += 9
    print("Species: %d" % species_no)

    game_ver = int(b_mon_str[curbyte:curbyte+3], 2)
    curbyte += 3
    print("Game version: %d" % game_ver)

    level = int(b_mon_str[curbyte:curbyte+7], 2)
    curbyte += 7
    print("Level: %d" % level)

    item = int(b_mon_str[curbyte:curbyte+7], 2)
    curbyte += 7
    print("Item: %d" % item)

    nature = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("Nature: %d" % nature)

    ability = int(b_mon_str[curbyte:curbyte+1], 2)
    curbyte += 1
    print("ability: %d" % ability)

    gender = int(b_mon_str[curbyte:curbyte+1], 2)
    curbyte += 1
    print("gender: %d" % gender)

    shiny = int(b_mon_str[curbyte:curbyte+1], 2)
    curbyte += 1
    print("shiny: %d" % shiny)

    inbox = int(b_mon_str[curbyte:curbyte+4], 2)
    curbyte += 4
    print("in box: %d" % inbox)

    unownletter = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("unown letter (if applicable): %d" % unownletter)

    moveno = int(b_mon_str[curbyte:curbyte+9], 2)
    curbyte += 9
    print("move 1: %d" % moveno)

    moveno = int(b_mon_str[curbyte:curbyte+9], 2)
    curbyte += 9
    print("move 2: %d" % moveno)

    moveno = int(b_mon_str[curbyte:curbyte+9], 2)
    curbyte += 9
    print("move 3: %d" % moveno)

    moveno = int(b_mon_str[curbyte:curbyte+9], 2)
    curbyte += 9
    print("move 4: %d" % moveno)

    hpdv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("HP DV: %d" % hpdv)
    
    atkdv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("Atk DV: %d" % atkdv)
    
    defdv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("Def DV: %d" % defdv)
    
    spedv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("Spe DV: %d" % spedv)
    
    spadv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("SpA DV: %d" % spadv)
    
    spddv = int(b_mon_str[curbyte:curbyte+5], 2)
    curbyte += 5
    print("SpD DV: %d" % spddv)

    hpev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("HP EV: %d" % hpev)
    
    atkev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("Atk EV: %d" % atkev)
    
    defev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("Def EV: %d" % defev)
    
    speev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("Spe EV: %d" % speev)
    
    spaev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("SpA EV: %d" % spaev)
    
    spdev = int(b_mon_str[curbyte:curbyte+8], 2)
    curbyte += 8
    print("SpD EV: %d" % spdev)


if versionstr in [b"PNB4.0", b"PNB4.1"]:
    version = 4

    name_len = team[curbyte]
    curbyte += 1
    name = team[curbyte:curbyte+name_len]
    curbyte += name_len

    print("Name: %s" % name)

    extrainfo_len = team[curbyte]
    curbyte += 1
    extrainfo = team[curbyte:curbyte+extrainfo_len]
    curbyte += extrainfo_len

    print("Extra info: %s" % extrainfo)

    winmsg_len = team[curbyte]
    curbyte += 1
    winmsg = team[curbyte:curbyte+winmsg_len]
    curbyte += winmsg_len

    print("Win message: %s" % winmsg)

    losemsg_len = team[curbyte]
    curbyte += 1
    losemsg = team[curbyte:curbyte+losemsg_len]
    curbyte += losemsg_len

    print("Lose message: %s" % losemsg)

    game_version = team[curbyte]
    curbyte += 1

    avatar = team[curbyte]
    curbyte += 1

    sprite_type = team[curbyte]
    curbyte += 1

    POKELEN = 35

    for i in range(6):
        print("Mon %d" % i)
        mon = team[curbyte:curbyte+POKELEN]

        read_mon_str(mon)

        curbyte += POKELEN



else:
    print("currently unsupported")