members = ['drus_s', 'Dostatochno_geniy']
printing_members = []
is_printed = False
for member in members:
    if member:
        if len(' '.join(printing_members)) + len(member) + 2 <= 4096:
            printing_members.append('@' + member)
        else:
            print(' '.join(printing_members))
            printing_members = []
            is_printed = True
if not is_printed:
    print(printing_members)