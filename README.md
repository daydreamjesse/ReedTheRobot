# ReedTheRobot
Reed the Robot was created to generate headlines and read them out.

I accomplished this by using the BeautifulSoup library to scrape hundreds of thousands of Buzzfeed articles on their archives. Once I stored those in a local database, I converted sections of the database to .txt files to send through a machine learning algorithm that taught Reed how to make his own headlines.

Once the headlines were generated, Reed would say them out loud via TTS and then host a simple website that could act as a marquee when embedded into OBS.
