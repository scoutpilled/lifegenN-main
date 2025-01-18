import random
from enum import Enum, Flag, auto
from typing import Union


class SkillPath(Enum):
    TEACHER = ("quick to help", "good teacher", "great teacher", "excellent teacher")
    HUNTER = ("moss ball hunter", "good hunter", "great hunter", "renowned hunter")
    FIGHTER = (
        "avid play-fighter",
        "good fighter",
        "formidable fighter",
        "unusually strong fighter",
    )
    RUNNER = (
        "never sits still",
        "fast runner",
        "incredible runner",
        "fast as the wind",
    )
    CLIMBER = (
        "constantly climbing",
        "good climber",
        "great climber",
        "impressive climber",
    )
    SWIMMER = (
        "splashes in puddles",
        "good swimmer",
        "talented swimmer",
        "fish-like swimmer",
    )
    SPEAKER = (
        "confident with words",
        "good speaker",
        "great speaker",
        "eloquent speaker",
    )
    MEDIATOR = (
        "quick to make peace",
        "good mediator",
        "great mediator",
        "skilled mediator",
    )
    CLEVER = ("quick witted", "clever", "very clever", "incredibly clever")
    INSIGHTFUL = (
        "careful listener",
        "helpful insight",
        "valuable insight",
        "trusted advisor",
    )
    SENSE = ("oddly observant", "natural intuition", "keen eye", "unnatural senses")
    KIT = (
        "active imagination",
        "good kitsitter",
        "great kitsitter",
        "beloved kitsitter",
    )
    STORY = (
        "lover of stories",
        "good storyteller",
        "great storyteller",
        "masterful storyteller",
    )
    LORE = (
        "interested in Clan history",
        "learner of lore",
        "lore keeper",
        "lore master",
    )
    CAMP = ("picky nest builder", "steady paws", "den builder", "camp keeper")
    HEALER = ("interested in herbs", "good healer", "great healer", "fantastic healer")
    STAR = (
        "curious about StarClan",
        "connection to StarClan",
        "deep StarClan bond",
        "unshakable StarClan link",
    )
    DARK = (
        "interested in the Dark Forest",
        "Dark Forest affinity",
        "deep Dark Forest bond",
        "unshakable Dark Forest link",
    )
    OMEN = ("interested in oddities", "omen seeker", "omen sense", "omen sight")
    DREAM = ("restless sleeper", "strange dreamer", "dream walker", "dream shaper")
    CLAIRVOYANT = (
        "oddly insightful",
        "somewhat clairvoyant",
        "fairly clairvoyant",
        "incredibly clairvoyant"
    )
    PROPHET = (
        "fascinated by prophecies",
        "prophecy seeker",
        "prophecy interpreter",
        "prophet"
    )
    GHOST = (
        "morbid curiosity",
        "ghost sense",
        "ghost sight",
        "ghost speaker"
    ) 
    GARDENER = (
        "loves to pick flowers",
        "grows herbs",
        "herb organizer",
        "caretaker of the greens"
    ) 
    WAKEFUL = (
        "never settles down",
        "light sleeper",
        "alert",
        "vigilant"
    ) 
    DELIVERER = (
        "queen helper",
        "helpful stork",
        "kit deliverer",
        "pregnancy expert"
    ) 
    DECORATOR = (
        "makes things pretty",
        "crafty paws",
        "creative",
        "decor master"
    ) 
    LEADERSHIP = (
        "deputy helper",
        "leads patrols",
        "leader's accomplice",
        "assiduous"
    ) 
    AGILE = (
        "parkours around camp",
        "light-footed",
        "lithe",
        "quick agilist"
    ) 
    STEALTHY = (
        "startles others",
        "underpawed",
        "furtive kitty",
        "clandestine"
    ) 
    MEMORY = (
        "remembers little details",
        "memorious",
        "retentive memory",
        "mnemonist"
    ) 
    MESSENGER = (
        "delivers messages",
        "message-bearer",
        "message-carrier",
        "harbinger to the clans"
    ) 
    ASSIST = (
        "little helper",
        "assist guard",
        "alert assistant",
        "camp's assister"
    ) 
    HISTORIAN = (
        "remembers stories",
        "bookkeeper",
        "archivist",
        "accountant of history"
    ) 
    BOOKMAKER = (
        "loves to tell stories",
        "journalist",
        "novelist",
        "author of many stories"
    ) 
    PATIENT = (
        "waits their turn",
        "serene",
        "even-tempered",
        "equanimous"
    ) 
    DETECTIVE = (
        "curious about mysteries",
        "elementary case-solver",
        "great sleuth",
        "masterful detective"
    ) 
    HERBALIST = (
        "curious about remedies",
        "herbal inventor",
        "poison maker",
        "creator of remedies"
    )
    CHEF = (
        "seasons their food",
        "cooks prey",
        "gourmet prey maker",
        "masterful chef"
    )
    PRODIGY = (
        "unusually gifted",
        "knows alot of facts",
        "smart role model",
        "seen as an omen"
    )
    EXPLORER = (
        "curious wanderer",
        "knowledgeable explorer",
        "brave pathfinder",
        "master of territories"
    )
    TRACKER = (
        "tracker instincts",
        "proficient tracker",
        "great tracker",
        "masterful tracker"
    )
    GUARDIAN = (
        "watchful",
        "good guard",
        "great guard",
        "guardian"
    )
    TUNNELER = (
        "enjoys digging",
        "good tunneler",
        "great tunneler",
        "fantastic tunneler"
    )
    NAVIGATOR = (
        "good with directions",
        "good navigator",
        "great navigator",
        "pathfinder"
    )
    SONG = (
        "likes to sing",
        "good singer",
        "great singer",
        "captivating singer"
    )
    GRACE = (
        "steps lightly",
        "graceful",
        "elegant",
        "radiates elegance"
    )
    CLEAN = (
        "tidy",
        "fur-care enthusiast",
        "meticulous cleaner",
        "master of aesthetics"
    )
    INNOVATOR = (
        "always curious",
        "problem solver",
        "creator of solutions",
        "visionary thinker"
    )
    COMFORTER = (
        "gentle voice",
        "comforting presence",
        "nightmare soother",
        "boogeyman-fighter"
    )
    MATCHMAKER = (
        "interested in relationship drama",
        "relationship advisor",
        "skilled heart-reader",
        "masterful matchmaker"
    )
    THINKER = (
        "oddly resourceful",
        "out-of-the-box thinker",
        "paradox enthusiast",
        "philosopher"
    )
    COOPERATIVE = (
        "lives in groups",
        "good sport",
        "team player",
        "insider"
    )
    SCHOLAR = (
        "always learning",
        "well-versed",
        "incredibly knowledgeable",
        "polymath"
    )
    TIME = (
        "oddly orderly",
        "always busy",
        "coordinated",
        "efficiency aficionado"
    )
    TREASURE = (
        "looks for trinkets",
        "item stasher",
        "trinket stower",
        "treasure keeper"
    )
    FISHER = (
        "bats at rivers", 
        "grazes fish", 
        "fish-catcher", 
        "gold star fishercat"
    )
    LANGUAGE = (
        "other-cat-ly whisperer",
        "dog-whisperer",
        "multilingual",
        "listener of all voices"
    ) 
    SLEEPER = (
        "dozes easily",
        "sunhigh log",
        "dormouse", 
        "leader of SnoozeClan"
    )
    DISGUISE = (
        "accessory hoarder",
        "creator of appearances",
        "skillful disguiser", 
        "shapeshifter"
    )
    PYRO = (
        "loves warmth",
        "messes with embers",
        "spark master", 
        "fire starter"
    )
    HYDRO = (
        "water lover",
        "great firefighter",
        "excellent extinguisher",
        "masterful extinguisher"
    )
    GIFTGIVER = (
        "loves to gift",
        "nice giftgiver",
        "excellent giftgiver", 
        "always gives gifts"
    )
    VIBES = (
        "senses vibes",
        "knows who to trust",
        "mood reader", 
        "vibe detector"
    )
    STARGAZER = (
        "gazes at the stars",
        "night vision",
        "star-filled eyes", 
        "celestial insight"
    )
    IMMUNE = (
        "rarely sick",
        "better immune system",
        "strong immune system", 
        "constant germ immunity"
    )

    MUSICVIBES = (
        "charming voice",
        "nice singing",
        "beautiful singing", 
        "lovely singing"
    )
    AURAVIBES = (
        "nice aura",
        "friendly aura",
        "calming aura", 
        "pleasant aura"
    )
    ANIMALTAKER = (
        "friendly with animals",
        "loves to care for animals",
        "wildlife friend", 
        "deep animal-lover"
    )
    VET = (
        "cares for injured creatures",
        "helps animals",
        "animal soother", 
        "woodland healer"
    )
    ANIMALMAGNET = (
        "small critters follow them",
        "attracts animals",
        "animals gather around them", 
        "animal magnet"
    )

    # bleu's expanded skillsets

    ACTING = (
    	"plays pretends",
    	"performs unique roles",
    	"skilled performer",
    	"great actor"
    	)

    ADVOCATE = (
        "suggests new ideas",
        "rallies for support",
        "supports causes",
        "speaks for others"
        )
    
    ANIMALOGIST = (
        "studies animal behavior",
        "gathers animal information",
        "trained zoologist",
        "expert zoologist"
        )
    
    ANTHROPOLOGIST = (
            "fascinated by Twolegs",
            "Twoleg enthusiast",
            "Kittypet sympathizer",
            "Kittypet affinity"
            )

    ARCHAEOLOGIST = (
            "plays with bones",
            "digs up graves",
            "analyzes skeletal remains",
            "skeletal collector"
            )

    ARCHIVER = (
            "remembers small details",
            "recounts past events",
            "trained fact checker",
            "expert archiver"
            )
    
    ARMORER = (
        "sharpens claws",
        "invents combative tools",
        "handles weapon accessories",
        "oversees weaponry"
        )

    ARRANGER = (
            "organizes flower petals",
            "crafts flower accessories",
            "trained florist",
            "flower arranger"
            )

    ASSASSIN = (
            "chases targets",
            "investigates codebreakers",
            "bloodhound",
            "bounty hunter"
            )

    ARTIFICER = (
            "decorates fur",
            "crafts pretty accessories",
            "designs accessories",
            "accessory crafter"
            )

    ARTISAN = (
            "drawn to pretty colors",
            "creative affinity",
            "artistically talented",
            "masterful artisan"
            )

    ASTRONOMER = (
            "enjoys stargazing",
            "guided by the stars",
            "star lore expert",
            "trained astronomer"
            )

    AURA = (
            "sensitive to environment", 
            "notices aura",
            "studies aura patterns",
            "aura reader" 
            )

    BALANCE = (
            "dexterous paws",
            "graceful moves",
            "balancer",
            "expert acrobatics"
            )
    
    BUILDER = (
            "interested in growing strong",
            "engages in muscle building",
            "strengthens muscles",
            "trained body builder"
            )
    
    CAMPER = (
            "makes up nests",
            "gathers nesting materials",
            "sets up camps",
            "camp builder"
            )

    CARPENTER = (
            "claws at wood",
            "forms wooden items",
            "whittles wood",
            "carpenter"
            )

    CHAMPION = (
            "aspiring defender",
            "powerful crusader",
            "mighty knight",
            "great champion"
            )

    COLLECTOR = (
            "picks up useful objects",
            "collects resources",
            "known hoarder",
            "skilled collector"
            )

    COMEDIAN = (
            "cracks silly jokes",
            "jokes around",
            "entertainer",
            "comedy genius"
            )
    
    COMMANDER = (
            "observes surroundings",
            "leads mock battles",
            "directs attacks",
            "commands allies"
            )
    
    COMPANION = (
            "offers comforting words",
            "close friend",
            "trusted ally",
            "personal favorite"
            )

    COMPULSION = (
            "charming presence",
            "weakens willpower",
            "compels others",
            "master manipulator"
            )
    
    CONSULTANT = (
            "observes relationships",
            "gives relationship advice",
            "specializes in personal matters",
            "relationship consultant"
            )

    CURSED = (
            "burdened by lineage",
            "suffers hardships",
            "encounters adversity",
            "cursed bloodline"
            )

    DANCER = (
            "rhythmic pawsteps",
            "prances around",
            "energetic mover",
            "lively motion"
            )
    
    DEATH = (
            "morbid senses",
            "smells death",
            "grim reaper",
            "angel of death"
            )

    DEBATER = (
            "quick to argue",
            "questions everything",
            "skilled debater",
            "serious debater"
            )

    DECEPTOR = (
            "tells white lies",
            "deceptive words",
            "smooth talker",
            "master swindler"
            )

    DISCIPLINE = (
            "follows rules",
            "judges misbehavior",
            "administers discipline",
            "atones for misconduct"
            )
    
    DIVER = (
            "holds in breath",
            "dives underwater",
            "swims with fishes",
            "plunges into deep waters"
            )

    ENFORCER = (
            "judges codebreakers",
            "pledges loyalty",
            "code follower",
            "code enforcer"
            )
    
    ENTERTAINER = (
            "center of attention",
            "fan favorite",
            "massive following",
            "beloved entertainer"
            )

    ETIQUETTE = (
            "conforms to society",
            "proper greeter",
            "respectfully cautious",
            "adequately behaves"
            )

    EXERCISE = (
            "always moving",
            "stretches legs",
            "body trainer",
            "muscle builder"
            )

    EXORCIST = (
            "scares away spirits",
            "evicts spirits",
            "commands spirits",
            "fearsome exorcist"
            )
    
    FAIRY = (
            "senses spirits",
            "dreams of the fae",
            "visited by fairies",
            "fairy kinship"
            )
    
    FOLLOWER = (
            "follows after others",
            "quick to take sides",
            "carefully chooses alliances",
            "loyal follower"
            )

    FORAGER = (
            "picks at berry bushes",
            "gathers fruits and seeds",
            "foraging dietician",
            "impressive forager"
            )
    
    FORTITUDE = (
            "rarely injured",
            "powerful fortitude",
            "high endurance",
            "strong constitution"
            )
    
    GAMBLER = (
            "takes big risks",
            "makes bold decision",
            "sacrifices safety",
            "daredevil"
            )
    
    GENEALOGIST = (
            "studies appearances",
            "guesses fur colors",
            "predicts pelt types",
            "foretells coat patterns"
            )

    GEOGRAPHER = (
            "nature spirit kindred",
            "observes land formations",
            "trained naturalist",
            "great geographer"
            )

    GRAVEKEEPER = (
            "ancestral curiosity",
            "tends to burial grounds",
            "burial caretaker",
            "ancestral groundskeeper"
            )

    GOSSIPER = (
            "socially engaged",
            "engages in idle gossip",
            "promotes internal strife",
            "politically active"
            )

    GUARDING = (
            "restless protector",
            "watches over others",
            "camp guard",
            "respected warden"
            )

    GUIDER = (
            "listens closely to others",
            "offers advice",
            "guides others",
            "skilled guider"
            )

    HERDER = (
            "groups together insects",
            "animal whisperer",
            "flock management",
            "herder"
            )

    HIDING = (
            "hide-and-seek winner",
            "blends into surroundings",
            "natural colors",
            "invisible hider"
            )
    
    HIKER = (
            "walks long distances",
            "takes extended walks",
            "skilled hiker",
            "expert hiker"
            )
    
    HYPNOTIST = (
            "offers persuasive arguments",
            "changes other's minds",
            "implants false memories",
            "powerful influence"
            )
    
    ILLUSION = (
            "magic affinity",
            "performs tricks",
            "skilled illusionist",
            "master of illusions"
            )

    INTIMIDATION = (
            "fluffs out chest",
            "fierce gaze",
            "threatening glare",
            "intimidating presence",
            )

    INVENTOR = (
            "innovative mind",
            "tinkers with random objects",
            "constructs creations",
            "inventor"
            )
    
    LEGACY = (
            "future heir",
            "prestigious lineage",
            "inherited status",
            "noble legacy"
            )
    
    LIFESAVER = (
            "quick reactor",
            "offers first aid",
            "rescues others from danger",
            "savior figure"
            )
    
    LUCKY = (
            "born lucky",
            "has good luck",
            "pushes luck",
            "lucky streak"
            )
    
    MANAGER = (
            "starts small tasks",
            "assigns roles",
            "dictates tasks",
            "oversees projects"
            )
    
    MECHANIC = (
            "gathers building materials",
            "plays with Twoleg objects",
            "learns mechanical structures",
            "makes helpful gadgets"
            )

    MEDITATION = (
            "ponders existence",
            "deep thinker",
            "reflects on life",
            "meditative"
            )

    MEDIUM = (
            "hears the dead's voices",
            "soul speaker",
            "spiritually intuitive",
            "spirit medium"
            )

    MENTALIST = (
            "knack for control",
            "offers suggestions",
            "diverts attention",
            "calculated guesser"
            )
    
    MINDER = (
            "looks after others",
            "deflects criticism",
            "controls public opinion",
            "experienced minder"
            )
    
    PARANORMAL = (
            "interested in the occult",
            "watches mystical spirits",
            "memorizes supernatural entities",
            "paranormal lorekeeper"
            )

    PILGRIM = (
            "interested in holy places",
            "takes care of shrines",
            "traveling pilgrim",
            "devoted worshipper"
            )

    POLITICIAN = (
            "asks small favors",
            "rallies for support",
            "persuasive charm",
            "drives personal agenda"
            )

    PSYCHOLOGIST = (
            "analyzes personal motives",
            "understands different perspectives",
            "studies cause and effect",
            "creates psychological profiles"
            )

    REPORTER = (
            "avid learner",
            "news bringer",
            "message giver",
            "grand herald"
            )
    
    GUARD = (
            "prevents accidents",
            "ensures collective safety",
            "navigates dangerous surroundings",
            "anticipates hazards"
            )

    SIGNALER = (
            "studies gestures",
            "makes up tail signs",
            "speaks in code",
            "commands with signals"
            )

    SOCIALITE = (
            "prominent background",
            "aristocratic power",
            "respected authority",
            "famous socialite"
            )

    SPORTER = (
            "imitates sporting activities",
            "trains with denmates",
            "skilled sporter",
            "master of a sport"
            )

    SUPPORTER = (
            "passive observer",
            "offers encouragement",
            "uplifts spirits",
            "strong moral support"
            )

    TRAINER = (
            "asks for advice",
            "studies techniques",
            "focuses on weakness",
            "personal trainer"
            )

    TRAVELER = (
            "curious about surroundings",
            "sight seer",
            "skilled tourist",
            "expert traveler"
            )

    TWOLEG = (
            "asks about twolegs",
            "part time kittypet",
            "studies twoleg interactions",
            "twoleg expert"
            )

    VOLUNTEER = (
            "cares for others",
            "eager helper",
            "charitable soul",
            "willing volunteer"
            )

    WRESTLER = (
            "starts play fights",
            "has a strong grasp",
            "wrestles opponents",
            "expert wrestler"
            )

    MIMICKER = (
            "repeats sounds",
            "copies vocal inflections",
            "repetitive chatterer",
            "perfect mimicry"
            )

    MINDFUL = (
            "sensitive of surroundings",
            "highly aware",
            "open mind",
            "enlightened"
            )

    MOURNER = (
            "grieves for the dead",
            "tells the departed's tales",
            "honored eulogist",
            "devoted mourner"
            )

    NEGOTIATOR = (
            "bargains for things",
            "offers solutions",
            "settles disputes",
           "negotiator"
            )
    
    NECROMANCER = (
            "resurrects insects",
            "defies death",
            "revives moribund",
            "necromancer"
            )
    
    NURSE = (
            "tends to denmates",
            "assists healers",
            "healer's assistant",
            "nurse"
            )
    
    ORATOR = (
            "speaks loudly",
            "makes speeches",
            "eloquent speaker",
            "known orator"
            )

    PAINTER = (
            "covered in mud",
            "enthusiastic dauber",
            "inspiring illustrator",
            "experienced painter"
            )

    PARENTING = (
            "offers praise and support",
            "cares for others",
            "respected nurturer",
            "beloved caregiver"
            )
    
    PLANNER = (
            "watches meetings",
            "offers praise",
            "hosts feasts",
            "plans parties"
            )

    PLAYING = (
            "plays around",
            "starts games with others",
            "invents games",
            "game maker"
            )

    PATROLLING = (
            "offers to join patrols",
            "joins the dawn patrol",
            "patrol enthusiast",
            "patrol leader"
            )

    PSYCHIC = (
            "senses strong feelings",
            "drawn to emotions",
            "emotionally perceptive",
            "reads minds"
            )

    POET = (
            "speaks from the heart",
            "rhymes words together",
            "eloquently speaks",
            "renowned poet"
            )
    
    POSSESSED = (
            "ghostly whispers",
            "acts oddly",
            "otherworldly gaze",
            "possessed"
            )
    PREACHER = (
            "curious about faith",
            "practices sermons",
            "spiritual leader",
            "respected preacher"
            )
    
    PROJECTION = (
            "shares emotions",
            "projects feelings",
            "manifests perception",
            "warps reality"
            )
    
    RANGER = (
            "throws pebbles",
            "attacks from a distance",
            "sharpened aim",
            "ranged attacks"
            )
    
    RECOVERER = (
            "heals quickly",
            "regenerates health",
            "hardy physique",
            "instant recovery"
            )
    
    REINCARNATED = (
            "dreams of a past life",
            "haunted by the past",
            "lives in the past",
            "reincarnated"
            )

    RESEARCHER = (
            "performs studies and tests",
            "discovers new concepts",
            "study evaluator",
            "detailed researcher"
            )
    
    RISEN = (
            "abnormal steps",
            "undead vessel",
            "risen walker",
            "ghastly figure"
            )
    
    RITE = (
            "tracks habits",
            "invents rituals",
            "honors traditions",
            "master of ceremonies"
            )

    SCAVENGER = (
            "picks up discarded items",
            "gathers worn material",
            "keeps all resources",
            "pack rat"
            )

    SCHEMER = (
            "pulls pranks on others",
            "discord seeker",
            "chaos bringer",
            "trickster"
            )

    SCOUTER = (
            "seeks new things",
            "surveys environment",
            "reliable informant",
            "scout"
            )

    SCRIBE = (
            "makes stone carvings",
            "inscribes into stone",
            "stonemason",
            "scribe"
            )
    
    SIREN = (
            "comforting purrs",
            "enchanted lilt",
            "hypnotic voice",
            "warning call"
            )
    
    SPY = (
            "collects secrets",
            "gathers intelligence",
            "highly informed",
            "spymaster"
            )

    STARLESS = (
            "interested in outsiders",
            "studies culture",
            "questions authority",
            "welcomes outsiders"
            )

    STEALTH = (
            "pounces on others",
            "stays out of sight",
            "quiet pawsteps",
            "snake-like attacks"
            )

    STRATEGIST = (
            "makes plans",
            "thinks carefully",
            "detailed planner",
            "strategist"
            )

    STYLIST = (
            "cleans other's furs",
            "tidies loose fur strands",
            "dappers pelt appearances",
            "stylizes fur"
            )

    SUMMONER = (
            "watches over the dead",
            "talks with the supernatural",
            "controls spirits",
            "powerful spirit summoner"
            )

    TAMER = (
            "soft-spoken",
            "warm towards animals",
            "accompanies animals",
            "animal tamer"
            )

    THIEF = (
            "steals items",
            "sneaky paws",
            "cat burglar",
           "criminal mastermind"
            )
    
    TELEPATHIC = (
            "perceives unspoken actions", 
            "reads minds",
            "shares thoughts",
            "expert telepath"
            )
    
    TESTER = (
            "avid risk taker",
            "insatiable curiosity",
            "performs experiments",
            "conducts trials"
            )

    TRADER = (
            "swaps prey with others",
            "makes deals",
            "supplies resources",
            "traderer"
            )

    VISION = (
            "curious about visions",
            "vision interpreter",
            "predicts future",
            "masterful seer"
            )

    WEATHER = (
            "observes the weather",
            "studies the weather",
            "predicts weather patterns",
            "weather expert"
            )

    WEAVER = (
            "weaves nesting material",
            "careful claws",
            "mends items",
            "weaver"
            )
    
    MYTHOLOGICAL = (
            "distinct nature",
            "unique presence",
            "legendary ability",
            "mythological figure"
            )

    LEARNER = (
            "quick witted",
            "fast learner",
            "sharp memory",
            "expert memorizer"
            )

    COMPETITOR = (
            "watches competitions",
            "organizes competitions",
            "skilled competitor",
            "talented competitor"
            )

    CHALLENGER = (
            "observes sparring matches",
            "challenges others",
            "duel challenger",
            "sparring master"
            )

    BEHAVIORIST = (
            "sensitive to attitudes",
            "notices behavioral changes",
            "examines behavior",
            "interprets intentions"
            )

    HAUNTED = (
            "friends with spirits",
            "soul magnet",
            "phantom charmer",
            "haunted by specters"
            )

    RESURRECTED = (
            "summoned from the dead",
            "second chance",
            "borrowed time",
            "extended life"
            )

    PROJECTOR = (
        "glimpses into the afterlife",
        "projects consciousness",
        "walks with the dead",
        "afterlife visitor"
        )

    RETRIEVER = (
        "motivates others",
        "retrieves energy",
        "offers empowerment",
        "energizer"
        )

    EXTRACTOR = (
        "sensitive to altered energies",
        "focuses energy",
        "channels other's energy",
        "connected to life"
        )

    PURIFIER = (
        "deters negative emotions",
        "sends waves of joy",
        "light bringer",
        "pure soul"
        )

    TRANCER = (
        "dazed gaze",
        "goes into trances",
        "extended daydreams",
        "frequent musing"
        )

    DIVINER = (
        "obtains insightful suggestions",
        "deeply self-reflective",
        "gives life advice",
        "manifests futures"
        )

    @staticmethod
    def get_random(exclude: list = ()):
        """Get a random path, with more uncommon paths being less common"""

        uncommon_paths = [
            i
            for i in [
                SkillPath.GHOST,
                SkillPath.PROPHET,
                SkillPath.CLAIRVOYANT,
                SkillPath.DREAM,
                SkillPath.OMEN,
                SkillPath.STAR,
                SkillPath.HEALER,
                SkillPath.DARK,
                SkillPath.PRODIGY,
                SkillPath.AURA,
                SkillPath.COMPULSION,
                SkillPath.CURSED,
                SkillPath.DEATH,
                SkillPath.EXORCIST,
                SkillPath.FAIRY,
                SkillPath.GRAVEKEEPER,
                SkillPath.MEDIUM,
                SkillPath.NECROMANCER,
                SkillPath.PSYCHIC,
                SkillPath.POSSESSED,
                SkillPath.PREACHER,
                SkillPath.PROJECTION,
                SkillPath.REINCARNATED,
                SkillPath.RISEN,
                SkillPath.SUMMONER,
                SkillPath.TELEPATHIC,
                SkillPath.VISION,
                SkillPath.HYPNOTIST,
                SkillPath.LUCKY,
                SkillPath.PARANORMAL,
                SkillPath.PILGRIM,
                SkillPath.PSYCHOLOGIST,
                SkillPath.HAUNTED,
                SkillPath.RESURRECTED,
                SkillPath.PROJECTOR,
                SkillPath.EXTRACTOR,
                SkillPath.DIVINER,
            ]
            if i not in exclude
        ]

        if not int(random.random() * 15):
            return random.choice(uncommon_paths)
        else:
            common_paths = [
                i
                for i in list(SkillPath)
                if i not in exclude and i not in uncommon_paths
            ]
            return random.choice(common_paths)


class HiddenSkillEnum(Enum):
    ROGUE = "rogue's knowledge"
    LONER = "loner's knowledge"
    KITTYPET = "kittypet's knowledge"


class SkillTypeFlag(Flag):
    SUPERNATURAL = auto()
    STRONG = auto()
    AGILE = auto()
    SMART = auto()
    OBSERVANT = auto()
    SOCIAL = auto()


class Skill:
    """Skills handling functions mostly"""

    tier_ranges = ((0, 9), (10, 19), (20, 29))
    point_range = (0, 29)

    short_strings = {
        SkillPath.TEACHER: "teaching",
        SkillPath.HUNTER: "hunting",
        SkillPath.FIGHTER: "fighting",
        SkillPath.RUNNER: "running",
        SkillPath.CLIMBER: "climbing",
        SkillPath.SWIMMER: "swimming",
        SkillPath.SPEAKER: "speaking",
        SkillPath.MEDIATOR: "mediating",
        SkillPath.CLEVER: "clever",
        SkillPath.INSIGHTFUL: "advising",
        SkillPath.SENSE: "observing",
        SkillPath.KIT: "caretaking",
        SkillPath.STORY: "storytelling",
        SkillPath.LORE: "lorekeeping",
        SkillPath.CAMP: "campkeeping",
        SkillPath.HEALER: "healing",
        SkillPath.STAR: "StarClan",
        SkillPath.OMEN: "omen",
        SkillPath.DREAM: "dreaming",
        SkillPath.CLAIRVOYANT: "predicting",
        SkillPath.PROPHET: "prophesying",
        SkillPath.GHOST: "ghosts",
        SkillPath.DARK: "dark forest",
        SkillPath.GARDENER: "gardener",
        SkillPath.WAKEFUL: "awake",
        SkillPath.DELIVERER: "delivery",
        SkillPath.DECORATOR: "decorator",
        SkillPath.LEADERSHIP: "great leader",
        SkillPath.AGILE: "agile",
        SkillPath.STEALTHY: "stealthy",
        SkillPath.MEMORY: "memorizing",
        SkillPath.MESSENGER: "messenger",
        SkillPath.ASSIST: "assisting",
        SkillPath.HISTORIAN: "history keeper",
        SkillPath.BOOKMAKER: "storymaker",
        SkillPath.TUNNELER: "tunneling",
        SkillPath.PATIENT: "patience",
        SkillPath.DETECTIVE: "solves mysteries",
        SkillPath.HERBALIST: "herbalist",
        SkillPath.CHEF: "chef",
        SkillPath.PRODIGY: "prodigy",
        SkillPath.EXPLORER: "exploring",
        SkillPath.TRACKER: "tracking",
        SkillPath.GUARDIAN: "guarding",
        SkillPath.NAVIGATOR: "navigating",
        SkillPath.SONG: "singing",
        SkillPath.GRACE: "grace",
        SkillPath.CLEAN: "cleaning",
        SkillPath.INNOVATOR: "innovating",
        SkillPath.COMFORTER: "comforting",
        SkillPath.MATCHMAKER: "matchmaking",
        SkillPath.THINKER: "thinking",
        SkillPath.COOPERATIVE: "cooperating",
        SkillPath.SCHOLAR: "learning",
        SkillPath.TIME: "efficient",
        SkillPath.TREASURE: "finding",
        SkillPath.FISHER: "fishing",
        SkillPath.LANGUAGE: "language",
        SkillPath.SLEEPER: "sleeping",
        SkillPath.DISGUISE: "disguiser",
        SkillPath.PYRO: "flame controller",
        SkillPath.HYDRO: "water hoarder",
        SkillPath.GIFTGIVER: "gives gifts",
        SkillPath.VIBES: "vibe detector",
        SkillPath.STARGAZER: "looks at the stars",
        SkillPath.IMMUNE: "immunity to sickness",
        SkillPath.MUSICVIBES: "musical aura",
        SkillPath.AURAVIBES: "pleasant aura",
        SkillPath.ANIMALTAKER: "loves animals",
        SkillPath.VET: "animal helper",
        SkillPath.ANIMALMAGNET: "animal attractor",

        SkillPath.ACTING: "acting",
        SkillPath.ANTHROPOLOGIST: "anthropology",
        SkillPath.ARCHAEOLOGIST: "archaeology",
        SkillPath.ARCHIVER: "archiving",
        SkillPath.ARRANGER: "arranging",
        SkillPath.ARTIFICER: "artificer",
        SkillPath.ARTISAN: "artistry",
        SkillPath.ASTRONOMER: "astronomy",
        SkillPath.BALANCE: "balancing",
        SkillPath.CARPENTER: "carpentry",
        SkillPath.COLLECTOR: "collecting",
        SkillPath.COMEDIAN: "comedy",
        SkillPath.DANCER: "dancing",
        SkillPath.DEBATER: "debating",
        SkillPath.DECEPTOR: "deception",
        SkillPath.DISCIPLINE: "disciplinary",
        SkillPath.ENFORCER: "enforcing",
        SkillPath.ETIQUETTE: "etiquette",
        SkillPath.EXERCISE: "exercising",
        SkillPath.EXORCIST: "exorcizing",
        SkillPath.FORAGER: "foraging",
        SkillPath.FORTITUDE: "fortitude",
        SkillPath.GEOGRAPHER: "geography",
        SkillPath.GRAVEKEEPER: "gravekeeping",
        SkillPath.GOSSIPER: "gossiping",
        SkillPath.GUARDING: "guarding",
        SkillPath.GUIDER: "guiding",
        SkillPath.HERDER: "herding",
        SkillPath.HIDING: "hiding",
        SkillPath.INTIMIDATION: "intimidation",
        SkillPath.INVENTOR: "inventing",
        SkillPath.MEDIUM: "mediumship",
        SkillPath.MENTALIST: "mentalist",
        SkillPath.REPORTER: "reporting",
        SkillPath.MIMICKER: "mimicry",
        SkillPath.MINDFUL: "mindfulness",
        SkillPath.MOURNER: "mourning",
        SkillPath.NEGOTIATOR: "negotiating",
        SkillPath.PAINTER: "painting",
        SkillPath.PARENTING: "parenting",
        SkillPath.PLAYING: "playing",
        SkillPath.PATROLLING: "patrolling",
        SkillPath.PSYCHIC: "psychic",
        SkillPath.POET: "poetry",
        SkillPath.RESEARCHER: "researchin",
        SkillPath.SCAVENGER: "scavenging",
        SkillPath.SCHEMER: "scheming",
        SkillPath.SCOUTER: "scouting",
        SkillPath.SCRIBE: "scribing",
        SkillPath.STARLESS: "starless cats",
        SkillPath.STEALTH: "stealthing",
        SkillPath.STRATEGIST: "strategizing",
        SkillPath.STYLIST: "stylizing",
        SkillPath.SUMMONER: "summoning",
        SkillPath.TAMER: "taming",
        SkillPath.THIEF: "thievery",
        SkillPath.TRADER: "trading",
        SkillPath.VISION: "visions",
        SkillPath.WEATHER: "weather reporting",
        SkillPath.WEAVER: "weaving",

        SkillPath.AURA: "aura reading",
        SkillPath.ADVOCATE: "advocation",
        SkillPath.ASSASSIN: "assassinating",
        SkillPath.CHAMPION: "championship",
        SkillPath.COMMANDER: "commanding",
        SkillPath.COMPULSION: "compelling",
        SkillPath.CURSED: "cursed",
        SkillPath.DEATH: "death",
        SkillPath.ENTERTAINER: "entertaining",
        SkillPath.FAIRY: "fairy",
        SkillPath.ILLUSION: "illusions",
        SkillPath.LEGACY: "legacy",
        SkillPath.MEDITATION: "meditating",
        SkillPath.MINDER: "minding",
        SkillPath.NECROMANCER: "resurrecting",
        SkillPath.NURSE: "nursing",
        SkillPath.ORATOR: "oration",
        SkillPath.PLANNER: "planning",
        SkillPath.POSSESSED: "possessed",
        SkillPath.PREACHER: "preaching",
        SkillPath.PROJECTION: "projection",
        SkillPath.RANGER: "ranging",
        SkillPath.RECOVERER: "recovery",
        SkillPath.REINCARNATED: "reincarnated",
        SkillPath.RISEN: "undead",
        SkillPath.RITE: "ritualistic",
        SkillPath.SIREN: "siren",
        SkillPath.SPY: "spying",
        SkillPath.TELEPATHIC: "telepathy",
        SkillPath.TESTER: "testing",

        SkillPath.ANIMALOGIST: "animal studies",
        SkillPath.ARMORER: "weapon crafting",
        SkillPath.BUILDER: "body building",
        SkillPath.CAMPER: "camping",
        SkillPath.COMPANION: "companionship",
        SkillPath.CONSULTANT: "consulting",
        SkillPath.DIVER: "deep diving",
        SkillPath.FOLLOWER: "following commands",
        SkillPath.GAMBLER: "risk taking",
        SkillPath.GENEALOGIST: "pelt studies",
        SkillPath.GUARD: "safety guard",
        SkillPath.HIKER: "hiking",
        SkillPath.HYPNOTIST: "hypnotizing",
        SkillPath.LIFESAVER: "saving lives",
        SkillPath.LUCKY: "lucky",
        SkillPath.MANAGER: "project management",
        SkillPath.MECHANIC: "mechanics",
        SkillPath.PARANORMAL: "paranormal",
        SkillPath.PILGRIM: "pilgrimage",
        SkillPath.POLITICIAN: "politics",
        SkillPath.PSYCHOLOGIST: "psychoanalyzing",
        SkillPath.SIGNALER: "signaling",
        SkillPath.SOCIALITE: "social influence",
        SkillPath.SPORTER: "sporting",
        SkillPath.SUPPORTER: "supporting",
        SkillPath.TRAINER: "training",
        SkillPath.TRAVELER: "traveling",
        SkillPath.TWOLEG: "twoleg lore",
        SkillPath.VOLUNTEER: "volunteering",
        SkillPath.WRESTLER: "wrestling",

        SkillPath.MYTHOLOGICAL: "mythological",
        SkillPath.LEARNER: "learning",
        SkillPath.COMPETITOR: "competing",
        SkillPath.CHALLENGER: "challenging",
        SkillPath.BEHAVIORIST: "behaviorist",
        SkillPath.HAUNTED: "haunted",
        SkillPath.RESURRECTED: "resurrected",

        SkillPath.PROJECTOR: "projecting",
        SkillPath.RETRIEVER: "energy retrieval",
        SkillPath.EXTRACTOR: "energy refocusing",
        SkillPath.PURIFIER: "cleansing emotions",
        SkillPath.TRANCER: "trancing",
        SkillPath.DIVINER: "divining",
    }

    def __init__(self, path: SkillPath, points: int = 0, interest_only: bool = False):

        self.path = path
        self.interest_only = interest_only
        if points > self.point_range[1]:
            self._p = self.point_range[1]
        elif points < self.point_range[0]:
            self._p = self.point_range[0]
        else:
            self._p = points

    def __repr__(self) -> str:
        return f"<Skill: {self.path}, {self.points}, {self.tier}, {self.interest_only}>"

    def get_short_skill(self):
        return Skill.short_strings.get(self.path, "???")

    @staticmethod
    def generate_from_save_string(save_string: str):
        """Generates the skill from the save string in the cat data"""
        if not save_string:
            return None

        split_values = save_string.split(",")
        if split_values[2].lower() == "true":
            interest = True
        else:
            interest = False

        return Skill(SkillPath[split_values[0]], int(split_values[1]), interest)

    @staticmethod
    def get_random_skill(
        points: int = None, point_tier: int = None, exclude=(), interest_only=False
    ):
        """Generates a random skill. If wanted, you can specify a tier for the points
        value to be randomized within."""

        if isinstance(points, int):
            points = points
        elif isinstance(point_tier, int) and 1 <= point_tier <= 3:
            points = random.randint(
                Skill.tier_ranges[point_tier - 1][0],
                Skill.tier_ranges[point_tier - 1][1],
            )
        else:
            points = random.randint(Skill.point_range[0], Skill.point_range[1])

        if isinstance(exclude, SkillPath):
            exclude = [exclude]

        return Skill(SkillPath.get_random(exclude), points, interest_only)

    @property
    def points(self):
        return self._p

    @points.setter
    def points(self, val):
        if val > self.point_range[1]:
            self._p = self.point_range[1]
        elif val < self.point_range[0]:
            self._p = self.point_range[0]
        else:
            self._p = val

    @property
    def skill(self):
        """Skill property"""
        return self.path.value[self.tier]

    @skill.setter
    def skill(self):
        """Can't set the skill directly with this setter"""
        print("Can't set skill directly")

    @property
    def tier(self):
        """Returns the tier level of the skill"""
        if self.interest_only:
            return 0
        for _ran, i in zip(Skill.tier_ranges, range(1, 4)):
            if _ran[0] <= self.points <= _ran[1]:
                return i

        return 1

    @tier.setter
    def tier(self):
        print("Can't set tier directly")

    def set_points_to_tier(self, tier: int):
        """This is seperate from the tier setter, since it will booonly allow you
        to set points to tier 1, 2, or 3, and never 0. Tier 0 is retricted to interest_only
        skills"""

        # Make sure it in the right range. If not, return.
        if not (1 <= tier <= 3):
            return

        # Adjust to 0-indexed ranges list
        self.points = Skill.tier_ranges[tier - 1][0]

    def get_points_to_tier(self, tier:int):
        """This is seperate from the tier setter, since it will booonly allow you
        to set points to tier 1, 2, or 3, and never 0. Tier 0 is retricted to interest_only
        skills"""
        
        # Make sure it in the right range. If not, return.
        if not (1 <= tier <= 3):
            return
        
        # Adjust to 0-indexed ranges list
        return Skill.tier_ranges[tier - 1][0]

    def get_save_string(self):
        """Gets the string that is saved in the cat data"""
        return f"{self.path.name},{self.points},{self.interest_only}"
    
    def get_skill_from_string(self, string):
        """Returns a SkillPath given a string skill"""
        for skill in SkillPath:
            if string in skill.value:
                index = skill.value.index(string)
                return self.generate_from_save_string(f"{skill.name},{Skill.get_points_to_tier(self, tier=max(1,index))},False")
            
        return "String not found in any Enum"


class CatSkills:
    """
    Holds the cats skills, and handled changes in the skills.
    """

    # Mentor Inflence groups.
    # pylint: disable=unsupported-binary-operation
    influence_flags = {
        SkillPath.TEACHER: SkillTypeFlag.STRONG
        | SkillTypeFlag.AGILE
        | SkillTypeFlag.SMART
        | SkillTypeFlag.OBSERVANT
        | SkillTypeFlag.SOCIAL,
        SkillPath.HUNTER: SkillTypeFlag.STRONG
        | SkillTypeFlag.AGILE
        | SkillTypeFlag.OBSERVANT,
        SkillPath.FIGHTER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.RUNNER: SkillTypeFlag.AGILE,
        SkillPath.CLIMBER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.SWIMMER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.SPEAKER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.MEDIATOR: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.CLEVER: SkillTypeFlag.SMART,
        SkillPath.INSIGHTFUL: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.SENSE: SkillTypeFlag.OBSERVANT,
        SkillPath.KIT: SkillTypeFlag.SOCIAL,
        SkillPath.STORY: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.LORE: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.CAMP: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.HEALER: SkillTypeFlag.SMART
        | SkillTypeFlag.OBSERVANT
        | SkillTypeFlag.SOCIAL,
        SkillPath.STAR: SkillTypeFlag.SUPERNATURAL,
        SkillPath.OMEN: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.DREAM: SkillTypeFlag.SUPERNATURAL,
        SkillPath.CLAIRVOYANT: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.PROPHET: SkillTypeFlag.SUPERNATURAL,
        SkillPath.GHOST: SkillTypeFlag.SUPERNATURAL,
        SkillPath.DARK: SkillTypeFlag.SUPERNATURAL,
        SkillPath.GARDENER: SkillTypeFlag.SMART,
        SkillPath.WAKEFUL: SkillTypeFlag.STRONG | SkillTypeFlag.OBSERVANT,
        SkillPath.DELIVERER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.DECORATOR: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.LEADERSHIP: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.AGILE: SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT,
        SkillPath.STEALTHY: SkillTypeFlag.SMART | SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT,
        SkillPath.MEMORY: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.MESSENGER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.ASSIST: SkillTypeFlag.STRONG | SkillTypeFlag.SOCIAL,
        SkillPath.HISTORIAN: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.BOOKMAKER: SkillTypeFlag.SOCIAL,
        SkillPath.TUNNELER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.PATIENT: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.DETECTIVE: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.HERBALIST: SkillTypeFlag.SMART | SkillTypeFlag.SUPERNATURAL,
        SkillPath.CHEF: SkillTypeFlag.AGILE | SkillTypeFlag.SOCIAL,
        SkillPath.PRODIGY: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.EXPLORER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.TRACKER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.GUARDIAN: SkillTypeFlag.STRONG | SkillTypeFlag.OBSERVANT,
        SkillPath.NAVIGATOR: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.SONG: SkillTypeFlag.SOCIAL,
        SkillPath.GRACE: SkillTypeFlag.AGILE,
        SkillPath.CLEAN: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.INNOVATOR: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.COMFORTER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.MATCHMAKER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.THINKER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.COOPERATIVE: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.SCHOLAR: SkillTypeFlag.SMART,
        SkillPath.TIME: SkillTypeFlag.AGILE | SkillTypeFlag.SMART,
        SkillPath.TREASURE: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.FISHER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT,
        SkillPath.LANGUAGE: SkillTypeFlag.SOCIAL,
        SkillPath.SLEEPER: SkillTypeFlag.STRONG,
        SkillPath.DISGUISE: SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SMART,
        SkillPath.PYRO: SkillTypeFlag.SMART,
        SkillPath.HYDRO: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.GIFTGIVER: SkillTypeFlag.SOCIAL,
        SkillPath.VIBES: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.STARGAZER: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.MUSICVIBES: SkillTypeFlag.SOCIAL,
        SkillPath.AURAVIBES: SkillTypeFlag.SOCIAL,
        SkillPath.ANIMALTAKER: SkillTypeFlag.SOCIAL,
        SkillPath.VET: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.ANIMALMAGNET: SkillTypeFlag.SOCIAL,
        SkillPath.IMMUNE: SkillTypeFlag.OBSERVANT,

        SkillPath.ACTING: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ANTHROPOLOGIST: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ARCHAEOLOGIST: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ARCHIVER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ARRANGER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ARTIFICER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ARTISAN: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ASTRONOMER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.BALANCE: SkillTypeFlag.AGILE,
        SkillPath.CARPENTER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.COLLECTOR: SkillTypeFlag.AGILE,
        SkillPath.COMEDIAN: SkillTypeFlag.SOCIAL,
        SkillPath.DANCER: SkillTypeFlag.AGILE,
        SkillPath.DEBATER: SkillTypeFlag.SOCIAL,
        SkillPath.DECEPTOR: SkillTypeFlag.SOCIAL,
        SkillPath.DISCIPLINE: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ENFORCER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ETIQUETTE: SkillTypeFlag.SOCIAL,
        SkillPath.EXERCISE: SkillTypeFlag.AGILE,
        SkillPath.EXORCIST: SkillTypeFlag.SUPERNATURAL,
        SkillPath.FORAGER: SkillTypeFlag.AGILE,
        SkillPath.GEOGRAPHER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.GRAVEKEEPER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.GOSSIPER: SkillTypeFlag.SOCIAL,
        SkillPath.GUARDING: SkillTypeFlag.AGILE,
        SkillPath.GUIDER: SkillTypeFlag.SOCIAL,
        SkillPath.HERDER: SkillTypeFlag.AGILE,
        SkillPath.HIDING: SkillTypeFlag.AGILE,
        SkillPath.FORTITUDE: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.INTIMIDATION: SkillTypeFlag.STRONG,
        SkillPath.INVENTOR: SkillTypeFlag.AGILE | SkillTypeFlag.SMART,
        SkillPath.MEDIUM: SkillTypeFlag.SUPERNATURAL,
        SkillPath.MENTALIST: SkillTypeFlag.SMART,
        SkillPath.REPORTER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART | SkillTypeFlag.AGILE,
        SkillPath.MIMICKER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.MINDFUL: SkillTypeFlag.OBSERVANT,
        SkillPath.MOURNER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.NEGOTIATOR: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.PAINTER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.PARENTING: SkillTypeFlag.SOCIAL,
        SkillPath.PLAYING: SkillTypeFlag.SOCIAL,
        SkillPath.PATROLLING: SkillTypeFlag.SOCIAL,
        SkillPath.PSYCHIC: SkillTypeFlag.OBSERVANT,
        SkillPath.POET: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.RESEARCHER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.SCAVENGER: SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE,
        SkillPath.SCHEMER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.SCOUTER: SkillTypeFlag.AGILE | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SMART,
        SkillPath.SCRIBE: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.STARLESS: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.STEALTH: SkillTypeFlag.AGILE | SkillTypeFlag.SMART,
        SkillPath.STRATEGIST: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SMART,
        SkillPath.STYLIST: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.SUMMONER: SkillTypeFlag.SUPERNATURAL,
        SkillPath.TAMER: SkillTypeFlag.STRONG | SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.THIEF: SkillTypeFlag.AGILE | SkillTypeFlag.SMART,
        SkillPath.TRADER: SkillTypeFlag.SOCIAL | SkillTypeFlag.SMART,
        SkillPath.VISION: SkillTypeFlag.SUPERNATURAL,
        SkillPath.WEATHER: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SMART,
        SkillPath.WEAVER: SkillTypeFlag.AGILE,

        SkillPath.AURA: SkillTypeFlag.SUPERNATURAL,
        SkillPath.ADVOCATE: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.ASSASSIN: SkillTypeFlag.STRONG | SkillTypeFlag.OBSERVANT,
        SkillPath.CHAMPION: SkillTypeFlag.STRONG,
        SkillPath.COMMANDER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.COMPULSION: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.CURSED: SkillTypeFlag.SUPERNATURAL,
        SkillPath.DEATH: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SUPERNATURAL,
        SkillPath.ENTERTAINER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.FAIRY: SkillTypeFlag.SUPERNATURAL,
        SkillPath.ILLUSION: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.LEGACY: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.MEDITATION: SkillTypeFlag.SMART,
        SkillPath.MINDER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.NECROMANCER: SkillTypeFlag.SUPERNATURAL,
        SkillPath.NURSE: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.ORATOR: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.PLANNER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.POSSESSED: SkillTypeFlag.SUPERNATURAL,
        SkillPath.PREACHER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.PROJECTION: SkillTypeFlag.SUPERNATURAL,
        SkillPath.RANGER: SkillTypeFlag.STRONG,
        SkillPath.RECOVERER: SkillTypeFlag.STRONG,
        SkillPath.REINCARNATED: SkillTypeFlag.SUPERNATURAL,
        SkillPath.RISEN: SkillTypeFlag.SUPERNATURAL,
        SkillPath.RITE: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.SIREN: SkillTypeFlag.SUPERNATURAL,
        SkillPath.SPY: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.TELEPATHIC: SkillTypeFlag.SUPERNATURAL,
        SkillPath.TESTER: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,

        SkillPath.ANIMALOGIST: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.ARMORER: SkillTypeFlag.OBSERVANT,
        SkillPath.BUILDER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.CAMPER: SkillTypeFlag.OBSERVANT,
        SkillPath.COMPANION: SkillTypeFlag.SOCIAL,
        SkillPath.CONSULTANT: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL,
        SkillPath.DIVER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.FOLLOWER: SkillTypeFlag.SOCIAL,
        SkillPath.GAMBLER: SkillTypeFlag.AGILE,
        SkillPath.GENEALOGIST: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.GUARD: SkillTypeFlag.SOCIAL | SkillTypeFlag.AGILE,
        SkillPath.HIKER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.HYPNOTIST: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SUPERNATURAL,
        SkillPath.LIFESAVER: SkillTypeFlag.AGILE,
        SkillPath.LUCKY: SkillTypeFlag.AGILE | SkillTypeFlag.SUPERNATURAL,
        SkillPath.MANAGER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.MECHANIC: SkillTypeFlag.SMART | SkillTypeFlag.OBSERVANT,
        SkillPath.PARANORMAL: SkillTypeFlag.SUPERNATURAL,
        SkillPath.PILGRIM: SkillTypeFlag.SUPERNATURAL,
        SkillPath.POLITICIAN: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.PSYCHOLOGIST: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.SIGNALER: SkillTypeFlag.SMART | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE,
        SkillPath.SOCIALITE: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.SPORTER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.SUPPORTER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT,
        SkillPath.TRAINER: SkillTypeFlag.STRONG | SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE,
        SkillPath.TRAVELER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,
        SkillPath.TWOLEG: SkillTypeFlag.SMART,
        SkillPath.VOLUNTEER: SkillTypeFlag.SOCIAL,
        SkillPath.WRESTLER: SkillTypeFlag.STRONG | SkillTypeFlag.AGILE,

        SkillPath.MYTHOLOGICAL: SkillTypeFlag.SOCIAL,
        SkillPath.LEARNER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.AGILE | SkillTypeFlag.SMART,
        SkillPath.COMPETITOR: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.STRONG,
        SkillPath.CHALLENGER: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.STRONG, 
        SkillPath.BEHAVIORIST: SkillTypeFlag.SOCIAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SMART, 
        SkillPath.HAUNTED: SkillTypeFlag.OBSERVANT | SkillTypeFlag.SUPERNATURAL,
        SkillPath.RESURRECTED: SkillTypeFlag.SUPERNATURAL,

        SkillPath.PROJECTOR: SkillTypeFlag.SUPERNATURAL,
        SkillPath.RETRIEVER: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL,
        SkillPath.EXTRACTOR: SkillTypeFlag.SUPERNATURAL,
        SkillPath.PURIFIER: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.TRANCER: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT,
        SkillPath.DIVINER: SkillTypeFlag.SUPERNATURAL | SkillTypeFlag.OBSERVANT | SkillTypeFlag.SOCIAL
    }

    # pylint: enable=unsupported-binary-operation

    def __init__(
        self,
        skill_dict=None,
        primary_path: SkillPath = None,
        primary_points: int = 0,
        secondary_path: SkillPath = None,
        secondary_points: int = 0,
        hidden_skill: HiddenSkillEnum = None,
        interest_only=False,
    ):

        if skill_dict:
            self.primary = Skill.generate_from_save_string(skill_dict["primary"])
            self.secondary = Skill.generate_from_save_string(skill_dict["secondary"])
            self.hidden = (
                HiddenSkillEnum[skill_dict["hidden"]] if skill_dict["hidden"] else None
            )
        else:
            if primary_path:
                self.primary = Skill(primary_path, primary_points, interest_only)
            else:
                self.primary = None
            if secondary_path:
                self.secondary = Skill(secondary_path, secondary_points, interest_only)
            else:
                self.secondary = None

            self.hidden = hidden_skill

    def __repr__(self) -> str:
        return f"<CatSkills: Primary: |{self.primary}|, Secondary: |{self.secondary}|, Hidden: |{self.hidden}|>"

    @staticmethod
    def generate_new_catskills(status, moons, hidden_skill: HiddenSkillEnum = None):
        """Generates a new skill"""
        new_skill = CatSkills()

        new_skill.hidden = hidden_skill

        # TODO: Make this nicer
        if status == "newborn" or moons <= 0:
            pass
        elif status == "kitten" or moons < 6:
            new_skill.primary = Skill.get_random_skill(points=0, interest_only=True)
        elif status == "apprentice":
            new_skill.primary = Skill.get_random_skill(point_tier=1, interest_only=True)
            if random.randint(1, 3) == 1:
                new_skill.secondary = Skill.get_random_skill(
                    point_tier=1, interest_only=True, exclude=new_skill.primary.path
                )
        elif moons < 50:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(1, 2))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(
                    point_tier=random.randint(1, 2), exclude=new_skill.primary.path
                )
        elif moons < 100:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(1, 3))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(
                    point_tier=random.randint(1, 2), exclude=new_skill.primary.path
                )
        elif moons < 150:
            new_skill.primary = Skill.get_random_skill(point_tier=random.randint(2, 3))
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(
                    point_tier=random.randint(1, 2), exclude=new_skill.primary.path
                )
        else:
            new_skill.primary = Skill.get_random_skill(point_tier=1)
            if random.randint(1, 2) == 1:
                new_skill.secondary = Skill.get_random_skill(
                    point_tier=1, exclude=new_skill.primary.path
                )

        return new_skill

    def get_skill_dict(self):
        return {
            "primary": self.primary.get_save_string() if self.primary else None,
            "secondary": self.secondary.get_save_string() if self.secondary else None,
            "hidden": self.hidden.name if self.hidden else None,
        }

    def skill_string(self, short=False):
        output = []

        if short:
            if self.primary:
                output.append(self.primary.get_short_skill())
            if self.secondary:
                output.append(self.secondary.get_short_skill())
        else:
            if self.primary:
                output.append(self.primary.skill)
            if self.secondary:
                output.append(self.secondary.skill)

        if not output:
            return "???"

        return " & ".join(output)

    def mentor_influence(self, mentor):
        """Handles mentor influence on the cat's skill
        :param mentor: the mentor's cat object
        """

        if not mentor:
            return

        # Determine if any skills can be effected
        mentor_tags = (
            CatSkills.influence_flags[mentor.skills.primary.path]
            if mentor.skills.primary
            else None
        )

        can_primary = (
            bool(CatSkills.influence_flags[self.primary.path] & mentor_tags)
            if self.primary and mentor_tags
            else False
        )
        can_secondary = (
            bool(CatSkills.influence_flags[self.secondary.path] & mentor_tags)
            if self.secondary and mentor_tags
            else False
        )

        # If nothing can be effected, just return as well.
        if not (can_primary or can_secondary):
            return

        amount_effect = random.randint(1, 4)

        if can_primary and can_secondary:
            if random.randint(1, 2) == 1:
                self.primary.points += amount_effect
                path = self.primary.path
            else:
                self.secondary.points += amount_effect
                path = self.secondary.path
        elif can_primary:
            self.primary.points += amount_effect
            path = self.primary.path
        else:
            self.secondary.points += amount_effect
            path = self.secondary.path

        return mentor.ID, path, amount_effect

    def progress_skill(self, the_cat):
        """
        this function should be run every moon for every cat to progress their skills accordingly
        :param the_cat: the cat object for affected cat
        """
        if the_cat.status == "newborn" or the_cat.moons <= 0:
            return

        # Give a primary is there isn't one already, and the cat is older than one moon.
        if not self.primary:
            parents = [
                the_cat.fetch_cat(i)
                for i in [the_cat.parent1, the_cat.parent2] + the_cat.adoptive_parents
                if type(the_cat) == type(the_cat.fetch_cat(i))
            ]
            parental_paths = [
                i.skills.primary.path for i in parents if i.skills.primary
            ] + [i.skills.secondary.path for i in parents if i.skills.secondary]

            # If there are parental paths, flip a coin to determine if they will get a parents path
            if parental_paths and random.randint(0, 1):
                self.primary = Skill(
                    random.choice(parental_paths),
                    points=0,
                    interest_only=(
                        True if the_cat.status in ["apprentice", "kitten"] else False
                    ),
                )
            else:
                self.primary = Skill.get_random_skill(
                    points=0,
                    interest_only=(
                        True if the_cat.status in ["apprentice", "kitten"] else False
                    ),
                )

        if not (the_cat.outside or the_cat.exiled):
            if the_cat.status == "kitten":
                # Check to see if the cat gains a secondary
                if not self.secondary and not int(random.random() * 22):
                    # if there's no secondary skill, try to give one!
                    self.secondary = Skill.get_random_skill(
                        points=0, interest_only=True, exclude=self.primary.path
                    )

                # if the the_cat has skills, check if they get any points this moon
                if not int(random.random() * 4):
                    amount_effect = random.randint(1, 4)
                    if self.primary and self.secondary:
                        if random.randint(1, 2) == 1:
                            self.primary.points += amount_effect
                        else:
                            self.secondary.points += amount_effect
                    elif self.primary:
                        self.primary.points += amount_effect

            elif "apprentice" in the_cat.status:
                # Check to see if the cat gains a secondary
                if not self.secondary and not int(random.random() * 22):
                    # if there's no secondary skill, try to give one!
                    self.secondary = Skill.get_random_skill(
                        points=0, interest_only=True, exclude=self.primary.path
                    )

                # Check if they get any points this moon
                if not int(random.random() * 4):
                    amount_effect = random.randint(2, 5)
                    if self.primary and self.secondary:
                        if random.randint(1, 2) == 1:
                            self.primary.points += amount_effect
                        else:
                            self.secondary.points += amount_effect
                    elif self.primary:
                        self.primary.points += amount_effect

            elif the_cat.moons > 120:
                # for old cats, we want to check if the skills start to degrade at all, age is the great equalizer

                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False

                chance = max(1, 160 - the_cat.moons)
                if not int(
                    random.random() * chance
                ):  # chance increases as the_cat ages
                    self.primary.points -= 1
                    if self.secondary:
                        self.secondary.points -= 1
            else:
                # If they are still in "interest" stage, there is a change to swap primary and secondary
                # If they are still in "interest" but reached this part, they just graduated.
                if self.primary.interest_only and self.secondary:
                    flip = random.choices(
                        [False, True],
                        [self.primary.points + 1, self.secondary.points + 1],
                    )[0]
                    if flip:
                        _temp = self.primary
                        self.primary = self.secondary
                        self.secondary = _temp

                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False

                # If a cat doesn't can a secondary, have a small change for them to get one.
                # but, only a first-tier skill.
                if not self.secondary and not int(random.random() * 300):
                    self.secondary = Skill.get_random_skill(
                        exclude=self.primary.path, point_tier=1
                    )

                # There is a change for primary to condinue to improve throughout life
                # That chance decreases as the cat gets older.
                # This is to simulate them reaching their "peak"
                if not int(random.random() * int(the_cat.moons / 4)):
                    self.primary.points += 1
        else:
            # For outside cats, just check interest and flip it if needed.
            # Going on age, rather than status here.
            if the_cat.age not in ["kitten", "adolescent"]:
                self.primary.interest_only = False
                if self.secondary:
                    self.secondary.interest_only = False

    def meets_skill_requirement(
        self, path: Union[str, SkillPath, HiddenSkillEnum], min_tier: int = 0
    ) -> bool:
        """Check if a cat meets a given skill requirement.

        :param Union[str, SkillPath, HiddenSkillEnum] path: todo: someone describe this amalgam
        :param int min_tier: the lowest tier of skill that will pass this test
        :return bool: True if cat meets skill requirement
        """

        if isinstance(path, str):
            # Try to conter to Skillpath or HiddenSkillEnum
            try:
                path = SkillPath[path]
            except KeyError:
                try:
                    path = HiddenSkillEnum[path]
                except KeyError:
                    print(f"{path} is not a real skill path")
                    return False

        if isinstance(path, HiddenSkillEnum):
            if path == self.hidden:
                return True
        elif isinstance(path, SkillPath):
            if self.primary:
                if path == self.primary.path and self.primary.tier >= min_tier:
                    return True

            if self.secondary:
                if path == self.secondary.path and self.secondary.tier >= min_tier:
                    return True

        return False

    def check_skill_requirement_list(self, skill_list: list) -> int:
        """Takes a whole list of skill requirements in the form
        [ "SKILL_PATH,MIN_TIER" ... ] and determines how many skill
        requirements are met. The list format is used in all patrol and event skill
        restrictions. Returns an integer value of how many skills requirements are met.
        """
        skills_meet = 0
        min_tier = 0
        for _skill in skill_list:
            spl = _skill.split(",")

            if len(spl) != 2:
                print("Incorrectly formatted skill restriction", _skill)
                continue
            try:
                min_tier = int(spl[1])
            except ValueError:
                print("Min Skill Tier cannot be converted to int", _skill)
                continue

            if self.meets_skill_requirement(spl[0], min_tier):
                skills_meet += 1

        return skills_meet

    @staticmethod
    def get_skills_from_old(old_skill, status, moons):
        """Generates a CatSkill object"""
        new_skill = CatSkills()
        conversion = {
            "strong connection to StarClan": (SkillPath.STAR, 2),
            "good healer": (SkillPath.HEALER, 1),
            "great healer": (SkillPath.HEALER, 2),
            "fantastic healer": (SkillPath.HEALER, 3),
            "good teacher": (SkillPath.TEACHER, 1),
            "great teacher": (SkillPath.TEACHER, 2),
            "fantastic teacher": (SkillPath.TEACHER, 3),
            "good mediator": (SkillPath.MEDIATOR, 1),
            "great mediator": (SkillPath.MEDIATOR, 2),
            "excellent mediator": (SkillPath.MEDIATOR, 3),
            "smart": (SkillPath.CLEVER, 1),
            "very smart": (SkillPath.CLEVER, 2),
            "extremely smart": (SkillPath.CLEVER, 3),
            "good hunter": (SkillPath.HUNTER, 1),
            "great hunter": (SkillPath.HUNTER, 2),
            "fantastic hunter": (SkillPath.HUNTER, 3),
            "good fighter": (SkillPath.FIGHTER, 1),
            "great fighter": (SkillPath.FIGHTER, 2),
            "excellent fighter": (SkillPath.FIGHTER, 3),
            "good speaker": (SkillPath.SPEAKER, 1),
            "great speaker": (SkillPath.SPEAKER, 2),
            "excellent speaker": (SkillPath.SPEAKER, 3),
            "good storyteller": (SkillPath.STORY, 1),
            "great storyteller": (SkillPath.STORY, 2),
            "fantastic storyteller": (SkillPath.STORY, 3),
            "smart tactician": (SkillPath.INSIGHTFUL, 1),
            "valuable tactician": (SkillPath.INSIGHTFUL, 2),
            "valuable insight": (SkillPath.INSIGHTFUL, 3),
            "good kitsitter": (SkillPath.KIT, 1),
            "great kitsitter": (SkillPath.KIT, 2),
            "beloved kitsitter": (SkillPath.KIT, 3),
            "camp keeper": (SkillPath.CAMP, 3),
            "den builder": (SkillPath.CAMP, 2),
            "omen sight": (SkillPath.OMEN, 3),
            "dream walker": (SkillPath.DREAM, 2),
            "clairvoyant": (SkillPath.CLAIRVOYANT, 2),
            "prophet": (SkillPath.PROPHET, 3),
            "lore keeper": (SkillPath.LORE, 2),
            "keen eye": (SkillPath.SENSE, 2),

            "grows herbs": (SkillPath.GARDENER, 1),
            "herb organizer": (SkillPath.GARDENER, 2),
            "caretaker of the greens": (SkillPath.GARDENER, 3),
            "light sleeper": (SkillPath.WAKEFUL, 1),
            "alert": (SkillPath.WAKEFUL, 2),
            "vigilant": (SkillPath.WAKEFUL, 3),
            "helpful stork": (SkillPath.DELIVERER, 1),
            "kit deliverer": (SkillPath.DELIVERER, 2),
            "pregnancy expert": (SkillPath.DELIVERER, 3),
            "crafty paws": (SkillPath.DECORATOR, 1),
            "creative": (SkillPath.DECORATOR, 2),
            "decor master": (SkillPath.DECORATOR, 3),
            "leads patrols": (SkillPath.LEADERSHIP, 1),
            "leader's accomplice": (SkillPath.LEADERSHIP, 2),
            "assiduous": (SkillPath.LEADERSHIP, 3),
            "light-footed": (SkillPath.AGILE, 1),
            "lithe": (SkillPath.AGILE, 2),
            "quick agilist": (SkillPath.AGILE, 3),
            "memorious": (SkillPath.MEMORY, 1),
            "retentive memory": (SkillPath.MEMORY, 2),
            "mnemonist": (SkillPath.MEMORY, 3),
            "message-bearer": (SkillPath.MESSENGER, 1),
            "message-carrier": (SkillPath.MESSENGER, 2),
            "harbinger to the clans": (SkillPath.MESSENGER, 3),
            "assist guard": (SkillPath.ASSIST, 1),
            "alert assistant": (SkillPath.ASSIST, 2),
            "camp's assister": (SkillPath.ASSIST, 3),
            "bookkeeper": (SkillPath.HISTORIAN, 1),
            "archivist": (SkillPath.HISTORIAN, 2),
            "accountant of history": (SkillPath.HISTORIAN, 3),
            "journalist": (SkillPath.BOOKMAKER, 1),
            "novelist": (SkillPath.BOOKMAKER, 2),
            "author of many stories": (SkillPath.BOOKMAKER, 3),
            "serene": (SkillPath.PATIENT, 1),
            "even-tempered": (SkillPath.PATIENT, 2),
            "equanimous": (SkillPath.PATIENT, 3),
            "elementary case-solver": (SkillPath.DETECTIVE, 1),
            "great sleuth": (SkillPath.DETECTIVE, 2),
            "masterful detective": (SkillPath.DETECTIVE, 3),
            "herbal inventor": (SkillPath.HERBALIST, 1),
            "poison maker": (SkillPath.HERBALIST, 2),
            "creator of remedies": (SkillPath.HERBALIST, 3),
            "knows alot of facts": (SkillPath.PRODIGY, 1),
            "smart role model": (SkillPath.PRODIGY, 2),
            "seen as an omen": (SkillPath.PRODIGY, 3),
            "knowledgeable explorer": (SkillPath.EXPLORER, 1),
            "brave pathfinder": (SkillPath.EXPLORER, 2),
            "master of territories": (SkillPath.EXPLORER, 3),
            "proficient tracker": (SkillPath.TRACKER, 1),
            "great tracker": (SkillPath.TRACKER, 2),
            "masterful tracker": (SkillPath.TRACKER, 3),
            "good guard": (SkillPath.GUARDIAN, 1),
            "great guard": (SkillPath.GUARDIAN, 2),
            "guardian": (SkillPath.GUARDIAN, 3),
            "good tunneler": (SkillPath.TUNNELER, 1),
            "great tunneler": (SkillPath.TUNNELER, 2),
            "fantastic tunneler": (SkillPath.TUNNELER, 3),
            "good navigator": (SkillPath.NAVIGATOR, 1),
            "great navigator": (SkillPath.NAVIGATOR, 2),
            "pathfinder": (SkillPath.NAVIGATOR, 3),
            "good singer": (SkillPath.SONG, 1),
            "great singer": (SkillPath.SONG, 2),
            "captivating singer": (SkillPath.SONG, 3),
            "graceful": (SkillPath.GRACE, 1),
            "elegant": (SkillPath.GRACE, 2),
            "radiates elegance": (SkillPath.GRACE, 3),
            "fur-care enthusiast": (SkillPath.CLEAN, 1),
            "meticulous cleaner": (SkillPath.CLEAN, 2),
            "master of aesthetics": (SkillPath.CLEAN, 3),
            "problem solver": (SkillPath.INNOVATOR, 1),
            "creator of solutions": (SkillPath.INNOVATOR, 2),
            "visionary thinker": (SkillPath.INNOVATOR, 3),
            "comforting presence": (SkillPath.COMFORTER, 1),
            "nightmare soother": (SkillPath.COMFORTER, 2),
            "boogeyman-fighter": (SkillPath.COMFORTER, 3),
            "relationship advisor": (SkillPath.MATCHMAKER, 1),
            "skilled heart-reader": (SkillPath.MATCHMAKER, 2),
            "masterful matchmaker": (SkillPath.MATCHMAKER, 3),
            "out-of-the-box thinker": (SkillPath.THINKER, 1),
            "paradox enthusiast": (SkillPath.THINKER, 2),
            "philosopher": (SkillPath.THINKER, 3),
            "good sport": (SkillPath.COOPERATIVE, 1),
            "team player": (SkillPath.COOPERATIVE, 2),
            "insider": (SkillPath.COOPERATIVE, 3),
            "well-versed": (SkillPath.SCHOLAR, 1),
            "incredibly knowledgeable": (SkillPath.SCHOLAR, 2),
            "polymath": (SkillPath.SCHOLAR, 3),
            "always busy": (SkillPath.TIME, 1),
            "coordinated": (SkillPath.TIME, 2),
            "efficiency aficionado": (SkillPath.TIME, 3),
            "item stasher": (SkillPath.TREASURE, 1),
            "trinket stower": (SkillPath.TREASURE, 2),
            "treasure keeper": (SkillPath.TREASURE, 3),
            "grazes fish": (SkillPath.FISHER, 1),
            "fish-catcher": (SkillPath.FISHER, 2),
            "gold star fishercat": (SkillPath.FISHER, 3),
            "dog-whisperer": (SkillPath.LANGUAGE, 1),
            "multilingual": (SkillPath.LANGUAGE, 2),
            "listener of all voices": (SkillPath.LANGUAGE, 3),
            "sunhigh log": (SkillPath.SLEEPER, 1),
            "dormouse": (SkillPath.SLEEPER, 2),
            "leader of SnoozeClan": (SkillPath.SLEEPER, 3),
            "creator of appearances": (SkillPath.DISGUISE, 1),
            "skillful disguiser": (SkillPath.DISGUISE, 2), 
            "shapeshifter": (SkillPath.DISGUISE, 3),
            "messes with embers": (SkillPath.PYRO, 1),
            "spark master": (SkillPath.PYRO, 2),
            "fire starter": (SkillPath.PYRO, 3),
            "great firefighter": (SkillPath.HYDRO, 1),
            "excellent extinguisher": (SkillPath.HYDRO, 2),
            "masterful extinguisher": (SkillPath.HYDRO, 3),
            "nice giftgiver": (SkillPath.GIFTGIVER, 1),
            "excellent giftgiver": (SkillPath.GIFTGIVER, 2),
            "always gives gifts": (SkillPath.GIFTGIVER, 3),
            "knows who to trust": (SkillPath.VIBES, 1),
            "mood reader": (SkillPath.VIBES, 2),
            "vibe detector": (SkillPath.VIBES, 3),
            "night vision": (SkillPath.STARGAZER, 1),
            "star-filled eyes": (SkillPath.STARGAZER, 2),
            "celestial insight": (SkillPath.STARGAZER, 3),
            "better immune system": (SkillPath.IMMUNE, 1),
            "strong immune system": (SkillPath.IMMUNE, 2),
            "constant germ immunity": (SkillPath.IMMUNE, 3),
            "nice singing": (SkillPath.MUSICVIBES, 1),
            "beautiful singing": (SkillPath.MUSICVIBES, 2),
            "lovely singing": (SkillPath.MUSICVIBES, 3),
            "friendly aura": (SkillPath.AURAVIBES, 1),
            "calming aura": (SkillPath.AURAVIBES, 2),
            "pleasant aura": (SkillPath.AURAVIBES, 3),
            "loves to care for animals": (SkillPath.ANIMALTAKER, 1),
            "wildlife friend": (SkillPath.ANIMALTAKER, 2),
            "deep animal-lover": (SkillPath.ANIMALTAKER, 3),
            "helps animals": (SkillPath.VET, 1),
            "animal soother": (SkillPath.VET, 2),
            "woodland healer": (SkillPath.VET, 3),
            "attracts animals": (SkillPath.ANIMALMAGNET, 1),
            "animals gather around them": (SkillPath.ANIMALMAGNET, 2),
            "animal magnet": (SkillPath.ANIMALMAGNET, 3),

            "performs unique roles": (SkillPath.ACTING, 1),
            "skilled performer": (SkillPath.ACTING, 2),
            "great actor": (SkillPath.ACTING, 3),
            "rallies for support": (SkillPath.ADVOCATE, 1),
            "supports causes": (SkillPath.ADVOCATE, 2),
            "speaks for others": (SkillPath.ADVOCATE, 3),
            "Twoleg enthusiast": (SkillPath.ANTHROPOLOGIST, 1),
            "Kittypet sympathizer": (SkillPath.ANTHROPOLOGIST, 2),
            "Kittypet affinity": (SkillPath.ANTHROPOLOGIST, 3),
            "digs up graves": (SkillPath.ARCHAEOLOGIST, 1),
            "analyzes skeletal remains": (SkillPath.ARCHAEOLOGIST, 2),
            "skeletal collector": (SkillPath.ARCHAEOLOGIST, 3),
            "recounts past events": (SkillPath.ARCHIVER, 1),
            "trained fact checker": (SkillPath.ARCHIVER, 2),
            "expert archiver": (SkillPath.ARCHIVER, 3),
            "crafts flower accessories": (SkillPath.ARRANGER, 1),
            "trained florist": (SkillPath.ARRANGER, 2),
            "flower arranger": (SkillPath.ARRANGER, 3),
            "investigates codebreakers": (SkillPath.ASSASSIN, 1),
            "bloodhound": (SkillPath.ASSASSIN, 2),
            "bounty hunter": (SkillPath.ASSASSIN, 3),
            "crafts pretty accessories": (SkillPath.ARTIFICER, 1),
            "designs accessories": (SkillPath.ARTIFICER, 2),
            "accessory crafter": (SkillPath.ARTIFICER, 3),
            "creative affinity": (SkillPath.ARTISAN, 1),
            "artistically talented": (SkillPath.ARTISAN, 2),
            "masterful artisan": (SkillPath.ARTISAN, 3),
            "guided by the stars": (SkillPath.ASTRONOMER, 1),
            "star lore expert": (SkillPath.ASTRONOMER, 2),
            "trained astronomer": (SkillPath.ASTRONOMER, 3),
            "notices aura": (SkillPath.AURA, 1),
            "studies aura patterns": (SkillPath.AURA, 2),
            "aura reader": (SkillPath.AURA, 3),
            "graceful moves": (SkillPath.BALANCE, 1),
            "balancer": (SkillPath.BALANCE, 2),
            "expert acrobatics": (SkillPath.BALANCE, 3),
            "forms wooden items": (SkillPath.CARPENTER, 1),
            "whittles wood": (SkillPath.CARPENTER, 2),
            "carpenter": (SkillPath.CARPENTER, 3),
            "powerful crusader": (SkillPath.CHAMPION, 1),
            "mighty knight": (SkillPath.CHAMPION, 2),
            "great champion": (SkillPath.CHAMPION, 3),
            "collects resources": (SkillPath.COLLECTOR, 1),
            "known hoarder": (SkillPath.COLLECTOR, 2),
            "skilled collector": (SkillPath.COLLECTOR, 3),
            "jokes around": (SkillPath.COMEDIAN, 1),
            "entertainer": (SkillPath.COMEDIAN, 2),
            "comedy genius": (SkillPath.COMEDIAN, 3),
            "leads mock battles": (SkillPath.COMMANDER, 1),
            "directs attacks": (SkillPath.COMMANDER, 2),
            "commands allies": (SkillPath.COMMANDER, 3),
            "weakens willpower": (SkillPath.COMPULSION, 1),
            "compels others": (SkillPath.COMPULSION, 2),
            "master manipulator": (SkillPath.COMPULSION, 3),
            "suffers hardships": (SkillPath.CURSED, 1),
            "encounters adversity": (SkillPath.CURSED, 2),
            "cursed bloodline": (SkillPath.CURSED, 3),
            "prances around": (SkillPath.DANCER, 1),
            "energetic mover": (SkillPath.DANCER, 2),
            "lively motion": (SkillPath.DANCER, 3),
            "smells death": (SkillPath.DEATH, 1),
            "grim reaper": (SkillPath.DEATH, 2),
            "angel of death": (SkillPath.DEATH, 3),
            "questions everything": (SkillPath.DEBATER, 1),
            "skilled debater": (SkillPath.DEBATER, 2),
            "serious debater": (SkillPath.DEBATER, 3),
            "deceptive words": (SkillPath.DECEPTOR, 1),
            "smooth talker": (SkillPath.DECEPTOR, 2),
            "master swindler": (SkillPath.DECEPTOR, 3),
            "judges misbehavior": (SkillPath.DISCIPLINE, 1),
            "administers discipline": (SkillPath.DISCIPLINE, 2),
            "atones for misconduct": (SkillPath.DISCIPLINE, 3),
            "pledges loyalty": (SkillPath.ENFORCER, 1),
            "code follower": (SkillPath.ENFORCER, 2),
            "code enforcer": (SkillPath.ENFORCER, 3),
            "fan favorite": (SkillPath.ENTERTAINER, 1),
            "massive following": (SkillPath.ENTERTAINER, 2),
            "beloved entertainer": (SkillPath.ENTERTAINER, 3),
            "proper greeter": (SkillPath.ETIQUETTE, 1),
            "respectfully cautious": (SkillPath.ETIQUETTE, 2),
            "adequately behaves": (SkillPath.ETIQUETTE, 3),
            "stretches legs": (SkillPath.EXERCISE, 1),
            "body trainer": (SkillPath.EXERCISE, 2),
            "muscle builder": (SkillPath.EXERCISE, 3),
            "evicts spirits": (SkillPath.EXORCIST, 1),
            "commands spirits": (SkillPath.EXORCIST, 2),
            "fearsome exorcist": (SkillPath.EXORCIST, 3),
            "dreams of the fae": (SkillPath.FAIRY, 1),
            "visited by fairies": (SkillPath.FAIRY, 2),
            "fairy kinship": (SkillPath.FAIRY, 3),
            "gathers fruits and seeds": (SkillPath.FORAGER, 1),
            "foraging dietician": (SkillPath.FORAGER, 2),
            "impressive forager": (SkillPath.FORAGER, 3),
            "observes land formations": (SkillPath.GEOGRAPHER, 1),
            "trained naturalist": (SkillPath.GEOGRAPHER, 2),
            "great geographer": (SkillPath.GEOGRAPHER, 3),
            "tends to burial grounds": (SkillPath.GRAVEKEEPER, 1),
            "burial caretaker": (SkillPath.GRAVEKEEPER, 2),
            "ancestral groundskeeper": (SkillPath.GRAVEKEEPER, 3),
            "engages in idle gossip": (SkillPath.GOSSIPER, 1),
            "promotes internal strife": (SkillPath.GOSSIPER, 2),
            "politically active": (SkillPath.GOSSIPER, 3),
            "watches over others": (SkillPath.GUARDING, 1),
            "camp guard": (SkillPath.GUARDING, 2),
            "respected warden": (SkillPath.GUARDING, 3),
            "offers advice": (SkillPath.GUIDER, 1),
            "guides others": (SkillPath.GUIDER, 2),
            "skilled guider": (SkillPath.GUIDER, 3),
            "animal whisperer": (SkillPath.HERDER, 1),
            "flock management": (SkillPath.HERDER, 2),
            "herder": (SkillPath.HERDER, 3),
            "blends into surroundings": (SkillPath.HIDING, 1),
            "natural colors": (SkillPath.HIDING, 2),
            "invisible hider": (SkillPath.HIDING, 3),
            "performs tricks": (SkillPath.ILLUSION, 1),
            "skilled illusionist": (SkillPath.ILLUSION, 2),
            "master of illusions": (SkillPath.ILLUSION, 3),
            "powerful fortitude": (SkillPath.FORTITUDE, 1),
            "high endurance": (SkillPath.FORTITUDE, 2),
            "strong constitution": (SkillPath.FORTITUDE, 3),
            "fierce gaze": (SkillPath.INTIMIDATION, 1),
            "threatening glare": (SkillPath.INTIMIDATION, 2),
            "intimidating presence": (SkillPath.INTIMIDATION, 3),
            "tinkers with random objects": (SkillPath.INVENTOR, 1),
            "constructs creations": (SkillPath.INVENTOR, 2),
            "inventor": (SkillPath.INVENTOR, 3),
            "prestigious lineage": (SkillPath.LEGACY, 1),
            "inherited status": (SkillPath.LEGACY, 2),
            "noble legacy": (SkillPath.LEGACY, 3),
            "deep thinker": (SkillPath.MEDITATION, 1),
            "reflects on life": (SkillPath.MEDITATION, 2),
            "meditative": (SkillPath.MEDITATION, 3),
            "soul speaker": (SkillPath.MEDIUM, 1),
            "spiritually intuitive": (SkillPath.MEDIUM, 2),
            "spirit medium": (SkillPath.MEDIUM, 3),
            "offers suggestions": (SkillPath.MENTALIST, 1),
            "diverts attention": (SkillPath.MENTALIST, 2),
            "calculated guesser": (SkillPath.MENTALIST, 3),
            "deflects criticism": (SkillPath.MINDER, 1),
            "controls public opinion": (SkillPath.MINDER, 2),
            "experienced minder": (SkillPath.MINDER, 3),
            "news bringer": (SkillPath.REPORTER, 1),
            "message giver": (SkillPath.REPORTER, 2),
            "grand herald": (SkillPath.REPORTER, 3),
            "copies vocal inflections": (SkillPath.MIMICKER, 1),
            "repetitive chatterer": (SkillPath.MIMICKER, 2),
            "perfect mimicry": (SkillPath.MIMICKER, 3),
            "highly aware": (SkillPath.MINDFUL, 1),
            "open mind": (SkillPath.MINDFUL, 2),
            "enlightened": (SkillPath.MINDFUL, 3),
            "tells the departed's tales": (SkillPath.MOURNER, 1),
            "honored eulogist": (SkillPath.MOURNER, 2),
            "devoted mourner": (SkillPath.MOURNER, 3),
            "offers solutions": (SkillPath.NEGOTIATOR, 1),
            "settles disputes": (SkillPath.NEGOTIATOR, 2),
            "negotiator": (SkillPath.NEGOTIATOR, 3),
            "defies death": (SkillPath.NECROMANCER, 1),
            "revives moribund": (SkillPath.NECROMANCER, 2),
            "necromancer": (SkillPath.NECROMANCER, 3),
            "assists healers": (SkillPath.NURSE, 1),
            "healer's assistant": (SkillPath.NURSE, 2),
            "nurse": (SkillPath.NURSE, 3),
            "makes speeches": (SkillPath.ORATOR, 1),
            "eloquent speaker": (SkillPath.ORATOR, 2),
            "known orator": (SkillPath.ORATOR, 3),
            "enthusiastic dauber": (SkillPath.PAINTER, 1),
            "inspiring illustrator": (SkillPath.PAINTER, 2),
            "experienced painter": (SkillPath.PAINTER, 3),
            "cares for others": (SkillPath.PARENTING, 1),
            "respected nurturer": (SkillPath.PARENTING, 2),
            "beloved caregiver": (SkillPath.PARENTING, 3),
            "offers praise": (SkillPath.PLANNER, 1),
            "hosts feasts": (SkillPath.PLANNER, 2),
            "plans parties": (SkillPath.PLANNER, 3),
            "starts games with others": (SkillPath.PLAYING, 1),
            "invents games": (SkillPath.PLAYING, 2),
            "game maker": (SkillPath.PLAYING, 3),
            "joins the dawn patrol": (SkillPath.PATROLLING, 1),
            "patrol enthusiast": (SkillPath.PATROLLING, 2),
            "patrol leader": (SkillPath.PATROLLING, 3),
            "drawn to emotions": (SkillPath.PSYCHIC, 1),
            "emotionally perceptive": (SkillPath.PSYCHIC, 2),
            "reads minds": (SkillPath.PSYCHIC, 3),
            "rhymes words together": (SkillPath.POET, 1),
            "eloquently speaks": (SkillPath.POET, 2),
            "renowned poet": (SkillPath.POET, 3),
            "acts oddly": (SkillPath.POSSESSED, 1),
            "otherworldly gaze": (SkillPath.POSSESSED, 2),
            "possessed": (SkillPath.POSSESSED, 3),
            "practices sermons": (SkillPath.PREACHER, 1),
            "spiritual leader": (SkillPath.PREACHER, 2),
            "respected preacher": (SkillPath.PREACHER, 3),
            "projects feelings": (SkillPath.PROJECTION, 1),
            "manifests perception": (SkillPath.PROJECTION, 2),
            "warps reality": (SkillPath.PROJECTION, 3),
            "attacks from a distance": (SkillPath.RANGER, 1),
            "sharpened aim": (SkillPath.RANGER, 2),
            "ranged attacks": (SkillPath.RANGER, 3),
            "regenerates health": (SkillPath.RECOVERER, 1),
            "hardy physique": (SkillPath.RECOVERER, 2),
            "instant recovery": (SkillPath.RECOVERER, 3),
            "haunted by the past": (SkillPath.REINCARNATED, 1),
            "lives in the past": (SkillPath.REINCARNATED, 2),
            "reincarnated": (SkillPath.REINCARNATED, 3),
            "discovers new concepts": (SkillPath.RESEARCHER, 1),
            "study evaluator": (SkillPath.RESEARCHER, 2),
            "detailed researcher": (SkillPath.RESEARCHER, 3),
            "undead vessel": (SkillPath.RISEN, 1),
            "risen walker": (SkillPath.RISEN, 2),
            "ghastly figure": (SkillPath.RISEN, 3),
            "invents rituals": (SkillPath.RITE, 1),
            "honors traditions": (SkillPath.RITE, 2),
            "master of ceremonies": (SkillPath.RITE, 3),
            "gathers worn material": (SkillPath.SCAVENGER, 1),
            "keeps all resources": (SkillPath.SCAVENGER, 2),
            "pack rat": (SkillPath.SCAVENGER, 3),
            "discord seeker": (SkillPath.SCHEMER, 1),
            "chaos bringer": (SkillPath.SCHEMER, 2),
            "trickster": (SkillPath.SCHEMER, 3),
            "surveys environment": (SkillPath.SCOUTER, 1),
            "reliable informant": (SkillPath.SCOUTER, 2),
            "scout": (SkillPath.SCOUTER, 3),
            "inscribes into stone": (SkillPath.SCRIBE, 1),
            "stonemason": (SkillPath.SCRIBE, 2),
            "scribe": (SkillPath.SCRIBE, 3),
            "enchanted lilt": (SkillPath.SIREN, 1),
            "hypnotic voice": (SkillPath.SIREN, 2),
            "warning call": (SkillPath.SIREN, 3),
            "gathers intelligence": (SkillPath.SPY, 1),
            "highly informed": (SkillPath.SPY, 2),
            "spymaster": (SkillPath.SPY, 3),
            "studies culture": (SkillPath.STARLESS, 1),
            "questions authority": (SkillPath.STARLESS, 2),
            "welcomes outsiders": (SkillPath.STARLESS, 3),
            "stays out of sight": (SkillPath.STEALTH, 1),
            "quiet pawsteps": (SkillPath.STEALTH, 2),
            "snake-like attacks": (SkillPath.STEALTH, 3),
            "thinks carefully": (SkillPath.STRATEGIST, 1),
            "detailed planner": (SkillPath.STRATEGIST, 2),
            "strategist": (SkillPath.STRATEGIST, 3),
            "tidies loose fur strands": (SkillPath.STYLIST, 1),
            "dappers pelt appearances": (SkillPath.STYLIST, 2),
            "stylizes fur": (SkillPath.STYLIST, 3),
            "talks with the supernatural": (SkillPath.SUMMONER, 1),
            "controls spirits": (SkillPath.SUMMONER, 2),
            "powerful spirit summoner": (SkillPath.SUMMONER, 3),
            "warm towards animals": (SkillPath.TAMER, 1),
            "accompanies animals": (SkillPath.TAMER, 2),
            "animal tamer": (SkillPath.TAMER, 3),
            "sneaky paws": (SkillPath.THIEF, 1),
            "cat burglar": (SkillPath.THIEF, 2),
            "criminal mastermind": (SkillPath.THIEF, 3),
            "reads minds": (SkillPath.TELEPATHIC, 1),
            "shares thoughts": (SkillPath.TELEPATHIC, 2),
            "expert telepath": (SkillPath.TELEPATHIC, 3),
            "insatiable curiosity": (SkillPath.TESTER, 1),
            "performs experiments": (SkillPath.TESTER, 2),
            "conducts trials": (SkillPath.TESTER, 3),
            "makes deals": (SkillPath.TRADER, 1),
            "supplies resources": (SkillPath.TRADER, 2),
            "traderer": (SkillPath.TRADER, 3),
            "vision interpreter": (SkillPath.VISION, 1),
            "predicts future": (SkillPath.VISION, 2),
            "masterful seer": (SkillPath.VISION, 3),
            "studies the weather": (SkillPath.WEATHER, 1),
            "predicts weather patterns": (SkillPath.WEATHER, 2),
            "weather expert": (SkillPath.WEATHER, 3),
            "careful claws": (SkillPath.WEATHER, 1),
            "mends items": (SkillPath.WEATHER, 2),
            "weaver": (SkillPath.WEATHER, 3),

            "gathers animal information": (SkillPath.ANIMALOGIST, 1),
            "trained zoologist": (SkillPath.ANIMALOGIST, 2),
            "expert zoologist": (SkillPath.ANIMALOGIST, 3),
            "invents combative tools": (SkillPath.ARMORER, 1),
            "handles weapon accessories": (SkillPath.ARMORER, 2),
            "oversees weaponry": (SkillPath.ARMORER, 3),
            "engages in muscle building": (SkillPath.BUILDER, 1),
            "strengthens muscles": (SkillPath.BUILDER, 2),
            "trained body builder": (SkillPath.BUILDER, 3),
            "gathers nesting materials": (SkillPath.CAMPER, 1),
            "sets up camps": (SkillPath.CAMPER, 2),
            "camp builder": (SkillPath.CAMPER, 3),
            "close friend": (SkillPath.COMPANION, 1),
            "trusted ally": (SkillPath.COMPANION, 2),
            "personal favorite": (SkillPath.COMPANION, 3),
            "gives relationship advice": (SkillPath.CONSULTANT, 1),
            "specializes in personal matters": (SkillPath.CONSULTANT, 2),
            "relationship consultant": (SkillPath.CONSULTANT, 3),
            "dives underwater": (SkillPath.DIVER, 1),
            "swims with fishes": (SkillPath.DIVER, 2),
            "plunges into deep waters": (SkillPath.DIVER, 3),
            "quick to take sides": (SkillPath.FOLLOWER, 1),
            "carefully chooses alliances": (SkillPath.FOLLOWER, 2),
            "loyal follower": (SkillPath.FOLLOWER, 3),
            "makes bold decision": (SkillPath.GAMBLER, 1),
            "sacrifices safety": (SkillPath.GAMBLER, 2),
            "daredevil": (SkillPath.GAMBLER, 3),
            "guesses fur colors": (SkillPath.GENEALOGIST, 1),
            "predicts pelt types": (SkillPath.GENEALOGIST, 2),
            "foretells coat patterns": (SkillPath.GENEALOGIST, 3),
            "takes extended walks": (SkillPath.HIKER, 1),
            "skilled hiker": (SkillPath.HIKER, 2),
            "expert hiker": (SkillPath.HIKER, 3),
            "changes other's minds": (SkillPath.HYPNOTIST, 1),
            "implants false memories": (SkillPath.HYPNOTIST, 2),
            "powerful influence": (SkillPath.HYPNOTIST, 3),
            "offers first aid": (SkillPath.LIFESAVER, 1),
            "rescues others from danger": (SkillPath.LIFESAVER, 2),
            "savior figure": (SkillPath.LIFESAVER, 3),
            "has good luck": (SkillPath.LUCKY, 1),
            "pushes luck": (SkillPath.LUCKY, 2),
            "lucky streak": (SkillPath.LUCKY, 3),
            "assigns roles": (SkillPath.MANAGER, 1),
            "dictates tasks": (SkillPath.MANAGER, 2),
            "oversees projects": (SkillPath.MANAGER, 3),
            "plays with Twoleg objects": (SkillPath.MECHANIC, 1),
            "learns mechanical structures": (SkillPath.MECHANIC, 2),
            "makes helpful gadgets": (SkillPath.MECHANIC, 3),
            "watches mystical spirits": (SkillPath.PARANORMAL, 1),
            "memorizes supernatural entities": (SkillPath.PARANORMAL, 2),
            "paranormal lorekeeper": (SkillPath.PARANORMAL, 3),
            "takes care of shrines": (SkillPath.PILGRIM, 1),
            "traveling pilgrim": (SkillPath.PILGRIM, 2),
            "devoted worshipper": (SkillPath.PILGRIM, 3),
            "rallies for support": (SkillPath.POLITICIAN, 1),
            "persuasive charm": (SkillPath.POLITICIAN, 2),
            "drives personal agenda": (SkillPath.POLITICIAN, 3),
            "understands different perspectives": (SkillPath.PSYCHOLOGIST, 1),
            "studies cause and effect": (SkillPath.PSYCHOLOGIST, 2),
            "creates psychological profiles": (SkillPath.PSYCHOLOGIST, 3),
            "ensures collective safety": (SkillPath.GUARD, 1),
            "navigates dangerous surroundings": (SkillPath.GUARD, 2),
            "anticipates hazards": (SkillPath.GUARD, 3),
            "makes up tail signs": (SkillPath.SIGNALER, 1),
            "speaks in code": (SkillPath.SIGNALER, 2),
            "commands with signals": (SkillPath.SIGNALER, 3),
            "aristocratic power": (SkillPath.SOCIALITE, 1),
            "respected authority": (SkillPath.SOCIALITE, 2),
            "famous socialite": (SkillPath.SOCIALITE, 3),
            "trains with denmates": (SkillPath.SPORTER, 1),
            "skilled sporter": (SkillPath.SPORTER, 2),
            "master of a sport": (SkillPath.SPORTER, 3),
            "offers encouragement": (SkillPath.SUPPORTER, 1),
            "uplifts spirits": (SkillPath.SUPPORTER, 2),
            "strong moral support": (SkillPath.SUPPORTER, 3),
            "studies techniques": (SkillPath.TRAINER, 1),
            "focuses on weakness": (SkillPath.TRAINER, 2),
            "personal trainer": (SkillPath.TRAINER, 3),
            "sight seer": (SkillPath.TRAVELER, 1),
            "skilled tourist": (SkillPath.TRAVELER, 2),
            "expert traveler": (SkillPath.TRAVELER, 3),
            "part time kittypet": (SkillPath.TWOLEG, 1),
            "studies twoleg interactions": (SkillPath.TWOLEG, 2),
            "twoleg expert": (SkillPath.TWOLEG, 3),
            "eager helper": (SkillPath.VOLUNTEER, 1),
            "charitable soul": (SkillPath.VOLUNTEER, 2),
            "willing volunteer": (SkillPath.VOLUNTEER, 3),
            "has a strong grasp": (SkillPath.WRESTLER, 1),
            "wrestles opponents": (SkillPath.WRESTLER, 2),
            "expert wrestler": (SkillPath.WRESTLER, 3),

            "unique presence": (SkillPath.MYTHOLOGICAL, 1),
            "legendary ability": (SkillPath.MYTHOLOGICAL, 2),
            "mythological figure": (SkillPath.MYTHOLOGICAL, 3),
            "fast learner": (SkillPath.LEARNER, 1),
            "sharp memory": (SkillPath.LEARNER, 2),
            "expert memorizer": (SkillPath.LEARNER, 3),
            "organizes competitions": (SkillPath.COMPETITOR, 1),
            "skilled competitor": (SkillPath.COMPETITOR, 2),
            "talented competitor": (SkillPath.COMPETITOR, 3),
            "challenges others": (SkillPath.CHALLENGER, 1),
            "duel challenger": (SkillPath.CHALLENGER, 2),
            "sparring master": (SkillPath.CHALLENGER, 3),
            "notices behavioral changes": (SkillPath.BEHAVIORIST, 1),
            "examines behavior": (SkillPath.BEHAVIORIST, 2),
            "interprets intentions": (SkillPath.BEHAVIORIST, 3),
            "soul magnet": (SkillPath.HAUNTED, 1),
            "phantom charmer": (SkillPath.HAUNTED, 2),
            "haunted by specters": (SkillPath.HAUNTED, 3),
            "second chance": (SkillPath.RESURRECTED, 1),
            "borrowed time": (SkillPath.RESURRECTED, 2),
            "extended life": (SkillPath.RESURRECTED, 3),

            "projects consciousness": (SkillPath.PROJECTOR, 1),
            "walks with the dead": (SkillPath.PROJECTOR, 2),
            "afterlife visitor": (SkillPath.PROJECTOR, 3),
            "retrieves energy": (SkillPath.RETRIEVER, 1),
            "offers empowerment": (SkillPath.RETRIEVER, 2),
            "energizer": (SkillPath.RETRIEVER, 3),
            "focuses energy": (SkillPath.EXTRACTOR, 1),
            "channels other's energy": (SkillPath.EXTRACTOR, 2),
            "connected to life": (SkillPath.EXTRACTOR, 3),
            "sends waves of joy": (SkillPath.PURIFIER, 1),
            "light bringer": (SkillPath.PURIFIER, 2),
            "pure soul": (SkillPath.PURIFIER, 3),
            "goes into trances": (SkillPath.TRANCER, 1),
            "extended daydreams": (SkillPath.TRANCER, 2),
            "frequent musing": (SkillPath.TRANCER, 3),
            "deeply self-reflective": (SkillPath.DIVINER, 1),
            "gives life advice": (SkillPath.DIVINER, 2),
            "manifests futures": (SkillPath.DIVINER, 3),


        }

        old_skill = old_skill.strip()
        if old_skill in conversion:
            new_skill.primary = Skill(conversion[old_skill][0])
            new_skill.primary.set_points_to_tier(conversion[old_skill][1])
        else:
            new_skill = CatSkills.generate_new_catskills(status, moons)

        return new_skill
