1. Team Members: Ritik Panda (rp3111), Jared Andrews()
2. apriori.py, create_dataset.py, README.md, example-run.txt, INTEGRATED-DATASET.csv, requirements.txt
3. How to run? 
    python3 main.py INTEGRATED-DATASET.csv min-supp min-conf 

    where,
        min-supp = Minimum Support
        min-conf = Minimum Confidence
4.
    NYC Open DATASET : DOHMH New York City Restaurant Inspection Results
    Description: The dataset contains every sustained or not yet adjudicated violation citation from every full or special program inspection conducted up to three years prior to the most recent inspection for restaurants and college cafeterias in an active status on the RECORD DATE (date of the data pull). When an inspection results in more than one violation, values for associated fields are repeated for each additional violation record. Establishments are uniquely identified by their CAMIS (record ID) number. Keep in mind that thousands of restaurants start business and go out of business every year; only restaurants in an active status are included in the dataset. 

    Integrated Dataset: We only keep the following relevant fields:
    "dba" : This field represents the name (doing business as) of the entity (restaurant);
    "boro" : Borough in which the entity (restaurant) is located.;• 1 = MANHATTAN • 2 = BRONX • 3 = BROOKLYN • 4 = QUEENS • 5 = STATEN ISLAND 
    "critical_flag": This field describes the entity (restaurant) cuisine. 
    "cuisine_description": Indicator of critical violation; "• Critical • Not Critical • Not Applicable"; Critical violations are those most likely to contribute to food-borne illnes
    "grade": Grade associated with the inspection; • N = Not Yet Graded• A = Grade A• B = Grade B• C = Grade C• Z = Grade Pending• P= Grade   Pending issued on re-opening following an initial inspection that resulted in a closure

    We extract around 50,000 rows from the original dataset using the Socrata api.
    We then analyze and clean the dataset,where we notice more than 50% of the grade fields are empty. We decide to drop these rows because we still end up with almost ~25,000 rows of data. 

    This cleaned datset is finally used as our INTEGRATED Dataset

5.
    This code implements the Apriori algorithm for frequent itemset mining and association rule generation. The input to the code is a CSV file containing a transactional dataset, minimum support, and minimum confidence thresholds. The algorithm works in the following steps:

        1. Convert the CSV file to a list of transactions where each transaction is represented as a set of items.
        2. Create a dictionary of items and their frequency in the dataset.
        3. Remove items that do not meet the minimum support threshold.
        4. Generate frequent itemsets of length 1.
        5. Generate frequent itemsets of length 2 and higher by joining frequent itemsets of length k-1.
        6. Generate association rules from frequent itemsets that satisfy the minimum confidence threshold.

    The output of the code is a file named 'output.txt' containing the frequent itemsets and association rules. The frequent itemsets are written in the format [itemset] , support%, and the association rules are written in the format antecedent ==> consequent (Conf: confidence%, Supp: support%).

6.
