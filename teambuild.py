from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import beckett
import pokepy
import os
pk = pokepy.V2Client()
root = Tk()
root.title("Pokemon Team Builder")
icon = PhotoImage(data=b'iVBORw0KGgoAAAANSUhEUgAAAA8AAAAPCAYAAAA71pVKAAAAeklEQVQ4T6WTSxLAIAhD4f6HplMUBjVpdXSJPMMnquBjIK'
                       b'xzbA449EMmU2FDEFFzLuAtMB7qkF7DR6pV/VWG8DAMMnqHybrEzESzszWrKQPtCrF7CrNqsmfVsqqDsfWqyqouYHcl6m1x'
                       b'WNMbHBY5zdvfA4TeriJbv+oBsrkuCxKhAwoAAAAASUVORK5CYIIA')
root.wm_iconphoto(True, icon)

res2 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
res4 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
weak2 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
weak4 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
neutral = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
immune = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}

ores2 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
oweak2 = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
oneutral = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}
oimmune = {
    "normal": 0,
    "fire": 0,
    "fighting": 0,
    "water": 0,
    "flying": 0,
    "grass": 0,
    "poison": 0,
    "electric": 0,
    "ground": 0,
    "psychic": 0,
    "rock": 0,
    "ice": 0,
    "bug": 0,
    "dragon": 0,
    "ghost": 0,
    "dark": 0,
    "steel": 0,
    "fairy": 0
}

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
tabs = ttk.Notebook(root)
tabs.grid(column=0, row=0)
defense = ttk.Frame(tabs)
offense = ttk.Frame(tabs)

tabs.add(defense, text='Defensive')
tabs.add(offense, text='Offensive')
for r in range(7):
    defense.columnconfigure(r, minsize=130)
    offense.columnconfigure(r, minsize=130)

# <editor-fold desc="Name Init">
name1 = StringVar()
name2 = StringVar()
name3 = StringVar()
name4 = StringVar()
name5 = StringVar()
name6 = StringVar()
names = (name1, name2, name3, name4, name5, name6)
count = -1
for n in names:
    count += 1
    ttk.Entry(defense, width=7, textvariable=n).grid(column=count, row=0, sticky=(W, E))
    ttk.Entry(offense, width=7, textvariable=n).grid(column=count, row=0, sticky=(W, E))
# </editor-fold>

# <editor-fold desc="Dict Init">
gimmune = dict((d, IntVar(value=v)) for (d, v) in immune.items())
gres2 = dict((d, IntVar(value=v)) for (d, v) in res2.items())
gres4 = dict((d, IntVar(value=v)) for (d, v) in res4.items())
gweak2 = dict((d, IntVar(value=v)) for (d, v) in weak2.items())
gweak4 = dict((d, IntVar(value=v)) for (d, v) in weak4.items())
gneutral = dict((d, IntVar(value=v)) for (d, v) in neutral.items())

goimmune = dict((d, IntVar(value=v)) for (d, v) in immune.items())
gores2 = dict((d, IntVar(value=v)) for (d, v) in res2.items())
goweak2 = dict((d, IntVar(value=v)) for (d, v) in weak2.items())
goneutral = dict((d, IntVar(value=v)) for (d, v) in neutral.items())
# </editor-fold>

# <editor-fold desc="Pokemon Init">
pokemon1 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
pokemon2 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
pokemon3 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
pokemon4 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
pokemon5 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
pokemon6 = {
    "Pokemon": None,
    "Type1": None,
    "Type2": None
}
# </editor-fold>


def do_the_thing(*args):
    global gimmune, gres2, gres4, gweak2, gweak4, gneutral, goimmune, goneutral, gores2, goweak2
    gvars = (gimmune, gres2, gres4, gweak2, gweak4, gneutral, goimmune, goneutral, gores2, goweak2)
    for d in gvars:
        for v in d.values():
            v.set(0)
    try:
        p1 = pk.get_pokemon(name1.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p1 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name1.get()}.')
        p1 = None
    try:
        p2 = pk.get_pokemon(name2.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p2 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name2.get()}.')
        p2 = None
    try:
        p3 = pk.get_pokemon(name3.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p3 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name3.get()}.')
        p3 = None
    try:
        p4 = pk.get_pokemon(name4.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p4 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name4.get()}.')
        p4 = None
    try:
        p5 = pk.get_pokemon(name5.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p5 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name5.get()}.')
        p5 = None
    try:
        p6 = pk.get_pokemon(name6.get().lower())[0]
    except beckett.exceptions.MissingUidException:
        p6 = None
    except beckett.exceptions.InvalidStatusCodeError:
        messagebox.showinfo('Error!', f'Could not find a pokemon named {name6.get()}.')
        p6 = None

    pokemon1["Pokemon"] = p1
    pokemon2["Pokemon"] = p2
    pokemon3["Pokemon"] = p3
    pokemon4["Pokemon"] = p4
    pokemon5["Pokemon"] = p5
    pokemon6["Pokemon"] = p6

    team = (pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6)
    team_actual = []

    for y in team:
        if y["Pokemon"] is not None:
            if len(y["Pokemon"].types) == 2:
                y["Type1"] = pk.get_type(y["Pokemon"].types[1].type.name)[0]
                y["Type2"] = pk.get_type(y["Pokemon"].types[0].type.name)[0]
            else:
                y["Type1"] = pk.get_type(y["Pokemon"].types[0].type.name)[0]
            team_actual.append(y)
        else:
            pass
    for x in team_actual:
        temp_list = []
        if x["Type2"] is None:
            for a in x["Type1"].damage_relations.double_damage_from:
                if a.name in temp_list:
                    break
                else:
                    gweak2[a.name].set(gweak2[a.name].get()+1)
                    temp_list.append(a.name)
            for b in x["Type1"].damage_relations.half_damage_from:
                if b.name in temp_list:
                    break
                else:
                    gres2[b.name].set(gres2[b.name].get()+1)
                    temp_list.append(b.name)
            for c in x["Type1"].damage_relations.no_damage_from:
                if c.name in temp_list:
                    break
                else:
                    gimmune[c.name].set(gimmune[c.name].get()+1)
                    temp_list.append(c.name)
            for d in gneutral:
                if d not in temp_list:
                    gneutral[d].set(gneutral[d].get()+1)

        else:
            for dd1 in x["Type1"].damage_relations.double_damage_from:
                for dd2 in x["Type2"].damage_relations.double_damage_from:
                    if dd1.name in temp_list:
                        pass
                    else:
                        if dd1.name == dd2.name:
                            gweak4[dd1.name].set(gweak4[dd1.name].get()+1)
                            temp_list.append(dd1.name)
                for hd2 in x["Type2"].damage_relations.half_damage_from:
                    if dd1.name in temp_list:
                        pass
                    else:
                        if dd1.name == hd2.name:
                            gneutral[dd1.name].set(gneutral[dd1.name].get()+1)
                            temp_list.append(dd1.name)
                for nd2 in x["Type2"].damage_relations.no_damage_from:
                    if dd1.name in temp_list:
                        pass
                    else:
                        if dd1.name == nd2.name:
                            gimmune[dd1.name].set(gimmune[dd1.name].get()+1)
                            temp_list.append(dd1.name)
                if dd1.name in temp_list:
                    pass
                else:
                    gweak2[dd1.name].set(gweak2[dd1.name].get()+1)
                    temp_list.append(dd1.name)
            for hd1 in x["Type1"].damage_relations.half_damage_from:
                for dd2 in x["Type2"].damage_relations.double_damage_from:
                    if hd1.name in temp_list:
                        pass
                    else:
                        if hd1.name == dd2.name:
                            gneutral[hd1.name].set(gneutral[hd1.name].get()+1)
                            temp_list.append(hd1.name)
                for hd2 in x["Type2"].damage_relations.half_damage_from:
                    if hd1.name in temp_list:
                        pass
                    else:
                        if hd1.name == hd2.name:
                            gres4[hd1.name].set(gres4[hd1.name].get()+1)
                            temp_list.append(hd1.name)
                for nd2 in x["Type2"].damage_relations.no_damage_from:
                    if hd1.name in temp_list:
                        pass
                    else:
                        if hd1.name == nd2.name:
                            gimmune[hd1.name].set(gimmune[hd1.name].get()+1)
                            temp_list.append(hd1.name)
                if hd1.name in temp_list:
                    pass
                else:
                    gres2[hd1.name].set(gres2[hd1.name].get()+1)
                    temp_list.append(hd1.name)
            for nd1 in x["Type1"].damage_relations.no_damage_from:
                if nd1.name in temp_list:
                    pass
                else:
                    gimmune[nd1.name].set(gimmune[nd1.name].get()+1)
                    temp_list.append(nd1.name)
            for d in x["Type2"].damage_relations.double_damage_from:
                if d.name in temp_list:
                    pass
                else:
                    gweak2[d.name].set(gweak2[d.name].get()+1)
                    temp_list.append(d.name)
            for e in x["Type2"].damage_relations.half_damage_from:
                if e.name in temp_list:
                    pass
                else:
                    gres2[e.name].set(gres2[e.name].get()+1)
                    temp_list.append(e.name)
            for f in x["Type2"].damage_relations.no_damage_from:
                if f.name in temp_list:
                    pass
                else:
                    gimmune[f.name].set(gimmune[f.name].get()+1)
                    temp_list.append(f.name)
            for g in gneutral:
                if g not in temp_list:
                    gneutral[g].set(gneutral[g].get()+1)

        temp_list_1 = []
        temp_list_2 = []
        for a in x["Type1"].damage_relations.double_damage_to:
            if a.name in temp_list_1:
                break
            else:
                goweak2[a.name].set(goweak2[a.name].get()+1)
                temp_list_1.append(a.name)
        for b in x["Type1"].damage_relations.half_damage_to:
            if b.name in temp_list_1:
                break
            else:
                gores2[b.name].set(gores2[b.name].get()+1)
                temp_list_1.append(b.name)
        for c in x["Type1"].damage_relations.no_damage_to:
            if c.name in temp_list_1:
                break
            else:
                goimmune[c.name].set(goimmune[c.name].get()+1)
                temp_list_1.append(c.name)
        if x["Type2"] is not None:
            for a in x["Type2"].damage_relations.double_damage_to:
                if a.name in temp_list_2:
                    break
                else:
                    goweak2[a.name].set(goweak2[a.name].get()+1)
                    temp_list_2.append(a.name)
            for b in x["Type2"].damage_relations.half_damage_to:
                if b.name in temp_list_2:
                    break
                else:
                    gores2[b.name].set(gores2[b.name].get()+1)
                    temp_list_2.append(b.name)
            for c in x["Type2"].damage_relations.no_damage_to:
                if c.name in temp_list_2:
                    break
                else:
                    goimmune[c.name].set(goimmune[c.name].get()+1)
                    temp_list_2.append(c.name)
            for d in goneutral:
                if d not in temp_list_2:
                    goneutral[d].set(goneutral[d].get()+1)


# <editor-fold desc="Types">
count = 1
ttk.Label(defense, text='Type').grid(column=0, row=1)
ttk.Label(offense, text='Type').grid(column=0, row=1, columnspan=2)
for i in immune:
    count += 1
    ttk.Label(defense, text=i.capitalize()).grid(column=0, row=count)
    ttk.Label(offense, text=i.capitalize()).grid(column=0, row=count, columnspan=2)
# </editor-fold>

# <editor-fold desc="Immune">
ttk.Label(defense, text='Immune').grid(column=1, row=1)
ttk.Label(offense, text='Immune').grid(column=1, row=1, columnspan=2)
count = 1
for i in gimmune:
    count += 1
    ttk.Label(defense, textvariable=gimmune[i]).grid(column=1, row=count)
    ttk.Label(offense, textvariable=goimmune[i]).grid(column=1, row=count, columnspan=2)
# </editor-fold>

# <editor-fold desc="1/4 Damage">
ttk.Label(defense, text='1/4x Damage').grid(column=2, row=1)
count = 1
for i in gres4:
    count += 1
    ttk.Label(defense, textvariable=gres4[i]).grid(column=2, row=count)
# </editor-fold>

# <editor-fold desc="1/2 Damage">
ttk.Label(defense, text='1/2x Damage').grid(column=3, row=1)
ttk.Label(offense, text='1/2x Damage').grid(column=2, row=1, columnspan=2)
count = 1
for i in gres2:
    count += 1
    ttk.Label(defense, textvariable=gres2[i]).grid(column=3, row=count)
    ttk.Label(offense, textvariable=gores2[i]).grid(column=2, row=count, columnspan=2)
# </editor-fold>

# <editor-fold desc="Neutral Damage">
ttk.Label(defense, text='Neutral Damage').grid(column=4, row=1)
ttk.Label(offense, text='Neutral Damage').grid(column=3, row=1, columnspan=2)
count = 1
for i in gneutral:
    count += 1
    ttk.Label(defense, textvariable=gneutral[i]).grid(column=4, row=count)
    ttk.Label(offense, textvariable=goneutral[i]).grid(column=3, row=count, columnspan=2)
# </editor-fold>

# <editor-fold desc="2x Damage">
ttk.Label(defense, text='2x Damage').grid(column=5, row=1)
ttk.Label(offense, text='2x Damage').grid(column=4, row=1, columnspan=2)
count = 1
for i in gweak2:
    count += 1
    ttk.Label(defense, textvariable=gweak2[i]).grid(column=5, row=count)
    ttk.Label(offense, textvariable=goweak2[i]).grid(column=4, row=count, columnspan=2)
# </editor-fold>

# <editor-fold desc="4x Damage">
ttk.Label(defense, text='4x Damage').grid(column=6, row=1)
count = 1
for i in gweak4:
    count += 1
    ttk.Label(defense, textvariable=gweak4[i]).grid(column=6, row=count)
# </editor-fold>

ttk.Button(defense, text="Calculate", command=do_the_thing).grid(column=6, row=0)
ttk.Button(offense, text="Calculate", command=do_the_thing).grid(column=6, row=0)

for child in tabs.winfo_children():
    for kids in child.winfo_children():
        kids.grid_configure(padx=5, pady=5)
        for babies in kids.winfo_children():
            babies.grid_configure(padx=5, pady=5)
root.bind('<Return>', do_the_thing)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
