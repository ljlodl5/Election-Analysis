# Python Challenge: Election-Analysis

## **Overview of Election Audit**
Utilizing a sample dataset of congressional election results from three Colorado counties (i.e Arapahoe, Denver, Jefferson) the goal of this assignment is to fulfill an audit on behalf of the election commission. Expections of the audit include: Providing the number of total ballots cast, statistics surrounding the winning congressional candidate, and details regarding voter representation among the counties represented in this dataset. 



## **Election-Audit Results**

### **Voter Turnout**

   * **Congressional Election: Total Votes** =369,711*

### **County Results**
   * **Number of votes and the percentage of total votes for each county in the precinct:** *
1.Jefferson: 10.5% (38,855)
2.Denver: 82.8% (306,055)
3.Arapahoe: 6.7% (24,801)

   * **County with the largest number of votes:** Denver *

### **Candidate Results**
   * **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.** *
1.Charles Casper Stockham: 23.0% (85,213)
2.Diana DeGette: 73.8% (272,892)
3.Raymon Anthony Doane: 3.1% (11,606)

   * **Election Winner:** Diana DeGette *
   * **Winning Candidate total votes:**  272,892 *
   * **Winning Candidate total percentage:** 73.8% *

### ![Election-Analysis Image](https://github.com/ljlodl5/Election-Analysis/blob/main/Analysis/Election%20Analysis-terminal%20.png)


## **Election-Audit Summary**
### **Business Proposal** 
The script created for the election commission audit is reusable, scalable and agnostic. In other words, the same script can be run irrespective of the ballot ids, candidates, and counties represented within the current import data structure. 
The script can accomodate automatic consumption and output with modifications (see #1 below). In addition, should an election commission want to expand the output to see additional data points (ex. ballot type, political affiliation etc.) or compare Colorado with national level details---the core lists, dictionaries, and read/write structures can remain with modifications to the script to include the new input/output elements. 
It is important to note that with modifications the script can also accomodate additional risk checks to ensure ballots are not counted more than once. (see #2 below)


### **Modifications: Increased scalability and automation**
1) The following output read/write strings to include version control in order to prevent read/write overlap and enable input/output automation.
*file_to_load = os.path.join("Resources", "election_results.csv")*
*file_to_save = os.path.join("analysis", "election_analysis.txt")*

2) This dataset assumes each row is representative of 1 vote. There should be statements validating the ballot ids are unique and not 'repeat-counted'. Statements prior to this segment should be considered that ensures uniqueness of the ballot ids. 
    for row in reader:
        total_votes = total_votes + 1

3) The core structure of the script can remain in place for congressional elections within the state, but also be expanded to include national* input/outputs as well. *It is important to note that performance will need to be evaluated and refactoring opportunities considered for national consumption( ~350M ballots) 

#### ![Election Summary: Script Modification Suggestions](https://github.com/ljlodl5/Election-Analysis/blob/main/Resources/Election-Analysis%20Script.png)

1.[Link to Resource Folder](https://github.com/ljlodl5/Election-Analysis/tree/main/Resources)
2.[Link to Analysis Folder](https://github.com/ljlodl5/Election-Analysis/tree/main/Analysis)