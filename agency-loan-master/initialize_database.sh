#!/bin/bash

# sudo -u postgres createuser owning_user
# sudo -u postgres -i

createdb agency-loan-level

# psql agency-loan-level -f C:\\Projects\\GitHub\\agency-loan-level-master\\db_scripts\\create_loans_and_supporting_tables.sql
psql agency-loan-level -f C:\\Projects\\GitHub\\agency-loan-level-master\\db_scripts\\create_loans_and_supporting_tables.sql

cat data/hpi_index_codes.txt | psql agency-loan-level -c "COPY hpi_indexes FROM stdin DELIMITER '|' NULL '';"
cat data/interpolated_hpi_values.txt | psql agency-loan-level -c "COPY hpi_values FROM stdin DELIMITER '|' NULL '';"
cat data/pmms.csv | psql agency-loan-level -c "COPY mortgage_rates FROM stdin NULL '' CSV HEADER;"
cat data/msa_county_mapping.csv | psql agency-loan-level -c "COPY raw_msa_county_mappings FROM stdin NULL '' CSV HEADER;"

function pause(){
   read -p "$*"
}
 
# ...
# call it
pause 'Press [Enter] key to continue...'
# rest of the script
# ...