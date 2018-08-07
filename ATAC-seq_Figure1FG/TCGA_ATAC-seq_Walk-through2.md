# TCGA ATAC-seq Walk-through

In Figure 1, Corces, 2018 show that they can identify known sites of chromatin accessibility, including a peak that shows increased accessibility in kidney renal clear cell carcinoma (rs35252396) and another associated with colon cancer susceptibility (rs6983267). Here we recreate a variation of this figure as well as further explore the relationship between the accessibility of these SNPs and cancer type.

## Live View of Figure 1F
<a href="http://xenabrowser.net/?bookmark=0014b6d379b0a69e5fd9a7c2930cf408"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/ATAC-seq_Figure1FG/Figure1F.png" width="700"></a>

Here we can see heterogenous accessibility of rs6983267 (column C) and rs35252396 (column D) by cancer type (column B). Red indicates higher chromatin accessibility and blue indicates lower. Examining peaks on either side of the rs6983267 locus (column E) reveals that this trend is specific to this locus. This SNP is associated with MYC in colorectal cancer (column F). Bookmark: <http://xenabrowser.net/?bookmark=0014b6d379b0a69e5fd9a7c2930cf408>


### Steps to reproduce

1. __Start here: <http://xenabrowser.net/?bookmark=3d71a8d22ac8b65207399f927ef50ea9>.__

	> Note that the GDC Pan-Cancer (PANCAN) cohort is already selected and we have filtered down to just those samples that have ATAC-seq data.

2. __Add cancer type to view.__ Click on 'Add Column', select 'Phenotypic', and select 'disease code'. Click 'done'.

3. __Add ATAC-seq peak for ESCA\_60954, which is the peak for rs6983267, and STAD\_57221, which is the peak for rs35252396.__ Click on 'Add Column' and enter 'ESCA\_60954' as the 'Gene or Position'. Click 'show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'. Repeat for STAD\_57221.

	> Note that you need to enter 'ESCA_60954'. If you can always edit the label to read 'rs6983267' by clicking on it and typing.

	> Bookmark: <http://xenabrowser.net/heatmap/?bookmark=2ab87ec9bde550dfac9f547cd3090e9a>

4. __Examine peaks in the region surrounding rs6983267.__ Click on 'Add Column' and enter 'chr8:127369679-127432497' as the 'Gene or Position'. Click 'Show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.

	> We could see from Step 3 that rs6983267 had cancer-dependent accessibility. In this step we are examining if these trends are just for this peak or if they affect a wider region. We see here that while some peaks nearby have a similar trend, this is isolated to this peak.

5. __Examine peaks around MYC.__ Click on 'Add Column' and enter 'chr8:127715668-127760786' as the 'Gene or Position'. Click 'show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.

	> rs6983267 is associated with MYC in colorectal cancer ([Pomerantz 2009](https://www.ncbi.nlm.nih.gov/pubmed/19561607)). Here we examine MYC accessibility.

	Bookmark: <http://xenabrowser.net/?bookmark=0014b6d379b0a69e5fd9a7c2930cf408>

## Explore further
<a href="http://xenabrowser.net/heatmap/?bookmark=9841aae3ca1ffca6156414e4b96dbb74"><img src="https://atacseq.xenahubs.net/download/meta/Figure1Fchart.png" width="700"></a>

Bookmark: <http://xenabrowser.net/heatmap/?bookmark=9841aae3ca1ffca6156414e4b96dbb74>
Another view of rs6983267 accessibility by cancer type.

### Steps to reproduce

<img src="https://atacseq.xenahubs.net/download/meta/atacseqchart.gif" width="90%">

We see a box plot of rs6983267 peak signal across cancer type. This more clearly identifies cancer types with increased accessibility for this locus, including LUSC, BLCA and BRCA. This finding is corroborated by other studies in the literature, including [Wokolorczyk 2008](https://www.ncbi.nlm.nih.gov/pubmed/19047180).

## Live View of Figure 1G/H
<a href="http://xenabrowser.net/?bookmark=a73a14eeba05a51a0da64a672b912355"><img src="https://atacseq.xenahubs.net/download/meta/Figure1GH.png" width="700"></a>

Bookmark: <http://xenabrowser.net/?bookmark=a73a14eeba05a51a0da64a672b912355>
Zooming into just colorectal (COAD) and kidney renal clear cell cancer (KIRC), we can see that rs6983267 is very accessible for COAD whereas in KIRC it is relatively inaccessible. The reverse is true for rs35252396. Red indicates higher chromatin accessibility and blue indicates lower.

### Steps to reproduce
__Filter to COAD and KIRC.__ Enter 'COAD OR KIRC' in the filter search bar to highlight and find samples that are COAD or KIRC. Choose 'Filter' from the menu next to the search bar.

<img src="https://atacseq.xenahubs.net/download/meta/atacseqfilter.gif" width="90%">

More help on our filter feature can be found here: <https://ucsc-xena.gitbook.io/project/overview-of-features/filter-and-subgrouping>

> Note that 'OR' needs to be capitalized. 

## More Resources
* Check out other ATAC-seq vignettes: URL
* Check out our Xena online tutorials: <https://xena.ucsc.edu/getting-started/>
