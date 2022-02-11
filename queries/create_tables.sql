CREATE TABLE Topics (
    TopicID int AUTO_INCREMENT PRIMARY KEY,
	Name varchar(1000),
    EngDescription varchar(500),
    NumberInChronology INT NOT NULL
);

CREATE TABLE Tags (
    TagID int AUTO_INCREMENT PRIMARY KEY,
	Name varchar(100)
);

CREATE TABLE Posts (
    PostID int AUTO_INCREMENT PRIMARY KEY,
    TopicID int,
    Header varchar(1000),
    TextHtml text,
    ReferencesHtml text,
    ImagePath_Original varchar(255),
    EngDescription varchar(500),
    ShortText varchar(1000),
    FOREIGN KEY(TopicID) 
       REFERENCES Topics(TopicID)
);

CREATE TABLE PostsTags (
	PostID int,
    TagID int,
	PRIMARY KEY(PostID,TagID),
    FOREIGN KEY(PostID) 
       REFERENCES Posts(PostID),
    FOREIGN KEY(TagId) 
       REFERENCES Tags(TagID)
);