print('Today, I watched the Champions League final.')

mancity_players = ['Ederson (GK)', 'Walker', 'Stones', 'Dias', 'Zinchenko', 'B.Silva', 'Gündogan', 'Foden', 'Mahrez', 'De Bruyne (C)', 'Sterling']
chelsea_players = ['Mendy (GK)', 'Rüdiger', 'T.Silva', 'Azpilicueta (C)', 'Chilwell', 'Jorginho', 'Kanté', 'James', 'Mount', 'Havertz', 'Werner']
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print(f'Man City starting 11: {mancity_players}')
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print(f'Chelsea starting 11: {chelsea_players}')
print('--------------------------------------------------------------------------------------------------------------------------------------------')

print('Match begins.')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

mancity_players.remove('Gündogan')
mancity_players.insert(6, 'Gündogan (Y)')
print(f'34 mins: Yellow Card for Gündogan (Man City) {mancity_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_players.remove('T.Silva')
chelsea_players.insert(2, 'Christensen')
print(f'39 mins: Chelsea Substitution (Injury)  < IN: Christensen   > OUT: T.Silva {chelsea_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_players.remove('Havertz')
chelsea_players.insert(9, 'Havertz (GOAL)')
print(f'42 mins: GOAL!!! HAVERTZ!!!. Man City 0-1 Chelsea {chelsea_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

print('45 mins: Half Time')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

print('2nd half begins.')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_players.remove('Rüdiger')
chelsea_players.insert(1, 'Rüdiger (Y)')
print(f'Yellow Card for Rüdiger (Chelsea) {chelsea_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

mancity_players = ['Ederson (GK)', 'Walker', 'Stones', 'Dias', 'Zinchenko', 'B.Silva', 'Gündogan', 'Foden', 'Mahrez', 'De Bruyne (C)', 'Sterling (C)']
mancity_players.remove('De Bruyne (C)')
mancity_players.insert(9, 'Jesus')
print(f'60 mins: Man City Substitution (Injury) < IN: Jesus  > OUT: De Bruyne {mancity_players}   Man City captain is now Sterling')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

mancity_players.remove('B.Silva')
mancity_players.insert(5, 'Fernandinho')
print(f'64 mins: Man City Substitution (Tactical) < IN: Fernandinho  > OUT: B.Silva {mancity_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_players.remove('Werner')
chelsea_players.insert(10, 'Pulisic')
print(f'66 mins: Chelsea Substitution (Tactical) < IN: Pulisic  > OUT: Werner {chelsea_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

mancity_players.remove('Sterling (C)')
mancity_players.insert(10, 'Agüero (C)')
print(f'77 mins: Man City Substitution (Tactical) < IN: Agüero  > OUT: Sterling {mancity_players}  Man City captain is now Agüero')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_players.remove('Mount')
chelsea_players.insert(8, 'Kovačić')
print(f'80 mins: Chelsea Substitution (Tactical) < IN: Kovačić  > OUT: Mount {chelsea_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

mancity_players.remove('Jesus')
mancity_players.insert(9, 'Jesus (Y)')
print(f'88 mins: Yellow Card for Jesus (Man City) {mancity_players}')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

print('Full Time  Man City 0-1 Chelsea')

print('--------------------------------------------------------------------------------------------------------------------------------------------')

chelsea_victory_message = ('CHELSEA', 'ARE', 'THE', 'CHAMPIONS', 'OF', 'EUROPE')
chelsea_victory_message_join = ' ** '.join(chelsea_victory_message)
print(chelsea_victory_message_join)

print('--------------------------------------------------------------------------------------------------------------------------------------------')

'''
        'E/M',  'W/R',  'S/T',  'D/A',  'Z/C',  'B/J',  'G/K',  'F/J',  'M/M',  'DB/H',  'S/W'
index     0       1       2       3       4       5       6       7       8       9       10
         -11     -10     -9      -8      -7      -6      -5      -4      -3      -2      -1
'''