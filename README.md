## Table of Contents
  - [Introduction](#introduction)
  - [How to use app](#how-to-use-app)

## Introduction:

A fixed deposit (FD) is a financial instrument provided by banks or non-bank financial institutions which provides investors a higher rate of interest than a regular savings account, until the given maturity date. It may or may not require the creation of a separate account.


[![PNG - 7  How to Use Custom Feature of Managing Fixed-Deposit in ERPNext](https://user-images.githubusercontent.com/18363620/237381063-2eba167f-57f6-4ffb-96fd-e8f2e637d454.png)](https://youtu.be/hZTaBWUbmf0)


## How to use App:

1.	To add a fixed deposit, go to the Fixed Deposit list and click on "Add Fixed Deposit."<br/>
2.	Enter the details such as FD Number, Posting Date, Bank Account, FD Account, Interest Account, FD Start Date, FD Amount, Maturity Date, and Maturity Amount.<br/>
3.	Click on "Save and Submit." <br/>
4.	After submission, the system will create a journal entry with the Bank Account credited and the Fixed Deposit account debited.<br/>


![New FD - 16-to-26](https://github.com/finbyz/FD-Management/assets/18363620/2d5d4c90-d11b-47b1-93e3-522e7702da40)


**`When the Fixed Deposit matures`**:
 
1.  Go to the Fixed Deposit list, select the Fixed Deposit, and check the "Matured" checkbox.<br/>
2.  Enter the Matured Amount and click on "Update."<br/>
3.  After updating the system will create a journal entry with the Bank Account debited, Fixed Deposit Account credited, and Interest Account credited.<br/>


![Matured - 45-to-52](https://github.com/finbyz/FD-Management/assets/18363620/016c9dd2-1edc-4320-a8c1-2e3e07d99458)


**`When The Fixed Deposit Renewed`**:

1.  Go to the Fixed Deposit List, select the Fixed Deposit, and check the "Renewed" checkbox.<br/>
2.  Enter the Renewed Amount, Next Maturity Date, and Maturity Amount. Click on "Update."<br/>
3.  After updating the system will create a journal entry with the Fixed Deposit Account debited with the new Renewal Amount and credited with the Principal Amount. The difference between the two will be credited to the FD Interest Account and System will create new Fixed deposit with reference of previous FD.<br/>


![Renewed - 68-to-78](https://github.com/finbyz/FD-Management/assets/18363620/67bb92fc-babc-4ff0-9de1-43d7e224cb7e)


## Documentation

Complete documentation for FD Management [here](https://finbyz.tech/fd-management)

## License

GNU GPL V3. (See [license.txt](https://github.com/finbyz/FD-Management/blob/main/license.txt) for more information).

The FD Management code is licensed as GNU General Public License (v3) and the copyright is owned by FinByz Tech Pvt Ltd.
 
 

