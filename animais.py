def div():
    print('xX------------------------------------------------xX')


div()
print('Bem-vindo à minha enciclopédia sobre animais!\n'
      'Escolha um número referente à um animal que\nvocê queira saber sobre.\n')
print('fontes: www.wikipedia.org\n')
print('1. Cachorro\n2. Gato\n3. Cavalo\n4. Urso')
div()
escolha = int(input('# '))

if escolha == 1:
    print('O cão (nome científico: Canis lupus familiaris), também chamado de cachorro, é um\n'
          'mamífero carnívoro da família dos canídeos, subespécie do lobo, e talvez o mais antigo\n'
          'animal domesticado pelo ser humano. Teorias postulam que surgiu do lobo cinzento no\n'
          'continente asiático há mais de 100 000 anos. Ao longo dos séculos, através da domesticação,\n'
          'o ser humano realizou uma seleção artificial dos cães por suas aptidões, características\n'
          'físicas ou tipos de comportamento. O resultado foi uma grande diversidade de\n'
          'raças caninas, as quais variam em pelagem e tamanho dentro de suas próprias\n'
          'raças, atualmente classificadas em diferentes grupos ou categorias.\n'
          'As designações vira-lata ou rafeiro são dadas aos cães sem raça definida\n'
          'ou mestiços descendentes.')
elif escolha == 2:
    print('O gato (nome científico: Felis silvestris catus) é um mamífero carnívoro da família dos felídeos,\n'
          'muito popular como animal de estimação. Ocupando o topo da cadeia alimentar, é predador natural de\n'
          'diversos animais, como roedores, pássaros, lagartixas e alguns insetos. Segundo pesquisas\n'
          'realizadas por instituições norte-americanas, os gatos consistem no segundo animal de estimação mais\n'
          'popular do mundo, estando numericamente atrás apenas dos peixes de aquário.')
elif escolha == 3:
    print('O cavalo (Equus ferus caballus) é uma das duas subespécies existentes de Equus ferus. É um mamífero\n'
          'perissodáctilo pertencente à família taxonômica Equidae. O cavalo evoluiu há entre 45 milhões a 55\n'
          'milhões de anos, desde uma pequena criatura com vários dedos, o Eohippus, até o animal grande e com um\n'
          'único dedo de hoje. Os seres humanos começaram a domesticar cavalos por volta de 4000 a.C.\n'
          'e acredita-se que sua domesticação tenha sido disseminada em 3000 a.C. Os cavalos da subespécie\n'
          'caballus são domesticados, embora algumas populações domesticadas vivam na natureza como cavalos\n'
          'selvagens. Essas populações selvagens não são verdadeiros cavalos "selvagens", pois esse termo é\n'
          'usado para descrever cavalos que nunca foram domesticados, como o cavalo de Przewalski, uma\n'
          'espécie em perigo de extinção, uma subespécie separada e o único verdadeiro cavalo selvagem restante\n'
          'na natureza. Existe um vocabulário extenso e especializado usado para descrever conceitos relacionados\n'
          'a equinos, cobrindo de tudo, desde anatomia a estágios da vida, tamanho, cores, marcações, raças, '
          'locomoção e comportamento. ')
elif escolha == 4:
    print('Os Ursos (latim científico: Ursidae) constituem uma família de mamíferos carnívoros de grande porte,\n'
          'contendo os ursos e os pandas. Eles são classificados como caníformes ou carnivoros caninos. Os ursos são\n'
          'encontrados nos continentes da América do Norte, América do Sul, Europa e Ásia. As características comuns\n'
          'dos ursos modernos incluem corpos grandes com pernas atarracadas, focinhos longos, orelhas pequenas\n'
          'e arredondadas, cabelos desgrenhados, patas plantígradas com cinco garras não retráteis e caudas curtas. ')
