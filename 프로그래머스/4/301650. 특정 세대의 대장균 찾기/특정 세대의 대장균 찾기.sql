/*
3세대의 대장균

 ID 에 대해 오름차순 정렬
*/

# 1세대 -> PARENT_ID IS NULL
# 2세대 -> 1세대ID 가 PARENT_ID
# 3TPEO -> 2세대ID 가 PARENT_ID


SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN (
    # 2세대 ID 선택
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IN (
        # 1세대 ID 선택
        SELECT ID
        FROM ECOLI_DATA
        WHERE PARENT_ID IS NULL
    )
)
ORDER BY ID ASC;



