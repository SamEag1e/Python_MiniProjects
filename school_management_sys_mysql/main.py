import ManagerPanel
import ExpertPanel
import TeacherPanel

while True:
    panel = (input("\n\nTeacher:t\tExpert:e\tManager:m\tExit:exit\n")).upper()
    if panel == "T":
        print("\n\n\t\tConnected as Teacher")
        TeacherPanel.what_to_do()
    if panel == "M":
        print("\n\n\t\tConnected as Manager")
        ManagerPanel.what_to_do()
    if panel == "E":
        print("\n\n\t\tConnected as Expert")
        ExpertPanel.what_to_do()
    if panel == "EXIT":
        exit()

# Problem 1: age daneshjuyi tuye bish az yek dore hozor dashte bashe
#               Lazeme chandin bar add beshe ba username jadid
#               chon tuye table e users, username UNIQUE tarif kardam.
#               in bayad ye rah hal behtari dashte bashe.

# Problem 2: Esm dore ha nbayad space va bazi character ha ro dashte bashe
#               ba esme dore ha gharare TABLE sakhte beshe....

# Problem 3: Error hayi ke ehtemal dare dar heyne add kardan be DB bede...
#           masalan yeki dota add mishe baad esmesh ok nis va....
#           va az onja be baad mimune, dar hali ke ghabli ha add shode.
