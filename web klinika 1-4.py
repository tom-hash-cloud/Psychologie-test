import streamlit as st
import random

# Tady jsou všechna tvá data z dokumentu
if 'questions' not in st.session_state:
    st.session_state.questions = {
        "ADHD": [
            ["Při diagnostice ADHD u dítěte psycholog pravděpodobně hledá:", ["charakteristické vzorce chování.", "metabolity v krvi.", "abnormality v čelním laloku mozku.", "násilné chování ze strany rodičů."], 0], # [cite: 1136]
        ["Děti s ADHD obecně:", ["mají potěšení z pocitu, že se vymykají kontrole.", "chtějí dosahovat dobrých výsledků, ale kvůli omezené sebekontrole mají potíže.", "se mohou chovat přiměřeně, pokud vynaloží dostatečné úsilí.", "lépe prospívají s jasnými pravidly."], 1], # [cite: 1141]
        ["Teorie poškození mozku u ADHD (40.-50. léta) byla zavržena, protože:", ["RTG nenašel důkazy.", "v roce 1958 byla identifikována psychologická příčina.", "vysvětluje jen velmi malý počet případů.", "poškození se pojilo s retardací."], 2], # [cite: 1146]
        ["Které tvrzení o ADHD je NEPRAVDIVÉ?", ["Nebyla zjištěna jediná příčina.", "ADHD je souhrnný pojem pro mírně se lišící vzorce chování.", "Hyperaktivita a nepozornost jsou základní znaky.", "Neexistují příznaky zjistitelné RTG nebo laboratoří."], 2], # [cite: 1151]
        ["Virginia Douglasová tvrdila, že:", ["hyperaktivita je primární složkou ADHD.", "kromě hyperaktivity jsou hlavními příznaky také nepozornost a nedostatky v kontrole impulzů.", "ADHD je způsobena minimálním poškozením mozku.", "ADHD je spíše psychologického původu."], 1], # [cite: 1156]
        ["V současnosti jsou za hlavní poruchy u ADHD považovány:", ["nepozornost a obtíže s regulací motorického chování.", "potíže s inhibicí chování a slabá seberegulace.", "nepozornost a špatná morální kontrola.", "hyperaktivita a kognitivní problémy."], 1], # [cite: 1161]
        ["Radek si nedokáže zapamatovat telefonní číslo bez zapsání. Má deficit v:", ["impulzivitě.", "udržení pozornosti.", "selektivní pozornosti.", "kapacity pozornosti."], 3], # [cite: 1166]
        ["Markétu při učení rozptýlí televize v jiné místnosti. Jde o deficit:", ["kontroly pozornosti.", "udržení pozornosti.", "selektivní pozornosti.", "kapacity pozornosti."], 2], # [cite: 1171]
        ["Tomáš má problémy s pozorností, když je unavený nebo ho úkol nezajímá. Má nedostatek v:", ["udržení pozornosti.", "rozptýlenosti.", "selektivní pozornosti.", "kapacity pozornosti."], 0], # [cite: 1177]
        ["Jiným označením deficitu selektivní pozornosti je:", ["rozptýlenost", "impulzivita", "duální pozornost", "dezorganizace"], 0], # [cite: 1183]
        ["Hlavní příčinou deficitu pozornosti u ADHD je:", ["selektivní pozornost.", "kapacita pozornosti.", "udržení pozornosti / bdělosti.", "rozptýlenost."], 2], # [cite: 1188]
        ["Který úkol může být pro dítě s ADHD nejobtížnější?", ["nová videohra", "pozor na učitele, když někdo jiný mluví", "zapamatování čísla", "45 minut práce na jednoduchých úlohách"], 3], # [cite: 1193]
        ["Kdy vykazuje dítě s ADHD pravděpodobně více pohybu?", ["když má v klidu sedět u stolu", "ve spánku", "při hře na hřišti", "ve všech situacích"], 0], # [cite: 1198]
        ["Příkladem kognitivní impulzivity je:", ["vyhrknutí odpovědi", "dotýkání se plotny", "překotné myšlení", "přerušení rodiče při volání"], 2], # [cite: 1203]
        ["Riziko problémů s chováním mají děti vykazující:", ["behaviorální impulzivitu.", "kognitivní impulzivitu.", "selektivní nepozornost.", "sníženou schopnost pozornosti."], 0], # [cite: 1208]
        ["Riziko v akademickém výkonu mají děti vykazující:", ["behaviorální impulzivitu.", "kognitivní impulzivitu.", "selektivní nepozornost.", "kombinaci behaviorální a kognitivní impulzivity."], 3], # [cite: 1213]
        ["Dalším kritériem pro diagnózu ADHD je:", ["příznaky před 12. rokem věku", "přítomnost aspoň rok", "výskyt aspoň v jednom prostředí", "významné narušení sociálního nebo školního fungování"], 3], # [cite: 1218]
        ["Které z následujících NENÍ kritériem pro diagnózu ADHD?", ["příznaky před 12. rokem věku", "přítomnost nejméně 6 měsíců", "výskyt ve více než jednom prostředí", "významné poruchy sociálního nebo školního fungování"], 0], # [cite: 1223]
        ["Děti s ADHD-PI mají ve srovnání s ADHD-HI vyšší riziko:", ["antisociálního chování.", "odmítání vrstevníky.", "úzkostných poruch a poruch nálady.", "speciálního vzdělávání."], 2], # [cite: 1228]
        ["Které tvrzení o ADHD-HI NENÍ pravdivé?", ["jsou často starší než děti s ADHD-C", "je to nejvzácnější podtyp", "častěji vykazují poruchy chování", "jsou častěji vyloučovány ze školy"], 0], # [cite: 1233]
        ["Které tvrzení o ADHD-PI NENÍ pravdivé?", ["jsou popisovány jako zasněné", "mají potíže s rychlostí zpracování", "jsou často popisovány jako agresivní a hrubé", "mohou mít zcela odlišnou poruchu"], 2], # [cite: 1238]
        ["Které tvrzení NENÍ kritikou kritérií DSM-V pro ADHD?", ["počet příznaků není přizpůsoben věku", "požadavek 6 měsíců může být pro děti příliš dlouhý", "DSM pojímá ADHD kategoriálně", "věk nástupu 7 let může být příliš nízký"], 1], # [cite: 1243]
        ["Mentální procesy k regulaci chování se nazývají:", ["exekutivní funkce.", "metakognice.", "sebepojetí.", "sledování myšlenek."], 0], # [cite: 1248]
        ["Které tvrzení nejlépe vystihuje inteligenci dětí s ADHD?", ["50 % má podprůměrnou inteligenci", "50 % má nadprůměrnou inteligenci", "inteligentnější děti vykazují více impulzivity", "většina dětí s ADHD má průměrnou inteligenci."], 3], # [cite: 1253]
        ["Které dítě spíše vykáže pozitivní iluzorní zkreslení?", ["dítě s ADHD-HI a poruchami chování", "dítě s ADHD-HI a depresí", "dítě s ADHD-PI a úzkostí", "dítě s ADHD-PI a poruchami chování"], 0], # [cite: 1258]
        ["Který znak NENÍ rysem řeči dítěte s ADHD?", ["tichá, mumlavá řeč", "časté změny tématu", "méně zájmen a spojek", "nejasné návaznosti"], 0], # [cite: 1263]
        ["Které tvrzení o zdraví dětí s ADHD je NEPRAVDIVÉ?", ["často trpí poruchami spánku", "mohou vykazovat mírné poruchy růstu kvůli lékům", "vyšší výskyt tiků", "náchylnější k úrazům"], 1], # [cite: 1268]
        ["Matky dětí s ADHD mají vyšší pravděpodobnost výskytu:", ["problémů se zneužíváním látek.", "schizofrenie.", "deprese.", "disociální poruchy osobnosti."], 2], # [cite: 1273]
        ["Které tvrzení o dětech s ADHD je pravdivé?", ["deficit v sociálním uvažování", "stejná sociální agenda jako vrstevníci", "vysoká sociální podpora od vrstevníků", "jsou trvale odmítány vrstevníky"], 3], # [cite: 1278]
        ["Děti s ADHD vykazují:", ["sníženou touhu po vztazích", "špatné porozumění sociálním vztahům", "silnou schopnost rozpoznávat emoce", "malou vzájemnost ve vztazích s vrstevníky"], 3], # [cite: 1283]
        ["Nejčastějšími komorbidními poruchami u ADHD jsou:", ["úzkost a deprese.", "opoziční vzdor a deprese.", "tikové poruchy.", "porucha chování a opoziční vzdor."], 3], # [cite: 1288]
        ["Které tvrzení o dětech s ADHD a úzkostmi je pravdivé?", ["často adolescenti", "často podtyp ADHD-HI", "často podtyp ADHD-PI", "tvoří 50 % klinicky odesílaných dětí"], 2], # [cite: 1293]
        ["Vztah mezi ADHD a depresí se zdá být funkcí:", ["demoralizace v důsledku příznaků.", "rodinného rizika.", "rodinného stresu.", "všech uvedených faktorů"], 1], # [cite: 1298]
        ["Nejlepší odhad prevalence ADHD u školních dětí je:", ["1-2 %", "3-5 %", "9-10 %", "15-20 %"], 1], # [cite: 1303]
        ["Vyšší výskyt ADHD u chlapců je nejspíše způsoben:", ["výběrovým zkreslením.", "společenským očekáváním.", "vyšší mírou agrese.", "všemi uvedenými faktory"], 3], # [cite: 1308]
        ["Ve srovnání s chlapci vykazují dívky s ADHD častěji:", ["vyšší úroveň hyperaktivity.", "větší postižení exekutivních funkcí.", "vyšší úroveň agrese.", "příznaky nepozornosti / dezorganizace."], 3], # [cite: 1313]
        ["Dívky s ADHD mají proti dívkám bez ADHD vyšší pravděpodobnost:", ["poruch chování, nálady a úzkostí.", "nižší míry verbální agrese.", "vyšší IQ.", "neplatí nic z uvedeného"], 0], # [cite: 1318]
        ["Vyšší výskyt ADHD v nízkých soc-ek. skupinách vysvětluje:", ["přítomnost deprese.", "psychopatologie u rodičů.", "souběžné poruchy chování.", "souběžné poruchy učení."], 2], # [cite: 1323]
        ["Které tvrzení o ADHD a kultuře NENÍ pravdivé?", ["častější ve vyšších soc-ek. skupinách", "zaznamenáno ve všech zemích", "odráží kulturní normy", "souvisí s rozdíly v definici"], 0], # [cite: 1328]
        ["Matky dětí s ADHD popisují své děti v kojeneckém věku jako:", ["obtížné", "snadné", "nerozeznatelné", "úzkostné"], 0], # [cite: 1333]
        ["Pokud jde o nástup příznaků ADHD:", ["příznaky se objevují ve stejnou dobu (předškolní věk)", "příznaky se objevují ve stejnou dobu (začátek školy)", "nepozornost dříve než hyperaktivita", "hyperaktivita-impulzivita obvykle dříve než nepozornost."], 3], # [cite: 1338]
        ["Které tvrzení o průběhu ADHD je pravdivé?", ["nerozvíjí se před školou", "většina před dospíváním překoná", "mnoho dospělých nebylo v dětství diagnostikováno", "všechna uvedená tvrzení"], 2], # [cite: 1343]
        ["Dospělí s ADHD mají šanci na lepší životní výsledky, pokud:", ["jsou příznaky méně závažné.", "mají podporu rodiny.", "mají přístup k pomoci.", "platí vše výše uvedené"], 3], # [cite: 1348]
        ["Která z možností nejpravděpodobněji způsobuje ADHD?", ["příliš mnoho cukru", "zářivkové osvětlení", "špatné školní prostředí", "žádná z uvedených možností není správná"], 3], # [cite: 1353]
        ["Děti s ADHD vykazují:", ["deficity motivace.", "deficity v úrovni aktivace.", "deficity v seberegulaci.", "všechny výše uvedené projevy"], 3], # [cite: 1358]
        ["Výzkum ukazuje, že ADHD je porucha s determinantami převážně:", ["biologickými", "neurobiologickými", "socio-environmentálními", "rodinnými"], 1], # [cite: 1363]
        ["Studie na dvojčatech naznačují, že největší roli hraje:", ["sdílené prostředí", "nesdílené prostředí", "dědičnost", "všechny faktory stejně"], 2], # [cite: 1368]
        ["Gen dopaminového receptoru DRD4 je spojován s:", ["vyhledáváním vzrušení.", "popudlivým chováním.", "impulzivitou.", "všemi výše uvedenými faktory"], 3], # [cite: 1373]
        ["Drobné tělesné anomálie a rizika u porodu jsou faktory pro:", ["ADHD (nikoli jiné)", "mnoho forem psychopatologie.", "pouze ADHD a poruchy chování.", "pouze úzkost a depresi."], 1], # [cite: 1378]
        ["Neurobiologický výzkum příčin ADHD podporuje zapojení:", ["limbického systému.", "hipokampu.", "retikulárního systému.", "frontostriatálních okruhů."], 3], # [cite: 1383]
        ["Ve studii Hoovera & Miliche (1994) matky věřící, že dítě požilo cukr:", ["byly milejší.", "byly klidnější.", "byly kritičtější a hodnotily je jako více hyperaktivní.", "nezaznamenaly změnu."], 2], # [cite: 1388]
        ["Výzkum vlivu rodiny na ADHD naznačuje, že:", ["rodinné faktory vysvětlují velkou část.", "vysvětlují pouze malou část.", "mohou zvyšovat závažnost symptomů.", "vysvětlují malou část, ale mohou zvýšit závažnost."], 3], # [cite: 1393]
        ["Nejlepší léčbou ADHD je:", ["stimulační léky.", "trénink rodičů.", "vzdělávací intervence.", "kombinace všech uvedených přístupů"], 3], # [cite: 1398]
        ["Stimulační léky fungují tak, že:", ["paradoxně zpomalují.", "mění aktivitu neurotransmiterů ve frontostriatálních oblastech.", "zlepšují náladu.", "působí jako placebo."], 1], # [cite: 1403]
        ["Vzdělávací intervence u ADHD zahrnuje:", ["token economy ve třídě.", "vizuální pomůcky.", "písemné i ústní instrukce.", "všechny výše uvedené možnosti"], 3], # [cite: 1408]
        ["Výsledky studie MTA ukázaly, že:", ["behaviorální léčba účinnější.", "přidání beh. léčby k medikaci přineslo větší zlepšení.", "přínos jen u farmakologické léčby.", "žádná z uvedených možností není správná"], 2] # [cite: 1413]
    ],
        "ÚZKOSTNÉ PORUCHY": [
            ["Která z následujících možností NEPLATÍ pro úzkostné poruchy?", ["U dětí jsou vzácné.", "Existuje několik typů.", "Mohou přetrvávat celý život.", "Často se vyskytují s jinými poruchami."], 0], # [cite: 1419]
        ["_______ mobilizuje tělo k akci v situaci boj/útěk:", ["CNS", "PNS", "Sympatický nervový systém", "Parasympatický nervový systém"], 2], # [cite: 1424]
        ["Při aktivaci sympatiku dochází k uvolnění:", ["inzulínu", "adrenalinu", "růstového hormonu", "testosteronu"], 1], # [cite: 1429]
        ["_______ je okamžitá poplachová reakce na aktuální nebezpečí:", ["Úzkost", "Panika", "Strach", "Obavy"], 2], # [cite: 1434]
        ["_______ se vyznačuje pocity strachu a nedostatku kontroly nad událostmi:", ["Úzkost", "Panika", "Strach", "Obavy"], 0], # [cite: 1439]
        ["_______ jsou tělesné příznaky boj/útěk bez zjevné hrozby:", ["Úzkost", "Panika", "Strach", "Obavy"], 1], # [cite: 1444]
        ["Strach _______ se zvyšuje s věkem:", ["ze sociálních situací", "ze školy", "z tmy", "z odloučení"], 0], # [cite: 1449]
        ["Strach ze smrti je běžný u dětí ve věku:", ["1-2 let.", "3-5 let.", "6-8 let.", "9-12 let."], 3], # [cite: 1454]
        ["Strach z odloučení od rodičů je běžný u dětí ve věku:", ["1-2 let.", "3-4 let.", "5-6 let.", "všechny věkové skupiny"], 3], # [cite: 1459]
        ["Děti s úzkostmi mají intenzivnější obavy z/ze:", ["školních úloh.", "bolístek.", "sportovních výsledků.", "cizích lidí."], 3], # [cite: 1464]
        ["Rituální chování je u malých dětí _______:", ["nepřítomné", "neobvyklé", "běžné", "obtížně pozorovatelné"], 2], # [cite: 1469]
        ["MKN-10 dělí úzkostné poruchy podle:", ["dimenzí", "druhy reakcí a vyhýbání se", "odpovědi na léčbu", "typického věku nástupu."], 1], # [cite: 1474]
        ["Kdy absence separační úzkosti naznačuje nejistou vazbu?", ["2 měsíce", "12 měsíců", "10 let", "nikdy"], 1], # [cite: 1479]
        ["Nejčastější úzkostnou poruchou v dětství je:", ["OCD", "panika", "GAD", "separační úzkostná porucha."], 3], # [cite: 1484]
        ["Porucha s nejčasnějším věkem nástupu je:", ["OCD", "panika", "GAD", "separační úzkostná porucha."], 3], # [cite: 1489]
        ["Průměrný věk nástupu separační úzkosti je:", ["2-3 roky", "4-6 let", "7-8 let", "9-10 let"], 2], # [cite: 1494]
        ["Co NENÍ u separační úzkosti běžné?", ["jiná úzkost", "deprese", "porucha chování", "odmítání školy"], 2], # [cite: 1499]
        ["Co vede nejméně pravděpodobně k odmítání školy?", ["potíže s učením", "separační úzkost", "strach z posměchu", "strach z hodnocení"], 0], # [cite: 1504]
        ["Která diagnóza NEPATŘÍ do MKN-10?", ["SAD", "OCD", "panika", "testová úzkost"], 3], # [cite: 1509]
        ["Které tvrzení o testové úzkosti je NEPRAVDIVÉ?", ["obavy z hodnocení", "může být specifická fobie", "často komorbidní s GAD", "všechny jsou pravdivé"], 3], # [cite: 1514]
        ["Přehnané obavy při absenci podmínek jsou:", ["tenze", "obavné očekávání.", "strach", "panika"], 1], # [cite: 1519]
        ["Děti s GAD se od ostatních liší tím, že:", ["obavy jsou mimo věk", "somatické příznaky", "starosti kvůli drobnostem", "starosti o drobnosti + somatika"], 2], # [cite: 1524]
        ["Pro diagnózu GAD se musí projevovat:", ["SAD", "obavy o výsledky", "aspoň jeden somatický příznak.", "perfekcionismus"], 2], # [cite: 1529]
        ["Prevalence GAD u dětí je:", ["1-2 %", "2-4 %", "3-6 %", "6-8 %"], 2], # [cite: 1534]
        ["Děti se specifickou fobií na rozdíl od dospělých:", ["se vyhýbají podnětům", "nerozpoznají, že jsou obavy extrémní.", "pociťují vzrušení", "jsou snadněji léčitelné"], 1], # [cite: 1539]
        ["Strach ze zvířat u dětí je nejpravděpodobněji způsoben:", ["expozicí", "evolučními procesy.", "ochranou rodičů", "všemi faktory"], 1], # [cite: 1544]
        ["Situační specifická fobie je strach z:", ["výšek", "výtahů.", "nemocí", "injekcí"], 1], # [cite: 1549]
        ["______ je nejčastější sekundární diagnózou u úzkostných poruch:", ["Specifická fobie", "Sociální fobie", "OCD", "Generalizovaná úzkostná porucha"], 1], # [cite: 1554]
        ["Sociální fobie se poprvé objevuje v:", ["školce", "mladším školním věku", "prepubertě", "pubertě a dospívání."], 3], # [cite: 1559]
        ["Selektivní mutismus je považován za typ:", ["specifické fobie", "GAD", "OCD", "sociální fobie."], 3], # [cite: 1564]
        ["Děti se selektivním mutismem mohou také mít:", ["zpožděný vývoj", "poruchy řeči", "poruchy sluchu", "vše výše uvedené"], 3], # [cite: 1569]
        ["U posedlosti čistotou je pravděpodobné nutkání:", ["mytí rukou.", "vyhýbat se prasklinám", "myslet na špínu", "dotýkat se špíny"], 0], # [cite: 1574]
        ["Nutkání počítat souvisí s obavou z/ze:", ["symetrie nebo řádu.", "poškození", "kontaminace", "náboženství"], 1], # [cite: 1579]
        ["Jaký je účel kompulzí?", ["spotřebovat čas", "nemyslet na jiné věci", "snížit úzkost.", "žádný"], 2], # [cite: 1584]
        ["Výskyt OCD u dětí je vůči dospělým:", ["menší", "větší", "je roven.", "variabilní"], 2], # [cite: 1589]
        ["_______ vlivy hrají roli u časných případů OCD:", ["Rodičovské", "Skupinové", "Neurobiologické", "Genetické"], 3], # [cite: 1594]
        ["Co NENÍ znakem záchvatu paniky?", ["strach", "trvá několik dní.", "pocit nebezpečí", "opakuje se"], 1], # [cite: 1600]
        ["Spontánní záchvaty paniky souvisí s:", ["věkem", "pubertální fází.", "kognicí", "řečí"], 1], # [cite: 1605]
        ["Agorafobie je strach z:", ["opuštění domova", "odloučení", "záchvatu paniky, kde je únik těžký.", "pavouků"], 2], # [cite: 1610]
        ["Záchvaty paniky se u dospívajících vyskytují u:", ["3-4 %", "8-10 %", "15-20 %", "25-30 %"], 0], # [cite: 1615]
        ["Které děti mají nejnižší míru remise?", ["SAD", "GAD", "OCD", "panická porucha"], 3], # [cite: 1620]
        ["Co NENÍ rysem PTSD?", ["prožívání traumatu", "podrážděnost a agitovanost.", "vyhýbání se", "vzrušení"], 1], # [cite: 1625]
        ["Děti s akutní stresovou poruchou se oproti PTSD:", ["rychleji zotavují.", "mají slabší stresory", "mají problémy s chováním", "mají méně podpory"], 0], # [cite: 1630]
        ["Nejméně pravděpodobná je deprese u:", ["sociální fobie", "specifické fobie.", "GAD", "SAD"], 1], # [cite: 1635]
        ["Ve většině případů:", ["úzkost předchází depresi.", "deprese dříve", "současně", "není vztah"], 0], # [cite: 1640]
        ["Oproti úzkostným mají depresivní děti:", ["více neg. afektivity", "méně neg. afektivity", "více poz. afektivity", "méně pozitivní afektivity."], 3], # [cite: 1645]
        ["U žen jsou úzkosti vůči mužům:", ["dvakrát častěji.", "méně často", "mírně více", "stejně"], 0], # [cite: 1650]
        ["Dětská psychopatologie odráží kombinaci skutečné/skutečného _______ dítěte a _______, skrze které se na něj dívají ostatní v kultuře dítěte.", ["symptomu, struktury", "poruchy, zaměření", "chování, perspektivy", "chování, behaviorální rámce"], 3], # [cite: 1655]
        ["Dvoufaktorová teorie vysvětluje úzkost kombinací:", ["vazby a učení", "temperamentu a expozice", "klasického a operantního podmiňování.", "modelování"], 2], # [cite: 1660]
        ["Plaché děti mají menší šanci na úzkost, pokud:", ["je rodiče chrání", "rodiče dají pevné hranice pro stres.", "mají sourozence", "rodiče je ignorují"], 1], # [cite: 1665]
        ["Genetický podíl úzkosti s věkem:", ["klesá", "je větší u kluků", "stoupá a je větší u dívek.", "je stejný"], 2], # [cite: 1670]
        ["Mozkový systém spojený s úzkostí je:", ["aktivační", "inhibiční.", "formační", "hypotalamický"], 1], # [cite: 1675]
        ["Neurotransmiter nejčastěji v úzkostech je:", ["dopamin", "noradrenalin", "GABA.", "prominergní"], 2], # [cite: 1680]
        ["Neurotoxické účinky může mít rané vystavení:", ["kortizolu.", "serotoninu", "GABA", "norepinefrinu"], 0], # [cite: 1685]
        ["Úzkost souvisí s:", ["výchovou", "vazbou", "rodinou", "vším uvedeným"], 3], # [cite: 1690]
        ["Rodičovský styl u úzkostí je nejčastěji:", ["neangažovaný", "příliš kontrolující.", "tolerantní", "pozitivní"], 1], # [cite: 1695]
        ["Behaviorální terapie úzkosti používá:", ["kognici", "rodinu", "léky", "prezentaci obavného podnětu."], 3], # [cite: 1700]
        ["Léčba fobie z jízdy autem zahrnuje:", ["hraní s autíčky", "sledování videí", "představy", "skutečnou jízdu."], 3], # [cite: 1705]
        ["Nejúčinnější léčba většiny úzkostí je:", ["behaviorální", "kognitivně-behaviorální.", "rodinná", "léky"], 1], # [cite: 1710]
        ["Nejsilnější důkazy léků u dětí jsou u:", ["GAD", "paniky", "OCD.", "sociální fobie"], 2] # [cite: 1715]
    ],
        "AUTISMUS": [
            ["Leo Kanner považoval za rysy autismu:", ["absenci řeči", "monotónnost", "stereotypy", "absenci sociálních interakcí."], 3], # [cite: 1721]
        ["Rané teorie připisovaly autismus:", ["biologii", "smyslům", "přání rodičů, aby se dítě nenarodilo.", "prostředí"], 2], # [cite: 1726]
        ["Pro diagnózu MKN-10 musí být příznaky patrné před věkem:", ["1 rok", "3 let.", "5 let", "7 let"], 1], # [cite: 1731]
        ["Které tvrzení o autismu je pravdivé?", ["vývojová porucha", "patří do PAS", "závažná porucha", "všechna uvedená."], 3], # [cite: 1736]
        ["Které tvrzení o sociálních dovednostech dětí s PAS je pravdivé?", ["potíže i při průměrné/nadprůměrné inteligenci.", "potíže jen u podprůměru", "potíže jen s MR", "potíže jen bez řeči"], 0], # [cite: 1741]
        ["Děti s _______ mají potíže s rozpoznáváním výrazů obličeje:", ["depresí", "autismem.", "ADHD", "úzkostí"], 1], # [cite: 1746]
        ["Sdílená sociální pozornost je schopnost:", ["mluvit se dvěma", "koordinovat pozornost na osobu a objekt.", "dvě témata", "sledovat cizí rozhovor"], 1], # [cite: 1751]
        ["Většina dětí s autismem:", ["nemá vazbu k rodičům", "náhodné vazby", "vztah jen s rodiči", "preferuje pečovatele před cizími."], 3], # [cite: 1756]
        ["O emocích u dětí s PAS nevíme, zda je odlišně:", ["prožívají", "zpracovávají", "vyjadřují", "vše uvedené."], 0], # [cite: 1761]
        ["Protodeklarativní gesta vyžadují:", ["řeč", "teorii mysli + řeč", "teorii mysli + sdílenou pozornost.", "inteligenci"], 2], # [cite: 1766]
        ["U kolika dětí s PAS se nevyvíjí funkční jazyk?", ["všech", "většiny", "přibližně poloviny.", "malého počtu"], 2], # [cite: 1771]
        ["Děti s PAS nejčastěji používají:", ["instrumentální gesta.", "expresivní", "protodeklarativní", "sdílené"], 0], # [cite: 1776]
        ["Echolálie jsou pravděpodobně:", ["patologie", "OCD", "krok v osvojování jazyka.", "návyk"], 2], # [cite: 1781]
        ["Primární jazykový deficit u PAS se týká:", ["gramatiky", "sémantiky", "morfologie", "pragmatiky."], 3], # [cite: 1786]
        ["Inteligenční testy (WISC) mohou PAS děti:", ["podhodnocovat.", "nadhodnocovat", "dávat stereotyp", "odrážet přesně"], 0], # [cite: 1791]
        ["Autostimulace může být způsobena:", ["touhou po stimulaci", "příliš podnětným prostředím", "posílením", "vším uvedeným."], 3], # [cite: 1796]
        ["Schopnosti přesahující běžný intelekt se nazývají:", ["savantské.", "ostrůvkovité", "makroschopnosti", "nadpřirozené"], 1], # [cite: 1801]
        ["Zaměření jen na jeden rys objektu je stimulová:", ["dominance", "specializace", "screening", "nadselektivita."], 3], # [cite: 1806]
        ["Upřednostňování vjemů před jinými je senzorická:", ["dominance.", "specializace", "screening", "nadselektivita"], 0], # [cite: 1811]
        ["Teorie mysli předpokládá, že děti s PAS:", ["ignorují rysy", "nerozumí duševním stavům druhých.", "detailismus", "nedělí pozornost"], 1], # [cite: 1816]
        ["Osoba bez centrální koherence:", ["vnímá po částech, ne celek.", "nerozumí stavům", "nekoordinuje tělo", "nechápe hierarchii"], 0], # [cite: 1821]
        ["Ve WISC by PAS dělalo nejvíc potíží:", ["opakování čísel", "kostky", "porozumění.", "vše stejné"], 2], # [cite: 1826]
        ["Děti s PAS trpí problémy s:", ["spánkem", "gastrointestinem", "stravou", "vším uvedeným."], 3], # [cite: 1831]
        ["Nejcharakterističtější kognitivní deficit u PAS je:", ["centrální koherence", "exekutivní funkce", "nedostatečná teorie mysli.", "nadselektivita"], 2], # [cite: 1836]
        ["Děti s PAS mají často současně:", ["MR a epilepsii.", "nadprůměrné IQ", "schizofrenii", "MR a schizofrenii"], 0], # [cite: 1841]
        ["Nástup epilepsie u PAS je nejspíše v:", ["kojeneckém věku", "škole", "adolescenci.", "dospělosti"], 2], # [cite: 1846]
        ["Co odlišuje některé PAS děti od MR?", ["uši", "zvětšený obvod hlavy.", "nos", "oči"], 1], # [cite: 1851]
        ["Dítě s MR (bez PAS) má oproti PAS spíše:", ["sebepoškozování", "oční kontakt a úsměv.", "stereotypy", "autostimulaci"], 1], # [cite: 1856]
        ["Děti s jazykovou poruchou mají proti PAS méně potíží v:", ["osvojování jazyka", "délce hovoru", "sociální konverzaci.", "gramatice"], 2], # [cite: 1861]
        ["Nejnovější prevalence PAS je asi:", ["1 z 1000", "1 z 500", "1 z 250", "1 ze 150."], 3], # [cite: 1866]
        ["Nárůst prevalence PAS je způsoben:", ["kritérii", "rozpoznáváním mírných forem", "screeningem", "vším uvedeným."], 3], # [cite: 1871]
        ["Genderové rozdíly u PAS:", ["stejně", "častější u chlapců", "chlapci (u těžké MR vyrovnanější).", "chlapci (u vysokého IQ podobný)"], 2], # [cite: 1876]
        ["Extrémní mužský mozek předpokládal, že PAS mozky jsou více:", ["systematizující.", "méně systematizující", "ženy jsou více syst.", "muži empatičtí"], 0], # [cite: 1881]
        ["Deficity PAS se projevují kolem:", ["narození", "6 měsíců", "2. roku.", "školy"], 2], # [cite: 1886]
        ["Dva prediktory úspěchu dospělých s PAS jsou:", ["stereotypy", "IQ a jazyk.", "rodiče a intervence", "motorika"], 1], # [cite: 1891]
        ["AAP doporučuje screening PAS ve věku:", ["12 m", "15 m", "12 a 24 m", "18 a 24 měsíců."], 3], # [cite: 1896]
        ["S PAS je nejčastěji spojena:", ["tuberózní skleróza.", "Down", "PKU", "fragilní X"], 0], # [cite: 1901]
        ["Příbuzní dětí s PAS mají vyšší výskyt:", ["echolálií", "MR", "pragmatických jazykových obtíží.", "všeho uvedeného"], 2], # [cite: 1906]
        ["Kolik % rodičů věří, že PAS způsobilo očkování?", ["10 %", "25 %.", "50 %", "75 %"], 2], # [cite: 1911]
        ["Nejčastější neurotransmiter v PAS je:", ["serotonin.", "dopamin", "noradrenalin", "GABA"], 0], # [cite: 1916]
        ["Dr. Lovaas vyvinul:", ["TEACCH", "Floor Time", "ABA.", "PRT"], 2], # [cite: 1921]
        ["Metoda vyžadování specifických odpovědí je trénink:", ["jemných pokusů", "odpovědí", "podnět-reakce", "diskrétních pokusů."], 3], # [cite: 1926]
        ["Posilování chování přes přirozené příležitosti je trénink:", ["naturalistický", "diskrétní", "náhodný", "klíčových reakcí."], 2], # [cite: 1931]
        ["Včasná intervence u PAS těží z:", ["rodičů", "absence chování", "ochoty se zavděčit", "plasticity."], 3], # [cite: 1936]
        ["UCLA Young Autism Project používá:", ["napodobování", "odměňování a tvarování.", "mimodomovní prostředí", "šoky"], 1], # [cite: 1941]
        ["Děti s Aspergerem na rozdíl od PAS:", ["nemají sociální postižení", "nemají omezené zájmy", "mají zájem o interakci", "menší zpoždění v řeči."], 2], # [cite: 1946]
        ["Co NENÍ pravda o Rettově syndromu?", ["dívky", "normální vývoj do 6-12 m", "růst hlavy", "nemají poruchy řeči."], 3], # [cite: 1951]
        ["25 % dětí s _______ možná nikdy nezačne chodit:", ["PAS", "Aspergerem", "Rettovým syndromem.", "dezintegrační poruchou"], 2], # [cite: 1956]
        ["Lukáš ztratil dovednosti po normálním vývoji:", ["PAS", "Asperger", "dětská dezintegrační porucha.", "Rett"], 2] # [cite: 1961]
    ],
        "PPP a ANOREXIE": [
            ["1. Přestože mají podobné obavy z jídla a přibírání na váze, jedinci s bulimií se liší od jedinců s anorexií v tom, že _______, zatímco jedinci s anorexií ne.", ["se přejídají a následně se zbavují jídla", "se pohybují v rozmezí 10 % své normální hmotnosti", "užívají projímadla", "jsou tajnůstkářští ohledně své poruchy"], 1], # [cite: 1967]
        ["2. Poruchy příjmu potravy jsou _______ nejčastějším onemocněním u dospívajících dívek.", ["druhým", "třetím", "pátým", "desátým"], 1], # [cite: 1972]
        ["3. Na rozdíl od většiny poruch dětství a dospívání jsou příčiny poruch příjmu potravy neúměrně spojeny s _______ vlivy.", ["sociokulturními", "biologickými", "rodinnými", "psychologickými"], 0], # [cite: 1977]
        ["4. Které z následujících tvrzení o vybíravém jedení v raném dětství je NEPRAVDIVÉ?", ["Téměř třetina malých dětí je označována jako vybíraví jedlíci", "Vybíravé jedení je častější u dívek než u chlapců", "Vybíravé jedení v raném dětství souvisí s pozdějším rozvojem poruch příjmu potravy", "Vybíravé jedení není považováno za součást normálního raného vývoje"], 3], # [cite: 1982]
        ["5. Která z následujících charakteristik je nejméně pravděpodobná u dospívajících, u nichž se rozvinou problémy s příjmem potravy?", ["vyšší procento tělesného tuku", "častý nástup puberty", "špatný školní prospěch", "souběžné psychické problémy"], 2], # [cite: 1987]
        ["6. Do poloviny adolescence přibližně _______ dívek uvádí, že byly během předchozího roku na dietě.", ["10 %", "25 %", "65 %", "90 %"], 2], # [cite: 1992]
        ["7. Který z následujících následků je u podvyživeného jedince nejméně pravděpodobný?", ["ztráta cirkadiánního rytmu", "pokles uvolňování růstového hormonu", "kožní změny", "letargie, apatie a deprese"], 1], # [cite: 1997]
        ["8. Rovnováha energetického výdeje jedince se označuje jako", ["set point", "metabolická rychlost", "cirkadiánní rytmus", "čistý kalorický příjem"], 1], # [cite: 2002]
        ["9. Pokud hladina tuku klesne pod normální rozmezí těla, hypotalamus", ["produkuje méně inzulinu", "spustí proliferaci tukových buněk", "zpomalí metabolismus", "uvolní růstový hormon"], 2], # [cite: 2007]
        ["10. Přibližně 50–75 % produkce růstového hormonu probíhá", ["prenatálně", "po nástupu hlubokého spánku", "během adolescence", "při jídle"], 1], # [cite: 2012]
        ["11. Porucha příjmu potravy kojenců a batolat je charakterizována", ["pojídáním nejedlých látek", "přejídáním a zvracením za účelem hubnutí", "výrazným zpomalením přibývání na váze", "záměrným regurgitováním potravy"], 2], # [cite: 2017]
        ["12. Porucha příjmu potravy je častější u", ["dívek", "dětí ze znevýhodněného prostředí", "dospívajících", "jedinců s mentálním postižením"], 1], # [cite: 2022]
        ["13. Časný nástup poruchy příjmu potravy je často spojen s", ["mentálním postižením", "nadměrným výchovným důrazem na jídlo", "nedostatečnou péčí", "špatnou metabolickou kontrolou"], 2], # [cite: 2027]
        ["14. _______ byl/byly/byla identifikován(y/a) jako specifický rizikový faktor poruch příjmu potravy u kojenců.", ["obtížný temperament", "Špatná metabolická kontrola", "rodičovská psychopatologie", "Poruchy příjmu potravy u matky"], 3], # [cite: 2032]
        ["15. Dítě, které jí hmyz a dřevěné třísky, bude pravděpodobně diagnostikováno s", ["poruchou příjmu potravy v dětství", "ruminací", "neprospíváním", "pikou"], 3], # [cite: 2037]
        ["16. Pika se často vyskytuje u jedinců s", ["mentálním postižením", "ADHD", "depresí", "bulimií"], 0], # [cite: 2042]
        ["17. Pika u malých dětí (bez mentálního postižení) často odezní", ["když dítěti začnou růst zuby", "poté, co dítě onemocní v důsledku požití nejedlé látky", "když dítě zažívá zvýšenou stimulaci", "jakmile dítě získá kognitivní schopnost pochopit, že určité látky nejsou jedlé"], 2], # [cite: 2047]
        ["18. Pika v prvním a druhém roce života u jinak normálně se vyvíjejících kojenců a batolat je pravděpodobně způsobena", ["nediagnostikovanými poruchami učení", "hladem", "nedostatečnou stimulací a dohledem v domácím prostředí", "depresí"], 2], # [cite: 2052]
        ["19. Neprospívání dítěte (failure to thrive) je charakterizováno hmotností pod _______ percentilem a/nebo zpomalením přírůstku hmotnosti od narození alespoň o _______ směrodatné odchylky.", ["5, 1", "5, 2.", "10, 1", "10, 2"], 1], # [cite: 2057]
        ["20. Bylo zjištěno, že matky kojenců, kteří neprospívají, jsou ve srovnání s matkami kojenců bez této poruchy", ["více nejisté v citové vazbě", "mladší", "starší", "méně inteligentní"], 0], # [cite: 2062]
        ["21. Studie zjistily, že neprospívání dítěte může ovlivnit tělesný růst v dětství, ale neovlivňuje budoucí", ["psychické zdraví", "tělesný růst", "stravovací návyky", "kognitivní fungování"], 3], # [cite: 2067]
        ["22. Obezita je:", ["chronické zdravotní onemocnění", "porucha regulace hmotnosti", "selhální vůle", "duševní porucha se začátkem v dětství"], 0], # [cite: 2072]
        ["23. Obezita je obvykle definována jako index tělesné hmotnosti nad ___ percentilem.", ["60", "70", "80", "95"], 3], # [cite: 2077]
        ["24. V 90. letech bylo přibližně ___ amerických dětí považováno za děti s nadváhou.", ["2%", "7%", "15%", "25%"], 2], # [cite: 2082]
        ["25. Obezita je silně spojena s obezitou v", ["kojeneckém věku a mladším školním věku", "kojeneckém věku a adolescenci", "dětství a dospělosti.", "jakémkoli období vývoje a dospělosti"], 2], # [cite: 2087]
        ["26. Výzkumníci předpovídají, že budoucí míra obezity u dětí v USA a Evropské unii", ["zůstane stejná", "mírně poklesne", "výrazně vzroste", "výrazně poklesne díky vzdělávání"], 2], # [cite: 2092]
        ["27. Vztah mezi obezitou v preadolescenci a pozdějším rozvojem poruch příjmu potravy je pravděpodobně způsoben", ["biologickými abnormalitami, které jsou základem obou stavů", "posměchem, které obézní děti zažívají od vrstevníků", "základní psychiatrickou poruchou", "žádnou z uvedených možností"], 1], # [cite: 2097]
        ["28. Protein, který hraje významnou roli v některých genetických případech obezity, se nazývá", ["lutein", "peptin", "leptin.", "tyrosin"], 2], # [cite: 2102]
        ["29. Metody léčby, které mají pomoci obézním dětem zhubnout, by měly klást důraz na", ["náročné cvičební režimy", "přísné kalorické omezení", "vyhýbání se podnětům spojeným s jídlem", "aktivní, méně sedavý životní styl"], 3], # [cite: 2107]
        ["30. U některých dospívajících, zejména dívek, mohou být nadměrné snahy o kontrolu příjmu potravy mylným pokusem", ["potrestat rodiče", "zvládnout stres a tělesné změny spojené s přechodem do adolescence", "potrestat samy sebe", "vrátit se do orální fáze vývoje"], 1], # [cite: 2112]
        ["31. Na počátku 20. století spočívala léčba anorexie v", ["psychodynamické psychoterapii", "hypnoterapii", "odebrání dítěte z domova a nuceném krmení", "rodinné terapii"], 2], # [cite: 2117]
        ["32. Která z následujících možností NENÍ charakteristickým znakem anorexie?", ["ztráta chuti k jídlu", "strach z přibírání na váze", "popírání vlastní podváhy", "odmítání udržovat minimální normální tělesnou hmotnost"], 0], # [cite: 2122]
        ["33. MKN-10 rozlišuje dva podtypy anorexie na základě", ["procenta úbytku hmotnosti", "metod používaných k omezení kalorického příjmu", "přítomnosti či nepřítomnosti komorbidní deprese", "rodinné dynamiky"], 1], # [cite: 2127]
        ["34. Ve srovnání s osobami s bulimií mají jedinci s anorexií typu přejídání/zvracení tendenci", ["jíst stejné množství jídla, ale důkladněji se zbavovat potravy vylučováním", "jíst relativně malé množství jídla a pravidelněji se zbavovat potravy vylučováním", "přejídat se pouze zdravými potravinami", "zbavovat se potravy méně důsledně"], 1], # [cite: 2132]
        ["35. Ve srovnání s typem přejídání/zvracení mají jedinci s restriktivní anorexií tendenci", ["být impulzivnější", "mít signifikantní rodinnou anamnézu obezity", "mít kolísavější nálady", "být více kontrolující a rigidní"], 3], # [cite: 2137]
        ["36. Ve srovnání s restriktivním typem mají jedinci s anorexií typu přejídání/zvracení tendenci", ["být více kontrolující a rigidní", "být více obsesivní", "vykazovat méně problémů s náladou", "vykazovat vyšší míru výskytu impulzivních poruch"], 3], # [cite: 2142]
        ["37. Které z následujících tvrzení o bulimii je pravdivé?", ["Anorexie je častější než bulimie", "MKN-10 rozděluje bulimii na typ projímavý a restriktivní", "Přibližně třetina osob s bulimií se uchyluje k vylučování potravy", "Žádné z uvedených tvrzení není pravdivé"], 3], # [cite: 2147]
        ["38. Bulimie se dělí na podtypy:", ["s přejídáním a bez přejídání", "se zvracením a bez zvracení", "projímavý a neprojímavý", "restriktivní a nerestriktivní"], 2], # [cite: 2152]
        ["39. Nejčastější kompenzační technikou po epizodě přejídání v klinických vzorcích je", ["hladovění", "zvracení", "cvičení", "projímadla"], 1], # [cite: 2157]
        ["40. Nejčastějším kompenzačním chováním v běžné populaci osob splňujících kritéria bulimie (které však nevyhledaly pomoc) je/jsou", ["cvičení", "projímadla", "zvracení", "dietní pilulky"], 0], # [cite: 2162]
        ["41. Mladé ženy s dietně-depresivním podtypem bulimie se od žen s čistě dietním podtypem liší tím, že vykazují", ["méně narušeného stravovacího chování", "větší sociální narušení", "méně psychiatrických komorbidit", "víc anorektických příznaků"], 1], # [cite: 2167]
        ["42. Nespokojenost s tělem a zkreslení tělesného obrazu u osob s poruchami příjmu potravy jsou s nejmenší pravděpodobností spojovány s/se", ["zkreslením pozornosti", "zkreslením paměti", "selektivní interpretací", "poruchami percepčních schopností"], 3], # [cite: 2172]
        ["43. Dvacet pět procent chlapců a dívek splňujících kritéria poruchy záchvatovitého přejídání rovněž referuje", ["užívání nelegálních drog", "sexuální promiskuitu", "pravidelnou konzumaci alkoholu", "pokus o sebevraždu v anamnéze"], 3], # [cite: 2177]
        ["44. Porucha záchvatovitého přejídání (BED) se liší od bulimie tím, že jedinci s BED", ["nepociťují ztrátu kontroly při přejídání", "snědí více než 1000 kalorií najednou", "nevykazují kompenzační chování", "mají nižší sebeúctu"], 2], # [cite: 2182]
        ["45. Mezi dospívajícími dívkami a mladými dospělými se prevalence anorexie odhaduje na", ["0,9 %", "3 %", "7 %", "14 %"], 0], # [cite: 2187]
        ["46. Které z následujících tvrzení o genderových rozdílech u poruch příjmu potravy je NEPRAVDIVÉ?", ["Mladí muži s poruchami příjmu potravy obecně vykazují stejné klinické rysy jako mladé ženy", "Muži vykazují menší touhu po štíhlosti než ženy", "Muži vykazují větší zaujetí jídlem než ženy", "Muži kladou větší důraz na atletický vzhled nebo atraktivitu než ženy"], 2], # [cite: 2192]
        ["47. Nejčastěji jedinci s anorexií ", ["umírají hladem", "se ze své poruchy zcela uzdraví", "se po dvacátém roce života stanou obézními", "obnoví normální hmotnost, ale poté relapsují"], 3], # [cite: 2197]
        ["48. Nástup bulimie je typicky v:", ["typicky nastává v rané i pozdní adolescenci", "typicky nastává v pozdní adolescenci a rané dospělosti", "typicky nastává v dospělosti", "může nastat kdykoli po nástupu puberty"], 1], # [cite: 2202]
        ["49. Studie pacientů s bulimií ukazují, že mezi _______ pacientů dosáhne během několika let úplného uzdravení.", ["10-15%", "20-25%", "30-45%", "50-75%"], 3], # [cite: 2207]
        ["50. Který z následujících faktorů není prediktorem úplného uzdravení u osob s bulimií?", ["vyšší sociální třída", "vyšší věk při nástupu poruchy", "zneužívání alkoholu v rodinné anamnéze", "všechny uvedené faktory jsou prediktory úplného uzdravení"], 1], # [cite: 2212]
        ["51. Neurotransmiterem, kterému byla věnována největší pozornost jako možnému původci poruch příjmu potravy, je", ["dopamin", "GABA", "serotonin", "noradrenalin"], 2], # [cite: 2217]
        ["52. Vědci zjistili biochemické podobnosti mezi lidmi s poruchami příjmu potravy a lidmi s/se", ["ADHD", "sociální fobií", "schizofrenií", "obsedantně-kompulzivní poruchou"], 3], # [cite: 2222]
        ["53. Které z následujících faktorů byly spojovány s rozvojem poruch příjmu potravy?", ["zneužívání návykových látek rodičů", "sexuální zneužívání", "rodinné konflikty", "všechny výše uvedené faktory"], 3], # [cite: 2227]
        ["54. Hilda Bruchová, průkopnice ve výzkumu psychologických procesů u poruch příjmu potravy, navrhla, že sebetrýznění hladem u osob s anorexií bylo", ["spojeno s jejich bojem o autonomii, kompetenci, kontrolu a sebeúctu", "snahou potrestat chladné a kontrolující rodiče", "snahou zabránit tělesnému dospívání", "spojeno s narušeným myšlením v důsledku působení environmentálních toxinů"], 0], # [cite: 2232]
        ["55. Arthur Crisp, průkopník v porozumění a léčbě poruch příjmu potravy, považoval anorexii za typ _______ poruchy.", ["fobické vyhýbavé.", "depresivní", "závislostní", "osobnostní"], 0], # [cite: 2237]
        ["56. Která z následujících charakteristik je nejméně pravděpodobná u dospívajícího s anorexií?", ["rigidita a obsesivnost", "nedostatek emoční zdrženlivosti", "preference známého", "vysoká potřeba schválení"], 1], # [cite: 2242]
        ["57. Která z následujících poruch je nejméně pravděpodobná jako komorbidní s poruchami příjmu potravy?", ["deprese", "úzkost", "obsesivně-kompulzivní porucha", "ADHD"], 3], # [cite: 2247]
        ["58. Společným spojovacím článkem mezi depresí a poruchami příjmu potravy může být", ["impulzivita", "perfekcionismus", "hněv", "rigidita"], 1], # [cite: 2252]
        ["59. _______ je počáteční léčbou volby u dětí a dospívajících s anorexií, kteří žijí doma.", ["dočasné odebrání z domova", "rodinná terapie", "psychofarmakologie", "individuální terapie"], 1], # [cite: 2257]
        ["60. Nejúčinnější současná léčba bulimie je:", ["psychoterapie zaměřená na náhled", "rodinná terapie", "psychofarmakologie", "kognitivně-behaviorální terapie"], 3] # [cite: 2262]
    ]
    }

# Nastavení stránky pro mobil
st.set_page_config(page_title="Psychologie Kvíz", page_icon="🧠")

if 'score' not in st.session_state: st.session_state.score = 0
if 'total' not in st.session_state: st.session_state.total = 0
if 'q' not in st.session_state: st.session_state.q = None

st.title("🧠 Kvíz z Klinické Psychologie")

# Výběr kategorie v menu
kat = st.selectbox("Vyber si okruh:", list(st.session_state.questions.keys()))

if st.button("Další náhodná otázka") or st.session_state.q is None:
    st.session_state.q = random.choice(st.session_state.questions[kat])
    st.session_state.answered = False

# Zobrazení otázky
q_text, options, correct = st.session_state.q
st.write(f"### {q_text}")

# Tlačítka pro odpovědi
for i, opt in enumerate(options):
    if st.button(opt, key=f"opt_{i}"):
        st.session_state.total += 1
        if i == correct:
            st.session_state.score += 1
            st.success("Správně! 🎉")
        else:
            st.error(f"Špatně. Správně je: {options[correct]}")

st.divider()
st.write(f"**Tvé skóre: {st.session_state.score} / {st.session_state.total}**")










