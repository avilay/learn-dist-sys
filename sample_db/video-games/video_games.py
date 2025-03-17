from dataclasses import dataclass
from datetime import date, datetime
import json
from typing import Any
from enum import Enum, auto


def to_date(daterepr: str) -> date:
    return datetime.strptime(daterepr, "%m/%d/%y").date()


class Genre(Enum):
    ACTION_ADVENTURE = auto()
    FIGHTING = auto()
    SHOOTER = auto()
    SIMULATION = auto()
    FAMILY_KIDS = auto()
    PUZZLE_TRIVIA = auto()
    ROLE_PLAYING = auto()

    def to_string(self):
        match self:
            case Genre.ACTION_ADVENTURE:
                return "Action & Adventure"
            case Genre.FIGHTING:
                return "Fighting"
            case Genre.SHOOTER:
                return "Shooter"
            case Genre.SIMULATION:
                return "Simulation"
            case Genre.FAMILY_KIDS:
                return "Family & Kids"
            case Genre.PUZZLE_TRIVIA:
                return "Puzzle & Trivia"
            case Genre.ROLE_PLAYING:
                return "Role playing"
            case _:
                raise ValueError()

    @classmethod
    def from_string(cls, value: str):
        match value:
            case "Action & Adventure":
                return Genre.ACTION_ADVENTURE
            case "Something else here":
                return Genre.SOMETHING_ELSE
            case _:
                raise ValueError()


@dataclass
class VideoGame:
    title: str
    published_by: str
    developed_by: str
    release_date: date
    genre: Genre
    rating: float
    num_reviews: int
    price: float
    is_on_pc: bool
    thumbnail_path: str
    description: str


class VideoGameJSONDecoder(json.JSONEncoder):
    def default(self, video_game: VideoGame) -> dict[str, Any]:
        return {
            "title": video_game.title,
            "published_by": video_game.published_by,
            "developed_by": video_game.developed_by,
            "release_date": datetime.strftime(video_game.release_date, "%Y-%m-%d"),
            "genre": video_game.genre.to_string(),
            "rating": video_game.rating,
            "num_reviews": video_game.num_reviews,
            "price": video_game.price,
            "is_on_pc": video_game.is_on_pc,
            "thumbnail_path": video_game.thumbnail_path,
            "description": video_game.description,
        }


video_games = [
    VideoGame(
        title="Stray",
        published_by="Annapurna Interactive",
        developed_by="BlueTwelve Studio",
        release_date=to_date("8/10/23"),
        genre=Genre.ACTION_ADVENTURE,
        rating=5,
        num_reviews=494,
        price=23.99,
        is_on_pc=True,
        thumbnail_path="./thumbnails/stray.jpeg",
        description="""Lost, alone and separated from family, a stray cat must untangle an ancient mystery to escape a long-forgotten city.
Stray is a third-person cat adventure game set amidst the detailed, neon-lit alleys of a decaying cybercity and the murky environments of its seedy underbelly. Roam surroundings high and low, defend against unforeseen threats and solve the mysteries of this unwelcoming place inhabited by curious droids and dangerous creatures.
See the world through the eyes of a cat and interact with the environment in playful ways. Be stealthy, nimble, silly, and sometimes as annoying as possible with the strange inhabitants of this mysterious world.
Along the way, the cat befriends a small flying drone, known only as B-12. With the help of this newfound companion, the duo must find a way out.
Stray is developed by BlueTwelve Studio, a small team from the south of France mostly made up of cats and a handful of humans.
""",
    ),
    VideoGame(
        title="Remnant II - Standard Edition",
        published_by="Gearbox Publishing",
        developed_by="Gunfire Games",
        release_date=to_date("7/25/23"),
        genre=Genre.ACTION_ADVENTURE,
        rating=4,
        num_reviews=817,
        price=49.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/remnant.jpeg",
        description="""Unimaginable Worlds. Unrelenting Odds

Remnant 2 is the sequel to the best-selling game Remnant: From the Ashes that pits survivors of humanity against new deadly creatures and god-like bosses across terrifying worlds. Play solo or co-op with two other friends to explore the depths of the unknown to stop an evil from destroying reality itself. To succeed, players will need to rely on their own skills and those of their team to overcome the toughest challenges and to stave off humanity’s extinction.

Intense Remnant Combat Experience

A mix of methodical and frenetic ranged/melee combat returns with cunning enemies and large scale boss battles. Choose specific gear and weapons to optimize for the different biomes and battles ahead. Bosses will bring high-level players to team up to overcome the challenge and try to obtain the biggest rewards
""",
    ),
    VideoGame(
        title="Mortal Kombat 11 Ultimate + Injustice 2 Leg. Edition Bundle",
        published_by="Warner Bros. Interactive Entertainment",
        developed_by="NetherRealm Studios",
        release_date=to_date("3/24/21"),
        genre=Genre.FIGHTING,
        rating=3.5,
        num_reviews=5200,
        price=99.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/mortal-kombat.jpeg",
        description="""The Ultimate Fighter Bundle delivers the ultimate 1-2 punch, combining both of NetherRealm Studios' blockbuster fighting franchises in one knockout package.

The definitive MK11 experience! Take control of Earthrealm's protectors in the game's TWO critically acclaimed, time-bending Story Campaigns as they race to stop Kronika from rewinding time and rebooting history. Friendships are tested, and new alliances forged, in the battle to save all of existence. MK11 Ultimate features the komplete 37-character roster, including new additions Rain, Mileena & Rambo.

Every Battle Defines You in Injustice™ 2 - Legendary Edition. Experience the epic story, dynamic gameplay and the biggest DC Universe roster ever assembled in a fighting game. Power up and build the ultimate version of your favorite DC legends. Includes all 10 add-on characters, including Hellboy and TMNT.

MK11 Ultimate is Smart Delivery enabled and includes FREE upgrades on the Xbox Series X|S:

• 4K Dynamic Resolution
• Enhanced Visuals
""",
    ),
    VideoGame(
        title="Diablo® IV - Standard Edition",
        published_by="Blizzard Entertainment",
        developed_by="Blizzard Entertainment",
        release_date=to_date("6/5/23"),
        genre=Genre.ACTION_ADVENTURE,
        rating=3,
        num_reviews=4500,
        price=69.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/diablo.jpeg",
        description="""Diablo® IV - Standard Edition includes:

- Diablo® IV for Xbox One / Xbox Series X|S
- Inarius Wings & Inarius Murloc Pet in Diablo® III*
- Amalgam of Rage Mount in World of Warcraft®*
- Umber Winged Darkness Cosmetics Set in Diablo Immortal®*

Diablo® IV is the next-gen action RPG experience with endless evil to slaughter, countless abilities to master, nightmarish Dungeons, and legendary loot. Embark on the campaign solo or with friends, meeting memorable characters through beautifully dark settings and a gripping story, or go rogue through an expansive End Game and shared world where players will meet in towns to trade, team up to battle World Bosses, or descend into PVP zones to test their skills against other players - no lobbies necessary - with cross-play and cross-progression on all available platforms.

This is only the beginning for Diablo® IV, with new events, stories, seasons, rewards, and more looming on the horizon.
""",
    ),
    VideoGame(
        title="Overwatch® 2: Hero Collection",
        published_by="Blizzard Entertainment Inc.",
        developed_by="Blizzard Entertainment Inc.",
        release_date=to_date("8/10/23"),
        genre=Genre.SHOOTER,
        rating=3.5,
        num_reviews=64700,
        price=4.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/overwatch.jpeg",
        description="""New to Overwatch 2? Jump into the game with the Overwatch 2: Hero Collection!

This bundle includes:
- Access to all legacy Overwatch heroes
- 3 legacy Epic Overwatch skins
- 1,500 Overwatch Credits

With your Overwatch Credits, you can purchase legacy in-game cosmetic items from the Hero Gallery to customize your heroes. Premium shop items are purchased with Overwatch Coins (sold separately).
""",
    ),
    VideoGame(
        title="Minecraft",
        published_by="Microsoft Studios",
        developed_by="Mojang/Microsoft Studios",
        release_date=to_date("9/19/17"),
        genre=Genre.FAMILY_KIDS,
        rating=5,
        num_reviews=2_399_600,
        price=19.99,
        is_on_pc=True,
        thumbnail_path="./thumbnails/minecraft",
        description="""Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles. Play in creative mode with unlimited resources or mine deep into the world in survival mode, crafting weapons and armor to fend off the dangerous mobs. Scale craggy mountains, unearth elaborate caves and mine large ore veins. Discover lush cave and dripstone cave biomes. Light up your world with candles to show what a savvy spelunker and master mountaineer you are!

FEATURES:
If you can dream it, you can build it. Put your imagination and limitless resources to work with Creative Mode.
Battle mobs, construct shelters and explore the landscape – it’s all in a day’s work when you try to survive and thrive in Survival Mode.
New tools, locations and spaces are yours to explore, thanks to our regular updates.
Cross-platform play for up to eight players across Windows, PlayStation, Nintendo, Xbox and mobile devices.
Discover skin, texture and mash-up packs from the community! Find out more at minecraft.net/marketplace.
""",
    ),
    VideoGame(
        title="Acceptance",
        published_by="Ratalaika Games S.L.",
        developed_by="Rasul Mono",
        release_date=to_date("8/10/23"),
        genre=Genre.ACTION_ADVENTURE,
        rating=None,
        num_reviews=None,
        price=4.79,
        is_on_pc=False,
        thumbnail_path="./thumbnails/acceptance.jpeg",
        description="""A story-driven psychological thriller about the horrific consequences of a loved one's suicide.

After the tragedy of his wife's suicide, an office worker must process the horrific events surrounding the incident. Experience haunting characterizations of five stages of grief – denial, anger, bargaining, depression and finally acceptance in this atmospheric 2D psychological thriller.

The story focuses on the social issue of suicide and explores relationships with people who are at risk.


Features:
* Story-driven psychological thriller
* Focus on suicide and people at risk
* Immersive story and detailed characters.
* Original graphics and soundtrack.
""",
    ),
    VideoGame(
        title="Bright Lights of Svetlov",
        published_by="Sometimes You",
        developed_by="Vladimir Cholokyan",
        release_date=to_date("8/10/23"),
        genre=Genre.PUZZLE_TRIVIA,
        rating=None,
        num_reviews=None,
        price=9.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/svetlov.jpeg",
        description="""Mid 1980s. A small industrial town somewhere in Soviet Union.

Panel houses, ordinary repetitive jobs, boring household activities. Take a look at the life of the most ordinary family, and become a witness to the difficulties that it will face.

- Carefully depicted atmosphere of USSR.
- Linear, story-focused experience.
- Do your daily routine and get to know about family members.
""",
    ),
    VideoGame(
        title="Stray Gods: The Roleplaying Musical",
        published_by="Humble Games",
        developed_by="Summerfall Studios",
        release_date=to_date("8/10/23"),
        genre=Genre.ROLE_PLAYING,
        rating=None,
        num_reviews=None,
        price=29.99,
        is_on_pc=False,
        thumbnail_path="./thumbnails/stray-gods.jpeg",
        description="""In a modern fantasy world, college dropout Grace is granted the power of a Muse - power she'll need to find out the truth behind her predecessor's death before time runs out. You’ll decide who Grace allies with, who she can trust, and who may betray her in this beautifully hand-illustrated roleplaying musical.

Written by David Gaider comes Stray Gods - an urban fantasy tale of finding your place, taking charge of your fate, and discovering answers. Your choices will change the endings, as well as the path you take to get there.

A compelling story of hope, self-discovery, and forging your path.

Find Your Voice
"Adventure, love, and songs await!

Charm, negotiate, or strong-arm your way through their world as Grace, playing through original, fully interactive musical numbers composed by Grammy-nominated composer Austin Wintory, Tripod (musicians Scott Edgar, Steven Gates, and Simon Hall) and Eurovision Australia's own Montaigne (Jess Cerro). Fully orchestrated and performed by an all-star cast, you'll feel as though you're right there on the stage.
""",
    ),
]

print(json.dumps(video_games, indent=2, cls=VideoGameJSONDecoder, ensure_ascii=False))
