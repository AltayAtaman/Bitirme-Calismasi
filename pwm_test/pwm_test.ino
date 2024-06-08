const int pwmPin1 = 9; // D9 Pini
const int pwmPin2 = 10; // D10 Pini

void setup() {
  Serial.begin(9600);
  pinMode(pwmPin, OUTPUT);
  pinMode(pwmPin2, OUTPUT);
}

void loop() {
  analogWrite(pwmPin1, 50); 
  analogWrite(pwmPin2, 0);  
  delay(2000);               

  analogWrite(pwmPin1, 100); 
  analogWrite(pwmPin2, 0);  
  delay(2000);               

  analogWrite(pwmPin1, 150); 
  analogWrite(pwmPin2, 0);  
  delay(2000);               

  analogWrite(pwmPin1, 100); 
  analogWrite(pwmPin2, 0);  
  delay(2000);            

  analogWrite(pwmPin1, 50); 
  analogWrite(pwmPin2, 0);  
  delay(2000);               

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 0);  
  delay(2000);          

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 50);  
  delay(2000);          

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 100);  
  delay(2000);               

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 150);  
  delay(2000);               

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 50);  
  delay(2000);

  analogWrite(pwmPin1, 0); 
  analogWrite(pwmPin2, 0);  
  delay(2000);               
}
