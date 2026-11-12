"""Words & Language: where words come from, languages of the world, alphabets, spelling and wordplay."""

from . import Category, wiki

w = Category("words")

MW_QUIZ = ("Merriam-Webster: the history of 'quiz'", "https://www.merriam-webster.com/wordplay/word-history-of-quiz")
MENTAL_FLOSS = ("Mental Floss: 21 words created by Shakespeare", "https://mentalfloss.com/article/48657/20-words-")
WIKTIONARY_HANDSCHUH = ("Wiktionary: Handschuh", "https://en.wiktionary.org/wiki/Handschuh")

# Alphabets and letters
w.choice("How many letters are there in the English alphabet?", "26", ["24", "25", "28"],
         "They come from the Latin alphabet. J, U and W were added much later than the rest.",
         wiki("English alphabet"), difficulty=1)
w.choice("Which letter is used most often in written English?", "E", ["T", "A", "S"],
         "E turns up in about one in every eight letters. T and A come next.",
         wiki("Letter frequency"), difficulty=2)
w.choice("Which alphabet is used to write Russian?", "Cyrillic", ["Latin", "Greek", "Arabic"],
         "Cyrillic is also used for Ukrainian, Bulgarian, Serbian and many other languages.",
         wiki("Russian alphabet"), difficulty=1)
w.choice("Which of these languages is written from right to left?", "Arabic", ["Greek", "Hindi", "Russian"],
         "Hebrew and Persian are written from right to left too, though numbers usually run left to right.",
         wiki("Right-to-left script"), difficulty=2)
w.choice("The word 'alphabet' comes from the first two letters of which alphabet?", "Greek", ["Latin", "Hebrew", "Cyrillic"],
         "Alpha and beta are the first two letters of the Greek alphabet.",
         wiki("Greek alphabet"), difficulty=1)
w.choice("What is the last letter of the Greek alphabet?", "Omega", ["Zeta", "Sigma", "Delta"],
         "That's why 'alpha and omega' means the beginning and the end.",
         wiki("Omega"), difficulty=2)
w.choice("How many letters does the Hawaiian alphabet have?", "13", ["9", "20", "26"],
         "Five vowels, seven consonants and the ʻokina, a mark that stands for a short pause in the voice.",
         wiki("Hawaiian alphabet"), difficulty=3)
w.yes_no("Is the letter Q always followed by a U in English words?", False,
         "Words such as Qatar, Iraqi and qwerty break the rule, and Scrabble players love 'qi'.",
         wiki("List of English words containing Q not followed by U"), difficulty=2)
w.choice("What is the QWERTY keyboard named after?", "The first six letters on its top row of letters", ["The man who invented it", "A town in America", "The sound the keys make"],
         "The layout dates from typewriters in the 1870s.",
         wiki("QWERTY"), difficulty=2)
w.choice("In the NATO radio alphabet, which word stands for the letter Z?", "Zulu", ["Zebra", "Zero", "Zed"],
         "The alphabet runs Alfa, Bravo, Charlie, and so on, so letters can't be misheard over a crackly radio.",
         wiki("NATO phonetic alphabet"), difficulty=2)

# Where words come from
w.choice("Which language does the word 'kindergarten' come from?", "German", ["Dutch", "French", "Swedish"],
         "It means 'children's garden'. Friedrich Fröbel opened the first one in Germany in 1837.",
         wiki("Kindergarten"), difficulty=1)
w.choice("Which language does the word 'shampoo' come from?", "Hindi", ["French", "Arabic", "Persian"],
         "It comes from a word meaning 'to press or knead'. Sake Dean Mahomed opened shampooing baths in Brighton in 1814.",
         wiki("Shampoo"), difficulty=3)
w.choice("The word 'robot' was first used in a play from 1920. Which language does it come from?", "Czech", ["Russian", "German", "Polish"],
         "Karel Čapek's play R.U.R. used it, from 'robota', meaning forced labour. His brother Josef suggested the word.",
         wiki("Robot"), difficulty=2)
w.choice("Which language does the word 'tsunami' come from?", "Japanese", ["Chinese", "Indonesian", "Hawaiian"],
         "It means 'harbour wave'.",
         wiki("Tsunami"), difficulty=1)
w.choice("Which language does the word 'safari' come from?", "Swahili", ["Zulu", "Afrikaans", "Hindi"],
         "In Swahili, safari simply means 'journey'.",
         wiki("Safari"), difficulty=2)
w.choice("The word 'avocado' comes, through Spanish, from which language?", "Nahuatl, the language of the Aztecs", ["Latin", "Arabic", "Portuguese"],
         "The Aztec word was āhuacatl. Tomato and chilli come from Nahuatl too.",
         wiki("Avocado"), difficulty=3)
w.choice("Which language does the word 'algebra' come from?", "Arabic", ["Greek", "Latin", "Persian"],
         "It comes from 'al-jabr' in the title of a maths book written in Baghdad in the 800s.",
         wiki("Algebra"), difficulty=2)
w.choice("The word 'bungalow' comes from a word meaning 'from Bengal' in which language?", "Hindi", ["Portuguese", "Malay", "Tamil"],
         "British people in India used it for low, single-storey houses with a veranda.",
         wiki("Bungalow"), difficulty=3)
w.yes_no("Do we know for certain where the word 'quiz' comes from?", False,
         "A famous story says a Dublin theatre manager chalked 'quiz' on walls to win a bet, but there's no evidence for it. Its origin is still a mystery.",
         MW_QUIZ, difficulty=3)
w.choice("Which of these words is first recorded in Shakespeare's plays?", "Eyeball", ["Robot", "Selfie", "Telephone"],
         "Shakespeare is also credited with 'swagger', 'fashionable' and 'uncomfortable'.",
         MENTAL_FLOSS, difficulty=2)
w.choice("Which language does the word 'ski' come from?", "Norwegian", ["German", "Swiss German", "Finnish"],
         "It comes from an Old Norse word for a split piece of wood.",
         wiki("Ski"), difficulty=2)
w.choice("Which language does the word 'yoghurt' come from?", "Turkish", ["Greek", "Bulgarian", "Persian"],
         "It comes from a Turkish word meaning to knead or thicken.",
         wiki("Yogurt"), difficulty=2)
w.choice("Which language does the word 'cookie' come from?", "Dutch", ["German", "French", "Danish"],
         "It comes from 'koekje', meaning 'little cake'.",
         wiki("Cookie"), difficulty=2)
w.yes_no("Does the word 'emoji' come from the English word 'emotion'?", False,
         "It's Japanese: 'e' means picture and 'moji' means character. The likeness to 'emotion' is a happy accident.",
         wiki("Emoji"), era="modern", difficulty=2)
w.choice("What does 'karaoke' mean in Japanese?", "Empty orchestra", ["Sing along", "Loud voice", "Happy music"],
         "The music plays without a singer, leaving the space for you.",
         wiki("Karaoke"), difficulty=3)
w.choice("The radio distress call 'Mayday' comes from which language?", "French", ["Spanish", "German", "Latin"],
         "It comes from 'm'aider', as in 'come and help me'. It was chosen in 1923 by a radio officer at Croydon airport.",
         wiki("Mayday"), difficulty=2)
w.choice("Which word was Oxford Dictionaries' Word of the Year in 2013?", "Selfie", ["Hashtag", "Vape", "Emoji"],
         "Vape was chosen in 2014.",
         wiki("Selfie"), era="modern", difficulty=2)
w.yes_no("Did a word that doesn't mean anything once get printed in a major dictionary by mistake?", True,
         "'Dord' appeared in Webster's dictionary in 1934, after a note saying 'D or d' was misread. It stayed for years before anyone noticed.",
         wiki("Dord"), era="classic", difficulty=3)

# Languages of the world
w.choice("'Piano' is short for 'pianoforte'. What does that mean in Italian?", "Soft-loud", ["Many strings", "Little music", "Big keys"],
         "Earlier keyboards couldn't change volume. The pianoforte could play softly or loudly depending on how hard you pressed.",
         wiki("Piano"), difficulty=3)
w.choice("What is the main language of Brazil?", "Portuguese", ["Spanish", "Italian", "French"],
         "Brazil has more Portuguese speakers than Portugal, by about 20 times.",
         wiki("Brazilian Portuguese"), difficulty=1)
w.higher_lower("Wales has two official languages. Does Switzerland have more or fewer national languages?", True,
               "Switzerland has four: German, French, Italian and Romansh.",
               wiki("Languages of Switzerland"), labels=("More", "Fewer"), difficulty=2)
w.choice("In which country is Afrikaans mainly spoken?", "South Africa", ["The Netherlands", "Kenya", "Nigeria"],
         "Afrikaans grew out of Dutch, so Dutch and Afrikaans speakers can often understand each other.",
         wiki("Afrikaans"), difficulty=2)
w.choice("How many official languages does the United Nations use?", "6", ["2", "4", "10"],
         "Arabic, Chinese, English, French, Russian and Spanish.",
         wiki("Official languages of the United Nations"), difficulty=3)
w.choice("What is the national language of Pakistan?", "Urdu", ["Hindi", "Punjabi", "Persian"],
         "English is an official language there too.",
         wiki("Urdu"), difficulty=2)
w.choice("In which country is Catalan the only official language?", "Andorra", ["Spain", "Monaco", "Malta"],
         "In Spain, Catalan is official in Catalonia alongside Spanish.",
         wiki("Andorra"), difficulty=3)
w.choice("Basque is spoken in parts of Spain and France. Which language is it related to?", "None that anyone has found", ["Spanish", "French", "Finnish"],
         "Basque is a 'language isolate': no link to any other living language has been proved.",
         wiki("Basque language"), difficulty=3)

# Words in other languages
w.choice("What does 'déjà vu' mean in French?", "Already seen", ["Good luck", "See you soon", "Too late"],
         "It's the strange feeling that you've lived a moment before.",
         wiki("Déjà vu"), difficulty=2)
w.choice("In Italian, what does 'ciao' mean?", "Both hello and goodbye", ["Only hello", "Thank you", "Please"],
         "It comes from an old Venetian phrase meaning 'I am your slave', said as a friendly 'at your service'.",
         wiki("Ciao"), difficulty=2)
w.choice("The German word 'Handschuh' means 'hand shoe'. What is it?", "A glove", ["A sock", "A ring", "A watch"],
         "German is full of words built like this. A 'Kühlschrank', a 'cool cupboard', is a fridge.",
         WIKTIONARY_HANDSCHUH, difficulty=2)
w.choice("What do Americans call the boot of a car?", "The trunk", ["The hood", "The deck", "The back"],
         "Americans call the bonnet the hood.",
         wiki("Trunk (car)"), difficulty=1)
w.choice("What do Americans call a full stop?", "A period", ["A dot", "A point", "A stop"],
         "Americans also say 'period' at the end of a sentence to mean 'and that's final'.",
         wiki("Full stop"), difficulty=1)

# Wordplay and grammar
w.choice("What do you call a word that reads the same backwards, like 'level'?", "A palindrome", ["An anagram", "A homophone", "An acronym"],
         "'Racecar' and 'kayak' are palindromes too.",
         wiki("Palindrome"), difficulty=1)
w.choice("Which of these is not an anagram of 'listen'?", "Listed", ["Silent", "Tinsel", "Enlist"],
         "An anagram uses exactly the same letters. 'Listed' swaps the N for a D.",
         wiki("Anagram"), difficulty=2)
w.choice("Which pair of words are homophones?", "Bear and bare", ["Cat and cot", "Tough and though", "Lead and leaf"],
         "Homophones sound the same but are spelled differently and mean different things.",
         wiki("Homophone"), difficulty=2)
w.yes_no("Is 'scuba' short for something?", True,
         "It stands for self-contained underwater breathing apparatus.",
         wiki("Scuba set"), difficulty=2)
w.choice("What does the A in LASER stand for?", "Amplification", ["Atomic", "Accelerated", "Array"],
         "LASER is short for light amplification by stimulated emission of radiation.",
         wiki("Laser"), difficulty=3)
w.choice("What does 'i.e.' mean?", "That is", ["For example", "And so on", "Note well"],
         "It's short for the Latin 'id est'. 'For example' is e.g.",
         wiki("List of Latin abbreviations"), difficulty=2)
w.choice("Which is usually called the longest word in major English dictionaries?", "Pneumonoultramicroscopicsilicovolcanoconiosis",
         ["Antidisestablishmentarianism", "Supercalifragilisticexpialidocious", "Floccinaucinihilipilification"],
         "It's a lung disease caused by breathing in very fine dust. It was invented in 1935 to be the longest word.",
         wiki("Longest word in English"), difficulty=3)
w.higher_lower("'Antidisestablishmentarianism' has 28 letters. Does 'pneumonoultramicroscopicsilicovolcanoconiosis' have more or fewer?", True,
               "It has 45 letters.",
               wiki("Longest word in English"), labels=("More", "Fewer"), difficulty=2)
w.choice("What is a group of flamingos called?", "A flamboyance", ["A pride", "A parliament", "A pod"],
         "A pride is lions, a parliament is owls and a pod is whales or dolphins.",
         wiki("List of English terms of venery, by animal"), difficulty=3)
w.choice("What is a group of whales called?", "A pod", ["A flock", "A herd", "A shoal"],
         "A shoal is fish.",
         wiki("List of English terms of venery, by animal"), difficulty=2)
w.choice("In English Scrabble, which two letters are worth 10 points?", "Q and Z", ["X and J", "K and V", "Y and W"],
         "J and X are worth 8.",
         wiki("Scrabble letter distributions"), difficulty=3)
w.choice("How many tiles are there in a standard English Scrabble set?", "100", ["50", "88", "120"],
         "Two of them are blanks, which can stand for any letter.",
         wiki("Scrabble letter distributions"), difficulty=3)
w.choice("What is the word for a word that sounds like what it describes, such as 'buzz'?", "Onomatopoeia", ["Alliteration", "Metaphor", "Simile"],
         "'Sizzle', 'pop' and 'splash' are onomatopoeia too.",
         wiki("Onomatopoeia"), difficulty=2)
w.choice("'She sells seashells by the seashore' is an example of what?", "Alliteration", ["Onomatopoeia", "A palindrome", "Rhyme"],
         "Alliteration repeats the same sound at the start of words close together.",
         wiki("Alliteration"), difficulty=2)
w.choice("What do you call a word that means the opposite of another, like 'hot' and 'cold'?", "An antonym", ["A synonym", "A homonym", "An acronym"],
         "A synonym means the same, like 'big' and 'large'.",
         wiki("Opposite (semantics)"), difficulty=1)
w.choice("Which word turns up more often than any other in written English?", "The", ["And", "A", "Of"],
         "'The' makes up roughly one in every 20 words people write. 'Be' and 'to' come next in most counts.",
         wiki("Most common words in English"), difficulty=2)
w.higher_lower("A haiku has 3 lines. Does a limerick have more or fewer?", True,
               "A limerick has 5 lines, and the first, second and fifth rhyme.",
               wiki("Limerick (poetry)"), labels=("More", "Fewer"), difficulty=2)
w.choice("How many lines does a sonnet have?", "14", ["10", "12", "16"],
         "Shakespeare wrote 154 of them.",
         wiki("Sonnet"), difficulty=2)
w.choice("What does 'www' stand for at the start of a web address?", "World Wide Web", ["Wide Web Window", "World Web Wire", "Web With Words"],
         "Tim Berners-Lee invented the World Wide Web in 1989.",
         wiki("World Wide Web"), difficulty=1)
