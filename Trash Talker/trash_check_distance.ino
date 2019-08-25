/*

 * ---------------------    ---------------------
 * | HC-SC04 | Arduino |    | 3 pins  | Arduino |
 * ---------------------    ---------------------
 * |   Vcc   |   5V    |    |   Vcc   |   5V    |
 * |   Trig  |   12    | OR |   SIG   |   13    |
 * |   Echo  |   13    |    |   Gnd   |   GND   |
 * |   Gnd   |   GND   |    ---------------------
 * ---------------------
 * 
 * By default, the distance returned by the distanceRead()
 * method is in centimeters, to get the distance in inches,
 * pass INC as a parameter.
 * Example: ultrasonic.distanceRead(INC)
 */

#include <Ultrasonic.h>

/*
 * Pass as a parameter the trigger and echo pin, respectively,
 * or only the signal pin (for sensors 3 pins), like:
 * Ultrasonic ultrasonic(13);
 */
Ultrasonic ultrasonic(12, 13);

void setup() {
  Serial.begin(9600);
  
  }

void loop() {

  Serial.println(ultrasonic.distanceRead());
  delay(1000);
}