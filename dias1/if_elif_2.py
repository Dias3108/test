'''
transport = input('Какой вид транспорта вы выберете: самолет,поезд,автобус,')

if transport == 'самолет':
    ticket_type == input('Каким классом вы хотите лететь: эконом , бизнес:')
    if ticket_type == 'эконом':
       place = input('Где вы хотите место: у окна,в проходе:')
    else:
       place = 'у вас свой зал'

elif transport == 'поезд':
       ticket_type = input('Как вы хотите ехать: плацкарт ,купе:')
    if ticket_type == 'купе':
       place = input('Выберите одно из свободных мест:5,13,8:')
    elif ticket_type == 'плацкарт':
       place = 'В плацкарте мест не осталось,жди следующий!'
	exit()
elif transport =='автобус':
      ticket_type == input('Как вы хотите ехать: стоя,сидя')
    if ticket_type == 'сидя'
      place = input('Выберите место:1,15,23:')
    else:
     place= 'Где угодно':
else:
    print('Такого вида транспорта нету!')
    exit()

print('ок,внесите оплату')
print('вы выбрали:'transport'ваше место',place)
'''

'''
fastfood =input('привет это шаурмечная,какое блюдо будете заказывать:шаурма,самса,пирожок:')


if fastfood == 'шаурма':
	doner = input('мясо или курица  ')
 	if doner == 'мясо':
		print('Вы заказали с мясом')
	elif doner == 'курица':
		print('Вы заказали с курицей')
elif fastfood == 'самса':
	doner = input('мясо или курица')
	if doner == 'мясо':
		print('Вы заказали с мясом')
	elif doner == 'курица':
		print('Вы заказали с курицей ')
'''
'''
fastfood = input('что вы хотите закзать: шаурма, самса, пирожок:')
if fastfood == 'шаурма':
	dobavki = input('какую начинку выберете: мясо, курица:')
	if dobavki == 'мясо':
		number = input('сколько хотите?:')
		temperature = input('нужно ли разогреть?:да,нет:')
		drink = input('что будете пить?чай,кофе,минералку:')
	elif dobavki == 'курица':
		number = input ('сколько хотите?:')
		temperature = input('Нужно ли разогреть?:да,нет:')
		drink = input('что будете пить?чай,кофе,минералку:')

elif fastfood == 'самса':
	dobavki = input('какую начинку выберете?: мясо,курица,сыр:')
	if dobavki == 'мясо':
		number = input('сколько хотите?:')
		temperature = input('Нужно ли разогреть?:да,нет:')
		drink = input('что будете пить?чай,кофе,минералку:')
	elif dobavki == 'курица':
		number = input('сколько хотите?:')
		temperature = input('Нужно ли разогреть?:да,нет:')
		drink = input('что будете пить?чай,кофе,минералку:')
	elif dobavki == 'сыр':
		waiting = input('самсы с сыром закончились, будут через 15 минут: будете ждать?: да, нет:')
		if waiting == 'да':
			number = input('сколько хотите?:')
			temperature = input('Нужно ли разогреть?:да,нет:')
			drink = input('что будете пить?чай,кофе,минералку:')
		elif waiting == 'нет':
			exit()
elif fastfood == 'пирожок':
	dobavki = input('какую начинку желаете?:капуста,картошка:')
	if dobavki == 'капуста':
		eror = input('Пирожки с капутой к сожалению закончились,будете с картошкой?:да,нет:')
		if eror == 'да':
			number = input('сколько хотите?:')
			temperature = input('Нужно ли разогреть?:да,нет:')
			drink = input('что будете пить?чай,кофе,минералку:')
		elif eror == 'нет':
			exit()
	elif dobavki == 'картошка':
		number = input('сколько хотите?:')
		temperature = input('Нужно ли разогреть?:да,нет:')
		drink = input('что будете пить?чай,кофе,минералку:')
	
else:
	print('ДРУЖИЩЕ ТАКОГО ТОВАРА У НАС НЕТУ!')
	exit()
print('вы заказали',{fastfood},{drink})

'''

transport = input('какой вид транспорта вы выбираете: самолет,поезд:')

if transport == 'самолет':
	ticket = input('Каким классом вы хотите лететь?: бизнес,эконом:')
	if ticket == 'эконом':
		place = input('ваше место в коридоре')
	else:
		plase = input('у вас свой зал')
elif transport == 'поезд':
	ticket = input('в каком вагоне вы хотите место?: первым, вторым:')
	if ticket == 'первым':
		plase = input('вы едете первым вагоном')
	else:
		place = input('вы едете вторым вагоном!')

