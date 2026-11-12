"""The second batch for existing subjects: landscapes and landmarks, history, famous people,
science, space, nature, music, and film and TV."""

from . import Category, wiki

# Landscapes and landmarks
land = Category("landmarks", prefix="landmarks2")
land.higher_lower("Mount Everest is 8,849 metres tall. Is K2, the second-highest mountain, higher or lower?", False,
                  "K2 is 8,611 metres tall. It's on the border of Pakistan and China and is much harder to climb than Everest.",
                  wiki("K2"), difficulty=1)
land.choice("Mount Everest sits on the border of Nepal and which other country?", "China", ["India", "Bhutan", "Pakistan"],
            "The border runs right across the summit. The Nepali name for Everest is Sagarmatha.",
            wiki("Mount Everest"), difficulty=2)
land.choice("Which snow-capped volcano is the highest mountain in Iran?", "Damavand", ["Sabalan", "Ararat", "Elbrus"],
            "Damavand is about 5,610 metres tall, the highest peak in the Middle East and often called Asia's highest volcano. It can be seen from Tehran on a clear day.",
            wiki("Mount Damavand"), difficulty=2)
land.higher_lower("Mont Blanc, the highest peak in the Alps, is about 4,800 metres tall. Is Damavand in Iran higher or lower?", True,
                  "Damavand is about 5,610 metres tall, roughly 800 metres higher than Mont Blanc.",
                  wiki("Mount Damavand"), difficulty=3)
land.choice("In which country is Mount Fuji?", "Japan", ["China", "South Korea", "Indonesia"],
            "Mount Fuji is 3,776 metres tall, the highest mountain in Japan.",
            wiki("Mount Fuji"), difficulty=1)
land.yes_no("Has Mount Fuji erupted since the year 1800?", False,
            "Mount Fuji is still an active volcano, but its last eruption was in 1707.",
            wiki("Mount Fuji"), difficulty=3)
land.choice("Mont Blanc sits on the border of France and which other country?", "Italy", ["Switzerland", "Austria", "Germany"],
            "The Italians call it Monte Bianco. Both names mean 'white mountain'.",
            wiki("Mont Blanc"), difficulty=2)
land.choice("Which pointed Alpine peak stands on the border of Switzerland and Italy?", "The Matterhorn", ["The Eiger", "The Zugspitze", "Mont Blanc"],
            "The Matterhorn is about 4,478 metres tall. Edward Whymper's team first climbed it in 1865.",
            wiki("Matterhorn"), difficulty=2)
land.choice("How many countries do the Alps stretch across?", "8", ["4", "6", "12"],
            "France, Monaco, Italy, Switzerland, Liechtenstein, Germany, Austria and Slovenia.",
            wiki("Alps"), difficulty=3)
land.choice("Which river carved the Grand Canyon?", "The Colorado River", ["The Mississippi", "The Rio Grande", "The Missouri"],
            "The river has been cutting the canyon for millions of years. It's up to about 1.8 kilometres deep.",
            wiki("Grand Canyon"), difficulty=2)
land.higher_lower("The Grand Canyon is about 1.8 km deep at its deepest. Is it more or less than 400 km long?", True,
                  "The Grand Canyon is about 446 kilometres long, in Arizona.",
                  wiki("Grand Canyon"), labels=("More", "Less"), difficulty=3)
land.choice("Niagara Falls sits on the border between the United States and which country?", "Canada", ["Mexico", "Cuba", "Greenland"],
            "Niagara Falls is really three waterfalls. The biggest, Horseshoe Falls, is mostly on the Canadian side.",
            wiki("Niagara Falls"), difficulty=1)
land.choice("Victoria Falls lies on the border of Zambia and which other country?", "Zimbabwe", ["Botswana", "Mozambique", "Malawi"],
            "Its local name, Mosi-oa-Tunya, means 'the smoke that thunders'. It's on the Zambezi River.",
            wiki("Victoria Falls"), difficulty=2)
land.choice("In which country is Angel Falls, the world's highest uninterrupted waterfall?", "Venezuela", ["Brazil", "Colombia", "Peru"],
            "The water drops 979 metres, so far that much of it turns to mist before it reaches the bottom.",
            wiki("Angel Falls"), difficulty=3)
land.choice("In which country is Uluru, the giant red rock?", "Australia", ["South Africa", "The United States", "Namibia"],
            "Uluru is in the Northern Territory. Climbing it has been banned since 2019 out of respect for the Anangu, its traditional owners.",
            wiki("Uluru"), difficulty=1)
land.choice("In which country is Mount Kilimanjaro, Africa's highest mountain?", "Tanzania", ["Kenya", "Uganda", "Ethiopia"],
            "Kilimanjaro is about 5,895 metres tall and has snow on top, even though it's close to the equator.",
            wiki("Mount Kilimanjaro"), difficulty=2)
land.choice("Which is the highest mountain in South America?", "Aconcagua", ["Chimborazo", "Huascarán", "Ojos del Salado"],
            "Aconcagua, in Argentina, is about 6,961 metres tall, the highest mountain outside Asia.",
            wiki("Aconcagua"), difficulty=3)
land.higher_lower("The shore of the Dead Sea is the lowest land on Earth. Is it more or less than 400 metres below sea level?", True,
                  "It's about 430 metres below sea level, and getting lower as the sea shrinks.",
                  wiki("Dead Sea"), labels=("More", "Less"), difficulty=3)
land.yes_no("Can you float in the Dead Sea without swimming?", True,
            "The water is about ten times saltier than the ocean, which makes people float easily.",
            wiki("Dead Sea"), difficulty=1)
land.choice("Which is the deepest lake in the world?", "Lake Baikal", ["Lake Tanganyika", "Lake Superior", "Lake Victoria"],
            "Lake Baikal, in Siberia, is about 1,640 metres deep and holds more fresh water than any other lake.",
            wiki("Lake Baikal"), difficulty=2)
land.choice("In which ocean is the Mariana Trench, the deepest place on Earth?", "The Pacific", ["The Atlantic", "The Indian Ocean", "The Arctic"],
            "Its deepest point, the Challenger Deep, is nearly 11 kilometres down.",
            wiki("Mariana Trench"), difficulty=2)
land.higher_lower("Mount Everest is 8,849 metres tall. Is the deepest point of the Mariana Trench more or less than 8,849 metres deep?", True,
                  "The Challenger Deep is about 10,935 metres deep. If Everest sat on the bottom, its top would still be under water.",
                  wiki("Challenger Deep"), labels=("More", "Less"), difficulty=2)
land.choice("The Danube flows through more countries than any other river. How many?", "10", ["4", "7", "15"],
            "It starts in Germany's Black Forest and reaches the Black Sea, passing four capital cities on the way.",
            wiki("Danube"), difficulty=3)
land.choice("Which river flows through Vienna, Bratislava, Budapest and Belgrade?", "The Danube", ["The Rhine", "The Elbe", "The Volga"],
            "No other river in the world flows through four capital cities.",
            wiki("Danube"), difficulty=2)
land.choice("In which country is Ha Long Bay, with its thousands of limestone islands?", "Vietnam", ["Thailand", "The Philippines", "Malaysia"],
            "Ha Long means 'descending dragon'. There are about 1,600 islands in the bay.",
            wiki("Hạ Long Bay"), difficulty=2)
land.choice("Which city sits beneath Table Mountain?", "Cape Town", ["Johannesburg", "Durban", "Nairobi"],
            "Table Mountain has a flat top about 3 kilometres across. Clouds that spill over it are called the 'tablecloth'.",
            wiki("Table Mountain"), difficulty=2)
land.choice("Where is the Giant's Causeway?", "Northern Ireland", ["Scotland", "Wales", "Iceland"],
            "About 40,000 stone columns, mostly six-sided, formed when lava cooled and cracked millions of years ago.",
            wiki("Giant's Causeway"), difficulty=2)
land.choice("Which was the world's first national park, in 1872?", "Yellowstone", ["Yosemite", "The Grand Canyon", "The Lake District"],
            "Yellowstone is home to Old Faithful, a geyser that shoots hot water into the air roughly every hour and a half.",
            wiki("Yellowstone National Park"), era="classic", difficulty=2)
land.choice("Which country do the Galápagos Islands belong to?", "Ecuador", ["Peru", "Chile", "Colombia"],
            "Giant tortoises and finches on the islands helped Charles Darwin develop his ideas about evolution.",
            wiki("Galápagos Islands"), difficulty=2)
land.choice("In which country is Neuschwanstein, the fairytale castle on a hill?", "Germany", ["Austria", "Switzerland", "France"],
            "It was built for King Ludwig II of Bavaria and is said to have inspired Disney's Sleeping Beauty castle.",
            wiki("Neuschwanstein Castle"), difficulty=2)
land.choice("How many large pyramids stand on the Giza plateau in Egypt?", "3", ["2", "5", "7"],
            "The Great Pyramid, built for Khufu, is the biggest. There are several much smaller pyramids beside them.",
            wiki("Giza pyramid complex"), difficulty=2)
land.choice("The Great Sphinx of Giza has the body of which animal?", "A lion", ["A bull", "A horse", "A dog"],
            "It has a lion's body and a human head, and is about 73 metres long.",
            wiki("Great Sphinx of Giza"), difficulty=1)
land.yes_no("Does the Eiffel Tower get slightly taller in summer?", True,
            "Its iron expands in the heat, so the top can rise by up to about 15 centimetres.",
            wiki("Eiffel Tower"), difficulty=2)
land.choice("What was the Leaning Tower of Pisa built to be?", "A bell tower", ["A lighthouse", "A prison", "A lookout tower"],
            "It began to lean while it was still being built in the 1170s, because the ground underneath is soft.",
            wiki("Leaning Tower of Pisa"), difficulty=2)
land.choice("What is the highest mountain in Wales?", "Yr Wyddfa (Snowdon)", ["Pen y Fan", "Cadair Idris", "Tryfan"],
            "Yr Wyddfa is 1,085 metres tall. You can ride a railway almost to the top.",
            wiki("Snowdon"), difficulty=1)
land.yes_no("Does Loch Ness hold more fresh water than all the lakes in England and Wales put together?", True,
            "Loch Ness is about 230 metres deep in places, so it holds a huge amount of water.",
            wiki("Loch Ness"), difficulty=3)
land.choice("In which country are the Cliffs of Moher?", "Ireland", ["Scotland", "Wales", "Norway"],
            "The cliffs, in County Clare, rise about 214 metres above the Atlantic.",
            wiki("Cliffs of Moher"), difficulty=2)
land.choice("Which country is most famous for its fjords?", "Norway", ["Finland", "Denmark", "The Netherlands"],
            "Fjords are deep, narrow sea inlets carved by glaciers. Fjord is a Norwegian word.",
            wiki("Fjord"), difficulty=1)
land.choice("Which is the driest desert that isn't at the North or South Pole?", "The Atacama", ["The Sahara", "The Gobi", "The Kalahari"],
            "Some weather stations in Chile's Atacama Desert have hardly ever recorded rain.",
            wiki("Atacama Desert"), difficulty=3)
land.choice("The word 'geyser' comes from a hot spring in which country?", "Iceland", ["New Zealand", "The United States", "Japan"],
            "The Great Geysir, in south-west Iceland, gave its name to every geyser in the world.",
            wiki("Geysir"), difficulty=2)
land.choice("Which river carries more water than any other in the world?", "The Amazon", ["The Nile", "The Yangtze", "The Mississippi"],
            "The Amazon carries more water than the next several biggest rivers put together.",
            wiki("Amazon River"), difficulty=2)
land.choice("Which active volcano towers over the Italian island of Sicily?", "Mount Etna", ["Vesuvius", "Stromboli", "Hekla"],
            "Etna is one of the most active volcanoes in the world and erupts often.",
            wiki("Mount Etna"), difficulty=2)
land.choice("Lake Titicaca lies on the border of Peru and which other country?", "Bolivia", ["Chile", "Ecuador", "Argentina"],
            "At about 3,800 metres above sea level, it's often called the highest lake that big boats can sail on.",
            wiki("Lake Titicaca"), difficulty=3)
land.choice("Which bridge is nicknamed 'the Coathanger'?", "Sydney Harbour Bridge", ["The Golden Gate Bridge", "Tower Bridge", "The Brooklyn Bridge"],
            "It opened in 1932. You can climb over the top arch with a guide.",
            wiki("Sydney Harbour Bridge"), difficulty=2)
land.choice("What is the official name of the Golden Gate Bridge's colour?", "International Orange", ["Golden Gate Red", "California Rust", "Sunset Orange"],
            "The colour was chosen because it stands out in fog and fits the hills around it.",
            wiki("Golden Gate Bridge"), difficulty=3)
land.choice("How many US presidents' faces are carved into Mount Rushmore?", "4", ["3", "5", "6"],
            "Washington, Jefferson, Theodore Roosevelt and Lincoln. Each face is about 18 metres tall.",
            wiki("Mount Rushmore"), difficulty=2)
land.choice("In which Spanish city is the Alhambra palace?", "Granada", ["Seville", "Córdoba", "Toledo"],
            "The Alhambra was built mostly in the 1300s and is famous for its tiles, carvings and gardens.",
            wiki("Alhambra"), difficulty=3)

# History
hist = Category("history", prefix="history2")
hist.choice("Who was the first emperor of Rome?", "Augustus", ["Julius Caesar", "Nero", "Caligula"],
            "Julius Caesar was never emperor. His adopted son Octavian became the first, taking the name Augustus in 27 BC.",
            wiki("Augustus"), difficulty=3)
hist.choice("Which queen led the Iceni tribe in a revolt against the Romans in Britain?", "Boudica", ["Cleopatra", "Cartimandua", "Matilda"],
            "Boudica's army burned Colchester, London and St Albans in about AD 60 to 61.",
            wiki("Boudica"), difficulty=2)
hist.choice("Which Viking explorer is believed to have reached North America about 500 years before Columbus?", "Leif Erikson", ["Erik the Red", "Ragnar Lothbrok", "Harald Hardrada"],
            "Remains of a Viking settlement have been found at L'Anse aux Meadows in Newfoundland, Canada.",
            wiki("Leif Erikson"), difficulty=3)
hist.choice("Whose expedition made the first voyage all the way round the world, finishing in 1522?", "Ferdinand Magellan's", ["Christopher Columbus's", "Francis Drake's", "James Cook's"],
            "Magellan himself was killed in the Philippines. Juan Sebastián Elcano led the last ship home to Spain.",
            wiki("Magellan expedition"), difficulty=2)
hist.choice("Who built Europe's first printing press with movable type, in about 1440?", "Johannes Gutenberg", ["William Caxton", "Leonardo da Vinci", "Galileo Galilei"],
            "Printed books spread ideas faster than ever before. William Caxton brought printing to England in 1476.",
            wiki("Johannes Gutenberg"), difficulty=2)
hist.choice("In which year did the Wall Street Crash happen?", "1929", ["1919", "1939", "1945"],
            "The crash in New York helped start the Great Depression, which spread around the world.",
            wiki("Wall Street crash of 1929"), era="classic", difficulty=2)
hist.choice("Which Chinese emperor's tomb is guarded by the Terracotta Army?", "Qin Shi Huang", ["Kublai Khan", "Puyi", "Genghis Khan"],
            "Farmers digging a well found the army in 1974. There are thousands of life-size clay soldiers, each with a different face.",
            wiki("Terracotta Army"), difficulty=3)
hist.choice("Which people built Machu Picchu?", "The Inca", ["The Maya", "The Aztecs", "The Olmecs"],
            "Machu Picchu was built in the 1400s, high in the Andes mountains of Peru.",
            wiki("Machu Picchu"), difficulty=2)
hist.choice("Which empire was ruled from Tenochtitlan, where Mexico City stands today?", "The Aztec Empire", ["The Inca Empire", "The Maya Empire", "The Ottoman Empire"],
            "Tenochtitlan was built on an island in a lake, and was one of the biggest cities in the world in the 1500s.",
            wiki("Tenochtitlan"), difficulty=2)
hist.higher_lower("The Battle of Hastings was in 1066. Was the Magna Carta agreed more or less than 200 years later?", False,
                  "The Magna Carta was agreed in 1215, 149 years after the Battle of Hastings.",
                  wiki("Magna Carta"), labels=("More", "Less"), difficulty=2)
hist.higher_lower("The Titanic sank in 1912. Did the liner Lusitania sink earlier or later?", False,
                  "The Lusitania was sunk by a German submarine in 1915, during the First World War.",
                  wiki("RMS Lusitania"), labels=("Earlier", "Later"), era="classic", difficulty=2)
hist.yes_no("Did the Romans invade Britain before the year AD 100?", True,
            "The Romans invaded in AD 43, under Emperor Claudius, and stayed for nearly 400 years.",
            wiki("Roman conquest of Britain"), difficulty=2)
hist.choice("In which year did some women in the UK first get to vote in general elections?", "1918", ["1900", "1928", "1945"],
            "In 1918 women over 30 who met certain conditions could vote. All women over 21 got the vote in 1928, the same as men.",
            wiki("Representation of the People Act 1918"), era="classic", difficulty=2)
hist.choice("How long did the Hundred Years' War between England and France last?", "116 years", ["100 years", "99 years", "150 years"],
            "It ran from 1337 to 1453, with long breaks in the fighting.",
            wiki("Hundred Years' War"), difficulty=3)
hist.choice("Which explorer was the first to sail from Europe to India, in 1498?", "Vasco da Gama", ["Christopher Columbus", "Marco Polo", "Ferdinand Magellan"],
            "Vasco da Gama sailed from Portugal around the southern tip of Africa.",
            wiki("Vasco da Gama"), difficulty=3)
hist.choice("Which ancient city was famous for its Hanging Gardens?", "Babylon", ["Athens", "Rome", "Carthage"],
            "The Hanging Gardens of Babylon were one of the Seven Wonders, but no one is sure exactly where, or even if, they existed.",
            wiki("Hanging Gardens of Babylon"), difficulty=2)
hist.true_false("Vikings wore helmets with horns on them in battle.", False,
                "No Viking helmet with horns has ever been found. The idea mostly comes from costumes for operas in the 1800s.",
                wiki("Horned helmet"), difficulty=2)
hist.true_false("Cleopatra lived closer in time to the Moon landing than to the building of the Great Pyramid.", True,
                "The Great Pyramid was built around 2560 BC. Cleopatra died in 30 BC, about 2,500 years later, and about 2,000 years before the Moon landing.",
                wiki("Cleopatra"), difficulty=3)
hist.yes_no("Was Napoleon unusually short for a man of his time?", False,
            "Napoleon was about 1.69 metres tall, about average for a Frenchman then. British cartoons made fun of him as tiny.",
            wiki("Napoleon complex"), difficulty=3)
hist.choice("Which age came straight after the Stone Age?", "The Bronze Age", ["The Iron Age", "The Ice Age", "The Middle Ages"],
            "Bronze is made by mixing copper and tin. The Iron Age came after the Bronze Age.",
            wiki("Three-age system"), difficulty=2)
hist.choice("Which ancient wonder was a giant lighthouse in Egypt?", "The Lighthouse of Alexandria", ["The Colossus of Rhodes", "The Hanging Gardens of Babylon", "The Mausoleum at Halicarnassus"],
            "It stood for well over 1,000 years before earthquakes brought it down.",
            wiki("Lighthouse of Alexandria"), difficulty=2)
hist.choice("Which Mongol leader founded the largest land empire in history?", "Genghis Khan", ["Attila the Hun", "Tamerlane", "Kublai Khan"],
            "Kublai Khan was his grandson, who went on to rule China.",
            wiki("Mongol Empire"), difficulty=2)
hist.choice("Which English queen ruled for only about nine days in 1553?", "Lady Jane Grey", ["Mary I", "Anne Boleyn", "Matilda"],
            "Lady Jane Grey was pushed aside by Mary I, Henry VIII's daughter.",
            wiki("Lady Jane Grey"), difficulty=3)
hist.choice("Which king of Scotland also became King James I of England in 1603?", "James VI", ["Robert the Bruce", "Charles I", "Malcolm III"],
            "When Elizabeth I died without children, James joined the two crowns.",
            wiki("James VI and I"), difficulty=3)

# Leaders and famous people, kept to history, never party politics
ppl = Category("people", prefix="people2")
ppl.choice("Who became the world's first woman prime minister, in Sri Lanka in 1960?", "Sirimavo Bandaranaike", ["Indira Gandhi", "Golda Meir", "Margaret Thatcher"],
           "Sri Lanka was called Ceylon at the time.",
           wiki("Sirimavo Bandaranaike"), era="classic", difficulty=3)
ppl.choice("Who was India's first prime minister?", "Jawaharlal Nehru", ["Mahatma Gandhi", "Indira Gandhi", "Vallabhbhai Patel"],
           "Nehru led India from independence in 1947 until 1964.",
           wiki("Jawaharlal Nehru"), era="classic", difficulty=2)
ppl.choice("Which US president was the first to live in the White House?", "John Adams", ["George Washington", "Thomas Jefferson", "Abraham Lincoln"],
           "George Washington chose the site, but the house wasn't ready until 1800, when John Adams moved in.",
           wiki("White House"), difficulty=3)
ppl.choice("How many years is a US president elected for?", "4", ["2", "5", "6"],
           "A US president can only be elected twice.",
           wiki("President of the United States"), difficulty=1)
ppl.choice("Who was the youngest person ever elected president of the United States?", "John F. Kennedy", ["Theodore Roosevelt", "Bill Clinton", "Barack Obama"],
           "Kennedy was 43 when elected in 1960. Theodore Roosevelt was younger when he took over, but he wasn't elected at first.",
           wiki("John F. Kennedy"), era="classic", difficulty=3)
ppl.choice("Which French president gave his name to Paris's biggest airport?", "Charles de Gaulle", ["François Mitterrand", "Georges Pompidou", "Jacques Chirac"],
           "Pompidou gave his name to the Centre Pompidou, a modern art museum in Paris.",
           wiki("Charles de Gaulle Airport"), difficulty=2)
ppl.choice("On which island did Nelson Mandela spend 18 of his 27 years in prison?", "Robben Island", ["Alcatraz", "Devil's Island", "Rottnest Island"],
           "Robben Island, off Cape Town, is now a museum.",
           wiki("Robben Island"), era="classic", difficulty=2)
ppl.choice("Jacinda Ardern was prime minister of which country?", "New Zealand", ["Australia", "Ireland", "Canada"],
           "She led New Zealand from 2017 to 2023.",
           wiki("Jacinda Ardern"), era="modern", difficulty=1)
ppl.choice("Who was the first woman to lead Pakistan?", "Benazir Bhutto", ["Indira Gandhi", "Sheikh Hasina", "Khaleda Zia"],
           "Benazir Bhutto became prime minister in 1988, aged 35.",
           wiki("Benazir Bhutto"), era="classic", difficulty=3)
ppl.choice("Who was Britain's prime minister when the Second World War began in 1939?", "Neville Chamberlain", ["Winston Churchill", "Clement Attlee", "Stanley Baldwin"],
           "Churchill took over in May 1940.",
           wiki("Neville Chamberlain"), era="classic", difficulty=3)
ppl.yes_no("Was Queen Victoria on the throne when Winston Churchill was born?", True,
           "Churchill was born in 1874. Victoria reigned from 1837 to 1901.",
           wiki("Winston Churchill"), difficulty=2)
ppl.choice("Which explorer gave his name to the Americas?", "Amerigo Vespucci", ["Christopher Columbus", "John Cabot", "Hernán Cortés"],
           "A German map of 1507 was the first to use the name America.",
           wiki("Amerigo Vespucci"), difficulty=2)
ppl.choice("Who wrote Romeo and Juliet?", "William Shakespeare", ["Christopher Marlowe", "Charles Dickens", "Geoffrey Chaucer"],
           "The play is set in Verona, Italy.",
           wiki("Romeo and Juliet"), difficulty=1)
ppl.choice("Which author created the detective Sherlock Holmes?", "Arthur Conan Doyle", ["Agatha Christie", "Charles Dickens", "Robert Louis Stevenson"],
           "Conan Doyle was a doctor, and based Holmes partly on one of his teachers in Edinburgh.",
           wiki("Arthur Conan Doyle"), difficulty=2)
ppl.choice("Who wrote Pride and Prejudice?", "Jane Austen", ["Charlotte Brontë", "Emily Brontë", "George Eliot"],
           "It came out in 1813. Jane Austen is on the Bank of England £10 note.",
           wiki("Pride and Prejudice"), difficulty=2)
ppl.choice("Who wrote The Gruffalo?", "Julia Donaldson", ["Roald Dahl", "Axel Scheffler", "Michael Rosen"],
           "Axel Scheffler drew the pictures. The book came out in 1999.",
           wiki("The Gruffalo"), era="modern", difficulty=2)
ppl.choice("Which scientist wrote A Brief History of Time?", "Stephen Hawking", ["Albert Einstein", "Brian Cox", "Carl Sagan"],
           "The book, from 1988, has sold more than 25 million copies.",
           wiki("A Brief History of Time"), difficulty=2)
ppl.choice("Who first climbed Everest without bottled oxygen, with Peter Habeler in 1978?", "Reinhold Messner", ["Edmund Hillary", "George Mallory", "Tenzing Norgay"],
           "Messner went on to climb all 14 of the world's mountains over 8,000 metres.",
           wiki("Reinhold Messner"), era="classic", difficulty=3)
ppl.choice("Who was the first person to swim the English Channel, in 1875?", "Matthew Webb", ["Gertrude Ederle", "David Walliams", "Mark Spitz"],
           "Captain Webb took nearly 22 hours. Gertrude Ederle was the first woman, in 1926.",
           wiki("Matthew Webb"), era="classic", difficulty=3)
ppl.choice("Who is the youngest person ever to win a Nobel Prize?", "Malala Yousafzai", ["Greta Thunberg", "Marie Curie", "Anne Frank"],
           "Malala won the Nobel Peace Prize in 2014, aged 17, for standing up for girls' education.",
           wiki("Malala Yousafzai"), era="modern", difficulty=2)
ppl.choice("Who was the last tsar of Russia?", "Nicholas II", ["Peter the Great", "Ivan the Terrible", "Alexander III"],
           "Nicholas II gave up the throne in 1917.",
           wiki("Nicholas II"), difficulty=2)
ppl.choice("Which explorer was the first European to see the east coast of Australia, in 1770?", "James Cook", ["Abel Tasman", "Francis Drake", "Walter Raleigh"],
           "Cook sailed on HMS Endeavour. Dutch sailors had reached Australia's west coast earlier.",
           wiki("James Cook"), difficulty=3)
ppl.choice("Which scientist set out three laws of motion in 1687?", "Isaac Newton", ["Galileo Galilei", "Albert Einstein", "Johannes Kepler"],
           "His first law says that things keep still, or keep moving in a straight line, unless a force acts on them.",
           wiki("Newton's laws of motion"), difficulty=2)
ppl.choice("Who was the first person to fly over the English Channel in an aeroplane, in 1909?", "Louis Blériot", ["Orville Wright", "Amelia Earhart", "Charles Lindbergh"],
           "The flight from Calais to Dover took about 37 minutes.",
           wiki("Louis Blériot"), era="classic", difficulty=3)

# Science
sci = Category("science", prefix="science2")
sci.choice("What is gold's chemical symbol?", "Au", ["Go", "Gd", "Ag"],
           "Au comes from aurum, the Latin word for gold. Ag is silver.",
           wiki("Gold"), difficulty=2)
sci.choice("How many teeth does an adult usually have, including wisdom teeth?", "32", ["20", "28", "40"],
           "Children have 20 baby teeth.",
           wiki("Human tooth"), difficulty=2)
sci.choice("Which blood cells help fight infection?", "White blood cells", ["Red blood cells", "Platelets", "Plasma cells only"],
           "Red blood cells carry oxygen. Platelets help blood clot when you cut yourself.",
           wiki("White blood cell"), difficulty=2)
sci.choice("What is the pH of pure water?", "7", ["0", "1", "14"],
           "Below 7 is acid, like lemon juice. Above 7 is alkaline, like soap.",
           wiki("PH"), difficulty=2)
sci.higher_lower("Water boils at 100 °C at sea level. At the top of Everest, does it boil at a higher or lower temperature?", False,
                 "The air pressure is much lower up there, so water boils at about 70 °C. Tea comes out weak.",
                 wiki("Boiling point"), difficulty=2)
sci.choice("Which element is there more of in the universe than any other?", "Hydrogen", ["Oxygen", "Carbon", "Helium"],
           "About three-quarters of the normal matter in the universe is hydrogen.",
           wiki("Abundance of the chemical elements"), difficulty=2)
sci.choice("What does a barometer measure?", "Air pressure", ["Temperature", "Wind speed", "Rainfall"],
           "Falling air pressure often means rain is on the way.",
           wiki("Barometer"), difficulty=2)
sci.choice("Which part of a plant makes most of its food?", "The leaves", ["The roots", "The flowers", "The stem"],
           "Leaves use sunlight, water and carbon dioxide to make sugar. This is called photosynthesis.",
           wiki("Leaf"), difficulty=1)
sci.choice("Which vitamin does your skin make in sunlight?", "Vitamin D", ["Vitamin C", "Vitamin A", "Vitamin B12"],
           "Vitamin D helps keep bones and teeth strong.",
           wiki("Vitamin D"), difficulty=2)
sci.choice("Roughly how fast does light travel?", "300,000 km a second", ["3,000 km a second", "30,000 km a second", "3 million km a second"],
           "Light could go round the Earth about seven times in one second.",
           wiki("Speed of light"), difficulty=3)
sci.true_false("Lightning never strikes the same place twice.", False,
               "Tall buildings get hit again and again. The Empire State Building is struck about 20 times a year.",
               wiki("Lightning"), difficulty=1)
sci.choice("Who arranged the first periodic table of the elements, in 1869?", "Dmitri Mendeleev", ["Marie Curie", "John Dalton", "Ernest Rutherford"],
           "Mendeleev left gaps for elements nobody had found yet, and predicted what they would be like.",
           wiki("Dmitri Mendeleev"), difficulty=3)
sci.choice("What is the centre of an atom called?", "The nucleus", ["The electron", "The core", "The cell"],
           "Electrons whizz around the nucleus, which holds protons and neutrons.",
           wiki("Atomic nucleus"), difficulty=2)
sci.yes_no("Are old church and castle windows thicker at the bottom because glass slowly flows?", False,
           "Old glass was uneven when it was made, and builders often put the thick edge at the bottom. Glass doesn't flow at room temperature.",
           wiki("Glass"), difficulty=3)
sci.choice("Which gas do we breathe out more of than we breathe in?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Helium"],
           "Our bodies use oxygen and make carbon dioxide as waste.",
           wiki("Breathing"), difficulty=1)

# Space
spc = Category("space", prefix="space2")
spc.choice("What was the name of the first dog to orbit the Earth, in 1957?", "Laika", ["Belka", "Rover", "Strelka"],
           "Laika flew on the Soviet Sputnik 2. Belka and Strelka orbited and came home safely in 1960.",
           wiki("Laika"), era="classic", difficulty=2)
spc.choice("Which planet has the most known moons?", "Saturn", ["Jupiter", "Uranus", "Neptune"],
           "Astronomers keep finding more small moons around Saturn. It has well over 200.",
           wiki("Moons of Saturn"), difficulty=3, as_of="2026-11")
spc.choice("What is the name of the giant volcano on Mars, the biggest in the Solar System?", "Olympus Mons", ["Mount Mars", "Valles Marineris", "Ares Peak"],
           "Olympus Mons is about two and a half times as tall as Mount Everest.",
           wiki("Olympus Mons"), difficulty=2)
spc.choice("Which Moon mission had an explosion on the way in 1970, but brought its crew home safely?", "Apollo 13", ["Apollo 11", "Apollo 8", "Gemini 4"],
           "The crew used the lunar module as a lifeboat. The film Apollo 13 came out in 1995.",
           wiki("Apollo 13"), era="classic", difficulty=2)
spc.choice("Which company makes the Falcon 9 rocket?", "SpaceX", ["Boeing", "Blue Origin", "NASA"],
           "Falcon 9's first stage lands back on Earth so it can be used again.",
           wiki("Falcon 9"), era="modern", difficulty=2)
spc.higher_lower("A day on Earth lasts 24 hours. Is a day on Jupiter longer or shorter?", False,
                 "Jupiter spins once in about 10 hours, even though it's by far the biggest planet.",
                 wiki("Jupiter"), labels=("Longer", "Shorter"), difficulty=2)
spc.choice("Which colour of star is the hottest?", "Blue", ["Red", "Yellow", "Orange"],
           "Red stars are the coolest. Our Sun is yellow-white, in the middle.",
           wiki("Stellar classification"), difficulty=3)
spc.true_false("There is no gravity on the International Space Station.", False,
               "Gravity up there is about 90% as strong as on the ground. Astronauts float because they're always falling around the Earth.",
               wiki("International Space Station"), difficulty=3)
spc.choice("What is a shooting star really?", "A bit of space rock burning up in the air", ["A star falling to Earth", "A satellite", "A comet"],
           "Most shooting stars are made by pieces of dust or rock smaller than a grain of sand.",
           wiki("Meteoroid"), difficulty=2)
spc.choice("Which space telescope, launched in 1990, is named after an American astronomer?", "Hubble", ["Kepler", "James Webb", "Galileo"],
           "Edwin Hubble showed that there are other galaxies beyond our own.",
           wiki("Hubble Space Telescope"), difficulty=2)
spc.choice("Which NASA rover landed on Mars in 2021, carrying a little helicopter?", "Perseverance", ["Curiosity", "Spirit", "Opportunity"],
           "The helicopter, Ingenuity, made the first powered flight on another planet.",
           wiki("Perseverance (rover)"), era="modern", difficulty=2)
spc.choice("Which famous comet comes back past the Earth about every 76 years?", "Halley's Comet", ["Comet Hale-Bopp", "Comet NEOWISE", "Shoemaker-Levy 9"],
           "It was last seen in 1986 and is due back in 2061.",
           wiki("Halley's Comet"), difficulty=2)

# Nature
nat = Category("nature", prefix="nature2")
nat.choice("What is a group of owls called?", "A parliament", ["A pride", "A murder", "A school"],
           "A pride is lions, a murder is crows and a school is fish.",
           wiki("List of English terms of venery, by animal"), difficulty=3)
nat.choice("How many legs does a crab have, counting its claws?", "10", ["6", "8", "12"],
           "Crabs are decapods, which means 'ten feet'.",
           wiki("Crab"), difficulty=3)
nat.higher_lower("A cheetah can reach about 100 km/h. Can a greyhound run faster or slower?", False,
                 "A greyhound tops out at about 70 km/h. It's still the fastest dog.",
                 wiki("Greyhound"), labels=("Faster", "Slower"), difficulty=1)
nat.choice("What is a baby swan called?", "A cygnet", ["A gosling", "A duckling", "A fledgling"],
           "A gosling is a baby goose.",
           wiki("Swan"), difficulty=2)
nat.choice("Which is the biggest member of the cat family?", "The tiger", ["The lion", "The jaguar", "The leopard"],
           "Siberian tigers are the biggest of all and can weigh more than 300 kg.",
           wiki("Tiger"), difficulty=2)
nat.yes_no("Do snails have teeth?", True,
           "A snail has thousands of tiny teeth on a ribbon-like tongue called a radula.",
           wiki("Radula"), difficulty=3)
nat.choice("Why are flamingos pink?", "Because of the food they eat", ["They are born pink", "Sunburn", "The colour of their blood"],
           "Flamingo chicks are grey. They turn pink from colours in the shrimp and algae they eat.",
           wiki("Flamingo"), difficulty=2)
nat.choice("How many arms does a starfish usually have?", "5", ["4", "6", "8"],
           "Some kinds have many more, and a starfish can grow a lost arm back.",
           wiki("Starfish"), difficulty=1)
nat.choice("Which tree do acorns grow on?", "The oak", ["The beech", "The horse chestnut", "The ash"],
           "Conkers come from the horse chestnut tree.",
           wiki("Acorn"), difficulty=1)
nat.yes_no("Is a strawberry a berry, in the way botanists use the word?", False,
           "Botanically, a strawberry isn't a berry, but bananas and grapes are.",
           wiki("Strawberry"), difficulty=3)
nat.choice("What is a male bee called?", "A drone", ["A worker", "A king", "A buzzer"],
           "Drones don't sting and don't collect food. The worker bees are female.",
           wiki("Drone (bee)"), difficulty=2)
nat.choice("Which animal has fingerprints so like ours that they're hard to tell apart, even under a microscope?", "The koala", ["The chimpanzee", "The panda", "The sloth"],
           "Koalas and humans developed fingerprints separately, probably for gripping.",
           wiki("Koala"), difficulty=3)
nat.true_false("Goldfish can only remember things for three seconds.", False,
               "Studies show goldfish can remember things for months, and can even be trained.",
               wiki("Goldfish"), difficulty=2)
nat.choice("Which is the only mammal that can truly fly?", "The bat", ["The flying squirrel", "The sugar glider", "The colugo"],
           "Flying squirrels and sugar gliders only glide.",
           wiki("Bat"), difficulty=2)
nat.choice("Which bird lays the biggest eggs?", "The ostrich", ["The emu", "The albatross", "The eagle"],
           "An ostrich egg weighs about as much as 24 hens' eggs.",
           wiki("Ostrich"), difficulty=1)

# Music
mus = Category("music", prefix="music2")
mus.choice("Which band's song 'Mr. Brightside' has stayed in the UK charts for years?", "The Killers", ["Arctic Monkeys", "Kings of Leon", "The Strokes"],
           "The Killers come from Las Vegas. 'Mr. Brightside' first came out in 2003.",
           wiki("Mr. Brightside"), era="modern", difficulty=2)
mus.choice("Which instrument usually has 47 strings and seven pedals?", "The harp", ["The piano", "The cello", "The sitar"],
           "The pedals change the pitch of the strings so the harp can play in any key.",
           wiki("Pedal harp"), difficulty=2)
mus.choice("Which Beatles album cover shows the band walking over a zebra crossing?", "Abbey Road", ["Revolver", "Let It Be", "Help!"],
           "The crossing is outside the Abbey Road Studios in London and is a listed site.",
           wiki("Abbey Road"), era="classic", difficulty=2)
mus.choice("Which singer is known as the Queen of Pop?", "Madonna", ["Kylie Minogue", "Britney Spears", "Lady Gaga"],
           "Madonna is the best-selling female solo artist of all time.",
           wiki("Madonna"), era="classic", difficulty=2)
mus.choice("Who sang 'Purple Rain'?", "Prince", ["Michael Jackson", "Stevie Wonder", "Lionel Richie"],
           "Purple Rain was also a film, in 1984.",
           wiki("Purple Rain (song)"), era="classic", difficulty=2)
mus.choice("Bono is the lead singer of which Irish band?", "U2", ["The Cranberries", "Westlife", "The Script"],
           "U2 formed in Dublin in 1976, when its members were still at school.",
           wiki("U2"), difficulty=1)
mus.choice("Which rapper's real name is Marshall Mathers?", "Eminem", ["Jay-Z", "Drake", "Snoop Dogg"],
           "Eminem comes from M and M, his initials.",
           wiki("Eminem"), era="modern", difficulty=2)
mus.choice("Who sang 'Uptown Funk' with Mark Ronson?", "Bruno Mars", ["Pharrell Williams", "Justin Timberlake", "Ed Sheeran"],
           "It was one of the biggest hits of 2015.",
           wiki("Uptown Funk"), era="modern", difficulty=1)
mus.choice("Which Spanish-language song by Luis Fonsi and Daddy Yankee was a worldwide hit in 2017?", "Despacito", ["La Bamba", "Macarena", "Bailando"],
           "Despacito means 'slowly'. Its video was the first on YouTube to pass 5 billion views.",
           wiki("Despacito"), era="modern", difficulty=1)
mus.choice("Which family of instruments does the trumpet belong to?", "Brass", ["Woodwind", "Strings", "Percussion"],
           "The saxophone is made of brass, but it counts as woodwind because it uses a reed.",
           wiki("Trumpet"), difficulty=1)
mus.higher_lower("The Beatles' first UK single came out in 1962. Did the Rolling Stones release their first single earlier or later?", False,
                 "The Rolling Stones' first single, 'Come On', came out in 1963.",
                 wiki("Come On (Chuck Berry song)"), labels=("Earlier", "Later"), era="classic", difficulty=3)
mus.choice("Which singer was known as the Queen of Soul?", "Aretha Franklin", ["Diana Ross", "Tina Turner", "Whitney Houston"],
           "Her hit 'Respect' came out in 1967.",
           wiki("Aretha Franklin"), era="classic", difficulty=2)
mus.choice("What does an orchestra's conductor usually hold?", "A baton", ["A bow", "A wand", "A drumstick"],
           "The baton helps the players see the beat from far away.",
           wiki("Baton (conducting)"), difficulty=1)
mus.choice("Which singer from Barbados had a huge hit with 'Umbrella'?", "Rihanna", ["Beyoncé", "Nicki Minaj", "Shakira"],
           "'Umbrella' was number one in the UK for ten weeks in 2007.",
           wiki("Umbrella (song)"), era="modern", difficulty=1)
mus.choice("Which group was Beyoncé in before she went solo?", "Destiny's Child", ["The Pussycat Dolls", "TLC", "Sugababes"],
           "Destiny's Child had hits with 'Survivor' and 'Say My Name'.",
           wiki("Destiny's Child"), era="modern", difficulty=2)
mus.choice("How many lines are there in a musical stave?", "5", ["4", "6", "8"],
           "Notes sit on the lines or in the spaces between them.",
           wiki("Staff (music)"), difficulty=2)
mus.choice("How many musicians play in a quartet?", "4", ["3", "5", "8"],
           "A string quartet has two violins, a viola and a cello.",
           wiki("String quartet"), difficulty=1)
mus.choice("Which composer wrote the piano piece 'Für Elise'?", "Beethoven", ["Mozart", "Bach", "Chopin"],
           "Nobody is sure who Elise was. The piece wasn't published until 40 years after Beethoven died.",
           wiki("Für Elise"), difficulty=2)
mus.choice("Which instrument did Jimi Hendrix famously play?", "The electric guitar", ["The drums", "The saxophone", "The keyboard"],
           "Hendrix was left-handed and played a right-handed guitar upside down.",
           wiki("Jimi Hendrix"), era="classic", difficulty=1)
mus.choice("Which singer's fans call themselves Swifties?", "Taylor Swift", ["Billie Eilish", "Olivia Rodrigo", "Dua Lipa"],
           "Taylor Swift started out as a country singer in Nashville.",
           wiki("Taylor Swift"), era="modern", difficulty=1)

# Film and TV
film = Category("film-tv", prefix="film2")
film.choice("Who plays Captain Jack Sparrow in Pirates of the Caribbean?", "Johnny Depp", ["Orlando Bloom", "Brad Pitt", "Russell Crowe"],
            "The films were inspired by a ride at Disneyland.",
            wiki("Jack Sparrow"), era="modern", difficulty=1)
film.choice("In which film does a great white shark terrorise the town of Amity Island?", "Jaws", ["The Meg", "Deep Blue Sea", "Finding Nemo"],
            "Jaws, from 1975, is often called the first summer blockbuster.",
            wiki("Jaws (film)"), era="classic", difficulty=1)
film.choice("What is the name of the school of witchcraft and wizardry in Harry Potter?", "Hogwarts", ["Beauxbatons", "Durmstrang", "Nevermore"],
            "Beauxbatons and Durmstrang are rival schools in Harry Potter. Nevermore is Wednesday Addams's school.",
            wiki("Hogwarts"), difficulty=1)
film.choice("In The Wizard of Oz, which character wants a brain?", "The Scarecrow", ["The Tin Man", "The Cowardly Lion", "Toto"],
            "The Tin Man wants a heart and the Lion wants courage.",
            wiki("Scarecrow (Oz)"), difficulty=1)
film.choice("Who played Hermione Granger in the Harry Potter films?", "Emma Watson", ["Emma Stone", "Bonnie Wright", "Keira Knightley"],
            "Bonnie Wright played Ginny Weasley.",
            wiki("Emma Watson"), era="modern", difficulty=1)
film.choice("In which country were The Lord of the Rings films made?", "New Zealand", ["Ireland", "Scotland", "Canada"],
            "The Hobbiton set in Matamata is now a place you can visit.",
            wiki("The Lord of the Rings (film series)"), era="modern", difficulty=2)
film.choice("Which hobbit does Elijah Wood play in The Lord of the Rings?", "Frodo Baggins", ["Bilbo Baggins", "Samwise Gamgee", "Pippin Took"],
            "Bilbo, Frodo's uncle, found the ring in The Hobbit.",
            wiki("Frodo Baggins"), era="modern", difficulty=2)
film.choice("Which superhero is secretly Bruce Wayne?", "Batman", ["Superman", "Spider-Man", "Iron Man"],
            "Superman is Clark Kent, Spider-Man is Peter Parker and Iron Man is Tony Stark.",
            wiki("Batman"), difficulty=1)
film.choice("What is the name of Thor's hammer in the Marvel films?", "Mjolnir", ["Excalibur", "Stormbreaker", "Gungnir"],
            "Stormbreaker is the axe Thor gets later, in Avengers: Infinity War.",
            wiki("Mjolnir (comics)"), era="modern", difficulty=3)
film.choice("On which TV quiz show do players hear the line 'Is that your final answer'?", "Who Wants to Be a Millionaire?", ["The Chase", "Pointless", "Mastermind"],
            "The show began on ITV in 1998 and has been copied in more than 100 countries.",
            wiki("Who Wants to Be a Millionaire? (British game show)"), difficulty=1)
film.choice("Which dinosaur chases the jeep in Jurassic Park?", "Tyrannosaurus rex", ["Velociraptor", "Triceratops", "Spinosaurus"],
            "The famous ripple in a glass of water warns that the T. rex is coming.",
            wiki("Jurassic Park (film)"), era="classic", difficulty=1)
film.choice("Who plays Mr Brown in the Paddington films?", "Hugh Bonneville", ["Hugh Grant", "Colin Firth", "Jim Broadbent"],
            "Hugh Grant played the villain, Phoenix Buchanan, in Paddington 2.",
            wiki("Paddington (film)"), era="modern", difficulty=3)
film.choice("Who plays Willy Wonka in the 2023 film Wonka?", "Timothée Chalamet", ["Johnny Depp", "Tom Holland", "Gene Wilder"],
            "Gene Wilder played Wonka in 1971 and Johnny Depp in 2005.",
            wiki("Wonka (film)"), era="modern", difficulty=2)
film.choice("Mamma Mia! is set on an island in which country?", "Greece", ["Italy", "Spain", "Croatia"],
            "Much of it was filmed on the Greek island of Skopelos. The songs are all by ABBA.",
            wiki("Mamma Mia! (film)"), era="modern", difficulty=1)
film.choice("Which actor played Sherlock in the BBC series Sherlock?", "Benedict Cumberbatch", ["Martin Freeman", "Robert Downey Jr.", "Matt Smith"],
            "Martin Freeman played his friend Dr Watson.",
            wiki("Sherlock (TV series)"), era="modern", difficulty=2)
film.higher_lower("The first Toy Story came out in 1995. Did the first Shrek come out more or less than five years later?", True,
                  "Shrek came out in 2001, six years after Toy Story.",
                  wiki("Shrek"), labels=("More", "Less"), difficulty=3)
film.choice("Which TV series is set in a land called Westeros?", "Game of Thrones", ["The Witcher", "The Last Kingdom", "Merlin"],
            "It was filmed in many places, including Northern Ireland, Croatia and Iceland.",
            wiki("Game of Thrones"), era="modern", difficulty=2)
film.choice("In Friends, what is the name of the coffee shop where the group meets?", "Central Perk", ["The Daily Grind", "Java Joe's", "Monk's Café"],
            "Monk's Café is the diner in Seinfeld.",
            wiki("Central Perk"), difficulty=2)
film.choice("Which spy has the code number 007?", "James Bond", ["Jason Bourne", "Ethan Hunt", "Johnny English"],
            "Ian Fleming, who wrote the books, worked in naval intelligence during the Second World War.",
            wiki("James Bond"), difficulty=1)
film.choice("In The Lion King, which song do Timon and Pumbaa teach Simba?", "Hakuna Matata", ["Circle of Life", "Be Prepared", "I Just Can't Wait to Be King"],
            "Hakuna matata is Swahili for 'no worries'.",
            wiki("Hakuna Matata (song)"), difficulty=1)
