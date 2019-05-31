

def get_triplets_list():
    words_triples_list = [['man', 'woman', 'king'],
                          ['sansa', 'stark', 'jaime'],  #lannister
                          ['jaime', 'cersei', 'jon'],  #'bran', 'ned', 'theon', 'rickon', 'rob'
                          ['jaime', 'cersei', 'arya'],  #sansa
                          ['tywin', 'tyrion', 'ned'],  #arya
                          ['valar', 'morghulis', 'valar'],  #dohaeris
                          ['catelyn', 'brienne', 'tyrion'],  #bronn
                          ['brienne', 'catelyn', 'bronn'],  #tyrion # NOT simetric relation!
                          ['valyrian', 'steel', 'dornish'],  #wine
                          ['he', 'eat', 'she'],  #fuck
                          ['baelish', 'littlefinger', 'daenerys'],  # dany
                          ['westeros', 'qyburn', 'winterfell'],  # luwin
                          ['westeros', 'pycelle', 'winterfell'],  # luwin
                          ['qyburn', 'westeros', 'luwin'],  # winterfell
                          ['pycelle', 'westeros', 'luwin'],  # winterfell
                          ['luwin', 'winterfell', 'qyburn'],  # westeros
                          ['luwin', 'winterfell', 'pycelle'],  # westeros
                          ['winterfell', 'luwin', 'westeros'],  # qyburn, pycelle
                          ['ghost', 'jon', 'nymeria'],  # arya
                          ['jon', 'ghost', 'arya'],  # nymeria
                          ['arya', 'nymeria', 'jon'],  # ghost
                          ['nymeria', 'arya', 'ghost'],  # jon
                          ['sansa', 'lady', 'jon'],  # lord
                          ['daenerys', 'khaleesi', 'cersei'],  # mlady
                          ['ned', 'robert', 'tywin'],  # joffrey
                          ['jon', 'fighting', 'tyrion'],  # joffrey
                          ['ned', 'fighting', 'tyrion'],  # joffrey
                          ['cloaks', 'gold', 'night'],  # #watch
                          ['cloaks', 'janos', 'crows'],  # #watch
                          ['crows', 'mormont', 'cloaks'],  # #watch
                          ['watch', 'mormont', 'cloaks'],  # #watch
                          ['mormont', 'crows', 'janos'],  # #watch
                          ['mormont', 'watch', 'janos'],  # #watch
                          ['cloaks', 'janos', 'crows'],  # #watch
                          ['cloaks', 'janos', 'watch'],  # #watch
                          ['crows', 'watch', 'gold'],  # #landing
                          ['crows', 'watch', 'cloak'],  # #landing
                          ['cloaks', 'landing', 'watch'],  # joffrey
                          ['robert', 'fighting', 'tyrion'],  # joffrey
                          ['petyr', 'catelyn', 'jorah'],  # dany
                          ['jon', 'north', 'cersei'],  # landing, kingdoms (AKA king's landing)
                          ['jon', 'north', 'daenerys'],  # westeros, meereen, yunkai
                          ['brienne', 'catelyn', 'hodor'],  # bran, rickon
                          ['mountain', 'hound', 'jon'],  # theon, arya



                          # tests of nicknames
                          ['imp', 'tyrion', 'littlefinger'],  #baelish, pyter
                          ['dwarf', 'tyrion', 'littlefinger'],  #baelish, pyter
                          ['baelish', 'littlefinger', 'tyrion'],  #imp, dwarf
                          ['tyrion', 'imp', 'baelish'],  #littlefinger
                          ['tyrion', 'dwarf', 'baelish'],  #littlefinger
                          ['daenerys', 'khaleesi', 'joffrey'],  #mlady
                          ['robert', 'ned', 'joffrey'],  #tywin
                          ['daenerys', 'jorah', 'catelyn'],  #petyr
                          ['jorah', 'daenerys', 'petyr'],  #catelyn



                          ['white', 'walker', 'black'],  #westeros, meereen, yunkai
                          ['stannis', 'baratheon', 'robb'],  #stark
                          ['mountain', 'hound', 'jon'],  #theon, arya
                          ['baelish', 'littlefinger', 'clegane'],  # hound
                          ['littlefinger', 'baelish', 'onion'],  # davos
                          ['petyr', 'littlefinger', 'sandor'],  # hound
                          ['petyr', 'littlefinger', 'clegane'],  # hound
                          ['gregor', 'mountain', 'sandor'],  # hound
                          ['clegane', 'hound', 'clegane'],  # mountain
                          ['clegane', 'hound', 'jon'],  # mountain
                          ['clegane', 'mountain', 'clegane'],  # hound
                          ['littlefinger', 'baelish', 'hound'],  # clegane
                          ['tyrion', 'imp', 'sandor'],  # clegane
                          ['tyrion', 'imp', 'clegane'],  # clegane
                          ['jon', 'king', 'davos'],  # ser
                          ['stannis', 'king', 'davos'],  # ser
                          ['davos', 'ser', 'jon'],  # king

                          # Bastard
                          ['gendry', 'robert', 'jon'],  # ned
                          ['robert', 'gendry', 'ned'],  # jon
                          ['gendry', 'baratheon', 'jon'],  # stark
                          ['baratheon', 'gendry', 'stark'],  # jon
                          ['ned', 'jon', 'robert'],  # gendry
                          ['jon', 'ned', 'gendry'],  # robert
                          ['jon', 'stark', 'gendry'],  # baratheon


                          ['gendry', 'bastard', 'jon'],
                          ['bastard', 'gendry', 'bastard'],
                          ['bastard', 'jon', 'bastard'],
                          ['bastard', 'ramsay', 'bastard'],
                          ['ramsay', 'bolton', 'gendry'],  # baratheon
                          ['ramsay', 'roose', 'gendry'], # baratheon(weak)
                          ['ramsay', 'roose', 'gendry'], # baratheon(weak)
                          ['ramsay', 'roose', 'jon'],  # ned
                          ['roose', 'ramsay', 'robert'],  # gendry
                          ['robert', 'gendry', 'roose'],  # gendry
                          ['gendry', 'robert', 'ramsay'],  # boltons(weak),
                          ['jon', 'ned', 'ramsay'],  # boltons(weak), roose(strong) - V
                          ['jon', 'ned', 'gendry'],  # robert

                            # Treatment to bastars

                          # """
                          # Due to its unique history and culture, bastards in Dorne are not looked down upon the way they are in the rest of the Seven Kingdoms.
                          # """
                          ['landing', 'bastard', 'dorne'],  # something bad
                          ['dorne', 'bastard', 'landing'],  # something good

                          ['winterfell', 'bastard', 'dorne'],  # something bad
                          ['dorne', 'bastard', 'winterfell'],  # something good

                          ['gendry', 'robert', 'ramsay'],  # boltons(weak), roose - V
                          ['robert', 'gendry', 'roose'],  # boltons(weak), ramsay - V

                          ['jon', 'ned', 'ramsay'],  # boltons(weak), roose(strong) - V
                          ['jon', 'ned', 'roose'],  # boltons(weak), ramsay(strong) - V

                          # ['khaleesi', 'daenerys', 'jon'],

                          ]
    return words_triples_list


def get_adjective_list():
    adjectives_list = ['bitch', 'fucker','fucked', 'sexy', 'pretty', 'ugly', 'killer', 'fighter', 'strong', 'thankless', 'tactful', 'distrustful', 'quarrelsome', 'effeminate', 'fickle',
                       'talkative', 'dependable', 'resentful', 'sarcastic', 'unassuming', 'changeable', 'resourceful',
                       'persevering', 'forgiving', 'assertive', 'individualistic', 'vindictive', 'sophisticated',
                       'persevering', 'forgiving', 'assertive', 'individualistic', 'vindictive', 'sophisticated',
                       'deceitful', 'impulsive', 'sociable', 'methodical', 'idealistic', 'thrifty', 'outgoing',
                       'intolerant', 'autocratic', 'conceited', 'inventive', 'dreamy', 'appreciative', 'forgetful',
                       'forceful', 'submissive', 'pessimistic', 'versatile', 'adaptable', 'reflective', 'inhibited',
                       'outspoken', 'quitting', 'unselfish', 'immature', 'painstaking', 'leisurely', 'infantile', 'sly',
                       'praising', 'cynical', 'irresponsible', 'arrogant', 'obliging', 'unkind', 'wary', 'greedy',
                       'obnoxious', 'irritable', 'discreet', 'frivolous', 'cowardly', 'rebellious', 'adventurous',
                       'enterprising', 'unscrupulous', 'poised', 'moody', 'unfriendly', 'optimistic', 'disorderly',
                       'peaceable', 'considerate', 'humorous', 'worrying', 'preoccupied', 'trusting', 'mischievous',
                       'robust', 'superstitious', 'noisy', 'tolerant', 'realistic', 'masculine', 'witty', 'informal',
                       'prejudiced', 'reckless', 'jolly', 'courageous', 'meek', 'stubborn', 'aloof', 'sentimental',
                       'complaining', 'unaffected', 'cooperative', 'unstable', 'feminine', 'timid', 'retiring',
                       'relaxed', 'imaginative', 'shrewd', 'conscientious', 'industrious', 'hasty', 'commonplace',
                       'lazy', 'gloomy', 'thoughtful', 'dignified', 'wholesome', 'affectionate', 'aggressive',
                       'awkward', 'energetic', 'tough', 'shy', 'queer', 'careless', 'restless', 'cautious', 'polished',
                       'tense', 'suspicious', 'dissatisfied', 'ingenious', 'fearful', 'daring', 'persistent',
                       'demanding', 'impatient', 'contented', 'selfish', 'rude', 'spontaneous', 'conventional',
                       'cheerful', 'enthusiastic', 'modest', 'ambitious', 'alert', 'defensive', 'mature', 'coarse',
                       'charming', 'clever', 'shallow', 'deliberate', 'stern', 'emotional', 'rigid', 'mild', 'cruel',
                       'artistic', 'hurried', 'sympathetic', 'dull', 'civilized', 'loyal', 'withdrawn', 'confident',
                       'indifferent', 'conservative', 'foolish', 'moderate', 'handsome', 'helpful', 'gentle',
                       'dominant', 'hostile', 'generous', 'reliable', 'sincere', 'precise', 'calm', 'healthy',
                       'attractive', 'progressive', 'confused', 'rational', 'stable', 'bitter', 'sensitive',
                       'initiative', 'loud', 'thorough', 'logical', 'intelligent', 'steady', 'formal', 'complicated',
                       'cool', 'curious', 'reserved', 'silent', 'honest', 'quick', 'friendly', 'efficient', 'pleasant',
                       'severe', 'peculiar', 'quiet', 'weak', 'anxious', 'nervous', 'warm']
    return adjectives_list


def get_man_and_woman_words_list():
    woman_words_list = ['she', 'daughter', 'hers', 'her', 'mother', 'woman', 'girl', 'herself', 'female', 'sister',
                        'daughters', 'mothers', 'women', 'girls',
                        'femen', 'sisters', 'aunt', 'aunts', 'niece', 'nieces']

    man_words_list = ['he', 'son', 'his', 'him', 'father', 'man', 'boy', 'himself', 'male', 'brother', 'sons',
                      'fathers', 'men', 'boys', 'males', 'brothers', 'uncle',
                      'uncles', 'nephew', 'nephews']
    return woman_words_list, man_words_list