from werkzeug.security import generate_password_hash

from .database import session_factory
from .enums import AnimalStatus

from ..animal.models import Animal
from ..user.models import User

animals = [
    {'name': 'Jack', 'species': 'Dog', 'age': 5, 'description': 'nice dog', 'image': 'https://pettownsendvet.com/wp-content/uploads/2023/01/iStock-1052880600-1024x683.jpg'},
    {'name': 'Whiskers', 'species': 'Cat', 'age': 3, 'description': 'playful kitty', 'image': 'https://www.bluecross.org.uk/sites/default/files/d8/2019-03/BX143130_IMG_9778amend-lpr.jpg'},
    {'name': 'Buddy', 'species': 'Dog', 'age': 7, 'description': 'friendly companion', 'image': 'https://media.posterlounge.com/img/products/700000/691873/691873_poster.jpg', 'status': AnimalStatus.unavailable},
    {'name': 'Mittens', 'species': 'Cat', 'age': 1, 'description': 'curious kitten', 'image': 'https://w0.peakpx.com/wallpaper/129/511/HD-wallpaper-cute-little-kitty-cute-little-kitty-cats-animals.jpg'},
    {'name': 'Sammy', 'species': 'Hamster', 'age': 2, 'description': 'quick little guy', 'image': 'https://upload.wikimedia.org/wikipedia/commons/c/cd/Peach_the_pet_hamster.jpg'},
    {'name': 'Luna', 'species': 'Rabbit', 'age': 4, 'description': 'gentle giant', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/1200px-Oryctolagus_cuniculus_Rcdo.jpg'},
    {'name': 'Sasha', 'species': 'Cat', 'age': 9, 'description': 'regal feline', 'image': 'https://www.fearfreehappyhomes.com/wp-content/uploads/2020/08/catwhiskersfeatured.jpg'},
    {'name': 'Toby', 'species': 'Rabbit', 'age': 7, 'description': 'friendly fellow', 'image': 'https://cdn.britannica.com/20/194520-050-DCAE62F1/New-World-Sylvilagus-cottontail-rabbits.jpg'},
]

users = [
    {'name': 'Default admin', 'password': '123456', 'phone': '88005553535', 'is_superuser': True},
]


async def test():
    async with session_factory() as session:

        for animal in map(lambda a: Animal(**a), animals):
            session.add(animal)

        for user in users:
            user['hashed_password'] = generate_password_hash(user['password'])
            user.pop('password')
            session.add(User(**user))

        await session.commit()
