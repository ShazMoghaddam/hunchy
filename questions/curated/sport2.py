"""More sport: tennis, the Olympics, the Tour de France, the World Cup, the Champions League and footballers."""

from . import Category, wiki

c = Category("sport", prefix="sport2")
WIMBLEDON_2026 = ("Flashscore: Sinner goes back-to-back at Wimbledon as Noskova wins all-Czech epic",
                  "https://www.flashscore.com/news/tennis-wimbledon-atp-singles-the-base-line-sinner-goes-back-to-back-at-wimbledon-as-noskova-wins-all-czech-epic/foxlI0me/")
SLAMS_2026 = ("Tennis365: the active ATP players to win a Grand Slam title", "https://www.tennis365.com/facts-stats/active-atp-players-win-grand-slam-title")
UCL_2026 = ("Euronews: Paris Saint-Germain wins the Champions League after penalty shootout", "https://www.euronews.com/2026/05/30/paris-saint-germain-wins-the-champions-league-after-penalty-shootout-victory-against-arsen")
WC_GOALS = ("Fox Sports: World Cup goal scorers of all time", "https://www.foxsports.com/stories/soccer/world-cup-goal-scorers-all-time-messi-mbappe")

# Tennis -------------------------------------------------------------------------------------------
c.yes_no("Is the Australian Open the first Grand Slam tournament of each year?", True,
         "It's played in January, in the middle of the Australian summer. The French Open, Wimbledon and the US Open follow.",
         wiki("Australian Open"), difficulty=2)
c.choice("Which Grand Slam tournament is played on red clay?", "The French Open", ["The US Open", "Wimbledon", "The Australian Open"],
         "The French Open is played at Roland Garros in Paris. The clay is made of crushed brick.",
         wiki("French Open"), difficulty=1)
c.choice("In which city is the Australian Open played?", "Melbourne", ["Sydney", "Brisbane", "Perth"],
         "The main court, Rod Laver Arena, has a roof that closes when it's too hot or wet.",
         wiki("Australian Open"), difficulty=2)
c.choice("In which city is the US Open played?", "New York", ["Los Angeles", "Miami", "Chicago"],
         "It's played at Flushing Meadows in the borough of Queens.",
         wiki("US Open (tennis)"), difficulty=2)
c.choice("How many times did Rafael Nadal win the French Open?", "14", ["9", "11", "20"],
         "No player has won any Grand Slam tournament as many times. Nadal retired in 2024.",
         wiki("Rafael Nadal"), difficulty=2)
c.higher_lower("Roger Federer won 20 Grand Slam singles titles. Did Rafael Nadal win more or fewer?", True,
               "Nadal won 22. Novak Djokovic has won more than either of them.",
               wiki("Rafael Nadal"), labels=("More", "Fewer"), difficulty=2)
c.choice("Which man has won the most Grand Slam singles titles?", "Novak Djokovic", ["Rafael Nadal", "Roger Federer", "Pete Sampras"],
         "Novak Djokovic has won 24.",
         SLAMS_2026, era="modern", difficulty=2, as_of="2026-11")
c.choice("Which country does Roger Federer come from?", "Switzerland", ["Austria", "Germany", "Sweden"],
         "Federer grew up in Basel and once worked as a ball boy at his home tournament there.",
         wiki("Roger Federer"), difficulty=1)
c.choice("Which country does Novak Djokovic play for?", "Serbia", ["Croatia", "Russia", "Slovenia"],
         "Djokovic won Olympic gold for Serbia at the Paris 2024 Games.",
         wiki("Novak Djokovic"), difficulty=2)
c.choice("Which country does Jannik Sinner play for?", "Italy", ["Austria", "Switzerland", "Germany"],
         "Sinner grew up in South Tyrol, a German-speaking part of northern Italy, and was a champion junior skier.",
         wiki("Jannik Sinner"), era="modern", difficulty=2)
c.choice("Which country does Carlos Alcaraz play for?", "Spain", ["Argentina", "Italy", "Portugal"],
         "Carlos Alcaraz became the youngest man ever to be ranked world number one, in 2022.",
         wiki("Carlos Alcaraz"), era="modern", difficulty=1)
c.choice("Who won the men's singles at Wimbledon in 2026?", "Jannik Sinner", ["Carlos Alcaraz", "Novak Djokovic", "Jack Draper"],
         "It was his second Wimbledon title in a row. He beat Alexander Zverev in the final.",
         WIMBLEDON_2026, era="modern", difficulty=2)
c.choice("Which Czech player won the women's singles at Wimbledon in 2026?", "Linda Nosková", ["Barbora Krejčíková", "Petra Kvitová", "Markéta Vondroušová"],
         "It was her first Grand Slam title, in a final between two Czech players.",
         WIMBLEDON_2026, era="modern", difficulty=3)
c.choice("How many Grand Slam singles titles did Serena Williams win?", "23", ["18", "20", "27"],
         "That's the most by any woman since tennis turned professional in 1968.",
         wiki("Serena Williams"), difficulty=2)
c.yes_no("Are the tennis players Venus and Serena Williams sisters?", True,
         "Venus is the older sister. They won 14 Grand Slam doubles titles together.",
         wiki("Venus Williams"), difficulty=1)
c.choice("Which Grand Slam did Emma Raducanu win in 2021, after starting in the qualifying rounds?", "The US Open", ["Wimbledon", "The French Open", "The Australian Open"],
         "She won all ten of her matches without dropping a set, the first qualifier ever to win a Grand Slam.",
         wiki("Emma Raducanu"), era="modern", difficulty=2)
c.higher_lower("Men play the best of five sets at Grand Slams. Do women play more or fewer?", False,
               "Women play the best of three sets at Grand Slams.",
               wiki("Grand Slam (tennis)"), labels=("More", "Fewer"), difficulty=2)
c.choice("In 1988, who won all four Grand Slams and Olympic gold, the 'Golden Slam'?", "Steffi Graf", ["Martina Navratilova", "Monica Seles", "Chris Evert"],
         "Steffi Graf is still the only player to do it in a single year.",
         wiki("Steffi Graf"), era="classic", difficulty=3)
c.choice("Roughly how long did the longest tennis match ever last, at Wimbledon in 2010?", "Over 11 hours", ["About 5 hours", "About 8 hours", "Over 20 hours"],
         "John Isner beat Nicolas Mahut over three days. The final set ended 70-68.",
         wiki("Isner–Mahut match at the 2010 Wimbledon Championships"), difficulty=3)
c.yes_no("Do players at Wimbledon have to wear almost all white?", True,
         "Wimbledon's dress code has asked for white since the 1800s. Since 2023 women may wear dark undershorts.",
         wiki("The Championships, Wimbledon"), difficulty=1)
c.choice("Who beat Bobby Riggs in the 1973 tennis match called the 'Battle of the Sexes'?", "Billie Jean King", ["Margaret Court", "Chris Evert", "Martina Navratilova"],
         "About 90 million people around the world watched on television.",
         wiki("Battle of the Sexes (tennis)"), era="classic", difficulty=2)
c.choice("Which Swedish player won Wimbledon five years in a row from 1976?", "Björn Borg", ["Stefan Edberg", "Mats Wilander", "Robin Söderling"],
         "Borg won five Wimbledon titles in a row from 1976 to 1980.",
         wiki("Björn Borg"), era="classic", difficulty=2)
c.choice("How many Olympic gold medals did Andy Murray win in men's singles?", "Two", ["One", "Three", "None"],
         "He won in London in 2012 and Rio in 2016, the only player to win two Olympic singles golds.",
         wiki("Andy Murray"), era="modern", difficulty=2)
c.choice("In which year did Wimbledon switch from white tennis balls to yellow ones?", "1986", ["1968", "1999", "1975"],
         "Yellow balls are easier to see on television.",
         wiki("Tennis ball"), era="classic", difficulty=3)
c.choice("Which country does Naomi Osaka represent?", "Japan", ["The United States", "China", "South Korea"],
         "Naomi Osaka was born in Japan and grew up in the United States. She lit the cauldron at the Tokyo Olympics.",
         wiki("Naomi Osaka"), era="modern", difficulty=2)
c.choice("In tennis scoring, what comes after 15 and 30?", "40", ["45", "35", "50"],
         "The odd scores may come from clock faces: 15, 30 and 45, later shortened to 40.",
         wiki("Tennis scoring system"), difficulty=1)
c.yes_no("Did the French tennis player René Lacoste give his nickname to a famous clothing logo?", True,
         "He was nicknamed 'the Crocodile', and the crocodile became the logo of his shirt company.",
         wiki("René Lacoste"), era="classic", difficulty=2)

# The Olympics -------------------------------------------------------------------------------------
c.choice("In which city were the first modern Olympic Games held, in 1896?", "Athens", ["Paris", "London", "Rome"],
         "The Games returned to Greece, where the ancient Olympics began.",
         wiki("1896 Summer Olympics"), difficulty=2)
c.choice("Which Frenchman founded the modern Olympic Games?", "Pierre de Coubertin", ["Louis Pasteur", "Gustave Eiffel", "Jules Verne"],
         "He set up the International Olympic Committee in 1894.",
         wiki("Pierre de Coubertin"), difficulty=3)
c.choice("Which city hosted the 2008 Summer Olympics?", "Beijing", ["Tokyo", "Seoul", "Shanghai"],
         "The opening ceremony began at 8pm on 8 August 2008. Eight is a lucky number in China.",
         wiki("2008 Summer Olympics"), era="modern", difficulty=1)
c.choice("Which city will host the 2032 Summer Olympics?", "Brisbane", ["Sydney", "Doha", "Madrid"],
         "It will be Australia's third Summer Games, after Melbourne in 1956 and Sydney in 2000.",
         wiki("2032 Summer Olympics"), era="modern", difficulty=2)
c.choice("Which country hosted the 2026 Winter Olympics?", "Italy", ["France", "Switzerland", "Austria"],
         "The Games were shared between Milan and Cortina d'Ampezzo.",
         wiki("2026 Winter Olympics"), era="modern", difficulty=2)
c.yes_no("Were the Tokyo 2020 Olympics actually held in 2021?", True,
         "They were delayed a year because of the Covid-19 pandemic but kept the name Tokyo 2020.",
         wiki("2020 Summer Olympics"), era="modern", difficulty=1)
c.choice("Which country does Usain Bolt come from?", "Jamaica", ["Trinidad and Tobago", "The United States", "Barbados"],
         "Bolt won eight Olympic gold medals and still holds the 100 m and 200 m world records.",
         wiki("Usain Bolt"), difficulty=1)
c.choice("In which sport is Simone Biles a superstar?", "Gymnastics", ["Swimming", "Athletics", "Diving"],
         "Simone Biles has several moves named after her, because she was the first to land them in competition.",
         wiki("Simone Biles"), era="modern", difficulty=1)
c.choice("Which country has won the most Summer Olympic medals of all time?", "The United States", ["China", "Russia", "Great Britain"],
         "The USA has won well over 2,000 Summer Olympic medals.",
         wiki("All-time Olympic Games medal table"), difficulty=1, as_of="2026-11")
c.yes_no("Are Olympic gold medals made of solid gold?", False,
         "They're mostly silver, covered with at least 6 grams of gold. The last solid gold medals were given out in 1912.",
         wiki("Olympic medal"), difficulty=2)
c.choice("The Olympic motto is 'Faster, Higher, Stronger'. Which word was added in 2021?", "Together", ["Fairer", "Kinder", "Forever"],
         "In Latin the motto is now 'Citius, Altius, Fortius, Communiter'.",
         wiki("Olympic symbols"), era="modern", difficulty=3)
c.choice("Where is the Olympic flame lit before each Games?", "Olympia, in Greece", ["Athens", "Lausanne, in Switzerland", "The host city"],
         "It's lit with the Sun's rays and a curved mirror, then carried to the host city in a relay.",
         wiki("Olympic flame"), difficulty=2)
c.choice("Which country hosted the first Winter Olympics, in 1924?", "France", ["Switzerland", "Norway", "Austria"],
         "They were held in Chamonix, at the foot of Mont Blanc.",
         wiki("1924 Winter Olympics"), era="classic", difficulty=3)
c.choice("Which dance sport made its Olympic debut at Paris 2024?", "Breaking", ["Ballroom dancing", "Tap dancing", "Salsa"],
         "Breaking, or breakdancing, began in the Bronx, New York, in the 1970s.",
         wiki("Breakdancing at the 2024 Summer Olympics"), era="modern", difficulty=2)
c.choice("Which cyclist has won the most Olympic gold medals for Great Britain?", "Jason Kenny", ["Chris Hoy", "Bradley Wiggins", "Laura Kenny"],
         "Jason Kenny won seven golds. His wife, Laura Kenny, won five, the most by a British woman.",
         wiki("Jason Kenny"), era="modern", difficulty=3, as_of="2026-11")
c.choice("Which English village is known as the birthplace of the Paralympic Games?", "Stoke Mandeville", ["Wimbledon", "Bisham", "Loughborough"],
         "Dr Ludwig Guttmann held games for injured soldiers at Stoke Mandeville hospital in 1948.",
         wiki("Stoke Mandeville Games"), difficulty=3)
c.choice("How many events are there in an Olympic decathlon?", "10", ["7", "5", "12"],
         "Deca means ten. Women's heptathlons have seven events.",
         wiki("Decathlon"), difficulty=1)
c.yes_no("Were the 2016 Olympics in Rio de Janeiro the first held in South America?", True,
         "Rio was the first South American city to host the Olympic Games.",
         wiki("2016 Summer Olympics"), era="modern", difficulty=2)

# The Tour de France -------------------------------------------------------------------------------
c.choice("In which city does the Tour de France traditionally finish?", "Paris", ["Lyon", "Marseille", "Nice"],
         "Riders usually finish on the Champs-Élysées. In 2024 it ended in Nice instead, because Paris was getting ready for the Olympics.",
         wiki("Tour de France"), difficulty=1)
c.choice("In which year was the first Tour de France?", "1903", ["1896", "1921", "1950"],
         "It was set up by a sports newspaper, L'Auto, to sell more copies.",
         wiki("1903 Tour de France"), era="classic", difficulty=3)
c.choice("In the Tour de France, who wears the green jersey?", "The best sprinter, with the most points", ["The overall leader", "The best young rider", "The best climber"],
         "Points are won at the end of stages and at sprints along the way.",
         wiki("Points classification in the Tour de France"), difficulty=2)
c.choice("In the Tour de France, what does the white jersey with red polka dots mean?", "The best climber, or King of the Mountains", ["The best sprinter", "The youngest rider", "The last rider"],
         "Points are won by getting to the tops of climbs first.",
         wiki("Mountains classification in the Tour de France"), difficulty=2)
c.choice("Who was the first British rider to win the Tour de France, in 2012?", "Bradley Wiggins", ["Chris Froome", "Mark Cavendish", "Geraint Thomas"],
         "Weeks later he won Olympic gold in the time trial in London.",
         wiki("Bradley Wiggins"), era="modern", difficulty=2)
c.choice("Which British rider won the Tour de France four times, in 2013, 2015, 2016 and 2017?", "Chris Froome", ["Bradley Wiggins", "Geraint Thomas", "Mark Cavendish"],
         "Chris Froome was born in Kenya and grew up there and in South Africa.",
         wiki("Chris Froome"), era="modern", difficulty=2)
c.choice("Which Slovenian rider won the Tour de France in 2020, 2021, 2024 and 2025?", "Tadej Pogačar", ["Primož Roglič", "Jonas Vingegaard", "Remco Evenepoel"],
         "Pogačar first won at the age of 21.",
         wiki("Tadej Pogačar"), era="modern", difficulty=3)
c.choice("Roughly how long does the Tour de France last?", "About three weeks", ["About one week", "About two months", "Four days"],
         "There are 21 stages, with two rest days.",
         wiki("Tour de France"), difficulty=2)
c.yes_no("Does the Tour de France ever start outside France?", True,
         "It often does. In 2014 it started in Yorkshire, and in 2024 in Florence, Italy.",
         wiki("Tour de France"), difficulty=2)
c.higher_lower("Mark Cavendish won 35 Tour de France stages. Did the great Eddy Merckx win more or fewer?", False,
               "Merckx won 34. Cavendish broke his record in 2024.",
               wiki("Mark Cavendish"), labels=("More", "Fewer"), era="modern", difficulty=3)

# The World Cup ------------------------------------------------------------------------------------
c.choice("Who is the all-time top scorer at men's World Cups?", "Kylian Mbappé", ["Miroslav Klose", "Lionel Messi", "Pelé"],
         "Mbappé scored 10 goals at the 2026 World Cup, taking him to 22 and past Miroslav Klose's old record of 16.",
         WC_GOALS, era="modern", difficulty=2, as_of="2026-11")
c.choice("Which country won the first World Cup, in 1930?", "Uruguay", ["Brazil", "Argentina", "Italy"],
         "Uruguay also hosted it, and beat Argentina 4-2 in the final.",
         wiki("1930 FIFA World Cup"), era="classic", difficulty=2)
c.choice("Which country hosted the first World Cup in Africa, in 2010?", "South Africa", ["Egypt", "Nigeria", "Morocco"],
         "Spain won it, and the noisy vuvuzela horns became famous around the world.",
         wiki("2010 FIFA World Cup"), era="modern", difficulty=1)
c.yes_no("Did Pelé win the World Cup three times as a player?", True,
         "He won in 1958, 1962 and 1970, the only player to win three.",
         wiki("Pelé"), era="classic", difficulty=2)
c.choice("By what score did Germany beat hosts Brazil in the 2014 World Cup semi-final?", "7-1", ["3-0", "4-2", "5-0"],
         "Germany were 5-0 up within 30 minutes. They went on to win the final.",
         wiki("Brazil v Germany (2014 FIFA World Cup)"), era="modern", difficulty=2)
c.choice("Which country won the 2006 World Cup in Germany?", "Italy", ["France", "Germany", "Brazil"],
         "Italy beat France on penalties in the final in Berlin.",
         wiki("2006 FIFA World Cup final"), era="modern", difficulty=2)
c.choice("Which country won the 2018 World Cup in Russia?", "France", ["Croatia", "Belgium", "England"],
         "France beat Croatia 4-2 in Moscow. Kylian Mbappé scored in the final at 19.",
         wiki("2018 FIFA World Cup final"), era="modern", difficulty=2)
c.choice("Who won the Golden Boot as top scorer at the 2022 World Cup?", "Kylian Mbappé", ["Lionel Messi", "Olivier Giroud", "Harry Kane"],
         "Mbappé scored eight goals, including a hat-trick in the final, but still finished on the losing side.",
         wiki("2022 FIFA World Cup"), era="modern", difficulty=2)
c.choice("What was the name of the dog who found the stolen World Cup trophy in London in 1966?", "Pickles", ["Rover", "Lucky", "Biscuit"],
         "Pickles found it wrapped in newspaper under a hedge in south London.",
         wiki("1966 FIFA World Cup"), era="classic", difficulty=2)
c.yes_no("Has the England men's team won the World Cup more than once?", False,
         "England have won it once, at home in 1966.",
         wiki("England national football team"), difficulty=1, as_of="2026-11")
c.choice("How many teams played at the 2026 World Cup?", "48", ["32", "24", "64"],
         "It was the first World Cup with 48 teams, up from 32.",
         wiki("2026 FIFA World Cup"), era="modern", difficulty=2)
c.higher_lower("Brazil have won five World Cups. Have Germany won more or fewer?", False,
               "Germany have won four: 1954, 1974, 1990 and 2014.",
               wiki("Germany national football team"), labels=("More", "Fewer"), difficulty=2, as_of="2026-11")

# The Champions League -----------------------------------------------------------------------------
c.choice("Which club has won the European Cup and Champions League the most times?", "Real Madrid", ["AC Milan", "Bayern Munich", "Liverpool"],
         "Real Madrid have won it 15 times, including the first five in a row from 1956.",
         wiki("Real Madrid CF"), difficulty=1, as_of="2026-11")
c.choice("Which club won the Champions League in both 2025 and 2026?", "Paris Saint-Germain", ["Real Madrid", "Arsenal", "Inter Milan"],
         "PSG beat Inter Milan 5-0 in 2025, then Arsenal on penalties in Budapest in 2026.",
         UCL_2026, era="modern", difficulty=2)
c.choice("Which English club came back from 3-0 down to win the 2005 Champions League final in Istanbul?", "Liverpool", ["Chelsea", "Manchester United", "Arsenal"],
         "Liverpool scored three goals in six minutes against AC Milan, then won on penalties.",
         wiki("2005 UEFA Champions League final"), era="modern", difficulty=2)
c.choice("Which club scored twice in stoppage time to win the 1999 Champions League final?", "Manchester United", ["Bayern Munich", "Arsenal", "Juventus"],
         "United were losing 1-0 to Bayern Munich until the last minutes, then won 2-1 to complete a treble.",
         wiki("1999 UEFA Champions League final"), era="classic", difficulty=2)
c.choice("Which Scottish club became the first British team to win the European Cup, in 1967?", "Celtic", ["Rangers", "Aberdeen", "Hearts"],
         "Every player in the team was born within about 30 miles of Celtic Park. They're remembered as the Lisbon Lions.",
         wiki("Lisbon Lions"), era="classic", difficulty=3)
c.yes_no("Have Nottingham Forest won more European Cups than English league titles?", True,
         "Forest won the European Cup twice, in 1979 and 1980, but the English league only once, in 1978.",
         wiki("Nottingham Forest F.C."), era="classic", difficulty=3)
c.choice("The Champions League anthem is based on which composer's music?", "George Frideric Handel", ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Edward Elgar"],
         "It's based on Handel's 'Zadok the Priest', written for the coronation of King George II in 1727.",
         wiki("UEFA Champions League Anthem"), difficulty=3)
c.choice("Who has scored the most goals in Champions League history?", "Cristiano Ronaldo", ["Lionel Messi", "Robert Lewandowski", "Karim Benzema"],
         "Cristiano Ronaldo scored 140 Champions League goals, for Manchester United, Real Madrid and Juventus.",
         wiki("Cristiano Ronaldo"), era="modern", difficulty=2, as_of="2026-11")
c.choice("Which club won the treble of the Premier League, FA Cup and Champions League in 2023?", "Manchester City", ["Liverpool", "Arsenal", "Chelsea"],
         "City beat Inter Milan 1-0 in the final in Istanbul, their first Champions League win.",
         wiki("2023 UEFA Champions League final"), era="modern", difficulty=2)
c.choice("Which Dutch club won the European Cup three times in a row, from 1971 to 1973?", "Ajax", ["PSV Eindhoven", "Feyenoord", "AZ Alkmaar"],
         "Their 'Total Football', led by Johan Cruyff, changed how the game was played.",
         wiki("AFC Ajax"), era="classic", difficulty=3)
c.higher_lower("The European Cup began in 1955. Was it renamed the Champions League before or after 1990?", False,
               "It became the Champions League in the 1992 to 1993 season.",
               wiki("UEFA Champions League"), labels=("Before", "After"), difficulty=2)

# Footballers and where they come from ---------------------------------------------------------------
c.choice("Which country does Erling Haaland play for?", "Norway", ["Sweden", "Denmark", "Iceland"],
         "Haaland was actually born in Leeds, where his father played for Leeds United.",
         wiki("Erling Haaland"), era="modern", difficulty=1)
c.choice("Which country does Mohamed Salah play for?", "Egypt", ["Morocco", "Tunisia", "Algeria"],
         "Salah is nicknamed the Egyptian King by Liverpool fans.",
         wiki("Mohamed Salah"), era="modern", difficulty=1)
c.choice("Which country does Kevin De Bruyne play for?", "Belgium", ["The Netherlands", "Denmark", "Germany"],
         "De Bruyne won six Premier League titles with Manchester City.",
         wiki("Kevin De Bruyne"), era="modern", difficulty=2)
c.choice("Which country did Luka Modrić captain to the 2018 World Cup final?", "Croatia", ["Serbia", "Slovenia", "Bosnia and Herzegovina"],
         "Modrić was named the best player of that tournament.",
         wiki("Luka Modrić"), era="modern", difficulty=2)
c.choice("Which country does Robert Lewandowski play for?", "Poland", ["Germany", "Czechia", "Ukraine"],
         "He once scored five goals in nine minutes for Bayern Munich.",
         wiki("Robert Lewandowski"), era="modern", difficulty=2)
c.choice("Which country does Son Heung-min play for?", "South Korea", ["Japan", "China", "Vietnam"],
         "Son won the Premier League Golden Boot in 2022 while at Tottenham.",
         wiki("Son Heung-min"), era="modern", difficulty=1)
c.choice("Which country does Vinícius Júnior play for?", "Brazil", ["Portugal", "Argentina", "Colombia"],
         "He won the FIFA Best Men's Player award for 2024.",
         wiki("Vinícius Júnior"), era="modern", difficulty=2)
c.choice("Which country does the young winger Lamine Yamal play for?", "Spain", ["Morocco", "Portugal", "France"],
         "Lamine Yamal won Euro 2024 with Spain when he was just 17.",
         wiki("Lamine Yamal"), era="modern", difficulty=1)
c.choice("Which country did Zlatan Ibrahimović play for?", "Sweden", ["Bosnia and Herzegovina", "Denmark", "Croatia"],
         "Zlatan scored a famous overhead kick from about 30 metres against England in 2012.",
         wiki("Zlatan Ibrahimović"), era="modern", difficulty=2)
c.choice("Which country did Didier Drogba play for?", "Côte d'Ivoire (Ivory Coast)", ["Ghana", "Cameroon", "Nigeria"],
         "Drogba scored the equaliser and the winning penalty for Chelsea in the 2012 Champions League final.",
         wiki("Didier Drogba"), era="modern", difficulty=2)
c.choice("George Best, one of the greatest dribblers ever, played for which country?", "Northern Ireland", ["Scotland", "Wales", "The Republic of Ireland"],
         "Best won the European Cup with Manchester United in 1968.",
         wiki("George Best"), era="classic", difficulty=2)
c.choice("Which country did Gareth Bale play for?", "Wales", ["England", "Scotland", "Northern Ireland"],
         "Bale led Wales to their first World Cup in 64 years, in 2022.",
         wiki("Gareth Bale"), era="modern", difficulty=1)
c.choice("Johan Cruyff, famous for the 'Cruyff turn', played for which country?", "The Netherlands", ["Belgium", "Germany", "Denmark"],
         "He showed off the Cruyff turn at the 1974 World Cup.",
         wiki("Johan Cruyff"), era="classic", difficulty=2)
c.choice("Which country did Thierry Henry play for?", "France", ["Belgium", "Senegal", "Switzerland"],
         "Henry is Arsenal's all-time top scorer, with 228 goals.",
         wiki("Thierry Henry"), era="modern", difficulty=1)
c.choice("Which of these footballers plays for Portugal?", "Cristiano Ronaldo", ["Luka Modrić", "Kylian Mbappé", "Erling Haaland"],
         "Cristiano Ronaldo has scored more goals for his country than any other man in history.",
         wiki("Cristiano Ronaldo"), era="modern", difficulty=1)
c.choice("Which of these footballers played for Argentina?", "Diego Maradona", ["Pelé", "Ronaldinho", "Eusébio"],
         "Maradona captained Argentina to the World Cup in 1986.",
         wiki("Diego Maradona"), era="classic", difficulty=1)
c.choice("Which country did the great striker Eusébio play for?", "Portugal", ["Brazil", "Mozambique", "Angola"],
         "Eusébio was born in Mozambique, then a Portuguese colony, and was top scorer at the 1966 World Cup.",
         wiki("Eusébio"), era="classic", difficulty=3)
c.yes_no("Does Jude Bellingham play for England?", True,
         "Bellingham joined Real Madrid from Borussia Dortmund in 2023.",
         wiki("Jude Bellingham"), era="modern", difficulty=1)
c.yes_no("Does Kylian Mbappé play for Belgium?", False,
         "Mbappé plays for France. He won the World Cup with them in 2018.",
         wiki("Kylian Mbappé"), era="modern", difficulty=1)
c.yes_no("Did Lionel Messi win the World Cup with Argentina?", True,
         "Messi lifted the trophy in Qatar in 2022, at his fifth World Cup.",
         wiki("Lionel Messi"), era="modern", difficulty=1)
