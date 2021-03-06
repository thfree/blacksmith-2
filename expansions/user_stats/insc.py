# coding: utf-8

if DefLANG in ("RU", "UA"):
	AnsBase_temp = tuple([line.decode("utf-8") for line in (
		"\nВсего входов - %d\nВремя последнего входа - %s\nПоследняя роль - %s", # 0
		"\nВремя последнего выхода - %s\nПричина выхода - %s", # 1
		"\nНики: %s", # 2
		"Нет статистики.", # 3
		"«%s» сидит здесь - %s.", # 4
		"Ты провёл здесь - %s.", # 5
		"Здесь нет такого юзера." # 6
	)])
else:
	AnsBase_temp = (
		"\nTotal joins - %d\nThe Last join-time - %s\nThe last role - %s", # 0
		"\nThe last leave-time - %s\nExit reason - %s", # 1
		"\nNicks: %s", # 2
		"No statistics.", # 3
		"'%s' spent here - %s.", # 4
		"You spent here - %s.", # 5
		"No such user here." # 6
	)