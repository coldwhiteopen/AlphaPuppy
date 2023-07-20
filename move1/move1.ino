#include <Servo.h>

Servo mys1,mys2,mys3;
int angleA = 90;
int angleB = 0;
int angleC = 0;

String comdata = "";
int flag = 1;

void Mys_123(int angle1,int angle2,int angle3,int t);

void setup(void){
  Serial.begin(9600);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  mys1.attach(7);
  mys2.attach(6);
  mys3.attach(5);
  // mys1.write(90);
  // mys2.write(90);
  // mys3.write(75);
}

void loop() {
  // while (Serial.available() > 0){
  //   comdata += char(Serial.read());
  //   delay(2);
  // }
  // if (comdata.length() > 0){
  //   data=comdata.toInt();
  //   //Serial.println(c);
  //   comdata = ""; 
  // }
  //范围
  // Mys_123(0,60,50,15);
  // Mys_123(180,160,110,15);
  // delay(5000);
  if(flag==1){
    Mys_123(180,90,40,15);
    chessUp();
    delay(2000);
    Mys_123(180,70,110,15);
    Mys_123(80,90,65,15);
    delay(500);
    //1hao
    Mys_123(67,135,60,30);
    //2hao
    //Mys_123(68,121,48,15);
    //3hao
    //Mys_123(83,135,60,15);
    //4hao
    //Mys_123(73,125,55,15);
    //5hao
    //Mys_123(60,110,40,30);
    //6hao
    //Mys_123(92,132,50,30);
    //7hao
    //Mys_123(85,160,70,15);
    //8hao
    //Mys_123(85,125,45,15);
    //9hao
    //Mys_123(93,115,35,30);
    //10hao
    //Mys_123(70,150,70,30);
    //11hao
    //Mys_123(105,105,35,30);
    chessDown();
    delay(2500);
    Mys_123(80,90,65,15);
    flag++;
  }
  // if(flag == 1){
  //   chessUp();
  //   flag++;
  //}
  
  //delay(2000);
  //chessDown();
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
