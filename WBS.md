# Work Breakdown Structure
### Portafoglio

|Project Start | 23/01/2023 |
| ---          |   ---      |


| Level       | WBS       | Task Descritpion                                | Assigned To                           | Start        | End          | Notes       				        |  DUR     |  Name   | Predecessors                    |
|   ---       |     ---   |       ---                                       |      ---                              | ---          | ---          |    ---      				        |   ---    |  ---    |  ---                            |
|   **1**     |   **1**   |   **ANALYSIS**                                  |                                       |              |              |           				          |          |  A      |                                 |
|   1         |   1       |   Analyze project requirements                  |   Ambrosi, Klein, Marcolini, Villardi |   23/01/2023 |   24/01/2023 |             				        |  1       |  B      |  -                              |
|   2         |   1.1     |   Create WBS and RACI matrix files              |   Marcolini                           |   24/01/2023 |   24/01/2023 |             				        |  1       |  C      |  -                              |
|   **1**     |   **2**   |   **DEVELOPMENT AND TESTING**                   |                                       |              |              |             				        |          |         |                                 |
|   2         |   2.1     |   Choose programming language                   |   Ambrosi, Klein, Marcolini, Villardi |   24/01/2023 |   24/01/2023 |   Python    				        |  1       |  D      |  -                              |
|   2         |   2.2     |   Add a version checklist                       |   Villardi                            |   30/01/2023 |   05/02/2023 |             				        |  1       |  E      |  -                              |
|   2         |   2.3     |   Handle library dependencies                   |   Ambrosi                             |   30/01/2023 |   05/02/2023 |   requirements.txt, core.py |  2       |  F      |  D                              |
|   2         |   2.4     |   Get csv file from Yahoo Finance               |   Klein                               |   25/01/2023 |   29/01/2023 |            					        |  1       |  G      |  D                              |
|   2         |   2.5     |   Create dictionary containing the csv data     |   Ambrosi                             |   25/01/2023 |   29/01/2023 |             				        |  1       |  H      |  D                              |
|   2         |   2.6     |   Convert from csv to json                      |   Villardi                            |   25/01/2023 |   29/01/2023 |             				        |  1       |  I      |  D, H                           | 
|   2         |   2.7     |   Convert from csv to yaml                      |   Marcolini                           |   25/01/2023 |   29/01/2023 |             				        |  1       |  J      |  D, H                           |
|   2         |   2.8     |   Add software metrics file                     |   Ambrosi                             |   30/01/2023 |   05/02/2023 |                             |  1       |  K      |  D                              |
|   2         |   2.9     |   Test the program                              |   Ambrosi                             |   25/01/2023 |   29/01/2023 |             				        |  1       |  L      |  D           				           |
|   2         |   2.10    |   Check if PEP7, PEP8 and DOCTEST are respected |   Klein                               |   30/01/2023 |   05/02/2023 |                             |  1       |  M      |  D      						             |
|   **1**     |   **3**   |   **DOCUMENTATION**                             |                                       |              |              |            					        |          |         |        						             |
|   1         |   3.1     |   Document project                              |   Klein                               |   25/01/2023 |   29/01/2023 |   README.md					        |  1       |  N      |  D, E, F, G, H, I, J, K, L, M   |


