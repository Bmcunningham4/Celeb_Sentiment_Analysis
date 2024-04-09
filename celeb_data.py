import re

#? Function to extract tweets (accounting for diff tweet dates)
def extract_tweets(data, pattern_num):
    tweets = []
    patterns = [
        r'(@[^\s]+)\s*·\s*(\w+\s+\d+,\s+\d+)\s*(.*)', 
        r'(@[^\s]+)\s*·\s*Apr \d+\s*(.*)', 
        r'(@[^\s]+)\s*·\s*(\w{3}\s+\d+(?:,\s+\d+)?)\s*(.*)',
        r'(@[^\s]+)\s*·\s*(\d+(?:m|mins)?)(?:\s*|\s+,?\s+\d{4})\s*(.*)',
        r'(@[^\s]+)\s*·\s*(\d+(?:h|hrs?|m|mins?|s|secs?)?)\s*(?:ago)?\s*(.*)'
    ]
    
    pattern = patterns[pattern_num]
    matches = re.findall(pattern, data)
    for match in matches:
        tweets.append([match[0], match[2]])
    return tweets


#? 50 Most recent Tweet replies on celebreties account
Joe_Biden = """
Gunther Eagleman™
@GuntherEagleman
·
Apr 1
Not today, dipshit!   Its Easter.
End Wokeness
@EndWokeness
·
Apr 1
No we aren't doing this crap, Joe. Today is Easter. Period + ratio.
Lavern Spicer 🇺🇸
@lavern_spicer
·
Apr 1
Nigga, you lost the whole Black vote with this shit. It’s Easter. Not some trans day.
Steve Guest
@SteveGuest
·
Apr 1
It’s Easter.
Dan Bilzerian
@DanBilzerian
·
Apr 1
Fuck right off
Cloudy 🌥️ (estrogen angel)
@oncloud_e
·
Apr 1
hey man that sounds cool, but what are you actually doing for us right now to show it
Culture Critic
@Culture_Crit
·
Apr 1
Today is Easter Sunday.
Ryan Fournier
@RyanAFournier
·
Apr 1
Enjoy the ratio.
DAN
@GordoDan_
·
Apr 1
HAPPY EGGS DAY


Paul Emerson
@notanokguy
·
Apr 1
You’re the weakest President in American history.
ALX 🇺🇸

@alx
·
Apr 1
The double down is wild
Jay Black
@jayblackisfunny
·
Apr 1
I’m sure the replies to this tweet asking for kindness and respect to be shown towards a marginalized community will be *filled* with the kind of Christian love that Jesus would have wanted from His followers.
⏰0HOUR⏰
@0HOUR
·
Apr 1
Christ is King

You mock the son of God

Fuck off

Satan
Liberacrat Media™️
@Liberacrat_
·
Apr 1
You misspelled HAPPY EASTER you loser.
Wealth Turtle 💰 🐢
@wealth_turtle
·
Apr 1
This is what democrats are celebrating


Steve Inman
@SteveInmanUIC
·
Apr 1
Happy Jesus Day of Visibility you demon .
Liberacrat Media™️
@Liberacrat_
·
Apr 1
What visibility and rights don’t these people have? Remind me again…
Paul A. Szypula 🇺🇸
@Bubblebathgirl
·
Apr 1
Today is Easter.

Stop bastardizing our sacred holidays by forcing gender ideology into the mix.

Everyone is America is already equal.

We don’t need another “special” holiday.

Joe Biden keeps proving that he’s a fake Catholic.

First abortion till birth now this.

Disgraceful.
Show more
Matt Wallace
@MattWallace888
·
Apr 1
THE BIDEN ADMINISTRATION IS RUN BY A GROUP OF PEOPLE WHO HATE CHRISTIANS‼️  

#ChristIsKing
🇺🇸 Pismo 🇺🇸
@Pismo_B
·
Apr 1
YOU ARE A SICK PATHETIC TWISTED POS!
Ronny Jackson
@RonnyJacksonTX
·
Apr 1
TODAY IS EASTER!!
Vince Langman
@LangmanVince
·
Apr 1
Speaking of Transgender Awareness, this one killed 6 people, including 3 children in Nashville last year


Scott Mason
@hypnoksa
·
Apr 1
Happy Easter
Clara Jones
@debbieformola
·
Apr 1
I noticed last week you didn’t mention Vietnams Veterans Day ..but you absolutely needed to announce this !!
classicsgroyp
@classicsgroyp
·
Apr 1
We're celebrating Easter
Quote
classicsgroyp
@classicsgroyp
·


Happy Easter, my friends. Excited to build a Christian future with you 🩵
Show more
0:03 / 0:58
Inverse Cramer (Not Jim Cramer)
@CramerTracker
·
Apr 1
On Easter?
PNWGUERRILLA
@pnwguerrilla
·
Apr 1
Now call me crazy, but wouldn’t this imply that there are invisible transgenders? 

How does this power work? 

If I say I am a woman can I become invisible???

I have questions.


Three Year Letterman
@3YearLetterman
·
Apr 1
It’s Jesus’s birthday, Joel. Delete this
Progressing California
@ProgressingCali
·
Apr 1
Then go full visibility, release the manifesto.
Manz🌪
@notmrmanziel
·
Apr 1
It’s Easter man 

It’s like you’re doing it on purpose at this point.
Filipe Sabará
@FilipeSabara
·
Apr 1
SHAME ON YOU! Today is Easter.
🌈 Tess T. Eccles-Brown, PhD
@TTEcclesBrown
·
Apr 1
Joe Biden stands up for women this Easter!
Vince Langman
@LangmanVince
·
Apr 1
You're truly demonic
Liberacrat Media™️
@Liberacrat_
·
Apr 1
We saw your real message, Briben.👇
Gimme3Steps
@TheSouthGAJohn
·
Apr 1
Patriot Day of Visibility is on November 5th


RAN_DUMB_LIBS
@Ran_Dumb_Libs
·
Apr 1
Like a dog that never gets attention 🤡
Brian Mazzola
@BrianNMazzola
·
Apr 1
I believe in forgiveness, but if you continue to live this way, there’s a special place in hell for you, Mr. Joe Biden.
Malissa Canton
@MalCan4401
·
Apr 1
Make them as visible as possible! #TransDayOfVisibility
Planet Of Memes
@PlanetOfMemes
·
Apr 1
I'm sorry, we moved that.
🏳️‍🌈🇮🇱🚩Shalom Barba
@MafinhaBarba
·
Apr 1
You will lose. The American people will not tolerate such disrespect.
DieselBabe🌟
@DieselBABE20
·
Apr 1
You’re a sick, evil, vile man.  Any other day…Easter is for JESUS.  I hope this backfires tremendously for you, 🤮
ConserValidity
@ConserValidity
·
Apr 1
Correction #DementiaJoe's Handlers: 
It's treat a mental illness like a lifestyle choice day - to defile our culture, humiliate Americans, and destroy the United States.

Amit Shah (Parody)
@Motabhai012
·
Apr 1
This pretty much explains today's society
0:02 / 1:27
From 
NI𝕏N ✨
Samirah
@SameeraKhan
·
Apr 1
IT’S EASTER, YOU SATANIC IDIOT.

Literally NO ONE cares about your precious transformers.
Brick Suit
@Brick_Suit
·
Apr 1
A stray template appeared
wokeandwoofing
@wokeandwoofing
·
Apr 1
One of the hardest struggles facing  these deeply oppressed people  is that the very often get mistaken for rich straight white guys who have just put on a dress to flip the game, and climb straight  to the top of the victimhood pyramid.
C O M F Y F Я E И
@RealComfyfren
·
Apr 1
This is my least favourite jewish holiday
Christy Canyon
@ChristyCanyon11
·
Apr 1
For the first time in a long time, I have no words. I’d seriously had to look four times to make sure that this wasn’t a parody account….

Happy Easter to you and the First Lady

Ray
@raymo_g
·
Apr 1
Oh f$ck off
MatthewJshow
@MatthewJshow
·
Apr 1
The American people are just sick of the evil installed scumbag in the WH!"""

Donald_Trump = """
Hodgetwins
@hodgetwins
·
Aug 25, 2023
#NOTGUILTY #FREETRUMP
Alyssa Milano
@Alyssa_Milano
·
Aug 25, 2023
It’s a sad day for America.
👉M-Û-R-Č-H👈
@TheEXECUTlONER_
·
Aug 25, 2023
Dinesh D'Souza
@DineshDSouza
·
Nov 2, 2023
New statement by Trump on my film “Police State”:
Cherry 🍒
@cherrynorrishhi
·
Aug 25, 2023
God is with you! We are with you! We support you! We are praying for you! 

👉M-Û-R-Č-H👈
@TheEXECUTlONER_
·
Aug 25, 2023
The Patriot Voice
@TPV_John
·
Aug 25, 2023
Vernon Jones
@VernonForGA
·
Aug 25, 2023
God this guy makes me sick
Vernon Jones
@VernonForGA
·
Aug 25, 2023
RETWEET if you have President Trump’s back and are voting for him on November 5th, 2024.
CALL TO ACTIVISM
@CalltoActivism
·
Aug 25, 2023
Kari Lake
@KariLake
·
Aug 25, 2023
Mr. President, We are with you ALL THE WAY.

P a u l ◉
@ybarrap
·
Aug 25, 2023
Here is a validated summary of the facts about Donald Trump:

91 Criminal charges: Donald Trump is currently facing 91 criminal charges across four criminal cases[1][2].

26 Sexual assault allegations: At least 26 women have publicly accused Trump of sexual assault or harassment,…
Show more
Madeline Marie ✝🇺🇸🧡
@MadelineMarie66
·
Aug 25, 2023
Welcome back Mr. President ! 🤗🙏🏼🔥🔥

“But the wicked will die. The Lord’s enemies are like flowers in a field— they will disappear like smoke.” Psalms 37:20 

The Lions of Judah walk with him. God will never let you walk alone 🙌❤️
☘ The Sober Irishman ☘
@NCMuscleCars001
·
Aug 26, 2023
Zadok 💫
@zadokq244514
·
Oct 27, 2023
Good sir, brother, for your consideration..

The Patriot Voice
@TPV_John
·
Aug 25, 2023
Chris D. Jackson
@ChrisDJackson
·
Aug 25, 2023
I couldn't decide if I like this guy or not
Chris D. Jackson
@ChrisDJackson
·
Aug 25, 2023
Mickey
@Mickey17176
·
Mar 26
Chuzii
@itx_Humna
·
Mar 22
Well come back
ANUJ BANSAL(SEC.)
@ANUJ_BANSAL738
·
Apr 1
#DonaldTrump_FOR_WORLD_PEACE 
#DonaldTrump_FOR_US 
#DonaldTrump_AS_US_PRESIDENT
#ANUJ_OF_NarendraMODI 
@realDonaldTrump
 
@POTUS44
 
@POTUS45
 
@POTUS
 
@SecPompeo
 
@DrSJaishankar
 
@MEAIndia

TheRealJohnnyBravo
@BouchellJohn
·
Mar 25
Josh Franco

Three Year Letterman
@3YearLetterman
·
Aug 25, 2023
Jesus is literally behind you sir
Matt Wallace
@MattWallace888
·
Aug 25, 2023
⚠️ THE ELITE ARE NOT PREPARED TO HANDLE TRUMP’S WAR OF REVENGE AGAINST THEM ⚠️

🚨 IT WILL BE INTENSE

🚨 IT WILL BE CONCISE

⚠️ THEY WILL NEVER RECOVER ⚠️
Bobby Wirsing
@sbgbobby17
·
Mar 28
This recipe looks amazing! Can't wait to try it out, thank you for sharing this.

"Yum, this dish is making my mouth water! Definitely adding this to my recipe book."

Hodgetwins
@hodgetwins
·
Aug 25, 2023
FREE TRUMP
From officialhodgetwins.com
Zadok 💫
@zadokq244514
·
Jan 23
This guy is the man I love this guy
Zadok 💫
@zadokq244514
·
Jan 23
🇺🇸 National Revival #MAGA #AmericaFirst #USA #Trump #trump2024 by Zoomer Waffen
0:24 / 1:00
Elon Musk

@elonmusk
·
Aug 26, 2023
Approximately 10 million views per hour of this image
Dinesh D'Souza
@DineshDSouza
·
Oct 18, 2023
Trump is the primary target of the #PoliceState


Tomi T Ahonen Moved to Post, Spoutible & Mastodon
@tomiahonen
·
Jan 9, 2021
Hey Loser,

The riot is now being treated as a murder (the police officer). The ORGANIZERS will now be part of a murder. All who incited this deadly riot will be prosecuted

Including Rudy Giuliani
Including Don Jr
And including Donald Trump

You'll go to prison
Show more
Thoughts
@Thoughts7763
·
Feb 21
You can't trust people who have a history of flip flopping on issues (unless they sincerely had a change of heart through education and new information).  However, I wouldn't trust anyone who was onboard with mandatory COVID vaccinations (after the first 3 months), banning…
Show more
Carter Hughes
@itscarterhughes
·
Nov 20, 2022
ReFollowed President Trump. Lets make America Great Again and fire the democrats.
lukas.badboy
@lukasbadboy
·
Mar 27
Thanks for sharing, it''s appreciated.
The Trump Train 🚂🇺🇸
@The_Trump_Train
·
Feb 23, 2023
Who else thinks President Trump should come back to Twitter?

Share this tweet so he sees it!
David Hogg 🟧
@davidhogg111
·
Jan 8, 2021
Thoughts and prayers 🥳
NFTMint
@Lunimor
·
Mar 27
Thanks for sharing your perspective, it''s appreciated.
Junior
@JrMoneyGetting
·
Nov 20, 2022
the fact this was the last tweet is hilarious
Andy Cohen

@Andy
·
Jan 9, 2021
Take your toys and go to Florida, Sweetie.
luana
@Luiiih
·
Mar 27
Thanks for sharing your perspective, it''s appreciated.
Nathalia Magacho
@natibronzeri
·
Mar 27
Absolutely, and thanks for sharing.
greg
@greg16676935420
·
Nov 20, 2022
Welcome back donald. Dm me QUICK I have something to tell you
Duncan Jones
@ManMadeMoon
·
Jan 9, 2021
Can I have your ticket?
Real Defender🇺🇸
@real_defender
·
Nov 20, 2022
Welcome back Mr. President!
LAZAR
@Lazarbeam
·

ManuMenon 💙ProudImmigrant🇺🇸🇮🇳💙DemocracyFirst
@themanumenon
·
Jan 8

@Sundog512
·
Feb 15
You won’t be there on January 20, 2025 either. You’ll be pouting again.
mariana fernandes
@marianafernan91
·
Mar 27
You''re making a compelling case, thank you.
Maisa
@maisaber
·
Mar 27
Thanks for sharing, it''s appreciated.
Dom Lucre | Breaker of Narratives
@dom_lucre
·
Aug 2, 2023
Make ‘em hurt Mr. President. Give them the Tweet.
David Leavitt 🎲🎮🧙‍♂️🌈
@David_Leavitt
·
Jan 9, 2021
Trump is choosing to cry over his own bruised ego over helping to unite the country under our new leader by not attending the inauguration of 
@JoeBiden
♠️Audsauce♠️
@Audjuice9989
·
Nov 20, 2022
Welcome back Trump!
·
Nov 20, 2022
Disgraceful
"""

Anthony_Albanese = """
Jennacide🐈‍⬛🏴‍☠️🧁
@Jennacide12
·
7m
J.M. Cheer
@jmcheer1
·
2m
The military-industrial complex doing high fives. 
Making 'us' richer and safer? Surely not.
Leftwing Bastard
@_SocialDemocrat
·
6m
I was totally expecting the pile on.
Oz Wiltshire.
@OzWiltshire
·
6m
$1 billion As against $368 billion for AUKUS.
*
The program is forecast to cost $268 billion to $368 billion between now and the mid 2050s.

#GetInTheBin
Rusty Shackleford 🍉
@dyingforashit
·
5m
Yet none of that will cause you to raise the rate or do anything else for anyone in poverty. 

Glad you pulled the ladder up behind you, though.
Matt
@MattH093
·
9m
War criminal
Michael Bell
@disirregardless
·
7m
Great timing dude
Marc de Cazanove
@TchhhTchhhh
·
7m
NOT a defence deal. A war mongering deal!!!!!
mrs ceasefire
@m_aryel_len
·
5m
heart heart love
ayshilin
@ayshipie
·
8m
Read the damn room
Rob
@songdo101
·
5m
And the transparency you promised!
BreadMaker
@__BreadMaker__
·
1m
Wait ! I need those electrons for my air conditioner!
DMac
@bobbydoobla
·
4m
with parts imported from... Germany
Alan Hawkswood 🇦🇺
@VyperMk1
·
8m
So we are becoming arms dealers now?
AusPolMate Researched Threads & oddities
@AusPolMate
·
1m
Great work. 1,000 well paid Jobs👏👏
It's a great sign of hope that Germany and Australia can work so closely together. #Auspol
Wild man
@DredgeDiver
·
6m
No doubt a positive spinoff from Albanese commitment to genocide in Gaza.

ghost
@ghosty_gamin
·
11m
Cut all ties with china and Russia now!!
DILLIGAF666☠️
@DILLIGAF666_
·
9m
Mickamious
@MickamiousG
·
5m
Anyone else noticing whilst the economy is crumbling, Australian's are suffering through a cost-of-living crisis.... 
The World is spending billions on military equipment.... 
High Interest Rates... 
High Utility bills... 
But more is being thrown at winning defense work &…
Show more
Beach Bbq
@1AdjustedOp
·
2m
So $368 billion (AUKUS) minus the $1 billion for the deal you say you've just done.
Just another 367 billion and you'll be a break even.
I guess it's baby steps for you and Bowen 👏👏
From theguardian.com
The opinionated Black woman ~ Aunty
@Theblackfemini3
·
3m
Where are the parts being sourced from? 
China
Moira Deeming MP
@MoiraDeemingMP
·
5m
But will they be gender neutral?
RESPECT AUSTRALIA NATIONAL MATE 🇦🇺

FREE SPEECH ROCKS 👊🏼🇦🇺

2yy'zur2yyzubicur2yyzz4me
@notonmywatchfyi
·
5m
You better hope between then and now 🧐👀👀🥴 nothing reeves up !! -- just remember china has eyes on their prize by 2027 ... that means any where between now and then .
Maddy
@maddymadz83
·
1m
EXPEL THE ISRAELI AMBASSADOR NOW!!!!!
daria hextell
@rambleon26
·
1m
Here we go a defence export deal with Germany one of the Zionist best friends
Andy J
@AndyJay16634390
·
5m
This is starting to wreak of propaganda... Just get on with the job.
ChanChan
@ChanCha52615650
·
4m
A future built on war, seriously 🤦‍♀️ come on we can do better than this old mans paradigm. Everyone is broke so let's have a war!! NOT ON MY WATCH! GET WITH THE PROGRAM! Order of the new world. Out with the old.
zjalapeño
@zjalapenoo
·
19m
lockheed deal on or off?
0:02 / 0:07
FrustratedMelburnian
@belyndar
·
24m
Enough warmongering already. Enough!
LisaJPG 😷
@LJPG_23
·
3m
Of all days to announce something like this PM; tone deaf and no shame. Australia, leading country in manufacturing war weapons and machinery. Wow, I’m so proud (not)🤷🏼‍♀️
Jewy 🇦🇺🏴‍☠️
@jewy_420
·
2m
Resign.
Mimi Flâneur
@FlaneurCulture
·
3m
The question this raises, is why Germany, the largest manufacturing economy in Europe, can’t produce their own vehicles.
They deactivated nuclear power plants, NordStream was destroyed by their (and our) allies, & they are deindustrialising.
This should serve as a warning to us.
Maureen Doyle
@Maureendoyle52
·
1m
You are the greatest embarrassment we have ever had in Australia, yep, even eclipsed the dreaded Morrison. You now have the blood of the Aussie Aid worker on you hands as well. You are a craven coward, grow some balls and speak up against the Zionist in your party.
Alternative Aussie.
@Im_just_a_dude8
·
1m
So are we revving up some sort of war economy now?
WhySoFishy
@whysofishy
·
5m
Albo getting ready for war.
Margaret Wright
@nviolets49
·
3m
So will this contract prop up Netanyahu, the Zionists that are into genocide and supply weapons to the IDF  ? Just asking ??????
🎗️Allen Ivermectin Proud Assangist 🇵🇸
@UserHomey
·
3m
Go phukc yourself Albo!!!


Nick Engerer
@nickengerer
·
7m
Make Australia a Republic and end such nonsense!
SeverusVape
@SonicTulane
·
7m
When you actually read the words ‘his majesty the king’ you realize how wanky it is and ridiculous that grown people are still playing dress ups like this in 2024
Vicki Mainard 🇦🇺🕹🏀🐈
@vmainard
·
7m
The next GG that should sack you and your government before you bankrupt us. You are worse than Gough Whitlam, and he was sacked.
Dave 🔥
@DLiibertarian
·
7m
Great, an Activist as Governer General🤦‍♂️
Aussie Bot 🇦🇺
@AussieBotStudio
·
7m
The King also sucks up the climate cult nonsense. You’re a joke Albo.
three dogs
@threedogsonekid
·
7m
“A climate change and gender advocate”.
Tracey
@TraceyLee_07
·
7m
What a brilliant decision to appoint a climate change/gender equity activist. These are the top priorities for Australians, and it's about time someone took action. 🙄
Dave Jones
@eevblog
·
7m
Cool, but is the new GG willing to ensure that the government doesn't violate our civil liberties like what what happened during covid under the previous GG?
steven
@nogulagsagain
·
7m
Sam Mostyn never had a real job but she is rather described as a climate change and gender equity advocate. 

God help us !

Press ❤️ if you had enough of Albo and corrupt Labor.
Greg Barns SC
@BarnsGreg
·
7m
This is pathetic. In 2024 having to go to a foreign monarch to appoint his representative in Australia. No wonder we are not fully embraced by Asia 
@AusRepublic
Aus Integrity
@QBCCIntegrity
·
40m
Why are you not respecting the democratic vote of our referendum?

We don’t want UNDRIP Treaty or Voice in Australia.

Anthony Scalise
@esilacSynohtnA
·
3m
Honoured? …You wouldn’t know what that means. 
Samantha Mostyn is a washed up old bat. ‘Another’ poor move from you. 👎
X-ing
@crypto_vishu
·
5m
What era we living - seeking approvals from someone in UK to appoint our own governor - this arrangement and constitution is old and obsolete- not fit for any purpose other than keeping king tax funded. 
"""
Harley_Reid = """

Harley Reid is the #1 rated player for his age 🥳
Footy on Nine

@FootyonNine
·

Mar 25
"He's doing don't argues like a 200-game player."
"You've got to admire the way he's gone about it."

Mar 25
@footyfooty 
Not sure if this guy is gonna be the goat anymore?

Lloydy and 
@kanecornes
 praise Harley Reid's efforts, but implore his senior teammates to give him some much-needed support. 

#9FootyClassified | Nine & 9Now 🖥️
1:08 / 2:11
SEN WA Breakfast
@SENWABreakfast
·
Apr 1
came in strong off the top of the show this morning with the big BREAKING NEWS that Harley Reid has requested a number change 👀
The Uranium Bull formerly known as Rob ☢️🐂
@Cpcc15
·
Mar 31
Unpopular opinion Harley Reid won’t win the rising star


Matt Nicholls
@matt__nicholls
·
Mar 25
Harley Reid, West Coast.
Quote
Mjay💫
@7Vini_szn
·
Mar 24
Explain this in football terms.
SEN WA Breakfast
@SENWABreakfast
·
Apr 1
Tim Gossage tells us that Harley Reid has requested a jumper number change from 9 to 17.
Daniel Warland
@DanielWarland
·
Mar 31
Harley Reid’s team mates absolutely burning him at every opportunity. Hate to see it #AFLDogsEagles
Rubbish
@RubbishYCH
·
Mar 31
Harley Reid is going to be good… but right now… he isn’t..
Matt Craig
@MattCraigDT
·
Mar 31
Not sure if this is forbidden to say, but Harley Reid is looking like I would on a Saturday early in the season. Haven't seen him break out of a jog. #unfit
Brendan Foster
@BrendanfFoster
·
Apr 1
In some personal news, I’ve been made editor of the 
@westaustralian
. Harley Reid will no longer be on the front and back pages! :)
Jimmye
@Jimmyewest
·
20h
Round 3 Great week 2061 and in top 1k now 😎

✅ Gawn VC 177 🚀 
✅  Matt Crouch again 110
✅ Heeney (Brownlow)
✅ Khamis on field 💥

❌ Wilson 25
❌ Howes 26
❌ Harley Reid 54
(Thankful for best 18)
Show more
TheBreakevens (Corey)
@BreakevensPod
·
Mar 31
1932 with Massimo to play. Harley Reid my lowest remaining score with 54, unless Massimo goes large looking at 1950+. #SuperCoach
SportsbyFry
@sportsbyfry
·
Mar 26
Power Ranking 2024 #AFLFantasy Cash Cows Round 2 💰🐮

1. Matt Roberts ⬆️ 1
2. Colby McKercher ⬇️ 1
3. Blake Howes ⬆️ 1
4. Ryley Sanders ⬆️ 1
5. Ollie Dempsey ⬇️ 2
6. Jeremy Sharp ↔️
7. Zane Duursma (NR)
8. Darcy Wilson ⬇️ 1
9. Harley Reid ⬇️ 1
10. Caleb Windsor (NR)
Show more
Grandy Promenade.
@RCT_10
·
Mar 31
"A goal to Harley Reid would get this crowd up and about" - Kelli is just voicing my thoughts on national TV now
Anthony Christodoulou 🐀💧🇦🇺🇨🇾
@AnthChristo
·
18h
Anyone else toying with the idea of trading down Harley Reid? #supercoach
Ben Hansen

Is this as true as Harley Reid not going to West Coast??
Tony
@acpea1989
·
Mar 31
The way West Coast looked today, there is a great chance that Harley Reid is going to pull a Horne-Francis and leave at seasons end.  #AFLDogsEagles
Ben Nexhip
@ben_nexhip
·
Mar 29

Sam Mclure said there’s no possible way Dustin Martin was playing at Richmond this year, he said confidently that West Coast would not take Harley Reid. No credibility whatsoever
luke
@LukePH10
·
Mar 25
Harley Reid being completely shit on by footy supporters already. God this is exhausting
Tim Gossage 🤓
@TimGossage
·
Mar 25
The promise of more transparency in 2024 continues with five players being made available to local media at club HQ tomorrow. 
And before you ask Harley Reid and Jack Darling are not amongst the five.
Hunt, Jamieson, Duggan, Edwards & Hough.


Hans Mücke
@reallyrealhans
·
Mar 27
'Almost untackleable': West Coast Eagle Harley Reid's fend-offs leave teammates in awe https://afl.com.au/news/1095325/almost-untackleable-west-coast-eagle-harley-reids-fend-offs-leave-teammates-in-awe #afl
From afl.com.au
The West Australian
@westaustralian
·
Mar 25
West Coast coach Adam Simpson has defended The West Australian’s coverage of star draftee Harley Reid.
From thewest.com.au
Lachlan McKirdy
@LMcKirdy7
·
Mar 28
West Coast supporters when Harley Reid made that run down the sideline against the Giants. 

#AFL
Quote
×
@5edicii
·
Mar 27
there is no scenario where he needs to be doing all that
Bobby
·
Mar 31

@PiesWrldd
Also good luck retaining Harley Reid past his contract.
CJ 🇦🇺
@stevosfooty
·
Mar 31
feel so bad for Harley Reid just let him go to Geelong where he would love and get heaps of Geelongs picks and players for it
Andrew
@giltius
·
Mar 31
Save your money Bombers, Harley Reid available in 2 years
Mark Duffield
@MarkDuffield1
·
Mar 31
What West Coast must do to keep Harley Reid in Perth
From codesports.com.au
Checkers from Marmalade
@marmalade_aus
·
Mar 31
Harley Reid matching up on the Bont
Jayden Hunt and Naughton with the headbands 
Tim English taking running bounces through the middle 
JJs hair looking super schlick 

You wouldn’t think Western Bulldogs vs West Coast would be all that exciting but it’s genuinely got it all
yxngbukayo1
@yxngbukayo1
·
Mar 31
If I was Harley Reid I would’ve rather been drafted into the army
Sambo1600 G
@GSambo16
·
Mar 31
Would love to see Harley Reid move to halfback, clearly doesnt have the tank to be full-time mid. Let him get use to feeling the ball. #afldogseagles #AFL
Des Doherty

@GeoffHutchison
Geoff if you do that you won’t know if Harley Reid breathes in or breaths out.
Adze
@leafy17
·
Mar 25
I don't know who has got a tougher job... 

Every member of the media desperately vying to suck Harley Reid's dick 

OR 

Harley Reid's dermatologist?
Quote
Daniel Garb
@DanielGarb
·
Mar 24
Eagles have been better than scoreline suggests but getting killed in the ruck. No choice but to keep Bailey Williams in there.

Sam Taylor enormous, again.

Harley Reid is mind blowing for a 2nd gamer. He’s happy in Perth but WCE need to get better fast to keep him after 3 yrs.
Show more
coby hewitt
@cobyhewitt1
·
Mar 31


She just said ohh bad miss by Harley Reid ,,, it was Gibney
96FM Perth
@96FMPerth
·
Mar 26
What Elliot Yeo said to Harley Reid seconds before THAT early play down the wing 💙 💛  | 🎧  Listen here! >> https://bit.ly/4a8pu6g #clairsyandlisa 
@elliotyeo6
 
@WestCoastEagles
 #westcoasteagles #perth #AFL #podcast
 
 
Rod Smith
@RocketSmith1985
·
Mar 27
Do not compare other areas with Colby McKercher….. he smashes Harley Reid
John cena
@Johncen16437480
·
Mar 27
Only w your shitty club will get wont make a difference tho will still be 18th next 10 years


Rod Smith
@RocketSmith1985
·
Mar 27
Harley Reid won’t make it…. Not fit enough


Demitri christou
@ChristouDe60816
·
Mar 27
I mean anything that says the Eagles are pathetic and Harley reid probably won't stick around


FreoGirl 🇦🇺💙🖤🤍💜🇦🇺
@FREOGIRL
·
Mar 27
He may be an ok up and coming but so far not matching with the other top picks.. Hes been close to the worse pick in SuperCoach which is mostly based on hard ball gets, pressure & efficient use of the ball. Do the talk do the walk.
Shauna Dale 🐋
@ShaunaDale18
·
Mar 27
How wonderful
Tandy
@ATeeL
·
Mar 27
Let's go boyyyyy
Rod Smith
@RocketSmith1985
·
Mar 27
Harley Reid what a superstar of the game!!!!!


Footy Nut
@agsirr_sirr
·
Mar 30
Any danger of performing tomorrow?


Pepsta
@Pepsta3
·
Mar 24
Let’s go Harley!! 💥
Andrew Carter
@AussiePunter32
·
Mar 25
He is, everyone who’s dealt with him at the club including the general staff all say the same just a genuinely decent nice country kid & he’s had a full year of dealing with the constant media so he copes with it well. Apparently all our kids are really good decent human beings🙂
Caprh Cap
@Caprah112
·
Mar 24
He seems a genuinely good guy. Just hope eagles fans have realistic expectations for him as he gets more experience
Jennifer Brock
@LALLI2024
·
Mar 25
Very creepy obsession with a very young man
Is a 12 year old girl running this page?


wulth
@wulth_
·
Mar 21
those clearances 🤌💋

wulth
@wullywool
·
Mar 21
Oh my he's good
@whughjackyjacky
·
Mar 21
Never seen someone more overated
@lightweightbby
·
Mar 21
How bout those marks
@wdidhetho
·
Mar 21
Did he get a touch all game

@wdidhetho
·
Mar 21
I think he's my dad


"""

Miley_Cyrus = """


Antonio José De Santis
@maga10
·
Mar 6
Aloha!!!!👋👏👋👏👋👏🍓❤️🌹🌷🍬. Psntd.
PowerRanger-X 
@powerranger_x
·
Mar 6
Absolutely Exceptional, Miley is sexy to the core. I actually had a dream of her yesterday or today, while I was sleeping. How awesome, no joke ,
Isa Massi
@Isa_Massi
·
Mar 6
That a girl Miles!!! 😍😘❤️🌹😇
Antonio Mautor 🎸
@AntonioMautor
·
Mar 6
QUEEEEENN.
Investorsaurus 🔺
@Investorsaurus2
·

Mar 6
U look stunning in this campaign best of luck D&G
Miley Nation
@MileyNation13
·
Mar 6
Lookin' like a model who just got a check ✨
Love Dogs
@LoveDog910
·
Mar 28
Looking at these sunglasses makes me want to throw out all my old pairs and start fresh! #DGEyewear
Huyền Châu Offical
@HChauOffical
·
Mar 29
Absolutely stunning photos! Can't decide if I'm more in awe of the eyewear or the photography skills. Amazing work!
Fear Queer Horror Guru
@fearqueerhorror
·
Mar 7
Love it queen 
@MileyCyrus
 #MileyCyrus #DolceGabbana #DGEyewear
AIDE
@AIDE_DePIN
·
Mar 29
Can't see myself affording those designer sunglasses, but I can definitely admire them from a distance. DGEyewear
thiago
@httpsrealitys
·
Mar 6
GOOOOOO
FLOWERS🌺
@Flo_Hauz
·
Mar 7
Love the looks! Those frames with the clear lenses look sooo good !
Isa Massi
@Isa_Massi
·
Mar 7
I'm glad that 
@MileyCyrus
 finally buried the hatchet with 
@taylorswift13
 .  They have so much in common, it would be a shame if they couldn't be friends over a misunderstanding. You ladies rule the industry now so kiss and make up 👄💕👄 🤠
Amazon Music
@amazonmusic


Princess Marie 🎀 Findom
@send2marie
·
Mar 6
This is so hot, Miley omg!
Miley Edition
@MileyEdition
·
Mar 6
These photos are insane 🔥
Quote
Miley Edition
@MileyEdition
·
Mar 6
Miley Cyrus x Dolce & Gabbana 😍❤️
Mike Wilkinson
@wilkystorm
·
Mar 6
you are so f*ing hot
Khalid
@khalidauad
·
Mar 6
WE NEED THE SONG ON SPOTIFY
Miley Cyrus Brasil | Fan Account
@MileyCyrusBR
·
Mar 6
Queen of glasses 
·
Mar 29
The song is literally perfect ♥️
Show replies
Miley Edition
@MileyEdition
·
Mar 29
TWO LEGENDS!! Its literally so perfect!!
Quote
Miley Edition
@MileyEdition
·
Mar 29
II MOST WANTED
BEYONCÉ, MILEY CYRUS
OUT NOW!
0:04 / 0:14
Miley Cyrus Brasil | Fan Account
@MileyCyrusBR
·
Mar 29
WE NEED AN LIVE PERFORMANCE 🩶
MTV
@MTV
·
Mar 30
THE SONG IS SOOOO GOOD
𝗱𝗮𝗻𝗻𝘆🫧💚
@beyoncegarden
·
Mar 29
OH EXACTLY MILEY AWWW😭😭😭🥹🥹🥹
gucci bucket hat.
@Unapologetic_Z
·
Mar 29
BEYHIVE LOVES YOU MILEY!!!
Verizon
@Verizon
·
Mar 29
The queen isn’t the only one with bars 📶
Show replies
Josh P. Jackson
@JoshJay990
·
Mar 29
We LOVE YOU 
@MileyCyrus
  You and 
@Beyonce
  out healing magic ❤️‍🩹 ✨ in this beautiful ballad!
thiago
@httpsrealitys
·
Mar 29
BEST DUO EVER ❤️❤️❤️❤️❤️
(((Tara Dublin))), Rock Star Author 📚❤️‍🔥🤘🏻
@taradublinrocks
·
Mar 29
I love this sisterhood so much #COWBOYCARTER
𝔏𝔢𝔞𝔥 ☾☀︎
@redforjanet
·
Mar 29
THE LEGENDNESS JUMPED OUT?!
Quote
𝔏𝔢𝔞𝔥 ☾☀︎
@redforjanet
·
Mar 29
Hearing Miley & Beyoncé on the same track has to be my favorite part of the night, honestly. They meshed into one right before my ears.
0:02 / 0:05
Khalid
@khalidauad
·
Mar 29
MOTHERS
YouTube Music

@youtubemusic
·
Mar 30
this song is IINSANE omg 😭
lex in tx
@alexissTyler
·
Mar 29
Hope you’re on the next album 💿💿 now playing “angels like you


vini
@viniwho
·
Mar 29
Love u so much, so happy to see everything u are achieving ❤️
Miley Cyrus Media
@MileyMedia
·
Mar 29
you both were amazing, love YOU & the song so much, we’re so proud of you MC🤍
Morphe
@MorpheBrushes
·
Mar 29
SCREAMING AND CRYING RN 😭
Niamh🥀 (Fan Acc) 𐚁
@msyonceslay
·
Mar 29
Yes Miley we love it 🥹🥹🥹🥹🥹
Miley Cyrus Brasil | Fan Account
@MileyCyrusBR
·
Mar 29
QUEENS 💕
II PURE WANTED HONEY 🍯
@purethiquekj
·
Mar 29
if you only knew how long i’ve dreamed about this collaboration, i’ve been a fan of the both of you since 2014 and y’all truly made me be the person i am today, i’m so proud and grateful 🤍
RockLey
@ObsessedSmiler
·
Mar 29
MOTHER YOU ATE OMG

Goonica Denise Arnold
@goonica_denise
·
Mar 29
babygirl the singing you put down on this one here

Miley Cyrus Brasil | Fan Account
@MileyCyrusBR
·
Mar 29
WE LOVE U GIRLS 🩷
ε☥εrηαﾚ ♕ 🥋
@s0urpatchkiid
·
Mar 29
easily one of my favorite songs i can’t wait to see this live you ate queen
𐚁 onii 𐚁
@__Onixivy_
·
Mar 29
MILEYONCÉ STANS WINNING!!!!!!
ReneighRidingBey 𐚁
@Bey_riding
·
Mar 29
Love you Miley
lesego. 🪩 (fan acc)
@LeeLovesBey
·
Mar 29
the song is so amazing 🥹 we love you miley
God is a woman (Sam)
@godisyung
·
Mar 29
Everyone get up!!!!!!!! STREAMMMMMMM
VIEW$
@viewsxpic
·
Mar 30
Yoooooo!!! This is where The  Original Shirt Link guys 🔥🔥🔥
#COWBOYCARTER
From anyimage.io
Mela Yela
@_melayela_
·
Mar 29
Period.”"""


Jake_Paul = """


VeVeMeister 🎮
@Der_Vevemeister
·
13h
Will your fight versus Tyson be real? Or a show fight? I'd really like to know.
suga /// xxx47.eth
@sugaFreeFC
·
13h
Better be ready for $MYKE 
@MykeThysenSOL
AJ
@AST_ute
·
13h
Sorry thats incorrect, this is the joint worst MVP Prospects card (along with number 2). The others were either headlined by Ashton Sylve, Amanda Serrano or Jake Paul.
Kimbo_Sabbi
@Kimbo_Sabbi
·
13h
Exhibition fight against a 60 year old man is not real boxing or any contribution to boxing in any way, shape or form. Its a circus show 🤷🏻‍♂️
HahaSoha
@Haha_Soha
·
13h
Ready to watch some NCAAW games, but let's be real, I'll probably spend half the time yelling at the screen and the other half marveling at these athletes' skills. Win or lose, they've already won our hearts and kept us entertained. Cheers to them, and to us fans who ride the…
Show more
Jimmy McCambridge
@JimmyMack0320
·
13h
Jake Paul taking his expo fight with Tyson more seriously than 
@RyanGarcia
 is for Haney.
Gordon
@AltcoinGordon
·
13h
When are you fighting the pensioner?
James Dylan
@dylonmusk_
·
13h
Play the game boy
@betr
Devotions
@GodlyDevotions
·
13h
Praying for a blessed day for everyone reading this 🙏 ❤️
FanScorecard
@fanscorecard
·
13h
Jake always brightens my day!

.wm
@W_M_T_V_
·
13h
KSI owns you dawg
J Stewart
@triffic_stuff_
·
13h
Thoughts on this Jake?
Quote
ksi
@KSI
·
15h
I’m back baby! Fighting 75 year old legend and former champ. Don’t worry, age ain’t nothing but a number. Forman hits harder and is faster than ever before!
Truth Seeker
@TheKingofJewelz
·
13h
this guy is launching
Lezra Gomez
@lezramgomez
·
13h
is this guy the goat
khid hb
@finestkhidhb
·
13h
We are watching👀
Jmag
@Jmagings
·
13h
April Fools!!
Geeky Glimpse
@GeekyGlimpse
·
13h
😎😎
SENYO
@ItsTheD0n
·
13h
Wasup
(W or B)ill
@Slickwilly617
·
13h
Bro angel reese is not lettin you hit
Michael Kentrell Brown 💚ﾒ𝟶
@breezybetter07
·
13h
Is that it? Is that the tweet you’re going with? Wow! As your biggest fan since 1947, I’m not impressed. You know, when it comes to expressing your thoughts on Twitter, you have the freedom to use up to 280 characters in a single tweet. It's incredible to think that there are…
Show more
TrRonaldo
@TrRonaldoCR7
·
8h
1 bitcoin ı need 🤲🏻❤️
____________
@KazzeeJ
·
12h
you to busy looking for fights in the retirement home 😅
Nikita Grokovich (Parody)
@GrokovichNik
·
13h
Try to beat this guy 😎


dan deitz
@dandeitz2
·
13h
To bad you can’t be like that for boxing fans
Emerge
@akaEmerge
·
13h
I don't want to lose anymore money on Jake 
Pay Levi Rogers using PayPal.Me
Go to paypal.me/LeviRogers and type in the amount. Since it’s PayPal, it's easy and secure. Don’t have a PayPal account? No worries.
Иван Рыбачук
@ivanrybachuk
·
33m
Hello Jake✌🏻
Heidi Fawcett
@fawcett_he82331
·
13h
Hi jake tell logan i said happy birthday
Joe
@JoeBets007
·
13h
Put it on betr
Kade
@5sKade
·
13h
Let’s go champ
Blinkx117x
@John117Jackson
·
13h
Geaux Tigers!
Mariano
@Nanovargas44
·
13h
Fight a boxer
Luke Jarrett
@LukeJarrett1892
·
13h
Ur just ksi’s pet
$GME
@smoke24356
·
13h
Yuck tweet
Human
@BloodRawTruth
·
10h
hi my name is jake paul, Im a feminist, please pay me
carmi🇬🇧
@Holywarsenal
·
13h
Has anyone noticed he tweets after ksi violates him 😭 bro acting like he don’t see it
.
@AXDVEmzGgN25234
·
13h
We ain’t watching them dishwashers 😭😭😭
GAKJellybean jill
@AshtonPillow3
·
11h
How much they pay you to say that?
Infamous
@_Mo2001_
·
13h
W for fighting old age pensioners Jake
Justin
@JKINGS314
·
12h
You take roids
DanaGoated
@DanaIsGoated
·
13h
Nobody watching it like your fights 😂


Devotions
@GodlyDevotions
·
17h
Praying for a blessed day for everyone reading this 🙏 ❤️
dewrld 🇳🇿
@dewrlddd
·
17h
We good
mistress💦
@ittybitty0titty
·
17h
Sounds like a stacked lineup! Can't wait to catch the action live on 
@DAZNBoxing
. Orlando is going to be on fire! 🔥🥊
TENBOXING
@Aus10Boxing
·
17h
This guy do be a lil fire
Die Hard Philadelphia Fan!
@Allday215757
·
17h
If you want ppl to take you serious in boxing why not fight, Tank, Canelo, Danny Garcia, Devin Hainey. Shoot I’ll even take Caleb Plant. But you continue to fight ppl with no boxing background or washed up UFC fighter. The REAL boxing community take you as a joke.
Liam Lazarus
@TheLordsLegion
·
17h
More real than your fight against Tyson.

Tim Childers
@omiherd
·
16h
Ohhhhh Yea Gotcha Belt lol lol lol
youtube.com
Gotcha Belt
Boxing music Paul/Tyson fight #veve #veveverse #nft #vr #meta #omi #boxing
Master_class
@Masterclas66394
·
16h
Nobody knows who these ppl are?
Olivia Kaya💕
@oliviakayax
·
16h
im not watching a bunch of nobodies box each other

"""

Taylor_Swift = """
odatrus (Taylor’s versions)🤍
@helltonrds
·
19h

 my Facebook account got hacked and suspended. How do I get my account back 😿
monsieurfalls
@MonsieurFAlls
·
19h
Finally, some new music to drown my sorrows in... Can't wait to cry and sing along to THE TORTURED POETS DEPARTMENT!
Pol vale
@Polvale2
·
20h
Can't wait to dive into this album and explore the highs and lows of love and poetry. April 19th can't come soon enough!
عبدالله الزهراني
@zwzzssksxx1
·
19h
Can't wait to dive into this poetic masterpiece, I've been needing some tortured poet vibes in my life! April 19 can't come soon enough.
NaaShiwis Bear
@BearxFromMARS
·
20h
Can't wait to dive into THE TORTURED POETS DEPARTMENT album on April 19! Who knew love and poetry could be so entertaining?
Koch Toshia
@KochClaudeg
·
18h
Finally, an album that speaks to my tortured soul! Can't wait to drown myself in poetic despair. April 19 can't come soon enough.
NaaShiwis Bear
@BearxFromMARS
·
21h
Can't wait to listen to the angsty sonnets and heartbreak ballads on THE TORTURED POETS DEPARTMENT album! Love a good poetic cry session.
PeterinLA
@PeterinL57476
·
19h
Can't wait to dive into the poetic drama! April 19th can't come soon enough. Love and poetry - what could go wrong?
Felipe Soto
@FelipeS86385650
·
19h
The album THE TORTURED POETS DEPARTMENT explores the depths of love and emotions beautifully. Can't wait!
dany fun
@danyfun66
·
23h
Finally, an album for those of us who can't express our feelings in a normal way! Can't wait to hear it.
Vítor Gomes
@gomes_vtor
·
19h
Excited to dive into this poetic rollercoaster! Hoping it doesn't leave me too tortured...well, maybe just a little. ?
Vinyl Vogue
@VinylVogue
·
19h
Taylor, you're a true inspiration! I'm launching a record store to support local music programs, and I'd love your support. Let's keep the music playing for future generations! ￼￼
cami punta
@camuflageee
·
16h
Can't wait to dive into the angsty, heart-wrenching lyrics of THE TORTURED POETS DEPARTMENT. Finally, a soundtrack for my dramatic love life!
alexis
@the_alex_x15
·
19h
Can't wait to dive into this album and get my heartbroken by some soulful poetry! April 19 can't come soon enough.
Vítor Gomes
@gomes_vtor
·
19h
Can't wait to dive into THE TORTURED POETS DEPARTMENT album! Love and poetry – hopefully no heartbreak songs on there! April 19 hurry up!
Cotting Boughey
@CottingLuds1
·
19h
Can't wait to dive into this new album and explore the tortured souls of the poetic world! April 19 can't come soon enough.
alexis
@the_alex_x15
·
19h
Excited to drown my sorrows in some poetic melodies! Can't wait for THE TORTURED POETS DEPARTMENT to drop on April 19.
محسن البلوي
@zpweiheng
·
19h
Can't wait to dive into the poetic depths of THE TORTURED POETS DEPARTMENT album! Love and heartbreak never sounded so good.
s🤍
@messuwanted
·
19h
Looking for tickets to buy ERAS TOUR 2024 TAYLOR SWIFT EUROPE
selene soledad
@selenesoledad
·
19h
Can't wait for the new album! The Tortured Poets Department sounds like it's going to be amazing.
Carlo
@blacksprawl
·
22h
Can't wait to dive into the emotional rollercoaster of THE TORTURED POETS DEPARTMENT album. Love and poetry, what a perfect combo!
AIDE
@AIDE_DePIN
·
19h
Finally, an album for all us heartbroken wordsmiths out there. Can't wait to drown in the sorrowful melodies.
Beautyass
@AssBeautyass
·
19h
I can't wait to hear the emotions poured into this new album from THE TORTURED POETS DEPARTMENT.
Nghĩa Bùi Khắc
@khacnghia2902
·
19h
I from VietNam ❤️❤️❤️❤️❤️
hamtaro/e
@ON9CCSeng
·
16h
Can't wait to dive into this emotional rollercoaster of a album! Grabbing tissues and preparing for all the feels.
sunkwa ransom
@sunkwaking
·
19h
I can't wait to dive into THE TORTURED POETS DEPARTMENT, I know it's going to be amazing!
Koch Toshia
@KochClaudeg
·
23h
Can't wait to dive into this album and drown in some poetic anguish. April 19 can't come soon enough!
DJ🏳️‍🌈🇺🇦
@DJ9035617762581
·
21h
Can't wait to get my hands on this! Finally, a soundtrack for all my dramatic relationship woes. Poetry and heartbreak, music to my ears.
Pol vale
@Polvale2
·
23h
Just what I needed to elevate my emo vibes! Can't wait to drown in the sea of tortured poet feels. April 19, hurry up!
elleffe
@elleffe_
·
19h
Finally, a soundtrack for all of us tortured souls out there! Can't wait to make my dramatic poetry readings even more dramatic with this album.
tolga erpik
@tolgaerpik
·
19h
I can't wait to listen to THE TORTURED POETS DEPARTMENT album, love Taylor Swift's artistry!
luana
@dtygghgfdry
·
19h
You''re contributing meaningfully, thank you.
İlkbahar
@lkbahar90045406
·
19h
Finally, a soundtrack for my deep, melodramatic soul. Can't wait to drown in poetic angst.??
hema emam
@10HeMaEmAm
·
17h
Finally, a soundtrack for all those emotional rollercoaster moments! Can't wait for THE TORTURED POETS DEPARTMENT to drop on April 19.



One Bad Dude
@OneBadDude_
·
16h
You look eerily similar to the daughter of the founders of the church of Satan.
Laza
@Laza43805690
·
16h
Taylor Swift's Eras Tour spans three and a half hours, featuring hits like "cardigan" and debuting four new tracks.
Drake__Just
@Drake__Just
·
16h
I can't believe I can now watch all of Taylor Swift's incredible performances whenever I want!
zinabe
@zinabe7
·
16h
Absolutely, and thanks for sharing.
JML_ 🐉 $MON 🕹️ $RCADE
@Omnifii
·
16h
screenshot this if you love taytay

Cant wait to watch you on disney plus


roselin carrera
@CarreraRoselin
·
15h
Agreed, thanks for sharing your thoughts.
matheus andrade
@teuteuandrade
·
15h
I can't believe I can now stream all 3 and a half hours of Tay Tay's concert on Disney Plus! Can't wait to listen to all of her new acoustic songs.
maria fernanda
@MariaMafedipa
·
15h
Agreed, your perspective sheds light.
donalduck
@donalduck_
·
15h
Spot on, I couldn''t agree more.
luis madden
@LuisMadden
·
15h
Absolutely, thanks for your contribution.
aleymar delvalle
@aleymar_0709
·
15h
Appreciate your comment, thank you.
omar bravo romero
@bravosambigotes
·
15h
Agreed, thanks for sharing.
marcos victor
@lupusssgc
·
15h
You''re making a strong point, thank you.
esmeralda chacon
@echacon12
·
15h
I am absolutely obsessed with Taylor Swift's acoustic songs from The Eras Tour on Disney Plus! They are pure magic.
BaseMan
@BaseMan14
·
15h
I am so excited to stream Taylor Swift's The Eras Tour on Disney Plus. It's a must-watch!
Laza
@Laza43805690
·
15h
Taylor Swift's The Eras Tour would be an incredible experience, showcasing her evolution as an artist over the years. With performances including hits like "cardigan" and four new songs, fans would be transported through time and get a taste of Swift's incredible musical journey…

"""

Lebron_James = """


Troy Weaver
@DanCampbellGOAT
·
7h
He’s just lucky he isn’t coaching you! We all know what you do your coaches 😒
Shivaye 🔱
@shivaye01
·
8h
The richest man in the world.. 😊
0:03 / 0:20
From 
Buitengebieden
Stagy
@UtdStagy
·
8h
The NBA wouldn’t be the same without you.
Stagy
@UtdStagy
·
8h
King!

@RansomPLS
Havoc Energy Drink
@tryhavocenergy
·
8h
Is he in fortnite tho?!?
sush
@2sush
·
5h
keep going on and keep blessing us 🙏
DIRTI.SEI
@Dirti_SEI
·
8h
dirty dog
cryptoknight
@cryptoknig65902
·
8h
goat👏👏👏👏👏
Wealth Turtle 💰 🐢
@wealth_turtle
·
8h
He’s definitely not perfect
Stagy
@UtdStagy
·
8h
Please don’t retire anytime soon 🙏🏽
MicahParsonsSZN ™
@ParsonsTakeover
·
8h
No diddy KING
Emmanuel.
@T_ee_mex
·
8h
What you doing bruh
Jairo Nehemías C.I.
@Nehemias77Cas
·
4h
The one english comment your looking for
Stagy
@UtdStagy
·
8h
God bless you
Adrian Wojnarowski ᶠᵃⁿ
@wojdespn
·
7h
Lebron pls check your dm's from me
Made In The World
@dekunleaa
·
8h
skippa lebron james is ma captain
Vladan
@Vladan48186430
·
4h
Who else is out here speaking fax about lebron like me
büşra akyüz
@braakyz8
·
4h
Goatest player of all time he's my man
𝐌𝐀𝐋𝐈𝐊
@Maleekback
·
7h
Lebron the Goat
pearl
@pearl1541253
·
8h
Such a cute Guy 😍💕💕💕💕
Sparkle
@sparkle0100
·
8h
Legend
MicahParsonsSZN ™
@ParsonsTakeover
·
8h
He looks like you KING
Teeshineee
@Teeeisback
·
7h
He's handsome too
Aslıayber
@marionnettea
·
4h
That doesn't even make sense
saif
@saif5553333
·
8h
Nice game tonight lebronto
Sparkle
@sparkle0100
·
8h
King 🤴


Wealth Turtle 💰 🐢
@wealth_turtle
·
8h
He’s lowkey ugly
andrea🧎🏽‍♀️
@scarydrea
·
8h
this is such a nice way to flirt with him
Jenn 💋
@ohmcrae
·
8h
Goat
Quote
𝐔𝐑𝐀𝐍𝐔𝐒 ⭐️
@uranuscertified
·
Mar 29
Jenn — 𝟐 𝐝!𝐞 𝟒 (ft. Foreign, houston, nick, URANUS & val)
ﾒ
@w5w99
·
8h
wait wait wait this is the guy
Quote
ﾒ
@w5w99
·
Apr 1
Eyatsu Massager for Neck and Back, Cordless Electric Massager, 5D Deep Tissue Massage Pillow for Shoulder

430 Ratings ⭐️⭐️⭐️
౹ Above 2000 Sold

https://s.click.aliexpress.com/e/_DmDA6Vf
Show more
0:06 / 0:36
Candice
@BOOGIE7278
·
4h
Just like his Pops right? Congrats Coach!👏🏿👏🏿💐
Demetrius Russell
@Meech330BBG
·
6h
🙏🏾
CR7GOAT7
@goat7_cr7
·
8h
U r my sunshine
Tom Foal
@GetBaitedSir
·
8h
AYOOOOOOO
DRE
@DADDYD_118
·
7h
PED’s
daniel Lucky
@luck43130
·
41m
$LBRN TO THE MOON 🚀🚀
Robert Bowe
@bobbybowe66
·
5h
That’s a Great Irish name Joyce we’ve had 
@DuqMBB
 to visit 
@ashfordcastle
 before I think it’s time again You don’t know where your going until you know where you’ve Come from nearly every cornerstone of US business, education, and sport, was laid by Irish Immigrants 🏰❤️☘️🏀😎
 
 
earl
@crackloverrr
·
3h
bronny goin there fosho
dreaaa 🫦
@jsllybeans
·
3h
i wish i was born in this type family
OED
@oyedun_emiola
·
3h
That's a wrap thumbs up
THEO🗽
@theo4982
·
3h
you are my SUNSHINE
The Barkhan times
@theBarkhantimes
·
3h
Bronny going to Dusquesne confirmed
 

C🎱LE (2-0) ITS ⚾️ SZN‼️‼️
@ownedbychoppa
·
3h
BRONNY TO DUQ ‼️‼️‼️
JoeMess
@THEEJoeMess
·
3h
Uh oh . Would be WILD
TheBlackOffice
@TheBlackOffice2
·
2h
Stop already smh
Josh Noah
@JoshuaNoah21
·
2h
#nodiddy #Diddler
𝓚𝓪𝓶𝔂𝓪𝓻 💎👑
@lakeshowbronc0
·
3h


is this your king why not?
·
3h
Bronny definitely transferring there


Key Emerson
@KeshaunEmerson
·
2h
Welp
Ken Hill
@KenHill11
·
2h
I admire how you always show appreciation, support, and loyalty to your family/friends and kids from Akron/Cleveland  & Columbus, Ohio. I am sure you've shared some plays/ ideas & tips with him already. Respect 👍🏾👏🏾
t/a Pennflex Global Marketing
@Pennflex_GM
·
40m
The King has spoken 🙌
 
 """

Billie_Eilish = """
Billie Eilish Brasil
@BillieEilishBR
·
Mar 30
ok…
General Strike 🍀(Terrence Daniels)
@Terrence_STR
·
4h


·
Mar 30
Ok
David Krepps
@dnk900
·
Mar 30
YES!
Derrick Anoa'i
@WWEderrickanoi4
·
Mar 30
Awesome
Daniel 🎨
@Makjesty
·
Mar 30
Milli Billie Irish Eilish 🫶🏾✨
Tony
@bloodylikeabody
·
Mar 30
IT’S BEEN 5 YEARS?
thomaz
@thisdracarys
·

Billie Eilish Spotify Data 📊
@billiestreams__
·
Mar 30
genius album ending
Billie Eilish Spotify Data 📊
@billiestreams__
·
Mar 30
billie now be3 please
moony
@st0pbeingflirty
·
Mar 30
WHAT NOW?!
@KxngPlayzYT
·
Mar 30
We would like to celebrate the new album
Quote
kxng
@KxngPlayzYT
·
Mar 29
My debut single “When I Thrive” is officially out now!

(Official Lyric Video)

On1 Culture ©
@On1Culture
·

@therrese_
·
Mar 30
clean
@EgheFamous
·
Mar 30
AOTY for a reason!

$BLOCK $PARAM $TRIP
FeelTheMusic
@feelthemusicglo
·
Mar 30
Yes!🏆🚀🎶🫶👌
Quote
Teslaconomics
@Teslaconomics
·
Mar 7
Yo quiero un Tesla en Argentina 🇦🇷

cardoso
@cardosojr1999
·
Mar 30
Libera mulher
Billie Eilish Daily Spotify
@BillieSpotify_
·
Mar 30
We want to celebrate with new music! ❤️
Darrien Lestrange⚡️
@Darrienprkr11
·
Mar 30
Wow, been playing tf out of this for the past week lol 



moni ❧
@dsambitch
·
Mar 30
girl bye.
ally ౨ৎ
@asheseilish
·
Mar 30
count ur DAYS
be³ era
@thebe3era
·
Mar 30
MOVE BILLIE MOVE
Angie
@itisangiec
·
Mar 30
will always be my favorite album 🖤
x
@KyleAMitchell
·
Mar 30
i remember this, wait, what is it?
Mark G
@MarkG52480690
·
Mar 30
You’re the best at doing you… so keep doing you’re
かみ
@paperboxZ
·
Mar 31
always be waiting🥑
Peep 🐣🐰
@Maritza12885182
·
Mar 30
Cool 😎👍
Vania (Taylor’s Version)
@VaniaRobles24
·
Mar 30
We’ve been listening 😳🥹🥹🥹🥹🥹😭 
@billieeilishtrs
 🫶 #5YearsOfWWAFA
erin ‧˚౨ৎ
@erinseilish
·
Mar 30
celebrate a new album announcement?
moony
@st0pbeingflirty
·
Mar 30
run from them haters gurl
P.H Eilish
@PabloHe00724178
·

@venus_moons0
·
Mar 30
the notif gave me a stroke actually
𝐥𝐢𝐭𝐭𝐥𝐞 𝐛𝐢 𝐢𝐧𝐭𝐞𝐫𝐧 𝐞𝐫𝐢𝐤𝐚
@erikaluvsidsb
·
Mar 30
palladium
@johanburgershop
·
Mar 31
my invisalign has i have taken i have taken out my invisalign and this is the album hahhahahahhahahhahahhahhahahaaaaaaaa




joel
@joeltovarr
·
Mar 30
well let’s say HELLO to the new era

@_positions__
·
Mar 30
ok now what?
Billie Eilish Daily Spotify
@BillieSpotify_
·
Mar 30
NOW PLEASE ANNOUNCE SOMETHING
Tony
@bloodylikeabody
·
Mar 30
Now what’s gonna happen
moni ❧
@dsambitch
·
Mar 30
atp we're tired
Comunidade Billie BR
@ComuBillieBR
·
Mar 30
BE3 RN?????
0:03 / 0:35
From 
billie eilish
Honest Andrew 🥀
@andrewscomet
·
Mar 30
you and your boss are annoying
Valeina 𐙚
@therrese_
·
Mar 30
BE3 PLEASE
marco 💋
@outfotime
·
Mar 30
GIRL ANNOUNCE THE FUCKING ALBUMMM


Billie Eilish Daily Spotify
@BillieSpotify_
·
Mar 30
OMG
QG Billie Eilish
@QGBillieEilish
·
Mar 30
Omg drop the album billie
thomaz
@thisdracarys
·
Mar 30
I can't do this right no your so hot
marco 💋
@outfotime
·
Mar 30
DROP THE ALBUM
𝐇𝐀𝐑𝐃
@AbcdHard
·
Mar 30


Billie is a bosslady queen
·
Mar 30
I had a dream
marco 💋
@outfotime
·
Mar 30
ANNOUNCEMENT
Info Billie Brasil
@InfoBillieBR
·
Mar 30
the one english TWeet your looking for...
kxng
@KxngPlayzYT
·
Mar 30
goodbye
Quote
kxng
@KxngPlayzYT
·
Mar 29
My debut single “When I Thrive” is officially out now!

(Official Lyric Video)

SUGARBOY👑
@SUGARBOY_SMALLY
·
Mar 30
You are better than cardi b
"""

Kim_Kardashian = """
Mudasar Choudhary
@MudasarJatt
·
Mar 28
Having tickles🤣

Ron Leith
@rl27base
·
Mar 28
Cyber babe!
SwapSpace
@SwapSpaceCo
·
Mar 28
Easy change any crypto without registration  
Quote
SwapSpace
@SwapSpaceCo
·
Feb 27
💸 Earn profit with our Affiliate Program

📍 Affiliate program - is a way to earn profit for providing a useful service to your crypto audience. Monetize any of the platforms you own or use

🤝 It offers you the opportunity to earn up to 50% revenue for every cryptocurrency…
Noa
@Trycolour
·
Mar 28


Your don't even
·
Mar 28
what am i looking at?
Amit Shah (Parody)
@Motabhai012
·
Mar 28
Love is the answer.. ❤️



@MudasarJatt
·
Mar 28
I want to be 💖


@arbabzia555
·
Mar 28
gorgeous
AhmadAleee
@AhmadAl11754421
·
Mar 29
Where are you going 😍
SHAKIR ANSARI
@shakiransari93
·
Mar 28
Nice outfit
fatiii
@fatiii4546
·
Mar 28
Looking so amazing
wwsews
@Wwsews
·
21h
Wow, who knew dogs were so sneaky? Better keep an eye on Fido next time he's near the treat jar!
Mery Sondal
@Merysondax
·
Mar 28
Can i be yours 🥹💦
The following media includes potentially sensitive content. Change settings
Diana paolacharamina
@paolacharamina
·
Mar 28

I guess this is ok
·
Mar 28
Mudasar Choudhary
@MudasarJatt
·
Mar 28
He doesn't aspecting😜


Mudasar Choudhary
@MudasarJatt
·
Mar 28

OOOOh kim I know what time it is
ZAQ RIDER
@zaqrider
·
Mar 28
Keep shinning
DW Hindi💫
@CLalChaudhary
·
Mar 28
Bobo
Oh my you should ride my rhino
·
Mar 28
Dĩ vãng là quá khứ, hãy tập trung vào hiện tại để xây dựng tương lai tươi sáng hơn.
Mudasar Choudhary
@MudasarJatt
·
Mar 28
Deadly wife🤣
0:10 / 0:25
J2🫀 .
@sp5derj2
·
Mar 28
i need more skims men😫😫
Chris Garcia
@chrgarciax
·
Apr 1
Who needs a personal trainer when you have a toddler? Running after them all day is the ultimate workout! ??
hema emam
@10HeMaEmAm
·
Apr 1
Seems like someone's been on a bit of a shopping spree! Maybe I need to take up knitting too...
Vítor Gomes
@gomes_vtor
·
Apr 1
Sounds like I need to up my selfie game if I want to attract a potential mate. Maybe it's time to invest in a selfie stick!
mitzi ariadna
@miiziipRiinZz
·
Apr 1
Sounds like my kind of diet plan - all the pizza I want without any guilt!
hema emam
@10HeMaEmAm
·
Mar 27
Who knew a conversation about socks could be so entertaining? I might have to rethink my sock drawer now!
luna maximiliano
@lunamaxi29
·
Apr 1
Just when you thought Mondays couldn't get any worse, I spilled my coffee all over my keyboard. Guess I'll be typing with sticky keys all day.
Pepe Ape Yacht Club
@YachtApe91521
·
Mar 27
Who needs a personal trainer when you can just chase your toddler around all day? momlife
Koch Toshia
@KochClaudeg
·
Mar 27
Looks like we've got a real-life superhero on our hands! Who knew saving the day could involve so much dental work?
Vítor Gomes
@gomes_vtor
·
Mar 27
Wow, this article really opened my eyes to the importance of wearing matching socks. Who knew my fashion choices could make such a difference?
Djayson Petrovski
@DjaysonPetrovsk
·
Mar 27
Looks like I'll be eating ramen noodles for the next month after seeing those holiday shopping receipts.
Ener Hocaoğlu 🏣
@EnerHocaoglu
·
Mar 27
Dat ass ages like fine wine

Ener Hocaoğlu 🏣
@EnerHocaoglu

Mar 27
Haha, this article cracks me up! Who knew misheard song lyrics could be so entertaining?
Ener Hocaoğlu 🏣
@EnerHocaoglu
·
Mar 27
I wanna clean all over that thing
Ener Hocaoğlu 🏣
@EnerHocaoglu

Apr 1
Who knew complaining about Mondays could lead to better time management skills? Maybe I should start moaning about Tuesdays next.
dinora amparo
@amparoal27
·
Apr 1
Wow, I had no idea llamas could be so sneaky! Watch out for those crafty little critters!
PROBERT LUKE
@LukeThesen
·
Apr 1
That's like trying to find a needle in a haystack! Good luck to the brave soul who attempts that challenge.
Tibberton Dickie
@tibberton1376
·
Mar 27
Trying to figure out if my great grandma's secret recipe for meatloaf is worth risking getting haunted by her ghost.
Hinduism
@hindusquotes
·
Mar 27
Can't believe I used to think eating kale was trendy. Now I'm all about that cauliflower craze! Who knew vegetables could be so hip?
elleffe
@elleffe_
·
Mar 27
Wow, who knew that talking to plants could actually help them grow? I might start having full-on conversations with my houseplants now!
Kai Salazar
@kai02eksalazar
·
Apr 1
Who knew a simple question could lead to such a hilarious debate among friends! Never underestimate the power of asking 'what if'.
PROBERT LUKE
@LukeThesen
·
Apr 1
Looks like someone's been sneaking into my pantry at night! Those missing snacks definitely weren't eaten by ghosts, that's for sure.
Sherrill Tinkle
@Schommero62
·
Apr 1
Seems like my dog has been practicing her escape artist skills... guess I need to up my game on securing the backyard!
Andrew 🤩
@BatKingAte
·
Mar 28
Whirlwind for sure 😦

RAYANANAS🍍 
@UnRayananas
·
Mar 27
Good car
Hassan Khan (Javaphile)
@meerhassankhan7
·
Mar 27
A perfect blend of style and sustainability.💕


RAYANANAS🍍 
@UnRayananas
·
Mar 27
When are returning my truck Kim?
Hassan Khan (Javaphile)
@meerhassankhan7
·
Mar 27
She's a boss


Giga Chad
@gigachad
·
Mar 26
When are you returning my truck Kim?
सुरेन्द्र चौधरी
@Surendrajaat01
·
Mar 26
Beautiful
Kim K Twink ☀️💋Taylor Supporter
@KimKKrave

Mar 26
@kimdieheard
Omg I can't even with this gorge
·
Mar 26
KIM PLZZZ STOP
gigi౨ৎ
@grandeiscozy
·
Mar 26
girl the boycott so you just don’t care?


सुरेन्द्र चौधरी
@Surendrajaat01
·
12h
Fantastic
Elvis JR💙
@ElpatronSFC
·
4h
Woww wowww woww this is fire
@muh3rmard
·
4h
Wow

sush
@2sush
·
Mar 27
Malibu hits different beautiful 🧡🔥

@2sushi3234
·
Mar 27
That ass aint bad fam innit

@2343hhourstogo
·
Mar 27
Why would you risk that with that car..


"""

Cristiano_Ronaldo = """

@GodlyDevotions
·
15h
Praying for a blessed day for everyone reading this 🙏 ❤️
Ibukun Aluko
@IbkSports
·
15h
Can’t wait to see you win 2034 FIFA World Cup..💪🏾🔥
kofi ĀDØFÔ
@kofi_adofo69
·
15h
They should rigged the World Cup for you…just like how Qatar did it for Messi.
Bothwell Chinyakata 
@bchinyakata
·
15h
When Cr7 put on a disguise and no one recognised him


Monther 🤍
@monthermh5
·
15h
The greatest of all time 💜😤🤯
Leo CULU Moh INT Miami🇬🇭🇦🇷 𓃵 🫶🏽🌝💛
@fawogyimiiko
·
13h
You yourself haven’t had a taste of a World Cup so how are u going to support someone to bring a World Cup to Saudi 😂😂😂
Nungua Burnaboy
@Views09
·
15h
Ambassador for Portugal 2030 and Saudi Arabia 2034, that’s my goat 🐐
Artist in War 🎨🎗🗡⚔❤
@SpiderManSpeak
·
15h
Best goal of Ronaldo 🤩🤩🤩
0:06 / 0:27
حسن الناقور Mr.Nagoor
@hasanalnaqour
·
15h
Great Support 

Thank you 🙏
صالح
@Q97m_
·
15h
Greatest of all time 🐐
Total CR7 🐐
@TotallCR7
·
15h
This is why we are all behind you my IDOLO 🐐
فرحان الفرحان
@farhan_alfarhan
·
15h
What good luck has brought you to a nation that loves peace and humanity .
United Radar
@UnitedRadar
·
14h
This man is influential😭
Hermione Oswin
@hermioneoswin
·
15h
He is really the greatest and most influential sportsman to ever exist.
frisktt¹⁵ (fan)
@TheVxlverdeSzn
·
15h
Automated
the goat
ديسلر
@hullf
·
15h
Ggggoooooooooooaaaaaaaat❤️❤️❤️❤️🐐🐐🐐🐐🐐🐐🐐🐐🐐🐐
RW 🇸🇪
@ronaldowarrior
·
15h
Maturity is when you realize that Ronaldo is better than Messi.


Arslan shah
@Arslanshah46
·
15h
Goat
DK
@AAKHIRI__SACH
·
15h
Well played 👏, proud of you 🫶❤️
Blaze
@CFCBlaze_
·
12h
🚨 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 | Cristiano Ronaldo has won the Player of the Month award in the Saudi Pro League! 🇵🇹🐐

His 4th POTM this season at 39 years old. 😅
محمد العقوبه CR7𓃵 𝕏
@abomnal
·
9h
We are also proud of your presence at Al-Nasr Club, Saudi Arabia. Thank you, #CristianoRonaldo
#AlNassr_fans


Fazal Elahi
@FazalElahiKhosa
·
46m
Wonderful Dear Ronaldo
fani rana
@faniranafanira1
·
7h
Great sir
Kamaldeen Kehinde
@kenkarmah
·
9h
The dream is big and realistic. I pray to be a witness. Here come 2034.

In sha Allah.
Zeeshan
@zeeshandigisink
·
13h
great
PhamHai
@DuchaiTb
·
4h
Yes 🔥🔥🔥
The Quiz master Ahmed
@quizmasterahmed
·
13h
Waw.. Hope u will be a legend this time and retired
Hashim Saqi
@hashimsaqi258
·
14h
Amazing
francis dickson
@okpraalekwu
·
9h
Big name
Quote
francis dickson
@okpraalekwu
·
Apr 1
When we told some of you that Jesus did not exist anywhere, that its a script written by the Europeans to further enslaved us, and that our so called men of God are using it to robb the masses, you think we don't know what we are saying, the way they brought Christianity with…
Show more
♥♻🌟ایمن🌟♻♥
@Ujala4u
·
7h
Best wishes
IPHONE POPE ..🚫🧢 
@sleyvinlegend
·
14h
Let’s make it happen and you better play too 😂🙌🏿
Aleezy Adeel🦋
@AlizeyAdeel
·
10h
Love you sir
Lê Bá Khánh Toàn
@LebaKevin
·
7h
Love
Esam_Baba
@esaambaba
·
14h
This nice
Ⓚ🇵🇰
@Harvey_Speectr
·
13h
I love Ronaldo
Jawad Khan
@JawadKh06093517
·
13h
Amazing star


CLINTON 💫
@LilMoGh
·
10h
Bottled the champions league when it mattered 
Bottled the league to Al Hilal when it mattered 
No World Cup 

But at usual more goals to keep you in the goat 🐐 debate v Messi

As long as it increase your numbers . Viva Ronaldo 🔥
Nungua Burnaboy
@Views09
·
10h
The last time Messi scored a club hatrick Ronaldo was still at Juventus. Cook them idolo🤣🤣


Mempeasem President
@AsieduMends
·
10h
No World Cup trophy hahahaha
Mo_ Gives Ⓜ️
@Mompha_Gives
·
10h
The greatest goat
The Random Guy
@RandomTheGuy_
·
10h
Name Something Ronaldo Can't Do 🥶


💪🎭..Rai ji..💪🎭
@Vinod_r108
·
10h
Cristiano Ronaldo's stunning headed goal against Sampdoria, rising 2 meters 56 centimeters.
0:01 / 0:45
From 
@EfsoSahne
Saint🏄‍♂️
@saintmufc
·
8h
Ageing like fine wine 🐐❤️
𝔸b𝕒𝕫𝕫
@abazwhyllzz
·
10h
Why didn’t you do all of this in Juventus or when you returned to Manchester United? Why did you run from Europe if you are not slowing down ?😂

💪🎭..Rai ji..💪🎭
@Vinod_r108
·
10h
2 beautiful hearts ❤️
From 
Enez Özen
Total CR7 🐐
@TotallCR7
·
10h
ALWAYS BEHIND YOU MY IDOL 🐐
ANGRYPUNTER
@OlaseniFeyisayo
·
10h
THE GREATEST PLAYER EVER TO PLAY THE BEAUTIFUL GAME OF FOOTBALL ⚽️  !!!!!
Aeesha of Arsenal🌹✨
@Queen_Aeesha
·
10h
Gather here if you farming $PARAM  for a 2x points
Aditya
@aditya_web3
·
10h
Who's the 🐐
1,687 votes
·
13 hours left
Nungua Cardi B💕
@ellyserwaaa
·
10h
Where is your World cup trophy

"""

Jimmy_Kimmel = """

ZAQ RIDER
@zaqrider
·
Mar 13
Another Bang🎉

Lunazmom
@Lunazmom2
·
Mar 13
I am never watching anything either of you produce ever.
Judy
@Ink8Judy
·
Mar 13
I'M STILL CRACKING UP WITH JIMMY'S 
"ISN'T PAST YOUR JAIL TIME JOKE"... 😂

Brendon 🇺🇸
@DadioKillerB
·
Mar 13
I don't get this joke
@kareemjeanjr
·
Mar 13
Oscars ratings were awful. Amercia KO’d Jimberly again.
Burrow to Chase TOUCHDOWN BENGALS
@Burrow2ChaseTD
·
Mar 13
Imagine being grown men and this obsessed with bashing another grown man

RHollist
@RobertHollist7
·
Mar 14
Jimmy when you go to prison are you going to do blackface again 🤡🤡🤡🤡
Loki the Pawtriot
@ScoutKopfjager
·
Mar 13
Newsflash. You and DeNiro are both irrelevant. No one cares. 😹😹😹😹😹
idkLeo
@leo_arellano92
·
Mar 13
No one likes yall lmao
Patrick Lac
@PatrickLac007
·
Mar 14
#banjimmykimmelshow
Eric Trammel
@EricTrammel3
·
Mar 12
You made Trump a cartoon villain!  I love you Jimmy ❣️. You are so awesome 😎
UltraWendy
@WenDogeCoin
·
Mar 11
Not watching that garbage
Jason
@Jason_oct
·
Mar 11
Make America Great Again. Vote Trump 2024!
🇨🇦Chantal Dugdale💙💛
@cldonline
·
Mar 11
Best reply ever “Isn’t it past your jail time?”  to Trump's rude, insulting post about your performance at the Oscar's tonight! 
@jimmykimmel
 You did a great job! We love you! Ignore Trump. He is always negative, boorish and just plain rude. Perhaps it's too many drugs or alcohol.…
Show more
pearljohn
@mjohn55
·
Mar 11
You are the worst host ever!!  You are not funny or talented !
Joshua Robinson
@JRobFreedom
·
Mar 11
You suck Jimmy
SLWells
@wells_sl
·
Mar 12
Pretty low to bring up someone’s drug addiction on the night they are up for probably the most prestigious award in their industry… but  what else should we expect from “black face Jimmy Kimmel”… I mean, he’s lower than the 💩 on my shoe.. sorry 
@RobertDowneyJr
 for having to…
Show more
🇺🇸Kirk🇺🇸
@Kirk_925
·
Mar 11
I would NEVER watch anything with you as a host.  You are a subhuman and filth!  
#JimmyKimmel is an asshole👍
MoneyPenny700
@MoneyPenny700
·
Mar 11
The following media includes potentially sensitive content. Change settings
I'LL BE BACK!!!
@DavidYeshua4
·
Mar 11
What a POS 🤡 Kimmel has no respect for women! We know that based on his public behavior! Lock him up!!!


d
@Ambriz_Dom
·
Mar 11
Jamie 🇺🇲 🇨🇦
@LibertyJamison
·
Mar 11
Hahaha time to give your awards to the most narcissistic and entitled celebrity 👌
Salmon La Sac Sue
@2020lizmac
·
Mar 11
Haven’t watched the Hollywood Pedos give each other awards in years. It used to be a classy show now it’s nothing but trash as are the movies produced in Hollywood.
Texas Aeronaut
@TxAeronaut
·
Mar 11
Sharing is caring!
Christopher Colombo
@clhwi2017
·
Mar 11
Boring.
StOrMyNiGhT
@Nautiguy48
·
Mar 11
Worst Oscars Host in history.
Brian
@girldad72
·
Mar 12
Hey Jimmy remember that time you spent  on the Island with your other pedo friends. We do.


Don't Tread on Memes
@donttreadmemes
·
Mar 11
Nobody cares.
Rocker Chic ❤️🇺🇸❤️🇺🇸❤️🇺🇸❤️
@glamfairey
·
Mar 11
Politics should not be mentioned at the oscars Neither party. Your disgusting 
.
Downunder girl. Doggos are my 🌏
@JustKimfromoz
·
Mar 12
You're going to be crying a flood of tears come November mate & don't move to Australia.  WE DON'T WANT YOU HERE!  You were an embarrassment at the Oscars & hopefully that will be the last time they ever ask you to host 🙏
TheShortKing
@TheShortKing93
·
Mar 11
PEDO JIMMY BACK AT IT AGAIN
G
@BenGleib2024
·
Mar 11
feel the music jimmy
FeelTheMusic
@feelthemusicglo
·
Mar 11
Yes!🫶🚀🏆👌🎶
Quote
Teslaconomics
@Teslaconomics
·
Mar 7
Yo quiero un Tesla en Argentina 🇦🇷
0:01 / 2:27
Bob Mute
@BobMute2
·
Mar 11
No thank you. 👎🏼👎🏼👎🏼
Mical Valencia
@micalvalencia
·
Mar 11
Congrats on the Oscars. It would be awesome if you used your platform & visibility to highlight a family in 🍉 ! There is a huge list to choose from on Operation Olive Branch (TIKTOK OR INSTAGRAM)
Bob Mute
@BobMute2
·
Mar 11
Perhaps the most entertaining part of the Oscars is watching the host try to be funny while simultaneously offending as few people as possible. It's a tightrope act that often results in a bland, forgettable performance. 🎭
😇Donna
@nurseangel777
·
Mar 11
It’s only been 15 minutes and I’m already tired of your lame insulting humor.👎🏼👎🏼👎🏼
Mustafa Hassan
@imustafazia
·
Mar 11
We love RDJ, and you are lower than dirt.
Tees Valley Voice 🇬🇧
@TeesValleyVoice
·
Mar 12
When Donald Trump is back in the White House it will be past your jail time, Epstein Island visitor.
Richard Willett
@WTAFRich
·
Mar 11
Coward making jokes about Michael surrounded by your Ptah action figures. We see you son.
Zen Satori🇺🇸
@Stevo_1969
·
Mar 12
We know what you did on Epstein Island. Your Sick
Jules Brogan Dinolfo
@BroganDinolfo
·
Mar 11
Time’s up, Jimmy. 👋🏼
Quote
il Donaldo Trumpo
@PapiTrumpo
·
Mar 11
JIMMY KIMMEL TOOK THE BAIT!!!🤣🤣🤣
0:01 / 0:45
@MrsAndy
@MrsAndy73529976
·
Mar 11
I’m ready 😁😁
𝚄𝚗𝚌𝚕𝚎𝚁𝚢🇨🇦⚡️
@UncleRy_eth
·
Mar 11
Is Rodgers handing out any awards? 👀😂
@MrsAndy
@MrsAndy73529976
·
Mar 11
You are welcome 🤗 jimmy 💙
BenCharles
@BenCharles2014
·
Mar 11
Yess! Let's go
Sapkota ✈️
@disser_sapkota
·
Mar 11
Wishing you luck, Jimmy. It should be a great show as long as you didn’t try to tell any jokes. Not your strongest suit. 😝
Sean Joseph
@sjoseph_sports
·
Mar 11
Be funny"""

Elon_Musk = """

Elon Musk (Parody)

@ElonMuskAOC
·
Mar 19
I could build it in a year
Anonymous
@YourAnonNews
·
Mar 19
The car manufacturer doesn't like high speed rail, not surprising
Mr. Bigglesworth Memes 𝕏
@Twitermytweet
·
Mar 19
Seriously this is the truth

Parker 🐐
@DotComParker
·
Mar 29
Elon, bots are able to comment scams on my posts and I can’t see it because they have me blocked. 

jailbreakrob
@RobJailbreakrob
·
Mar 29
For all those who want cars to take you where you want to go automatically, 

I can just say that driving my 69 Corvette manually was an amazing experience you all sadly missed.
Carmine’s Import Service ® 𝕏
@S3XYPLAID
·
Mar 29
And Tesla Auto Park with cameras only works absolutely perfect. Between this and my FSD test drive last night I totally get when Elon said, “LiDAR is a fools errand”. The others want to take the easy and temporary route to new features. 
@elonmusk
 sees long term real future.
0:02 / 0:32
CyberCat
@Tesla_Cybercat
·
Mar 29
The future is here！FSDV12 Navigates Three Sharp Turns and Merges with Ease in Boston’s Rain-Drenched Rush Hour
The following media includes potentially sensitive content. Change settings
EdwarDiGi
@EdwardDiGi
·
Mar 29
If cars will be drive themselves, we would not need cars at all. Urban transport will be zero margin and people will need less cars. The first threat to $TSLA are robotaxi indeed
Ɖ𝕓𝕝ℂ𝕒𝕡ℂ𝕣𝕚𝕞𝕡𝕚𝕟
@dblcapcrimpin
·
Mar 29
When no nags?
Timothy Raffler
@cymba_de
·
Mar 29
Yes yes yes but when working Autowipers?
BEBE
@X_BEBEeth
·
Mar 29
Elon, what day is the fourth launch plan for the starship?

James W Law
@JamesWLaw1
·
Mar 29
The second to last to have FSD will be for Emergency vehicles/Police. 

However, to reduce accidents to near non, we just need 1/3 of vehicles to have FSD. 

People will think we were crazy to get into a car knowing how many get killed every day.
Lisa #TeslaTruth
@TeslaLisa
·
Mar 31
QUESTION....  Why are a zillion newbies getting a free month of V12 when all Legacy S/X owners who paid thousands can't get it?    Thanks 
@ElonMusk
 
@aelluswamy
Two flags
@GagliardiLou
·
Mar 29
Elon, I can't believe how nice my new model y is. I don't understand why anyone would buy anything but a tesla. Maybe price would deter them, but I got a great deal on the model y. Best value out there, in my opinion.
Derek Wang
@derekhxw
·
Mar 31
I just tried V12 for the first time with 12.3.2.1, wow! I have been an enthusiast since V8, but still V12 really wow me. 
@elonmusk
 you’re so low key on this (which is good and prudent).  Really appreciate the great job!
Ramy
@TeslaXplored
·
Mar 29
Will that happen in the Nassau/Queens area of NY too? Seems to struggle here a lot. 
Lots of roads without lanes, more human drivers NOT follow driving rules than follow them, driving on shoulders, running red lights, NO patience, emergency vehicles. It’s INSANE here 😂
Tesla Girl 🇨🇦
@somi_teslagirl
·
Mar 30
Ive been sold on #FSD before I even got it in my 
@Tesla
. That’s why I bought it, sight unseen. After I witnessed regular #Autopilot in my 2019 road trip across the country, I knew full autonomous driving would 💯  work and change the world. https://x.com/somi_teslagirl/somi_teslagirl/status/1175804971368861696
This Post is unavailable. Learn more
Brian Basson
@BassonBrain
·
Mar 29
it will be way better than a human, period ... already is!
Lawrence 4.68e+3 🔋
@Avatrode
·
Mar 30
Seeing the progress achieved in FSD V12 .....In terms of safety and even considering only the financial prospect of robotaxi future income ... in my estimation .#Tesla #FSD is worth more now than the hardware value of my 2022 Model X Plaid.
Ryan Tanaka
@RyanTanaka3
·
Mar 29
Thanks for helping make the future great
Dave the Blind Tesla Guy
@DaveWarnedYou
·
Mar 30
Riding in a car is the most dangerous thing humans do every day, specifically because other human drivers are so bad and unpredictable.

Self Driving Vehicles can't come SOON enough for disabled people, like me... I can't wait to get some of my freedom back!!

Just waiting for…


2THdoc2012
@2thdoc2012
·
Mar 29
I’ve been thinking about that as I’ve been testing v12.    It really is to a certain extent already like a personal taxi
Mark
@CodingMark
·
Mar 30
now that the machine is finally churning on a capable, future-proof architecture, progress should be unbelievable
Phil Fox
@PhilFox43249797
·
Mar 29
And Tesla has a multiyear advantage in this high margin, “winner take most” FSD business

Thank you Elon for your superb leadership
Tesla Synopsis
@TeslaSynopsis
·
Mar 30
Elon can FSD beta roll out be a bit faster, especially to cars that had been using FSD beta forever?
Roel Smelt
@roelsmelt
·
Mar 29
I’ve told my kids that they most likely will not be allowed to get their driving license and drive their own cars on the road. Way to dangerous! 
And why would they. It is so easy and save to get everywhere.
Ananto Mohammad
@01Ananto
·
Mar 30
By saying this now people will get drunk and then try FSD. Which not supervise by a human. Big statement Elon. Not a safe one. Cause 12.3 is still not 100% perfect.
Wayne Snyder
@WayneSn35339982
·
Mar 29
I really don't want or like that. Perhaps if someone, you, would build a people carrier train of FSD's linked together to take the mindless where they want to go and drop them off along it's way, less traffic, so I can drive my 1949 Ford pickup ice 3 speed truck with no worries.
Liz Burgess
@LizBurgess92677
·
Mar 29
I think i would put a breathalizer. Against the law to drive  DRUNK🤣🤣🤣🤣🤣🤣
Steven Peeters
@aikisteve
·
Mar 30
I assume that when FSD beta is rolled out in Europe it will be again starting with a very limited group of beta testers? Makes sense because of all the differences with the US and specifics per country
Rob
@crossland_rob
·
Mar 29
I don't like to be the barer of bad news 
@elonmusk
 , but, some people, myself included, actually enjoy driving their cars.
I am retired, but ready to take on a new adventure in my Hope Foundation,  but, love to drive a muscle car that sounds like a muscle car, just how it is.

To…
Show more
🇺🇸Victor the SnakeMannn™®🇮🇱 (Dude/DUDE!)
@SnakeMannn
·
Mar 30
It will really be amazing how good 
@X
 will be once someone fixes the Shadowbans too! What? Too soon?
@B.p🇺🇸⚔️
@BdPwll81
·
Mar 29
Well I will be that guy in the future that still has a gas guzzler in his garage ......I'd rather transport myself -- I would however love a ride in one of those rockets of yours. I hear you're close to breaking through the firmament....😉
Dan D.
@DansTesla
·
Mar 29
Can’t wait to get V12….my car has been downloading this for 3 days lol $tsla
Susana CL
@schheng1
·
Mar 30
The improvements that the world of computing and engineering has brought to the way we live in North America have been incredible and mind-boggling. 🤯🤩🚀🙌🏻👏🏻🍫😘💫
#artificialintelligence #enginnering #automobile #aeronautic #computing
Dreams of Mars 🕊❤️🚀🌕
@MemesOfMars
·
Mar 31
in Germany 🇩🇪 the beta still has a lot of work ahead. One week it behaves ok the next it does weird things like trying to go on the exit lane even though the straight lane is super clearly marked.
Landon Hamilton
@LandonH
·
Mar 29
It’s crazy good. Thanks for all the great work 
@Tesla
 & 
@elonmusk
Brian
@oi8achevy
·
Mar 29
Speed management is still an issue. How are you going to deal with all the inaccurate speed limit map data? Even on v12 most of my drives in upstate NY are crippled by the system defaulting to 25mph on unmarked roads.
Melissa Jean
@MelissaJeanSays
·
Mar 29
That sounds cool. But I still want a manual control option.
Nick Lippis
@NickLippis
·
Mar 29
I love FSD.  It's part of living in exponential progress time.
Furkan Gözükara
@GozukaraFurkan
·
Mar 29
I agree with this
Nelson Alves
@NAlves_EJ
·
Mar 29
For the time being the question is how will that affect the sales outlook.
Quote
Nelson Alves
@NAlves_EJ
·
Mar 29
Tesla's gearing up to drop its Q1 delivery figures. $TSLA

It hasn't been all smooth sailing. Tesla's Berlin gig got hit by an arson attack. Shut them down temporarily, messing with production. Analysts are scrambling, slashing their delivery forecasts. 

These numbers will guide…
Show more
N Suresh
@NSuresh_ECW
·
Mar 29
Legacy OEM's should licence Tesla FSD into their cars & rapidly progress towards Autonomous vehicles
alexisd3000
@alexisd3000
·
Mar 29
If every car used FSD, the roads would be so much safer!  It’s the human drivers we need to look out for.
TheBigDeal
@griffithe
·
Mar 29
NGL I watched 
@colin_gladman
 demonstration and it had me antsy. 

I wanted to grab the yoke on every turn.
Marcus Aurelius | Practical Stoicism
@Wisdom_MAPS
·
Mar 29
Thinking long term and continually investing in that...gives you these kinds of results!
Rani
@aqsarani76
·
Mar 29
👏👏👏 It will be interesting when licenses and all the admin and bureaucracy is no longer necessary. It’s sure to be an interesting transformation. Not sure the Government will make this easy. 🤣
Jeremy Merchant
@Jeremywmerchant
·
Mar 29
All future car purchases will require FSD in my family!
Fyrewede ☦️
@fyrewede
·
Mar 29
I will never trust FSD if for no other reason than that I don't trust other drivers (or other FSD vehicles). All ot takes is one loose tire hurtling towards my car through the air at speed.  I might manage to dodge it. I'm not certain FSD will.
"""

Andrew_Tate = """


Aleks.V.S
@AleksAlwaysWins
·
Apr 3, 2024
Inspiring to tears.

Andrew Tate is my hero.
Walid Zada
@WalidZada1
·
Apr 3, 2023
Tears For Fears.
Akono Schrand
@akono14
·
12m
The power of a dad!
Fibonacci.Man
@Fibonacci_Mann
·
28m
Your story reflects the invaluable lessons we learn from our mentors and the impact their words can have on our journey. Epic!!!
𝘋𝘢𝘬𝘴𝘩
@okdaksh
·
Apr 4, 2023
wholesome
ReclaimYourThrone
@ReclaimYourX
·
Apr 4, 2023
Awww so sweet 🙏🏾👑
Tate News
@TateNews_
·
Apr 3, 2023
Free Top G
Raul Serrano
@FgvPlanet
·
Apr 3, 2023
What a great lesson.
ZUBY:
@ZubyMusic
·
Apr 3, 2023
This is cool.
The Real World
@therealworld_hq
·
Apr 3, 2023
The greatest gift a son can receive from his father is the inheritance of knowledge and wisdom. 

He was the real Top G 🙏
Black Sheep 🥷🐑
@BlackSheepMfer

Hustler's University / The Real World
@JoinTheHUWorld
·
Apr 3, 2023
A great father and a great son.

He sure would be proud of what you have become.

He never doubted you for a second.
Tristan Tate

@TateTheTalisman
·
Apr 3, 2023
What’s cool, at least for me is that when this happened dad was the age I am now.
shah

@shahh
·
Apr 3, 2023
Extreme focus when playing chess at that age is insane, I couldn’t even focus on a cartoon at that age.
Rap God
@twomad
·
Apr 3, 2023
I would of checkmated you little smart ah instantaneously my brudda
Hendrik Vandermaesen
@Hendrikvdmaesen
·
Apr 3, 2023
Very cool. Have you ever considered opening up an international chess-school?
Ninety Eight
@98sThoughts
·

🎨Paintress April🌸Sunshine Daydream
@PaintressApril
·
23m
Dude, I had no idea you were a Hoosier!  Me too!  Nice to meet you!
Abigail
@abigail_fekete
·
Apr 3, 2023
You were a top kid even at a young age.
Keez
@SulaymanABS
·
Apr 4, 2023
this is amazing
HairyLahey
@HairyLahey
·
Apr 3, 2023
Son, once youre grown up, youll beat anyone at anything

Apr 3, 2023
And Emory was right.
The Real World
@AccessTRW
·
Apr 3, 2023
Raised to be exceptional.
·
Oct 26, 2023
Yo DYOR is rule #1
A.
@Blue_flamingo__
·
Oct 26, 2023
No one ever made money in crypto . I lost few K bucks 🥺
S. Yeshitharan
@themoneymod
·
Mar 26
Interesting about the success with your team.  

Building trust with experts is key in this volatile market.  

Would love to hear more about your approach.
la_gent
@lagent213
·
Oct 27, 2023
Hodl and win the race.
Crypto King
@Cryptoking
·
Oct 26, 2023
U shi* on BTC then use it for clout?
nftinos.eth ᵍfᵐ
@nftinos
·
Oct 26, 2023
And that for the small fee of just $50 per year. 🤔
MysterE
@MysterEgora
·
Oct 29, 2023
Success in $BTC isn't guaranteed by following 'pros.' Cryptocurrency is volatile and unpredictable, with market conditions changing rapidly. Rely on thorough research, risk assessment, and consider seeking advice from certified financial advisors. Invest wisely. 🔍💡 #CryptoFacts…
Show more
Bromie
@CryptoBromie
·
Oct 26, 2023
I thought you said crypto bros are dork nerd geeks? 

Nvm

Can you shill another ticker please? $sluts is ded
Mike: The Username
@RotondoAGoGo
·
Oct 27, 2023
Lol ok big boy, your jenga tower is wobbling - gonna be a hoot to watch

Remember we are all under the 10x blessing - our actions are returned to us 10 times over
I have a feeling you’re in line for the Gauntlet
JustMj
@jamesmj85
·
Oct 26, 2023
This is really a good pitch and video
drnick - dao/acc
@DrNickA
·
Oct 28, 2023
I hope you’re going to teach the lads not to get rugged rather than feed them to them.
OMEGAMILLIONS⛈
@OMEGAMILLIONS1
·
Mar 26
Or they could have just used that 50 a month to add to their own allocated weekly dollar cost strategy and would still be up all alone bruv.
The Dutch Doge Guy 🐕
@070guy
·
18h
Make money on $Doge!
Patryk
@PatrykDumicz
·
Oct 28, 2023
“Made money” - meaning that they already sold BTC securing their profits? I’ll bet you a Bugatti most of them will wait until it’s too late #greed
Masculine Empire⚔️
@Masc_Empire
·
Oct 26, 2023
Your money problems are usually your mindset problems.

Will not explain.
McJoker
@mcJoker_05
·
Apr 1
dm me what you think of top G in chat now

@vectorchatai
 🤝 getting in early in a crypto #AI project is as manly as it gets my g's. you're welcome in advance
 
 
DogShortsTV
@LegitPersian
·
Oct 26, 2023
This is a top signal
Patriot Father
@realPatriot_Dad
·
Oct 26, 2023
I'm signed up in the Market course now! I am motivated to learn and expand my financial future for my 5 children!
Eli
@TheLoveOfJoy
·
Oct 26, 2023
XLM and stellar are where it’s really at
Joshua Silent Mode
@joshsilentmode
·
Mar 29
Find The Hero Inside You
@FindYourHero
·
51m
Heroes don’t depend on inspiration, they thrive on self discipline.
Famous
@Famous_999_
·
Oct 26, 2023
Bro you are lying and I can confirm
Tyler Robertson
@copyxtyler
·
Mar 20
TRW costs less than what these people would invest.

And they'll still not join.
𝘋𝘢𝘬𝘴𝘩
@okdaksh
·
Oct 26, 2023
David Halliwell
@D_Halliwell95
·
Dec 5, 2023
Professor Adam is a G.
Kat
@kittiesbitties
·
Oct 26, 2023
you scammed me
Jack Willis
@jackwillis004
·
Jan 11
I’m in TRW and don’t have a network tho?

Nor have I closed a client yet.

How would one go about it from this approach ?
YEYEmeta 🥲 | KIND
@YEYEmeta
·
Oct 26, 2023
You just said nfts were bad.

Dorks were lucky on crypto.

Now you want us to do crypto with you?

Ima confused when are you joking or real.

🥲
EtherMage

@ethermage
·
Oct 26, 2023
Didn't this guy just post a video saying crypto shillers are the worst?
Karlsson Daniel
@KarlssonDaniel4
·
Oct 26, 2023
BEAST MODE ! $RED $STAN
@BEASTMODEAPEE
·
Oct 26, 2023
$MULTIX GOING HAM
Kacee Allen 🇺🇸
@KaceeRAllen
·
Feb 29
Only the real ones HODL
web3ie
@web3ie
·
Oct 26, 2023
Remember when you said crypto was for dorks and your never touching it? 

Now your here pumping my bags.. 🥂


Zarar Khan
@DrZarar01
·
Jan 11
thanks for sharing
SKY LINE

@SkylineETH
·
Oct 27, 2023
You just called crypto is scam 

and 

Now you shilling your own scam paid crypto group ?

Do better, G.
Mr. Cypherpunk
@ABlastforever
·
Oct 27, 2023
The scam artist is back again"""

Dwayne_Johnson = """
Mahr Irfan Hiraj
@Raj_diary
·
Mar 7
General Booty 🇨🇲
@big_hero_chris
·
Mar 11
But will i feel the mana though?
Anthony Russo
@Anthony_Russo97
·
Mar 7
Cody Rhodes sticking with head and shoulders
ShiGod
@jnr_kali
·
Mar 7
The Rock! 🪨
Dr. Martin Hartmann
@the_artofhealth
·
Mar 7
I also really love wellness and sauna. 

Sauna helps me regenerate after workout and improves my immune system.
Jonni Martinez
@iJonniM
·
Mar 8
Rock please bring it to Canada too 

@WalmartCanada
This guy sucks I want to slap him
@Raj_diary
·
Mar 7
ZAFAR ABBAS
@xafar_
·
Mar 7
Thanks. Good advocate for wellness
Wyssii∆Hun
@Wyssii_Hun
·
Mar 7
Omprakash Choudhary
@OmChoudhary01
·
Mar 7
Bang bang this is sparks
DEX 💙
@DXSD_1
·
Mar 7
Rollins owns you


Kakarot
@ShadBoogie
·
Mar 7
Listen, if you’re going to be a “heel” imma need you to stop doing these types of ads, I know I know it’s part of your brand but you can’t be talking how you do on SD and then get on here and start talking nice and proper and wholesome
Joshua Harley Davidson
@jharleyd12
·
Mar 8
Will be checking it out.
This guy sucks I want to slap him
@Raj_diary
·
Mar 7
SaltyEssentials
@SaltyEssentials
·
Mar 8
What a sellout 😂
Tommy Slaight
@TommySlaight
·
Mar 22
Christhecool
@christhecool21
·
Mar 7
Thanks unc !
AEWBlog
@AEW_Blog
·
Mar 8
I'm gonna quote his ass because he's lovely
AEWBlog
@AEW_Blog
·
Mar 7
The Story of The Rock vs. Hulk Hogan
Leading Up To #WrestleMania 18
0:02 / 1:05:12
Mahr Irfan Hiraj
@Raj_diary
·
Mar 7
District411
@iamdistrict411
·
Mar 7
Wow
Daran NVASEG
@daranvaseg
·
Mar 7
Oh my star eyes
FeelTheMusic
@feelthemusicglo
·
Mar 9
Yes!🏆🎶👌🚀🫶


Mahr Irfan Hiraj
@Raj_diary
·
Mar 7
Mahr Irfan Hiraj
@Raj_diary
·
Mar 7
Mahr Irfan Hiraj
@Raj_diary
·
Mar 7
#takebettercare
Omprakash Choudhary
@OmChoudhary01
·
Mar 7
and the trophy goes to
rxo9191 🥦
@rxo9191
·
Mar 7
At 
@BrocOnSol
 we also advocate for healthy habits using memes and making a broccoli character funny and intriguing! Eating vegetables and adopting healthy habits is the key to our health and our wealth! #EatYourGreens #TheBrock 😁
NerdyX 🐼
@ShawnS90x
·
Mar 7
Putting in work.. i see you. Good stuff, best of luck on your new endeavor
DaveHuze
@DaveHuze
·
Mar 7
Casas Plays
@CasasPlays
·
Mar 7
That tattoo care though 👀
Cheelee
@Cheelee_Tweet
·
Mar 7
🌶 🌶 🌶  https://twitter.com/Cheelee_Tweet/status/1751310823459606634
is this the quote your looking for rock man
Cheelee
@Cheelee_Tweet
·
Jan 28
Hey, Cheeleeland 🌶️ 
We have amazing news! 
Our CHEEL token got into the top-5 tokens of 2024 🔥

“CHEEL tokens have a high utility that boosts demand for the token, deeply integrated into the platform’s mechanics. Each Cheelee enthusiast automatically becomes a crypto user from…
𝐴𝑛𝑡ℎ𝑜𝑛𝑦 “v LEX LUTHOR v” 𝑅𝑖𝑣𝑒𝑟𝑎
@_AVMR_
·
Mar 7
I went to the website and was gonna put an order in. I had the sandlewood suede body wash, shampoo, and deodorant.

With the shipping, the total was $34.78. However, when I put in my 10% off code PAPA10, it changes the shipping to $8-9and this canceling you actual 10% off. #Shady
ItsDJ
@PhotobombChamp
·
Mar 8
Alright Rock, I’ll make a trip to Target this Sunday
HankSalmonsJr📈
@salmons_jr
·
Mar 8
#DiarrheaDwayne
Voices
@VforVoices
·
Mar 8
Well if the Rock says it's good, it's good 👍🏾
Thyrone Cameron 🏆🥇🎯
@GetMeCash
·
Mar 8
Bro when do you sleep?!?!
mtzslivegaming
@mtzslivegaming
·
Mar 8
Wow good day



Living OG
@LivngOG
·
Mar 22
THE PEOPLES CHAMP FOR SURE
Kryptonian Saiyan
@NarutoExplained
·
Mar 22
The people’s champion for a reason!
light yagami
@habdoolahi
·
Mar 22
This is legit heartwarming.. it’s what you expect from the final bosss
ziamalik
@ziamalik685
·
Mar 22
History will be made on this wrestle mania.
Mr. Wright Way
@SteveWrightJr
·
Mar 22
The Rock is a Man of his word
KT
@KeanuTrades
·
Mar 22
or is this the quote you ass
KT
@KeanuTrades
·
Dec 11, 2022
OUR OLD BUDDY @toddster85 had surgery! Todd was born w spina bifida and has had countless surgeries and trials. He drives for @lyft when he can & is the biggest @WWE fan I know! 

We live near LA so LET'S SEND TODD TO WRESTLEMANIA! 

RT LIKE TAG EM @TheRock  x.com/KeanuTrades/st…
Show more
🐊 🅃🄸🄼 🅶🅰🆃🅾🆁 🐊
@MrGator84
·
Mar 22
This whole story with you and Cody has made this an epic legendary show. Cody vs The Final Boss in a belt match would be sick, twisted, and badass
Uncle Chad
@GIGACHAD2021
·
Mar 22
ABSOLUTELY INCREDIBLE
Penn State FB Thoughts
@PSU_FB_Thoughts
·
Mar 22
What an awesome back and forth
Mike Bacon
@MikeBacon
·
Mar 22
Great stuff dude. Makes me want to go to my first WWE event ever here in my hometown. Much love ❤️
Rakshit Shah - DUNKI
@rshah2611


"""