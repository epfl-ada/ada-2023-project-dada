# Feedback: 

* Textual quality: Needs major improvements 
* Code quality: Needs improvements 
* Proposal quality: Needs major improvements

Your project mentor throughout the semester is Beatriz Borges: beatriz.borges@epfl.ch . For all project-related discussions, including your P3 deliverables, you are encouraged to be in touch with your mentor. 

## General remarks 
* Your submission was underdeveloped. 
* The README contained unfinished TODOs for Data Sampling, and your notebook had **poor readibility**, as you used few textual comments to contextualize your analysis. 

```
TODO : Add more textual comments
Comment : The TODOs left are for milestone 3
```

### Abstract 
Abstract is **clear**, it presents and **motivates the idea well**. 

### Research questions 
* *Most research questions* are **clear**. 
* The last one, *"Is the rating influenced by the number of reviews?"* is **not clear** to me. 
Are you measuring if more popular beers (as in, beers with more reviews) have higher scores? 

### Data exploration 
Considering the size of the data, **uncompressing** the data directly from .tar to .csv is **nonoptimal**. You should directly **work with the compressed file** or use an optimized file storage like **Parquet or pyarrow**. 

```
TODO : Look at efficient way to handle the large dataset

Comment (Anthony) : I did not know it was possible to work with compressed files directly
```

You start the exploration by stating **you do not understand a number of columns** in the data. By either looking at the relevant papers for this dataset (Comment : *We've done that*) or by asking me (your TA mentor), you should have first sought to understand the data rather than just discard columns because you don't. 

```
Comment (Anthony) : Papers had been read, but the column were still not clear.

TODO : Ask TA mentor
```

I am not sure the exploration was finished, as you not only presented a very brief, uncommented exploration which consisted of a few plots, and cell 29 is a TODO. How many missing values were they? Did you drop them? Fill them in? Etc. 

```
TODO : Complete data exploration (explain nan data handling)
```

### Methods 
The **methods themselves look good**, but as I explain below, your analysis is very limited by its **poor readability**. 

### Initial analysis 
While I can see you investigated a wide range of dimensions for your analysis, it was difficult to read throught it. 

In the future, you should use much more textual commentary to **explain** **what** you are doing, **why** you are doing, and what the **main findings** are **for each analysis** you do. Your proposal is also vague and shallow. Except for Linear Regression, everything else is not defined. You provide examples of tools you might use and vague statements like "Perform further, more in depth, analysis following the results of the exploratory analysis." What analysis? using what techniques? What is your plan overall, other than generally conducting an analyis? 

```
TODO : 

For each analysis write comment with
    - What we are doing 
    - Why ?
    - Main findings

--> More details for each analysis

```

### Questions for TAs 
Indeed **you will not be able to establish a causal relationship** from this data. You will be able to find correlations and possibly establish a hypothesis for causation which would then require a separate experiment to verify. *Still, having two beers be equal in all aspects except one (to be able to objectively measure its impact) is another challenging task. Maybe you'll be able to find such pairs of beers in the data you have thought, if you want to propose a future causal study*! I think you won't have the time to try to prevent unobserved covariates (unless you mean actions like using z-score which normalizes the ratings across platforms and time), so I suggest you **just acknowledge the limitations of your analysis** and possibly suggest *how you could build upon it to identify if there are any such confounders*. 