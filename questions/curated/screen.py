"""Film & TV, and Music. Questions ask about songs, artists and years, never lyrics."""

from . import Category, wiki

tv = Category("film-tv")

tv.yes_no("Did Leonardo DiCaprio star in The Wolf of Wall Street?", True,
          "He played the stockbroker Jordan Belfort in Martin Scorsese's 2013 film.",
          wiki("The Wolf of Wall Street (2013 film)"), era="modern", difficulty=2)
tv.choice("For which film did Leonardo DiCaprio finally win his first Oscar for Best Actor?", "The Revenant", ["Titanic", "Inception", "The Wolf of Wall Street"],
          "He won at the 2016 Academy Awards, after four earlier nominations for acting.",
          wiki("Leonardo DiCaprio"), era="modern", difficulty=2)
tv.choice("In which year was the film Titanic released?", "1997", ["1993", "2001", "1999"],
          "Titanic won 11 Oscars, a record it shares with Ben-Hur and The Lord of the Rings: The Return of the King.",
          wiki("Titanic (1997 film)"), era="classic", difficulty=2)
tv.choice("Who voices Woody in the Toy Story films?", "Tom Hanks", ["Tim Allen", "Robin Williams", "Billy Crystal"],
          "Tim Allen voices Buzz Lightyear.",
          wiki("Woody (Toy Story)"), difficulty=1)
tv.yes_no("Was Toy Story the first feature film made entirely with computer animation?", True,
          "Pixar's Toy Story came out in 1995 and changed animation for ever.",
          wiki("Toy Story"), difficulty=2)
tv.choice("What was Walt Disney's first full-length animated film, released in 1937?", "Snow White and the Seven Dwarfs", ["Pinocchio", "Bambi", "Cinderella"],
          "People called it 'Disney's Folly' before it came out, sure it would flop. It was a huge hit.",
          wiki("Snow White and the Seven Dwarfs (1937 film)"), era="classic", difficulty=2)
tv.choice("In which Disney film does Elsa sing 'Let It Go'?", "Frozen", ["Tangled", "Moana", "Encanto"],
          "Frozen came out in 2013 and 'Let It Go' won the Oscar for Best Original Song.",
          wiki("Frozen (2013 film)"), era="modern", difficulty=1)
tv.choice("In The Lion King, what is the name of Simba's father?", "Mufasa", ["Scar", "Rafiki", "Zazu"],
          "The Lion King came out in 1994. Scar is Mufasa's brother.",
          wiki("The Lion King"), difficulty=1)
tv.choice("In which year did the first Star Wars film come out?", "1977", ["1983", "1971", "1980"],
          "The first film was later renamed Star Wars: Episode IV, A New Hope.",
          wiki("Star Wars (film)"), era="classic", difficulty=2)
tv.choice("Who directed E.T. the Extra-Terrestrial and Jurassic Park?", "Steven Spielberg", ["George Lucas", "James Cameron", "Ridley Scott"],
          "E.T. came out in 1982 and Jurassic Park in 1993.",
          wiki("Steven Spielberg"), difficulty=2)
tv.choice("Which actor played James Bond in the first Bond film, Dr. No, in 1962?", "Sean Connery", ["Roger Moore", "George Lazenby", "David Niven"],
          "Sean Connery played Bond in six official films.",
          wiki("Dr. No (film)"), era="classic", difficulty=2)
tv.higher_lower("Daniel Craig first played James Bond in Casino Royale. Was that before or after 2005?", False,
                "Casino Royale came out in 2006. Daniel Craig's last Bond film was No Time to Die in 2021.",
                wiki("Casino Royale (2006 film)"), labels=("Before", "After"), era="modern", difficulty=2)
tv.choice("Which actor played Harry Potter in all eight films?", "Daniel Radcliffe", ["Rupert Grint", "Tom Felton", "Eddie Redmayne"],
          "Daniel Radcliffe was 11 when filming began on Harry Potter and the Philosopher's Stone.",
          wiki("Daniel Radcliffe"), era="modern", difficulty=1)
tv.choice("Which film has made the most money at cinemas ever, without adjusting for inflation?", "Avatar", ["Avengers: Endgame", "Titanic", "Star Wars: The Force Awakens"],
          "James Cameron's Avatar, first released in 2009, has taken more than $2.9 billion around the world.",
          wiki("List of highest-grossing films"), era="modern", difficulty=2, as_of="2026-11")
tv.choice("Which British studio makes Wallace & Gromit?", "Aardman Animations", ["Pixar", "DreamWorks", "Studio Ghibli"],
          "Aardman is based in Bristol. Wallace and Gromit first appeared in A Grand Day Out in 1989.",
          wiki("Wallace & Gromit"), difficulty=2)
tv.choice("Which actor plays Mr Bean?", "Rowan Atkinson", ["Hugh Laurie", "Stephen Fry", "Ricky Gervais"],
          "Mr Bean barely speaks, which is why he's popular all over the world.",
          wiki("Mr. Bean"), difficulty=1)
tv.choice("Which film won the first ever Oscar for Best Animated Feature?", "Shrek", ["Toy Story", "Monsters, Inc.", "Spirited Away"],
          "Shrek won at the 2002 Academy Awards, the first year the award was given.",
          wiki("Academy Award for Best Animated Feature"), era="modern", difficulty=3)
tv.choice("In Home Alone, who gets left behind when his family flies to Paris for Christmas?", "Kevin", ["Harry", "Marv", "Buzz"],
          "Home Alone came out in 1990. Macaulay Culkin played Kevin McCallister.",
          wiki("Home Alone"), difficulty=1)
tv.choice("Who stars as Buddy, a human raised by elves, in the Christmas film Elf?", "Will Ferrell", ["Jim Carrey", "Adam Sandler", "Ben Stiller"],
          "Elf came out in 2003 and was directed by Jon Favreau.",
          wiki("Elf (film)"), era="modern", difficulty=2)
tv.choice("Who plays Scrooge in The Muppet Christmas Carol?", "Michael Caine", ["Patrick Stewart", "Jim Carrey", "Bill Murray"],
          "The film came out in 1992. Michael Caine played the part completely straight, as if acting with real people.",
          wiki("The Muppet Christmas Carol"), difficulty=2)
tv.choice("In Back to the Future, what speed does the DeLorean need to reach to travel in time?", "88 mph", ["100 mph", "70 mph", "121 mph"],
          "Doc Brown's time machine was powered by 1.21 gigawatts of electricity.",
          wiki("DeLorean time machine"), era="classic", difficulty=2)
tv.choice("What colour are Dorothy's magic slippers in the 1939 film of The Wizard of Oz?", "Ruby red", ["Silver", "Gold", "Emerald green"],
          "In the original book they are silver. The film made them red to show off its new Technicolor.",
          wiki("Ruby slippers"), era="classic", difficulty=2)
tv.choice("Which film won the Oscar for Best Picture at the 2024 Academy Awards?", "Oppenheimer", ["Barbie", "Poor Things", "Killers of the Flower Moon"],
          "Oppenheimer won seven Oscars, including Best Director for Christopher Nolan.",
          wiki("Oppenheimer (film)"), era="modern", difficulty=2)
tv.choice("Which was the highest-earning film of 2023 at cinemas around the world?", "Barbie", ["Oppenheimer", "The Super Mario Bros. Movie", "Wonka"],
          "Barbie, directed by Greta Gerwig, took more than $1.4 billion.",
          wiki("Barbie (film)"), era="modern", difficulty=2)
tv.choice("In which year did Stranger Things first appear on Netflix?", "2016", ["2013", "2019", "2010"],
          "The series is set in the 1980s in the made-up town of Hawkins, Indiana.",
          wiki("Stranger Things"), era="modern", difficulty=2)
tv.choice("In which country is the Netflix series Squid Game made?", "South Korea", ["Japan", "China", "Thailand"],
          "Squid Game came out in 2021 and became Netflix's most-watched series at the time.",
          wiki("Squid Game"), era="modern", difficulty=1)
tv.choice("Which royal family is the Netflix drama The Crown about?", "The British royal family", ["The Danish royal family", "The Spanish royal family", "The Dutch royal family"],
          "The Crown follows the reign of Queen Elizabeth II and ran from 2016 to 2023.",
          wiki("The Crown (TV series)"), era="modern", difficulty=1)
tv.choice("Which Addams Family character has her own Netflix series, first shown in 2022?", "Wednesday", ["Morticia", "Lurch", "Gomez"],
          "Jenna Ortega plays Wednesday Addams. The series was directed in part by Tim Burton.",
          wiki("Wednesday (TV series)"), era="modern", difficulty=1)
tv.choice("Which streaming service makes the comedy Ted Lasso?", "Apple TV+", ["Netflix", "Amazon Prime Video", "Disney+"],
          "Ted Lasso is about an American football coach who ends up managing an English football club.",
          wiki("Ted Lasso"), era="modern", difficulty=2)
tv.choice("In which year was Doctor Who first shown on the BBC?", "1963", ["1970", "1955", "1980"],
          "The first episode went out on 23 November 1963. The Doctor travels in the TARDIS, which is bigger on the inside.",
          wiki("Doctor Who"), era="classic", difficulty=2)
tv.choice("What does the Doctor in Doctor Who travel in?", "The TARDIS", ["The Millennium Falcon", "The DeLorean", "The Enterprise"],
          "TARDIS stands for Time And Relative Dimension In Space. It looks like an old police box.",
          wiki("TARDIS"), difficulty=1)
tv.choice("Which is the longest-running TV soap opera in the UK?", "Coronation Street", ["EastEnders", "Emmerdale", "Hollyoaks"],
          "Coronation Street began on 9 December 1960. It's set in the fictional town of Weatherfield.",
          wiki("Coronation Street"), era="classic", difficulty=2)
tv.choice("In Only Fools and Horses, what is Del Boy's surname?", "Trotter", ["Fawlty", "Steptoe", "Mainwaring"],
          "Del Boy, Rodney and Grandad lived in a tower block in Peckham called Nelson Mandela House.",
          wiki("Only Fools and Horses"), era="classic", difficulty=2)
tv.choice("How many series of Friends were made?", "10", ["8", "12", "6"],
          "Friends ran from 1994 to 2004, with 236 episodes.",
          wiki("Friends"), era="classic", difficulty=2)
tv.choice("What is the name of the town where The Simpsons live?", "Springfield", ["Shelbyville", "Riverdale", "Quahog"],
          "The Simpsons began as a series in 1989 and is the longest-running American sitcom.",
          wiki("The Simpsons"), difficulty=1)
tv.choice("Which BBC children's programme gives out famous badges?", "Blue Peter", ["Newsround", "Grange Hill", "Byker Grove"],
          "Blue Peter began in 1958, making it the longest-running children's TV programme in the world.",
          wiki("Blue Peter"), difficulty=1)
tv.choice("What do contestants make in The Great British Bake Off's 'technical challenge'?", "A recipe they haven't been told about in advance", ["Their own favourite cake", "Bread only", "A giant showstopper"],
          "In the technical challenge everyone gets the same stripped-down recipe, and the judges taste the results without knowing who made what.",
          wiki("The Great British Bake Off"), era="modern", difficulty=2)
tv.choice("In which year did Strictly Come Dancing begin?", "2004", ["1999", "2010", "2007"],
          "Its name joins two older shows: Come Dancing and the film Strictly Ballroom. Around the world the format is known as Dancing with the Stars.",
          wiki("Strictly Come Dancing"), era="modern", difficulty=3)
tv.choice("Which Christmas cartoon features a song called 'Walking in the Air'?", "The Snowman", ["The Gruffalo", "Father Christmas", "The Polar Express"],
          "The Snowman was first shown on Channel 4 in 1982. The story itself is told without any dialogue.",
          wiki("The Snowman (film)"), era="classic", difficulty=2)
tv.choice("Which bear from 'darkest Peru' loves marmalade sandwiches?", "Paddington", ["Winnie-the-Pooh", "Rupert", "Baloo"],
          "Michael Bond's first Paddington book came out in 1958. The bear is named after the London station where he's found.",
          wiki("Paddington Bear"), difficulty=1)
tv.choice("Which video game became a hit film in 2025, starring Jack Black and Jason Momoa?", "A Minecraft Movie", ["The Super Mario Bros. Movie", "Sonic the Hedgehog 3", "Five Nights at Freddy's"],
          "A Minecraft Movie came out in April 2025. Jack Black played Steve.",
          wiki("A Minecraft Movie"), era="modern", difficulty=1)
tv.choice("Who directed the films Inception, Interstellar and Oppenheimer?", "Christopher Nolan", ["Denis Villeneuve", "Ridley Scott", "James Cameron"],
          "Christopher Nolan was born in London in 1970.",
          wiki("Christopher Nolan"), era="modern", difficulty=2)
tv.choice("In the Harry Potter films, which house does the Sorting Hat put Harry in?", "Gryffindor", ["Slytherin", "Hufflepuff", "Ravenclaw"],
          "The hat thought about Slytherin, but Harry asked it not to put him there.",
          wiki("Hogwarts"), difficulty=1)
tv.choice("Which magical nanny flies in with an umbrella in a 1964 Disney film?", "Mary Poppins", ["Nanny McPhee", "Maria von Trapp", "Matilda"],
          "Julie Andrews won the Oscar for Best Actress for playing Mary Poppins.",
          wiki("Mary Poppins (film)"), era="classic", difficulty=1)
tv.yes_no("Did Tom Hanks win Best Actor Oscars two years in a row?", True,
          "He won for Philadelphia in 1994 and for Forrest Gump in 1995.",
          wiki("Tom Hanks"), era="classic", difficulty=3)

music = Category("music")

music.choice("Which city did the Beatles come from?", "Liverpool", ["Manchester", "London", "Birmingham"],
             "John, Paul, George and Ringo played at Liverpool's Cavern Club nearly 300 times.",
             wiki("The Beatles"), era="classic", difficulty=1)
music.choice("Which Beatle played the drums?", "Ringo Starr", ["Paul McCartney", "George Harrison", "John Lennon"],
             "Ringo Starr joined in 1962, replacing Pete Best.",
             wiki("Ringo Starr"), era="classic", difficulty=1)
music.choice("Who was the lead singer of Queen?", "Freddie Mercury", ["Brian May", "Roger Taylor", "Elton John"],
             "Freddie Mercury was born Farrokh Bulsara in Zanzibar in 1946.",
             wiki("Freddie Mercury"), era="classic", difficulty=1)
music.choice("In which year did Queen release 'Bohemian Rhapsody'?", "1975", ["1968", "1985", "1980"],
             "It spent nine weeks at number one in the UK, and went to number one again in 1991.",
             wiki("Bohemian Rhapsody"), era="classic", difficulty=2)
music.choice("With which song did ABBA win the Eurovision Song Contest in 1974?", "Waterloo", ["Dancing Queen", "Mamma Mia", "Fernando"],
             "The contest was held in Brighton. Waterloo launched ABBA around the world.",
             wiki("Waterloo (ABBA song)"), era="classic", difficulty=2)
music.choice("Which country did ABBA come from?", "Sweden", ["Norway", "Denmark", "Finland"],
             "The band's name is made from the first letters of its members' names: Agnetha, Björn, Benny and Anni-Frid.",
             wiki("ABBA"), difficulty=1)
music.choice("Who was known as the King of Rock and Roll?", "Elvis Presley", ["Chuck Berry", "Buddy Holly", "Little Richard"],
             "Elvis's home, Graceland in Memphis, Tennessee, is now a museum.",
             wiki("Elvis Presley"), era="classic", difficulty=1)
music.choice("Which album by Michael Jackson is the best-selling album of all time?", "Thriller", ["Bad", "Off the Wall", "Dangerous"],
             "Thriller came out in 1982. Estimates of its sales are around 70 million copies.",
             wiki("Thriller (album)"), era="classic", difficulty=1, as_of="2026-11")
music.choice("Which singer-songwriter released 'Shape of You' in 2017?", "Ed Sheeran", ["Harry Styles", "Lewis Capaldi", "Sam Smith"],
             "Ed Sheeran grew up in Framlingham, Suffolk.",
             wiki("Shape of You"), era="modern", difficulty=1)
music.choice("Which tour by Taylor Swift became the highest-earning concert tour of all time?", "The Eras Tour", ["The Reputation Tour", "The 1989 World Tour", "The Red Tour"],
             "The Eras Tour ran from March 2023 to December 2024 and took more than $2 billion.",
             wiki("The Eras Tour"), era="modern", difficulty=1, as_of="2026-11")
music.choice("Which girl group's first single was 'Wannabe' in 1996?", "The Spice Girls", ["All Saints", "Girls Aloud", "Little Mix"],
             "Wannabe went to number one in 37 countries.",
             wiki("Wannabe (song)"), era="classic", difficulty=1)
music.choice("Which brothers led the band Oasis?", "Liam and Noel Gallagher", ["Ray and Dave Davies", "Barry and Robin Gibb", "Jim and William Reid"],
             "Oasis came from Manchester. The brothers reunited for a world tour in 2025, 16 years after the band split.",
             wiki("Oasis (band)"), era="classic", difficulty=1)
music.choice("Which famous composer kept writing music after going deaf?", "Ludwig van Beethoven", ["Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frédéric Chopin"],
             "Beethoven was almost completely deaf when he wrote his Ninth Symphony.",
             wiki("Ludwig van Beethoven"), difficulty=2)
music.choice("Which composer wrote 'The Four Seasons'?", "Antonio Vivaldi", ["Mozart", "Handel", "Beethoven"],
             "Vivaldi published the four violin concertos in 1725. Each one paints a season in music.",
             wiki("The Four Seasons (Vivaldi)"), difficulty=3)
music.choice("Which composer wrote the music for the ballet The Nutcracker?", "Pyotr Ilyich Tchaikovsky", ["Johann Strauss", "Igor Stravinsky", "Edward Elgar"],
             "The Nutcracker was first performed in St Petersburg in 1892 and is now a Christmas favourite.",
             wiki("The Nutcracker"), difficulty=2)
music.choice("In which Austrian city was Mozart born?", "Salzburg", ["Vienna", "Innsbruck", "Graz"],
             "Mozart was born in 1756 and was writing music by the age of five.",
             wiki("Wolfgang Amadeus Mozart"), difficulty=2)
music.choice("In which year was 'All I Want for Christmas Is You' by Mariah Carey first released?", "1994", ["1999", "1988", "2004"],
             "It took 25 years to reach number one in the US charts, in December 2019.",
             wiki("All I Want for Christmas Is You"), era="classic", difficulty=2)
music.choice("Which group released 'Last Christmas' in 1984?", "Wham!", ["Duran Duran", "Spandau Ballet", "Culture Club"],
             "Last Christmas reached number one in the UK for the first time on New Year's Day 2021, 36 years after it came out.",
             wiki("Last Christmas"), era="classic", difficulty=1)
music.choice("Which charity group released 'Do They Know It's Christmas?' in 1984?", "Band Aid", ["Live Aid", "USA for Africa", "Comic Relief"],
             "It was organised by Bob Geldof and Midge Ure to raise money for famine relief in Ethiopia.",
             wiki("Do They Know It's Christmas?"), era="classic", difficulty=2)
music.choice("Who sang 'Fairytale of New York' with Kirsty MacColl?", "The Pogues", ["U2", "The Clash", "Simple Minds"],
             "It came out in 1987 and reached number two in the UK.",
             wiki("Fairytale of New York"), era="classic", difficulty=2)
music.choice("Which band released 'Merry Xmas Everybody' in 1973?", "Slade", ["Wizzard", "T. Rex", "Sweet"],
             "Slade's song was the UK Christmas number one in 1973.",
             wiki("Merry Xmas Everybody"), era="classic", difficulty=2)
music.choice("Which singer had the best-selling single of all time with 'White Christmas'?", "Bing Crosby", ["Frank Sinatra", "Dean Martin", "Nat King Cole"],
             "Guinness World Records lists it as the best-selling single ever, at an estimated 50 million copies.",
             wiki("White Christmas (song)"), era="classic", difficulty=2, as_of="2026-11")
music.choice("Which song by Elton John became the best-selling single ever in the UK, in 1997?", "Candle in the Wind 1997", ["Your Song", "Rocket Man", "I'm Still Standing"],
             "He re-recorded it in memory of Diana, Princess of Wales.",
             wiki("Candle in the Wind 1997"), era="classic", difficulty=3)
music.choice("Which singer won Eurovision for Switzerland in 1988, before becoming a world star?", "Celine Dion", ["Shania Twain", "Whitney Houston", "Lara Fabian"],
             "Celine Dion, who is Canadian, won with the song 'Ne partez pas sans moi'.",
             wiki("Eurovision Song Contest 1988"), era="classic", difficulty=3)
music.choice("Which group won Eurovision for the UK in 1997 with 'Love Shine a Light'?", "Katrina and the Waves", ["Bucks Fizz", "Brotherhood of Man", "Take That"],
             "It was the UK's fifth Eurovision win. The UK hasn't won since.",
             wiki("Love Shine a Light"), era="classic", difficulty=3, as_of="2026-11")
music.choice("In which year were the Live Aid concerts held at Wembley and in Philadelphia?", "1985", ["1980", "1990", "1975"],
             "Live Aid took place on 13 July 1985. Queen's performance is often called the best live set ever.",
             wiki("Live Aid"), era="classic", difficulty=2)
music.choice("Which song was the first YouTube video to reach a billion views?", "Gangnam Style", ["Baby", "Despacito", "Shake It Off"],
             "PSY's Gangnam Style passed a billion views in December 2012.",
             wiki("Gangnam Style"), era="modern", difficulty=2)
music.choice("Which South Korean band has members called RM, Jin, Suga, J-Hope, Jimin, V and Jungkook?", "BTS", ["Blackpink", "EXO", "Stray Kids"],
             "BTS became the first Korean act to top the US Billboard Hot 100, with 'Dynamite' in 2020.",
             wiki("BTS"), era="modern", difficulty=1)
music.choice("Who has won more Grammy Awards than any other artist?", "Beyoncé", ["Taylor Swift", "Quincy Jones", "Michael Jackson"],
             "Her win for Cowboy Carter at the 2025 Grammys took her total to 35.",
             wiki("Beyoncé"), era="modern", difficulty=2, as_of="2026-11")
music.choice("How many keys does a standard piano have?", "88", ["64", "76", "100"],
             "52 white keys and 36 black keys.",
             wiki("Piano"), difficulty=2)
music.choice("How many strings does a standard guitar have?", "Six", ["Four", "Five", "Eight"],
             "A bass guitar usually has four.",
             wiki("Guitar"), difficulty=1)
music.choice("How many strings does a violin have?", "Four", ["Three", "Five", "Six"],
             "The violin is the smallest and highest-pitched member of the violin family.",
             wiki("Violin"), difficulty=2)
music.choice("Which kind of music is Bob Marley famous for?", "Reggae", ["Jazz", "Blues", "Country"],
             "Bob Marley and the Wailers came from Jamaica.",
             wiki("Bob Marley"), era="classic", difficulty=1)
music.choice("Which Australian singer was in the soap Neighbours before her pop career?", "Kylie Minogue", ["Dannii Minogue", "Natalie Imbruglia", "Delta Goodrem"],
             "Kylie played Charlene in Neighbours. Her first big hit was 'I Should Be So Lucky' in 1988.",
             wiki("Kylie Minogue"), era="classic", difficulty=2)
music.choice("Which singer created the character Ziggy Stardust?", "David Bowie", ["Marc Bolan", "Freddie Mercury", "Elton John"],
             "Bowie's album The Rise and Fall of Ziggy Stardust came out in 1972.",
             wiki("Ziggy Stardust"), era="classic", difficulty=2)
music.choice("Who is the lead singer of the Rolling Stones?", "Mick Jagger", ["Keith Richards", "Ronnie Wood", "Rod Stewart"],
             "The Rolling Stones formed in London in 1962.",
             wiki("Mick Jagger"), era="classic", difficulty=1)
music.yes_no("Did Dolly Parton write 'I Will Always Love You', the song made huge by Whitney Houston?", True,
             "Dolly Parton wrote and released it in 1974. Whitney Houston's version came out in 1992 for the film The Bodyguard.",
             wiki("I Will Always Love You"), era="classic", difficulty=2)
music.choice("Which singer from Tottenham, London, released the albums 19, 21, 25 and 30?", "Adele", ["Amy Winehouse", "Dua Lipa", "Florence Welch"],
             "Each album is named after how old she was when she wrote most of it.",
             wiki("Adele"), era="modern", difficulty=1)
music.choice("Which music festival has a famous Pyramid Stage?", "Glastonbury", ["Reading", "Isle of Wight", "Download"],
             "Glastonbury first took place in 1970, the day after Jimi Hendrix died. Tickets cost £1 and included free milk.",
             wiki("Glastonbury Festival"), difficulty=2)
music.choice("Which singer is famous for the 'moonwalk' dance?", "Michael Jackson", ["Prince", "James Brown", "Justin Timberlake"],
             "He first did the moonwalk on TV in 1983, during 'Billie Jean'.",
             wiki("Moonwalk (dance)"), era="classic", difficulty=1)
music.choice("Which band, with Harry Styles, was formed on The X Factor in 2010?", "One Direction", ["Take That", "JLS", "The Wanted"],
             "One Direction finished third on The X Factor but became one of the best-selling boy bands ever.",
             wiki("One Direction"), era="modern", difficulty=1)
music.choice("Which singer had a huge hit with 'Bad Guy' in 2019?", "Billie Eilish", ["Olivia Rodrigo", "Ariana Grande", "Dua Lipa"],
             "Billie Eilish co-writes her songs with her brother, Finneas.",
             wiki("Bad Guy (Billie Eilish song)"), era="modern", difficulty=1)
music.choice("Which country won the 2026 Eurovision Song Contest in Vienna?", "Bulgaria", ["Israel", "Sweden", "Ukraine"],
             "It was Bulgaria's first ever Eurovision win. The UK's entry, Look Mum No Computer, came last.",
             ("Express & Star: Bulgaria wins first trophy as UK finishes last", "https://www.expressandstar.com/whats-on/showbiz/uks-look-mum-no-computer-last-in-eurovision-final-as-bulgaria-wins-first-trophy-8550005"),
             era="modern", difficulty=2)
music.choice("Which British band sang 'Yellow' and 'Viva la Vida'?", "Coldplay", ["Radiohead", "Keane", "Snow Patrol"],
             "Coldplay formed at University College London in 1997.",
             wiki("Coldplay"), era="modern", difficulty=1)
music.choice("Which Swedish songwriter has written hits for Britney Spears, Katy Perry and Taylor Swift?", "Max Martin", ["Benny Andersson", "Avicii", "Björn Ulvaeus"],
             "Only Paul McCartney and John Lennon have written more US number one hits than Max Martin.",
             wiki("Max Martin"), era="modern", difficulty=3)

assert (len(tv.questions), len(music.questions)) == (45, 45), (len(tv.questions), len(music.questions))
