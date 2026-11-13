"""More music: who sang it, which song belongs to which star, and the stories behind the hits.

Questions only ever use song titles, never lyrics. The wrong answers are picked to tempt: songs with nearly the
same title, the singer who made the cover famous, or the act from the same scene. Every song and artist was checked
against a second source (see CHECKS.md).
"""

from . import Category, wiki

c = Category("music", prefix="music4")

# Which of these is theirs? -------------------------------------------------------------------------
c.choice("Which of these is a Madonna song?", "Like a Prayer", ["Livin' on a Prayer", "Like a Rolling Stone", "I'm Like a Bird"],
         "Like a Prayer came out in 1989. 'Livin' on a Prayer' is Bon Jovi, 'Like a Rolling Stone' is Bob Dylan and 'I'm Like a Bird' is Nelly Furtado.",
         wiki("Like a Prayer (song)"), era="classic", difficulty=2)
c.choice("Which of these is a Michael Jackson song?", "Billie Jean", ["Bennie and the Jets", "Jolene", "Roxanne"],
         "It was on Thriller. When he sang it on TV in 1983, he did the moonwalk in public for the first time.",
         wiki("Billie Jean"), difficulty=1)
c.choice("Which of these songs is by Beyoncé?", "Crazy in Love", ["Crazy", "Crazy for You", "Crazy Train"],
         "It was her first solo number one, in both Britain and America, in 2003. The others are other artists' songs with 'Crazy' in the title.",
         wiki("Crazy in Love"), era="modern", difficulty=2)
c.choice("Which of these is an Adele song?", "Someone like You", ["Someone You Loved", "Somebody That I Used to Know", "Someone to Watch Over Me"],
         "It's from her 2011 album 21. She sang it at the Brit Awards that year, and it went to number one the next week.",
         wiki("Someone like You (Adele song)"), era="modern", difficulty=2)
c.choice("Which of these is an Elvis Presley song?", "Jailhouse Rock", ["Rock Around the Clock", "Johnny B. Goode", "Great Balls of Fire"],
         "The other three are early rock and roll too: Bill Haley, Chuck Berry and Jerry Lee Lewis.",
         wiki("Jailhouse Rock (song)"), era="classic", difficulty=2)
c.choice("Which of these is a Taylor Swift song?", "Shake It Off", ["Shake It Out", "Shake Your Groove Thing", "Shake Ya Tailfeather"],
         "'Shake It Out' is Florence and the Machine. Shake It Off was the first single from Swift's album 1989.",
         wiki("Shake It Off"), era="modern", difficulty=2)
c.choice("Which of these is a Taylor Swift album?", "1989", ["1999", "1984", "1979"],
         "It's named after the year she was born. '1999' is a Prince song, '1984' a Van Halen album and '1979' a Smashing Pumpkins song.",
         wiki("1989 (album)"), era="modern", difficulty=2)
c.choice("Which of these is a Rihanna song?", "Diamonds", ["Diamonds Are a Girl's Best Friend", "Diamonds and Pearls", "Diamond Dogs"],
         "Marilyn Monroe sang 'Diamonds Are a Girl's Best Friend'. 'Diamonds and Pearls' is Prince and 'Diamond Dogs' is David Bowie.",
         wiki("Diamonds (Rihanna song)"), era="modern", difficulty=2)
c.choice("Which of these is an Ed Sheeran song?", "Perfect", ["Perfect Day", "Perfect Illusion", "Perfect Strangers"],
         "'Perfect Day' is Lou Reed and 'Perfect Illusion' is Lady Gaga. Sheeran's Perfect was the UK Christmas number one in 2017.",
         wiki("Perfect (Ed Sheeran song)"), era="modern", difficulty=2)
c.choice("Which of these is a Coldplay song?", "Paradise", ["Paradise City", "Gangsta's Paradise", "Paradise by the Dashboard Light"],
         "'Paradise City' is Guns N' Roses, 'Gangsta's Paradise' is Coolio and the last is Meat Loaf.",
         wiki("Paradise (Coldplay song)"), era="modern", difficulty=2)
c.choice("Which of these is an ABBA song?", "Money, Money, Money", ["Money for Nothing", "Money Talks", "Price Tag"],
         "'Money for Nothing' is Dire Straits, 'Money Talks' is AC/DC and 'Price Tag' is Jessie J.",
         wiki("Money, Money, Money"), era="classic", difficulty=2)
c.choice("Which of these is NOT a Queen song?", "Rock You Like a Hurricane", ["We Will Rock You", "Don't Stop Me Now", "Radio Ga Ga"],
         "Rock You Like a Hurricane is by the German band Scorpions, from 1984.",
         wiki("Rock You Like a Hurricane"), difficulty=2)
c.choice("Which of these is a Whitney Houston song?", "I Wanna Dance with Somebody", ["Dancing on My Own", "Dancing Queen", "Dancing in the Dark"],
         "'Dancing on My Own' is Robyn, 'Dancing Queen' is ABBA and 'Dancing in the Dark' is Bruce Springsteen.",
         wiki("I Wanna Dance with Somebody (Who Loves Me)"), era="classic", difficulty=2)
c.choice("Which of these is a David Bowie song?", "Heroes", ["Hero", "Holding Out for a Hero", "Superheroes"],
         "'Hero' is Mariah Carey, 'Holding Out for a Hero' is Bonnie Tyler and 'Superheroes' is The Script. Bowie recorded Heroes in Berlin in 1977.",
         wiki('"Heroes" (David Bowie song)'), era="classic", difficulty=3)

# Who sang it? ---------------------------------------------------------------------------------------
c.choice("Who sang 'SexyBack' in 2006?", "Justin Timberlake", ["Justin Bieber", "Usher", "Bruno Mars"],
         "It was the first single from his second solo album, and went to number one in America and Britain.",
         wiki("SexyBack"), era="modern", difficulty=1)
c.choice("Who sang 'Total Eclipse of the Heart' (1983)?", "Bonnie Tyler", ["Tina Turner", "Kim Wilde", "Celine Dion"],
         "Tyler is from near Swansea. The song was a number one in both Britain and America.",
         wiki("Total Eclipse of the Heart"), era="classic", difficulty=2)
c.choice("Who sang 'Bat Out of Hell' (1977)?", "Meat Loaf", ["Alice Cooper", "Bruce Springsteen", "Bonnie Tyler"],
         "Jim Steinman wrote it. The album of the same name has sold more than 40 million copies.",
         wiki("Bat Out of Hell"), era="classic", difficulty=2)
c.choice("Which band sang 'Don't Stop Believin''?", "Journey", ["Boston", "Foreigner", "REO Speedwagon"],
         "It came out in 1981. It became a hit all over again after the cast of Glee sang it in 2009.",
         wiki("Don't Stop Believin'"), era="classic", difficulty=2)
c.choice("Which band sang 'Africa' (1982)?", "Toto", ["Chicago", "Kansas", "Journey"],
         "A sneaky one: two of the others are named after places too. Africa was an American number one in 1983.",
         wiki("Africa (Toto song)"), era="classic", difficulty=2)
c.choice("Who sang 'Sweet Caroline' (1969)?", "Neil Diamond", ["Tom Jones", "Barry Manilow", "Elvis Presley"],
         "England football fans made it their anthem during the Euro 2020 tournament.",
         wiki("Sweet Caroline"), era="classic", difficulty=2)
c.choice("Which band had a 1983 number one with 'Red Red Wine', a song first written and sung by Neil Diamond?", "UB40", ["Madness", "The Specials", "Culture Club"],
         "UB40 are from Birmingham. Their name comes from a form people filled in to claim unemployment benefit.",
         wiki("Red Red Wine"), era="classic", difficulty=3)
c.choice("Who sang 'Delilah' (1968), now a favourite of Welsh rugby fans?", "Tom Jones", ["Engelbert Humperdinck", "Cliff Richard", "Neil Diamond"],
         "Tom Jones is from Pontypridd, and was knighted in 2006.",
         wiki("Delilah (Tom Jones song)"), era="classic", difficulty=2)
c.choice("Which band sang 'Common People' (1995)?", "Pulp", ["Blur", "Suede", "Supergrass"],
         "Pulp are from Sheffield, fronted by Jarvis Cocker.",
         wiki("Common People"), difficulty=2)
c.choice("Which band sang 'Bitter Sweet Symphony' (1997)?", "The Verve", ["Oasis", "Radiohead", "Embrace"],
         "It uses a sample of an orchestral version of a Rolling Stones song, and the songwriting credit went to the Stones until 2019.",
         wiki("Bitter Sweet Symphony"), difficulty=2)
c.choice("Which band's first hit was 'Creep' (1992)?", "Radiohead", ["Coldplay", "Muse", "Keane"],
         "Radiohead formed at school in Abingdon, near Oxford.",
         wiki("Creep (Radiohead song)"), difficulty=2)
c.choice("On which Oasis album is 'Wonderwall'?", "(What's the Story) Morning Glory?", ["Definitely Maybe", "Be Here Now", "Dig Out Your Soul"],
         "Definitely Maybe was their first album, in 1994. Morning Glory came out the next year.",
         wiki("(What's the Story) Morning Glory?"), difficulty=3)
c.choice("Which Manchester band sang 'Love Will Tear Us Apart' (1980)?", "Joy Division", ["New Order", "The Smiths", "The Stone Roses"],
         "After their singer Ian Curtis died in 1980, the others carried on as New Order.",
         wiki("Love Will Tear Us Apart"), era="classic", difficulty=3)
c.choice("Who was the singer in The Smiths?", "Morrissey", ["Johnny Marr", "Ian Brown", "Shaun Ryder"],
         "Johnny Marr was their guitarist. Ian Brown sang for the Stone Roses and Shaun Ryder for the Happy Mondays.",
         wiki("The Smiths"), era="classic", difficulty=2)
c.choice("Which band had Sting as its singer?", "The Police", ["Dire Straits", "Simple Minds", "Genesis"],
         "Sting's real name is Gordon Sumner. He got his nickname from a black and yellow striped jumper.",
         wiki("The Police"), era="classic", difficulty=1)
c.choice("Which band did Phil Collins drum and sing for?", "Genesis", ["Yes", "Pink Floyd", "The Police"],
         "Peter Gabriel was Genesis's first singer. Collins took over the microphone when he left in 1975.",
         wiki("Genesis (band)"), era="classic", difficulty=2)
c.choice("Who sang 'Livin' la Vida Loca' (1999)?", "Ricky Martin", ["Enrique Iglesias", "Marc Anthony", "Lou Bega"],
         "Ricky Martin is from Puerto Rico. He started out as a boy in the band Menudo.",
         wiki("Livin' la Vida Loca"), difficulty=2)
c.choice("Who had a worldwide hit with 'Mambo No. 5' in 1999?", "Lou Bega", ["Ricky Martin", "Shaggy", "Pérez Prado"],
         "A tricky one: Pérez Prado wrote and recorded the original, as an instrumental, in 1949. Lou Bega is German.",
         wiki("Mambo No. 5"), difficulty=3)
c.choice("Who sang 'It Wasn't Me' (2000)?", "Shaggy", ["Sean Paul", "Shabba Ranks", "Bob Marley"],
         "It features RikRok and went to number one in Britain and America.",
         wiki("It Wasn't Me"), difficulty=2)
c.choice("Which Jamaican star had hits with 'Get Busy' and 'Temperature'?", "Sean Paul", ["Shaggy", "Beenie Man", "Damian Marley"],
         "Before music, he played water polo for Jamaica's national youth team.",
         wiki("Sean Paul"), era="modern", difficulty=2)
c.choice("Who sang the 1990s dance craze 'Macarena'?", "Los del Río", ["Gipsy Kings", "Las Ketchup", "Los Lobos"],
         "Los del Río are a Spanish duo. Las Ketchup had their own dance hit, 'Aserejé', in 2002.",
         wiki("Macarena (song)"), difficulty=2)
c.choice("Who sang 'Hey Ya!' (2003)?", "OutKast", ["The Black Eyed Peas", "Gnarls Barkley", "N.E.R.D"],
         "OutKast were André 3000 and Big Boi, from Atlanta.",
         wiki("Hey Ya!"), era="modern", difficulty=2)
c.choice("Whose 'Crazy' (2006) was the first UK number one from downloads alone?", "Gnarls Barkley", ["OutKast", "Daft Punk", "The Killers"],
         "Gnarls Barkley is CeeLo Green with the producer Danger Mouse.",
         wiki("Crazy (Gnarls Barkley song)"), era="modern", difficulty=3)
c.choice("Who sang 'Toxic' (2004)?", "Britney Spears", ["Christina Aguilera", "Kylie Minogue", "Jessica Simpson"],
         "It won Britney her first Grammy.",
         wiki("Toxic (song)"), era="modern", difficulty=1)
c.choice("Who sang 'Can't Get You Out of My Head' (2001)?", "Kylie Minogue", ["Dannii Minogue", "Sophie Ellis-Bextor", "Madonna"],
         "It went to number one in about 40 countries. Dannii Minogue is Kylie's younger sister.",
         wiki("Can't Get You Out of My Head"), difficulty=1)
c.choice("Whose 2001 hit 'Murder on the Dancefloor' became a hit again after the film Saltburn?", "Sophie Ellis-Bextor", ["Kylie Minogue", "Dua Lipa", "Jessie Ware"],
         "The song plays at the end of the 2023 film, and climbed back into the top 10 more than 20 years after it first came out.",
         wiki("Murder on the Dancefloor"), difficulty=2)
c.choice("Whose 1985 song 'Running Up That Hill' became a UK number one in 2022, after Stranger Things?", "Kate Bush", ["Annie Lennox", "Stevie Nicks", "Siouxsie Sioux"],
         "It reached number one 37 years after it first came out. Kate Bush was 19 when 'Wuthering Heights' made her famous.",
         wiki("Running Up That Hill"), difficulty=2)
c.choice("Who sang 'Sweet Dreams (Are Made of This)' (1983)?", "Eurythmics", ["Yazoo", "Soft Cell", "Pet Shop Boys"],
         "Eurythmics were Annie Lennox and Dave Stewart.",
         wiki("Sweet Dreams (Are Made of This)"), era="classic", difficulty=2)
c.choice("Which band had the 1981 Christmas number one 'Don't You Want Me'?", "The Human League", ["Duran Duran", "Depeche Mode", "Spandau Ballet"],
         "The Human League are from Sheffield. The song topped the charts in America too.",
         wiki("Don't You Want Me"), era="classic", difficulty=3)
c.choice("Which band sang 'True' and 'Gold'?", "Spandau Ballet", ["Duran Duran", "ABC", "Tears for Fears"],
         "Spandau Ballet came from Islington in London, and were rivals of Duran Duran.",
         wiki("Spandau Ballet"), era="classic", difficulty=2)
c.choice("Which band sang 'Hungry Like the Wolf' and 'Rio'?", "Duran Duran", ["Spandau Ballet", "ABC", "A Flock of Seagulls"],
         "Duran Duran formed in Birmingham. They also sang the Bond theme 'A View to a Kill'.",
         wiki("Duran Duran"), era="classic", difficulty=2)
c.choice("Who sang 'Everybody Wants to Rule the World' (1985)?", "Tears for Fears", ["Simple Minds", "a-ha", "Duran Duran"],
         "Tears for Fears are Roland Orzabal and Curt Smith, from Bath.",
         wiki("Everybody Wants to Rule the World"), era="classic", difficulty=2)
c.choice("Which Norwegian band sang 'Take On Me'?", "a-ha", ["Europe", "Roxette", "Ace of Base"],
         "Its pencil-sketch music video won six MTV awards. a-ha's singer, Morten Harket, later sang the Bond theme The Living Daylights.",
         wiki("Take On Me"), era="classic", difficulty=2)
c.choice("Which Swedish band sang 'The Final Countdown' (1986)?", "Europe", ["a-ha", "Roxette", "Def Leppard"],
         "It went to number one in 25 countries, and is still played at sports grounds before big moments.",
         wiki("The Final Countdown (song)"), era="classic", difficulty=2)
c.choice("Who sang 'Wake Me Up Before You Go-Go' (1984)?", "Wham!", ["Culture Club", "Duran Duran", "Bros"],
         "Wham! were George Michael and Andrew Ridgeley, who met at school in Bushey, Hertfordshire.",
         wiki("Wake Me Up Before You Go-Go"), era="classic", difficulty=1)
c.yes_no("Did Wham!'s 'Last Christmas' finally reach number one in the UK, decades after it came out?", True,
         "It came out in 1984 and finally got to number one on New Year's Day 2021, then became Christmas number one in 2023.",
         wiki("Last Christmas"), difficulty=2)
c.choice("Who sang 'Karma Chameleon' (1983)?", "Culture Club", ["Wham!", "Frankie Goes to Hollywood", "Bronski Beat"],
         "Culture Club's singer was Boy George. It was a number one in Britain and America.",
         wiki("Karma Chameleon"), era="classic", difficulty=2)
c.choice("Who sang 'Walk Like an Egyptian' (1986)?", "The Bangles", ["The Go-Go's", "Bananarama", "Blondie"],
         "The Bangles were an all-female band from Los Angeles.",
         wiki("Walk Like an Egyptian"), era="classic", difficulty=2)
c.choice("Which band sang 'Heart of Glass' (1979)?", "Blondie", ["The Pretenders", "The Bangles", "Eurythmics"],
         "Debbie Harry was Blondie's singer, but Blondie is the band's name, not hers.",
         wiki("Heart of Glass (song)"), era="classic", difficulty=2)
c.choice("Who sang 'Piano Man' (1973)?", "Billy Joel", ["Elton John", "Barry Manilow", "Neil Diamond"],
         "It's about Joel's time playing piano in a bar in Los Angeles. Elton John's 'Rocket Man' came out the year before.",
         wiki("Piano Man (song)"), era="classic", difficulty=2)
c.choice("Westlife had a number one with 'Uptown Girl' in 2001. Who sang it first?", "Billy Joel", ["Elton John", "Bruce Springsteen", "Frankie Valli"],
         "Billy Joel's version came out in 1983, with a video starring the model Christie Brinkley.",
         wiki("Uptown Girl"), difficulty=2)
c.choice("Who sang 'Born in the U.S.A.' (1984)?", "Bruce Springsteen", ["Bob Seger", "Tom Petty", "John Mellencamp"],
         "Springsteen's nickname is The Boss. He comes from New Jersey.",
         wiki("Born in the U.S.A. (song)"), era="classic", difficulty=2)
c.choice("Which band sang 'Hotel California' (1976)?", "Eagles", ["Fleetwood Mac", "Lynyrd Skynyrd", "The Doobie Brothers"],
         "Eagles' Their Greatest Hits 1971 to 1975 is one of the best-selling albums ever in America.",
         wiki("Hotel California (song)"), era="classic", difficulty=2)
c.choice("Which band recorded 'Highway to Hell' (1979)?", "AC/DC", ["Guns N' Roses", "Metallica", "Iron Maiden"],
         "AC/DC are from Australia, but the brothers Angus and Malcolm Young were born in Glasgow.",
         wiki("Highway to Hell (song)"), era="classic", difficulty=2)
c.choice("Which band sang 'Sweet Child o' Mine' (1987)?", "Guns N' Roses", ["Bon Jovi", "Aerosmith", "Def Leppard"],
         "It was the band's only American number one. Slash's guitar riff began as a warm-up exercise.",
         wiki("Sweet Child o' Mine"), era="classic", difficulty=2)
c.choice("Which band sang 'Smoke on the Water' (1972)?", "Deep Purple", ["Black Sabbath", "Led Zeppelin", "Uriah Heep"],
         "It's about a real fire at a casino in Montreux, Switzerland, during a Frank Zappa concert in 1971.",
         wiki("Smoke on the Water"), era="classic", difficulty=2)
c.choice("Which band did Ozzy Osbourne sing for?", "Black Sabbath", ["Iron Maiden", "Judas Priest", "Motörhead"],
         "Black Sabbath formed in Birmingham in 1968, and are often called the first heavy metal band.",
         wiki("Black Sabbath"), era="classic", difficulty=2)
c.choice("Which Birmingham band sang 'Mr. Blue Sky' (1977)?", "Electric Light Orchestra", ["Supertramp", "10cc", "The Moody Blues"],
         "ELO were led by Jeff Lynne, who mixed rock with violins and cellos.",
         wiki("Mr. Blue Sky"), era="classic", difficulty=2)
c.choice("Who sang 'September' (1978)?", "Earth, Wind & Fire", ["Kool & the Gang", "Chic", "The Commodores"],
         "Fans celebrate '21st night of September' day every year because the date is in the song.",
         wiki("September (Earth, Wind & Fire song)"), era="classic", difficulty=2)
c.choice("Who sang 'I Will Survive' (1978)?", "Gloria Gaynor", ["Donna Summer", "Diana Ross", "Chaka Khan"],
         "It began as the B-side of another song, until DJs started playing it in clubs.",
         wiki("I Will Survive"), era="classic", difficulty=2)
c.choice("Which singer, known as the Queen of Disco, sang 'I Feel Love' and 'Hot Stuff'?", "Donna Summer", ["Gloria Gaynor", "Diana Ross", "Grace Jones"],
         "'I Feel Love' (1977) was one of the first hits made almost entirely with synthesizers.",
         wiki("Donna Summer"), era="classic", difficulty=2)
c.choice("Who sang 'Y.M.C.A.' (1978)?", "Village People", ["Bee Gees", "KC and the Sunshine Band", "Boney M."],
         "The dance spells out the letters with your arms.",
         wiki("Y.M.C.A. (song)"), era="classic", difficulty=1)
c.choice("Which group had hits with 'Rivers of Babylon' and 'Rasputin'?", "Boney M.", ["ABBA", "Village People", "Baccara"],
         "Boney M. were put together in West Germany by the producer Frank Farian, with singers from the Caribbean.",
         wiki("Boney M."), era="classic", difficulty=2)
c.choice("Who sang 'Superstition' (1972)?", "Stevie Wonder", ["Ray Charles", "Marvin Gaye", "Al Green"],
         "Wonder wrote it and played almost every instrument on it himself.",
         wiki("Superstition (song)"), era="classic", difficulty=2)
c.choice("Who sang 'What's Going On' (1971)?", "Marvin Gaye", ["Stevie Wonder", "Smokey Robinson", "Curtis Mayfield"],
         "Motown's boss, Berry Gordy, didn't want to release it at first. It went on to sell millions.",
         wiki("What's Going On (Marvin Gaye song)"), era="classic", difficulty=3)
c.choice("Who sang 'Stand by Me' (1961)?", "Ben E. King", ["Sam Cooke", "Otis Redding", "Smokey Robinson"],
         "It went back into the charts in 1986 after the film Stand by Me came out.",
         wiki("Stand by Me (Ben E. King song)"), era="classic", difficulty=3)
c.choice("Who sang 'What a Wonderful World' (1967)?", "Louis Armstrong", ["Nat King Cole", "Ray Charles", "Frank Sinatra"],
         "It was a number one in Britain in 1968, when Armstrong was 66.",
         wiki("What a Wonderful World"), era="classic", difficulty=1)
c.choice("Which singer was nicknamed 'Ol' Blue Eyes'?", "Frank Sinatra", ["Dean Martin", "Bing Crosby", "Sammy Davis Jr."],
         "His signature song, 'My Way', is based on a French song, 'Comme d'habitude', with English words by Paul Anka.",
         wiki("Frank Sinatra"), era="classic", difficulty=2)
c.choice("Who sang 'Jolene' (1973)?", "Dolly Parton", ["Loretta Lynn", "Tammy Wynette", "Patsy Cline"],
         "Parton has said the song was inspired by a red-haired bank clerk who flirted with her husband.",
         wiki("Jolene (song)"), era="classic", difficulty=1)
c.choice("Who sang 'Stand by Your Man' (1968)?", "Tammy Wynette", ["Dolly Parton", "Loretta Lynn", "Patsy Cline"],
         "Wynette wrote it with her producer in about 15 minutes.",
         wiki("Stand by Your Man"), era="classic", difficulty=3)
c.choice("Which country star is Miley Cyrus's godmother?", "Dolly Parton", ["Reba McEntire", "Shania Twain", "Cher"],
         "Miley's dad, Billy Ray Cyrus, sang 'Achy Breaky Heart'.",
         wiki("Miley Cyrus"), difficulty=2)
c.choice("Who sang 'Old Town Road' (2019) with Billy Ray Cyrus?", "Lil Nas X", ["Post Malone", "Lil Wayne", "Kid Cudi"],
         "It spent 19 weeks at number one in America, a record at the time.",
         wiki("Old Town Road"), era="modern", difficulty=2)
c.choice("Who sang 'Flowers' (2023)?", "Miley Cyrus", ["Taylor Swift", "Olivia Rodrigo", "Dua Lipa"],
         "It won her first Grammy, for Record of the Year.",
         wiki("Flowers (Miley Cyrus song)"), era="modern", difficulty=1)
c.choice("Who sang 'drivers license' (2021)?", "Olivia Rodrigo", ["Billie Eilish", "Sabrina Carpenter", "Gracie Abrams"],
         "Rodrigo started out on the Disney+ series High School Musical: The Musical: The Series.",
         wiki("Drivers License"), era="modern", difficulty=1)
c.choice("Who sang 'Espresso' (2024)?", "Sabrina Carpenter", ["Olivia Rodrigo", "Chappell Roan", "Dua Lipa"],
         "Carpenter started out on the Disney Channel, in Girl Meets World.",
         wiki("Espresso (song)"), era="modern", difficulty=1)
c.choice("Who sang 'As It Was' (2022)?", "Harry Styles", ["Niall Horan", "Louis Tomlinson", "Zayn"],
         "It topped the charts in Britain and America. All four were in One Direction.",
         wiki("As It Was"), era="modern", difficulty=1)
c.choice("Who sang 'Someone You Loved', the UK's biggest-selling single of 2019?", "Lewis Capaldi", ["Tom Walker", "Calum Scott", "James Arthur"],
         "Capaldi is from Scotland. He made a much-loved comeback at Glastonbury in 2025.",
         wiki("Someone You Loved"), era="modern", difficulty=2)
c.choice("Which X Factor winner had a hit with 'Say You Won't Let Go' (2016)?", "James Arthur", ["Matt Cardle", "Olly Murs", "Ben Haenow"],
         "Arthur won The X Factor in 2012. Olly Murs never won it: he came second in 2009.",
         wiki("Say You Won't Let Go"), era="modern", difficulty=2)
c.choice("Which X Factor winner had the 2008 Christmas number one with 'Hallelujah'?", "Alexandra Burke", ["Leona Lewis", "Matt Cardle", "Jedward"],
         "Leonard Cohen wrote the song. Jeff Buckley's version climbed to number two the same week.",
         wiki("Alexandra Burke"), era="modern", difficulty=3)
c.choice("Which band beat The X Factor winner to Christmas number one in 2009, thanks to a Facebook campaign?", "Rage Against the Machine", ["Arctic Monkeys", "Muse", "Green Day"],
         "Their 'Killing in the Name' came out in 1992. The X Factor had produced the Christmas number one for four years running.",
         wiki("Killing in the Name"), era="modern", difficulty=3)
c.choice("Which singer wore a dress made of raw meat to the 2010 MTV Video Music Awards?", "Lady Gaga", ["Katy Perry", "Nicki Minaj", "Björk"],
         "Björk had her own famous outfit, a swan dress, at the 2001 Oscars.",
         wiki("Meat dress of Lady Gaga"), era="modern", difficulty=2)
c.choice("Who sang 'Firework' and 'Roar'?", "Katy Perry", ["Kesha", "Lady Gaga", "P!nk"],
         "Perry started out singing gospel music as a teenager.",
         wiki("Katy Perry"), era="modern", difficulty=1)
c.choice("Which singer had a 1984 number one called 'Hello', 31 years before Adele's?", "Lionel Richie", ["Stevie Wonder", "Billy Ocean", "Luther Vandross"],
         "Its video shows a blind art student making a clay sculpture of his head.",
         wiki("Hello (Lionel Richie song)"), era="classic", difficulty=2)
c.choice("Which band was Lionel Richie in before he went solo?", "The Commodores", ["Earth, Wind & Fire", "Kool & the Gang", "The Temptations"],
         "He wrote their hits 'Three Times a Lady' and 'Easy'.",
         wiki("Commodores"), era="classic", difficulty=2)
c.choice("Who sang 'I Gotta Feeling' (2009)?", "The Black Eyed Peas", ["LMFAO", "Pitbull", "Flo Rida"],
         "It spent 14 weeks at number one in America.",
         wiki("I Gotta Feeling"), era="modern", difficulty=2)
c.choice("Who sang 'Happy' (2013), from Despicable Me 2?", "Pharrell Williams", ["Bruno Mars", "Justin Timberlake", "will.i.am"],
         "Its music video was 24 hours long. Pharrell later became the men's creative director at Louis Vuitton.",
         wiki("Happy (Pharrell Williams song)"), era="modern", difficulty=1)
c.choice("Who sang 'Hips Don't Lie' (2006) with Wyclef Jean?", "Shakira", ["Jennifer Lopez", "Rihanna", "Camila Cabello"],
         "It was a number one in about 55 countries.",
         wiki("Hips Don't Lie"), era="modern", difficulty=1)
c.choice("Which band had a 1982 hit with 'Our House'?", "Madness", ["UB40", "The Specials", "Squeeze"],
         "Madness were a ska band from Camden in London, nicknamed the Nutty Boys.",
         wiki("Our House (Madness song)"), era="classic", difficulty=2)
c.choice("Which band's 'Seven Nation Army' riff is chanted by football crowds?", "The White Stripes", ["The Black Keys", "The Strokes", "Kings of Leon"],
         "The White Stripes were just two people, Jack and Meg White, from Detroit.",
         wiki("Seven Nation Army"), era="modern", difficulty=2)
c.choice("Which Sheffield band's 2006 album was then the UK's fastest-selling debut ever?", "Arctic Monkeys", ["Kaiser Chiefs", "The Kooks", "Bloc Party"],
         "The album was 'Whatever People Say I Am, That's What I'm Not'. The band first became known through fans sharing their songs online.",
         wiki("Whatever People Say I Am, That's What I'm Not"), era="modern", difficulty=2)
c.choice("Which band sang 'Chasing Cars' (2006)?", "Snow Patrol", ["Keane", "The Fray", "Travis"],
         "Snow Patrol formed at the University of Dundee. Their singer, Gary Lightbody, is from Northern Ireland.",
         wiki("Chasing Cars"), era="modern", difficulty=2)
c.choice("Which DJ from Dumfries had hits with 'Summer' and 'One Kiss'?", "Calvin Harris", ["David Guetta", "Avicii", "Martin Garrix"],
         "'One Kiss', sung with Dua Lipa, was the UK's biggest-selling single of 2018.",
         wiki("Calvin Harris"), era="modern", difficulty=2)
c.choice("Who sang 'Ice Ice Baby' (1990)?", "Vanilla Ice", ["MC Hammer", "Snow", "Will Smith"],
         "Its bass line comes from 'Under Pressure' by Queen and David Bowie.",
         wiki("Ice Ice Baby"), era="classic", difficulty=2)
c.choice("Who sang 'U Can't Touch This' (1990)?", "MC Hammer", ["Vanilla Ice", "Coolio", "Kris Kross"],
         "It's built on the music of Rick James's 'Super Freak'. Hammer was famous for his baggy 'Hammer pants'.",
         wiki("U Can't Touch This"), era="classic", difficulty=2)
c.choice("Which rapper won an Oscar for 'Lose Yourself', from the film 8 Mile?", "Eminem", ["Jay-Z", "50 Cent", "Dr. Dre"],
         "It was the first rap song to win the Oscar for Best Original Song, in 2003.",
         wiki("Lose Yourself"), era="modern", difficulty=2)
c.choice("Which rapper is married to Beyoncé?", "Jay-Z", ["Kanye West", "Drake", "Pharrell Williams"],
         "They married in 2008 and have released an album together, as The Carters.",
         wiki("Jay-Z"), era="modern", difficulty=1)
c.choice("Which Toronto rapper had a hit with 'Hotline Bling'?", "Drake", ["The Weeknd", "Justin Bieber", "Shawn Mendes"],
         "All four are Canadian. Before music, Drake was an actor in the teen drama Degrassi.",
         wiki("Drake (musician)"), era="modern", difficulty=2)
c.choice("Which singer was discovered on YouTube as a boy from Stratford, Ontario?", "Justin Bieber", ["Shawn Mendes", "Drake", "The Weeknd"],
         "Usher helped sign him to a record deal when he was 14.",
         wiki("Justin Bieber"), era="modern", difficulty=2)
c.choice("Which BLACKPINK singer had a 2024 hit with Bruno Mars called 'APT.'?", "Rosé", ["Jennie", "Lisa", "Jisoo"],
         "All four are in BLACKPINK. The title comes from a Korean party game.",
         wiki("APT. (song)"), era="modern", difficulty=2)
c.choice("Who sang 'Die with a Smile' (2024) with Bruno Mars?", "Lady Gaga", ["Rosé", "Dua Lipa", "Ariana Grande"],
         "Bruno Mars had two huge duets out at once, this one and 'APT.' with Rosé.",
         wiki("Die with a Smile"), era="modern", difficulty=2)
c.choice("Which made-up girl group sings 'Golden' in the Netflix film KPop Demon Hunters (2025)?", "HUNTR/X", ["Saja Boys", "BLACKPINK", "TWICE"],
         "The Saja Boys are the rival boy band in the film. 'Golden' became a real number one in America and Britain.",
         wiki("Golden (Huntrix song)"), era="modern", difficulty=2)
c.choice("Who writes and produces Billie Eilish's songs with her?", "Her brother, Finneas", ["Her dad", "Mark Ronson", "Max Martin"],
         "They made her first album in his small bedroom studio in Los Angeles.",
         wiki("Finneas O'Connell"), era="modern", difficulty=2)
c.choice("What do Beyoncé's fans call themselves?", "The BeyHive", ["The Navy", "Little Monsters", "Barbz"],
         "Rihanna's fans are the Navy, Lady Gaga's are Little Monsters and Nicki Minaj's are the Barbz.",
         wiki("Beyoncé"), era="modern", difficulty=2)
c.choice("Which star's beauty brand is called Fenty Beauty?", "Rihanna", ["Beyoncé", "Kylie Jenner", "Selena Gomez"],
         "Fenty is Rihanna's real surname. Kylie Jenner has Kylie Cosmetics and Selena Gomez has Rare Beauty.",
         wiki("Fenty Beauty"), era="modern", difficulty=2)

# Covers and the stories behind them ------------------------------------------------------------------
c.choice("'Valerie', a hit for Amy Winehouse and Mark Ronson, was first recorded by which Liverpool band?", "The Zutons", ["The Coral", "The La's", "The Farm"],
         "The Zutons released it in 2006. Winehouse and Ronson's version came out the next year.",
         wiki("Valerie (The Zutons song)"), era="modern", difficulty=3)
c.choice("Which soul singer recorded '(Sittin' On) The Dock of the Bay' days before he died in 1967?", "Otis Redding", ["Sam Cooke", "Wilson Pickett", "Marvin Gaye"],
         "It became the first song to reach number one in America after the singer had died.",
         wiki("(Sittin' On) The Dock of the Bay"), era="classic", difficulty=3)
c.choice("Soft Cell had a huge hit with 'Tainted Love' in 1981. Who recorded it first, in 1964?", "Gloria Jones", ["Diana Ross", "Dusty Springfield", "Martha Reeves"],
         "Gloria Jones's original was a favourite in Northern Soul clubs. She was later Marc Bolan's partner.",
         wiki("Tainted Love"), era="classic", difficulty=3)
c.choice("Who first had a hit with 'Girls Just Want to Have Fun', in 1983?", "Cyndi Lauper", ["Madonna", "Debbie Harry", "Pat Benatar"],
         "Lauper rewrote the words of a song by Robert Hazard. Its video helped make her a star on MTV.",
         wiki("Girls Just Want to Have Fun"), era="classic", difficulty=2)
c.choice("Johnny Cash had a late hit with a cover of 'Hurt' (2002). Which band's song was it?", "Nine Inch Nails", ["Depeche Mode", "U2", "Soundgarden"],
         "Trent Reznor of Nine Inch Nails wrote it. He said that after seeing Cash's video, the song wasn't his any more.",
         wiki("Hurt (Nine Inch Nails song)"), difficulty=3)
c.choice("Who had five UK Christmas number ones in a row, from 2019 to 2023, with charity songs about sausage rolls?", "LadBaby", ["Ed Sheeran", "Mariah Carey", "The Beatles"],
         "Before LadBaby, the record was three in a row, shared by the Beatles and the Spice Girls.",
         wiki("LadBaby"), era="modern", difficulty=2)

# Albums and the Beatles ----------------------------------------------------------------------------
c.choice("Which album cover shows a baby swimming towards a dollar bill?", "Nevermind, by Nirvana", ["Ten, by Pearl Jam", "Dookie, by Green Day", "In Utero, by Nirvana"],
         "Nevermind (1991) includes 'Smells Like Teen Spirit'.",
         wiki("Nevermind"), difficulty=2)
c.choice("Which Beatles album cover shows the band in front of a crowd of famous faces?", "Sgt. Pepper's Lonely Hearts Club Band", ["Abbey Road", "Revolver", "The White Album"],
         "The artist Peter Blake designed it with Jann Haworth. The White Album's cover is plain white.",
         wiki("Sgt. Pepper's Lonely Hearts Club Band"), era="classic", difficulty=2)
c.choice("Which of these Michael Jackson albums came out first?", "Off the Wall", ["Thriller", "Bad", "Dangerous"],
         "Off the Wall (1979), then Thriller (1982), Bad (1987) and Dangerous (1991).",
         wiki("Off the Wall"), era="classic", difficulty=3)
c.choice("Who was the youngest Beatle?", "George Harrison", ["Paul McCartney", "John Lennon", "Ringo Starr"],
         "Harrison was born in 1943. He was sent home from Hamburg in 1960 for being too young to play in the clubs there.",
         wiki("George Harrison"), era="classic", difficulty=3)
c.higher_lower("Did the Beatles release 'Hey Jude' before or after the first Moon landing in July 1969?", True,
               "Before: it came out in August 1968, almost a year earlier.",
               wiki("Hey Jude"), labels=("Before", "After"), era="classic", difficulty=3)
c.higher_lower("The Beatles had 17 UK number one singles. Did Elvis Presley have more or fewer?", True,
               "More: Elvis has 21, the most of any act in Britain.",
               wiki("List of artists with the most UK singles chart number ones"), labels=("More", "Fewer"), difficulty=3, as_of="2026")
c.higher_lower("Did Taylor Swift release her first album before or after 2010?", True,
               "Before: her first album, Taylor Swift, came out in 2006, when she was 16.",
               wiki("Taylor Swift (album)"), labels=("Before", "After"), era="modern", difficulty=2)
c.higher_lower("Michael Jackson's Thriller came out in 1982. Did Prince's Purple Rain come out before or after it?", False,
               "After: Purple Rain came out in 1984, with a film of the same name.",
               wiki("Purple Rain (album)"), labels=("Before", "After"), era="classic", difficulty=3)
c.choice("Which Taylor Swift album came out in October 2025?", "The Life of a Showgirl", ["The Tortured Poets Department", "Midnights", "Evermore"],
         "The Tortured Poets Department came out in 2024 and Midnights in 2022.",
         wiki("The Life of a Showgirl"), era="modern", difficulty=2)

# Eurovision ----------------------------------------------------------------------------------------
c.choice("Which countries have won Eurovision the most times?", "Ireland and Sweden, seven each", ["Sweden alone, with eight", "Ireland alone, with eight", "The UK and France, five each"],
         "Ireland won three years in a row, from 1992 to 1994. Sweden's seventh win was Loreen's 'Tattoo' in 2023.",
         wiki("List of Eurovision Song Contest winners"), difficulty=3, as_of="2026")
c.choice("Which Irish singer won Ireland's first Eurovision, in 1970, with 'All Kinds of Everything'?", "Dana", ["Linda Martin", "Mary Black", "Sinéad O'Connor"],
         "Dana was 18. Ireland went on to win seven times, level with Sweden for the most wins.",
         wiki("Dana (Irish singer)"), era="classic", difficulty=3)
c.choice("Which UK group won Eurovision in 1981, famously pulling off their skirts on stage?", "Bucks Fizz", ["Brotherhood of Man", "Sandie Shaw", "Katrina and the Waves"],
         "The song was 'Making Your Mind Up'. Brotherhood of Man won for the UK in 1976 and Sandie Shaw in 1967.",
         wiki("Bucks Fizz"), era="classic", difficulty=2)

# Classical, instruments and the stage --------------------------------------------------------------
c.choice("Which composer wrote The Planets, including 'Mars' and 'Jupiter'?", "Gustav Holst", ["Edward Elgar", "Ralph Vaughan Williams", "Benjamin Britten"],
         "Holst was born in Cheltenham. He wrote The Planets during the First World War.",
         wiki("The Planets"), difficulty=3)
c.choice("Which English composer wrote the march heard as 'Land of Hope and Glory' at the Last Night of the Proms?", "Edward Elgar", ["Gustav Holst", "George Frideric Handel", "Henry Purcell"],
         "It's his Pomp and Circumstance March No. 1, from 1901. Elgar appeared on the £20 note from 1999 to 2010.",
         wiki("Pomp and Circumstance Marches"), difficulty=2)
c.choice("Which composer wrote Messiah, with its famous 'Hallelujah' chorus?", "George Frideric Handel", ["Johann Sebastian Bach", "Joseph Haydn", "Wolfgang Amadeus Mozart"],
         "Handel was German but lived in London. Jimi Hendrix later lived in the house next door to his on Brook Street.",
         wiki("Messiah (Handel)"), difficulty=2)
c.choice("Which tenor's 'Nessun dorma' became the BBC's theme for the 1990 World Cup?", "Luciano Pavarotti", ["Plácido Domingo", "José Carreras", "Andrea Bocelli"],
         "Pavarotti, Domingo and Carreras sang together as the Three Tenors the night before the 1990 final, in Rome.",
         wiki("Nessun dorma"), difficulty=2)
c.choice("Which composer wrote the operas Madama Butterfly and Turandot?", "Giacomo Puccini", ["Giuseppe Verdi", "Gioachino Rossini", "Antonio Vivaldi"],
         "Puccini died before finishing Turandot, which includes 'Nessun dorma'.",
         wiki("Giacomo Puccini"), difficulty=3)
c.choice("Whose ballet The Rite of Spring caused uproar in the audience at its first night in Paris in 1913?", "Igor Stravinsky", ["Claude Debussy", "Maurice Ravel", "Sergei Prokofiev"],
         "The music and dancing were so new and wild that people shouted, whistled and argued during the performance.",
         wiki("The Rite of Spring"), era="classic", difficulty=3)
c.choice("In Prokofiev's Peter and the Wolf, which instrument plays the bird?", "The flute", ["The oboe", "The clarinet", "The bassoon"],
         "Every character has its own instrument: the oboe is the duck, the clarinet the cat and the bassoon the grandfather.",
         wiki("Peter and the Wolf"), difficulty=3)
c.choice("How many symphonies did Beethoven finish?", "9", ["7", "12", "41"],
         "Mozart's last symphony was number 41, the 'Jupiter'. Beethoven's Ninth ends with 'Ode to Joy'.",
         wiki("Symphony No. 9 (Beethoven)"), difficulty=2)
c.choice("Which composer wrote the piano piece 'Clair de lune'?", "Claude Debussy", ["Erik Satie", "Frédéric Chopin", "Maurice Ravel"],
         "The name means moonlight. It's the third part of his Suite bergamasque.",
         wiki("Suite bergamasque"), difficulty=3)
c.choice("Which composer, who wrote mostly for the piano, has his heart buried in Warsaw and his body in Paris?", "Frédéric Chopin", ["Franz Liszt", "Sergei Rachmaninoff", "Robert Schumann"],
         "Chopin left Poland at 20 and never went back. His sister smuggled his heart home after he died in 1849.",
         wiki("Frédéric Chopin"), difficulty=3)
c.choice("On a piece of music, what does 'piano' tell you to do?", "Play softly", ["Play loudly", "Play slowly", "Play quickly"],
         "Forte means loud. The instrument's full name, pianoforte, means 'soft-loud', because it can play both.",
         wiki("Dynamics (music)"), difficulty=2)
c.choice("Which is the biggest instrument in an orchestra's string section?", "The double bass", ["The cello", "The viola", "The harp"],
         "It stands about 1.8 metres tall, so players stand up or sit on a high stool.",
         wiki("Double bass"), difficulty=1)
c.choice("Which instrument does Yo-Yo Ma play?", "The cello", ["The violin", "The piano", "The double bass"],
         "He was born in Paris to Chinese parents, and played for President Kennedy when he was seven.",
         wiki("Yo-Yo Ma"), difficulty=2)
c.choice("Which country does the didgeridoo come from?", "Australia", ["New Zealand", "South Africa", "Papua New Guinea"],
         "Aboriginal Australians make them from eucalyptus branches that termites have hollowed out.",
         wiki("Didgeridoo"), difficulty=1)
c.choice("Which country does the sitar come from?", "India", ["Japan", "Turkey", "Iran"],
         "Ravi Shankar taught George Harrison to play it, and Harrison used it on Beatles songs.",
         wiki("Sitar"), difficulty=1)
c.choice("Which musical tells the story of an American founding father through hip-hop?", "Hamilton", ["In the Heights", "Rent", "Jersey Boys"],
         "Lin-Manuel Miranda wrote it and played Alexander Hamilton. He wrote In the Heights too.",
         wiki("Hamilton (musical)"), era="modern", difficulty=1)
c.choice("Which musical has the songs 'Defying Gravity' and 'Popular'?", "Wicked", ["Matilda", "Hairspray", "The Wizard of Oz"],
         "It tells the story of the witches of Oz. The two-part film starred Cynthia Erivo and Ariana Grande.",
         wiki("Wicked (musical)"), era="modern", difficulty=1)
c.choice("Which musical, based on a Roald Dahl book, is about a girl with special powers who loves reading?", "Matilda", ["Annie", "Wicked", "Mary Poppins"],
         "The comedian Tim Minchin wrote its songs. It began with the Royal Shakespeare Company in 2010.",
         wiki("Matilda the Musical"), era="modern", difficulty=1)
c.choice("Which musical turns the six wives of Henry VIII into a pop group?", "SIX", ["Wives", "Tudor!", "Divorced, Beheaded, Died"],
         "Two Cambridge students wrote it for the Edinburgh Fringe in 2017. It's now on in the West End and on Broadway.",
         wiki("Six (musical)"), era="modern", difficulty=1)
