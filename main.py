import random


kim = [' Najim ', ' Etik kiygan pishak ',' Jackuy ', ' Jackuy tentak ', ' Messi ', ' Ranaldo ', ' quyon ', ' qo\'y ', ' qo\'chqor ', ' Elon Musk ',  'Bill Geyts ', ' Steve Jobs ', ' Shoqosim ', ' Tulki ',
	' Bo\'ri ', ' Tesha ', ' Arslon ', ' O\'tkir ', ' G\'ishmat ', ' Toshmat ', ' Eshmat ', ' Oysha ', ' Robiya ', ' Ergashbiyi ', ' Alijon ',
	' Alla Pugachova ', ' Maradonna ', ' Zelenskiy ', ' Putin ', ' Donald Tramp ', ' Ip Man ', ' Jo Biden aka ', ' Jorj ', ' Zorro ', 
	' Despenser ', ' Brus Li ', ' Sardor ', ' Amir ', ' eshshak ', ' Tim ']



qachon = [' kecha ', ' o\'tgan kuni ', ' bir oy oldin ', ' bir hafta oldin ', ' o\'tgan yili ', ' 2 yil oldin ', ' 3 yil oldin ',
	' Qadim-qadim zamonda ', ' 4 yil oldin ', ' 5 yil oldin ', ' 10 yil oldin ', ' bir kuni ', ' Qadim-qadim zamonda ',
	' 2-3 kun oldin ', ' 5 kun oldin ', ' bir kuni ', ' 50 yil oldin ', ' tosh asrida ', ' Pandimiya paytida ']



qayerdan = [' uyidan ', ' bobosinikidan ', ' buvisinikidan ', ' onasini uyidan ', ' Susambildan ', ' otasini uyidan ',
	' molxonadan ', ' qo\'yxonadan ', ' qassobxonadan ', ' magazindan ', ' qishloqdan ', ' Toshkentdan ', ' Buxorodan ', ' Navoidan ',
	' Samarqandan ', ' Namangandan ', ' Jizaxdan ', ' Xorazmdan ', ' Qoraqalpoqdan ', ' Qashqadaryodan ', ' Surxandaryodan ',
	' Andijondan ', ' Farg\'onadan ', ' Tojikistondan ', ' Turkiyadan ', ' Rassiyadan ', ' Amerikadan ', ' Angliyadan ', 
	' Afrikadan ', ' Texasdan ']



qayerga = [' bobosinikiga ', ' buvisinikiga ', ' onasini uyiga ', ' Susambilga ', ' otasini uyiga ',
	' molxonaga ', ' qo\'yxonaga ', ' qassobxonaga ' ' magazinga ', ' qishloqga ', ' Toshkentga ', ' Buxoroga ', ' Navoiga ',
	' Samarqanga ', ' Namanganga ', ' Jizaxga ', ' Xorazmga ', ' Qoraqalpoqga ', ' Qashqadaryoga ', ' Surxandaryoga ',
	' Andijonga ', ' Farg\'onaga ', ' Tojikistonga ', ' Turkiyaga ', ' Rassiyaga ', ' Amerikaga ', ' Angliyaga ', 
	' Afrikaga ', ' maktabga ', ' institutga ', ' Unversitetga ', ' Texasga ', ' kutubxonaga ']



nm_qlshga = [' Ishlashga ', ' dam olishga ', ' sayohatga ', ' zerikkani uchun ', ' o\'qishga ', ' aylanishga ', ' urushga ',
	' talpa bo\'lgani uchun ', ' pul topishga ', ' bozorlik qilishga ', ' kitob o\'qishga ', ' o\'ynashga ', ' Alifbe bayramga ',
	' ovqatlanishga borib ', ' ov qilishga ', ' baliq tutishga ', ' karra jadvalni yodlab ', ' yo\'lga ustozini ko\'rib ',
	' xazina topishga ']



boglovchi = [' keyin ', ' indan keyin ', ' va ']



nm_qldi = [' yiqilib tushibdi ', ' urush qilibdi ', ' latifa eshitib kulib-kulib o\'lib qolibdi ', ' nima qilishni bilmay qarab o\'tiribdi ',
	' nima qilishni bilmay yig\'lab yuboribdi', ' hojatxona kirib qaytib kelibdi ', ' maqtangandan keyin uni o\'ldirib qo\'yibdilar ',
	' kitob yozibdi ', ' pubg o\'ynabdi ', ' minecraft o\'ynibadi ', ' farrosh bo\'ibldi ', ' kitob yozibdi ', ' Burger yeb qaytib kelibdi ',
	' mashxur bo\'lib ketpdi ', ' boyib ketipti ']

chiqipti = [' chiqiptiyu ', ', ', ', ', ', ', ', ', ', ', ', ', ', ', ', ', ' yugurib	 ']

tinish = ['.', '!']

f = open("logger.txt", "a")

latifa = random.choice(qachon) + random.choice(kim) + random.choice(qayerdan) + random.choice(chiqipti) + random.choice(qayerga) + random.choice(nm_qlshga) + ' boribdi, ' + random.choice(boglovchi) + random.choice(nm_qldi) + random.choice(tinish)

f.write(latifa + "\n\n")
f.close()

print(latifa)