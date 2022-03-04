# malaria_case_study
BINP29 exercise by Dorottya Ralbovszki

## Obtaining files
The files containing the genomes of the *Plasmodium* species and the outgroup taxon *Taxoplasma gondii* were obtained from the course server as plasmodiumGenomes.tgz.

## Gene prediction
Gene prediction was carried out on all genome files on the course server as:

```shell
gmes_petap.pl --ES --sequence /path_to_file/file.genome
```

Version: GeneMark-ES Suite version 4.62_lic

## Filtering the *Haemoproteus tartakovskyi* genome
### Keeping the scaffolds that are longer than 3000 nucleotides
For that filtering step, the filtering_scaffolds_3000.py script was run as:
```shell
python /path_to_script/filtering_scaffolds_3000.py /path_to_file/Haemoproteus_tartakovskyi.genome
```
### Filtering according to GC content
For that filtering step 30% or below was choosen which is a blabla and for that the GC_content_malaria.py script was run as:
```shell
python /path_to_script/GC_content_malaria.py /path_to_file/above_3000_filtered.genome
```

## Gene prediction on the filtered genome file
The gene prediction was run exactly as before.

## Creating fasta files from the filtered genome file and the gene prediction file
First, the gene prediction file was changed to have the right format for gffParse.pl as:
```shell
cat gene_prediction.gtf | sed "s/ length=.\*\tGeneMark.hmm/\tGeneMark.hmm/" > fixed_file.gtf
```

Than the fasta was created on the course server as:
```shell
perl /path_to_program/gffParse.pl  -i ../path_to_file/filetered_file.genome -g /path_to_file/gene_prediction_file.gtf -c -p
```
Version: gffParse.pl version 1.1

## Removing scaffolds that have avian origin
First, blastp was carried out as:
```shell
blastp -query gffParse.faa -db SwissProt -evalue 1e-10 -out Ht.blastp
```
Version: blast 2.11.0, build Oct  6 2020 03:24:05
The e-value cut off was set according to the previous gene annotation exercise. This cut off may cause some bird proteins to be undetected since hits that didn't meet the e-value filter arem't identified so they will "stay" in the genome file surviving filtering.

After the blastp, the scaffolds that contained a bird protein hit were filtered out from the genome file using the script blastprocess.py:
```shell
python /path_to_script/blastprocess.py /path_to_file/file.blastp /path_to_file/SwissProt_dat_file /path_to_file/file.fna /path_to_file/file.genome /path_to_file/output.genome
```
More information about the script can be found in the script comments. The output is a genome file not containing the scaffolds thad had a bird protein hit.

## Gene prediction on the newly filtered genome file
This was run on the server as before:

```shell
gmes_petap.pl --ES --sequence /path_to_file/file.genome
```

## Creating fasta files from the filtered genome file and the gene prediction file for all species
First, the gene prediction file of the filtered file was changed to have the right format for gffParse.pl as:
```shell
cat gene_prediction.gtf | sed "s/ length=.\*\tGeneMark.hmm/\tGeneMark.hmm/" > fixed_file.gtf
```
Then, gffParse.pl was run as before on all genome files and their gtf files on the course server:
```shell
perl /path_to_program/gffParse.pl  -i ../path_to_file/file.genome -g /path_to_file/file.gtf -b shortname -c -p
```
## Answering question 3
Python and bash scripts were written to answer this question. They were run as:
```shell
for f in ../genome/*.genome; do python q_3_genome.py "$f"; echo "$f"; done > q_3_genome.txt

for f in ../fasta_all/*.fna; do python q_3_genes.py "$f"; echo "$f"; done > q_3_genes.txt

for f in ../genome/*.genome; do python q_3_gc.py "$f"; echo "$f"; done > q_3_gc.txt
```
## Identifying orthologs
To install proteinortho and BUSCO, first conda was installed as:
```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh

bash Miniconda3-py39_4.11.0-Linux-x86_64.sh

conda activate

conda config --add channels bioconda


conda install proteinortho

conda update proteinortho

proteinortho6.pl /path_to_files/{Ht,Pb,Pc,Pf,Pk,Pv,Py,Tg}.faa
```
## Filling out group table
Getting the number of Proteinortho IDs found in all eight genomes
```shell
cat myproject.proteinortho.tsv | grep "^8" | wc -l
```
