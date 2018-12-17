# Categorical Data Analysis in Python
## Chapter 1 - Understand categorical data
  * Lesson 1.1 - Introduction to variables
    * A learning objective: Learn about variable types: categorical (nominal, ordinal), interval, ratio.
  * Lesson 1.2 - Summary Statistics
    * A learning objective: Frequencies, proportions, data types
  * Lesson 1.3 - Visual exploration
    * A learning objective: Visualize data via _bar chart_, _pairplot (seaborn)_.
## Chapter 2 - Taking a closer look
  * Lesson 2.1 - _Contigency tables_
    * A learning objective: create a _contigency table_ in pandas, collapse larger groups into smaller (['baby', 'toddler', 'child', 'adolescent', 'young adult', 'adult', 'senior'] -> ['young', 'old'])
  * Lesson 2.2 - Measures of Agreement
    * A learning objective: _Cohen's Kappa_; Use _statsmodels.stats.inter_rater.cohens_kappa_ or implement function
  * Lesson 2.3 - Correlation
    * A learning objective: Use _Point-Biserial Correlation Coefficient_ and _Phi Correlation Coefficient_ to understand relationships between one binary categorical and numerical variables and between multiple categorical binary variables respectively. Use _Pearson's rank-order coefficient_ and _Kendall's Tau_ for ordinal variables. Use _scipy.stats.pointbiserialr_, _scipy.stats.pearsonr_, _scipy.stats.kendalltau_. For Phi either create function or use _sklearn.metrics.matthews_corrcoef_.
## Chapter 3 - Hypothesis testing
  * Lesson 3.1 - _Chi-Square Distribution/ Pearson's Chi-Square Test_
    * A learning objective: Learn about the distribution, calculate critical values, perform 3 flavours of _Chi-Square tests_: test for independence, test for equality of properties, test of goodness of fit; use _scipy.stats.chisquare_ and _scipy.stats.chi2_contingency_
  * Lesson 3.2 - _Fisher's Exact Test_
    * A learning objective: use _scipy.stats.fisher_exact_
  * Lesson 3.3 - ANOVA
    * A learning objective: use _scipy.stats.f_oneway_ 
## Chapter 4 - Use case _Simpson's Paradox_
  * Lesson 4.1 - Problem description
    * A learning objective: Get data from CSV, take a quick look at the data, create categories
  * Lesson 4.2 - Understand and test data
    * A learning objective: Test for correlation and significance, combine several groups, create visualizations
  * Lesson 4.3 - Draw conclusion
    * A learning objective: Observe and understand _Simpson's paradox_: reversal of trend in combined group vs. looking at groups individually
