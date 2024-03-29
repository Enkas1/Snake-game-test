CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE highscores (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players(id),
    score INTEGER NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE VIEW sorted_score_list AS
SELECT p.name, h.score
FROM highscores h
JOIN players p ON h.player_id = p.id
ORDER BY h.score DESC; 


DROP TABLE highscores CASCADE;
DROP VIEW sorted_score_list;

