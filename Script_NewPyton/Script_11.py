ch=" salut tout le monde "
print(len(ch))
ch1=ch.strip()
print(ch1)
print(len(ch1))
#print(len(ch.strip())) comme ca on enleve les espaces
ch2=ch.lstrip()# rstrip() left ou right espace
print(ch2)
print(len(ch2))

ch4="***salut***tout***le***monde***"
print(ch4)
ch5=ch4.strip("*")
print(ch5)
print(len(ch5))
print(ch4.replace("*"," "))

ch6="SALUT TOUT le monde"
print(ch6.lower())# vse malenikimi bykvami
print(ch6.upper())# vse bolisimi bukvami
ch7="salut tout le mond mond mond"
print(ch7.count("mond"))# scitaet sckoliko raz
print(ch7.startswith("salut"))#boleen
print(ch7.endswith("mond"))#boleen
ch8="un-deux-qatre-cinq-six-sept-huit-neuf-dix"
print(ch8.split())# razdeliaet zapiatimi i kak v tableau



