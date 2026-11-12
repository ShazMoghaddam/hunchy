"""Geography (the hand-written part) and Cities & Landmarks."""

from . import Category, wiki

geo = Category("geography")

geo.choice("Which is the largest ocean on Earth?", "The Pacific", ["The Atlantic", "The Indian", "The Arctic"],
           "The Pacific covers about a third of the Earth's surface, more than all the land put together.",
           wiki("Pacific Ocean"), difficulty=1)
geo.choice("What is the highest mountain above sea level?", "Mount Everest", ["K2", "Kilimanjaro", "Mont Blanc"],
           "Everest's official height, agreed by China and Nepal in 2020, is 8,848.86 metres.",
           wiki("Mount Everest"), difficulty=1)
geo.choice("Which is the largest hot desert in the world?", "The Sahara", ["The Gobi", "The Kalahari", "The Arabian Desert"],
           "The Sahara covers about 9 million km² of North Africa. Antarctica, a cold desert, is even bigger.",
           wiki("Sahara"), difficulty=1)
geo.yes_no("Is Antarctica counted as a desert?", True,
           "A desert is a place with very little rain or snow. Antarctica gets so little that it is the largest desert on Earth.",
           wiki("Antarctica"), difficulty=2)
geo.choice("How many continents are there, in the way most countries teach it?", "Seven", ["Five", "Six", "Eight"],
           "Africa, Antarctica, Asia, Australia (or Oceania), Europe, North America and South America.",
           wiki("Continent"), difficulty=1)
geo.choice("Which is the longest river in the United Kingdom?", "The River Severn", ["The River Thames", "The River Trent", "The River Tay"],
           "The Severn runs about 354 km from the Welsh mountains to the Bristol Channel. The Thames is second.",
           wiki("River Severn"), difficulty=2)
geo.choice("What is the highest mountain in the United Kingdom?", "Ben Nevis", ["Snowdon", "Scafell Pike", "Slieve Donard"],
           "Ben Nevis, in the Scottish Highlands, is 1,345 metres high.",
           wiki("Ben Nevis"), difficulty=2)
geo.choice("Which river flows through Paris?", "The Seine", ["The Rhine", "The Loire", "The Thames"],
           "The Seine flows through the middle of Paris, under 37 bridges.",
           wiki("Seine"), difficulty=2)
geo.choice("Which line of latitude runs around the middle of the Earth?", "The Equator", ["The Tropic of Cancer", "The Prime Meridian", "The Arctic Circle"],
           "The Equator is about 40,075 km long and divides the Earth into the northern and southern hemispheres.",
           wiki("Equator"), difficulty=1)
geo.choice("Which is the largest island in the world (not counting Australia)?", "Greenland", ["Madagascar", "Borneo", "Great Britain"],
           "Greenland covers about 2.2 million km². Australia is counted as a continent rather than an island.",
           wiki("Greenland"), difficulty=2)

city = Category("landmarks")

city.higher_lower("The Eiffel Tower is about 330 metres tall. Is the Shard in London taller or shorter?", False,
                  "The Shard is 310 metres tall, the tallest building in the UK.",
                  wiki("The Shard"), labels=("Taller", "Shorter"), era="modern", difficulty=2)
city.choice("What is the tallest building in the world?", "Burj Khalifa", ["Shanghai Tower", "Empire State Building", "The Shard"],
            "The Burj Khalifa in Dubai is 828 metres tall. It opened in 2010.",
            wiki("Burj Khalifa"), era="modern", difficulty=1, as_of="2026-11")
city.higher_lower("The Burj Khalifa is 828 metres tall. Is the Empire State Building, to its tip, more or less than half that height?", False,
                  "The Empire State Building is 443 metres to the tip of its antenna, a little over half the height of the Burj Khalifa.",
                  wiki("Empire State Building"), labels=("More", "Less"), difficulty=3)
city.choice("In which city is the Colosseum?", "Rome", ["Athens", "Istanbul", "Naples"],
            "The Colosseum opened in AD 80 and could hold about 50,000 spectators.",
            wiki("Colosseum"), difficulty=1)
city.choice("In which country is Machu Picchu?", "Peru", ["Mexico", "Chile", "Bolivia"],
            "Machu Picchu is an Inca city high in the Andes mountains, built in the 1400s.",
            wiki("Machu Picchu"), difficulty=2)
city.choice("In which Indian city is the Taj Mahal?", "Agra", ["Delhi", "Mumbai", "Jaipur"],
            "The emperor Shah Jahan built the Taj Mahal in memory of his wife Mumtaz Mahal.",
            wiki("Taj Mahal"), difficulty=2)
city.choice("Which city is home to the Sydney Opera House?", "Sydney", ["Melbourne", "Canberra", "Auckland"],
            "It opened in 1973. Its roof looks like sails on the harbour.",
            wiki("Sydney Opera House"), difficulty=1)
city.choice("In which city is the Statue of Liberty?", "New York", ["Washington D.C.", "Boston", "Philadelphia"],
            "The statue was a gift from France and was put up in New York Harbor in 1886.",
            wiki("Statue of Liberty"), difficulty=1)
city.yes_no("Was the Statue of Liberty a gift from France?", True,
            "The people of France gave it to the United States. It was designed by Frédéric Auguste Bartholdi.",
            wiki("Statue of Liberty"), difficulty=1)
city.choice("What colour was the Statue of Liberty when it was first put up?", "Copper brown", ["Green", "Gold", "White"],
            "It was the colour of a shiny new penny. The copper slowly turned green as it reacted with the air, until it was fully green by about 1920.",
            wiki("Statue of Liberty"), difficulty=3)
city.choice("What is the name of the great bell inside London's famous clock tower?", "Big Ben", ["Great Tom", "Great George", "Great Paul"],
            "Big Ben is really the bell. The tower was renamed the Elizabeth Tower in 2012.",
            wiki("Big Ben"), difficulty=2)
city.choice("In which city is the Leaning Tower?", "Pisa", ["Florence", "Venice", "Bologna"],
            "The tower began to lean while it was still being built, in the 1170s, because the ground underneath was too soft.",
            wiki("Leaning Tower of Pisa"), difficulty=1)
city.choice("Which city has canals instead of streets and gondolas instead of taxis?", "Venice", ["Amsterdam", "Bruges", "Copenhagen"],
            "Venice is built on more than 100 small islands in a lagoon, linked by about 400 bridges.",
            wiki("Venice"), difficulty=1)
city.choice("In which city is the Sagrada Família, a church still being built more than a century after it was started?", "Barcelona", ["Madrid", "Seville", "Lisbon"],
            "Work began in 1882. The architect Antoni Gaudí spent the last 43 years of his life on it.",
            wiki("Sagrada Família"), difficulty=2)
city.choice("Which is the only one of the Seven Wonders of the Ancient World still standing?", "The Great Pyramid of Giza", ["The Colossus of Rhodes", "The Hanging Gardens of Babylon", "The Lighthouse of Alexandria"],
            "The Great Pyramid is also the oldest of the seven, built about 4,500 years ago.",
            wiki("Seven Wonders of the Ancient World"), difficulty=2)
city.true_false("You can see the Great Wall of China from the Moon with your own eyes.", False,
                "That's a myth. The wall is long but very narrow, and astronauts say it can't be seen from the Moon.",
                wiki("Great Wall of China"), difficulty=2)
city.choice("In which city is the famous Christ the Redeemer statue?", "Rio de Janeiro", ["São Paulo", "Buenos Aires", "Lima"],
            "The statue stands on top of Corcovado mountain, looking out over Rio. It was finished in 1931.",
            wiki("Christ the Redeemer (statue)"), difficulty=2)
city.choice("What is the name of the famous red bridge in San Francisco?", "The Golden Gate Bridge", ["The Brooklyn Bridge", "Tower Bridge", "The Bay Bridge"],
            "The Golden Gate Bridge opened in 1937. Its colour is called International Orange.",
            wiki("Golden Gate Bridge"), difficulty=1)
city.higher_lower("Tower Bridge in London opened in 1894. Did the Golden Gate Bridge open earlier or later?", False,
                  "The Golden Gate Bridge opened in 1937, 43 years after Tower Bridge.",
                  wiki("Golden Gate Bridge"), labels=("Earlier", "Later"), difficulty=2)
city.choice("In which city would you find the Brandenburg Gate?", "Berlin", ["Munich", "Vienna", "Prague"],
            "The gate stood right next to the Berlin Wall and became a symbol of Germany reunited.",
            wiki("Brandenburg Gate"), difficulty=2)
city.choice("Which famous museum has a glass pyramid at its entrance?", "The Louvre in Paris", ["The British Museum in London", "The Prado in Madrid", "The Met in New York"],
            "The glass pyramid, designed by I. M. Pei, opened in 1989.",
            wiki("Louvre Pyramid"), difficulty=2)
city.choice("Which ancient stone circle stands on Salisbury Plain in England?", "Stonehenge", ["Avebury", "Callanish", "Castlerigg"],
            "Stonehenge was built in stages over about 1,500 years, starting around 3000 BC.",
            wiki("Stonehenge"), difficulty=1)
city.choice("Which city is known as the Big Apple?", "New York", ["Los Angeles", "Chicago", "San Francisco"],
            "The nickname was made popular by a 1970s tourism campaign, though it was used decades earlier.",
            wiki("Big Apple"), difficulty=1)
city.choice("Which city is known as the City of Light?", "Paris", ["Rome", "Las Vegas", "Vienna"],
            "Paris earned the name as a centre of ideas and learning, and for being one of the first cities with gas street lights.",
            wiki("Paris"), difficulty=2)
city.choice("Which London landmark is a giant observation wheel on the South Bank?", "The London Eye", ["The Shard", "The Gherkin", "Battersea Power Station"],
            "The London Eye opened in 2000. A full turn takes about 30 minutes.",
            wiki("London Eye"), era="modern", difficulty=1)
city.choice("Which city hosted the Olympic Games in 2012?", "London", ["Beijing", "Rio de Janeiro", "Paris"],
            "London became the first city to host the modern Summer Olympics three times: 1908, 1948 and 2012.",
            wiki("2012 Summer Olympics"), era="modern", difficulty=1)
city.choice("Which city is the capital of Scotland?", "Edinburgh", ["Glasgow", "Aberdeen", "Dundee"],
            "Edinburgh Castle sits on the rock of an old volcano in the middle of the city.",
            wiki("Edinburgh"), difficulty=1)
city.choice("Which city is the capital of Wales?", "Cardiff", ["Swansea", "Newport", "Bangor"],
            "Cardiff has been the capital of Wales since 1955.",
            wiki("Cardiff"), difficulty=1)
city.choice("Which city is the capital of Northern Ireland?", "Belfast", ["Derry", "Armagh", "Newry"],
            "The Titanic was built in Belfast, at the Harland and Wolff shipyard.",
            wiki("Belfast"), difficulty=1)
city.choice("Which city has the most people in the world, counting its whole urban area?", "Jakarta", ["Tokyo", "Dhaka", "London"],
            "A United Nations report in late 2025, using a new way of measuring cities, put Jakarta top with nearly 42 million people, ahead of Dhaka and Tokyo.",
            ("UN DESA: Latest urbanization data reveal world's most populous cities", "https://desapublications.un.org/un-desa-voice/feature/december-2025/latest-urbanization-data-reveal-worlds-most-populous-cities"),
            era="modern", difficulty=3, as_of="2025")
city.choice("In which city is the Kremlin?", "Moscow", ["St Petersburg", "Kyiv", "Warsaw"],
            "The Kremlin is a walled fortress in the centre of Moscow. Next to it is Red Square.",
            wiki("Moscow Kremlin"), difficulty=2)
city.choice("Which city is split between two continents, Europe and Asia?", "Istanbul", ["Cairo", "Athens", "Moscow"],
            "The Bosphorus strait runs through Istanbul, with Europe on one side and Asia on the other.",
            wiki("Istanbul"), difficulty=2)
city.choice("In which city is the Acropolis?", "Athens", ["Rome", "Sparta", "Delphi"],
            "The Parthenon, a temple to the goddess Athena, stands on the Acropolis. It was finished in 432 BC.",
            wiki("Acropolis of Athens"), difficulty=1)
city.choice("Which Dutch city is famous for its canals and the Anne Frank House?", "Amsterdam", ["Rotterdam", "The Hague", "Utrecht"],
            "Amsterdam's ring of 17th-century canals is a UNESCO World Heritage Site.",
            wiki("Amsterdam"), difficulty=1)
city.choice("Which Scottish lake is famous for stories about a monster?", "Loch Ness", ["Loch Lomond", "Loch Tay", "Loch Awe"],
            "Loch Ness is so deep, about 230 metres, that it holds more fresh water than all the lakes in England and Wales put together.",
            wiki("Loch Ness"), difficulty=1)
city.choice("Which famous medieval clock in Prague's Old Town Square shows the positions of the Sun and Moon?", "The Astronomical Clock", ["The Cuckoo Clock", "The Floral Clock", "The Water Clock"],
            "Prague's Astronomical Clock was first installed in 1410. It is the oldest one still working.",
            wiki("Prague astronomical clock"), difficulty=3)
city.choice("Which city is home to the Little Mermaid statue?", "Copenhagen", ["Oslo", "Stockholm", "Helsinki"],
            "The statue, unveiled in 1913, is based on Hans Christian Andersen's fairy tale.",
            wiki("The Little Mermaid (statue)"), difficulty=2)
city.choice("Which American city is home to Hollywood?", "Los Angeles", ["San Francisco", "Las Vegas", "Miami"],
            "The Hollywood sign first went up in 1923 and originally said HOLLYWOODLAND.",
            wiki("Hollywood Sign"), difficulty=1)
city.higher_lower("Big Ben's clock tower is 96 metres tall. Is the Leaning Tower of Pisa taller or shorter?", False,
                  "The Leaning Tower of Pisa is about 56 metres tall on its high side.",
                  wiki("Leaning Tower of Pisa"), labels=("Taller", "Shorter"), difficulty=2)

city.choice("In which year was the Eiffel Tower finished?", "1889", ["1851", "1900", "1925"],
            "It was built for the 1889 World's Fair, marking 100 years since the French Revolution. It was meant to stand for only 20 years.",
            wiki("Eiffel Tower"), difficulty=2)
city.choice("In which country is Petra, the ancient city carved into pink rock?", "Jordan", ["Egypt", "Turkey", "Morocco"],
            "Petra was carved by the Nabataeans more than 2,000 years ago. It is one of the New Seven Wonders of the World.",
            wiki("Petra"), difficulty=2)
city.choice("In which country are the Maya pyramids of Chichén Itzá?", "Mexico", ["Peru", "Guatemala", "Egypt"],
            "The great pyramid, El Castillo, has 365 steps if you count the top platform: one for each day of the year.",
            wiki("Chichen Itza"), difficulty=2)
city.choice("Which canal links the Mediterranean Sea to the Red Sea?", "The Suez Canal", ["The Panama Canal", "The Corinth Canal", "The Kiel Canal"],
            "The Suez Canal opened in 1869. It saves ships sailing all the way round Africa.",
            wiki("Suez Canal"), difficulty=2)
city.choice("Which canal lets ships cross between the Atlantic and Pacific Oceans?", "The Panama Canal", ["The Suez Canal", "The Erie Canal", "The Grand Canal"],
            "The Panama Canal opened in 1914. Locks lift ships about 26 metres up to a lake and back down again.",
            wiki("Panama Canal"), difficulty=2)
city.choice("In which city is Times Square, famous for its giant screens and New Year's Eve ball drop?", "New York", ["Chicago", "Los Angeles", "Las Vegas"],
            "Times Square is named after The New York Times, which moved there in 1904.",
            wiki("Times Square"), difficulty=1)

assert len(geo.questions) == 10 and len(city.questions) == 45, (len(geo.questions), len(city.questions))
