
- How many passengers survived, and how many died?
	- SELECT COUNT(*) FROM titanic_table WHERE "Survived" = 0;
		
- How many passengers were in each class?
	- SELECT COUNT(*) FROM titanic_table GROUP BY "Pclass";
	
- How many passengers survived/died within each class?
	- SELECT COUNT('Survived') FROM titanic_table
WHERE "Pclass" = 1 
GROUP BY "Survived";

- What was the average age of survivors vs nonsurvivors?
	- SELECT AVG("Age") FROM titanic_table
WHERE "Survived" = 0;

- What was the average age of each passenger class?
	- SELECT AVG("Age") FROM titanic_table
WHERE "Pclass" = 1;

- What was the average fare by passenger class? By survival?
	- SELECT AVG("Fare") FROM titanic_table
WHERE "Pclass" = 1;
	-SELECT AVG("Fare") FROM titanic_table
WHERE "Survived" = 1;

- How many siblings/spouses aboard on average, by passenger class? By survival?
	- SELECT AVG("Siblings/Spouses Aboard") FROM titanic_table
WHERE "Pclass" = 1;
	-SELECT AVG("Siblings/Spouses Aboard") FROM titanic_table
WHERE "Survived" = 0;

- How many parents/children aboard on average, by passenger class? By survival?
	- SELECT AVG("Parents/Children Aboard") FROM titanic_table
WHERE "Pclass" = 1;
	-SELECT AVG("Parents/Children Aboard") FROM titanic_table
WHERE "Survived" = 0;

- Do any passengers have the same name?
	- SELECT DISTINCT("Name") FROM titanic_table;






- (Bonus! Hard, may require pulling and processing with Python) How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name and with at least 1 sibling/spouse aboard are a married couple.
- ???






