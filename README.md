# BasqueGLUE

## A Natural Language Understanding Benchmark for Basque

## *Euskarazko Hizkuntza Naturalaren Ulermena Ebaluatzeko Euskarria*

Natural Language Understanding (NLU) technology has improved significantly over the last few years, 
and multitask benchmarks such as GLUE are key to evaluate this improvement in a robust and general way. 
These benchmarks take into account a wide and diverse set of NLU tasks that require some form of 
language understanding, beyond the detection of superficial, textual clues. However, they are costly 
to develop and language-dependent, and therefore they are only available for a small number of languages. 

We present BasqueGLUE, the first NLU benchmark for Basque, which has been elaborated from previously 
existing datasets and following similar criteria to those used for the construction of GLUE and SuperGLUE. 
BasqueGLUE is freely available under an open license.



### The 9 tasks included in BasqueGLUE:

| Dataset        | \|Train\| | \|Val\| | \|Test\| | Task                   | Metric | Domain          |
|----------------|-----------|---------|----------|------------------------|--------|-----------------|
| NERCid         |   51,539  |  12,936 |  35,855  | NERC                   | F1     | News            |
| NERCood        |   64,475  |  14,945 |  14,462  | NERC                   | F1     | News, Wikipedia |
| FMTODeu_intent |    3,418  |   1,904 |   1,087  | Intent classification  | F1     | Dialog system   |
| FMTODeu_slot   |   19,652  |  10,791 |   5,633  | Slot filling           | F1     | Dialog system   |
| BHTCv2         |    8,585  |   1,857 |   1,854  | Topic classification   | F1     | News            |
| BEC2016eu      |    6,078  |   1,302 |   1,302  | Sentiment analysis     | F1     | Twitter         |
| VaxxStance     |      864  |     206 |     312  | Stance detection       | MF1*   | Twitter         |
| QNLIeu         |    1,764  |     230 |     238  | QA/NLI                 | Acc    | Wikipedia       |
| WiCeu          |  408,559  |     600 |   1,400  | WSD                    | Acc    | Wordnet         |
| EpecKorrefBin  |      986  |     320 |     587  | Coreference resolution | Acc    | News            |


NERCid stands for NERC in-domain, while NERCood stands for NERC out-of-domain. 
Dataset sizes for sequence labeling tasks (NERC and Slot filling) are given in tokens.
Acc refers to accuracy, while F1 refers to micro-average F1-score. *The metric used for VaxxStance is macro-average F1-score of two classes: FAVOR and AGAINST.

Note: The train file for WiCeu needs to be uncompressed.


### Examples of each task:

| NERC                            |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        Tokens:  | Helburuetako bat McLareni eta Ferrariri aurre egitea izango du taldeak .                                                                                                                                                                       |
|                         Labels: |        O       O   B-ORG    O    B-ORG     O     O      O     O    O    O                                                                                                                                                                      |
|                    Translation: | One of the objectives that will have the team is to confront McLaren and Ferrari.                                                                                                                                                              |

| Intent Class (FMTODeu_intent)  |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           Text: | alarma ezarri gaurko 6:00etan                                                                                                                                                                                                                  |
|                    Translation: | set the alarm today at 6:00am                                                                                                                                                                                                                  |
|                         Intent: | alarm/set alarm                                                                                                                                                                                                                                |

| Slot Filling (FMTODeu_slot)     |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         Tokens: |          Euria      egingo  du    gaur     ?                                                                                                                                                                                                   |
|                         Labels: | B-weather/attribute   O    O  B-datetime  O                                                                                                                                                                                                    |
|                    Translation: | Is it going to rain today?                                                                                                                                                                                                                     |

| Topic Classification (BHTCv2)   |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           Text: | Gurasotasun baimena eta seme-alabak zaintzeko baimena lau hilabetera luzatzeko proposamena egitea onartu du Europako Batzordeak. Proposamenak aldaketa handia ekarriko luke Hego Euskal Herrian, lau asteetara luzatu berri baita baimen hori. |
|                    Translation: | The European Commission has approved to make the proposal of extending paternity leave to four months. The proposal would represent an important change in Hego Euskal Herria, as it has been extended recently to four weeks.                 |
|                          Topic: | Gizartea (society)                                                                                                                                                                                                                             |

| Sentiment Analysis (BEC)        |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           Text: | Mezu txoro, patetiko eta lotsagarri hori ongi hartuko duenik badela uste du PSEk.                                                                                                                                                              |
|                    translation: | PSE thinks there are people who will respond positively to that crazy, pathetic and shameful message.                                                                                                                                          |
|                       Polarity: | Negative                                                                                                                                                                                                                                       |

| Stance Detection (VaxxStance)   |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           Text: | Gure nagusiak babestuko dituen txertoa martxan da. Zor genien. Gaur mundua apur bat hobeagoa da. #OsasunPublikoarenGaraipena #GureGaraipena                                                                                                    |
|                    Translation: | The vaccine that will protect our elderly people is on it’s way. We owned them. Today the world is a little bit better. #TheVictoryOfPublicHealthcare #OurVictory                                                                              |
|                         Stance: | FAVOR                                                                                                                                                                                                                                          |

| QNLI                            |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       Question: | “Irrintziaren oihartzunak” dokumentalaz gain, zein best lan egin ditu zinema arloan?                                                                                                                                                           |
|                    Translation: | Aside from the documentary “Irrintziaren ohiartzunak”, in what other projects has she worked on in the field of cinema?                                                                                                                        |
|                       Sentence: | “Irrintziaren oihartzunak” du lehen filma zuzendari eta gidoilari gisa.                                                                                                                                                                        |
|                    Translation: | “Irrintziaren oihartzunak” is her first film as a director and scriptwriter.                                                                                                                                                                   |
|                            NLI: | not_entailment                                                                                                                                                                                                                                 |

| WiC                             |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      Sentence1: | Asterix, zazpi [egunen] segida asmatu zuen galiarra .                                                                                                                                                                                          |
|                    Translation: | Asterix, the Gaul who invented the 7 [days] week.                                                                                                                                                                                              |
|                      Sentence2: | Etxeko landareek sasoi aktiboan tenperatura epelak behar dituzte : [egunez] 25 C ingurukoak .                                                                                                                                                  |
|                    Translation: | House plants need warm temperatures during active season: around 25C in [daylight].                                                                                                                                                            |
|                     Same sense: | False                                                                                                                                                                                                                                          |

| Coreference (EpecKorrefBin)     |                                                                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           Text: | Birmoldaketan daudenen artean [Katalunia , Madril , Hego Euskal Herria , Aragoi , Balear irlak eta Errioxa] aurkitzen dira . [Horien] artean , Hego Euskal Herriak 47.870 milioi pezeta jasoko ditu .                                          |
|                    Translation: | Among those under reconversion are [Catalonia, Madrid, Southern Basque Country, Aragon, Balearic islands and Rioja] . Among [them], the Southern Basque Country will receive 47,870 million pesetas.                                           |
|                    Coreference: | True                                                                                                                                                                                                                                           |


For more details, each dataset is provided with their corresponding README file.

### Evaluation

We provide an evaluation python script. Finetuning is left up to the user, script evaluates predictions provided on each task against test gold standards (test.jsonl files).
The script expects the same format the datasets have.

```
python3 eval_basqueglue.py  \
        --task [nerc_id | nerc_od | intent | slot | bhtc | bec | vaxx | qnli | wic | coref] \
        --pred prediction_file.jsonl \
        --ref reference_file.jsonl #(usually test.jsonl)
```                    


Authors
-----------
Gorka Urbizu [1], Iñaki San Vicente [1], Xabier Saralegi [1],
Rodrigo Agerri [2] and Aitor Soroa [2]


Affiliation of the authors: 
[1] Elhuyar Foundation
[2] HiTZ Center - Ixa, University of the Basque Country UPV/EHU



Licensing
-------------

Each dataset of the BasqueGLUE benchmark has it's own license (due to most of them being or 
being derived from already existing datasets). See their respective README files for details. 

But, here we provide a brief summary of them:

| Dataset        | License                             |
|----------------|-------------------------------------|
| NERCid         |                     CC BY-NC-SA 4.0 |
| NERCood        |                     CC BY-NC-SA 4.0 |
| FMTODeu_intent |                     CC BY-NC-SA 4.0 |
| FMTODeu_slot   |                     CC BY-NC-SA 4.0 |
| BHTCv2         |                     CC BY-NC-SA 4.0 |
| BEC2016eu      | Twitter's license + CC BY-NC-SA 4.0 |
| VaxxStance     | Twitter's license + CC BY       4.0 |
| QNLIeu         |                     CC BY-SA    4.0 |
| WiCeu          |                     CC BY-NC-SA 4.0 |
| EpecKorrefBin  |                     CC BY-NC-SA 4.0 |



For the rest of the files of the benchmark, including the evaluation script, the following license applies:

Copyright (C) by Elhuyar Foundation. 
This benchmark and evaluation scripts are licensed under the Creative Commons Attribution Share Alike 4.0
International License (CC BY-SA 4.0). To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.




Acknowledgements
-------------------
If you use this benchmark please cite the following paper:

- G. Urbizu, I. San Vicente, X. Saralegi, R. Agerri, A. Soroa. BasqueGLUE: A Natural Language Understanding Benchmark for Basque. In proceedings of the 13th Language Resources and Evaluation Conference (LREC 2022). June, 2022. Marseille, France

 



Contact information
-----------------------
Gorka Urbizu, Iñaki San Vicente: {g.urbizu,i.sanvicente}@elhuyar.eus
