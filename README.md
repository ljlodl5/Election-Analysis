# Python Challenge: Election-Analysis

## **Overview of Election Audit**
Utilizing a sample dataset of congressional election results from three Colorado counties (i.e Arapahoe, Denver, Jefferson) the goal of this assignment is to fulfill an audit on behalf of the election commission. Expections of the audit include, providing the number of total ballots cast, statistics surrounding the winning congressional candidate, and details regarding voter representation among the counties represented in this dataset. 



## **Election-Audit Results**

### **Voter Turnout**

   * **Total Votes casted in this congressional election:** 369,711 

### **County Results**
   * **Number of votes and the percentage of total votes for each county in the precinct:**
		Jefferson: 10.5% (38,855)
		Denver: 82.8% (306,055)
		Arapahoe: 6.7% (24,801)
   * **County with the largest number of votes:** Denver

### **Candidate Results**
   * **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**
		Charles Casper Stockham: 23.0% (85,213)
		Diana DeGette: 73.8% (272,892)
		Raymon Anthony Doane: 3.1% (11,606)

   * **Election Winner:** Diana DeGette
   * **Winning Candidate total votes:**  272,892
   * **Winning Candidate total percentage:** 73.8%

### **Support audit file**


## **Election-Audit Summary**
### **Business Proposal** 
The script created for the election commission audit is scalable and agnostic of the amount of ballots, candidates, and counties represented in the current data structure. Therefore the script can be reused to support other precints and those of increased size with no modifications. 
The script can also accomodate automatic consumption and output with small modifications (see #1 below)
Should an election commission want to expand the output to see additional data points (ex. ballot type, political affiliation) or to compare Colorado with national level details---the core lists, dictionaries, and read/write structures can remain with small modifications to the script to include the new input/output elements. 
It is important to note that with modifications the script can also accomodate additional risk checks to ensure ballots are not counted more than once. (see #2 below)


### **Modifications: Increased scalability and automation
1) The following output read/write strings to include version control in order to prevent read/write overlap and enable input/output automation.
#### ex. file_to_load = os.path.join("Resources", "election_results.csv")
#### ex. file_to_save = os.path.join("analysis", "election_analysis.txt") 

2) This dataset assumes each row is representative of 1 vote. There should be statements validating the ballot ids are unique and not 'repeat-counted'.
#### ex. statements prior to this segment should be considered that ensures uniqueness of the ballot ids. 
    for row in reader:
        total_votes = total_votes + 1
3) The core structure of the script can remain in place for congressional elections within the state, but also be expanded to include national* input/outputs as well. *It is important to note that performance will need to be evaluated and refactoring opportunities considered for national consumption( ~350M ballots) 

#### Script Modification Proposals (2) -see attached

