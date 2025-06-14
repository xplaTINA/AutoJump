import threading
import time
import tkinter as tk
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

# round_type_names = {
#     1: "Classic",
#     2: "Fog",
#     3: "Punished",
#     4: "Sabotage",
#     5: "Cracked",
#     6: "Bloodbath",
#     7: "Double_Trouble",
#     8: "EX",
#     9: "Ghost",
#     10: "Unbound",
#     50: "Midnight",
#     51: "Alternate",
#     52: "Fog_Alternate",
#     53: "Ghost_Alternate",
#     100: "Mystic_Moon",
#     101: "Blood_Moon",
#     102: "Twilight",
#     103: "Solstice",
#     104: "RUN",
#     105: "Eight_Pages",
#     106: "GIGABYTE",
#     107: "Cold_Night"
# }
# terror_names = {
#     0: "huggy",
#     1: "Corrupted Toys",
#     2: "Demented Spongebob",
#     3: "Specimen 8",
#     4: "HER",
#     5: "Tails Doll",
#     6: "Black Sun",
#     7: "Aku Ball",
#     8: "Ao Oni",
#     9: "Toren's Shadow",
#     10: "[CENSORED]",
#     11: "WhiteNight",
#     12: "An Arbiter",
#     13: "Specimen 5",
#     14: "Comedy",
#     15: "Purple Guy",
#     16: "Spongefly swarm",
#     17: "Hush",
#     18: "Mope Mope",
#     19: "Sawrunner",
#     20: "Imposter",
#     21: "Something",
#     22: "Starved",
#     23: "The Painter",
#     24: "The Guidance",
#     25: "With Many Voices",
#     26: "Nextbots",
#     27: "Harvest",
#     28: "Smileghost",
#     29: "Karol_Corpse",
#     30: "MX",
#     31: "Big Bird",
#     32: "Dev Bytes",
#     33: "Luigi and Luigi dolls",
#     34: "V2",
#     35: "Withered Bonnie",
#     36: "The Boys",
#     37: "Something Wicked",
#     38: "Seek",
#     39: "Rush",
#     40: "Sonic",
#     41: "Bad Batter",
#     42: "Signus",
#     43: "Mirror",
#     44: "Legs",
#     45: "Mona and The mountain",
#     46: "Judgement Bird",
#     47: "Slenderwheels",
#     48: "Maul-A-Child",
#     49: "Garten Goers",
#     50: "Don't Touch Me",
#     51: "Specimen 2",
#     52: "Specimen 10",
#     53: "The Lifebringer",
#     54: "Pale Association",
#     55: "Toy Enforcer",
#     56: "TBH",
#     57: "DoomBox",
#     58: "Christian Brutal Sniper",
#     59: "Nosk",
#     60: "Apocrean Harvester",
#     61: "Arkus",
#     62: "Cartoon Cat",
#     63: "Wario Apparition",
#     64: "Shinto",
#     65: "Hell Bell",
#     66: "Security",
#     67: "The Swarm",
#     68: "Shiteyanyo",
#     69: "Bacteria",
#     70: "Tiffany",
#     71: "HoovyDundy",
#     72: "Haket",
#     73: "Akumii-kari",
#     74: "Lunatic Cultist",
#     75: "Sturm",
#     76: "Punishing Bird",
#     77: "Prisoner",
#     78: "Red Bus",
#     79: "Waterwraith",
#     80: "Astrum Aureus",
#     81: "Snarbolax",
#     82: "All-Around-Helpers",
#     83: "lain",
#     84: "Sakuya Izayoi",
#     85: "Arrival",
#     86: "Miros Bird",
#     87: "BFF",
#     88: "Scavenger",
#     89: "Tinky Winky",
#     90: "Tricky",
#     91: "Yolm",
#     92: "Red Fanatic",
#     93: "Dr. Tox",
#     94: "Ink Demon",
#     95: "Retep",
#     96: "Those Olden Days",
#     97: "S.O.S",
#     98: "Bigger Boot",
#     99: "The Pursuer",
#     100: "Spamton",
#     101: "Immortal Snail",
#     102: "Charlotte",
#     103: "Herobrine",
#     104: "Peepy",
#     105: "The Jester",
#     106: "Wild yet curious creature",
#     107: "Manti",
#     108: "Horseless Headless Horsemann",
#     109: "Ghost girl",
#     110: "Cubor's Revenge",
#     111: "Poly",
#     112: "Dog mimic",
#     113: "Warden",
#     114: "FOX squad",
#     115: "Express Train To Hell",
#     116: "Deleted",
#     117: "Killer Fish",
#     118: "Terror of Nowhere",
#     119: "Beyond",
#     120: "The Origin",
#     121: "Time Ripper",
#     122: "This Killer Does Not Exist",
#     123: "Parhelion's Victims",
#     124: "Bed Mecha",
#     125: "Killer rabbit",
#     126: "Bravera",
#     127: "Missingno",
#     128: "Living Shadow",
#     129: "The Plague Doctor",
#     130: "The Rat",
#     131: "Waldo",
#     132: "Clockey",
#     133: "Malicious Twins"
# }

# aterror_name = {
#     0: "Decayed Sponge",
#     1: "WHITEFACE",
#     2: "Sanic",
#     3: "Parhelion",
#     4: ",D@;Q7Y",
#     5: "Chomper",
#     6: "The Knight Of Toren",
#     7: "Tragedy",
#     8: "Apathy",
#     9: "MR MEGA",
#     10: "sm64.z64",
#     11: "Convict Squad",
#     12: "Paradise Bird",
#     13: "Angry Munci",
#     14: "Lord's Signal",
#     15: "Feddys",
#     16: "TBH Spy",
#     17: "Observation",
#     18: "(LISA)",
#     19: "Judas",
#     20: "Glaggle Gang",
#     21: "Try Not To Touch Me",
#     22: "Ambush",
#     23: "Teuthida",
#     24: "Eggman's Announcement",
#     25: "S.T.G.M",
#     26: "Army In Black",
#     27: "Bliss",
#     28: "Roblander",
#     29: "Fusion Pilot",
#     30: "Joy",
#     31: "The Red Mist",
#     32: "Sakuya The Ripper",
#     33: "Walpurgisnacht",
#     34: "Dev Maulers",
#     35: "Restless Creator"
# }

# sterror_name = {
#     0: "Meatball Man",
#     1: "Rift Monsters",
#     2: "GIGABYTE",
# }

# mterror_name = {
#     0: "Psychosis",
#     1: "Virus",
#     2: "Apocalypse Bird",
#     3: "Pandora"
# }

# vterror_name = {
#     0: "Hungry Home Invader",
#     1: "Alternates",
#     2: "Red Mist Apparition",
#     3: "Baldi",
#     4: "Shadow Freddy",
#     5: "Attrached",
#     6: "Wild Yet Bloodthirsty Creature",
#     7: "Searchlights"
# }

# item_names = {
#     1: "Radar",
#     2: "Medkit",
#     3: "Red Medkit",
#     4: "Have's Mysterious Brew",
#     5: "Portable Slots",
#     6: "Glow Coil",
#     7: "Psycho Coil",
#     8: "Teleporter",
#     9: "Pale Suitcase",
#     10: "Bloody Teleporter",
#     11: "Thorn Hacker",
#     12: "Soul Visitor",
#     13: "Speed Coil",
#     14: "Bloody Coil",
#     15: "Regen Coil",
#     16: "Pale Coil",
#     17: "Root Coil",
#     18: "Metal Bat",
#     19: "Bloody Bat",
#     20: "Justitia",
#     21: "Colorable Bat",
#     22: "Metal Pipe",
#     23: "Ghost Bat",
#     24: "Silver Kat Charm",
#     25: "Bloody Kat Charm",
#     26: "Luna Charm",
#     27: "Chaos Coil",
#     28: "Twilight Coil",
#     29: "Glass Coil",
#     30: "Corkscrew Coil",
#     31: "Destroyer Coil",
#     32: "Antique Revolver",
#     33: "Bloody Revolver",
#     34: "Pale Pistol",
#     35: "Hamburger",
#     36: "Haunted Burger",
#     37: "Beyond Plush",
#     38: "Nora Plush",
#     39: "Magic Conch",
#     40: "Radar Coil",
#     41: "Rubber Mallet",
#     42: "Banana",
#     43: "TBH",
#     44: "Taser",
#     45: "Darkgrey Plush",
#     46: "Roblander Plush",
#     47: "Delicate Coil",
#     48: "Emerald Coil",
#     49: "Pot of Greed",
#     50: "Brick",
#     51: "Luxury Coil",
#     52: "Blue Medkit",
#     53: "Sealed Sword",
#     54: "Gran Faust",
#     55: "Divine Avenger",
#     56: "Maxwell",
#     57: "Rock",
#     58: "Illumina",
#     59: "Redbull",
#     60: "Omori Plush",
#     61: "Paradise Lost",
#     62: "Have Plush",
#     63: "Observation Plush",
#     64: "Joyous Orb",
#     65: "Jailbird",
#     66: "Thorn Glognut",
#     67: "Silver Coil",
#     68: "Snowy Coil",
#     69: "Torch of Obsession",
#     70: "Dropkick",
#     71: "Wave Coil",
#     72: "Shape & ???",
#     73: "Overseer Plush",
#     74: "Darkheart",
#     75: "Knife (SABOTAGE)",
#     76: "Carrot (Mara)",
#     77: "Wispy WISPYYY!!!",
#     79: "Judia (Nicomal) & Memoria (バ亀⁄bakame)",
#     80: "Dev Phone",
#     81: "Fuwatti Plush",
#     82: "Seer Pen",
#     83: "NeoTamago",
#     84: "IJED",
#     85: "Mini Chest",
#     86: "Panthera MK.II",
#     87: "King's Kit"
# }


import tkinter as tk
import threading
import time
import asyncio
import websockets
import json
from pythonosc.udp_client import SimpleUDPClient

# === OSC送信設定 ===
send_ip = "127.0.0.1"
send_port = 9000
client = SimpleUDPClient(send_ip, send_port)

# === OSC送信関数 ===
def send_osc_parameter(address, value):
    client.send_message(address, value)

# === 状態フラグ ===
auto_jump_enabled = False
circle_chase_enabled = False
round_start_enabled = False

# === AutoJumpループ ===
def auto_jump_loop():
    global auto_jump_enabled
    while True:
        if auto_jump_enabled:
            send_osc_parameter("/input/Jump", True)
            time.sleep(1)
            send_osc_parameter("/input/Jump", False)
            print("Jump signal sent. Waiting 70 seconds...")
            time.sleep(70)
        else:
            time.sleep(0.5)

# === 円チェイスループ ===
def circle_chase_loop():
    global circle_chase_enabled
    while True:
        if circle_chase_enabled:
            send_osc_parameter("/input/MoveForward", 1)
            send_osc_parameter("/input/LookRight", 1)
            time.sleep(0.1)
            send_osc_parameter("/input/LookRight", 0)
            time.sleep(0.5)
            send_osc_parameter("/input/MoveForward", 0)
        else:
            time.sleep(0.5)

def round_start():
    global round_start_enabled
    while True:
        if round_start_enabled:
            send_osc_parameter("/input/MoveForward", 1)
            time.sleep(2.5)
            send_osc_parameter("/input/MoveForward", 0)
            send_osc_parameter("/input/LookLeft", 1)
            time.sleep(0.3)
            send_osc_parameter("/input/LookLeft", 0)
            time.sleep(0.1)
            send_osc_parameter("/input/UseRight", 1)
            time.sleep(0.1)
            send_osc_parameter("/input/UseRight", 0)
            round_start_enabled = False

# === OSC受信 + WebSocket処理 ===
async def listen():
    uri = "ws://localhost:11398"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            try:
                data = json.loads(message)
                name = data.get("Name")
                if name == "TerrorName":
                    terror1_var.set(f"Terror1: {data.get('Value')}")
                if name == "RoundType":
                    roundtype_var.set(f"RoundType: {data.get('Value')}")
                if name == "ItemName":
                    item_var.set(f"Item: {data.get('Value')}")
                print(name)
            except json.JSONDecodeError:
                print("JSONパース失敗:", message)

def start_websocket_thread():
    asyncio.run(listen())

# === UI処理 ===
def toggle_auto_jump():
    global auto_jump_enabled
    auto_jump_enabled = not auto_jump_enabled
    status_label.config(text=f"Auto Jump: {'ON' if auto_jump_enabled else 'OFF'}")
    toggle_button.config(text="停止" if auto_jump_enabled else "開始")

def toggle_circle_chase():
    global circle_chase_enabled
    circle_chase_enabled = not circle_chase_enabled
    circle_button.config(text="円チェイス停止" if circle_chase_enabled else "円チェイス開始")

def toggle_round_start():
    global round_start_enabled
    round_start_enabled = not round_start_enabled
    circle_button.config(text="ラウンド停止" if round_start_enabled else "ラウンド開始")

# === tkinter ウィンドウ構築 ===
root = tk.Tk()
root.title("VRChat AutoJump & CircleChase")
root.geometry("500x350")

toggle_button = tk.Button(root, text="開始", width=20, height=2, command=toggle_auto_jump)
toggle_button.pack(pady=10)

circle_button = tk.Button(root, text="円チェイス開始", width=20, height=2, command=toggle_circle_chase)
circle_button.pack(pady=5)

round_start_button = tk.Button(root, text="ラウンド開始", width=20, height=2, command=toggle_round_start)
round_start_button.pack(pady=5)


status_label = tk.Label(root, text="Auto Jump: OFF", font=("Arial", 14))
status_label.pack()

terror1_var = tk.StringVar(value="Terror1: 未受信")
roundtype_var = tk.StringVar(value="RoundType: 未受信")
item_var = tk.StringVar(value="Item: 未受信")

tk.Label(root, textvariable=terror1_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=roundtype_var, font=("Arial", 12)).pack()
tk.Label(root, textvariable=item_var, font=("Arial", 12)).pack()

# === スレッド起動 ===
threading.Thread(target=auto_jump_loop, daemon=True).start()
threading.Thread(target=circle_chase_loop, daemon=True).start()
threading.Thread(target=start_websocket_thread, daemon=True).start()
threading.Thread(target=round_start, daemon=True).start()

# === UI開始 ===
root.mainloop()
