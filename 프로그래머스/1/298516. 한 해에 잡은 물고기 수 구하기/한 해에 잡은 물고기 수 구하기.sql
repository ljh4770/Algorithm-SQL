# 2021 물고기 출력 -> FISH_COUNT
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021;