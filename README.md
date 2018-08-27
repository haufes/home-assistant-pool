# Home Assistant config for pool control

## Features 
- Control the weekday schedual of the pool pump and heat pump via the UI (Hydro off peak hours)
- Control whether the pump and heat pump are following their scheduals or on manual control
- Monitor the temperature of the water and air
- Monitor the water presure at the filter
- Warn if the pump is running, but there is no water presure
- Monitor if the heat pump is running based on temperature increase of the water


![UI](https://lh3.googleusercontent.com/v1Uf9MVy6jaN_2t-V4kQCkd_2EOaAohvx3qK0AJ6RIJLizPPPgCjgLc7U4RYnaDYZ31S8QyjNLmTUkduZrAV-yvFJU3T1Zhc-bEiuckZ57EOceDclWlPkUdAby_INQH3O4BVtT4Ap424n5Wg2TF1Nv78FVVHMQgyM_nEQIMJe4yjAD3n4-iO9cnhm2XlpnNdB_hETr_KXyTs-NJ_fl8InUcygpElL4StRbVhkAs0B_6JkYQdWTRs-TrxgP0otdB2uHAs3bpYPKtmJE7qHFfgF2hhn1hfR93EPRZKvlO9NnzZyEAj-Z4tcqGqlxDoR-bEegFvktiBJpJIRFio3zw3BAr2RiVgnjK0ZHg0kGHP4d4Aki1ghiaQc7tEpkkPUsZGMYD5YMC_BoEVTD_PDDnJwBR5X1mZCx3MDpjuN5Cjb73TNNjO08GARUknxXCGvW8Ju6pwF1Q6VshGyicuVMRmDFyLC2jvd27cYooCHx2Un9vHc5fbepV56I1TBYKHEp_13y5QVXOgpEDhELMK8dQFeUjIT04g1Lu1ViQRbcR7_5eb0sH2Bd75qYUwBf4cATH0WJ0RXOLDHF4XPQRWB89lYtN0q8cvhM1DaGb_ccuhXbmIPhzR0NPABBGA5SbGpQRiDpL9GGr11z67yT5sKWsVYY4lcrjArgz9HlQq99z5SYmeKyozCS6F6h66=w1123-h631-no)

## Hardware
 - [Raspberry Pi 3](https://www.amazon.ca/gp/product/B01CCF9BYG/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [8 Channel DC 5V Relay](https://www.amazon.ca/gp/product/B06XCN5JNH/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [Waterproof Digital Temperature Temp Sensor Probe DS18b20](https://www.amazon.ca/gp/product/B00KUNKR3M/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)
 - [Pressure Transducer Sensor](https://www.amazon.ca/gp/product/B01HZ3ZZOA/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
 - [MCP3008](https://www.arrow.com/en/products/mcp3008-isl/microchip-technology)
 

![Prototype](https://lh3.googleusercontent.com/waQtGIF67kGwf7V296dOhuWUJnspYXckcvVhmi2y508CW8mvcgHtvnjeL556jIWcE4PD1NDbTcQuVWMEWGL1gu0J4FUGL7j7nA9M1a0NdUv7eYiTDNlVLifd4En36SFTgVO5ZtdyHVRHeZuRUfRwUeLE3B7DIZmd8y2zdTM1E2I0fcjz5uRJbgfWyGSuWllJfVgxQQBDwS4A8UAPUsIwlB4ry0NrtjxUIYFmf2mea-lTEEQ0ilPRF_fkeH7gMJkJqKRfYXNa5lBtJM4pLN-tjyo0Lsk3pSAKP7P03BV4KuRhOH4CG5qegp2L61acqIS1iOqoTKphAy4zJpZFhqglPSdcN261rUtFQusJuK7NTWyy74r5mn_MDa85QxZQOlak9Gc7V5d4xpj3DKK5Wqm-zEAk1TZKP_1PS7hGdMDCXdz5v3YBvrO5-MjUTYctP8mZKgeLDErUKuGGGj0lgpLhMb4rJkbbK94wTMjZLd-PB_y3TIwtq_NsagGmVUeYJeq16_8794BJP7-Z4Vun9Sgn1kIttRSPrmyr1JMAcZtDjNWuEX0xXxBc2wwQjzPgG9aSjcKuiEVL6ya2nRvjoJkA1Qo9bsx5nY-nxR8IeVuPTl00LTzSEqjf0B5a9mCKMwI=w842-h631-no)

 ## Wiring diagram
 Todo
 
 ## References
 - [Multiple DS18B20 temperature sensors - Raspberry Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?t=167896)
 - [Reading from a MCP3002 analog-to-digital converter](http://raspberry.io/projects/view/reading-from-a-mcp3002-analog-to-digital-converter/)
 - [Python code to use the MCP3008 analog to digital converter with a Raspberry Pi or BeagleBone black.](https://github.com/adafruit/Adafruit_Python_MCP3008)
 - [Raspberry Pi Analog Water Sensor Tutorial | Rototron](https://www.rototron.info/raspberry-pi-analog-water-sensor-tutorial/)
 
## Install

Install Home assiant, then clone this repo into it's config folder.

Add a secrets.yaml file after cloning. Contains the login and email details for gmail and recipients
