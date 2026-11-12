"""More geography: great rivers, the Arctic and Antarctic, the Equator, and the shape of the world."""

from . import Category, wiki, brit

c = Category("geography", prefix="geography2")

# The Nile ------------------------------------------------------------------------------------------
c.choice("Which river is usually named as the longest in the world?", "The Nile", ["The Amazon", "The Yangtze", "The Mississippi"],
         "The Nile is about 6,650 km long. Some scientists argue the Amazon is longer, depending on where you say it starts.",
         wiki("Nile"), difficulty=1)
c.yes_no("Does the River Nile flow from south to north?", True,
         "It rises in East Africa and flows north through Sudan and Egypt into the Mediterranean Sea.",
         wiki("Nile"), difficulty=2)
c.choice("In which city do the White Nile and the Blue Nile meet?", "Khartoum", ["Cairo", "Aswan", "Kampala"],
         "Khartoum is the capital of Sudan. Most of the Nile's water comes from the Blue Nile, which starts in Ethiopia.",
         wiki("Nile"), difficulty=3)
c.choice("Into which sea does the River Nile flow?", "The Mediterranean", ["The Red Sea", "The Arabian Sea", "The Black Sea"],
         "It spreads out into a huge fan-shaped delta north of Cairo before it reaches the sea.",
         wiki("Nile Delta"), difficulty=2)
c.choice("Which giant dam, finished in 1970, controls the Nile's yearly floods in Egypt?", "The Aswan High Dam", ["The Hoover Dam", "The Three Gorges Dam", "The Kariba Dam"],
         "Building its lake meant moving the ancient temples of Abu Simbel to higher ground, block by block.",
         wiki("Aswan Dam"), difficulty=3)
c.choice("The Nile's basin, all the land that drains into it, spreads across roughly how many countries?", "11", ["3", "6", "20"],
         "Eleven, from Tanzania and Ethiopia to Egypt. The basin covers about a tenth of Africa.",
         wiki("Nile"), difficulty=3)

# The Amazon ----------------------------------------------------------------------------------------
c.choice("Into which ocean does the Amazon River flow?", "The Atlantic", ["The Pacific", "The Indian", "The Southern"],
         "It pours out so much fresh water that the sea is less salty more than 100 km out from the shore.",
         wiki("Amazon River"), difficulty=2)
c.choice("Which country has the largest share of the Amazon rainforest?", "Brazil", ["Peru", "Colombia", "Bolivia"],
         "About 60% of the rainforest is in Brazil.",
         wiki("Amazon rainforest"), difficulty=1)
c.yes_no("Are there any bridges across the main Amazon River?", False,
         "Not one. It runs mostly through thick forest with few roads, and its banks flood and move each year.",
         wiki("Amazon River"), difficulty=3)
c.choice("Roughly how many countries share the Amazon rainforest?", "9", ["3", "5", "14"],
         "Brazil, Peru, Colombia, Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana, which is part of France.",
         wiki("Amazon rainforest"), difficulty=3)
c.higher_lower("Is the Amazon rainforest bigger or smaller than the whole of Western Europe?", True,
               "It covers about 5.5 million km², larger than Western Europe.",
               brit("Amazon Rainforest", "place/Amazon-Rainforest"), labels=("Bigger", "Smaller"), difficulty=3)

# Other rivers -------------------------------------------------------------------------------------
c.choice("Which is the longest river in Asia?", "The Yangtze", ["The Ganges", "The Mekong", "The Indus"],
         "It flows about 6,300 km across China, past Shanghai and into the sea.",
         wiki("Yangtze"), difficulty=2)
c.choice("Which is the longest river in Europe?", "The Volga", ["The Danube", "The Rhine", "The Thames"],
         "It flows about 3,500 km through Russia into the Caspian Sea.",
         wiki("Volga"), difficulty=3)
c.choice("Which river flows through London?", "The Thames", ["The Severn", "The Trent", "The Mersey"],
         "It used to freeze over in very cold winters, and Londoners held 'frost fairs' on the ice.",
         wiki("River Thames"), difficulty=1)
c.choice("Which river runs through New Orleans before reaching the Gulf of Mexico?", "The Mississippi", ["The Missouri", "The Colorado", "The Rio Grande"],
         "With the Missouri, it forms the longest river system in North America.",
         wiki("Mississippi River"), difficulty=2)
c.choice("Which river forms much of the border between the USA and Mexico?", "The Rio Grande", ["The Colorado", "The Mississippi", "The Columbia"],
         "In Mexico it's called the Río Bravo del Norte.",
         wiki("Rio Grande"), difficulty=2)
c.choice("Which river flows through Baghdad?", "The Tigris", ["The Euphrates", "The Jordan", "The Nile"],
         "The land between the Tigris and the Euphrates was called Mesopotamia, one of the places where cities began.",
         wiki("Tigris"), difficulty=3)

# The Arctic and the Antarctic ------------------------------------------------------------------------
c.yes_no("Is there land under the ice at the North Pole?", False,
         "The North Pole is in the middle of the Arctic Ocean, on floating sea ice. The South Pole is on land, on Antarctica.",
         wiki("North Pole"), difficulty=2)
c.choice("Which is the smallest of the world's five oceans?", "The Arctic Ocean", ["The Indian Ocean", "The Southern Ocean", "The Atlantic Ocean"],
         "It's also the shallowest, and much of it is covered in ice.",
         wiki("Arctic Ocean"), difficulty=2)
c.choice("Where does the word 'Arctic' come from?", "The Greek word for bear", ["The Latin word for ice", "A Viking explorer", "The Inuit word for north"],
         "The Great Bear constellation sits in the northern sky. 'Antarctic' means 'opposite the Arctic'.",
         wiki("Arctic"), difficulty=3)
c.choice("What is the coldest temperature ever measured on Earth's surface by a thermometer?", "About −89 °C", ["About −40 °C", "About −60 °C", "About −120 °C"],
         "It was −89.2 °C at Vostok Station in Antarctica, in July 1983.",
         wiki("Lowest temperature recorded on Earth"), difficulty=2)
c.higher_lower("Does Antarctica hold more or less than half of the world's fresh water?", True,
               "Its ice sheet holds about 70% of all the fresh water on Earth.",
               wiki("Antarctic ice sheet"), labels=("More", "Less"), difficulty=2)
c.yes_no("Does any one country own Antarctica?", False,
         "Under the Antarctic Treaty of 1959 it's kept for peace and science. Several countries claim parts, but the claims are frozen.",
         wiki("Antarctic Treaty System"), difficulty=2)
c.higher_lower("Antarctica is the fifth-largest continent. Is it bigger or smaller than Europe?", True,
               "Antarctica covers about 14 million km², about 40% more than Europe.",
               wiki("Antarctica"), labels=("Bigger", "Smaller"), difficulty=3)
c.yes_no("Do people stay in Antarctica right through its dark winter?", True,
         "About 1,000 scientists and staff stay through the winter at research stations, rising to around 5,000 in summer. Nobody lives there for good.",
         wiki("Demographics of Antarctica"), difficulty=3)
c.yes_no("Is Antarctica the highest continent, on average?", True,
         "Its ice sheet is so thick that its average height is about 2,500 metres.",
         wiki("Antarctica"), difficulty=3)
c.choice("Which is the biggest country with land inside the Arctic Circle?", "Russia", ["Canada", "Greenland", "Norway"],
         "Eight countries have land inside the Arctic Circle. Russia has the most.",
         wiki("Arctic Circle"), difficulty=2)
c.choice("At the North Pole in summer, how long is the sun up?", "All day and all night", ["About 12 hours", "About 18 hours", "It never rises"],
         "From March to September the sun never sets at the North Pole. For the other six months, it never rises.",
         wiki("Midnight sun"), difficulty=2)

# The Equator and lines on the map ----------------------------------------------------------------------
c.choice("Roughly how long is the Equator?", "About 40,000 km", ["About 12,000 km", "About 25,000 km", "About 100,000 km"],
         "It's 40,075 km, the distance round the Earth at its widest.",
         wiki("Equator"), difficulty=2)
c.choice("Which country is named after the Equator?", "Ecuador", ["Kenya", "Gabon", "Indonesia"],
         "Ecuador is Spanish for 'equator'.",
         wiki("Ecuador"), difficulty=1)
c.yes_no("Does the Equator pass through India?", False,
         "It passes through 13 countries, including Ecuador, Brazil, Kenya and Indonesia, but not India.",
         wiki("Equator"), difficulty=2)
c.yes_no("Is there anywhere on the Equator with snow on the ground?", True,
         "The slopes of Cayambe, a volcano in Ecuador, are the only place on the Equator with snow and ice all year.",
         wiki("Cayambe (volcano)"), difficulty=3)
c.choice("Near the Equator, roughly how long is the daylight each day, all year round?", "About 12 hours", ["About 8 hours", "About 16 hours", "It changes a lot with the seasons"],
         "Day and night are almost the same length all year, so there are no long summer evenings.",
         wiki("Equator"), difficulty=2)
c.choice("Through which London district does the Prime Meridian, 0° longitude, run?", "Greenwich", ["Westminster", "Camden", "Kensington"],
         "Since 1884 the world has measured longitude east and west from Greenwich.",
         wiki("Prime meridian (Greenwich)"), difficulty=1)
c.choice("The Tropic of Cancer is north of the Equator. What is the matching line to the south called?", "The Tropic of Capricorn", ["The Tropic of Aries", "The Antarctic Line", "The Southern Meridian"],
         "On the Tropic of Capricorn, the sun is right overhead at noon in late December.",
         wiki("Tropic of Capricorn"), difficulty=2)
c.choice("In which ocean is the International Date Line, where the date changes by a whole day?", "The Pacific", ["The Atlantic", "The Indian", "The Arctic"],
         "It zigzags round islands so that no country is split between two dates.",
         wiki("International Date Line"), difficulty=2)

# The shape of the world -------------------------------------------------------------------------------
c.choice("Which country has more islands than any other?", "Sweden", ["Indonesia", "The Philippines", "Greece"],
         "Sweden has around 267,000, though fewer than 1,000 have people living on them.",
         wiki("Archipelago"), difficulty=3)
c.choice("Which country has the longest coastline in the world?", "Canada", ["Russia", "Australia", "Norway"],
         "Canada's coastline is over 200,000 km long, thanks to its thousands of Arctic islands.",
         wiki("List of countries by length of coastline"), difficulty=2)
c.choice("Which country stretches across 11 time zones, more than any other in one piece?", "Russia", ["China", "Canada", "The United States"],
         "When it's morning on Russia's Pacific coast, it's still the evening before in Kaliningrad.",
         wiki("Time in Russia"), difficulty=2)
c.choice("Counting its islands around the world, which country has the most time zones?", "France", ["Russia", "The United States", "The United Kingdom"],
         "France has 12, from French Polynesia in the Pacific to Réunion in the Indian Ocean.",
         wiki("Time in France"), difficulty=3, as_of="2026-11")
c.choice("Which is the smallest country in the world?", "Vatican City", ["Monaco", "San Marino", "Liechtenstein"],
         "It covers less than half a square kilometre, inside the city of Rome.",
         wiki("Vatican City"), difficulty=1)
c.choice("Which is the largest lake in the world, so big it's called a sea?", "The Caspian Sea", ["The Dead Sea", "The Aral Sea", "Lake Superior"],
         "It's bordered by Russia, Kazakhstan, Turkmenistan, Iran and Azerbaijan.",
         wiki("Caspian Sea"), difficulty=2)
c.choice("What is the 'Ring of Fire'?", "A horseshoe of volcanoes round the Pacific Ocean", ["A ring of hot deserts", "The hottest part of the Sun", "A circle of oil fields"],
         "About three quarters of the world's active volcanoes are on it, and most earthquakes happen there.",
         wiki("Ring of Fire"), difficulty=2)
c.yes_no("Does the warm Gulf Stream current help keep Britain's winters mild?", True,
         "It carries warm water across the Atlantic from the Gulf of Mexico.",
         wiki("Gulf Stream"), difficulty=2)
c.yes_no("Is Australia both a country and a continent?", True,
         "It's the only country that covers a whole continent by itself.",
         wiki("Australia (continent)"), difficulty=1)
c.choice("Which is the largest country in Africa by area?", "Algeria", ["Nigeria", "Egypt", "The Democratic Republic of the Congo"],
         "Most of Algeria is covered by the Sahara.",
         wiki("Algeria"), difficulty=3)
c.choice("Which is the largest country in South America?", "Brazil", ["Argentina", "Peru", "Colombia"],
         "Brazil borders every South American country except Chile and Ecuador.",
         wiki("Brazil"), difficulty=1)
