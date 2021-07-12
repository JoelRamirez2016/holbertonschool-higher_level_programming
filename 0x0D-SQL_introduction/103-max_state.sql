-- script that displays the max temperature of each statescript that displays the max temperature of each state
SELECT state, MAX(value) max_temp FROM temperatures GROUP BY state
