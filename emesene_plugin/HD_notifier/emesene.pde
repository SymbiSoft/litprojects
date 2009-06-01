#include <Metro.h>
/*
 * Button
 * by DojoDave <http://www.0j0.org>
 *
 * Turns on and off a light emitting diode(LED) connected to digital  
 * pin 13, when pressing a pushbutton attached to pin 7. 
 *
 * http://www.arduino.cc/en/Tutorial/Button
 */

int ledPinG =5; //green LED pin (blink)
int ledPinY = 11; //yellow LED pin (busy - free)
int mac = 17;// transistor pin
int stop = 2;// stop blinking button pin
int away = 4;// busy-free button pin
int buzzerPin = 9; //buzzer pin (pwm)


boolean blink = 0;  //incoming message
boolean buzzer = 0; //buzzer on-off
boolean awayer = 0; //busy-free status


int value = LOW;
long time = 0;         // the last time the output pin was toggled
long debounce = 1000;   // the debounce time, increase if the output flickers
int val = 0;                    // variable for reading the pin status
long previousMillis = 0;        // will store last time LED was updated
long prevMillisB = 0;          // will store last time LED was updated
long intervalB = 1000;         //interval

Metro led_blink = Metro(1000);


void setup() {
  pinMode(ledPinG, OUTPUT);      // declare LED as output
  pinMode(ledPinY, OUTPUT);      // declare LED as output
  pinMode(stop, INPUT);     // declare pushbutton as input
  pinMode(away, INPUT);     // declare pushbutton as input
  pinMode(mac, OUTPUT);
  Serial.begin(9600);


}

void loop(){
  val = digitalRead(stop);  // read input value
  if (val == HIGH && blink == 1) { 
    blink = 0;
    buzzer = 0;
    digitalWrite(ledPinG, LOW); // turn off blinking
    digitalWrite(mac, LOW); // turn off transistor
    analogWrite(buzzerPin,0);  // turn off buzzer
  }
  val = digitalRead(away);
  if (val == HIGH  && millis() - time > debounce){
    if (awayer==0 )
      awayer=1;
    else
      awayer=0;

    time=millis();
  }


  if (blink){
    if (led_blink.check()){
      digitalWrite(ledPinG,!digitalRead(ledPinG));
    }
  }

  if (millis()<time +debounce)
    if (awayer)
      Serial.print("B");
    else
      Serial.print("F");



  if (buzzer){
    if (millis() - prevMillisB > intervalB && millis() - prevMillisB < intervalB*2)
      analogWrite(buzzerPin,0);  // turn off buzzer
    if (millis() - prevMillisB > intervalB*2 && millis() - prevMillisB < intervalB*3)
      analogWrite(buzzerPin,200);
    if (millis() - prevMillisB > intervalB*3)
      analogWrite(buzzerPin,0);        
    if (millis() > prevMillisB + 121000){
      prevMillisB = millis();  
      analogWrite(buzzerPin,128);
    }
  }
  if (Serial.available()>0) {
    val = Serial.read();

    if (val == 'H' && blink == 0) {
      blink = 1;
      led_blink.reset();
      digitalWrite(ledPinG,HIGH);
      if (!awayer){
        prevMillisB=millis();
        analogWrite(buzzerPin,128);
        buzzer = 1;
      }
      else{
        digitalWrite(mac,HIGH);
        Serial.println("mac");
      }
    }
    else if (val=='B'){
      awayer=1;
      Serial.println("busy");
    }
    else if (val=='F'){
      Serial.println("free");
      awayer=0;
    }
  }
  digitalWrite(ledPinY,awayer);

}
