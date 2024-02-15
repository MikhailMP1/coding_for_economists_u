* Import data
**# Bookmark #1
use "data\derived\tender_data_analysis.dta", clear 

* Keep only tenders with a single winning countries 
**# Bookmark #2
keep if strlen(win_country_code) == 2 

**# Bookmark #3
gen same_country = win_country_code == iso_country_code

* tabulate frequency
tabulate same_country // Strong home bias 

* Does the value of the tender differ if home firm wins?
* In levels
regress award_value_euro same_country

* In logs 
reg ln_award_value_euro same_country, coeflegend

merge m:1 iso_country_code using "data\derived\country_codes.dta", keepusing(untermenglishformal)