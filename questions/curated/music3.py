"""More music: bands, hit songs, singers, composers and the stories behind them."""

from . import Category, wiki

c = Category("music", prefix="music3")
SUPER_BOWL_LX = ("JamBase: Bad Bunny's Super Bowl LX halftime show", "https://www.jambase.com/article/bad-bunny-super-bowl-lx-halftime-show-video")

# Bands ---------------------------------------------------------------------------------------------
c.choice("Which Beatle played bass guitar, left-handed?", "Paul McCartney", ["John Lennon", "George Harrison", "Ringo Starr"],
         "McCartney taught himself by turning a right-handed guitar upside down and restringing it.",
         wiki("Paul McCartney"), difficulty=2)
c.choice("Which Beatle wrote and sang 'Imagine', released in 1971?", "John Lennon", ["Paul McCartney", "George Harrison", "Ringo Starr"],
         "It came out the year after the Beatles split up.",
         wiki("Imagine (John Lennon song)"), difficulty=1)
c.choice("In which Liverpool club did the Beatles play nearly 300 times before they were famous?", "The Cavern Club", ["The Marquee", "Ronnie Scott's", "The Hacienda"],
         "It was a cellar club on Mathew Street. Their manager, Brian Epstein, first saw them there in 1961.",
         wiki("The Cavern Club"), era="classic", difficulty=2)
c.choice("Which band's 20-minute set is often called the greatest live performance ever, at Live Aid in 1985?", "Queen", ["U2", "The Who", "Status Quo"],
         "Freddie Mercury had 72,000 people at Wembley singing and clapping along.",
         wiki("Queen at Live Aid"), difficulty=2)
c.yes_no("Does Queen's guitarist Brian May have a PhD in astrophysics?", True,
         "He started it in the 1970s, left to tour with Queen, and finished it in 2007, more than 30 years later.",
         wiki("Brian May"), difficulty=2)
c.choice("Where does the name ABBA come from?", "The first letters of the members' names", ["A Swedish word for 'song'", "A fish company in Gothenburg", "Their first record label"],
         "Agnetha, Björn, Benny and Anni-Frid. A Swedish fish-canning company was already called Abba, and agreed to share the name.",
         wiki("ABBA"), difficulty=2)
c.choice("Which ABBA song begins 'You can dance, you can jive'?", "Dancing Queen", ["Mamma Mia", "Waterloo", "Super Trouper"],
         "Dancing Queen was ABBA's only number one in the United States.",
         wiki("Dancing Queen"), difficulty=2)
c.choice("Which Pink Floyd album cover shows a beam of light passing through a prism?", "The Dark Side of the Moon", ["The Wall", "Wish You Were Here", "Animals"],
         "It has spent more than 900 weeks in the US album charts, more than 17 years in all.",
         wiki("The Dark Side of the Moon"), era="classic", difficulty=2)
c.choice("Which rock band recorded 'Stairway to Heaven' in 1971?", "Led Zeppelin", ["Deep Purple", "Black Sabbath", "The Who"],
         "It was never released as a single in Britain, but became one of the most-played rock songs on the radio.",
         wiki("Led Zeppelin"), era="classic", difficulty=2)
c.choice("Which band, led by Kurt Cobain, had a huge hit with 'Smells Like Teen Spirit' in 1991?", "Nirvana", ["Pearl Jam", "Foo Fighters", "Soundgarden"],
         "Nirvana came from near Seattle. Their drummer, Dave Grohl, later started the Foo Fighters.",
         wiki("Nirvana (band)"), era="classic", difficulty=2)
c.choice("Which Fleetwood Mac album, released in 1977, is one of the best-selling albums of all time?", "Rumours", ["Tusk", "Tango in the Night", "Mirage"],
         "It was written while the band's members were going through break-ups with each other.",
         wiki("Rumours (album)"), era="classic", difficulty=3)
c.choice("What is the famous logo of the Rolling Stones?", "A mouth with a tongue sticking out", ["A rolling stone", "A guitar on fire", "A lightning bolt"],
         "It was designed in 1970 by John Pasche, a London art student, who was paid £50.",
         wiki("Rolling Stones logo"), difficulty=1)
c.choice("In 1995, Blur and Oasis released singles on the same day. Who got to number one?", "Blur", ["Oasis", "Both, in a tie", "Neither of them"],
         "Blur's 'Country House' beat Oasis's 'Roll With It' in the 'Battle of Britpop'.",
         wiki("Battle of Britpop"), era="classic", difficulty=3)
c.yes_no("Did Oasis get back together for a world tour in 2025, after 16 years apart?", True,
         "Liam and Noel Gallagher reunited for Oasis Live '25, starting in Cardiff in July 2025.",
         wiki("Oasis Live '25 Tour"), era="modern", difficulty=1)
c.choice("Which of these was not one of the Spice Girls' nicknames?", "Cool Spice", ["Posh Spice", "Sporty Spice", "Ginger Spice"],
         "The five were Posh, Scary, Sporty, Baby and Ginger.",
         wiki("Spice Girls"), difficulty=1)
c.choice("Which brothers made up the Bee Gees?", "Barry, Robin and Maurice Gibb", ["Noel and Liam Gallagher", "Ray and Dave Davies", "Don and Phil Everly"],
         "Their songs 'Stayin' Alive' and 'Night Fever' were on the soundtrack of Saturday Night Fever.",
         wiki("Bee Gees"), era="classic", difficulty=2)
c.choice("Which American band sang 'Good Vibrations' and 'Surfin' USA'?", "The Beach Boys", ["The Monkees", "The Eagles", "The Byrds"],
         "They came from California and were three brothers, a cousin and a school friend.",
         wiki("The Beach Boys"), era="classic", difficulty=2)
c.choice("Which French duo always wore robot helmets in public?", "Daft Punk", ["Air", "Justice", "Phoenix"],
         "They hid their faces for almost 30 years before splitting up in 2021.",
         wiki("Daft Punk"), era="modern", difficulty=2)
c.choice("Which German band helped invent electronic pop music, with songs like 'The Model'?", "Kraftwerk", ["Rammstein", "Scorpions", "Tangerine Dream"],
         "Kraftwerk came from Düsseldorf. Their name means 'power station'.",
         wiki("Kraftwerk"), era="classic", difficulty=3)
c.choice("How many members are there in the K-pop girl group BLACKPINK?", "4", ["3", "5", "7"],
         "Jisoo, Jennie, Rosé and Lisa. Rosé had a worldwide hit with Bruno Mars, 'APT.', in 2024.",
         wiki("Blackpink"), era="modern", difficulty=2)
c.choice("Which band was Robbie Williams in before he went solo?", "Take That", ["Westlife", "Boyzone", "East 17"],
         "He left in 1995. His solo hit 'Angels' came out two years later.",
         wiki("Robbie Williams"), difficulty=1)

# Singers -------------------------------------------------------------------------------------------
c.choice("What was Freddie Mercury's name when he was born?", "Farrokh Bulsara", ["Frederick Mercer", "Fred Hoffman", "Farid Patel"],
         "He was born on the island of Zanzibar, now part of Tanzania, and moved to England as a teenager.",
         wiki("Freddie Mercury"), difficulty=3)
c.choice("What is Elton John's real name?", "Reginald Dwight", ["John Elton", "Reginald Bush", "Elton Hercules"],
         "He changed his name in 1972. 'Hercules' became his middle name.",
         wiki("Elton John"), difficulty=2)
c.choice("What is Lady Gaga's real name?", "Stefani Germanotta", ["Gabriella Garcia", "Stephanie Gates", "Gaia Lamberti"],
         "She took 'Gaga' from Queen's song 'Radio Ga Ga'.",
         wiki("Lady Gaga"), era="modern", difficulty=3)
c.choice("Which singer had a worldwide number one at 16 with '...Baby One More Time', in 1998?", "Britney Spears", ["Christina Aguilera", "Jessica Simpson", "Mandy Moore"],
         "It was her very first single. Its producer was the Swedish songwriter Max Martin.",
         wiki("...Baby One More Time (song)"), difficulty=2)
c.choice("At what age did Stevie Wonder sign with Motown?", "11", ["15", "18", "21"],
         "He has been blind since he was a baby and plays piano, drums and the harmonica.",
         wiki("Stevie Wonder"), era="classic", difficulty=3)
c.choice("In which American city did the Motown sound begin?", "Detroit", ["Memphis", "Chicago", "Nashville"],
         "The name is short for 'Motor Town', Detroit's nickname because of its car factories.",
         wiki("Motown"), difficulty=2)
c.choice("What was the name of Elvis Presley's mansion in Memphis?", "Graceland", ["Neverland", "Paisley Park", "Sun House"],
         "It's now a museum, and one of the most visited homes in America.",
         wiki("Graceland"), difficulty=2)
c.choice("Which country singer was known as 'The Man in Black'?", "Johnny Cash", ["Willie Nelson", "Kenny Rogers", "Hank Williams"],
         "He said he wore black for the poor and the forgotten.",
         wiki("Johnny Cash"), era="classic", difficulty=2)
c.choice("What was the name of Bob Marley's band?", "The Wailers", ["The Specials", "The Skatalites", "UB40"],
         "Bob Marley and the Wailers made 'No Woman, No Cry', 'One Love' and 'Three Little Birds'.",
         wiki("The Wailers"), difficulty=2)
c.yes_no("Did the singer-songwriter Bob Dylan win the Nobel Prize in Literature?", True,
         "He won it in 2016, the first songwriter to do so, 'for having created new poetic expressions within the great American song tradition'.",
         wiki("Bob Dylan"), difficulty=2)
c.choice("Which singer sang 'My Heart Will Go On', the theme from the film Titanic?", "Celine Dion", ["Whitney Houston", "Mariah Carey", "Shania Twain"],
         "It won the Oscar for Best Original Song in 1998.",
         wiki("My Heart Will Go On"), difficulty=1)
c.choice("Which London singer won five Grammy Awards in 2008 for the album Back to Black?", "Amy Winehouse", ["Adele", "Duffy", "Lily Allen"],
         "Her hits included 'Rehab' and 'Valerie'.",
         wiki("Amy Winehouse"), difficulty=2)
c.choice("In which English county did Ed Sheeran grow up?", "Suffolk", ["Yorkshire", "Cornwall", "Kent"],
         "His song 'Castle on the Hill' is about his home town of Framlingham.",
         wiki("Ed Sheeran"), era="modern", difficulty=3)
c.choice("Which grime artist headlined Glastonbury in 2019, wearing a stab vest designed by Banksy?", "Stormzy", ["Dizzee Rascal", "Skepta", "Dave"],
         "He was the first Black British solo artist to headline the Pyramid Stage.",
         wiki("Stormzy"), era="modern", difficulty=2)
c.choice("Which pop star, born in London, has parents from Kosovo?", "Dua Lipa", ["Rita Ora", "Jessie J", "Anne-Marie"],
         "She lived in Kosovo as a teenager, then moved back to London alone at 15 to chase music.",
         wiki("Dua Lipa"), era="modern", difficulty=2)
c.choice("Which singer re-recorded her first six albums, adding '(Taylor's Version)' to their names?", "Taylor Swift", ["Olivia Rodrigo", "Katy Perry", "Billie Eilish"],
         "She did it so she would own the recordings herself. In 2025 she bought back the originals too.",
         wiki("Taylor Swift"), era="modern", difficulty=1)
c.choice("Which Puerto Rican star headlined the Super Bowl halftime show in February 2026, singing almost entirely in Spanish?", "Bad Bunny", ["Daddy Yankee", "Ricky Martin", "J Balvin"],
         "A week earlier his album Debí Tirar Más Fotos had won the Grammy for Album of the Year.",
         SUPER_BOWL_LX, era="modern", difficulty=2)
c.choice("Which singer comes from Colombia?", "Shakira", ["Jennifer Lopez", "Gloria Estefan", "Rosalía"],
         "Shakira was born in Barranquilla and wrote her first song at the age of eight.",
         wiki("Shakira"), difficulty=1)
c.choice("Which American singer was known as 'the Godfather of Soul'?", "James Brown", ["Ray Charles", "Otis Redding", "Marvin Gaye"],
         "He was also called 'the hardest-working man in show business'.",
         wiki("James Brown"), era="classic", difficulty=2)
c.choice("Who sang 'Rocket Man' and 'Your Song'?", "Elton John", ["David Bowie", "Rod Stewart", "Billy Joel"],
         "Most of his songs have words by Bernie Taupin, his writing partner since 1967.",
         wiki("Elton John"), difficulty=1)
c.choice("Which Canadian singer released the huge 2019 hit 'Blinding Lights'?", "The Weeknd", ["Drake", "Post Malone", "Harry Styles"],
         "The Weeknd is the stage name of Abel Tesfaye, from Toronto. The song spent 90 weeks in the US Hot 100.",
         wiki("Blinding Lights"), era="modern", difficulty=2)

# Hit songs and big moments ------------------------------------------------------------------------------
c.choice("Which football song, by Baddiel, Skinner and the Lightning Seeds, says 'It's coming home'?", "Three Lions", ["World in Motion", "Vindaloo", "Back Home"],
         "It was written for Euro 96, which England hosted.",
         wiki("Three Lions (song)"), difficulty=1)
c.choice("Which festival on a dairy farm in New York State in 1969 drew around 400,000 people?", "Woodstock", ["Glastonbury", "Coachella", "Monterey Pop"],
         "It rained so much the fields turned to mud. Jimi Hendrix played the last set on Monday morning.",
         wiki("Woodstock"), era="classic", difficulty=2)
c.choice("Which 1960s girl group sang 'Baby Love' and 'Stop! In the Name of Love'?", "The Supremes", ["The Ronettes", "The Shirelles", "The Shangri-Las"],
         "Their lead singer was Diana Ross.",
         wiki("The Supremes"), era="classic", difficulty=2)
c.choice("Which Swedish singer won Eurovision twice, in 2012 and 2023?", "Loreen", ["Carola", "Måns Zelmerlöw", "Agnetha Fältskog"],
         "She won with 'Euphoria' and then 'Tattoo'. Only Ireland's Johnny Logan had won twice as a singer before her.",
         wiki("Loreen"), era="modern", difficulty=3)
c.choice("Which Italian rock band won Eurovision in 2021?", "Måneskin", ["Il Volo", "Negramaro", "Pooh"],
         "Their winning song, 'Zitti e buoni', was sung in Italian.",
         wiki("Måneskin"), era="modern", difficulty=3)
c.choice("Which Michael Jackson song has a music video with dancing zombies?", "Thriller", ["Bad", "Beat It", "Smooth Criminal"],
         "The video is almost 14 minutes long, more like a short film.",
         wiki("Michael Jackson's Thriller (music video)"), difficulty=1)
c.choice("What did Michael Jackson's family pop group call themselves?", "The Jackson 5", ["The Jackson Family", "The Osmonds", "The Jacksonville Five"],
         "Michael was the youngest of the five brothers in the group, and was singing lead at about 10 years old.",
         wiki("The Jackson 5"), difficulty=1)
c.choice("Who sang 'Respect', which became a theme song of 1960s America?", "Aretha Franklin", ["Diana Ross", "Tina Turner", "Etta James"],
         "Otis Redding wrote and recorded it first, but her version became far more famous.",
         wiki("Respect (song)"), era="classic", difficulty=2)

# Composers and instruments --------------------------------------------------------------------------
c.choice("Which piece of music by Beethoven is used as the anthem of the European Union?", "'Ode to Joy'", ["'Für Elise'", "'Moonlight Sonata'", "'The Blue Danube'"],
         "It comes from the last part of his Ninth Symphony, written when he was completely deaf.",
         wiki("Anthem of Europe"), difficulty=2)
c.choice("Roughly how old was Mozart when he wrote his first pieces of music?", "5", ["10", "14", "18"],
         "He was writing short keyboard pieces at five and his first symphony at about eight.",
         wiki("Wolfgang Amadeus Mozart"), difficulty=2)
c.choice("Which Austrian composer wrote 'The Blue Danube' waltz?", "Johann Strauss II", ["Mozart", "Haydn", "Schubert"],
         "It's played every New Year's Day in Vienna's famous concert.",
         wiki("The Blue Danube"), era="classic", difficulty=3)
c.choice("Who wrote the music for the musicals The Phantom of the Opera and Cats?", "Andrew Lloyd Webber", ["Tim Rice", "Stephen Sondheim", "Cameron Mackintosh"],
         "The Phantom of the Opera ran on Broadway for 35 years, longer than any other show.",
         wiki("Andrew Lloyd Webber"), difficulty=2)
c.choice("In which country is The Sound of Music set?", "Austria", ["Switzerland", "Germany", "Norway"],
         "It's based on the real von Trapp family singers from Salzburg.",
         wiki("The Sound of Music"), difficulty=1)
c.choice("Which instrument was invented by a Belgian called Adolphe and is named after him?", "The saxophone", ["The sousaphone", "The accordion", "The clarinet"],
         "Adolphe Sax patented it in 1846.",
         wiki("Adolphe Sax"), difficulty=2)
c.choice("How many valves does a standard trumpet have?", "3", ["2", "4", "6"],
         "Pressing the valves in different combinations, along with how you blow, makes all the notes.",
         wiki("Trumpet"), difficulty=2)
c.choice("Which family of instruments does the clarinet belong to?", "Woodwind", ["Brass", "Strings", "Percussion"],
         "It's usually made of wood and played with a reed, even though it has metal keys.",
         wiki("Clarinet"), difficulty=1)
c.choice("Which instrument does the leader of an orchestra usually play?", "The violin", ["The piano", "The cello", "The flute"],
         "The leader is the first violinist and tunes the orchestra before the concert.",
         wiki("Concertmaster"), difficulty=2)
c.choice("At what speed does a long-playing vinyl LP usually spin?", "33⅓ turns a minute", ["45 turns a minute", "78 turns a minute", "100 turns a minute"],
         "Singles usually spin at 45. Old shellac records spun at 78.",
         wiki("Phonograph record"), era="classic", difficulty=3)
