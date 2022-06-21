**Pierre's GestPEA Project**

########################################################################################################
########################################################################################################
**Presentation**

This project is to handle my trading account (PEA) and see its evolution (do I win money or not ???)

The development environment is the following:
- A Debian Linux server (IP adress: 54.37.9.75) for the backend using:
    - A mySQL database (gestpea)
    - Python scripts to handle API and communication with the database using:
        - Flask and Flask_restful
- A Flutter App to visualize the data anywhere
- An Excel worksheet (to input some data and visualize data)

A lot of free apps are available out there to do this but I havn't found any that enables me to
follow how much I make thanks to the dividends (and this is important for me since I dont try
crazy things, I'm going in for the long run and dividends are great for that)

########################################################################################################
########################################################################################################
**In detail**

The input is an Excel document (GestPEA.xlsm) containing the list of all the operations applied on my trading account:
- buy
- sell
- dividend
- stocks buyback thanks to dividends
- the money transfer as input in the trading account (useless as of now)
- and the bank balance of the account (available each month) (useless as of now)

