createdb agency-loan-level passwd=test

psql agency-loan-level -f db_scripts\create_loans_and_supporting_tables.sql

type data/hpi_index_codes.txt | psql agency-loan-level -c "COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';"
type data/interpolated_hpi_values.txt | psql agency-loan-level -c "COPY hpi_values FROM stdin DELIMITER '|' NULL '';"
type data/pmms.csv | psql agency-loan-level -c "COPY mortgage_rates FROM stdin NULL '' CSV HEADER;"
type data/msa_county_mapping.csv | psql agency-loan-level -c "COPY raw_msa_county_mappings FROM stdin NULL '' CSV HEADER;"