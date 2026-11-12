"""Even more sport: the World Cup, the Olympics, Formula One and the big tournaments."""

from . import Category, wiki

c = Category("sport", prefix="sport3")
HAMILTON_WINS = ("Formula 1: the records Hamilton holds ahead of his 400th Grand Prix",
                 "https://www.formula1.com/en/latest/article/in-numbers-the-incredible-records-hamilton-holds-ahead-of-his-400th-grand-prix.1yNnQ8vuefRFhQj4AprTh0")
GLASGOW_2026 = ("TNT Sports: Glasgow 2026 Commonwealth Games closing ceremony",
                "https://www.tntsports.co.uk/commonwealth-games/2026/closing-ceremony-how-to-watch-start-time-who-is-performing_sto23324807/story.shtml")
COPA = ("CONMEBOL: all the Copa América champions", "https://copaamerica.com/en/news/all-of-the-conmebol-copa-america-champions")

# The World Cup --------------------------------------------------------------------------------------
c.choice("How often is the men's football World Cup held?", "Every 4 years", ["Every 2 years", "Every 3 years", "Every 5 years"],
         "It has been held every four years since 1930, apart from 1942 and 1946, which were cancelled because of the Second World War.",
         wiki("FIFA World Cup"), difficulty=1)
c.choice("The 2022 World Cup in Qatar was the first to be played in which months?", "November and December", ["January and February", "March and April", "September and October"],
         "It was moved out of the usual June and July slot because of the summer heat in Qatar.",
         wiki("2022 FIFA World Cup"), era="modern", difficulty=2)
c.choice("Which country won the World Cup on home soil in 1998?", "France", ["Brazil", "Italy", "Germany"],
         "France beat Brazil 3-0 in the final in Paris. Zinedine Zidane scored twice, both with headers.",
         wiki("1998 FIFA World Cup"), difficulty=2)
c.choice("In the 2006 World Cup final, which French captain was sent off for headbutting an opponent?", "Zinedine Zidane", ["Thierry Henry", "Patrick Vieira", "Lilian Thuram"],
         "It was the last match of Zidane's career. France went on to lose to Italy on penalties.",
         wiki("2006 FIFA World Cup final"), difficulty=2)
c.yes_no("Was the 2002 World Cup the first to be shared by two countries?", True,
         "Japan and South Korea hosted it together. It was also the first World Cup held in Asia.",
         wiki("2002 FIFA World Cup"), difficulty=2)
c.choice("Which Brazilian striker scored both goals in the 2002 World Cup final?", "Ronaldo", ["Ronaldinho", "Rivaldo", "Romário"],
         "Brazil beat Germany 2-0 in Yokohama. Ronaldo finished the tournament with eight goals.",
         wiki("2002 FIFA World Cup final"), difficulty=2)
c.choice("Who scored Spain's winning goal in the 2010 World Cup final?", "Andrés Iniesta", ["Fernando Torres", "David Villa", "Xavi"],
         "He scored in extra time against the Netherlands. It was Spain's first World Cup win.",
         wiki("2010 FIFA World Cup final"), difficulty=3)
c.choice("Which country won the 2014 World Cup in Brazil?", "Germany", ["Argentina", "Brazil", "The Netherlands"],
         "Mario Götze scored the only goal of the final against Argentina, in extra time.",
         wiki("2014 FIFA World Cup"), difficulty=2)
c.yes_no("Geoff Hurst scored a hat-trick in the 1966 World Cup final. Has anyone else ever scored a hat-trick in a men's World Cup final?", True,
         "Kylian Mbappé did it for France against Argentina in 2022, and still ended up on the losing side after a penalty shootout.",
         wiki("2022 FIFA World Cup final"), difficulty=2)
c.choice("At the 2010 World Cup, which animal became famous for 'predicting' match results?", "An octopus", ["A parrot", "A tortoise", "A goat"],
         "Paul the Octopus lived at an aquarium in Germany and picked the winner of all eight matches he was asked about.",
         wiki("Paul the Octopus"), era="modern", difficulty=1)
c.choice("What was World Cup Willie, the first World Cup mascot, in 1966?", "A lion", ["A bulldog", "A bear", "A fox"],
         "He wore a Union Jack shirt. Every World Cup since has had a mascot.",
         wiki("World Cup Willie"), era="classic", difficulty=2)
c.choice("Which country was allowed to keep the original World Cup trophy for good after winning it a third time, in 1970?", "Brazil", ["Italy", "Uruguay", "West Germany"],
         "The Jules Rimet Trophy was later stolen in Rio in 1983 and has never been found.",
         wiki("Jules Rimet Trophy"), era="classic", difficulty=2)
c.choice("Which country has won the Women's World Cup the most times?", "The United States", ["Germany", "Norway", "Spain"],
         "The USA have won it four times: 1991, 1999, 2015 and 2019.",
         wiki("FIFA Women's World Cup"), difficulty=2, as_of="2026-11")
c.choice("Which country will host the 2027 Women's World Cup?", "Brazil", ["Australia", "England", "Mexico"],
         "It will be the first Women's World Cup held in South America.",
         wiki("2027 FIFA Women's World Cup"), era="modern", difficulty=3)
c.choice("The 2030 World Cup will be hosted mainly by Spain, Portugal and which other country?", "Morocco", ["Italy", "Egypt", "France"],
         "The first three matches will be played in Uruguay, Argentina and Paraguay to mark 100 years since the first World Cup.",
         wiki("2030 FIFA World Cup"), era="modern", difficulty=2)
c.higher_lower("The first World Cup was in 1930. Was the first World Cup penalty shootout more or less than 50 years later?", True,
               "It was 52 years later, in the 1982 semi-final between West Germany and France. Before that, drawn knockout games were replayed or decided by drawing lots.",
               wiki("1982 FIFA World Cup"), labels=("More", "Less"), era="classic", difficulty=3)
c.choice("Which song did Shakira perform as the official song of the 2010 World Cup in South Africa?", "Waka Waka", ["Hips Don't Lie", "Whenever, Wherever", "La La La"],
         "Its full title is 'Waka Waka (This Time for Africa)'. It's one of the most-watched music videos on YouTube.",
         wiki("Waka Waka (This Time for Africa)"), era="modern", difficulty=2)

# The Euros and the Copa América ------------------------------------------------------------------------
c.choice("Which country won Euro 2024, beating England in the final in Berlin?", "Spain", ["France", "Germany", "Italy"],
         "Spain won 2-1. It was their record fourth European Championship.",
         wiki("UEFA Euro 2024"), era="modern", difficulty=1)
c.yes_no("Was Euro 2020 actually played in 2021?", True,
         "It was put back a year because of the pandemic but kept its name. Italy beat England on penalties in the final at Wembley.",
         wiki("UEFA Euro 2020"), era="modern", difficulty=1)
c.choice("Which country shocked Europe by winning Euro 2004 as huge outsiders?", "Greece", ["Denmark", "Portugal", "Czechia"],
         "Greece beat the hosts, Portugal, in both the opening match and the final.",
         wiki("UEFA Euro 2004"), difficulty=2)
c.yes_no("Did Denmark win Euro 1992 after only getting in as a late replacement?", True,
         "They took Yugoslavia's place about ten days before the tournament started, then beat Germany 2-0 in the final.",
         wiki("UEFA Euro 1992"), era="classic", difficulty=3)
c.choice("Which countries will host Euro 2028?", "The UK and Ireland", ["Spain and Portugal", "Italy and Turkey", "France and Belgium"],
         "Matches are planned in England, Scotland, Wales and the Republic of Ireland.",
         wiki("UEFA Euro 2028"), era="modern", difficulty=2)
c.choice("Which country has won the Copa América, South America's championship, the most times?", "Argentina", ["Brazil", "Uruguay", "Chile"],
         "Argentina have won it 16 times, one more than Uruguay. Brazil have won it nine times.",
         COPA, difficulty=3, as_of="2026-11")

# The Olympics --------------------------------------------------------------------------------------
c.choice("How often are the Summer Olympics usually held?", "Every 4 years", ["Every 2 years", "Every 5 years", "Every 6 years"],
         "The four years between Games is called an Olympiad.",
         wiki("Olympiad"), difficulty=1)
c.choice("Since 1994, how many years after a Summer Olympics are the Winter Olympics held?", "2", ["1", "3", "4"],
         "Until 1992 both were held in the same year. Now there's an Olympics of one kind every two years.",
         wiki("Winter Olympic Games"), difficulty=2)
c.yes_no("Was London the first city to host the Summer Olympics three times?", True,
         "London hosted in 1908, 1948 and 2012. Paris joined it in 2024 and Los Angeles will in 2028.",
         wiki("Summer Olympic Games"), difficulty=2)
c.choice("How many Olympic medals did the swimmer Michael Phelps win altogether?", "28", ["18", "22", "35"],
         "23 of them were gold. No other Olympian has won as many.",
         wiki("Michael Phelps"), difficulty=3)
c.choice("Which American athlete won four gold medals at the 1936 Olympics in Berlin?", "Jesse Owens", ["Carl Lewis", "Jim Thorpe", "Babe Ruth"],
         "He won the 100 m, 200 m, long jump and the relay.",
         wiki("Jesse Owens"), era="classic", difficulty=2)
c.choice("At the 1976 Olympics, who scored the first ever perfect 10 in gymnastics?", "Nadia Comăneci", ["Olga Korbut", "Simone Biles", "Mary Lou Retton"],
         "She was 14. The scoreboard couldn't show a 10, so it read 1.00.",
         wiki("Nadia Comăneci"), era="classic", difficulty=2)
c.choice("Which of these colours is not one of the five Olympic rings?", "Orange", ["Blue", "Green", "Yellow"],
         "The rings are blue, yellow, black, green and red, on white. Every country's flag had at least one of those colours.",
         wiki("Olympic symbols"), difficulty=1)
c.choice("Which country has hosted the Winter Olympics the most times?", "The United States", ["France", "Switzerland", "Norway"],
         "Four times: Lake Placid twice, Squaw Valley and Salt Lake City. Salt Lake City is due to host again in 2034.",
         wiki("Winter Olympic Games"), difficulty=3, as_of="2026-11")
c.choice("Who will host the 2030 Winter Olympics?", "The French Alps", ["Sapporo", "Salt Lake City", "Stockholm"],
         "It will be France's fourth Winter Olympics, after Chamonix, Grenoble and Albertville.",
         wiki("2030 Winter Olympics"), era="modern", difficulty=3)
c.choice("Which British rower won gold at five Olympics in a row, from 1984 to 2000?", "Steve Redgrave", ["Matthew Pinsent", "Chris Hoy", "Bradley Wiggins"],
         "After his fourth he famously said that anyone who saw him in a boat again could shoot him. He came back for Sydney anyway.",
         wiki("Steve Redgrave"), era="classic", difficulty=2)
c.choice("How many Olympic gold medals does Usain Bolt have?", "8", ["6", "9", "11"],
         "He won nine, but one relay gold from 2008 was taken away when a teammate failed a drugs test.",
         wiki("Usain Bolt"), difficulty=3)
c.choice("Which British ski jumper became a folk hero at the 1988 Winter Olympics, despite finishing last?", "Eddie 'the Eagle' Edwards", ["Franz Klammer", "Ted Ligety", "Alain Baxter"],
         "His story was made into the 2016 film Eddie the Eagle.",
         wiki("Eddie the Eagle"), era="classic", difficulty=2)
c.yes_no("Did Jamaica send a bobsleigh team to the 1988 Winter Olympics?", True,
         "A country with no snow, racing on ice. Their story inspired the film Cool Runnings.",
         wiki("Jamaica national bobsleigh team"), era="classic", difficulty=1)
c.choice("The marathon is named after a battle in which country?", "Greece", ["Italy", "Turkey", "Egypt"],
         "Legend says a messenger ran from Marathon to Athens with news of victory, then collapsed.",
         wiki("Marathon"), difficulty=2)
c.yes_no("Did the Olympic torch relay, carrying the flame to the host city, start in ancient Greece?", False,
         "The relay was first held for the 1936 Berlin Olympics. The ancient Games had a flame, but no relay.",
         wiki("Olympic flame"), difficulty=3)
c.choice("Which sport came back to the Olympics in 2016 after 112 years away?", "Golf", ["Cricket", "Polo", "Tug of war"],
         "Golf was last played at the 1904 Games in St Louis. Rugby sevens also joined in 2016.",
         wiki("Golf at the 2016 Summer Olympics"), difficulty=3)
c.yes_no("Was the opening ceremony of the Paris 2024 Olympics held on a river rather than in a stadium?", True,
         "Teams sailed along the Seine in boats. It was the first opening ceremony held outside a stadium.",
         wiki("2024 Summer Olympics opening ceremony"), era="modern", difficulty=1)
c.choice("Which Scottish city hosted the 2026 Commonwealth Games?", "Glasgow", ["Edinburgh", "Aberdeen", "Dundee"],
         "Glasgow stepped in when Victoria in Australia pulled out. Australia topped the medal table with 70 golds.",
         GLASGOW_2026, era="modern", difficulty=1)

# Formula One ---------------------------------------------------------------------------------------
c.choice("Which driver has won the most Formula One races?", "Lewis Hamilton", ["Michael Schumacher", "Max Verstappen", "Ayrton Senna"],
         "Hamilton has 106 wins. His first for Ferrari came at the Barcelona-Catalunya Grand Prix in June 2026, aged 41.",
         HAMILTON_WINS, difficulty=1, as_of="2026-11")
c.choice("Which team did Lewis Hamilton join in 2025?", "Ferrari", ["Red Bull", "McLaren", "Aston Martin"],
         "He left Mercedes after 12 seasons and six world titles there.",
         wiki("Lewis Hamilton"), era="modern", difficulty=1)
c.yes_no("Is Ferrari the oldest team still racing in Formula One?", True,
         "Ferrari has raced in every season since the championship began in 1950, and has won more races than any other team.",
         wiki("Scuderia Ferrari"), difficulty=2)
c.choice("Which British circuit hosted the very first Formula One World Championship race, in 1950?", "Silverstone", ["Brands Hatch", "Donington Park", "Goodwood"],
         "Silverstone was built on a wartime RAF airfield, and it still hosts the British Grand Prix.",
         wiki("1950 British Grand Prix"), difficulty=2)
c.choice("Which Grand Prix is raced through the streets of a tiny country on the French Riviera?", "Monaco", ["Monza", "Spa", "Marseille"],
         "The Monaco track is so narrow and twisty that overtaking is almost impossible.",
         wiki("Monaco Grand Prix"), difficulty=1)
c.choice("Which country did the great driver Ayrton Senna come from?", "Brazil", ["Argentina", "Portugal", "Italy"],
         "Senna won three world titles, in 1988, 1990 and 1991.",
         wiki("Ayrton Senna"), era="classic", difficulty=1)
c.choice("Which country does Max Verstappen race for?", "The Netherlands", ["Belgium", "Germany", "Austria"],
         "He was born in Belgium to a Dutch father and a Belgian mother, but races as a Dutchman. He was champion four years in a row, 2021 to 2024.",
         wiki("Max Verstappen"), era="modern", difficulty=2)
c.higher_lower("Max Verstappen won his first Formula One race in 2016. Was he older or younger than 20 at the time?", False,
               "He was 18, which makes him the youngest race winner ever.",
               wiki("Max Verstappen"), labels=("Older", "Younger"), era="modern", difficulty=2)
c.choice("How many points does a Formula One driver get for winning a race?", "25", ["10", "20", "50"],
         "The winner has scored 25 points since 2010. Before that it was 10.",
         wiki("List of Formula One World Championship points scoring systems"), difficulty=2)
c.choice("What does a black and white chequered flag mean in motor racing?", "The race is over", ["Danger ahead", "Slow down for a crash", "Come into the pits"],
         "Waving a yellow flag means danger: no overtaking.",
         wiki("Racing flags"), difficulty=1)
c.yes_no("Can a Formula One pit crew change all four tyres in under 2 seconds?", True,
         "The fastest stops are about 1.8 seconds, by a crew of around 20 people.",
         wiki("Pit stop"), difficulty=2)
c.choice("Which father and son were the first to both become Formula One world champions?", "Graham and Damon Hill", ["Keke and Nico Rosberg", "Jos and Max Verstappen", "Gilles and Jacques Villeneuve"],
         "Graham won in 1962 and 1968, and Damon in 1996. Keke and Nico Rosberg later did it too.",
         wiki("Damon Hill"), era="classic", difficulty=3)
c.choice("Which Scottish driver won three world titles and then spent decades campaigning for safer racing?", "Jackie Stewart", ["Jim Clark", "David Coulthard", "Paul di Resta"],
         "Jackie Stewart was champion in 1969, 1971 and 1973.",
         wiki("Jackie Stewart"), era="classic", difficulty=3)
c.choice("In 'Formula One', what does the word 'Formula' mean?", "The set of rules the cars must follow", ["The shape of the track", "The fuel the cars burn", "The way points are added up"],
         "Every car must be built to the same rule book, called the formula.",
         wiki("Formula One"), difficulty=2)
c.choice("Which city has hosted a night-time Formula One race along its famous Strip since 2023?", "Las Vegas", ["Miami", "Los Angeles", "New York"],
         "The track runs past the city's giant hotels and casinos.",
         wiki("Las Vegas Grand Prix"), era="modern", difficulty=1)
c.choice("In which country is the Suzuka circuit, with its unusual figure-of-eight layout?", "Japan", ["China", "South Korea", "Malaysia"],
         "A bridge carries one part of the track over another.",
         wiki("Suzuka International Racing Course"), difficulty=2)

# The big tournaments and events ----------------------------------------------------------------------
c.choice("What does the winner of the Masters golf tournament get to wear?", "A green jacket", ["A gold crown", "A red cap", "A white blazer"],
         "The Masters is played every April at Augusta National in Georgia, in the United States.",
         wiki("Masters Tournament"), difficulty=1)
c.higher_lower("Tiger Woods has won 15 of golf's major tournaments. Did Jack Nicklaus win more or fewer?", True,
               "Jack Nicklaus won 18, still the record.",
               wiki("Jack Nicklaus"), labels=("More", "Fewer"), difficulty=2)
c.choice("Who plays in golf's Ryder Cup?", "Europe against the United States", ["England against Scotland", "Amateurs against professionals", "The world's top 30 players"],
         "It's played every two years and has been going since 1927.",
         wiki("Ryder Cup"), difficulty=2)
c.yes_no("Was the 2019 Cricket World Cup final decided by a 'super over' after the scores were level?", True,
         "England and New Zealand tied the match and the super over. England won on boundaries scored, at Lord's.",
         wiki("2019 Cricket World Cup final"), era="modern", difficulty=2)
c.choice("Which horse won the Grand National three times in the 1970s?", "Red Rum", ["Shergar", "Desert Orchid", "Frankel"],
         "He won in 1973, 1974 and 1977, and is buried at the winning post at Aintree.",
         wiki("Red Rum"), era="classic", difficulty=2)
c.choice("Which two universities race each other in the Boat Race on the River Thames?", "Oxford and Cambridge", ["Durham and York", "Harvard and Yale", "Edinburgh and St Andrews"],
         "The first race was in 1829.",
         wiki("The Boat Race"), difficulty=1)
c.choice("Which team won Super Bowl LX in February 2026?", "The Seattle Seahawks", ["The New England Patriots", "The Kansas City Chiefs", "The Philadelphia Eagles"],
         "They beat the New England Patriots in Santa Clara, California. Bad Bunny did the halftime show.",
         ("JamBase: Bad Bunny's Super Bowl LX halftime show", "https://www.jambase.com/article/bad-bunny-super-bowl-lx-halftime-show-video"),
         era="modern", difficulty=3)
c.choice("Which rugby trophy do England and Scotland play for each year in the Six Nations?", "The Calcutta Cup", ["The Webb Ellis Cup", "The Triple Crown", "The Bledisloe Cup"],
         "It was made from melted-down silver rupees from a club in Calcutta, India.",
         wiki("Calcutta Cup"), difficulty=3)
c.choice("Which team gets the 'wooden spoon' in the Six Nations?", "The team that finishes last", ["The team with the youngest captain", "The winners", "The team with the most tries"],
         "It's not a real trophy, just a joke 'prize'.",
         wiki("Wooden spoon (award)"), difficulty=2)
c.higher_lower("Luke Littler won the World Darts Championship in January 2025. Was he older or younger than 18?", False,
               "He was 17, the youngest world champion ever.",
               wiki("Luke Littler"), labels=("Older", "Younger"), era="modern", difficulty=2)
c.choice("In which city is the Crucible Theatre, home of the World Snooker Championship?", "Sheffield", ["Manchester", "Nottingham", "Leeds"],
         "The championship has been held there every year since 1977.",
         wiki("Crucible Theatre"), difficulty=2)
c.choice("What was Muhammad Ali's name before he changed it in 1964?", "Cassius Clay", ["Joe Frazier", "Sonny Liston", "George Foreman"],
         "He changed his name soon after becoming heavyweight champion of the world.",
         wiki("Muhammad Ali"), era="classic", difficulty=2)
c.choice("In which country was the 1974 boxing match called the 'Rumble in the Jungle' held?", "Zaire, now DR Congo", ["Kenya", "Nigeria", "Brazil"],
         "Muhammad Ali beat George Foreman in Kinshasa, winning back the heavyweight title.",
         wiki("The Rumble in the Jungle"), era="classic", difficulty=3)
c.choice("In which year was the first London Marathon?", "1981", ["1971", "1991", "1966"],
         "Around 7,000 people started the first one. Now it's one of the biggest marathons in the world.",
         wiki("London Marathon"), difficulty=3)
c.choice("Which country joined rugby's Five Nations in 2000, turning it into the Six Nations?", "Italy", ["Argentina", "Georgia", "Spain"],
         "The other five are England, France, Ireland, Scotland and Wales.",
         wiki("Six Nations Championship"), difficulty=2)
