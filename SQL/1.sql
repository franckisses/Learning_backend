
# 牛 确实是牛！

SELECT id, 
       MAX(drink) OVER (PARTITION BY grp) AS drink
FROM (
    SELECT id
    , drink
    , rn
    , SUM(CASE WHEN drink IS NULL THEN 0 ELSE 1 END) OVER (ORDER BY rn) AS grp
    FROM (
        SELECT id
        , drink
        , ROW_NUMBER() OVER () AS rn
	    FROM CoffeeShop
    ) t1
) t2
ORDER BY rn
