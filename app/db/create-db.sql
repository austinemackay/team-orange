-- Reading table
DROP TABLE IF EXISTS reading;
CREATE TABLE reading
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER,
    name CHAR(40) NOT NULL,
    creation_time INTEGER,
    text CHAR(500) NOT NULL,
    translation CHAR(20) NOT NULL,
    CONSTRAINT author_id_fk FOREIGN KEY (author_id) REFERENCES user (id)
);
CREATE UNIQUE INDEX reading_id_uindex ON reading (id);

-- Content table
DROP TABLE IF EXISTS content;
CREATE TABLE content
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER,
    content_type INTEGER,
    name CHAR(40) NOT NULL,
    creation_time INTEGER,
    approved BOOLEAN DEFAULT FALSE,
    description CHAR(1000) NOT NULL,
    CONSTRAINT content_id_fk FOREIGN KEY (content_type) REFERENCES content_type (id),
    CONSTRAINT author_id_fk FOREIGN KEY (author_id) REFERENCES user (id)
);
CREATE UNIQUE INDEX content_id_uindex ON content (id);

-- Reading Passages table
DROP TABLE IF EXISTS reading_passages;
CREATE TABLE reading_passages
(
    reading_id INTEGER,
    BG_passage_reference text
);

-- Reading Content table
DROP TABLE IF EXISTS reading_content;
CREATE TABLE reading_content
(
    reading_id INTEGER,
    content_id INTEGER,
    PRIMARY KEY (reading_id,content_id)
);

-- Content Type table
DROP TABLE IF EXISTS content_type;
CREATE TABLE content_type
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(40) NOT NULL
);
CREATE UNIQUE INDEX content_type_id_uindex ON content_type (id);

-- User table
DROP TABLE IF EXISTS user;
CREATE TABLE user
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_address VARCHAR(320) NOT NULL,
    password CHAR(100) NOT NULL,
    first_name CHAR(100) NOT NULL,
    last_name CHAR(100) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    creation_time INTEGER NOT NULL,
    UNIQUE (id, email_address)
);


-- Group table
DROP TABLE IF EXISTS user_group;
CREATE TABLE user_group
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(100) NOT NULL,
    public BOOLEAN NOT NULL,
    creation_time DATE,
    description CHAR(500) NOT NULL
);
CREATE UNIQUE INDEX group_id_uindex ON 'user_group' (id);

--Group Invitation table
DROP TABLE IF EXISTS group_invitation;
CREATE TABLE group_invitation
(
    user_id INTEGER,
    group_id INTEGER,
    creation_time timestamp,
    PRIMARY KEY (user_id, group_id)
);

-- Plan table
DROP TABLE IF EXISTS plans;
CREATE TABLE plans
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id_fk INTEGER,
    name CHAR(40) NOT NULL,
    creation_time INTEGER,
    description CHAR(1000) NOT NULL,
    FOREIGN KEY (author_id_fk) REFERENCES user (id)
);
CREATE UNIQUE INDEX plans_id_uindex ON plans (id);

-- Reading Plan table
DROP TABLE IF EXISTS plan_reading;
CREATE TABLE plan_reading
(
    plans_id INTEGER,
    reading_id INTEGER,
    start_time_offset INTEGER,
    end_time_offset INTEGER,
    PRIMARY KEY (plans_id,reading_id)
);

-- Subscription table
DROP TABLE IF EXISTS subscription;
CREATE TABLE subscription
(
    plans_id INTEGER,
    user_id INTEGER,
    creation_time INTEGER,
    PRIMARY KEY (plans_id,user_id)
);

-- Group Subscription table
DROP TABLE IF EXISTS group_subscription;
CREATE TABLE group_subscription
(
    plans_id INTEGER,
    group_id INTEGER,
    creation_time INTEGER,
    PRIMARY KEY (plans_id,group_id)
);

-- Feedback table
DROP TABLE IF EXISTS feedback;
CREATE TABLE feedback
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id_fk INTEGER,
    plan_id_fk INTEGER,
    content_id_fk INTEGER,
    reading_id_fk INTEGER,
    comment CHAR(1000) NOT NULL,
    creation_time INTEGER,

    FOREIGN KEY (author_id_fk) REFERENCES user (id),
    FOREIGN KEY (plan_id_fk) REFERENCES plan (id),
    FOREIGN KEY (content_id_fk) REFERENCES content (id),
    FOREIGN KEY (reading_id_fk) REFERENCES reading (id)
);
CREATE UNIQUE INDEX feedback_id_uindex ON feedback (id);

-- Post table
DROP TABLE IF EXISTS post;
CREATE TABLE post
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id_fk INTEGER,
    approved BOOLEAN DEFAULT TRUE,
    time INT,
    message CHAR(1000) NOT NULL,
    FOREIGN KEY (user_id_fk) REFERENCES user(id)
);
CREATE UNIQUE INDEX post_id_uindex ON post(id);

-- Connect posts to readings
DROP TABLE IF EXISTS reading_post;
CREATE TABLE reading_post
(
    reading_id INT,
    post_id INT,
    PRIMARY KEY (reading_id, post_id),
    FOREIGN KEY (reading_id) REFERENCES reading(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);

-- Connect posts to groups
DROP TABLE IF EXISTS group_post;
CREATE TABLE group_post
(
    group_id INT,
    post_id INT,
    PRIMARY KEY (group_id, post_id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (post_id) REFERENCES post(id)
);
