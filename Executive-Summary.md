
## Executive Summary

-----

### Data Collection

Like any scraping or API centered project, I started by exploring the webpage and website structure of https://www.totalwine.com/ . Given that pages for each spirit and spirit list pages are relatively similar, I tried to make sure my scraping functions were universal and could be applied to other item groups on their website such as tequila or wine.
Since [Total Wine's](https://www.totalwine.com/) website is also a retail website, they require that users declare that they are over 21 in order to proceed via a pop-up when first visiting the page.  This aspect required me to switch from my normal `requests`/`bs4` combination for acquiring and parsing and add `Selenium` in order to interact with the webpage.  This proved to be useful in the long run as I needed to click 'load more' buttons in order to get all of the user review data.
- Their website also had two different pop-up options that could appear to check for age.  One was red which I deemed "red" and one was blue which I deemed "blue", so my function had to accommodate both of these options since they were coded differently.
Once all this was figured out and the appropriate functions were constructed, the scraper worked by landing on the scotch homepage, then used some of the options available in the https structure to filter the content returned. I could add details to the https request in order to better request and get the information I wanted.  I used the following link in order to create the webpages in order to get all the scotch items listed.
 `"https://www.totalwine.com/spirits/scotch/c/000885?tab=fullcatalog&text=&spiritsvolume=standard-size-750-ml&pagesize=180&sort=name-asc&page=2"`

 I was able to filter the returned webpage content to do the following.

- Full catalog of options (as opposed to those available)
- Only bottle sizes of 750ml (standard)
- Have 180 items returned per page
- Sorted by name A to Z
- Iterate through pages (I believe there were 8 in total).

As number of observations gathered and associated amount of information about their item was small, I could store information in RAM, via a `pandas` dataframe, until all was collected.  In hindsight, I wouldn't recommend this 'all or nothing tactic' as this scrape ended up taking about six hours.

**Ethical Considerations**
- As always when scraping data, it is important to consider ethical dilemmas.  The data data available on most websites is available for personal, private use to the individual accessing it.  With that in mind I believe it to be unethical (and in many situations illegal) to utilize the data for anything but personal. Non-personal use of the data would include using the data would include things like..
- Using the data for an application.
- Building a public system that uses their data.
- Selling their data or building anything with their data and charging a fee.  

- In addition to ethical use of the data acquired, one must also consider the impact on the resources hosting the website.  If you do not already, you should have pauses in your scraper so that it is not making requests to the server as fast as it can.  This will 1. probably get you blocked as they'll immediately determine that a bot is requesting access to the website and 2. overload their resources potentially creating a DDoS because of request overload.

### Exploratory Data Analysis

I started off by count vectorizing the taste notes data to better understand which words appear the most, the least and what terms have the strongest positive and negative correlations.  Given that the taste notes listed on the website were often 3 to 5 adjectives in a list, the amount of data cleaning and text preprocessing prior to vectorization was very small(No stopword removal, stemmings or lemming needed).
After viewing with notes appeared the most (Rich, Balanced, Long, Spice & Vanilla), I decided to look for correlation amongst notes to better understand which appear often together and which don't seem to appear at all together.

**Common Combinations**
- "Cereal" & "Grain"
- "Floral" & "Fruit"
- "Blueberry" & "Yeast"
- "Raspberry" & "Hazelnut"
- "Seaweed" & "Brine"
- "Mustard" & "Seed"

**Rare Combinations**
- "Long", "Balanced" & "complex"
- "Rich" & "Delicate", "Intense", "Light" or "Medium"


"Mustard" & "Seed" were perfectly correlated because the actual note is "Mustard Seed"; getting both as individual notes was a result of using an ngram size of 1. As a result I decided to remove the "seed" vector as a possible feature.

**Price vs. Score**
As some scotches can be quite expensive, we really start to see the effect of these as outliers when looking at the price.  In my data collection, I acquired data for 131 scotches priced over $1,500 and 64 priced above $5,000.  Given this range and consistency of outliers, I looked at three separate ways of definitively labelling observations as outliers. Two utilized Tukey's method and one used my personal preference.
- 1. Q3($299.99) + 1.5 * IQR = \$488.36
- 2. Q3($299.99) + 3   * IQR = \$746.74
- 3. Personal Limit          = \$250   
    _This is probably the most I'd ever spend and I'd be extremely hesitant going anywhere near it_         

As the majority of scotches fall in the \$50 to \$100 dollar range, I think using the 1.5 times IQR for outlier detection would have been fine as this was able to capture all scotches with prices less than $500, which in my opinion is ok, because if you want an overly expensive scotch you probably have money to burn or already have an idea of what you want and don't need a recommendation.

Now that I've talked about price, I imagine the next thing you want to know about is "does price influence ratings?".  To be honest, not really.  The average user ratings for scotch showed a rather strange trend in that the majority of them were 4.9 stars or higher (35.9%). In addition, getting below a 3 star rating was very rare (4.9%).  Based on that information I concluded that those users reviewing scotch, generally enjoy their scotch.  The other insight that lead me to the conclusion that price doesn't really influence how score was shown by my scatter plot comparing the two.  In the scatter plot one can see that those few observations that score particularly bad, 1 star ranged from $50 to $300 a bottle.  On the other side of the plot, we can see that bottles that received 5 stars ranged from $30 to $350 a bottle.   

**Country and State**
Just because Scotch is called "Scotch" doesn't mean it needs to be "Scottish", a handful of other countries have scotches available to purchase such as Japan and India. Naturally, the idea would be to look and see if the country of origin has any relation to average user score, overall score or even the flavors that are most common _and_ if this is a viable feature to include in the recommender system.
Before actually looking into that information I decided against using country in the recommender as it would potentially remove the adventure of being recommended a scotch from Taiwan or France.
Pricing and scoring by country seems to be relatively similar to pricing and scoring as a whole so nothing interesting there.  Probably the most interesting finding was that the three Asian countries who were the leading producers (after Scotland) all had fruit appear in their top words leading me to believe that those consumers of whiskey in asian countries tend to enjoy scotches with more fruity tones.

_The rest of the countries had 6 or fewer observations with lesson of those being complete making them not worth the time to look at more in depth._

Within Scotland there are five regions that scotches hail from.  These regions have flavor profiles that are typically associated with the scotches that come from them.  This is mainly due to the process and ingredients typically used in the region, such as Islay & Islands being known for stronger peat and smoke flavors. (_Looking back, I should have looked at most prominent flavors based on state_)
Knowing this breakdown of regions, I wanted to get a better understanding as to if a scotches region or origin influences its price or average user rating.
From looking at the violin plots of price based on state, Highland, Islay & Islands and Speyside had very similar price distributions.  Lowland looks like it has less of the more expensive scotches so its upper boundaries are shorter.  Campbelltown had the smallest quartile range, mostly due to the fact that has the fewest observations out of all the regions.
Average rating distributions for every region except Campbelltown were similar as well with Speyside and Lowlands having a few of the really bad reviews.  Interestingly, Campbelltown had the highest median average rating and the smallest quartile range.  While one can conclude that users tend to be much more satisfied with products from Campbelltown, the lack of observations could also be contributing to this insight (our sample isn't relative to the population).

**Single Malt vs. Blended**
 If you're a data scientist or analyst or are familiar with machine learning, but not scotches, let me break this down for you as to the differences between Single Malt and Blended Scotch Whiskies.  

 Single Malt is like a single, very accurate model.  Given its test set it performs very well, but introduce some outside information and it tends to exhibit some overfitting and error due to variance . Each single malt focuses on achieving a specific flavor profile which most users enjoy, but some are not so fond of.

 Blended is like an ensemble method in which several lesser quality single malts(models) are mixed together with the intent of balancing out the flaws/impurities and come together to make a more diverse flavor profile that generally generalizes better to the population as a whole. More drinkers can agree upon blended as they can find a flavor or note in a blended that they enjoy.

 _This would actually make a cool blog post._

 Now that we have a bit more insight on single malt and blended varieties, I wanted to see if there was a difference in how they are perceived.  Like I mentioned earlier, I estimated that single malts would be "more accurate but prone to overfitting" meaning that on average they would receive higher average rating, but also have a chance to receive very low ratings. Blended varieties would receive more consistent user ratings, but the median and mode would not be as high as single malt.

 Single malts tended to be more expensive that blended, which makes sense.  They also tend to be rate higher by the fact that there fourth/upper quartile can't be seen (overlapped my the third).  The median rating is also a bit higher as well.  In addition to be rated at the top more often, they have more cases of being rated towards the bottom as their first quartile tail extends much further down.  These observations align with my assumptions that I listed prior.

**Cosign Similarity Recommendation**
Given the EDA on taste notes, scotch variety and region, I decided to only user the taste notes in order to note exclude the possibilities of having something more "out there" or unique recommended.  Since this recommender is for personal use, exploration into new things is important to me and I don't want to have options brushed away because of their region of origin or that they are blended. The last feature I wanted to look at was price.  Price is actually important to me, so I would like it factored into the model, the question is "how should it be represented?".
 As we observed, its not exactly normally distributed, however, I was able to make something a bit more normal by taking the log value.  I looked at five separate ways of representing price ; 'Price', 'Price Logged', 'Price Scaled', 'Price Scaled then Logged' and 'Price Logged then Scaled'.  After reviewing results, I believed that Price Logged Scaled would make price too much of an important feature and lower priced scotches would be penalized in their ability to be recommended. Price Scaled Logged would remove too much of the importance of price and not make it as useful as a feature as I would have liked.  In the end I settled on using the scaled price variable and adding a model argument that manually weighted the emphasis on price based on what value was passed to it.

**Recommendation**
In the end my similarity model used the taste notes, after being count vectorized and the Price Scaled feature and a weight that was provided with the input to indicate how important price was to the user. I choose Count Vectorization over Hashing or TFIDF as there are not duplicate words per observation and comparing on is there or isn't there was really the only reasonable option.

 The model also worked on averaging inputs so users could provide up to three scotches they enjoy and get a compromise recommendation of such.  
 I tested mostly on scotches that I enjoy (tending to be peaty and smokey) and scotches my coworker Nick enjoyed (Fruity and Spicy).  These tests were conducted on the multi-input and single method. According to my multi input of 'Laphroaig 10 Yr','Laphroaig Quarter Cask' and 'Lagavulin 16 Yr' I should definitely check out 'Talisker 18 yr'($149.99), 'Dalwhinnie Distillers Edition'($76.99), 'Glenfiddich 12 Yr'($26.99), 'Shieldaig Islay Single Malt'($16.99) as these seemed to be consistent regardless of price weight.  I also had a recommendation of 'Amrut Peated Single Malt'($59.99) which peaked my interest as its from India.

 **Conclusion**
 All-in-All I am pleased with the results that are recommended.  I have a lot of recommendations that I can sift through and try.  I probably only buy a bottle of scotch once every one to two months so I have a list of recommendations to last me a year or so.  
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


Hope you enjoyed this!
