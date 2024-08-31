import getfromweb
messages = []
pt=[]
potato_taag=[
"$$$$$$$\\             $$\\                $$\\               ",
"$$  __$$\\            $$ |               $$ |              ",
"$$ |  $$ | $$$$$$\\ $$$$$$\\    $$$$$$\\ $$$$$$\\    $$$$$$\\"  ,
"$$$$$$$  |$$  __$$\\\\_$$  _|   \\____$$\\\\_$$  _|  $$  __$$\\" ,
"$$  ____/ $$ /  $$ | $$ |     $$$$$$$ | $$ |    $$ /  $$ |",
"$$ |      $$ |  $$ | $$ |$$\\ $$  __$$ | $$ |$$\\ $$ |  $$ |",
"$$ |      \\$$$$$$  | \\$$$$  |\\$$$$$$$ | \\$$$$  |\\$$$$$$  |",
"\\__|       \\______/   \\____/  \\_______|  \\____/  \\______/ ",
]

loadingui=[]
loadingui.append("[               ]")
loadingui.append("[#              ]")
loadingui.append("[##             ]")
loadingui.append("[###            ]")
loadingui.append("[ ###           ]")
loadingui.append("[  ###          ]")
loadingui.append("[   ###         ]")
loadingui.append("[    ###        ]")
loadingui.append("[     ###       ]")
loadingui.append("[      ###      ]")
loadingui.append("[       ###     ]")
loadingui.append("[        ###    ]")
loadingui.append("[         ###   ]")
loadingui.append("[          ###  ]")
loadingui.append("[           ### ]")
loadingui.append("[            ###]")
loadingui.append("[             ##]")
loadingui.append("[              #]")
loadingui.append("[               ]")

def getandreturn():
    messages = getfromweb.potatoget()
    message = f"公 告:{messages[0]}"        
    loadingui.append(message)

def guireturn(index:int):
    mode = False
    try:
        message=loadingui[19]
        quitevent="click 's' to start"
        mode = True
    except IndexError:
        message=loadingui[index]

    if mode:
        pt=potato_taag.copy()
        pt.append(message)
        pt.append(quitevent)
        return pt,mode
    else:
        pt=potato_taag.copy()
        pt.append(message)
        pt.append('')
        return pt,mode