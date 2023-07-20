#include <Servo.h>

Servo mys1,mys2,mys3;

int flag = 1;
int dt = 5000;

void Mys_123(int angle1,int angle2,int angle3,int t);

void setup(void){
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  mys1.attach(7);
  mys2.attach(6);
  mys3.attach(5);
}

void loop() {
  if(flag==1){
    // one();
    // delay(dt);
    // two();
    // delay(dt);
    // three();
    // delay(dt);
    // four();
    // delay(dt);
    // five();
    // delay(dt);
    // six();
    // delay(dt);
    // seven();
    // delay(dt);
    // eight();
    // delay(dt);
    // nine();
    // delay(dt);
    // ten();
    delay(dt);
    eleven();
    flag++;
  }
}

void Mys_123(int angle1,int angle2,int angle3,int t){      //控制机械臂的3个舵机，编号1、2、3
  double ang1=mys1.read();double ang2=mys2.read();double ang3=mys3.read();
  double cha[3];
  cha[0]=angle1-ang1;cha[1]=angle2-ang2;cha[2]=angle3-ang3;
  for(int i=0;i<3;i++){if(cha[i]<0){cha[i]=-cha[i];}}
  double chaMax=0;
  for(int i=0;i<3;i++){if(chaMax<cha[i]){chaMax=cha[i];}}
  while(1){
    if(mys1.read()==angle1 && mys2.read()==angle2 && mys3.read()==angle3){break;}    
    if(mys1.read()>angle1)     {ang1-=(cha[0]/chaMax);mys1.write(int(ang1));}
    else if(mys1.read()<angle1){ang1+=(cha[0]/chaMax);mys1.write(int(ang1));}
    if(mys2.read()>angle2)     {ang2-=(cha[1]/chaMax);mys2.write(int(ang2));}
    else if(mys2.read()<angle2){ang2+=(cha[1]/chaMax);mys2.write(int(ang2));}
    if(mys3.read()>angle3)     {ang3-=(cha[2]/chaMax);mys3.write(int(ang3));}
    else if(mys3.read()<angle3){ang3+=(cha[2]/chaMax);mys3.write(int(ang3));}
    delay(t);
  }
}
void chessDown(){
  digitalWrite(9, LOW);  // 控制继电器打开
}
void chessUp(){
  digitalWrite(9, HIGH);  // 控制继电器打开
}
void one(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //1hao
  Mys_123(65,135,60,30);

  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void two(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //2hao
  Mys_123(68,121,48,30);

  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void three(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //3hao
  Mys_123(83,135,60,30);

  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void four(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //4hao
  Mys_123(73,125,55,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void five(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //5hao
  Mys_123(60,110,40,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void six(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //6hao
  Mys_123(92,132,50,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void seven(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //7hao
  Mys_123(85,150,70,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void eight(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //8hao
  Mys_123(85,115,45,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void nine(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //9hao
  Mys_123(93,115,35,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void ten(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //10hao
  Mys_123(68,150,80,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}

void eleven(){
  Mys_123(180,90,40,15);
  chessUp();
  delay(2000);
  Mys_123(180,70,110,15);
  Mys_123(80,90,65,15);
  delay(500);

  //11hao
  Mys_123(105,95,35,30);
  
  chessDown();
  delay(2500);
  Mys_123(80,90,65,15);
  Mys_123(180,90,40,15);
}