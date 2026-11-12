from . import Category, wiki

c = Category("sport")
WC2026 = ("ABC News: Spain defeats Argentina 1-0 to win 2026 World Cup", "https://abcnews.com/culture/story/spain-argentina-win-2026-world-cup-134824556")
F1_2025 = ("Formula 1: Norris seals his debut title in Abu Dhabi", "https://www.formula1.com/en/latest/article/abu-dhabi-lowdown-all-the-key-moments-as-norris-seals-his-debut-title-and.6WLoFRGsfe4fbq1TZeoVIa")

# Football
c.choice("Which country won the 2026 FIFA World Cup?", "Spain", ["Argentina", "France", "England"],
         "Spain beat Argentina 1-0 after extra time in the final on 19 July 2026, their second World Cup win after 2010.",
         WC2026, era="modern", difficulty=2)
c.choice("Which country won the 2022 FIFA World Cup in Qatar?", "Argentina", ["France", "Brazil", "Croatia"],
         "Argentina beat France on penalties after a 3-3 draw, in one of the most exciting finals ever played.",
         wiki("2022 FIFA World Cup final"), era="modern", difficulty=1)
c.choice("In which year did England win the men's football World Cup?", "1966", ["1970", "1990", "1958"],
         "England beat West Germany 4-2 after extra time at Wembley. Geoff Hurst scored a hat-trick.",
         wiki("1966 FIFA World Cup final"), era="classic", difficulty=1)
c.choice("Which country has won the men's football World Cup the most times?", "Brazil", ["Germany", "Italy", "Argentina"],
         "Brazil have won it five times: 1958, 1962, 1970, 1994 and 2002.",
         wiki("FIFA World Cup"), difficulty=1, as_of="2026-11")
c.choice("Which countries hosted the 2026 World Cup together?", "The USA, Canada and Mexico", ["Spain, Portugal and Morocco", "England, Scotland and Wales", "Argentina, Uruguay and Paraguay"],
         "It was the first World Cup with 48 teams, and the first hosted by three countries.",
         wiki("2026 FIFA World Cup"), era="modern", difficulty=2)
c.choice("In which year did the Premier League begin?", "1992", ["1888", "1982", "2000"],
         "The Premier League replaced the old First Division as the top league in English football in 1992.",
         wiki("Premier League"), difficulty=2)
c.choice("Which club has won the most Premier League titles?", "Manchester United", ["Manchester City", "Liverpool", "Chelsea"],
         "Manchester United won 13 Premier League titles, all under Sir Alex Ferguson.",
         wiki("List of English football champions"), difficulty=2, as_of="2026-11")
c.choice("Who has scored the most goals in Premier League history?", "Alan Shearer", ["Harry Kane", "Wayne Rooney", "Mohamed Salah"],
         "Alan Shearer scored 260 Premier League goals for Blackburn Rovers and Newcastle United.",
         wiki("Alan Shearer"), era="classic", difficulty=2, as_of="2026-11")
c.choice("How many players does each team have on the pitch in a football match?", "11", ["10", "12", "9"],
         "Each side has ten outfield players and one goalkeeper.",
         wiki("Association football"), difficulty=1)
c.choice("Which is the oldest national football competition in the world?", "The FA Cup", ["The Premier League", "The Scottish Cup", "The World Cup"],
         "The first FA Cup was played in the 1871 to 1872 season. Wanderers won the first final.",
         wiki("FA Cup"), era="classic", difficulty=2)
c.choice("Which team, nicknamed the Lionesses, won the women's European Championship in 2022 and 2025?", "England", ["Spain", "Germany", "The Netherlands"],
         "England beat Germany 2-1 at Wembley in 2022, and Spain on penalties in Basel in 2025.",
         wiki("England women's national football team"), era="modern", difficulty=1)
c.choice("Which country won the 2023 Women's World Cup?", "Spain", ["England", "The USA", "Sweden"],
         "Spain beat England 1-0 in the final in Sydney.",
         wiki("2023 FIFA Women's World Cup"), era="modern", difficulty=2)
c.choice("Which footballer has won the Ballon d'Or, the award for the world's best player, the most times?", "Lionel Messi", ["Cristiano Ronaldo", "Michel Platini", "Johan Cruyff"],
         "Lionel Messi has won it eight times, most recently in 2023.",
         wiki("Ballon d'Or"), era="modern", difficulty=1, as_of="2026-11")
c.choice("Who scored the 'Hand of God' goal against England at the 1986 World Cup?", "Diego Maradona", ["Pelé", "Lionel Messi", "Mario Kempes"],
         "Four minutes later, Maradona dribbled past half the England team to score what was voted the Goal of the Century.",
         wiki("Argentina v England (1986 FIFA World Cup)"), era="classic", difficulty=2)
c.choice("Which national stadium in London has an arch over it?", "Wembley Stadium", ["Twickenham", "The Emirates", "Stamford Bridge"],
         "The new Wembley opened in 2007. Its arch is 133 metres tall.",
         wiki("Wembley Stadium"), era="modern", difficulty=1)

# Olympics and athletics
c.choice("Who holds the men's 100 metres world record?", "Usain Bolt", ["Carl Lewis", "Justin Gatlin", "Noah Lyles"],
         "Usain Bolt ran 9.58 seconds in Berlin in 2009.",
         wiki("Men's 100 metres world record progression"), difficulty=1, as_of="2026-11")
c.higher_lower("Usain Bolt's 100 metres world record is 9.58 seconds. Is the women's world record faster or slower than 10.5 seconds?", True,
               "Florence Griffith-Joyner ran 10.49 seconds in 1988. Her record still stands.",
               wiki("Women's 100 metres world record progression"), labels=("Faster", "Slower"), era="classic", difficulty=3, as_of="2026-11")
c.choice("How many rings are on the Olympic flag?", "Five", ["Four", "Six", "Seven"],
         "The five rings stand for the five inhabited continents joined by the Games.",
         wiki("Olympic symbols"), difficulty=1)
c.choice("Which swimmer has won the most Olympic gold medals?", "Michael Phelps", ["Mark Spitz", "Ian Thorpe", "Katie Ledecky"],
         "Michael Phelps won 23 gold medals, and 28 medals in all, between 2004 and 2016.",
         wiki("Michael Phelps"), era="modern", difficulty=2, as_of="2026-11")
c.choice("Which city hosted the 2024 Summer Olympics?", "Paris", ["Tokyo", "Los Angeles", "London"],
         "It was Paris's third time hosting, a hundred years after it last did so in 1924.",
         wiki("2024 Summer Olympics"), era="modern", difficulty=1)
c.choice("Which city will host the 2028 Summer Olympics?", "Los Angeles", ["Brisbane", "Madrid", "Paris"],
         "It will be the third time Los Angeles has hosted, after 1932 and 1984. Brisbane hosts in 2032.",
         wiki("2028 Summer Olympics"), era="modern", difficulty=2)
c.choice("How long is a marathon?", "26.2 miles (42.195 km)", ["20 miles (32 km)", "30 miles (48 km)", "13.1 miles (21 km)"],
         "The odd distance comes from the 1908 London Olympics, where the course was laid out to finish in front of the royal box.",
         wiki("Marathon"), difficulty=2)
c.choice("Which British runner won the 5,000 m and 10,000 m at both the 2012 and 2016 Olympics?", "Mo Farah", ["Paula Radcliffe", "Steve Cram", "Kelly Holmes"],
         "Mo Farah's four Olympic gold medals make him Britain's most successful track athlete.",
         wiki("Mo Farah"), era="modern", difficulty=2)
c.choice("What is the highest score possible with three darts?", "180", ["150", "200", "171"],
         "Three darts in the treble 20 score 3 × 60 = 180.",
         wiki("Darts"), difficulty=2)
c.choice("What is the highest break possible in snooker, without any fouls?", "147", ["100", "155", "180"],
         "A maximum break means potting all 15 reds with 15 blacks, then all six colours.",
         wiki("Maximum break"), difficulty=3)

# Tennis
c.choice("On what surface is Wimbledon played?", "Grass", ["Clay", "Hard court", "Carpet"],
         "Wimbledon is the only one of the four Grand Slam tournaments still played on grass.",
         wiki("The Championships, Wimbledon"), difficulty=1)
c.choice("Which British man won Wimbledon in 2013, the first home winner of the men's title for 77 years?", "Andy Murray", ["Tim Henman", "Greg Rusedski", "Jack Draper"],
         "Before Andy Murray, the last British man to win was Fred Perry in 1936. Murray won again in 2016.",
         wiki("Andy Murray"), era="modern", difficulty=1)
c.choice("Which man has won the most Wimbledon singles titles?", "Roger Federer", ["Novak Djokovic", "Pete Sampras", "Björn Borg"],
         "Roger Federer won eight Wimbledon titles between 2003 and 2017.",
         wiki("List of Wimbledon gentlemen's singles champions"), era="modern", difficulty=2, as_of="2026-11")
c.choice("Which woman has won the most Wimbledon singles titles?", "Martina Navratilova", ["Serena Williams", "Steffi Graf", "Venus Williams"],
         "Martina Navratilova won nine Wimbledon singles titles, six of them in a row from 1982 to 1987.",
         wiki("List of Wimbledon ladies' singles champions"), era="classic", difficulty=3, as_of="2026-11")
c.choice("How many Grand Slam tennis tournaments are there each year?", "Four", ["Three", "Five", "Six"],
         "The Australian Open, the French Open, Wimbledon and the US Open.",
         wiki("Grand Slam (tennis)"), difficulty=1)
c.choice("What is a score of zero called in tennis?", "Love", ["Nil", "Duck", "Nought"],
         "Nobody is quite sure why. One idea is that it comes from playing 'for love', rather than for anything.",
         wiki("Tennis scoring system"), difficulty=1)

# Motor racing, rugby, cricket and more
c.choice("Which drivers share the record of seven Formula One world titles?", "Lewis Hamilton and Michael Schumacher", ["Ayrton Senna and Alain Prost", "Max Verstappen and Sebastian Vettel", "Nigel Mansell and Jackie Stewart"],
         "Michael Schumacher won his seventh in 2004, and Lewis Hamilton equalled him in 2020.",
         wiki("List of Formula One World Drivers' Champions"), era="modern", difficulty=2, as_of="2026-11")
c.choice("Who won the 2025 Formula One world championship?", "Lando Norris", ["Max Verstappen", "Oscar Piastri", "Lewis Hamilton"],
         "Lando Norris of McLaren clinched his first title at the last race of the season in Abu Dhabi.",
         F1_2025, era="modern", difficulty=2)
c.choice("Which club won the Premier League in the 2025 to 2026 season?", "Arsenal", ["Manchester City", "Liverpool", "Chelsea"],
         "It was Arsenal's first league title for 22 years, since their unbeaten 'Invincibles' season of 2003 to 2004.",
         ("Premier League: Arsenal end 22-year wait for Premier League title", "https://www.premierleague.com/es/news/4662306/arsenal-win-2025-26-premier-league-title-ending-22-year-wait-to-be-crowned-champions-again"),
         era="modern", difficulty=2)
c.choice("How many players does a rugby union team have on the pitch?", "15", ["11", "13", "18"],
         "Rugby union has 15 players a side. Rugby league has 13.",
         wiki("Rugby union"), difficulty=2)
c.choice("Which country won the 2023 Rugby World Cup?", "South Africa", ["New Zealand", "France", "England"],
         "South Africa beat New Zealand 12-11 in Paris, winning a record fourth title.",
         wiki("2023 Rugby World Cup final"), era="modern", difficulty=2)
c.choice("Whose drop goal won England the Rugby World Cup in 2003?", "Jonny Wilkinson", ["Martin Johnson", "Jason Robinson", "Owen Farrell"],
         "Wilkinson kicked it in the last minute of extra time against Australia in Sydney.",
         wiki("2003 Rugby World Cup final"), era="modern", difficulty=2)
c.choice("What is the famous trophy that England and Australia play for in cricket?", "The Ashes", ["The Calcutta Cup", "The Ryder Cup", "The Webb Ellis Cup"],
         "The trophy is a tiny urn. The name comes from a joke 1882 obituary saying English cricket had died.",
         wiki("The Ashes"), difficulty=1)
c.choice("How many players are in a cricket team?", "11", ["9", "12", "15"],
         "Eleven players a side, and a match can last from a few hours to five days.",
         wiki("Cricket"), difficulty=1)
c.choice("In golf, what is it called when you take one shot fewer than par on a hole?", "A birdie", ["An eagle", "A bogey", "An albatross"],
         "One under par is a birdie, two under is an eagle, and one over is a bogey.",
         wiki("Par (score)"), difficulty=2)
c.choice("Which basketball player led the Chicago Bulls to six NBA titles in the 1990s?", "Michael Jordan", ["Kobe Bryant", "LeBron James", "Magic Johnson"],
         "Jordan won six championships in two 'three-peats': 1991 to 1993 and 1996 to 1998.",
         wiki("Michael Jordan"), era="classic", difficulty=1)
c.choice("How high is a basketball hoop?", "10 feet (3.05 m)", ["8 feet (2.44 m)", "12 feet (3.66 m)", "9 feet (2.74 m)"],
         "The hoop height was set at 10 feet by James Naismith, who invented the game in 1891.",
         wiki("Basketball"), difficulty=3)
c.choice("Which boxer called himself 'The Greatest'?", "Muhammad Ali", ["Mike Tyson", "Joe Frazier", "Sugar Ray Leonard"],
         "Muhammad Ali won the world heavyweight title three times.",
         wiki("Muhammad Ali"), era="classic", difficulty=1)
c.choice("What colour jersey does the leader of the Tour de France wear?", "Yellow", ["Pink", "Green", "Red"],
         "The yellow jersey, or maillot jaune, has been worn by the race leader since 1919.",
         wiki("General classification in the Tour de France"), difficulty=2)
c.choice("Which sport is played in the Super Bowl?", "American football", ["Baseball", "Basketball", "Ice hockey"],
         "The Super Bowl decides the champion of the NFL. It's one of the most watched TV events in the world.",
         wiki("Super Bowl"), difficulty=1)
c.choice("Which British diver won Olympic gold in 2021 at his fourth Games?", "Tom Daley", ["Jack Laugher", "Chris Mears", "Peter Waterfield"],
         "Tom Daley won the synchronised 10 m platform with Matty Lee at the Tokyo Olympics, held in 2021. He also knitted in the stands.",
         wiki("Tom Daley"), era="modern", difficulty=2)
c.choice("In which sport would you use a shuttlecock?", "Badminton", ["Squash", "Table tennis", "Volleyball"],
         "A shuttlecock has 16 feathers. The fastest smashes are over 400 km/h.",
         wiki("Shuttlecock"), difficulty=1)
c.choice("Which country invented the sport of judo?", "Japan", ["China", "South Korea", "Brazil"],
         "Jigoro Kano created judo in Japan in 1882. Its name means 'the gentle way'.",
         wiki("Judo"), difficulty=2)
c.higher_lower("A football pitch is usually about 100 metres long. Is a standard running track lap longer or shorter?", True,
               "One lap of a standard track is 400 metres.",
               wiki("Running track"), labels=("Longer", "Shorter"), difficulty=1)
c.choice("Which country won the most gold medals at the Paris 2024 Olympics?", "The United States", ["China", "Great Britain", "France"],
         "The USA and China both won 40 golds, but the USA won more silver medals, so came top.",
         wiki("2024 Summer Olympics medal table"), era="modern", difficulty=2)

assert len(c.questions) == 50, len(c.questions)
