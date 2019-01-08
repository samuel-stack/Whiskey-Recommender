# If its going to cost you, you better enjoy it!

### Project Overview

Scotch isn't exactly the cheapest of spirits one can buy, in fact its probably, on average the most expensive with the majority of bottles being priced around $60-$80 and the upper end being in the thousands or even tens of thousands of dollars.  That being said, most consumers of it want to known that if they are going to spend the equivalent of a weeks worth of groceries on a bottle that they are going to enjoy it.  

**Problem**
- Is it possible to use professional tasting notes to compare different scotches are recommend similar ones?

**Goal**
- Create a recommender systems that allows users to input a scotch or scotches they enjoy have the output be a list of scotches they should consider trying.

**Conclusion**

All-in-all I am pleased with the results that are recommended.  I have a lot of recommendations that I can sift through and try.  I probably only buy a bottle of scotch once every one to two months so I have a list of recommendations to last me a year or so.  
Unfortunately, since I've finished these set of recommendations I have only tried one of my recommendations, the 'Shieldaig Islay Single Malt'($16.99), which in my opinion was excellent for its price.  It had a bit of that alcohol sting towards the end of taste, but still very good for its price point.


Heres the list of Scotches I'm going to try to check out in the future. (two to three years worth)

- Amrut Peated Single Malt (Laph. 10, Laph. QC, Lag. 16)
- Ardbeg Uigeadail (Lagavulin 16 Yr)
- Berrys' Ardmore 8yr (Laph. 10, Laph. QC, Lag. 16)
- Bowmore 12 Yr (Laphroaig 10 Yr.)
- Dalwhinnie Distillers Edition (Laph. 10, Laph. QC, Lag. 16)
- Deanston 12 Yr (Laphroaig Quarter Cask)
- Glenfiddich 12 Yr (Laph. 10, Laph. QC, Lag. 16)
- Glen Ness 12 Yr  (Laphroaig Quarter Cask)
- Isle of Jura 16 Yr (Laphroaig 10 Yr.)
- Jura 10 Yr (Laphroaig Quarter Cask)
- Ledaig 10 Yr (Laphroaig 10 Yr.)
- Nikka Coffey Malt Whisky (Lagavulin 16 Yr)
- Talisker 18 Yr (Laph. 10, Laph. QC, Lag. 16)
- Tomatin Single Malt 12 Yr


Hope you enjoy this!
----

### Repository Structure

**Notebooks/Project Workflow**
[Website Investigation](1-Scotch-Scrape.ipynb)
- Investigation of https://www.totalwine.com/ to understand how to properly gather information.

[Scraper Finalization and Execution](2-Scraper-Notebook.ipynb)
- Finalization of scraping functions and running of the process

[Scotch Exploratory Data Analysis](3-Scotch-EDA.ipynb)
- Exploratory Data Analysis to better understand Scotch(personal) and what features to use in the recommendation model.

[Model Data Engineering](4-Simple-Recommender-DataEngineering.ipynb)
- Engineering and preprocessing the data desired to be used in the recommendation model.

[Model Building and Evaluation](5-Simple-Recommender-Model.ipynb)
- Creating the recommender model then running and evaluating several recommendation trials.

[Next Steps](6-NextSteps.ipynb)
- Steps that could be taken to better improve the current model or add more value.

**Other Files**  
[Executive Summary](./Executive-Summary.md)
- Summary of project process, workflow and analysis.  

[Data Folder](./Data)
- Data used for project.  

[Images Folder](./Images)
- Images used in project notebooks.

[Chrome Driver](./driver)
- Chrome Driver used for Selenium.  

[Scotch Presentation](./Scotch-Presentation.pdf)
- Accompanying Presentation for Project (instructional Purposes)  

[Scraper Functions](./scrape_lib.py)
- Functions developed in notebook 1 and used in notebook 2  
