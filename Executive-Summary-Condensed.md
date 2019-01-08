## Executive Summary (Condensed)

-----

### Data Collection
- Scraped https://www.totalwine.com/spirits/scotch to aquire data.
- Website used popups and load more buttons which required the implementation of `Selenium` in addition to the  `requests` and `bs4` libraries.
- Since size of data was expected to me small, scraper was run locally and gathered data was deposited locally.

**Ethical Considerations**
- This data is to be used by the individual for the individual and not exploited to create any publicly facing application or revenue without the explicit permission from the owners of the data.
- Put pauses in your scraper so you don't have your IP blocked or overload the websites server.

### Exploratory Data Analysis
- Data was relatively clean so no need for stopword or special character removal, stemming or lemmatization.
- Taste note data was count vectorized to find most common flavor notes. (rich, balanced, long, spice, vanilla, oak.)
- Correlation of notes was looked at to find common and rare combinations  of flavors.
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

**Price vs. Score**
- As some scotches were very expensive (131 samples over $1,500), an outlier threshold was set at $500.
- Average user price was exceptionally high with 35.9% of observations being greater than a 4.9 rating.
- Very rare to see a user rating below 3 as well with only 4.9% of observations having an average rating below 3.
- Price did not really affect score as bottles that had average reviews of 1 ranged from $50 to $300 in price which those with 5 star averages ranged from $30 to $350 in price.
  - This is likely a result of subjectivity of reviewer where price is considered when accessing flavor and also having average reviews that are based off of limited number of reviews (i.e. One bad review or one raving review.)

**Country and State**
- Outside of Scotland, Japan, India and Taiwan are the leading producers of scotch.  These asian style scotches seemed to have a commonality of having a fruity tone present most of the time.
- Reviews and pricing was relatively similar across regions in Scotland.  Campbelltown's distribution often stuck out visually, having both a distribution of price that was slightly higher than other regions and a tighter distribution of average ratings around the top of the spectrum.  Campbelltown also had the fewest number of observations, so one can rationalize that these differences in distribution could be the result of not having comparative sample sizes.  
  - One could further investigate this insight via creating and comparing equal samples and/or doing t-tests.

**Single Malt vs. Blended**
- Single malts, while having higher average scores than blended, also had a wide distribution of average scores as they were more likely to have the occasional very negative review.
- Blended average scores were not as high as single malts, but they were more consistent and had a tighter distribution.
- Single Malts tended to be more expensive than blended.

**Cosign Similarity Recommendation**
- Price Scaled and count vectorization of taste notes were included in the cosign similarity recommendation model.
- All other features were excluded by nature of personal justification.
  - This is intended to be a recommender for myself and I was to not have potential recommendations excluded because country, region or variety creates unnecessary distance.
- The Price feature had an added optional weight in the model allowing the user (me) to manually change how much price was considered in the model.
- The model also used an averaging or compromise system that could take up to three inputs in order to find a list of outputs.

**Recommendation**
- Prior to this project my personal favorite scotches were 'Laphroaig 10 Yr','Laphroaig Quarter Cask' and 'Lagavulin 16 Yr' as I am very fond of the strong peat and smoke flavors.
- Given these three inputs, my recommendations were as follows.
  - 'Talisker 18 yr'($149.99)
  - 'Dalwhinnie Distillers Edition'($76.99)
  - 'Glenfiddich 12 Yr'($26.99)
  - 'Shieldaig Islay Single Malt'($16.99)
These were common across several of the pricing weights.

**Conclusion**
- I am happy with the initial results and have quite a bit of recommendations to check out in the coming years.
