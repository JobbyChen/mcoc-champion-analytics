-- Average illustrative attributes by champion class
SELECT class, COUNT(*) AS champion_count,
       ROUND(AVG(offense), 1) AS avg_offense,
       ROUND(AVG(survivability), 1) AS avg_survivability,
       ROUND(AVG(utility), 1) AS avg_utility
FROM champions GROUP BY class ORDER BY class;
