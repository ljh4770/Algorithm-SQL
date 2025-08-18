SELECT id,
    CASE 
    WHEN P.percentile <= 0.25 THEN "CRITICAL"
    WHEN P.percentile <= 0.50 THEN "HIGH"
    WHEN P.percentile <= 0.75 THEN "MEDIUM"
    WHEN P.percentile <= 1.00 THEN "LOW"
    END AS colony_name
FROM (
    SELECT id, PERCENT_RANK() OVER (
        ORDER BY size_of_colony DESC
    ) AS percentile
    FROM ECOLI_DATA
) AS P
ORDER BY id ASC;