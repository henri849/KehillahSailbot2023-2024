//pins
#define DT  2
#define CLK  3
#define RLY 12
#define KB A0

//Controler
volatile int t_speed = 20;
//Feeback and error evaluation
volatile long pos=0; //volatile as it will be changing very quickly and often
long oldposition = 0;
unsigned long newtime;
unsigned long oldtime = 0;
int p_e = 0; // previous error
void setup()
{
  pinMode(DT, INPUT);digitalWrite(DT, HIGH);       // Set up Dt and turn on pullup resistor
  pinMode(CLK, INPUT);digitalWrite(CLK, HIGH);       // Set up CLK and turn on pullup resistor
  pinMode(RLY, OUTPUT); //relay
  attachInterrupt(digitalPinToInterrupt(DT), encode, RISING);//run encode every time DT rises
  Serial.begin(9600);
}

void loop(){
  //read knob and set speed
  t_speed = map(analogRead(KB),0,660,0,100);

  //calculate error
  newtime = millis();
  double speed = abs((double)(pos-oldposition)/20*1000/((newtime-oldtime)));
  int e = t_speed - speed;

  //controler
  int u = map(e+ (e-p_e),-70,70,-1000,1000);// the negatives are just cut off but they are nesseary to the maping
  if (newtime%1000<u){
    digitalWrite(12,HIGH);
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

void encode()
{
  if (digitalRead(DT) == digitalRead(CLK)) {
    pos++;
  } else {
    pos--;
  }
}