# TCGA ATAC-seq Walk-through: Figure 1D & E

In Figure 1, Corces et. al. 2018 investigate the relationship between MYC, chromatin accessibility, and cancer type.  They observed substantial diversity in the chromatin accessibility landscape of the MYC locus to cluster cancer types into two primary categories: (i) cancer types with extensive chromatin accessibility at 5’ and 3’ DNA elements, such as colon adenocarcinoma (COAD), and (ii) cancer types with chromatin accessibility primarily at 3’ regulatory elements, such as kidney renal clear cell carcinoma (KIRC).

Further, they identify known sites of chromatin accessibility including peaks surrounding two functionally validated GWAS cancer susceptibility SNPs: rs6983267, which is associated with colon and prostate cancer susceptibility,  and rs35252396, which is associated with renal cancer. Both of these SNPs show accessibility in other cancer types, indicating that they may be important in other cancer types.

Here we recreate a variation of this figure as well as further explore the relationship between the accessibility of these SNPs and cancer type.

## Live View of Figure 1D
<a href="/?bookmark=5000d4a3b9a2e874545fcf0a77ac85bd"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure1DE/Figure1D.png" width="700"></a>

Here we can see heterogenous accessibility of rs6983267 (column C) and rs35252396 (column D) by cancer type (column B). Red indicates higher chromatin accessibility and blue indicates lower. Examining peaks on either side of the rs6983267 locus (column E) and rs35252396 locus (column F) reveals that these trends are specific to these loci. Both SNPs are associated with MYC in colorectal cancer and renal cancer respectively (column G). Bookmark: </?bookmark=5000d4a3b9a2e874545fcf0a77ac85bd>


### Steps to reproduce

1. __Start here: [3d71a8d22ac8b65207399f927ef50ea9](/?bookmark=3d71a8d22ac8b65207399f927ef50ea9).__

	> Note that the GDC Pan-Cancer (PANCAN) cohort is already selected and we have filtered down to just those samples that have ATAC-seq data.

2. __Add cancer type to view.__ Click 'Add Column' next to the samples column, select 'Phenotypic', and select 'disease_code.project'. Click 'done'.

3. __Add ATAC-seq peak ESCA\_60954, which is the peak for rs6983267__ Click 'Add Column' and enter 'ESCA\_60954' as the 'Gene or Position'. Click 'show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.

	> Note that you need to enter 'ESCA_60954'. After adding the column you can always edit the label to read 'rs6983267' by clicking on the label.
	
	> Note that the color threshold in the images are different (max:4 min:-2) than what is used by default. See [this help](https://ucsc-xena.gitbook.io/project/how-do-i/how-do-i-change-the-color-threshold-for-a-column) for more information.
	
	> We could see that rs6983267 is more accessible in COAD and PRAD, which is predicted from [Yeager 2007](https://www.nature.com/articles/ng2022), [Tomlinson 2008](https://www.ncbi.nlm.nih.gov/pubmed/18372905), and [Sur 2012](https://www.ncbi.nlm.nih.gov/pubmed/23118011). It is also accessible in breast and other squamous cancer types.

4. __Add ATAC-seq peak STAD\_57221, which is the peak for rs35252396.__  Repeat step 3 for STAD\_57221.

	> We can see that rs35252396 is more accessible in KIRC, which is predicted from [Grampp 2016](https://www.nature.com/articles/ncomms13183). 
	
	> Bookmark: [bookmark=65966798c18f3f361b751609a66d3a6d](/?bookmark=65966798c18f3f361b751609a66d3a6d)

5. __Examine peaks in the region surrounding rs6983267.__ Click 'Add Column' and enter 'chr8:127369679-127432497' as the 'Gene or Position'. Click 'Show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.

	> We could see from Step 3 that rs6983267 had cancer-dependent accessibility. In this step we are examining if these trends are just for this peak or if they affect a wider region. We see here that while some peaks nearby show changes in accessibility, this the observed cancer type-specificity of rs6983267 is isolated to this peak.

6. __Examine peaks in the region surrounding rs35252396.__ Repeat step 5 for 'chr8:127841010-127911511'

	> Similarly, for rs35252396  we see here that while some peaks nearby have a similar trend, this is isolated peaks that are active in renal cancer types.

7. __Examine peaks around MYC.__ Click on 'Add Column' and enter 'chr8:127715668-127760786' as the 'Gene or Position'. Click 'show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.

	> Both of these SNPs are linked to the gene MYC. Here we see that in addition to the distal peaks of rs6983267 and rs35252396, that MYC itself has cancer-dependent trends in chromatin accessibility. Some cancer types have extensive chromatin accessibility at 5’ and 3’ DNA elements, such as colon adenocarcinoma (COAD), and some cancer types have chromatin accessibility primarily at 3’ regulatory elements, such as kidney renal clear cell carcinoma (KIRC).

	> Bookmark: [5000d4a3b9a2e874545fcf0a77ac85bd](/?bookmark=5000d4a3b9a2e874545fcf0a77ac85bd)

## Explore further
<a href="/?bookmark=443b97e1754fde0d252134ac6f1d3480"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure1DE/Figure1Dchart.png" width="700"></a>

Bookmark: [443b97e1754fde0d252134ac6f1d3480](/?bookmark=443b97e1754fde0d252134ac6f1d3480)

Another view of rs6983267 accessibility by cancer type.

### Steps to reproduce

1. __Click the chart icon__

	> <img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure1DE/atacseqchart.gif" width="90%">

	> We see a box plot of rs6983267 peak signal across cancer type. This more clearly identifies cancer types with increased accessibility for this locus, including LUSC, BLCA and BRCA. This finding is corroborated by other studies in the literature, including [Wokolorczyk 2008](https://www.ncbi.nlm.nih.gov/pubmed/19047180).

## Live View of Figure 1E
<a href="/?bookmark=ce4e0c581f6cbc8e894aacc3a5566373"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure1DE/Figure1E.png" width="700"></a>

Bookmark: [ce4e0c581f6cbc8e894aacc3a5566373](/?bookmark=ce4e0c581f6cbc8e894aacc3a5566373)

Zooming into just colorectal (COAD) and kidney renal clear cell cancer (KIRC), we can see that rs6983267 is very accessible for COAD whereas in KIRC it is relatively inaccessible. The reverse is true for rs35252396. Red indicates higher chromatin accessibility and blue indicates lower.

### Steps to reproduce

1. __Filter to COAD and KIRC.__ Enter 'COAD OR KIRC' in the filter search bar to highlight and find samples that are COAD or KIRC. Choose 'Filter' from the menu next to the search bar.

	> <img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure1DE/atacseqfilter.gif" width="90%">

	> More help on our filter feature can be found here: <https://ucsc-xena.gitbook.io/project/overview-of-features/filter-and-subgrouping>

	> Note that 'OR' needs to be capitalized. 

## More Resources
* Check out other ATAC-seq vignettes: <https://atacseq.xenahubs.net>
* Check out our Xena online tutorials: <https://xena.ucsc.edu/getting-started/>
