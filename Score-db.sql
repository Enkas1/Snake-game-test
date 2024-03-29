CREATE TABLE highscore_list (
    score INT NOT NULL,
    name TEXT
);

CREATE VIEW sorted_score_list AS
SELECT name, score
FROM highscore_list
ORDER BY score DESC;

DROP TABLE highscore_list CASCADE;
DROP VIEW sorted_score_list;
