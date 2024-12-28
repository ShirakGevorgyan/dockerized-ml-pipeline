
CREATE TABLE IF NOT EXISTS gene_data (
    id SERIAL PRIMARY KEY,
    gene_one FLOAT NOT NULL,
    gene_two FLOAT NOT NULL,
    cancer_present INT NOT NULL
);

COPY gene_data(gene_one, gene_two, cancer_present)
FROM '/data/gene_expression.csv'
DELIMITER ','
CSV HEADER;
