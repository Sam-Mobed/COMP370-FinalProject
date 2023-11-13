# COMP370-FinalProject
The Final Project for COMP370

-> we want to understand how Taylor Swift is being covered in the media.
-> we ONLY want North American Coverage

-> we want to know the extent to which the coverage is positive or negative
    (we need pos,neg and neutral. Think of articles who discuss her early life.)
    (unless we are exclusively looking for pos/neg coverage of her music, movies, politics, etc.)
->the topics the coverage focuses on (each article belongs to one topic)


How do we make sure it's only NA articles??
- when you make a request you can specify a value for 'country='
I think this request parameter accepts a single value, so we can't have country=us&ca or wtv.
Also, we're looking for north american news outlets, but should we exclude mexico? it'll be hard to analyze since it's in spanish. (depending on the endpoint we use, we might be able to use the language= parameter, which would solve this problem.)

we can use the newsapi-python module instead of going through the requests library, doesnt change much.
aside: everyone should have a venv setup for the project.

Keywords we are looking for:
Taylor Swift
Taylor Alison Swift
The Eras Tour
The Eras Tour Concert Film
Taylor Swift Career
Taylor Swift Legacy
Taylor Swift Acting
Taylor Swift Cultural Status
Taylor Swift Social activism
Taylor Swift Public image
Taylor Swift Philantropy

Taylor Swift 1989
Taylor Swift Lover
Taylor Swift reputation
Taylor Swift Midnights
Taylor Swift Speak Now
Taylor Swift The More Red
Taylor Swift Fearless
Taylor Swift Red
Taylor Swift Folklore
Taylor Swift Evermore

(but these aren't about positive or negative coverage, so should we exclude them?)
Taylor Swift Travis Kelce
Taylor Swift Biography
Taylor Swift Early Life
Taylor Swift Career Beginnings
