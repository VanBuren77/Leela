import typing
import pandas as pd
import numpy as np
import os
import sys


from leela.utils.utils import Utils
from leela.database.database import Database
import leela.config.config as config

# import psycopg

def load_fannie():

    db_name = "agency-loan-level"
    process_sql_file = "C:\Projects\GitHub\Leela\leela\database\sql\load_fannie.sql"

    # EEL: Each of these are a disconnect/ reconnect. Wondering if I can set up to do single connection;

    DATA_DIR = r"data\Fannie\zips"
    TEMP_ZIP_OUT_DIR = r"data\Fannie\temp"
    DEBUG = True
    
    MAX_FILE_LOAD = 21
    FILE_LOAD_COUNTER = 0
    file_list = os.listdir(DATA_DIR)
    file_list.reverse()

    for file_name in file_list:

        zip_file_path = os.path.join(DATA_DIR, file_name)
        csv_file_path = f"""{TEMP_ZIP_OUT_DIR}\\{file_name.replace(".zip", ".csv")}"""

        print()
        print("==============================================")
        print(f"Processing: {zip_file_path}")
        print(f"Loading: {csv_file_path}")
        print("==============================================")

        if ".zip" in zip_file_path and "sample" not in zip_file_path:
            # create_index_command = f"""psql --dbname="{db_name}" --command="CREATE INDEX idx_loan_id_monthly_raw ON raw_fannie (loan_id, monthly_reporting_period DESC);" """
            # insert_raw_command = f"type {file_path} psql agency-loan-level COPY raw_fannie  FROM stdin DELIMITER '|' NULL '';"
            # analyze_command = f"""psql --dbname="{db_name}" --command="ANALYZE verbose fannie_processed;" """
            # set_utf_command = f"""psql --dbname="{db_name}" --command="SET CLIENT_ENCODING TO 'WIN1252';" """

            # set_utf_command = f"""psql --dbname="{db_name}" --command="SET CLIENT_ENCODING TO 'utf8';" """
            unzip_command = f"""7z e "{zip_file_path}" "-o{TEMP_ZIP_OUT_DIR}" """
            drop_index_command = f"""psql --dbname="{db_name}" --command="DROP INDEX IF EXISTS idx_loan_id_monthly_raw;" """
            unlog_command = f"""psql --dbname="{db_name}" --command="ALTER TABLE public.raw_fannie SET UNLOGGED;"  """
            insert_raw_command = f"""psql --dbname="{db_name}" --command="\copy public.raw_fannie (reference_pool_id, loan_id, monthly_reporting_period, channel, seller_name, servicer_name, master_servicer, original_interest_rate, current_interest_rate, original_upb, upb_at_issuance, current_actual_upb, original_loan_term, origination_date, first_payment_date, loan_age, remaining_months_to_legal_maturity, remaining_months_to_maturitry, maturity_date, oltv, ocltv, number_of_borrowers, dti, borrower_credit_score_at_origination, coborrower_credit_score_at_origination, first_time_buyer_flag, loan_purpose, property_type, number_of_units, occupancy_status, property_state, msa, zip_code_short, mortgage_insurance_pct, amortization_type, prepayment_penalty_indicator, interest_only_indicator, interest_only_first_prin_and_int_pay_dt, months_to_amortization, current_loan_delinq_status, loan_payment_history, modification_flag, mortgage_insurance_cancellation_indicator, zero_balance_code, zero_balance_effective_date, upb_at_time_of_removal, repurchase_date, scheduled_principcal_current, total_principal_current, unscheduled_principal_current, last_paid_installment_date, foreclosure_date, disposition_date, foreclosure_costs, property_preservation_and_repair_costs, asset_recovery_costs, misc_holding_expenses_and_credit, associated_taxes_for_holding_property, net_sales_proceeds, credit_enhancement_proceeds, repurchase_make_whole_proceeds, other_foreclosure_proceeds, non_interest_bearing_upb, principal_forgiveness_amount, original_list_start_date, original_list_price, current_list_start_date, current_list_price, borrower_credit_score_at_issuance, coborrower_credit_score_at_issuance, borrower_credit_score_current, coborrower_credit_score_current, mortgage_insurance_type, servicing_activity_indicator, current_period_modification_loss_amount, cumulative_modification_loss_amount, current_period_credit_event_net_gain_or_loss, cumulative_credit_event_net_gain_or_loss, home_ready_program_indicator, foreclosure_principcal_write_off_amount, relocation_mortgage_indicator, zero_balance_code_change_date, loan_holdback_indicator, loan_holdback_effective_date, delinquent_accrued_interest, property_valuation_method, high_balance_loan_indicator, arm_init_fixed_rate_period_5yr, arm_product_type, initial_fixed_rate_period, interest_rate_adj_freq, next_interest_rate_adj_date, next_payment_change_date, index_col, arm_cap_structure, initial_interest_rate_cap_up_pct, periodic_interest_rate_cap_up_pct, lifetime_interest_rate_cap_up_pct, mortgage_margin, arm_balloon_indicator, arm_plan_number, borrower_assistance_plan, hltv_refi_option_indicator, deal_name, repurchase_make_whole_proceeds_flag, alternative_delinq_resolution, alternative_delinq_resolution_count, total_deferral_amount) FROM '{csv_file_path}' DELIMITER '|' CSV " """
            relog_command = f"""psql --dbname="{db_name}" --command="ALTER TABLE public.raw_fannie SET LOGGED;" """
            process_raw_data_command = f"""psql --dbname="{db_name}" -f {process_sql_file} """
            
            delete_command = f"""del {csv_file_path}"""
            
            commands = {
                "Unzipping" : unzip_command,
                # "Setting UTF Encoding" : set_utf_command,
                "Dropping Index" : drop_index_command,
                "Unlogging Table" : unlog_command,
                "Copying Data" : insert_raw_command,
                "Relogging Table" : relog_command,
                "Postprocessing" : process_raw_data_command,
                "Deleting Temp" : delete_command,
            }

            for key in commands:
                if DEBUG:
                    print(key)
                os.system(commands[key])
            
            if MAX_FILE_LOAD < FILE_LOAD_COUNTER:
                break
            
            FILE_LOAD_COUNTER += 1

    print(f"All Done.")


    # Load file from STD IN ->


    # ------------------- #
    # Insert into tables ->
    # ------------------- #
    
    # load_fannie_sql = "leela\database\sql\load_fannie.sql"
    # all_sql = open(load_fannie_sql).read().split(";")
    
    # for sql in all_sql:
        # print(sql)


# import os
# # assign directory
# directory = 'files'
#
# # iterate over files in
# # that directory
# for filename in os.listdir(directory):
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         print(f)
#
# all_sql = []
#
# BUFFER_SIZE = 100
#
# for file_name in os.listdir(DATA_DIR):
#     file_path = os.path.join(DATA_DIR, file_name)
#     print(file_path)
#
#     if ".csv" in file_path:
#         fh = open(file_path)
#         number_of_lines = 3
#         for i in range(number_of_lines): 
#             line = fh.readline()
#         print(line)
#         # df = pd.read_csv(file_path, delimiter="|")
#         # all_sql.append(Utils.sql_insert_statement_from_df(df, "loans_raw_fannie"))