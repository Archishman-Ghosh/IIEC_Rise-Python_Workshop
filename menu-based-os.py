import os
while True:
    inp = input("Which application do you want to launch?")
    if 'launch' in inp or 'run' in inp or 'start' in inp or 'execute' in inp:
        if 'notepad' in inp or 'editor' in inp:
            os.system('start notepad')
        elif 'chrome' in inp or 'browser' in inp or 'internet' in inp:
            os.system('start chrome')
        elif 'player' in inp or 'video' in inp:
            os.system('start KMPlayer64')
        else:
            print("Doesn't support")
    elif 'exit' in inp:
        break
    else:
        print("Doesn't support")
        
