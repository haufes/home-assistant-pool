# Home assiant config for pool control

Able to 
- Control the weekday schedual of the pool pump and heat pump via the UI (Hydro off peak hours)
- Control whether the pump and heat pump are following their scheduals or on manual control
- Monitor the temperature of the water and air
- Monitor the water presure at the filter
- Warn if the pump is running, but there is no water presure
- Monitor if the heat pump is running based on temperature increase of the water


![alt text](https://lh3.googleusercontent.com/2E4Yv6r-RpyCwkQaTBPESYk0M1LpvHssUGXeua4q5KJRFskp-Q1vOR2qAIqnIG0c2s9cxDFi0sf4bE1PLenfIpwFTPY2woea9urkpW2bhvDSDZ2vLKx9vcDEcWRUvhHvPjEa_kcYUEN2FuBDMUzgxiyLxbDsHDhdFos5roJy2eB7GH4xNgJmVCCzqdAWokZCdgCkr3FSNUZaXJQ2EK7op3kd22gY6_iIrYp2UxGTFzGGJG1ji-1WChEx6a0T_HLS41UWAvTmnU6CfnmbYUm3_ciXHhg8oqyRG8Bj1QzsjVaBcQXX_3IqTQI7xAEei01Z_qkXq6hVbAewGmNN3VPLoMM5jtd6414E_FhBO7C7F9QBKFnuK9fVmbh3QaKK1HG0syvVOonCULcuofebaiSAx5R6lPDr3Ya9YT20nmugQqsEJxs0ELttPVG6WcBp_t3uSprgsTgGvwCH7usMXY74BQEIWh0-12j4QwX--hwAEM-icOk_Lv0WC4QNRrgmWz_FVvy3EQFAs37KnUnXRmr_0S34oDZr5BQvWPP3g877dajJM78o2W7eA9C0My2ZYkUU-wyOgNqZkQz6ZQm0tPKkZTd3Qx3Cmkpy-MC7Wn1i1151vvUigVFCgKj1mO92MznsRKqWXdafZuE8dFXUZgipJ76EnImPQ5HwWdmbWcNYVI-P0XULb0BYCVmb=w1364-h630-no)

Hardware
 - [Raspberry Pi 3](https://www.amazon.ca/gp/product/B01CCF9BYG/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [8 Channel DC 5V Relay](https://www.amazon.ca/gp/product/B06XCN5JNH/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [Waterproof Digital Temperature Temp Sensor Probe DS18b20](https://www.amazon.ca/gp/product/B00KUNKR3M/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)
 - [Pressure Transducer Sensor](https://www.amazon.ca/gp/product/B01HZ3ZZOA/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
 - [MCP3008](https://www.arrow.com/en/products/mcp3008-isl/microchip-technology)
 

![Prototype](https://lh3.googleusercontent.com/waQtGIF67kGwf7V296dOhuWUJnspYXckcvVhmi2y508CW8mvcgHtvnjeL556jIWcE4PD1NDbTcQuVWMEWGL1gu0J4FUGL7j7nA9M1a0NdUv7eYiTDNlVLifd4En36SFTgVO5ZtdyHVRHeZuRUfRwUeLE3B7DIZmd8y2zdTM1E2I0fcjz5uRJbgfWyGSuWllJfVgxQQBDwS4A8UAPUsIwlB4ry0NrtjxUIYFmf2mea-lTEEQ0ilPRF_fkeH7gMJkJqKRfYXNa5lBtJM4pLN-tjyo0Lsk3pSAKP7P03BV4KuRhOH4CG5qegp2L61acqIS1iOqoTKphAy4zJpZFhqglPSdcN261rUtFQusJuK7NTWyy74r5mn_MDa85QxZQOlak9Gc7V5d4xpj3DKK5Wqm-zEAk1TZKP_1PS7hGdMDCXdz5v3YBvrO5-MjUTYctP8mZKgeLDErUKuGGGj0lgpLhMb4rJkbbK94wTMjZLd-PB_y3TIwtq_NsagGmVUeYJeq16_8794BJP7-Z4Vun9Sgn1kIttRSPrmyr1JMAcZtDjNWuEX0xXxBc2wwQjzPgG9aSjcKuiEVL6ya2nRvjoJkA1Qo9bsx5nY-nxR8IeVuPTl00LTzSEqjf0B5a9mCKMwI=w842-h631-no)

 Todo: wiring diagram
 
 References
 - [Multiple DS18B20 temperature sensors - Raspberry Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?t=167896)
 - [Reading from a MCP3002 analog-to-digital converter](http://raspberry.io/projects/view/reading-from-a-mcp3002-analog-to-digital-converter/)
 
 
Add secrets.yaml file after cloning
