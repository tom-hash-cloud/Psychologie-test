import streamlit as st
import random

# Tady jsou všechna tvá data z dokumentu
if 'questions' not in st.session_state:
    st.session_state.questions = {
        "ADHD": [
            ["1. Při diagnostice ADHD u dítěte psycholog pravděpodobně hledá", ["charakteristické vzorce chování.", "metabolity v krvi.", "abnormality v čelním laloku mozku.", "násilné chování ze strany rodičů."], 0],
    ["2. Děti s ADHD obecně", ["mají potěšení z pocitu, že se vymykají kontrole.", "chtějí dosahovat dobrých výsledků, ale kvůli omezené sebekontrole mají potíže.", "se mohou chovat přiměřeně, pokud vynaloží dostatečné úsilí.", "lépe prospívají, když mají jasně stanovená a důsledně dodržovaná pravidla."], 1],
    ["3. Teorie poškození mozku u ADHD, která vznikla ve 40. a 50. letech 20. století, byla zavržena, protože", ["pomocí rentgenu nebyly nalezeny žádné důkazy o poškození mozku.", "v roce 1958 byla identifikována psychologická příčina ADHD.", "vysvětluje jen velmi malý počet případů ADHD.", "poškození mozku bylo spojováno spíše s mentální retardací než s ADHD."], 2],
    ["4. Které z následujících tvrzení o ADHD je NEPRAVDIVÉ?", ["Nebyla zjištěna jediná příčina chování dětí s ADHD.", "ADHD je souhrnný pojem, který popisuje několik různých vzorců chování, jež se mírně liší.", "Hyperaktivita a nepozornost jsou základními znaky ADHD.", "Nexistují výrazné příznaky ADHD, které lze zjistit pomocí rentgenového snímku nebo laboratorního testu."], 2],
    ["5. Virginia Douglasová tvrdila, že", ["hyperaktivita je primární složkou ADHD.", "kromě hyperaktivity jsou hlavními příznaky také nepozornost a nedostatky v kontrole impulzů.", "ADHD je způsobena minimálním poškozením mozku.", "ADHD je spíše psychologického než biologického původu."], 1],
    ["6. V současnosti jsou za hlavní poruchy u ADHD považovány", ["nepozornost a obtíže s regulací motorického chování.", "potíže s inhibicí chování a slabá seberegulace.", "nepozornost a špatná morální kontrola.", "hyperaktivita a kognitivní problémy."], 1],
    ["7. Radek si nedokáže zapamatovat telefonní číslo, pokud si jej nezapíše. Vykazuje deficit v oblasti", ["impulzivity.", "udržení pozornosti.", "selektivní pozornosti.", "kapacity pozornosti."], 3],
    ["8. Když si Markéta sedne k domácím úkolům a učení, snadno ji rozptýlí televize v jiné místnosti. Markéta vykazuje deficit v oblasti", ["kontroly pozornosti.", "udržení pozornosti.", "selektivní pozornosti.", "kapacity pozornosti."], 2],
    ["9. Tomáš má problémy s udržením pozornosti zejména tehdy, když je unavený nebo ho úkol nezajímá. Tomáš vykazuje nedostatky v oblasti", ["udržení pozornosti.", "rozptýlenosti.", "selektivní pozornosti.", "kapacity pozornosti."], 0],
    ["10. Který z následujících pojmů je jiným označením deficitu selektivní pozornosti?", ["rozptýlenost", "impulzivita", "duální pozornost", "dezorganizace"], 0],
    ["11. Mnozí se domnívají, že hlavní příčinou deficitu pozornosti u ADHD je", ["selektivní pozornost.", "kapacita pozornosti.", "udržení pozornosti / bdělosti.", "rozptýlenost."], 2],
    ["12. Který úkol může být pro dítě s ADHD nejobtížnější?", ["naučit se novou videohru", "věnovat pozor učiteli, zatímco někdo jiný ve třídě mluví", "zapamatovat si telefonní číslo kamaráda", "pracovat 45 minut na stránce s jednoduchými matematickými úlohami"], 3],
    ["13. Kdy vykazuje dítě s ADHD pravděpodobně více pohybové aktivity než ostatní děti?", ["když je požádáno, aby v klidu sedělo u stolu", "ve spánku", "při hře na hřišti", "ve všech uvedených situacích"], 0],
    ["14. Který z následujících příkladů představuje kognitivní impulzivitu?", ["vyhrknutí odpovědi ve třídě", "dotýkání se horké plotny", "překotné myšlení", "přerušení rodiče při telefonování"], 2],
    ["15. Děti s ADHD, u nichž je zvýšené riziko problémů s chováním nebo opozičním vzdorem, jsou ty, které vykazují", ["behaviorální impulzivitu.", "kognitivní impulzivitu.", "selektivní nepozornost.", "sníženou schopnost pozornosti."], 0],
    ["16. Děti, které jsou více ohroženy problémy v akademickém výkonu, jsou ty, které vykazují", ["behaviorální impulzivitu.", "kognitivní impulzivitu.", "selektivní nepozornost.", "kombinaci behaviorální a kognitivní impulzivity."], 3],
    ["17. Které z následujících je dalším kritériem pro diagnózu ADHD?", ["příznaky se musí objevit před 12. rokem věku", "příznaky musí být přítomny alespoň jeden rok", "příznaky se musí vyskytovat alespoň v jednom prostředí", "příznaky musí způsobovat významné narušení sociálního nebo školního fungování dítěte"], 3],
    ["18. Které z následujících NENÍ dalším kritériem pro diagnózu ADHD?", ["příznaky se musí objevit před 12. rokem věku", "příznaky musí být přítomny nejméně 6 měsíců", "příznaky se musí vyskytovat ve více než jednom prostředí", "příznaky musí způsobovat významné poruchy sociálního nebo školního fungování dítěte"], 0],
    ["19. Ve srovnání s dětmi s ADHD-HI mají děti s podtypem ADHD-PI vyšší riziko", ["antisociálního chování.", "odmítání ze strany vrstevníků.", "úzkostných poruch a poruch nálady.", "zařazení do speciálního vzdělávání."], 2],
    ["20. Které z následujících tvrzení o ADHD-HI NENÍ pravdivé?", ["děti s ADHD-HI jsou často starší než děti s ADHD-C", "podtyp ADHD-HI je nejvzácnějším podtypem ADHD", "děti s ADHD-HI častěji vykazují poruchy chování než děti s ADHD-PI", "děti s ADHD-HI jsou častěji vyloučovány ze školy než děti s ADHD-PI"], 0],
    ["21. Které z následujících tvrzení o ADHD-PI NENÍ pravdivé?", ["děti s ADHD-PI jsou často popisovány jako zasněné a ospalé", "děti s ADHD-PI mají potíže s rychlostí zpracování informací", "děti s ADHD-PI jsou často popisovány jako agresivní a hrubé", "výzkumy naznačují, že děti s ADHD-PI mohou mít zcela odlišnou poruchu než děti s ADHD-HI a ADHD-C"], 2],
    ["22. Které z následujících tvrzení NENÍ kritikou diagnostických kritérií DSM-V pro ADHD?", ["počet požadovaných příznaků není přizpůsoben věku nebo úrovni vyspělosti dítěte", "požadavek přetrvání příznaků po dobu 6 měsíců může být pro malé děti příliš dlouhý", "DSM pojímá ADHD striktně kategoriálně", "požadovaný věk nástupu onemocnění 7 let může být příliš nízký"], 1],
    ["23. Mentální procesy, které stojí za schopností dětí regulovat vlastní chování, se nazývají", ["exekutivní funkce.", "metakognice.", "sebepojetí.", "sledování myšlenek."], 0],
    ["24. Které z následujících tvrzení nejlépe vystihuje inteligenci dětí s ADHD?", ["více než 50 % dětí s ADHD má podprůměrnou inteligenci", "více než 50 % dětí s ADHD má nadprůměrnou inteligenci", "inteligentnější děti vykazují více impulzivity a hyperaktivity", "většina dětí s ADHD má průměrnou inteligenci."], 3],
    ["25. Které dítě bude s větší pravděpodobností vykazovat pozitivní iluzorní zkreslení?", ["dítě s ADHD-HI a poruchami chování", "dítě s ADHD-HI a depresí", "dítě s ADHD-PI a úzkostí", "dítě s ADHD-PI a proruchami chováním"], 0],
    ["26. Který z následujících znaků NENÍ charakteristickým rysem řeči/jazyka dítěte s ADHD?", ["tichá, mumlavá řeč, kterou je obtížné slyšet", "časté změny tématu rozhovoru", "používání menšího množství zájmen a spojek", "nejasné návaznosti v konverzaci"], 0],
    ["27. Které z následujících tvrzení o zdravotním stavu dětí s ADHD je NEPRAVDIVÉ?", ["děti s ADHD často trpí poruchami spánku", "děti s ADHD mohou vykazovat mírné poruchy růstu, které jsou pravděpodobně způsobené užíváním léků", "děti s ADHD vykazují vyšší výskyt tikových poruch než ostatní děti", "děti s ADHD jsou náchylnější k úrazům než ostatní děti"], 1],
    ["28. Matky dětí s ADHD mají vyšší pravděpodobnost výskytu", ["problémů se zneužíváním návykových látek.", "schizofrenie.", "deprese.", "disociální poruchy osobnosti."], 2],
    ["29. Které z následujících tvrzení o dětech s ADHD je pravdivé?", ["mají deficit v sociálním uvažování", "mají stejnou sociální agendu jako jejich vrstevníci", "uvádějí, že dostávají vysokou míru sociální podpory od vrstevníků", "jsou trvale odmítány vrstevníky"], 3],
    ["30. Děti s ADHD vykazují", ["sníženou touhu po vztazích s vrstevníky", "špatné porozumění sociálním vztahům", "silnou schopnost správně rozpoznávat emoce u druhých", "malou vzájemnost ve vztazích s vrstevníky"], 3],
    ["31. Nejčastějšími komorbidními psychickými poruchami u dětí s ADHD jsou", ["úzkost a deprese.", "porucha opozičního vzdoru a deprese.", "tikové poruchy.", "porucha chování a porucha opozičního vzdoru."], 3],
    ["32. Které tvrzení o dětech s ADHD a úzkostnými poruchami je pravdivé?", ["často se jedná o adolescenty", "často patří k podtypu ADHD-HI", "často patří k podtypu ADHD-PI", "tvoří přibližně 50 % klinicky odesílaných dětí s ADHD"], 2],
    ["33. Vztah mezi ADHD a depresí se zdá být funkcí", ["provokování a demoralizace, kterou dítě zažívá v důsledku svých příznaků.", "rodinného rizika jedné poruchy, které zvyšuje riziko druhé.", "celkového rodinného stresu.", "všech uvedených faktorů"], 1],
    ["34. Nejlepší odhad prevalence ADHD u dětí školního věku je", ["1–2 %", "3–5 %", "9–10 %", "15–20 %"], 1],
    ["35. Vyšší výskyt ADHD u chlapců ve srovnání s dívkami je s největší pravděpodobností způsoben", ["výběrovým a referenčním zkresleními.", "společenským očekáváním a tolerancí.", "vyšší mírou agrese u chlapců.", "všemi uvedenými faktory"], 3],
    ["36. Ve srovnání s chlapci vykazují dívky s ADHD častěji", ["vyšší úroveň hyperaktivity.", "větší postižení exekutivních funkcí.", "vyšší úroveň agrese.", "příznaky nepozornosti / dezorganizace."], 3],
    ["37. Dívky s ADHD mají ve srovnání s dívkami bez ADHD vyšší pravděpodobnost", ["poruch chování, nálady a úzkostných poruch.", "nižší míru verbální agrese.", "vyšší IQ a lepší školní výsledky.", "neplatí nic z výše uvedeného"], 0],
    ["38. Vyšší výskyt ADHD v nízkých socioekonomických skupinách je nejlépe vysvětlen", ["přítomností souběžné deprese.", "přítomností psychopatologie u rodičů.", "přítomností souběžných poruch chování.", "přítomností souběžných poruch učení."], 2],
    ["39. Které tvrzení o ADHD a kultuře NENÍ pravdivé?", ["ADHD se častěji vyskytuje ve vyšších socioekonomických skupinách než v nižších", "ADHD bylo zaznamenáno ve všech zemích, kde bylo studováno", "rozdíly v prevalenci ADHD mezi kulturami mohou odrážet kulturní normy", "rozdíly v prevalenci ADHD mezi kulturami mohou souviset s rozdíly v definici"], 0],
    ["40. Matky dětí s ADHD často popisují své děti v kojeneckém věku jako _________.", ["obtížné", "snadné", "nerozeznatelné od sourozenců", "nadměrně úzkostné a depresivní"], 0],
    ["41. Pokud jde o nástup příznaků ADHD", ["příznaky hyperaktivity-impulzivity a nepozornosti se obvykle objevují přibližně ve stejnou dobu, zpravidla v předškolním věku.", "příznaky hyperaktivity-impulzivity a nepozornosti se objevují přibližně ve stejnou dobu, obvykle na počátku školní docházky.", "příznaky nepozornosti se obvykle objevují dříve než příznaky hyperaktivity-impulzivity.", "příznaky hyperaktivity-impulzivity se obvykle objevují dříve než příznaky nepozornosti."], 3],
    ["42. Které tvrzení o průběhu ADHD je pravdivé?", ["ADHD se nerozvíjí dříve než ve školním věku", "většina dětí s ADHD své potíže před dospíváním překoná", "mnoho dospělých má ADHD, ale v dětství nebyli nikdy diagnostikováni", "všechna uvedená tvrzení jsou pravdivá"], 2],
    ["43. Dospělí s ADHD mají větší šanci na lepší životní výsledky, pokud", ["jsou jejich příznaky méně závažné.", "mají podporu rodiny.", "mají přístup ke zdrojům pomoci.", "platí vše výše uvedené"], 3],
    ["44. Která z následujících možností nejpravděpodobněji způsobuje ADHD?", ["příliš mnoho cukru", "zářivkové osvětlení", "špatné školní prostředí", "žádná z uvedených možností není správná"], 3],
    ["45. Děti s ADHD vykazují", ["deficity motivace.", "deficity v úrovni aktivace (arousalu).", "deficity v seberegulaci.", "všechny výše uvedené projevy"], 3],
    ["46. Výzkum příčinných faktorů poskytuje silné důkazy, že ADHD je porucha s převážně _________ determinantami.", ["biologickými", "neurobiologickými", "socio-environmentálními", "rodinnými"], 1],
    ["47. Studie na dvojčatech naznačují, že největší roli při vzniku ADHD hrají faktory _________.", ["sdíleného prostředí", "nesdíleného prostředí", "dědičnosti", "všechny uvedené faktory hrají podobnou roli"], 2],
    ["48. Gen dopaminového receptoru DRD4, je spojován s", ["vyhledáváním vzrušení.", "popudlivým chováním.", "impulzivitou.", "všemi výše uvedenými faktory"], 3],
    ["49. Drobné tělesné anomálie a další rizikové faktory před, během a po narození jsou specifickými rizikovými faktory pro", ["ADHD, ale nikoli pro jiné formy psychopatologie.", "mnoho forem psychopatologie.", "pouze ADHD a poruchy chování.", "pouze úzkost a depresi."], 1],
    ["50. Neurobiologický výzkum příčin ADHD opakovaně podporuje zapojení", ["limbického systému.", "hipokampu.", "retikulárního aktivačního systému.", "frontostriatálních okruhů."], 3],
    ["51. Ve studii Hoovera & Miliche (1994) matky, které se (mylně) domnívaly, že jejich děti požily cukr,", ["popisovaly své děti jako „milejší“ než matky v kontrolní skupině.", "hodnotily své děti jako šťastnější a klidnější než matky v kontrolní skupině.", "byly ke svým dětem kritičtější a hodnotily je jako více hyperaktivní než matky v kontrolní skupině.", "nezaznamenaly žádnou změnu v chování svých dětí."], 2],
    ["52. Výzkum negativního vlivu rodiny na symptomatologii ADHD naznačuje, že", ["rodinné faktory vysvětlují významnou část variability symptomů ADHD.", "rodinné faktory vysvětlují pouze malou část variability symptomů ADHD.", "rodinné faktory mohou zvyšovat závažnost některých symptomů ADHD.", "rodinné faktory vysvětlují pouze malou část variability symptomů ADHD, přesto však mohou zvyšovat závažnost některých symptomů."], 3],
    ["53. Nejlepší léčbou ADHD je", ["použití stimulačních léků.", "trénink rodičovských dovedností.", "vzdělávací intervence.", "kombinace všech uvedených přístupů"], 3],
    ["54. Stimulační léky fungují tak, že", ["paradoxně děti zpomalují.", "mění aktivitu neurotransmiterů ve frontostriatálních oblastech mozku (stimulují oblasti s nízkou aktivací).", "zlepšují náladu, což následně zvyšuje sebehodnocení a kontrolu chování.", "„přesvědčují“ rodiče a učitele, že fungují, i když ve skutečnosti nefungují (placebo efekt)."], 1],
    ["55. Vzdělávací intervence u ADHD může zahrnovat", ["postupy založené na odečítání bodů (token economy) ve třídě.", "používání vizuálních pomůcek.", "poskytování písemných i ústních instrukcí.", "všechny výše uvedené možnosti"], 3],
    ["56. Výsledky Multimodální studie léčby dětí s ADHD (MTA Study) ukázaly, že", ["behaviorální léčba byla obecně účinnější než farmakologická léčba.", "přidání behaviorální léčby k medikaci přineslo větší zlepšení základních symptomů než samotná medikace.", "tři roky po ukončení léčby přetrvával přínos léčby pouze u skupiny s farmakologickou léčbou.", "žádná z uvedených možností není správná"], 2]
],
        "ÚZKOSTNÉ PORUCHY": [
            ["1. Která z následujících možností NEPLATÍ pro úzkostné poruchy?", ["U dospělých jsou sice časté, ale u dětí jsou relativně vzácné.", "Existuje několik různých typů úzkostných poruch.", "Úzkostné poruchy mohou přetrvávat po celý život.", "Úzkostné poruchy se často vyskytují společně s jinými poruchami."], 0],
    ["2. _______ mobilizuje tělo k akci v situaci boj/útěk.", ["Centrální nervový systém", "Periferní nervový systém", "Sympatický nervový systém", "Parasympatickým nervovým systémem"], 2],
    ["3. Při aktivaci sympatického nervového systému dochází k uvolnění _______ v nadledvinkách.", ["inzulínu", "adrenalinu", "růstového hormonu", "testosteronu"], 1],
    ["4. _______ je/jsou okamžitá poplachová reakce na aktuální nebezpečí nebo ohrožení života.", ["Úzkost", "Panika", "Strach", "Obavy"], 2],
    ["5. _______ se vyznačuje/vyznačují pocity strachu a nedostatku kontroly nad nadcházejícími událostmi.", ["Úzkost", "Panika", "Strach", "Obavy"], 0],
    ["6. _______ je/jsou skupina tělesných příznaků reakce boj/útěk, které se nečekaně objevují bez zjevné hrozby nebo nebezpečí.", ["Úzkost", "Panika", "Strach", "Obavy"], 1],
    ["7. Strach _______ se zvyšuje s věkem.", ["ze sociálních situací", "ze školy", "z tmy", "z odloučení od rodičů"], 0],
    ["8. Strach ze smrti je běžný u dětí ve věku", ["1-2 let.", "3-5 let.", "6-8 let.", "9-12 let."], 3],
    ["9. Strach z odloučení od rodičů je běžný u dětí ve věku", ["1-2 let.", "3-4 let.", "5-6 let.", "všechny tyto věkové skupiny"], 3],
    ["10. Ve srovnání s dětmi bez úzkostných poruch mají děti s úzkostnými poruchami intenzivnější obavy z/ze", ["školních úloh.", "bolístek.", "dobrých výsledků ve sportu.", "pobytu v blízkosti cizích lidí."], 3],
    ["11. Rituální chování je u malých dětí ______援.", ["nepřítomné", "neobvyklé", "běžné", "obtížně pozorovatelné"], 2],
    ["12. Úzkostné poruchy jsou v MKN-10 rozděleny do kategorií, které odrážejí", ["primární dimenze úzkosti (biologické/kognitivní/behaviorální).", "druhy reakcí a vyhýbání se.", "odpověď na léčbu (dobrá/špatná).", "typický věk nástupu."], 1],
    ["13. Kdy absence separační úzkosti naznačuje nejistou vazbu?", ["ve 2 měsících věku", "ve 12 měsících věku", "ve věku 10 let", "nikdy"], 1],
    ["14. Nejčastější úzkostnou poruchou v dětství je", ["obsedantně-kompulzivní porucha.", "panická porucha.", "generalizovaná úzkostná porucha.", "separační úzkostná porucha."], 3],
    ["15. Úzkostná porucha s nejčasnějším věkem nástupu je", ["obsedantně-kompulzivní porucha.", "panická porucha.", "generalizovaná úzkostná porucha.", "separační úzkostná porucha."], 3],
    ["16. Průměrný věk nástupu separační úzkostné poruchy je", ["ve věku 2-3 let.", "ve věku 4-6 let.", "ve věku 7-8 let.", "ve věku 9-10 let."], 2],
    ["17. Který z následujících případů NENÍ u dětí se separační úzkostnou poruchou běžný?", ["souběžný výskyt jiné úzkostné poruchy", "souběžný výskyt depresivní poruchy", "souběžný výskyt poruchy chování", "odmítání školní docházky"], 2],
    ["18. Která z následujících možností vede nejméně pravděpodobně k odmítání školní docházky?", ["potíže s učením", "separační úzkostná porucha", "strach z posměchu nebo šikany", "strach z hodnocení okolím"], 0],
    ["19. Která z následujících diagnóz NEPATŘÍ mezi diagnózy MKN-10?", ["separační úzkostná porucha", "obsedantně-kompulzivní porucha", "panická porucha", "testová úzkost"], 3],
    ["20. Které z následujících tvrzení o testové úzkosti je NEPRAVDIVÉ?", ["Děti s testovou úzkostí se často obávají, že budou při testu negativně hodnoceny.", "Testová úzkost může občas odrážet specifickou fobii z testových situací.", "Testová úzkost je často komorbidní s generalizovanou úzkostnou poruchou.", "Všechny uvedené možnosti jsou pravdivé."], 3],
    ["21. Přehnané obavy a napětí při absenci podmínek, které by normálně takovou reakci vyvolaly, se označují jako", ["očekávaná tenze.", "obavné očekávání.", "strach.", "panika."], 1],
    ["22. Která z následujících možností odlišuje děti s generalizovanou úzkostnou poruchou od dětí s jinými úzkostnými poruchami?", ["jejich obavy jsou nepřiměřené věku", "vyskytují se u nich somatické příznaky", "dělají si starosti kvůli drobným událostem", "mají obavy z drobných událostí a pociťují somatické příznaky"], 2],
    ["23. Aby byla u dítěte diagnostikována generalizovaná úzkostná porucha, musí se u něj projevovat", ["separační úzkostná porucha.", "obavy o studijní výsledky.", "alespoň jeden somatický příznak.", "perfekcionismus a sebekritické chování."], 2],
    ["24. Prevalence generalizované úzkostné poruchy u dětí je", ["1-2 %", "2-4 %", "3-6 %", "6-8 %"], 2],
    ["25. Na rozdíl od dospělých děti specifickými fobiemi", ["se vyhýbají obavným podnětům.", "nerozpoznají, že jejich obavy jsou extrémní a nepřiměřené.", "pociťují fyziologické vzrušení, když se setkají s obávanými podněty.", "jsou snadněji léčitelné."], 1],
    ["26. Předpokládá se, že nejčastější specifickou fobií u dětí je strach ze zvířat způsobený", ["vysokou mírou vystavení zvířatům v raném dětství.", "evolučními procesy.", "nadměrnou ochranou rodičů při setkání malých dětí se zvířaty.", "všechny tyto faktory"], 1],
    ["27. Příkladem situační specifické fobie je strach z", ["výšek.", "výtahů.", "nemocí.", "injekcí."], 1],
    ["28. ______ je nejčastější sekundární diagnózou u dětí s jinou úzkostnou poruchou.", ["Specifická fobie", "Sociální fobie", "Obsedantně-kompulzivní porucha", "Generalizovaná úzkostná porucha"], 1],
    ["29. Většina sociálních fobií se poprvé objevuje v", ["předškolním věku.", "mladší školním věku.", "prepubertě.", "pubertě a dospívání."], 3],
    ["30. Selektivní mutismus je považován za typ", ["specifická fobie.", "generalizované úzkostné poruchy.", "obsedantně-kompulzivní poruchy.", "sociální fobie."], 3],
    ["31. Děti, u nichž se projevuje selektivní mutismus, mohou také", ["být opožděné ve vývoji.", "mít poruchy řeči.", "mít poruchy sluchového vnímání.", "platí vše výše uvedené"], 3],
    ["32. U dítěte, jehož posedlostí je čistota, je pravděpodobné, že bude doprovázeno nutkáním", ["mytí rukou.", "vyhýbat se prasklinám na chodníku.", "přemýšlet o špíně.", "opakovaně se dotýkat špinavých předmětů."], 0],
    ["33. Nutkání počítat stále dokola do určitého čísla často souvisí s obavou z/ze", ["symetrie nebo řádu.", "poškození.", "kontaminace.", "náboženských otázek."], 1],
    ["34. Jaký je účel kompulzí?", ["spotřebovat čas", "vyhnout se soustředění na jiné věci", "snížit úzkost", "nemá žádný záměr"], 2],
    ["35. Míra výskytu obsedantně-kompulzivní poruchy u dětí je _______ míra/míře výskytu obsedantně-kompulzivní poruchy u dospělých.", ["menší než", "větší než", "je rovna", "více variabilní než"], 2],
    ["36. _______ vlivy hrají větší roli u časných případů obsedantně-kompulzivní poruchy než v případech pozdního nástupu obsedantně-kompulzivní poruchy.", ["Rodičovské", "Skupinové", "Neurobiologické", "Genetické"], 3],
    ["37. Která z následujících možností NENÍ charakteristická pro záchvat paniky?", ["intenzivní strach nebo nepříjemné pocity", "může trvat několik dní", "pocit bezprostředního nebezpečí", "vyskytují se několikrát týdně nebo měsíčně"], 1],
    ["38. Výskyt spontánních záchvatů paniky souvisí s", ["chronologickým věkem.", "pubertální fází.", "kognitivním vývojovým stadiem.", "vývojem internalizované řeči."], 1],
    ["39. Agorafobii lze nejlépe popsat jako strach z", ["opuštění domova.", "odloučení od rodičů.", "záchvatu paniky v situacích, kdy by únik byl obtížný nebo pomoc nedostupná.", "pavouků."], 2],
    ["40. Záchvaty paniky se vyskytují přibližně u _______ dospívajících.", ["3-4 %", "8-10 %", "15-20 %", "25-30 %"], 2],
    ["41. Děti a dospívající s/se _______ mají nejnižší míru remise ze všech úzkostných poruch.", ["separační úzkostnou poruchou", "generalizovanou úzkostnou poruchou", "obsedantně-kompulzivní poruchou", "panickou poruchou"], 3],
    ["42. Která z následujících možností NENÍ základním rysem posttraumatické stresové poruchy?", ["přetrvávající opakované prožívání traumatické události", "přetrvávající podrážděnost a agitovanost", "přetrvávající vyhýbání se souvisejícím podnětům a otupení celkové reaktivity", "přetrvávající příznaky extrémního vzrušení"], 1],
    ["43. Ve srovnání s dětmi s PTSD se děti s akutní stresovou poruchou", ["rychleji zotavují.", "zažívají méně závažné stresory.", "vykazují v pozdějším věku problémy s chováním.", "mají méně zdrojů podpory."], 0],
    ["44. Nejméně pravděpodobná je diagnóza deprese u", ["sociální fobie.", "specifická fobie.", "generalizované úzkostné poruchy.", "separační úzkostné poruchy."], 1],
    ["45. Ve většině případů", ["úzkost předchází depresi.", "deprese předchází úzkost.", "se deprese a úzkost vyskytují současně.", "není mezi úzkostí a depresí jasný vztah."], 0],
    ["46. Ve srovnání s úzkostnými dětmi vykazují děti s depresí", ["více negativní afektivity.", "menší negativní afektivitu.", "více pozitivní afektivity.", "méně pozitivní afektivity."], 3],
    ["47. U žen se příznaky úzkosti vyskytují _______ u mužů.", ["dvakrát častěji než", "s menší pravděpodobností než", "s mírně vyšší pravděpodobností než", "se stejnou pravděpodobností jako"], 0],
    ["48. Dětská psychopatologie odráží kombinaci skutečné/skutečného _______ dítěte a _______, skrze které se na něj dívají ostatní v kultuře dítěte.", ["symptomu, struktury", "poruchy, zaměření", "chování, perspektivy", "chování, behaviorálního rámce"], 3],
    ["49. Dvoufaktorová teorie vysvětluje, že úzkostné poruchy vznikají a přetrvávají v důsledku kombinace", ["teorie attachmentu a sociálního učení.", "temperamentu a expozice.", "klasického a operantního podmiňování.", "modelování a posilování."], 2],
    ["50. Děti s plachým a zdrženlivým temperamentem mohou mít menší pravděpodobnost, že se u nich později vyvine úzkostná porucha, pokud", ["je rodiče chrání před stresujícími událostmi.", "jim rodiče stanoví pevné hranice, které je naučí, jak se vyrovnat se stresem.", "mají starší sourozence.", "rodiče ignorují jejich žádosti o útěchu a ochranu."], 1],
    ["51. Výsledky studií úzkosti u dětí a dospívajících, které byly provedeny na dvojčatech a při adopcích, naznačují, že genetický podíl úzkosti", ["se s věkem snižuje a je větší u chlapců než u dívek.", "klesá s věkem a je větší u dívek než u chlapců.", "s věkem se zvyšuje a je větší u chlapců než u dívek.", "s věkem se zvyšuje a je větší u dívek než u chlapců."], 3],
    ["52. Mozkový systém spojený s úzkostí se nazývá", ["behaviorální aktivační systém.", "behaviorální inhibiční systém.", "behaviorální formační systém.", "hypotalamický systém."], 1],
    ["53. Neurotransmiterový systém, který se nejčastěji podílí na vzniku úzkostných poruch, je _______ systém.", ["dopaminergní", "nordopaminergní", "GABA-erginí", "prominergní"], 2],
    ["54. Dlouhodobé vystavení ________ v důsledku raného stresu nebo traumatu může mít neurotoxické účinky na vyvíjející se mozek.", ["kortizolu", "serotoninu", "GABA", "norepinefrinu"], 0],
    ["55. Úzkost je spojena s", ["výchovnými postupy.", "vazbou mezi rodičem a dítětem.", "fungováním rodiny.", "platí vše výše uvedené"], 3],
    ["56. Rodičovský styl, který je nejčastěji spojován s úzkostnými poruchami u dětí, je takový, při kterém jsou rodiče", ["neangažovaní.", "příliš kontrolující.", "příliš tolerantní.", "příliš pozitivní."], 1],
    ["57. Ve většině behaviorálních terapií zaměřených na snížení úzkosti a strachu dětí se používá/používají", ["kognitivní techniky.", "zapojení rodiny.", "podávání léků.", "prezentování obavného podnětu."], 3],
    ["58. Nejúčinnější léčba fobie dítěte z jízdy v autě zahrnuje", ["hraní si s autíčky.", "sledování nahrávek jiných dětí, které jezdí v autě.", "představování si jízdy v autě.", "skutečnou jízdu v autě."], 3],
    ["59. Nejúčinnějším postupem při léčbě většiny úzkostných poruch je", ["behaviorální terapie.", "kognitivně-behaviorální terapie.", "rodinná terapie.", "užívání léků."], 1],
    ["60. Dosud nejsilnější důkazy o účinnosti medikace při léčbě úzkostných poruch u dětí a dospívajících se týkají", ["generalizované úzkostné poruchy.", "panické poruchy.", "obsedantně-kompulzivní poruchy.", "sociální fobie."], 2]
    ],
        "AUTISMUS": [
            ["1. Leo Kanner považoval za základní rysy raného dětského autismu", ["absenci řeči.", "potřebu monotónnosti.", "stereotypní chování.", "absenci sociálních interakcí."], 3],
    ["2. Rané teorie autismu připisovaly chování autistického dítěte", ["biologickým abnormalitám mozku.", "neschopnosti integrovat smyslové podněty.", "přání rodičů, aby se dítě bylo bývalo nenarodilo.", "chybění podnětného prostředí."], 2],
    ["3. Pro stanovení diagnózy autismu podle MKN-10 musí být první příznaky patrné před dosažením věku", ["1 roku.", "3 let.", "5 let.", "7 let."], 1],
    ["4. Které z následujících tvrzení o autismu je pravdivé?", ["Autismus je vývojová porucha.", "Autismus patří mezi poruchy autistického spektra.", "Autismus je závažná porucha.", "Všechna uvedená tvrzení jsou pravdivá."], 3],
    ["5. Které z následujících tvrzení o sociálních dovednostech dětí s autismem je pravdivé?", ["Děti s autismem mají výrazné potíže ve vztazích s ostatními, i když mají průměrnou či nadprůměrnou inteligenci.", "Děti s autismem mají potíže ve vztazích pouze tehdy, pokud mají podprůměrnou inteligenci.", "Děti s autismem mají potíže ve vztazích jen tehdy, pokud mají zároveň mentální retardaci.", "Děti s autismem mají potíže ve vztazích pouze v případě podprůměrné inteligence a absence funkční řeči."], 0],
    ["6. Děti, u nichž byl/a/o diagnostikován/a/o _______ mají potíže s rozpoznáváním výrazů v obličeji.", ["deprese", "autismus", "ADHD", "úzkostná porucha"], 1],
    ["7. Sdílená sociální pozornost označuje schopnost", ["komunikovat se dvěma lidmi současně.", "koordinovat zaměření pozornosti na jinou osobu a na objekt společného zájmu.", "vést rozhovor na dvě různá témata.", "věnovat pozornost rozhovoru, který vedou dva jiní lidé."], 1],
    ["8. Pokud jde o navazování vztahů, většina dětí s autismem", ["si nevytváří smysluplné sociální vazby k rodičům.", "si vytváří nahodilé vazby k jakémukoli dospělému.", "si nevytváří vztah s žádným člověkem kromě rodičů.", "preferuje své pečovatele před neznámými dospělými."], 3],
    ["9. O emočním životě dětí s autismem nevíme, zda emoce _______ odlišně.", ["prožívají", "zpracovávají", "vyjadřují", "platí všechny výše uvedené možnosti"], 0],
    ["10. Používání protodeklarativních gest vyžaduje", ["verbální schopnosti a sdílenou sociální pozornost.", "teorii mysli a verbální schopnosti.", "teorii mysli a sdílenou sociální pozornost.", "inteligenci a sdílenou sociální pozornost."], 2],
    ["11. U _______ dětí s autismem se nerozvíjí žádný funkční jazyk.", ["všech", "většiny", "přibližně poloviny", "malého počtu"], 2],
    ["12. Děti s autismem nejčastěji používají", ["instrumentální gesta.", "expresivní gesta.", "protodeklarativní gesta.", "sdílené sociální chování."], 0],
    ["13. Předpokládá se, že echolálie u dětí s autismem jsou", ["znakem patologie.", "projevem souběžné obsedantně-kompulzivní poruchy.", "důležitým krokem v osvojování jazyka.", "nekontrolovatelným návykem."], 2],
    ["14. Primární jazykový deficit u dětí s autismem (které si jazyk postupně osvojují) se týká především", ["používání gramatiky.", "sémantiky.", "používání morfologie.", "pragmatiky."], 3],
    ["15. Tradiční inteligenční testy, jako například WISC, mohou _______ intelektuální fungování dětí s autismem.", ["podhodnocovat", "uměle nadhodnocovat", "podávat stereotypní obraz", "přesně odrážet"], 0],
    ["16. Autostimulační chování u dětí s autismem může být způsobeno tím, že", ["touží po stimulaci, a autostimulace slouží k dráždění jejich nervového systému.", "prostředí je pro ně příliš podnětné, a autostimulace pomáhá blokovat či regulovat nežádoucí vjemy.", "bývá často doprovázeno nějakým druhem posílení.", "platí kterákoli z uvedených možností"], 3],
    ["17. Speciální kognitivní schopnosti, které výrazně přesahují běžnou úroveň intelektu dítěte s autismem i průměr běžné populace, se označují jako", ["savantské schopnosti", "ostrůvkovité schopnosti", "makroschopnosti", "nadpřirozené schopnosti"], 1],
    ["18. Tendence zaměřovat se pouze na jeden rys objektu v prostředí a ignorovat přitom další stejně významné vlastnosti se nazývá stimulová/stimulový", ["dominance.", "specializace.", "screening.", "nadselektivita."], 3],
    ["19. Upřednostňování určitých typů smyslových vjemů před jinými se označuje jako senzorická/senzorický", ["dominance.", "specializace.", "screening.", "nadselektivita."], 0],
    ["20. Hypotéza teorie mysli u autismu předpokládá, že děti s autismem", ["se soustředí pouze na jeden rys objektu v prostředí, zatímco ignorují další stejně důležité znaky.", "nerozumí duševním stavům druhých.", "nejsou schopné vytvořit si celkový obraz kvůli tendenci soustředit se na detail.", "nejsou schopné rozdělit svou sociální pozornost v sociálních situacích."], 1],
    ["21. Osoba postrádající centrální koherenci", ["zpracovává informace po částech a po kouscích, nedokáže však nevnímat celek.", "nerozumí duševním stavům ostatních.", "nedokáže koordinovat pohyby pravé a levé poloviny těla.", "nechápe společenskou hierarchie."], 0],
    ["22. Pokud byste administrovali test WISC dítěti s autismem, která z následujících podškál by s největší pravděpodobností způsobila dítěti nejvíce obtíží?", ["Opakování čísel", "Kostky", "Porozumění", "Všechny uvedené podškály by byly pro dítě přibližně stejně náročné"], 2],
    ["23. Děti s autismem často trpí problémy spojenými s", ["vzorcem spánek-bdění.", "gastrointestinálními obtížemi.", "vybíravostí ve stravování.", "všemi výše uvedenými obtížemi"], 3],
    ["24. Nejcharakterističtějším kognitivním deficitem u dětí s autismem je", ["oslabená centrální koherence.", "deficity exekutivních funkcí.", "nedostatečná teorie mysli.", "senzorická nadselektivita."], 2],
    ["25. Mnoho dětí s autismem má současně", ["mentální retardaci a epilepsii.", "nadprůměrnou inteligenci.", "schizofrenii.", "mentální retardaci a schizofrenii."], 0],
    ["26. Nejpravděpodobnějším obdobím nástupu epilepsie u dětí s autismem je", ["kojenecký věk.", "mladší školní věk.", "adolescence.", "dospělost."], 2],
    ["27. _______ u některých dětí s autismem je odlišuje/odlišují od dětí s mentální retardací či poruchou řeči.", ["Nízko posazené uši", "Abnormálně zvětšený obvod hlavy", "Zploštělý kořen nosu", "Široce posazené oči"], 1],
    ["28. Dítě s mentální retardací, ale bez autismu, má vyšší pravděpodobnost projevu _______ než dítě s autismem.", ["sebepoškozujícího chování", "očního kontaktu a úsměvu", "stereotypního motorického chování", "autostimulačního chování"], 1],
    ["29. Děti s vývojovými jazykovými poruchami mají menší pravděpodobnost obtíží v oblasti _______ ve srovnání s dětmi s autismem.", ["osvojování jazyka", "délky hovoru", "spontánní sociální konverzace", "gramatické složitosti"], 2],
    ["30. Nejnovější odhady prevalence autismu udávají výskyt přibližně", ["1 dítě z 1 000.", "1 dítě z 500.", "1 dítě z 250.", "1 dítě ze 150."], 3],
    ["31. Nárůst prevalence autismu je s největší pravděpodobností způsoben", ["rozšířením diagnostických kritérií.", "lepším rozpoznáváním mírnějších forem autismu.", "zvýšeným povědomím a screeningem v raném věku.", "všemi výše uvedenými faktory"], 3],
    ["32. Které z následujících tvrzení o genderových rozdílech v rámci autismu je pravdivé?", ["Autismus se vyskytuje stejně často u chlapců i dívek.", "Autismus je častější u chlapců.", "Autismus je častější u chlapců, s výjimkou jedinců s těžkou mentální retardací, kde je poměr pohlaví vyrovnanější.", "Autismus je častější u chlapců, s výjimkou osob s průměrným nebo nadprůměrným IQ, kde je poměr chlapců a dívek podobný."], 2],
    ["33. Dnes již obsoletní „Teorie extrémního mužského mozku“ snažící se vysvětlit autismus předpokládala, že", ["mozky osob s autismem jsou více „systematizující“.", "mozky osob s autismem jsou méně „systematizující“.", "ženy jsou více systematické.", "muži jsou více empatičtí."], 0],
    ["34. Deficity zapříčiněné autismem se s rostoucí mírou projevují", ["již od narození.", "přibližně od 6 měsíců věku.", "kolem 2. roku života.", "při nástupu dítěte do školy."], 2],
    ["35. Dva nejvýznamnější prediktory úspěšnosti v dospělosti u dětí s autismem jsou", ["absence stereotypního chování a teorie mysli.", "úroveň IQ a rozvoj jazyka.", "citlivý přístup rodičů a včasná intervence.", "intaktní motorické dovednosti a senzorická specializace."], 1],
    ["36. Americká pediatrická akademie (AAP) doporučuje, že dítě by mělo podstoupit screening na autismus ve věku _______.", ["12 měsíců", "15 měsíců", "12 a 24 měsíců", "18 a 24 měsíců"], 3],
    ["37. Ze všech onemocnění je s autismem nejčastěji spojován/a _______.", ["Tuberózní skleróza", "Downův syndrom", "Fenylketonurie (PKU)", "Syndrom fragilního X"], 0],
    ["38. Příbuzní dětí s autismem vykazují zvýšený výskyt", ["echolálií.", "mentální retardace.", "pragmatických jazykových obtíží.", "všech výše uvedených"], 2],
    ["39. Přibližně _______ procent rodičů dětí s autismem věří, že MMR vakcíny, rtuť (thimerosal) ve vakcínách a/nebo zvýšený počet očkování v dětství měly za následek vznik autismu u jejich dítěte.", ["deset", "dvacet pět", "padesát", "sedmdesát pět"], 2],
    ["40. Nejčastěji spojovaný neurotransmiter s autismem je", ["serotonin.", "dopamin.", "noradrenalin.", "GABA."], 0],
    ["41. Dr. Ivar Lovaas je nejvíce známý díky své práci na vývoji", ["programu TEACCH.", "metody Floor Time.", "aplikované behaviorální analýzy (ABA).", "terapie zaměřené na klíčové reakce (PRT)."], 2],
    ["42. Metoda postupného předkládání podnětů (stimulů) a vyžadování specifických odpovědi používaná při terapii autismu se nazývá", ["trénink jemných pokusů.", "trénink odpovědí.", "metoda podnět–reakce.", "trénink diskrétních pokusů."], 3],
    ["43. _______ posiluje chování pomocí přirozeně se vyskytujících příležitostí.", ["Naturalistický trénink", "Trénink diskrétních pokusů", "Náhodný trénink", "Trénink klíčových reakcí"], 2],
    ["44. Účinnost včasné intervence u autismu vychází především z", ["pravděpodobnosti, rodiče ještě nebyli odrazeni.", "pravděpodobnosti, že se ještě nevyvinulo obtěžující a rušivé chování.", "ochoty malých dětí zavděčit se dospělým.", "plasticity nervového systému v raném dětství."], 3],
    ["45. Projekt UCLA Young Autism Project se snaží zmírnit příznaky autismu prostřednictvím", ["napodobování dětí, jakmile začnou produkovat perseverativním chování.", "využívání technik modifikace chování, jako je odměňování a tvarování.", "umístění dětí do strukturovaného prostředí mimo domov.", "používání elektrických šoků."], 1],
    ["46. Na rozdíl od dětí s autismem děti s Aspergerovým syndromem", ["nevykazují postižení v sociální oblasti.", "nevykazují omezené zájmy.", "projevují větší zájem o sociální interakce.", "vykazují menší opoždění ve vývoji jazyka."], 2],
    ["47. Které z následujících tvrzení o Rettově syndromu je NEPRAVDIVÉ?", ["Rettův syndrom je obecně považován za poruchu postihující dívky.", "Děti s Rettovým syndromem obvykle procházejí obdobím normálního prenatálního a raného postnatálního vývoje během prvních 6 až 12 měsíců života.", "Děti s Rettovým syndromem vykazují zpomalený růst obvodu hlavy.", "Ve srovnání s dětmi s autismem nevykazují děti s Rettovým syndromem poruchy řeči."], 3],
    ["48. Dvacet pět procent dětí s _______ možná nikdy nezačne chodit a přibližně polovina z těch, které chůzi zvládnou, tuto schopnost později ztratí.", ["autismem", "Aspergerovým syndromem", "Rettovým syndromem", "dětskou dezintegrační poruchou"], 2],
    ["49. Čtyřletý Lukáš vykazuje výraznou ztrátu dříve osvojených dovedností po období zdánlivě normálního vývoje. Lukášovi bude s největší pravděpodobností diagnostikován/a", ["porucha autistického spektra.", "Aspergerův syndrom.", "dětská dezintegrační porucha.", "Rettův syndrom."], 2]
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











