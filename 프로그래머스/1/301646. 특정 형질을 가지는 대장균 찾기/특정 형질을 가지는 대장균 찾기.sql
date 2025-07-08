SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE (
    GENOTYPE & 2 = 0
    AND (GENOTYPE & 1 = 1
        OR GENOTYPE & 4 = 4) 
);

# 1 -> 01 -> 1
# 2 -> 10 -> 2
# 3 -> 100 -> 4
# 4 -> 1000 -> 8