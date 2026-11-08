SELECT g.nazwa, COUNT(*) FROM oceny_txt o
INNER JOIN gry_txt g ON g.id_gry=o.id_gry
GROUP BY o.id_gry
ORDER BY COUNT(*) DESC

SELECT g.nazwa, AVG(o.ocena) FROM oceny_txt o
INNER JOIN gry_txt g ON g.id_gry=o.id_gry WHERE g.kategoria='imprezowa'
GROUP BY o.id_gry
ORDER BY o.id_gry DESC