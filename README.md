# covid-19-model
 The SIR model fitted to COVID-19 infected cases data from Wuhan. Apply parameters of SIR to UK for prediction.

## Wuhan model

![wuhan_model](Wuhan/wuhan_model.png)

`wuhan_SIR_model.py' fits parameters in SIR model: gamma and beta
- gamma: contact parameter = 1/R0
- beta: recovery rate = 1/days-required-to-recover
  
Current fitted parameter:

|gamma|beta|
|---|---|
|0.33838125|0.06476182|

|R0|recovery-day|
|---|---|
|2.9552465186097683|15.441196085990235|

Covariance matrix:
|pcov|gamma|beta|
|---|---|---|
|gamma|5.10117057e-06|4.55526000e-07|
|beta|4.55526000e-07|9.14512396e-07|

Last update: 15 Mar 2020

## Compare South Korea case development data

![S_Korea](South_Korea/s_korea_model.png)

Assume suspected population of south korea is 51/11 larger than Wuhan. Data with selected days fitted to SIR model. The above figure showed the fast outbreak part of the confirmed cases between **30th Jan and 24th Feb** (25 days).

Fitted parameters:

|gamma|beta|
|---|---|
|1.43634329|1.18480972|

|R0|recovery-day|
|---|---|
|0.6962123914245263|0.8440173825556665|

Note: R0 in S Korea seemed to be smaller than 1.

Covariance matrix:
|pcov|gamma|beta|
|---|---|---|
|gamma|5.80282701e-05|5.65953981e-05|
|beta|5.65953981e-05|5.60933292e-05|

Last update: 23 Mar 2020

## UK prediction

![UK_predict](UK/UK_prediction.png)

Note: y axis is **log10** of infected cases.

Last update: 23 Mar 2020