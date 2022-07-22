
create view model_test as (
select *
from fannie_processed
where monthly_reporting_period >= '2021-03-01'
    and original_interest_rate >= 2.5
    and original_interest_rate < 3.5
    and 201000 < original_upb
    and 225000 > original_upb
    and loan_age < 180
    and oltv <= 95
    and oltv > 75
    and original_loan_term = 360.0
order by monthly_reporting_period desc
limit 500000
)