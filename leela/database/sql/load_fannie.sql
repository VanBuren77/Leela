INSERT INTO public.fannie_processed 
SELECT 
  reference_pool_id,
  loan_id,
  to_date(monthly_reporting_period,'MMYYYY'),
  channel,
  seller_name,
  servicer_name,
  master_servicer,
  original_interest_rate,
  current_interest_rate,
  original_upb,
  upb_at_issuance,
  current_actual_upb,
  original_loan_term,
  to_date(origination_date,'MMYYYY'),
  to_date(first_payment_date,'MMYYYY'),
  loan_age,
  remaining_months_to_legal_maturity,
  remaining_months_to_maturitry,
  to_date(maturity_date,'MMYYYY'),
  oltv,
  ocltv,
  number_of_borrowers,
  dti,
  borrower_credit_score_at_origination,
  coborrower_credit_score_at_origination,
  first_time_buyer_flag,
  loan_purpose,
  property_type,
  number_of_units,
  occupancy_status,
  property_state,
  msa,
  zip_code_short,
  mortgage_insurance_pct,
  amortization_type,
  prepayment_penalty_indicator,
  interest_only_indicator,
  to_date(interest_only_first_prin_and_int_pay_dt,'MMYYYY'),
  months_to_amortization,
  current_loan_delinq_status,
  loan_payment_history,
  modification_flag,
  mortgage_insurance_cancellation_indicator,
  zero_balance_code,
  to_date(zero_balance_effective_date,'MMYYYY'),
  upb_at_time_of_removal,
  to_date(repurchase_date,'MMYYYY'),
  scheduled_principcal_current,
  total_principal_current,
  unscheduled_principal_current,
  to_date(last_paid_installment_date,'MMYYYY'),
  to_date(foreclosure_date,'MMYYYY'),
  to_date(disposition_date,'MMYYYY'),
  foreclosure_costs,
  property_preservation_and_repair_costs,
  asset_recovery_costs,
  misc_holding_expenses_and_credit,
  associated_taxes_for_holding_property,
  net_sales_proceeds,
  credit_enhancement_proceeds,
  repurchase_make_whole_proceeds,
  other_foreclosure_proceeds,
  non_interest_bearing_upb,
  principal_forgiveness_amount,
  to_date(original_list_start_date,'MMYYYY'),
  original_list_price,
  to_date(current_list_start_date,'MMYYYY'),
  current_list_price,
  borrower_credit_score_at_issuance,
  coborrower_credit_score_at_issuance,
  borrower_credit_score_current,
  coborrower_credit_score_current,
  mortgage_insurance_type,
  servicing_activity_indicator,
  current_period_modification_loss_amount,
  cumulative_modification_loss_amount,
  current_period_credit_event_net_gain_or_loss,
  cumulative_credit_event_net_gain_or_loss,
  home_ready_program_indicator,
  foreclosure_principcal_write_off_amount,
  relocation_mortgage_indicator,
  to_date(zero_balance_code_change_date,'MMYYYY'),
  loan_holdback_indicator,
  to_date(loan_holdback_effective_date,'MMYYYY'),
  delinquent_accrued_interest,
  property_valuation_method,
  high_balance_loan_indicator,
  arm_init_fixed_rate_period_5yr,
  arm_product_type,
  initial_fixed_rate_period,
  interest_rate_adj_freq,
  to_date(next_interest_rate_adj_date,'MMYYYY'),
  to_date(next_payment_change_date,'MMYYYY'),
  index_col,
  arm_cap_structure,
  initial_interest_rate_cap_up_pct,
  periodic_interest_rate_cap_up_pct,
  lifetime_interest_rate_cap_up_pct,
  mortgage_margin,
  arm_balloon_indicator,
  arm_plan_number,
  borrower_assistance_plan,
  hltv_refi_option_indicator,
  deal_name,
  repurchase_make_whole_proceeds_flag,
  alternative_delinq_resolution,
  alternative_delinq_resolution_count,
  total_deferral_amount
FROM public.raw_fannie;




delete from public.raw_fannie;



CREATE OR REPLACE INDEX 














-- DROP INDEX IF EXISTS idx_loan_id_monthly_raw;
-- ALTER TABLE raw_fannie SET UNLOGGED;
-- COPY TO public.raw_fannie (reference_pool_id, loan_id, monthly_reporting_period, channel, seller_name, servicer_name, master_servicer, original_interest_rate, current_interest_rate, original_upb, upb_at_issuance, current_actual_upb, original_loan_term, origination_date, first_payment_date, loan_age, remaining_months_to_legal_maturity, remaining_months_to_maturitry, maturity_date, oltv, ocltv, number_of_borrowers, dti, borrower_credit_score_at_origination, coborrower_credit_score_at_origination, first_time_buyer_flag, loan_purpose, property_type, number_of_units, occupancy_status, property_state, msa, zip_code_short, mortgage_insurance_pct, amortization_type, prepayment_penalty_indicator, interest_only_indicator, interest_only_first_prin_and_int_pay_dt, months_to_amortization, current_loan_delinq_status, loan_payment_history, modification_flag, mortgage_insurance_cancellation_indicator, zero_balance_code, zero_balance_effective_date, upb_at_time_of_removal, repurchase_date, scheduled_principcal_current, total_principal_current, unscheduled_principal_current, last_paid_installment_date, foreclosure_date, disposition_date, foreclosure_costs, property_preservation_and_repair_costs, asset_recovery_costs, misc_holding_expenses_and_credit, associated_taxes_for_holding_property, net_sales_proceeds, credit_enhancement_proceeds, repurchase_make_whole_proceeds, other_foreclosure_proceeds, non_interest_bearing_upb, principal_forgiveness_amount, original_list_start_date, original_list_price, current_list_start_date, current_list_price, borrower_credit_score_at_issuance, coborrower_credit_score_at_issuance, borrower_credit_score_current, coborrower_credit_score_current, mortgage_insurance_type, servicing_activity_indicator, current_period_modification_loss_amount, cumulative_modification_loss_amount, current_period_credit_event_net_gain_or_loss, cumulative_credit_event_net_gain_or_loss, home_ready_program_indicator, foreclosure_principcal_write_off_amount, relocation_mortgage_indicator, zero_balance_code_change_date, loan_holdback_indicator, loan_holdback_effective_date, delinquent_accrued_interest, property_valuation_method, high_balance_loan_indicator, arm_init_fixed_rate_period_5yr, arm_product_type, initial_fixed_rate_period, interest_rate_adj_freq, next_interest_rate_adj_date, next_payment_change_date, index_col, arm_cap_structure, initial_interest_rate_cap_up_pct, periodic_interest_rate_cap_up_pct, lifetime_interest_rate_cap_up_pct, mortgage_margin, arm_balloon_indicator, arm_plan_number, borrower_assistance_plan, hltv_refi_option_indicator, deal_name, repurchase_make_whole_proceeds_flag, alternative_delinq_resolution, alternative_delinq_resolution_count, total_deferral_amount) FROM '{file_path}' DELIMITER '|' CSV;


-- Keep 
-- INSERT INTO servicers (name)
-- SELECT DISTINCT servicer_name FROM monthly_observations_raw_fannie
-- WHERE servicer_name IS NOT NULL
-- AND servicer_name NOT IN (SELECT name FROM servicers WHERE name IS NOT NULL);

-- INSERT INTO servicers (name)
-- SELECT DISTINCT seller_name FROM loans_raw_fannie
-- WHERE seller_name IS NOT NULL
-- AND seller_name NOT IN (SELECT name FROM servicers WHERE name IS NOT NULL);

-- CREATE INDEX tmp_idx_monthly ON monthly_observations_raw_fannie (loan_sequence_number, reporting_period DESC);

-- CREATE TABLE tmp_msas AS
-- SELECT DISTINCT ON (loan_sequence_number)
--   loan_sequence_number,
--   msa AS most_recent_msa
-- FROM monthly_observations_raw_fannie
-- WHERE msa IS NOT NULL
--   AND msa != 0
-- ORDER BY loan_sequence_number, reporting_period DESC;

-- CREATE TABLE tmp_original_servicers AS
-- SELECT DISTINCT ON (loan_sequence_number)
--   m.loan_sequence_number,
--   s.id AS original_servicer_id
-- FROM monthly_observations_raw_fannie m
--   INNER JOIN servicers s
--     ON m.servicer_name = s.name
-- ORDER BY m.loan_sequence_number, m.reporting_period ASC;

-- CREATE TABLE tmp_months_with_zero_balance_code AS
-- SELECT
--   loan_sequence_number,
--   reporting_period,
--   NULLIF(zero_balance_code, '')::integer AS zero_balance_code,
--   to_date(zero_balance_date, 'MM/YYYY') AS zero_balance_date,
--   last_paid_installment_date,
--   foreclosure_date,
--   disposition_date,
--   foreclosure_costs,
--   preservation_and_repair_costs,
--   asset_recovery_costs,
--   miscellaneous_expenses,
--   associated_taxes,
--   net_sale_proceeds,
--   credit_enhancement_proceeds,
--   repurchase_make_whole_proceeds,
--   other_foreclosure_proceeds,
--   non_interest_bearing_upb,
--   principal_forgiveness_upb,
--   repurchase_make_whole_proceeds_flag,
--   foreclosure_principal_write_off_amount,
--   servicing_activity_indicator,
--   ROW_NUMBER() OVER (PARTITION BY loan_sequence_number ORDER BY reporting_period ASC) AS row_num
-- FROM monthly_observations_raw_fannie
-- WHERE zero_balance_code IS NOT NULL;
-- CREATE INDEX idx_mz ON tmp_months_with_zero_balance_code (loan_sequence_number);

-- CREATE TABLE tmp_months_with_dq_status AS
-- SELECT
--   loan_sequence_number,
--   MIN(reporting_period) AS first_serious_dq_date
-- FROM monthly_observations_raw_fannie
-- WHERE dq_status IN ('2','3','4','5','6')
-- GROUP BY loan_sequence_number;

-- INSERT INTO loans (
--   agency_id, credit_score, first_payment_date, first_time_homebuyer_flag,
--   maturity_date, msa, mip, number_of_units, occupancy_status, ocltv, dti,
--   original_upb, oltv, original_interest_rate, channel, prepayment_penalty_flag,
--   product_type, property_state, property_type, postal_code,
--   loan_sequence_number, loan_purpose, original_loan_term, number_of_borrowers,
--   seller_id, servicer_id, vintage, hpi_index_id, hpi_at_origination,
--   final_zero_balance_code, final_zero_balance_date, first_serious_dq_date,
--   sato, co_borrower_credit_score, mortgage_insurance_type,
--   relocation_mortgage_indicator, pre_harp_loan_sequence_number
-- )
-- SELECT
--   (SELECT id FROM agencies WHERE name = 'Fannie Mae'),
--   credit_score,
--   to_date(first_payment_date, 'MM/YYYY'),
--   first_time_homebuyer_indicator,
--   (to_date(first_payment_date, 'MM/YYYY') + original_loan_term * '1 month'::interval)::date,
--   tmp_msas.most_recent_msa,
--   mip,
--   number_of_units::integer,
--   CASE occupancy_status WHEN 'P' THEN 'O' WHEN 'S' THEN 'S' WHEN 'I' THEN 'I' END,
--   original_cltv,
--   dti,
--   original_upb,
--   original_ltv,
--   original_interest_rate,
--   channel,
--   'N', -- fannie data excludes loans with prepayment penalty
--   product_type,
--   property_state,
--   property_type,
--   (zip_code || '00')::integer,
--   l.loan_sequence_number,
--   CASE loan_purpose WHEN 'P' THEN 'P' WHEN 'C' THEN 'C' WHEN 'R' THEN 'N' WHEN 'U' THEN 'U' END,
--   original_loan_term,
--   number_of_borrowers,
--   sel.id,
--   ser.original_servicer_id,
--   EXTRACT('year' FROM to_date(first_payment_date, 'MM/YYYY')),
--   COALESCE(COALESCE(hpi_msa.id, hpi_state.id), 0),
--   hpi.hpi,
--   mz.zero_balance_code,
--   mz.zero_balance_date,
--   md.first_serious_dq_date,
--   original_interest_rate - (CASE WHEN original_loan_term <= 180
--                             THEN rates.zero_point_rate_15_year
--                             ELSE rates.zero_point_rate_30_year
--                             END),
--   co_borrower_credit_score,
--   mortgage_insurance_type,
--   relocation_mortgage_indicator,
--   harp.pre_harp_loan_sequence_number
-- FROM loans_raw_fannie l
--   LEFT JOIN servicers sel
--     ON l.seller_name = sel.name
--   LEFT JOIN tmp_original_servicers ser
--     ON l.loan_sequence_number = ser.loan_sequence_number
--   LEFT JOIN tmp_msas
--     ON l.loan_sequence_number = tmp_msas.loan_sequence_number
--   LEFT JOIN tmp_months_with_zero_balance_code mz
--     ON l.loan_sequence_number = mz.loan_sequence_number
--     AND mz.row_num = 1
--   LEFT JOIN tmp_months_with_dq_status md
--     ON l.loan_sequence_number = md.loan_sequence_number
--   LEFT JOIN hpi_indexes hpi_msa
--     ON tmp_msas.most_recent_msa = hpi_msa.id AND (to_date(first_payment_date, 'MM/YYYY') - interval '1 month') > hpi_msa.first_date
--   LEFT JOIN hpi_indexes hpi_state
--     ON l.property_state = hpi_state.name
--   LEFT JOIN hpi_values hpi
--     ON hpi.hpi_index_id = COALESCE(COALESCE(hpi_msa.id, hpi_state.id), 0)
--     AND hpi.date = (to_date(first_payment_date, 'MM/YYYY') - interval '2 months')
--   LEFT JOIN mortgage_rates rates
--     ON rates.month = (to_date(first_payment_date, 'MM/YYYY') - interval '2 months')
--   LEFT JOIN fannie_harp_mapping harp
--     ON l.loan_sequence_number = harp.post_harp_loan_sequence_number;

-- INSERT INTO monthly_observations (
--   loan_id, date, current_upb, previous_upb, dq_status, previous_dq_status,
--   loan_age, rmm, repurchase_flag, modification_flag, zero_balance_code,
--   zero_balance_date, current_interest_rate
-- )
-- SELECT
--   loan_id,
--   date,
--   current_upb,
--   CASE WHEN previous_date IS NULL OR previous_date = date - '1 month'::interval THEN previous_upb END,
--   dq_status,
--   CASE WHEN previous_date IS NULL OR previous_date = date - '1 month'::interval THEN previous_dq_status END,
--   loan_age,
--   rmm,
--   repurchase_flag,
--   modification_flag,
--   zero_balance_code,
--   zero_balance_date,
--   current_interest_rate
-- FROM (
--   SELECT
--     l.id AS loan_id,
--     m.reporting_period AS date,
--     LAG(m.reporting_period, 1) OVER (PARTITION BY l.id ORDER BY m.reporting_period ASC) AS previous_date,
--     m.current_upb,
--     LAG(m.current_upb, 1) OVER (PARTITION BY l.id ORDER BY m.reporting_period ASC) AS previous_upb,
--     NULLIF(m.dq_status, 'X')::integer AS dq_status,
--     LAG(NULLIF(m.dq_status, 'X')::integer, 1) OVER (PARTITION BY l.id ORDER BY m.reporting_period ASC) AS previous_dq_status,
--     m.loan_age,
--     m.rmm,
--     m.repurchase_make_whole_proceeds_flag AS repurchase_flag,
--     m.modification_flag,
--     NULLIF(m.zero_balance_code, '')::integer AS zero_balance_code,
--     to_date(m.zero_balance_date, 'MM/YYYY') AS zero_balance_date,
--     m.current_interest_rate
--   FROM monthly_observations_raw_fannie m
--     INNER JOIN loans l
--       ON m.loan_sequence_number = l.loan_sequence_number
--       AND l.agency_id = 0
-- ) subquery;

-- INSERT INTO zero_balance_monthly_observations (
--   loan_id, date, zero_balance_code, zero_balance_date,
--   last_paid_installment_date, foreclosure_date, disposition_date,
--   foreclosure_costs, preservation_and_repair_costs, asset_recovery_costs,
--   miscellaneous_expenses, associated_taxes, net_sale_proceeds,
--   credit_enhancement_proceeds, repurchase_make_whole_proceeds,
--   other_foreclosure_proceeds, non_interest_bearing_upb,
--   principal_forgiveness_upb, repurchase_make_whole_proceeds_flag,
--   foreclosure_principal_write_off_amount, servicing_activity_indicator
-- )
-- SELECT
--   l.id,
--   t.reporting_period,
--   t.zero_balance_code,
--   t.zero_balance_date,
--   t.last_paid_installment_date,
--   t.foreclosure_date,
--   t.disposition_date,
--   t.foreclosure_costs,
--   t.preservation_and_repair_costs,
--   t.asset_recovery_costs,
--   t.miscellaneous_expenses,
--   t.associated_taxes,
--   t.net_sale_proceeds,
--   t.credit_enhancement_proceeds,
--   t.repurchase_make_whole_proceeds,
--   t.other_foreclosure_proceeds,
--   t.non_interest_bearing_upb,
--   t.principal_forgiveness_upb,
--   t.repurchase_make_whole_proceeds_flag,
--   t.foreclosure_principal_write_off_amount,
--   t.servicing_activity_indicator
-- FROM tmp_months_with_zero_balance_code t
--   INNER JOIN loans l
--     ON t.loan_sequence_number = l.loan_sequence_number
--     AND l.agency_id = 0;

-- DROP INDEX tmp_idx_monthly;
-- DROP TABLE tmp_msas;
-- DROP TABLE tmp_original_servicers;
-- DROP TABLE tmp_months_with_zero_balance_code;
-- DROP TABLE tmp_months_with_dq_status;
-- TRUNCATE TABLE loans_raw_fannie;
-- TRUNCATE TABLE monthly_observations_raw_fannie;
