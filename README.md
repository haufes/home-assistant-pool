# Home Assistant config for pool control

This repository contains the config files for my Home Assiant installation as well as the wiring and part details. 

## Features 
- Control the weekday schedual of the pool pump and heat pump via the UI (Hydro off peak hours)
- Control whether the pump and heat pump are following their scheduals or on manual control
- Monitor the temperature of the water and air
- Monitor the water presure at the filter
- Warn if the pump is running, but there is no water presure
- Monitor if the heat pump is running based on temperature increase of the water


![UI](XUYUpdRn6QAPsC8mUuM3jmWnTPGO2fbyvdCzQvwz3KISJVSdbpSBATFoEVtHP5atw4mNS3kBz0JXPJb_2VblFy4hK2IadFxCQJflW3N6unxs2x7CwSqPSjAIPp0F1gqPCSJSB1n4EnE7XgXxm4h2QoROAwF0hNys0OF3jeCqSwJC6GTA1SHHZUlRkXr9W2J2DDJBsFBJkX5HUdZQIwfip6i_jPsxvlk8UYJlDNrdWkMLwp_1Qko6PnaSOgzS)

Changed from a MCP3008 to MCP3304 to get a better resolution of the pressure sensor.

## Hardware
 - [Raspberry Pi 3](https://www.amazon.ca/gp/product/B01CCF9BYG/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [8 Channel DC 5V Relay](https://www.amazon.ca/gp/product/B06XCN5JNH/ref=oh_aui_detailpage_o09_s00?ie=UTF8&psc=1)
 - [Waterproof Digital Temperature Temp Sensor Probe DS18b20](https://www.amazon.ca/gp/product/B00KUNKR3M/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)
 - [Pressure Transducer Sensor](https://www.amazon.ca/gp/product/B01HZ3ZZOA/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
 - ~~[MCP3008](https://www.arrow.com/en/products/mcp3008-isl/microchip-technology)~~
 - [MCP3304](https://www.arrow.com/en/products/mcp3304-cip/microchip-technology) Better resolution than the MCP3008
 

![Prototype](https://lh3.googleusercontent.com/waQtGIF67kGwf7V296dOhuWUJnspYXckcvVhmi2y508CW8mvcgHtvnjeL556jIWcE4PD1NDbTcQuVWMEWGL1gu0J4FUGL7j7nA9M1a0NdUv7eYiTDNlVLifd4En36SFTgVO5ZtdyHVRHeZuRUfRwUeLE3B7DIZmd8y2zdTM1E2I0fcjz5uRJbgfWyGSuWllJfVgxQQBDwS4A8UAPUsIwlB4ry0NrtjxUIYFmf2mea-lTEEQ0ilPRF_fkeH7gMJkJqKRfYXNa5lBtJM4pLN-tjyo0Lsk3pSAKP7P03BV4KuRhOH4CG5qegp2L61acqIS1iOqoTKphAy4zJpZFhqglPSdcN261rUtFQusJuK7NTWyy74r5mn_MDa85QxZQOlak9Gc7V5d4xpj3DKK5Wqm-zEAk1TZKP_1PS7hGdMDCXdz5v3YBvrO5-MjUTYctP8mZKgeLDErUKuGGGj0lgpLhMb4rJkbbK94wTMjZLd-PB_y3TIwtq_NsagGmVUeYJeq16_8794BJP7-Z4Vun9Sgn1kIttRSPrmyr1JMAcZtDjNWuEX0xXxBc2wwQjzPgG9aSjcKuiEVL6ya2nRvjoJkA1Qo9bsx5nY-nxR8IeVuPTl00LTzSEqjf0B5a9mCKMwI=w842-h631-no)

 ## Wiring diagram
 ![Wiring diagram](https://lh3.googleusercontent.com/eiYkt-wOfxL9Qv-RUSDkqZ2L9bfmHqCE7K6mz7LyLNYNLfosTCYQESngmEZoNrIEtnQ_40ytn3GTp26-CWt-OcqcY03n6nWddu0i6QY2B1N2w2-UwPgFAm-RfXL8cnL5oFGaiXnB3GDshH64vcoRjBgHPrrA3t7botwhrSThMWIx0TY1QvWOMH3njeQkqR7gbOXLsFrWLf461xFsiCFxGxIt0Y_J-litAL2rI51_KiV7T__OS1nmh6ISJKWPUPPDM3nUqG6Ck-XfVMrl_35BVq2Z0bhcl_0DZf_Iwllxeght8OLlnJJhLRV8VcDiViES8mlDO6BZJzBvt64hVZg6obhGHB9_9RTnIpjHNl09x7rZlUXsOl0xOfREqutuDYC3AQ4xJbafswRiv-drhsinZkbUzGNTUqsmDMFSW1GHa36-Lw4YCVd_-DsvVk15aNWPYAq5xyd2aJ8ETUXD0sL4MY1fu7IR5obbMUQjYd-kOK_mtSh10mwZyG9ZgqB0pud_zFed8wrJk066ePGZsYCk5Le8xhbxcr6paDik7H09r3MMYMetHl9jC5tKqLnoUBTNC2YcSmdkafI0IYfKWqip4ZU9eFvwpre7y3kLMtcgWdBVIXmavGN5_GAO_n9b4mmbANJnVvPaiz4stVvO3gVmpVBfeiEmKihw50ftCKWLhF5zlU2W-VG01mAv=w1366-h402-no)
 
 ## References
 - [Multiple DS18B20 temperature sensors - Raspberry Pi Forums](https://www.raspberrypi.org/forums/viewtopic.php?t=167896)
 - [Reading from a MCP3002 analog-to-digital converter](http://raspberry.io/projects/view/reading-from-a-mcp3002-analog-to-digital-converter/)
 - [Python code to use the MCP3008 analog to digital converter with a Raspberry Pi or BeagleBone black.](https://github.com/adafruit/Adafruit_Python_MCP3008)
 - [Raspberry Pi Analog Water Sensor Tutorial | Rototron](https://www.rototron.info/raspberry-pi-analog-water-sensor-tutorial/)
 - [Install docker] (https://howchoo.com/g/nmrlzmq1ymn/how-to-install-docker-on-your-raspberry-pi)
## Install

Install the docker home assistant container

sudo docker run --restart always --init -d --name="homeassistant" --cap-add ALL -v /lib/modules:/lib/modules -v /sys:/sys --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -v /home/pi/homeassiant-pool:/config -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/raspberrypi3-homeassistant

Install gpiozero into the container
sudo docker exec -it homeassistant pip install gpiozero

run in container
sudo docker exec -it homeassistant /bin/bash

restart
sudo docker restart homeassistant


Clone this repo into it's config folder. /home/homeassistant/docker

Add a secrets.yaml file after cloning. Contains the login and email details for gmail and recipients
