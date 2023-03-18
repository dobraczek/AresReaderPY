from AresReader import AresReader

# vypis nahodnyho uzivatele (muze i zeny)
ares = AresReader(ic = '87344416')
data = ares.printAres()
print(f"Zjistene informace: {data}")