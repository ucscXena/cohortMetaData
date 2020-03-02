# TCGA ATAC-seq Walk-through: Figure 7H & I

[Corces et. al. 2018](http://science.sciencemag.org/content/362/6413/eaav1898) overlapped WGS and ATAC-seq data to uncover a mutation upstream of the FGD4 gene in a bladder cancer (sample TCGA-BL-A13J-01A) where the variant allele frequency observed in ATAC-seq is markedly higher than the variant allele frequency observed in WGS. This mutation is associated with a significant increase in accessibility compared to other bladder cancer samples in this cohort and is accompanied by the highest FGD4 gene expression among the 10 samples. Further, higher FGD4 expression is significantly associated with worse overall survival in bladder cancer, leading the authors to believe this mutation is likely to have functional consequence in this particular cancer.

Here we recreate a variation of this figure.

## Live View of Figure 7H
<a href="/?bookmark=c54e9592355684ed00bc6efce7e0312b"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure7HI/Figure7H.png" width="700"></a>

Here we can see chromatin accessibility in the promoter region of FGD4 for 10 samples in TCGA Bladder Cancer. We can see that TCGA-BL-A13J-01A (top sample) has increased accessibility in the region upstream from FGD4 (column D), as highlighted by the black oval. This increased accessibility is associated with the highest FGD4 gene expression for this sample (column C).

At the top of column D we have highlighted the ATACseq peak (BLCA_65729) that overlaps with the eFGD4 point mutation ("enhancer FGD4") at chr12:32385775:C->T. Note that it is not possible to visualize the mutation in the mutation data on Xena because mutations outside the coding region are considered protected data by TCGA.

[Click here for a live view.](/?bookmark=c54e9592355684ed00bc6efce7e0312b)

### Steps to reproduce

1. __Start [here](/?bookmark=8392712ad22f0eef71624061c04b17e5).__

	> Note that the GDC Pan-Cancer (PANCAN) cohort is already selected and we have filtered down to just those samples that have ATAC-seq data.

2. __Add cancer type to view.__ Click 'Add Column' next to the samples column, select 'Phenotypic', and select 'project_id'. Click 'done'.

3. __Add ATAC-seq peaks for chr12:32335774-32435774.__ Click 'Add Column' and enter 'chr12:32335774-32435774' as the 'Gene or Position'. Click 'show Advanced' and choose 'All peak signal' under 'ATAC-seq'. Click 'done'.
	
	> Note that the color threshold in the images are different than what is used by default (new color thresholds: max:4 min:-2).  See [this help](https://ucsc-xena.gitbook.io/project/how-do-i/how-do-i-change-the-color-threshold-for-a-column) for more information.
	
	> We can see there is a lot of variation for in chromatin accessibility for this region across all cancer types

4. __Filter to bladder cancer (BLCA).__ Enter 'BLCA' in the filter search bar to highlight and find bladder samples. Choose 'Filter' from the menu next to the search bar.

	> <img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure7HI/atacseqfilterblca.gif" width="90%">

	> We can see the third sample from the top (TCGA-BL-A13J-01A) has increased accessibility upstream from FGD4. [Click here for a live view.](/?bookmark=9174d81f5bc9f3a2a27657ffd586c574)

5. __Examine relationship to FGD4 expression.__ Click 'Add Column' and enter 'FGD4' as the 'Gene or Position'. Click 'Gene Expression' and then click 'done'. Grab the top of the column and move it to the left.

	> <img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure7HI/makedragcolumn.gif" width="90%">

	> We can see that TCGA-BL-A13J-01A has the highest FGD4 gene expression for these samples. [Click here for a live view.](/?bookmark=c94f38d25c5f66cbfe8881824ed70806)


## Live View of Figure 1I
<a href="/?bookmark=2897c1734c3dbdcddd6b5e424d351904"><img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure7HI/Figure7I.png" width="700"></a>

Here we can see that higher FGD4 expression is significantly associated with worse overall survival in bladder cancer. [Click here for a live view.](/?bookmark=2897c1734c3dbdcddd6b5e424d351904)

1. __Start [here](/?bookmark=c6d33d31653d6a6f5c7ba413b61ba33c)__

2. __Choose the GDC TCGA Bladder Cancer (BLCA) study.__ Type 'GDC TCGA Bladder Cancer' in the 'Search for Study' field. Choose the GDC TCGA Bladder Cancer (BLCA) study and click 'done'.

3. __Add FGD4 gene expression and mutation status.__ Type 'FGD4' in the 'Add Gene or Position' field. Check the 'Gene Expression' and Somatic 'Mutation' check boxes and click 'done'.
	
	> We can see here that there is a range of gene expression but not very many mutations in the gene itself.

4. __Generate a KM plot on FGD4 expresion.__ Click on the column menu at the top of the column and choose 'Kaplan Meier Plot'

	> <img src="https://github.com/ucscXena/cohortMetaData/raw/master/hub_atacseq.xenahubs.net/Figure7HI/atacseqfgd4km.gif" width="90%">

	> We can see that samples with high FGD4 expression have worse overall survival. [Click here for a live view.](/?bookmark=2897c1734c3dbdcddd6b5e424d351904)

## More Resources

* Check out other ATAC-seq vignettes: <https://atacseq.xenahubs.net>
* Check out our Xena online tutorials: <https://xena.ucsc.edu/getting-started/>
* KM help <https://ucsc-xena.gitbook.io/project/overview-of-features/kaplan-meier-plots>
