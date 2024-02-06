members = ['@drus_s', '@Dostatochno_geniy']
stop_printing = False
while not stop_printing:
    printing_members = ''
    while members and len(printing_members) + len(members[0]) + 1 < 4096:
        printing_members += members[0] + ' '
        del members[0]
    if not members:
        stop_printing = True
    print(printing_members)