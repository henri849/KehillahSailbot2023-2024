//pins
#define DT  2
#define CLK  3
#define RLY 12
#define KB A0

//Controler:
volatile int t_speed = 20;
//Feeback and error evaluation:
volatile long pos=0; //volatile as it will be changing very quickly and often
long oldposition = 0;
unsigned long newtime;
unsigned long oldtime = 0;
int p_e = 0; // previous error
void setup(){
  pinMode(DT, INPUT); //set the input pins to digital inputs
  pinMode(CLK, INPUT);
  digitalWrite(DT, HIGH);digitalWrite(CLK, HIGH); //turn on pullup resistor to ensure a known states for all these inputs
  pinMode(RLY, OUTPUT); //set the relay signal pin to a digital output
  attachInterrupt(digitalPinToInterrupt(DT), encode, RISING);//run encode every time DT rises
  Serial.begin(9600);
}

void loop(){
  //read knob and set speed
  t_speed = map(analogRead(KB),0,660,0,100);//read the knob and set t_speed to a number between 0-100 maping to 0-360 degrees of rotation

  //calculate error
  newtime = millis();
  double rot = (double)(pos-oldposition)/20;//20 pulses per rotation so this is a fraction representing the number of turns
  double dt = (double)(newtime-oldtime)/1000 //change in time in seconds
  double speed = abs(rot/dt)); //rotations/dt so rotations per second
  int e = t_speed - speed;//error is the difference between desired speed and current speed

  //controler
  int u = map(e+ (e-p_e),-70,70,-1000,1000);// the negatives are just cut off but they are nesseary to the maping
  if (newtime%1000<u){
    digitalWrite(12,HIGH);// motor accelerates
  }else{
    digitalWrite(12,LOW);
  }

  //outputing and updating variables
  if (newtime %1000 < oldtime%1000){ //print only when the second changes
    Serial.print("speed = ");
    Serial.println(speed);
  }
  oldposition = pos;
  oldtime = newtime;
  p_e = e;//previous error = current error, this permits the derivative and integral term for the PID loop
  delay(20);
}

void encode(){
  if (digitalRead(DT) == digitalRead(CLK)) {//if there is a pulse, record it
    pos++;
  } else {
    pos--;
  }
}
