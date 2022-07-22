from leela.database.database import Database


#	
# select monthly_reporting_period, count(*)
# 	   from fannie_processed
# 	where monthly_reporting_period >= '2021-03-01'
# 	and  201000 < original_upb
# 	and  225000 > original_upb
# 	group by monthly_reporting_period;
# 		  # 201-225k
#         # 176-200k
#         # 151-175k
#         # 111-150k HLB
#         # 86-110k MLB
#         # 0-85k LLB
#
# -------------------------- #
# Results ->
# -------------------------- #
# "2021-03-01"	730472
# "2021-04-01"	743856
# "2021-05-01"	755706
# "2021-06-01"	768266
# "2021-07-01"	774299
# "2021-08-01"	786617
# "2021-09-01"	794201
# "2021-10-01"	800874
# "2021-11-01"	807762
# "2021-12-01"	816075

# Resources ->
# https://docs.fhnfinancial.com/?0d8a7e7e-2521-43f7-a527-b8786452b172

# original_interest_rate >= 2.5 and original_interest_rate <= 3.5
# and 201000 < original_upb and  225000 > original_upb
#  and loan_age < 75
#  and oltv < 90 and oltv > 75
#  and monthly_reporting_period > '2021-03-01'
#  --and loan_purpose = 'R'
#  and original_loan_term = 360.0
#  --group by loan_purpose;

def main():
    start_date = "2021-03-01"
    filter = "original_interest_rate >= 2.5 and original_interest_rate < 3.5"
    filter += " and 201000 < original_upb and  225000 > original_upb"
    filter += " and loan_age < 180"
    filter += " and oltv <= 95 and oltv > 75"
    filter += " and original_loan_term = 360.0"
    # filter += " and loan_purpose = 'R'"
    data = Database.get_model_input(start_date, my_filter=filter, DEBUG=True)
    print(data)
    print(len(data))

    # Type here ->
    data.to_csv(r"C:\Projects\GitHub\Leela\leela\research\Nikita\data\30_yr.csv")

# def main():
    # data = Database.query_db("select * from fannie_processed where loan_id = '000097568237'")
    # print(data)

if __name__ == "__main__":
    main()
    # main_dep()