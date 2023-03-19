from AresReader import AresReader

ares = AresReader(ic = '87344416')
data = ares.printAres()
print(f"Zjistene informace: {data}")