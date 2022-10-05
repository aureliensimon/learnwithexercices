"""
J'ai empilé les pommes d'or pour toi, sous la forme d'une pyramide. L'étage le plus haut ne contient qu'une pomme. L'étage juste en dessous forme un carré 2x2 (contenant 4 pommes), l'étage juste en dessous forme un carré 3x3 (contenant 9 pommes). La pyramide que tu vois contient 50 étages. L'étage de base contient donc 2 500 pommes... Je suis d'accord pour te laisser partir avec les pommes contenues dans certains étages. Précisément, si un étage contient un nombre de pommes multiple de 3, tu peux l'emporter. Si tu m'annonces combien de pommes tu emporteras au total, je te laisserai partir avec les pommes...

Pour relever ce défi, vous devez aider Hercule en lui indiquant le nombre de pommes qu'il pourra emporter. Par exemple, si la pyramide n'avait compté que 6 étages comme indiqué sur la figure suivante, chaque étage aurait été composé de : 1, 4, 9, 16, 25 et 36 pommes. Hercule aurait pu emporter les 9 pommes de l'étage 3 (car 9 est un multiple de 3) et les 36 pommes de l'étage 6 (car 36 est un multiple de 3). Au total il aurait donc emporté 45 pommes. Mais combien peut-il en emporter pour une pyramide de 50 étages ? 

"""

print(sum([i*i if not i**2 % 3 else 0 for i in range(7)]))