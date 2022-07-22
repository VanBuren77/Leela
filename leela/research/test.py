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
#  2017-01-01               |   186457
#  2017-02-01               |   334384
#  2017-03-01               |   487648
#  2017-04-01               |   635451
#  2017-05-01               |   795997
#  2017-06-01               |   976863
#  2017-07-01               |  1150498
#  2017-08-01               |  1336812
#  2017-09-01               |  1511580
#  2017-10-01               |  1677095
#  2017-11-01               |  1834551
#  2017-12-01               |  2008072
#  2018-01-01               |  2164959
#  2018-02-01               |  2307472
#  2018-03-01               |  2441021
#  2018-04-01               |  2565564
#  2018-05-01               |  2708519
#  2018-06-01               |  2861196
#  2018-07-01               |  3014909
#  2018-08-01               |  3180604
#  2018-09-01               |  3315246
#  2018-10-01               |  3456749
#  2018-11-01               |  3577825
#  2018-12-01               |  3689926
#  2019-01-01               |  3804014
#  2019-02-01               |  3891309
#  2019-03-01               |  3981960
#  2019-04-01               |  4073105
#  2019-05-01               |  4181366
#  2019-06-01               |  4285020
#  2019-07-01               |  4450928
#  2019-08-01               |  4614384
#  2019-09-01               |  4778027
#  2019-10-01               |  4925860
#  2019-11-01               |  5058288
#  2019-12-01               |  5206902
#  2020-01-01               |  5339128
#  2020-02-01               |  5469262
#  2020-03-01               |  5664029
#  2020-04-01               |  5947504
#  2020-05-01               |  6187433
#  2020-06-01               |  6461316
#  2020-07-01               |  6720866
#  2020-08-01               |  7058611
#  2020-09-01               |  7309302
#  2020-10-01               |  7611070
#  2020-11-01               |  7957534
#  2020-12-01               |  8214302
#  2021-01-01               |  8448017
#  2021-02-01               |  8668897
#  2021-03-01               |  9001393
#  2021-04-01               |  9253877
#  2021-05-01               |  9497563
#  2021-06-01               |  9729089
#  2021-07-01               |  9858289
#  2021-08-01               | 10080292
#  2021-09-01               | 10241844
#  2021-10-01               | 10399235
#  2021-11-01               | 10543596
#  2021-12-01               | 10726578

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
    data = Database.get_model_input(start_date, my_filter=filter, DEBUG=True, limit=500000)
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