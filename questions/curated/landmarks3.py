"""More famous places: great buildings, bridges, statues and natural wonders."""

from . import Category, wiki

c = Category("landmarks", prefix="landmarks3")

# The Great Wall of China -------------------------------------------------------------------------------
c.higher_lower("Counting all its branches, is the Great Wall of China more or less than 20,000 km long?", True,
               "A Chinese survey in 2012 measured all its sections at about 21,196 km. That's more than half way round the world.",
               wiki("Great Wall of China"), labels=("More", "Less"), difficulty=2)
c.yes_no("Was sticky rice mixed into the mortar of parts of the Great Wall of China?", True,
         "Builders in the Ming dynasty added sticky rice soup to lime mortar, which made it much stronger.",
         wiki("Great Wall of China"), difficulty=3)
c.choice("Which famous palace in Beijing was home to Chinese emperors for almost 500 years?", "The Forbidden City", ["The Summer Palace", "The Potala Palace", "The Temple of Heaven"],
         "Ordinary people weren't allowed in, which is how it got its name. It's now a museum.",
         wiki("Forbidden City"), difficulty=2)

# American wonders ------------------------------------------------------------------------------------
c.choice("In which US state is the Grand Canyon?", "Arizona", ["Colorado", "Utah", "Nevada"],
         "The river that carved it is the Colorado, but the canyon itself is in Arizona.",
         wiki("Grand Canyon"), difficulty=2)
c.choice("How many waterfalls make up Niagara Falls?", "3", ["1", "2", "5"],
         "Horseshoe Falls, American Falls and the small Bridal Veil Falls.",
         wiki("Niagara Falls"), difficulty=2)
c.choice("Who was the first person to go over Niagara Falls in a barrel and survive, in 1901?", "A 63-year-old schoolteacher", ["A circus strongman", "A teenage boy", "A trained stuntman"],
         "Annie Edson Taylor did it on her birthday, hoping to get rich. She warned others never to try it.",
         wiki("Annie Edson Taylor"), difficulty=3)
c.choice("Which famous engineer designed the iron frame inside the Statue of Liberty?", "Gustave Eiffel", ["Isambard Kingdom Brunel", "Thomas Edison", "Frank Lloyd Wright"],
         "The statue's sculptor was Frédéric Auguste Bartholdi. Eiffel built its skeleton a few years before his Paris tower.",
         wiki("Statue of Liberty"), difficulty=2)
c.choice("Which hand does the Statue of Liberty hold her torch in?", "Her right hand", ["Her left hand", "Both hands", "She holds a book, not a torch"],
         "Her left hand holds a tablet with the date of American independence, 4 July 1776, in Roman numerals.",
         wiki("Statue of Liberty"), difficulty=2)
c.choice("How many points are there on the Statue of Liberty's crown?", "7", ["5", "9", "12"],
         "They're often said to stand for the seven continents and seven seas.",
         wiki("Statue of Liberty"), difficulty=3)
c.choice("Which island prison in San Francisco Bay closed in 1963?", "Alcatraz", ["Rikers Island", "Robben Island", "Devil's Island"],
         "It's now a museum, and one of San Francisco's most visited sights.",
         wiki("Alcatraz Island"), difficulty=1)
c.higher_lower("The Empire State Building opened in 1931. Did building it take more or less than 18 months?", False,
               "It went up in about 410 days, around 13 months, often at more than four floors a week.",
               wiki("Empire State Building"), labels=("More", "Less"), difficulty=3)
c.choice("Which San Francisco street is famous for its eight tight hairpin bends?", "Lombard Street", ["Market Street", "Castro Street", "Haight Street"],
         "The bends were added in 1922 because the hill was too steep for cars to drive straight down.",
         wiki("Lombard Street (San Francisco)"), difficulty=2)
c.choice("Which giant dam on the Colorado River sits on the border of Nevada and Arizona?", "The Hoover Dam", ["The Three Gorges Dam", "The Aswan Dam", "The Grand Coulee Dam"],
         "It was finished in 1936 and holds back Lake Mead, the biggest reservoir in the United States.",
         wiki("Hoover Dam"), difficulty=2)
c.choice("Which New York bridge opened in 1883 and was the first to use steel wire cables?", "The Brooklyn Bridge", ["The George Washington Bridge", "The Manhattan Bridge", "The Verrazzano Bridge"],
         "To prove it was safe, P. T. Barnum led 21 elephants across it in 1884.",
         wiki("Brooklyn Bridge"), era="classic", difficulty=3)
c.choice("In which Canadian city is the CN Tower?", "Toronto", ["Vancouver", "Montreal", "Ottawa"],
         "It was the world's tallest free-standing structure for 32 years, until 2007.",
         wiki("CN Tower"), difficulty=2)
c.choice("Which American city is home to the Space Needle?", "Seattle", ["Houston", "Chicago", "San Francisco"],
         "It was built for the 1962 World's Fair.",
         wiki("Space Needle"), difficulty=2)

# Britain ------------------------------------------------------------------------------------------
c.choice("In 2012, Big Ben's clock tower was renamed to honour which monarch?", "Elizabeth II", ["Queen Victoria", "George VI", "Charles III"],
         "It became the Elizabeth Tower for her Diamond Jubilee. Big Ben is really the name of the bell.",
         wiki("Big Ben"), difficulty=2)
c.choice("Which birds are said to keep the kingdom safe as long as they stay at the Tower of London?", "Ravens", ["Pigeons", "Swans", "Owls"],
         "At least six are kept there at all times, looked after by a Ravenmaster.",
         wiki("Ravens of the Tower of London"), difficulty=1)
c.choice("Where are the Crown Jewels kept?", "The Tower of London", ["Buckingham Palace", "Windsor Castle", "Westminster Abbey"],
         "They're kept in the Jewel House and have been on show to the public since the 1600s.",
         wiki("Crown Jewels of the United Kingdom"), difficulty=1)
c.choice("Roughly how many rooms does Buckingham Palace have?", "775", ["120", "350", "1,500"],
         "Including 52 royal and guest bedrooms and 78 bathrooms.",
         wiki("Buckingham Palace"), difficulty=3)
c.choice("Edinburgh Castle sits on top of what?", "An old volcano", ["A man-made hill", "A sea cliff", "An ancient burial mound"],
         "Castle Rock is the plug of a volcano that last erupted about 350 million years ago.",
         wiki("Castle Rock, Edinburgh"), difficulty=2)
c.yes_no("Is Windsor Castle the oldest castle in the world that people still live in?", True,
         "It was begun by William the Conqueror after 1066, and kings and queens have lived there ever since.",
         wiki("Windsor Castle"), difficulty=2)
c.choice("What do visitors traditionally throw into Rome's Trevi Fountain?", "Coins", ["Flowers", "Bread", "Ribbons"],
         "Legend says throwing a coin over your shoulder means you'll come back to Rome. The money goes to charity.",
         wiki("Trevi Fountain"), difficulty=1)
c.higher_lower("Did the Colosseum in Rome hold more or fewer than 20,000 people?", True,
               "It held around 50,000 to 80,000. It's still the largest ancient amphitheatre ever built.",
               wiki("Colosseum"), labels=("More", "Fewer"), difficulty=2)
c.choice("Which French ruler ordered the Arc de Triomphe in Paris to be built?", "Napoleon", ["Louis XIV", "Charles de Gaulle", "Marie Antoinette"],
         "He ordered it in 1806 after his win at Austerlitz, but it wasn't finished until 1836.",
         wiki("Arc de Triomphe"), difficulty=2)
c.choice("In which city is the Atomium, a giant model of an iron crystal?", "Brussels", ["Amsterdam", "Geneva", "Vienna"],
         "It was built for the 1958 World's Fair and is 102 metres tall.",
         wiki("Atomium"), difficulty=3)
c.choice("Which island in France is cut off by the sea at high tide?", "Mont-Saint-Michel", ["Corsica", "Belle-Île", "Île de Ré"],
         "Its tides are among the strongest in Europe. Since 2014 a bridge lets visitors cross at any time.",
         wiki("Mont-Saint-Michel"), difficulty=2)
c.choice("Who designed the Sydney Opera House?", "Jørn Utzon, from Denmark", ["Frank Gehry, from Canada", "Zaha Hadid, from Iraq", "Norman Foster, from England"],
         "He won a competition in 1957 but left before it was finished, and never saw it completed.",
         wiki("Jørn Utzon"), difficulty=3)
c.choice("Which twin skyscrapers in Kuala Lumpur were the tallest buildings in the world from 1998 to 2004?", "The Petronas Towers", ["The Twin Towers", "The Shanghai Towers", "The Marina Bay Towers"],
         "A skybridge links them on the 41st and 42nd floors.",
         wiki("Petronas Towers"), difficulty=2)

# Natural wonders ----------------------------------------------------------------------------------
c.choice("What does Mosi-oa-Tunya, the local name for Victoria Falls, mean?", "The smoke that thunders", ["The river of gold", "The falling sky", "The white mountain"],
         "Its spray can rise hundreds of metres and be seen from far away.",
         wiki("Victoria Falls"), difficulty=3)
c.choice("Iguazu Falls, with around 275 waterfalls, lies on the border of Argentina and which country?", "Brazil", ["Chile", "Peru", "Uruguay"],
         "When the American First Lady Eleanor Roosevelt saw it, she reportedly said 'Poor Niagara!'",
         wiki("Iguazu Falls"), difficulty=2)
c.choice("On which island are the giant stone heads called moai?", "Easter Island", ["Tahiti", "Hawaii", "Fiji"],
         "There are almost 1,000 of them. Easter Island, or Rapa Nui, belongs to Chile.",
         wiki("Moai"), difficulty=1)
c.choice("Which is the largest freshwater lake in the world by area?", "Lake Superior", ["Lake Victoria", "Lake Baikal", "Lake Michigan"],
         "It's on the border of the USA and Canada. The Caspian Sea is bigger, but its water is salty.",
         wiki("Lake Superior"), difficulty=3)
c.choice("Which is the largest lake in Africa?", "Lake Victoria", ["Lake Tanganyika", "Lake Malawi", "Lake Chad"],
         "It's shared by Uganda, Kenya and Tanzania, and is a main source of the Nile.",
         wiki("Lake Victoria"), difficulty=2)
c.choice("Which desert, partly in Mongolia, is famous for dinosaur fossils?", "The Gobi", ["The Kalahari", "The Atacama", "The Mojave"],
         "The first dinosaur eggs known to science were found there in 1923.",
         wiki("Gobi Desert"), difficulty=2)
c.choice("What is the longest mountain range above sea level?", "The Andes", ["The Himalayas", "The Rockies", "The Alps"],
         "It runs about 7,000 km down the west side of South America.",
         wiki("Andes"), difficulty=2)
c.higher_lower("The Sahara is the biggest hot desert. Is it bigger or smaller than Australia?", True,
               "The Sahara covers about 9.2 million km², a bit bigger than Australia's 7.7 million.",
               wiki("Sahara"), labels=("Bigger", "Smaller"), difficulty=3)
c.choice("Which is the largest salt flat in the world, so flat and shiny that it mirrors the sky after rain?", "Salar de Uyuni, in Bolivia", ["Death Valley, in the USA", "The Dead Sea, in Jordan", "Lake Eyre, in Australia"],
         "It covers more than 10,000 km² and sits about 3,650 metres up in the Andes.",
         wiki("Salar de Uyuni"), difficulty=2)
c.choice("Which British territory, at the southern tip of Spain, is home to Europe's only wild monkeys?", "Gibraltar", ["Malta", "Cyprus", "The Channel Islands"],
         "About 300 Barbary macaques live on the Rock of Gibraltar. Legend says Britain will keep it as long as they stay.",
         wiki("Barbary macaques in Gibraltar"), difficulty=2)
