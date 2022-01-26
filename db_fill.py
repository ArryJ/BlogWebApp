from blog import db
from blog.models import User, Post, Comment, Rating

def add_post(post):
    db.session.add(post)
    db.session.commit()


title1 = "IPL Dashboard : My first Full stack project"
content1 = '''I completed several front-end projects personally and as a freelance developer in 2021, so I had a good grasp of front-end technologies such as HTML, CSS, and JavaScript. My undergraduate degree was in the Electronics and communication field of engineering. Thus, my knowledge in core Computer Science subjects was lacking. I was curious about how data was delivered to the front end and how web requests were handled at the backend. So, I decided to expand my skills by learning more about databases and backend development. The best way in my opinion to learn anything is through making projects. 

Indian Premier League (IPL) is a popular form of cricket in India, where players from all over the world come to play for clubs representing different states of India. It’s a huge affair in India where families and friends come around a television to see the match and support their favourite teams. I too am a follower of this tradition. Thus, I decided to create a dashboard with statistics of every match played in the IPL since its inception. To make the backend, I decided to learn Java and the Spring framework to develop a REST api. Java and spring are mature technologies with good community support, this led to the decision for me to use them. For the database, an in-memory embedded H2 rdbms was selected. The reason behind this is that since the data is static and the website just shows the statistics of the matches held, loading data into the rdms each time the application starts won’t be too resource intensive while making the development process easier by packaging the database with the application. The front end is made using HTML, CSS, Bootstrap and React framework to make development easier and its popularity in the front end community. The data to populate the tables was downloaded from an open kaggle database repository.  The database is populated from a CSV file using Spring Batch which makes loading data into the database fast. 

The features to be implemented were decided to be, the front page should be showing the tiles of team names. Clicking on the tiles should take us to that team’s different match statistics. The matches won should be in green and lost in red. The latest 4 matches will be shown in tiles, while a pie chart will display the team’s win percentage alongside the team’s name. There is also a scroll bar on the left where the user can choose the year for which they want to see the past match history for the team. The backend REST api would supply all the data required for the features to be implemented after processing the csv file match data of all the teams. The following are the endpoints that the REST api when hit with a request will be returning the data to: 
Match List for every team - REST Endpoint → /team/{teamName/}/matches?year='year'; Returns List<Match> data for a particular year.
{teamName} and 'year' are PathVariables and Query parameters respectively.
Team List - REST Endpoint → /team; Returns List<Team>
Fetches team with latest 4 matches played - REST Endpoint → /team/{teamName}
Returns Team object

The spring boot backend has been divided into just 2 layers -

Controller layer → This layer maps the resources to call the repository method that returns the appropriate response. There is only one controller that is TeamController present.
Data Layer → This layer consists of 2 entities - Team & Match. Consecutively there are two repositories MatchRepository and TeamRepository to connect to the in-memory database using Spring JPA hibernate. Which in turn runs JPQL queries to extract desired data from the H2 database. 
The data package consists of the Spring batch configurations, jobs instructions, Reader, writer and processor logic for each step. Spring batch reads data in chunks, processes them, and then writes them all at once into the database by mapping MatchInput to Match object. The Team gets populated after the job finishes.

The front end is then made keeping all the functionalities in mind and by getting data from backend by making REST calls to the developed REST api. Another technology that was learnt through this project is git. Git is the most powerful tool in a developer’s skills that in my opinion anyone can use whether they are into software development or not. I myself use git to not only store my code but documents too so that I can use them whenever I want, wherever I am.
'''
summary1 ="My first full stack project and my motivation to explore backend development is explained through this post. The various design decisions and my learning journey will give a beginner developer an insight on how to tackle problems while creating projects."
image_file1 ="post1.png" 
author_id1 = 1
post1 = Post(title = title1, content = content1, summary = summary1, image_file = image_file1, author_id = author_id1)

title2 = "Water Flow Analyzer"
content2 = '''With the increased effects of Global Warming on our environment, the need for judicial use of our resources has never been more urgent. Water is one among many such resources. There are many cases of careless water wastage in households, commercial complexes, and many other places. Moreover, though people are aware of such incidents they are not mindful of the amount of waste these practices lead to.
We feel that if people are just notified of the amount of water they are consuming on a daily basis and how they compare to the recommended usage they will be more conscious of their water consumption. The recommended usage will be calculated by studying numerous households spread across various areas in a city over a period of time and taking an average of the data. The Intelligent Water Flow Analyzer will then check if any particular household goes over the usage limit by a pre-decided value or not, then an email or SMS notification will be sent to the household owner if they do go over. The usage limit will be flexible which can be changed according to some special occasions or holidays like Diwali, Holi, marriage, etc.
To accomplish this, I used a Water Flow Sensor(YF-S201), Raspberry Pi 3, some jumper wires, a breadboard, and some pipes for water flow. The tech stack used was Python, Google Firebase, and AWS SNS service. The Problems faced were:
1. MongoDB couldn’t be used as a Database. Why? 
a. First, the pymongo driver in python for connecting to MongoDB didn’t support a version for MongoDB less than 2.6 
b. Our code was in python and the Raspbian OS in our Raspberry Pi 3 only supported MongoDB version 2.4 
c. Cloud services offered by MongoDB which is MongoDB atlas too couldn’t be accessed from the Raspbian OS 
2. The SMS service which we decided to use was Twilio, but couldn’t be used as they didn’t provide SMS service in our region 
3. Unavailability of a real-life database for water consumption in households

The Resolutions:
1. Used Google Firebase to create a real-time cloud database instead of MongoDB 
2. After Twilio, we came across Amazon Simple Notification Service, which is a notification service provided as part of Amazon Web Services, which resolved our SMS issue 
3. While checking the proper working of our device we used the same readings to create a database, which although does not relate to real-life household water consumption, saved us from creating a fake database with arbitrary values 
'''
summary2 ="Intelligent water flow analyzer to measure household water consumption metrics with alerting mechanism in case of water wastage. The alerts are sent to the household owners based upon a recommended water consumption for the area."
image_file2 ="post2.jpg" 
author_id2 =1 
post2 = Post(title = title2, content = content2, summary = summary2, image_file = image_file2, author_id = author_id2)

title3 = "Air Force Selection Board : An experience of a lifetime"
content3 = '''The Indian Air Force is one of the premier air forces globally, with it being the 4th largest in terms of its fleet and personnel. Being the son of an Indian Air Force officer, I have had the privilege of being an extended part of this esteemed organisation all my life. I had always been and continue to be enamoured with the lives defence officers lead. The charisma, work ethic, and sense of responsibility they have towards their nation, organisation, and troops is an inspiration. Though I had always wanted to be an engineer and continue with computer science, a part of my heart wanted to join the forces. I wanted to give it my one best shot. I thought it was not supposed to happen if I didn’t get selected. Thus, I decided to give the Air Force Common Admission Test on 21st February 2021 and successfully cleared it. Then came the step to choose a date for my five day Air force Selection Board (AFSB for short) Interview, and I decided to give it on 28th June 2021. I had three months to prepare for this interview process which had a selection rate of less than 3%. First, let me give you a 10,000 feet overview of the AFSB 5 day process - it is divided into 2 phases and candidates are judged on 15 officers' qualities through their conduct in performing a myriad of tasks. The first phase is a one-day elimination round where the candidates appear for two tasks - the first is an aptitude test, and the second is a picture perception and discussion test (PP&DT). In the second task, candidates are shown a picture for 60 seconds and are expected to form a story around the image and write in 4 minutes. Afterwards, candidates in a group of 6 - 10 are taken to a separate room to discuss their stories for 15 - 20 minutes. The discussion aims to reach a mutual story for the whole group. The second phase lasts for four days, followed by a Conference with the Selection Board members. The second phase is divided into a psychology assessment exercise, an outdoor group task, and a personal interview. The conference is, in effect, a short interview cum conversation session of 5 minutes with all the officers of the selection board. 

Now that we are done with the overview of the selection process, I will move on to my experience. Even though I had expected a shift in the lifestyle of being an officer and was prepared for it, when it came to doing it, I realised that it was not as easy as it seemed. We were a total of 210 candidates that arrived at the board fully dressed in formals sharp at 0600 hrs in the morning. Seeing so many people made me a bit nervous; however, I was confident in my abilities and preparation to clear the first phase. After the document verifications, we all were taken to the aptitude test area, then to an auditorium for the PP&DT test. I had practised my story writing speed and story formations in the three months I had to prepare. Thus, the story writing part went well. We were divided into a group of 10 and taken to an open area due to covid restrictions for the discussion. I had always been a good speaker. I made sure I listened to what others were saying and put thought behind my words before speaking. This made the discussion task a breeze. I was nominated to narrate the group story, and then the assessors took us all to another open area for the result announcement. My name was called out. I had cleared phase 1. After the announcement, out of 210 people, only 48 candidates who cleared stage 1 were taken to deposit all our electronic items - earphones, chargers, laptops, mobile phones or any Bluetooth device. The 48 candidates were divided into six groups of 8 candidates each and taken to our rooms. My teammates and I went to our room. The following four days were nothing I had expected them to be. All candidates were called for a fall in at 0600 hrs in the morning and evening, where we were expected to be bathed, dressed, and have finished our breakfast. Subsequently, our groups were taken to perform different tasks. Here, I keep referring to the tests as tasks simply because tasks don’t have a single correct answer, whereas tests do. All that was expected of us was to follow instructions, be ourselves and leave the assessment part to the assessors only. Lest we needlessly worry ourselves with unnecessary thoughts. I had a joyous time during all the tasks. Away from the internet or outside communication, spending time with the candidates who came from all parts of the country. We quickly became friends, had our meals together, played against other teams in the evening sports, and exchanged our life stories in between tasks when all were at our rooms. 

I did not clear the phase 2 assessment; however, I made friends I still stay in touch with today. I enjoyed myself there, and the experience was helpful in getting to know myself better.
'''
summary3 ="Being an Indian Air Force officer’s son, the lives led by our defence personnel had always been an inspiration to me. Though I had a passion for computers, a part of me wanted to give a shot at being an officer. This post is my experience of the selection process for being an officer in the Indian Air Force."
image_file3="post3.jpg" 
author_id3 = 1
post3 = Post(title = title3, content = content3, summary = summary3, image_file = image_file3, author_id = author_id3)

title4 = "BTech Group Project"
content4 ='''Information is drawn from numerous areas, channels, and stages together with
mobile phones, web-based media, online business locales, treatment studies, and web
look. The increment within the life of data accessible created the approach for one
more field of study addicted to giant information—the large informational collections
that augment the formation of higher operational instruments altogether areas.

Data is considered the new oil and has limitless potential in the coming future. Data
is being collected, stored, and studied whenever we interact with any smart device. In
this project, we are dealing with data that is retrieved from news articles of different
news providers namely Times of India, Hindustan Times, and The Hindu. As the
news articles, these days have become redundant and repetitive. The purpose of our
project is to cluster unsupervised news articles and then look for articles that are
redundant and remove them. Administrations that give news stories gathered from different distributors have gotten mainstream. In these administrations, the most recent articles appear on the top page and permit the client to look for news put away for some period.
Notwithstanding, since these benefits gather the articles from numerous distributors
and since new news stories are in effect persistently distributed, the measure of these
substances is turning out to be tremendous to the point that the client can not
effectively track down the ideal articles. To take care of this issue, Google News
bunches the news articles that talk about a similar news occasion as shown by the
comparability of the news titles. This can diminish the number of news stories that
appear to the client. Notwithstanding, this methodology presents a level rundown of
the list items to the client, which is not the most productive strategy.

To achieve this, first, we scraped the archives of the news providers and created our
dataset to work further upon. Then preprocessed the data which includes, cleaning of
stop words, punctuations, special characters, etc. then lemmatizing and tokenizing
them. This preprocessing data is further converted into word vectors for the topic
modeler- Latent Dirichlet Allocation (LDA) model - to feed. This model gives us a
topic distribution matrix and keywords for each topic. We then find similar articles
in their respective cluster using cosine similarity.

We filter the cosine similarities result which gives us the similarity between two
documents. The higher the similarity the more redundant the data in the articles.
'''
summary4 ="We have a lot of new articles online with the same content. To eliminate this problem, we created an application that can remove redundant news articles by clustering them using LDA and cosine similarity."
image_file4 ="post4.jpg" 
author_id4 = 1
post4 = Post(title = title4, content = content4, summary = summary4, image_file = image_file4, author_id = author_id4)


# add_post(post1)
# add_post(post2)
# add_post(post3)
add_post(post4)


