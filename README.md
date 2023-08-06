# ITT_analysis
Comparing cycling ITT performances 1993 - 2023

Since people were very impressed by Jonas Vingegaard's Tour de France 2023 stage 16 ITT performance (Tom Dumoulin said it was the best ITT ever), I decided to do a quick comparison.
I scraped the data for all ITT's from major 1 week and GT's from 1993 to 2023 and calculated the average speed of the top 10 finishers to get a good baseline to compare to (assuming the fastest 10 finishers of a stage did well).
Then I calculated every result's difference compared to that baseline and JV's stage 16 ITT is far beyond any other.

The script is far from optimal, but it does the work. You could get a list of every tour's stages and find ITT's from there rather than going through all of them and checking for 'ITT' etc.

Top 20 performances according to that criterion (stage 0 means prologue):

| Rnk | FinalGC | RiderName | Avg | Race | Year | Stage | Distance | ProfileScore | AvgTop10 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | VINGEGAARD Jonas | 41.227 | Tour de France | 2023 | 16 | 22.4 km | 109 | 8.2 % |
| 1 | 2 | ZÜLLE Alex | 43.881 | Vuelta a Espana | 1993 | 21 | 44.6 km |  | 6 % |
| 1 | 1 | INDURAIN Miguel | 50.548 | Tour de France | 1994 | 9 | 64 km | 37 | 5.9 % |
| 1 | 2 | ULLRICH Jan | 48.178 | Tour de France | 2003 | 12 | 47 km | 49 | 5.1 % |
| 1 | 1111 | BOARDMAN Chris | 55.267 | Tour de France | 1994 | 0 | 7.2 km | 2 | 5 % |
| 1 | 1 | PECHARROMÁN José Antonio | 36.028 | Volta a Catalunya | 2003 | 6 | 13.1 km |  | 5 % |
| 1 | 1 | ULLRICH Jan | 42.494 | Vuelta a Espana | 1999 | 20 | 46 km |  | 5 % |
| 105 | 12 | ESCARTÍN Fernando | 55.149 | Tour de France | 1994 | 0 | 7.2 km | 2 | 4.8 % |
| 1 | 1 | ULLRICH Jan | 43.194 | Tour de France | 1997 | 12 | 55 km | 145 | 4.8 % |
| 151 | 1111 | PIOVACCARI Giusvan | 43.194 | Tour de France | 1997 | 12 | 55 km | 145 | 4.8 % |
| 1 | 2 | ULLRICH Jan | 49.791 | Tour de France | 1998 | 20 | 53 km | 58 | 4.7 % |
| 1 | 8 | MCGEE Bradley | 48.706 | Giro d Italia | 2004 | 0 | 6.9 km | 8 | 4.7 % |
| 1 | 2 | PÉREZ Santiago | 28.424 | Vuelta a Espana | 2004 | 15 | 29.6 km | 214 | 4.7 % |
| 1 | 116 | GANNA Filippo | 56.636 | Tirreno Adriatico | 2020 | 8 | 10.1 km | 0 | 4.6 % |
| 1 | 1 | CANCELLARA Fabian | 50.053 | Tour de Suisse | 2009 | 0 | 7.8 km |  | 4.6 % |
| 2 | 1 | ROMINGER Tony | 43.313 | Vuelta a Espana | 1993 | 21 | 44.6 km |  | 4.6 % |
| 1 | 1 | ARMSTRONG Lance | 23.436 | Tour de France | 2004 | 16 | 15.5 km | 249 | 4.6 % |
| 1 | 76 | GANNA Filippo | 55.348 | Tirreno Adriatico | 2023 | 1 | 11.5 km | 0 | 4.5 % |
| 1 | 70 | SOBRERO Matteo | 46.607 | Giro d Italia | 2022 | 21 | 17.4 km | 30 | 4.5 % |
| 1 | 1111 | OLANO Abraham | 52.005 | Vuelta a Espana | 1999 | 6 | 46.4 km |  | 4.5 % |

For reference, Pogacar's TdF 2020 stage 20 ITT is 'only' 61st, being 3.4% faster than the average of the top 10.
