# WordleBotES
A wordle bot that solves the game in spanish.

Run the Front.py file to run the interface.

The bot will recommend a word to play, then you have to put the wordle values returned with that word on the program and then the bot will recomend another word to play.

# How it works?

WordleBot will always start with the world "TARES" which was calculated beforehand using the same principles applied for the rest of the bot. The bot removes all the non feasible answers depending on the colors given to that first word. Then, it will recover the word with the highest entropy and choose it as the best option; finally it will repeat this process until the word is found.

The list of all 5 letter words was taken from https://www.listasdepalabras.es/palabras5letras.htm
