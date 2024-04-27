from datetime import datetime

from .models import User, Animal, Role, Walk


animals = [
    {'name': 'Jack', 'species': 'Dog', 'age': 5, 'description': 'nice dog', 'image': 'https://pettownsendvet.com/wp-content/uploads/2023/01/iStock-1052880600-1024x683.jpg'},
    {'name': 'Whiskers', 'species': 'Cat', 'age': 3, 'description': 'playful kitty', 'image': 'https://www.thespruce.com/thmb/PrfluQWFB8RhXABxIUeN5nNHrIo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/discourage-feral-cats-386479-hero-50eeb16535844e75853d52720baeaec5.jpg'},
    {'name': 'Buddy', 'species': 'Dog', 'age': 7, 'description': 'friendly companion', 'image': 'https://media.posterlounge.com/img/products/700000/691873/691873_poster.jpg'},
    {'name': 'Mittens', 'species': 'Cat', 'age': 1, 'description': 'curious kitten', 'image': 'https://w0.peakpx.com/wallpaper/129/511/HD-wallpaper-cute-little-kitty-cute-little-kitty-cats-animals.jpg'},
    {'name': 'Sammy', 'species': 'Hamster', 'age': 2, 'description': 'quick little guy', 'image': 'https://upload.wikimedia.org/wikipedia/commons/c/cd/Peach_the_pet_hamster.jpg'},
    {'name': 'Luna', 'species': 'Rabbit', 'age': 4, 'description': 'gentle giant', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Oryctolagus_cuniculus_Rcdo.jpg/1200px-Oryctolagus_cuniculus_Rcdo.jpg'},
    {'name': 'Sasha', 'species': 'Cat', 'age': 9, 'description': 'regal feline', 'image': 'https://www.thesprucepets.com/thmb/Wy9Vno45XeFtos7omJ80qkZrtZc=/3760x0/filters:no_upscale():strip_icc()/GettyImages-174770333-0f52afc06a024c478fafb1280c1f491f.jpg'},
    {'name': 'Toby', 'species': 'Rabbit', 'age': 7, 'description': 'friendly fellow', 'image': 'https://cdn.britannica.com/20/194520-050-DCAE62F1/New-World-Sylvilagus-cottontail-rabbits.jpg'},
]

users = [
    {'name': 'NOTANADMIN', 'role': Role.admin},
    {'name': 'ADMIN', 'role': Role.user},
    {'name': 'volunteer', 'role': Role.volunteer},
]

async def test():
    for user in users:
        await User.add(User(**user))
    me = (await User.all())[0]
    for animal in map(lambda a: Animal(**a), animals):
        await Animal.add(animal)
        await Walk.add(Walk(date=datetime.now(), duration=30, animal=animal, user=me))
