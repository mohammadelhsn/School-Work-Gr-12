import random 
import time


def distribute():
    attributes = {
            "strength": 0,
            "iq": 0,
            "constituion": 0,
            "dexterity": 0,
            "piety": 0,
            "luck": 0
        }

    pts = 0

    while pts != 37:
        pts = 0
        for i in attributes: 
            ranNum = random.randint(1,9)
            attributes[i] = ranNum
            pts += ranNum
    
    return attributes

class Character: 
    def __init__(self, name) -> None:
        self.name: str = name
        self.attributes = distribute()
        self.strength: int = self.attributes["strength"]
        self.iq: int = self.attributes["iq"]
        self.constituion: int = self.attributes["constituion"]
        self.dexterity: int = self.attributes["dexterity"]
        self.piety: int = self.attributes["piety"]
        self.luck: int = self.attributes["luck"]
    def refresh(self):
        self.strength: int = self.attributes["strength"]
        self.iq: int = self.attributes["iq"]
        self.constituion: int = self.attributes["constituion"]
        self.dexterity: int = self.attributes["dexterity"]
        self.piety: int = self.attributes["piety"]
        self.luck: int = self.attributes["luck"]
    def addPoints(self, attribute):
        self.refresh()
        self.attributes[attribute] = self.attributes[attribute] + 1
    def isFighter(self):
        self.refresh()
        if (self.strength >= 7 and self.dexterity >= 7): return True
        else: return False
    def isMage(self): 
        self.refresh()
        if (self.iq >= 8 and self.constituion >= 9): return True
        else: return False
    def isThief(self):
        self.refresh()
        if (self.dexterity >= 7 and self.luck >= 9): return True
        else: return False
    def isCleric(self):
        self.refresh()
        if (self.piety >= 9 and self.iq >= 6): return True
        else: return False
    def isAssassin(self):
        self.refresh()
        if (self.luck >= 5 and self.strength >= 8 and self.dexterity >= 7): return True
        else: return False
    def displayPts(self):
        self.refresh()
        print(self.name.title())
        print(f"💪 | Strength: {self.strength}")
        print(f"🧠 | IQ: {self.iq}")
        print(f"➕ | Constituion: {self.constituion}")
        print(f"👷 | Dexterity: {self.dexterity}")
        print(f"🙏 | Piety: {self.piety}")
        print(f"🍀 | Luck: {self.luck}")
    def highest(self):
        self.refresh()
        highest = { "name": 'none', "value": 0}

        if (self.isFighter()): 
            highest["name"] = "fighter"
            highest["value"] = self.strength + self.dexterity
        if (self.isMage()): 
            mage = self.iq + self.constituion

            if (mage > highest["value"]): 
                highest["value"] = mage
                highest["name"] = "mage"
        if (self.isThief()): 
            thief = self.dexterity + self.luck

            if (thief > highest["value"]):
                highest["value"] = thief
                highest["name"] = "thief"
        if (self.isCleric()):
            cleric =  self.piety + self.iq

            if (cleric > highest["value"]): 
                highest["value"] = cleric
                highest["name"] = "cleric"
        if (self.isAssassin()): 
            assassin = self.luck + self.strength + self.dexterity

            if (assassin > highest["value"]): 
                highest["value"] = assassin
                highest["name"] = "assassin"
        self.highestValue = highest
        return highest
    def getascii(self):
        if (self.highestValue["name"] == "assassin"): 
            return r'''
                                            .-""""-.
                            / j      \
                            :.d;       ;
                            $$P        :
                .m._       $$         :
                dSMMSSSss.__$$b.    __ :
                :MMSMMSSSMMMSS$$$b  $$P ;
                SMMMSMMSMMMSSS$$$$     :b
                dSMMMSMMMMMMSSMM$$$b.dP SSb.
            dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
            :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
            SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.
            dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm
            dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;
        .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;
        dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM
        :MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM
        MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
        "TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
        )MMMMMMM;     _/\\    :`.:    :MMMMMMMM
        d$SS$$$MMMb.  |._\\\   :`.:     MMMMMMMM
        T$$S$$$$$$$$$$m;O\\\\"-;`.:_.-  MMMMMMM;
        :$$$$$$$$$$$$$$$b_l./\\ ;`.:    mMMSSMMM;
        :$$$$$$$$$$$$$$$$$$$./\\;`.:  .$$MSMMMMMM
        $$$$$$$$$$$$$$$$$$$$. \\`.:.$$$$SMSSSMMM;
        $$$$$$$$$$$$$$$$$$$$$. \\.:$$$$$SSMMMMMMM
        :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
        :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
        $$$$$$$$$;"^$J "^$$$$;.`.$$P  `SSSMMMM
        :$$$$$$$$$       :$$$;.`.P'..   TMMM$$b
        :$$$$$$$$$;      $$$$;.`/ c^'   d$$$$$S;
        $$$$$S$$$$;      '^^^:_d$g:___.$$$$$$SSS
        $$$$SS$$$$;            $$$$$$$$$$$$$$SSS;
        :$$$SSSS$$$$            : $$$$$$$$$$$$$SSS
        :$P"TSSSS$$$            ; $$$$$$$$$$$$$SSS;
        j    `SSSSS$           :  :$$$$$$$$$$$$$SS$
        :       "^S^'           :   $$$$$$$$$$$$$S$;
        ;.____.-;"               "--^$$$$$$$$$$$$$P
        '-....-"  bug                  ""^^T$$$$P"
        '''
        if (self.highestValue["name"] == "fighter"):
            return r"""
                                            /////'
                                '  # o
                                C   - |
                    ___          '  =__'        ___
                    (` _ \_       |   |        _/  ')
                    \  (__\  ,---- _ |----.  /__)- |
                    \__  ( (           /  ) )  __/
                        |_X_\/ \.   #  _.|  \/_X_|
                        |  \ /(   /    /\ /  |
                        \ /  (  ,    /  \ _/
                                /______/
                            [:::::::]
                            /*%*%*%*%*\
                            >%*%#%*%*%|
                            /%*%*#*%*%*\
                            ######^######  b'ger"""
        if (self.highestValue["name"] == "mage"):
            return r"""
                          _,._      
  .||,       /_ _\\     
 \.`',/      |'L'| |    
 = ,. =      | -,| L    
 / || \    ,-'\"/,'`.   
   ||     ,'   `,,. `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | >-'' _,\\ 
   ||'      ==\ ,-'  ,' 
   ||       |  V \ ,|   
   ||       |    |` |   
   ||       |    |   \  
   ||       |    \    \ 
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/       
   ||                hjm"""

        if (self.highestValue["name"] == "thief"):
            return  r"""
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣶⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⠿⠿⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠙⠷⣄⠙⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡄⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⣄⠀⠀⠈⠻⠟⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣄⠀⠀⠀⠀⢠⣿⡇⠀⠀⠙⠻⢶⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣤⣀⣴⣿⣿⡄⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠿⠿⠛⠉⠻⣿⣿⣷⣀⡀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⣠⣤⣶⣄⠀⠘⢿⠃⠉⠛⠻⣶⣶⣤⣤⣄⡀⠀⠙⢿⣿⣿⣿⠟⢿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣦⡀⠀⠹⠟⠁⣠⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            """

        if (self.highestValue["name"] == "cleric"):
            return r'''
                        ,-----.
           #,-. ,-.#
          () a   e ()
          (   (_)   )
          #\_  -  _/#
        ,'   `"""`    `.
      ,'      \X/      `.
     /         X     ____\
    /          v   ,`  v  `,
   /    /         ( <==+==> )
   `-._/|__________\   ^   /
  (\\)  |______@____\  ^  /
    \\  |     ( )    \ ^ /
     )  |             \^/
    (   |             |v
   <(^)>|             |
     v  |             |
        |             |
ZOT     |_.--.__ .--._|
          `==='  `===`'''
while True:
        name = input("What is the name of the character? ")

        # output randomly assigned points

        char = Character(name)

        pts = 3
        while pts != 0:
            maxPts = "You have already added the maximum points for this attribute"


            char.displayPts()
            print(f"You have {pts} point(s) to distribute to any attribute")

            attribute = int(input("Where would you like to add points?\n1) 💪 | Strength\n2) 🧠 | IQ\n3) ➕ | Constituion\n4) 👷 | Dexterity\n5) 🙏 | Piety\n6) 🍀 | Luck\n"))

            fighter = char.isFighter()

            if (fighter == True): print("Your character is well suited to be a Fighter")

            mage = char.isMage()

            if (mage == True): print("Your character is well suited to be a Mage")

            thief = char.isThief()

            if (thief == True): print("Your character is well suited to be a Thief")

            cleric = char.isCleric()

            if (cleric == True): print("Your character is well suited to be a Cleric")

            assassin = char.isAssassin()

            if (assassin == True): print("Your character is well suited to be an Assassin")

            if (attribute == 1): 
                if (char.strength == 10): 
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("strength")
                    pts = pts - 1
            elif (attribute == 2): 
                if (char.iq == 10): 
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("iq")
                    pts = pts - 1
            elif (attribute == 3): 
                if (char.constituion == 10):
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("constituion")
                    pts = pts - 1
            elif (attribute == 4): 
                if (char.dexterity == 10): 
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("dexterity")
                    pts = pts - 1
            elif (attribute == 5): 
                if (char.piety == 10): 
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("piety")
                    pts = pts - 1
            elif (attribute == 6): 
                if (char.luck == 10): 
                    print(maxPts)
                    continue
                else: 
                    char.addPoints("luck")
                    pts = pts - 1
            else: 
                print("Invalid choice!")
                continue

            highest = char.highest()

        if (highest["value"] == 0): 
            print("You are not well suited to be any character! Try again!")
        else: 
            print(f'Your character is a {highest["name"]} with a value of {highest["value"]}')

            restart = int(input("Are you happy with this character? (0 for no, 1 for yes)"))

            if (restart == 0): pass
            else: 
                file = open(f"{char.name}.txt", "w")
                art = char.getascii()
                file.write(art)
                file.close()
