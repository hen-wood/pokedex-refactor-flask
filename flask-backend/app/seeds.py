from .models import db, Pokemon


def seed_data():
    pikachu = Pokemon(
        number=25, 
        name='Pikachu', 
        type='electric', 
        attack=55, 
        defense=30, 
        moves= '["tackle","vine whip"]',
        image_url='/images/pokemon_snaps/25.svg'
    )

    charmander = Pokemon(
        number=4, 
        name='Charmander', 
        type='fire', 
        attack=52, 
        defense=43, 
        moves= '["tackle","vine whip"]',
        image_url='/images/pokemon_snaps/4.svg'
        )
    
    bulbasaur = Pokemon(
        number=1, 
        name='Bulbasaur', 
        type='grass',
        attack=49, 
        defense=49, 
        moves= '["tackle","vine whip"]',
        image_url='/images/pokemon_snaps/1.svg'
        )

    db.session.add(pikachu)
    db.session.add(charmander)
    db.session.add(bulbasaur)

    db.session.commit()