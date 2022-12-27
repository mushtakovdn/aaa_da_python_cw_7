class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    ICON = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __str__(self):
        text = super().__str__()
        for cat, emoji in self.ICON.items():
            replaced = text.replace(cat, emoji)
            if replaced != text:
                return replaced
        return text


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self.weaknesses = weaknesses


if __name__ == '__main__':
    base_charmander = BasePokemon(name='Charmander', category='Lizard')
    charmander = Pokemon(
        name='Charmander',
        category='Lizard',
        weaknesses=('water', 'ground', 'rock')
    )
    pikachu = Pokemon(
        name='Pikachu',
        category='electric',
        weaknesses=('honesty')
    )
    print(charmander.to_str())
    print(charmander)
    print(pikachu)
