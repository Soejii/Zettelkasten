
## How to do Normality
- Analyze
- Regression
- Add Variables
- Save => Standarized Residual
- Plots => ZPRED - ZRESID
- Descriptive Stat
- Explore
- Add Residual
- Stat => Outliers
- Plots => Normality plots with test

![[Pasted image 20241210194928.png]]

## Linearity Test
- Analyze
- Compare Means
- Means
- Add Variable
- Options => Test For Linearity

- Graphs
- Legacy Dialog
- Scatter / Dot
-  Simple Scatter

![[Pasted image 20241210195406.png]]

## Heteroskedastisitas Test
- Transform
- Compute Variable
- On target variable type in AbsRes_1 / AbsZRE_1
- On Numeric Expression type ABS(RES_1) / ABS(ZRE_1)
- Back to Linear Regression
- Dependent Variable use Absolute Residual
- Uncheck all of shit on Save

![[Pasted image 20241210195819.png]]


## Regresi Berganda
- Analyze
- Regression
- Add Variables
- Stat => Confidence Interval, Descriptives, Part and Partial Correlations

![[Pasted image 20241210200930.png]]

![[Pasted image 20241210200947.png]]

## Multikolinearity Test
- Analyze 
- Regression
- Linear
- Add Variables
- Stat => Check the box for Collinearity Diagnostics

![[Pasted image 20241210201121.png]]

![[Pasted image 20241210201152.png]]

## Correlate
- Analyze
- Correlate
- Bivariate
- Put in all variables
- Options => means and standard
- Check Pearson

![[Pasted image 20241210201433.png]]

![[Pasted image 20241210201450.png]]

## Homogenity Test
- Analyze
- Compare Means
- One-Way Anova
- Add Variables
- Options => Homogenity of variance test

![[Pasted image 20241210201902.png]]

## Uji Beda Dua Sampel (Independent)
- First of all we need to take our variables, in this case are Scores, and Offering
- Change the offering value to desired value in int
- Compare Means
- Independent Sample T test
- Define Groups as 1 and 2

![[Pasted image 20241210202033.png]]

## Uji Beda Dua Sampel (Paired)
- Analyze 
- Compare Means
- Paired Sample T-Test
- before to variable 1, and after to 2

![[Pasted image 20241210202149.png]]

## Uji Beda Dua Sample Non Parametric

### Independent Sample
- Analyze
- Non parametric test
- Legacy
- 2 Independent Sample
- add variables
- Define the groups
- Test Type Mann-Whitney U

![[Pasted image 20241210202527.png]]

### Paired Sample
- Analyze
- Non Parametric Test
- 2 Related Samples
- Before to 1 after to 2
- Test type Wilcoxon

![[Pasted image 20241210202627.png]]

### Correlation:

- Linearity
- Normality of Variables
- Homoscedasticity

### Regression (Linear Regression):

- Linearity
- Independence of Errors
- Homoscedasticity
- Normality of Errors
- No Multicollinearity

### Regresi Berganda (Multiple Regression):

- Linearity
- Independence of Errors
- Homoscedasticity
- Normality of Errors
- No Multicollinearity
- No Endogeneity

### Uji Beda Paired (Paired Sample t-Test):

- Normality of Differences
- Independence of Observations

### Uji Beda Independent (Independent Sample t-Test):

- Normality of Each Group
- Homogeneity of Variance (Levene’s Test)
- Independence of Observations