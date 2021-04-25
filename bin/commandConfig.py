from string import Template


# 'command Name':{
#   'answer': 'some text',
#   'function': 'function()',
#   'delay': 5,
#}


commands = {
    'private': {
    },
    'guild':{
        'usual': {
            '!помощь':{
                'answer': 'Готово',
                'function': 'asyncio.run_coroutine_threadsafe(helpCommand(self, message), self.loop)',
                'delay': 1,
            },
            '!создать':{
                'answer': 'Готово',
                'function': 'asyncio.run_coroutine_threadsafe(createRequest(self, message, command), self.loop)',
                'delay': 1,
            },
            '!np':{
                'answer': 'self.musicPlayer.nowPlay()',
                'function': None,
                'delay': 5,
            },
            '!q':{
                'answer': 'self.musicPlayer.query()',
                'function': None,
                'delay': 60,
            },
        },
        'music': {
            '!p':{
                'answer': 'Добавила песенку в плейлист',
                'function': 'self.musicPlayer.play(msg, command)',
                'delay': 5,
            },
            '!pause':{
                'answer': 'Поставила на паузу',
                'function': 'self.musicPlayer.pauseAudio()',
                'delay': 5,
            },
            '!r':{
                'answer': 'Поставила дальше играть',
                'function': 'self.musicPlayer.resume()',
                'delay': 5,
            },
            '!stop':{
                'answer': 'Остановила и очистила',
                'function': 'self.musicPlayer.stop()',
                'delay': 5,
            },
            '!shuffle':{
                'answer': 'Перемешала',
                'function': 'self.musicPlayer.shuffle()',
                'delay': 5,
            },
            '!s':{
                'answer': 'self.musicPlayer.skip()',
                'function': None,
                'delay': 5,
            },
            '!repeat':{
                'answer': 'self.musicPlayer.repeat(msg)',
                'function': None,
                'delay': 5,
            },
        },
        'token': {
            '!монета':{
                'answer': 'self.token.addToken(self, msg.split(command)[1].strip())',
                'function': None,
                'delay': 10,
            },
            '!немонета':{
                'answer': 'self.token.removeToken(self, msg.split(command)[1].strip())',
                'function': None,
                'delay': 5,
            },
            '!монеты':{
                'answer': 'self.token.viewToken(self)',
                'function': None,
                'delay': 60,
            },
        },
        'moviegoers':{
            '!удалить':{
                'answer': 'Удалила',
                'function': 'asyncio.run_coroutine_threadsafe(removeSession(self, msg), self.loop)',
                'delay': 5,
            },
        },
        'my':{
            '!connect':{
                'answer': 'Подключилась',
                'function': 'asyncio.run_coroutine_threadsafe(self.musicPlayer.connect(self.client, msg, command), self.loop)',
                'delay': 5,
            },
        }

    }
}

texts = {
    'cock': '<:YEP:771044606913151002> COCK',
    'глоськ': '<:Huggu:832641068355813376>',
    'ёка': '<:pepoHappyHug:832270928830136381>',
    'йока': '<:hack:835971292481847356>',
    'бава': '<:pepeW:835965188825153546>',
    'гвин': '<:peepoHappy:785159818901192704>',
    'сили': '<:eulaLove:823858744844091412>',
    'айня': '<:peepoAweSome:835965240567005245>',
    'кешб': '<:peepoPolice:835970576140730409>',
    'трин': '<:Jebaited:835970645920972831>',
    'синг': '<:peepoSadSwipe:835970920598339614>',
    'пепус': '<:peepoFat:835970987597496330>',
    #'': '',
    #'': '',
}
#'': '',
#сначала проверка на функцию, если функция есть, то ивал её, если нет, то ответ евал ансвера
