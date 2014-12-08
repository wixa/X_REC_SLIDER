#include <AccelStepper.h>
#define enablerun 4                    //4 пин - пин активизации двигателя перемащения
#define enablerotate 8                 //8 пин - пин активизации двигателя поворота
#define step_mode 5                    //5 пин - пин выбора режима шага
#define limit_switch 9                 //9 пин - пин концевика

AccelStepper bogie_run(1,2,3);         //1-режим биполярного шаговового двигателя, 2ой пин - шаг, 3ий пин - направление;(движение каретки) 
AccelStepper rotate_run(1,6,7);        //1-режим биполярного шаговового двигателя, 6ый пин - шаг, 7ой пин - направление;(поворот каретки)

boolean initdone = false;              //переменная выполненния инициализации(присваевается внутри программы)
boolean direct;                        //переменная направления езды каретки(приходит от пользователя) имеет два режима (false или true), если false - каретка едет с права на лево, если true - слева на право
int runspeed;                          //переменная скорости езды каретки(приходит от пользователя) колеблится от 0 до 2500 шагов в сек
int rotatespeed;                       //переменная скорости поворота каретки(вычесляется взависимости от runspeed, moveto и rotatesteps)
boolean stepmode;                          //переменная режима делителя шагов драйвера(приходит от пользователя) может быть либо false - полношаговый режим (200 шагов на оборот вала), если true - то микрошаговый 1/16 (200*16=3200 шагов на оборот)
int accel;                             //переменная ускорения (приходит от пользователя) может быть от 0 до 1000 шагов в сек(приходит от пользователя)
long rotatesteps;                      //переменная количества шагов поворота каретки(приходит от пользователя) в микрошагах с делителем 1/32 
long moveto;                           //переменная количества шагов езды каретки. Зависит от длины слайдера (приходит от пользователя), в полных шагах
String incomingstring;                 //переменная строки приемы данных(приходит от пользователя)
boolean change;                        //переменная изменения инициализации (если true разрешается выполнить повторную инициализацию)(приходит от пользователя)
//функция движения или движения и поворота каретки возвращет true если выполнилась успешно, возвращает false если произошел сбой
//функция инициализации. Возвращет true если выполнилась успешно, возвращает false если произошел сбой
boolean FULLSTEP_MODE(boolean);         //функция активизации полношагового режима True - полношаговый режим, если False - микрошаговый режим
char message[8]={'s','m','a','d','r','t','c','\0'};//масив символов для четения сообщении и разбивания его на переменные

//--------------------------------------------------------------------------------------------------------------------------------------------------------------
void setup()
{
 pinMode(enablerun, OUTPUT);           //настраиваем пин активизации двигателя перемещения на выход 
 pinMode(enablerotate, OUTPUT);        //настраиваем пин активизации двигателя поворота на выход
 pinMode(step_mode, OUTPUT);           //настраиваем пин выбора режимашага на выход. Этим пином будем задавать режим драйвера двигателя перемещения
 pinMode(limit_switch, INPUT);         //настраиваем пин концевика на вход. Этим пином будем считывать состояние концевика
 bogie_run.setEnablePin (enablerun);   //задаем Enable пин двигателя перемещения 4ому пину
 rotate_run.setEnablePin(enablerotate);//задаем Enable пин двигателя поворота 8ому пину
 bogie_run.setPinsInverted(false,false,true); //инвентируем Enable так как в драйвере DRV8825 он инвентирован
 rotate_run.setPinsInverted(false,false,true);//инвентируем Enable так как в драйвере DRV8825 он инвентирован
 bogie_run.enableOutputs();            //активизируем двигатель перемещения каретки
 rotate_run.enableOutputs();           //активизируем двигатель поворота каретки
 interrupts();                         //разрешаем прерывания глобально 
 Serial.begin(9600);                   //стартуем COM соеденение со скоростью 9600
 Serial1.begin(9600);                  //стартуем COM1 через TTL USB для отладки
}
//--------------------------------------------------------------------------------------------------------------------------------------------------------------
boolean FULLSTEP_MODE(boolean)                 //функция активизации полношагового режима True - полношаговый режим, если False - микрошаговый режим 
{
if (true)
  digitalWrite (step_mode,HIGH);
if (false) 
  digitalWrite (step_mode,LOW);
}
//--------------------------------------------------------------------------------------------------------------------------------------------------------------
boolean initialization(boolean,long)   //функция инициализации, передвигает каретку на точку старта, в зависимости от direct каретка будет 
{                                      //стартовать либо с правой либо слевой стороны слайдера
 bogie_run.setAcceleration(500);       //задаемся оптимальным ускорением 
 bogie_run.setMaxSpeed(2000);          //задаемся оптимальной скоростю для быстрого перемещения каретки
 bogie_run.moveTo(-moveto);            //задаемся количеством полных шагов - означает что будем двигатся к правой стороне, на двигатель
 bogie_run.setCurrentPosition(0);      //задаем текущее положение каретки как 0 шаг
 FULLSTEP_MODE(true);                  //включаем полношаговый режим
 while (digitalRead(limit_switch)!=HIGH || bogie_run.currentPosition()!=moveto) //едем в сторону двигателя пока не сработает концевик 
    bogie_run.run();                   // либо пока не приедем на последний шаг слайдера(полная длина слайдера в полных шагах)
 if (direct == true)                   //если пользователем заданно что слайдер будет ехать с левой стороны, т.е. на двигатель, то
 {                                     //едем от концевика на другой край слайдера
  bogie_run.moveTo(moveto);
  while (bogie_run.currentPosition()!=moveto)
    bogie_run.run();
  bogie_run.setCurrentPosition(0);
  moveto=-moveto;                      //зададим отрицательное значение полным шагам длины слайдера, для того что бы ехать на двигатель 
  Serial1.println("Bogie will be run from left side");//с лева на право
  return true;
 }
 else if (direct==false)               //если пользователем заданно что слайдер будет ехать с правой стороны, т.е. от двигатель, то                                
 {                                     //остаемся на месте
   Serial1.println("Bogie will be run from right side");
   return true;
 }
 else                                  //если в переменно направления не булеан значение, выводим в отладочный порт ошибку
 {
  Serial1.print ("Unexpected error, direction= ");
  Serial1.print (direct);
  Serial1.println (". This is bad range it must be 0 or 1");
  return false;
 }
}
//-------------------------------------------------------------------------------------------------------------------------------------------------------------- 
boolean run_video_mode(int, int, long, boolean, boolean, long)          //функция движения или движения и поворота каретки возвращет true если 
{                                                                       //выполнилась успешно, возвращает false если произошел сбой
 if (direct==true)                                                      //если будем ехать с лева на право, 
 {                                                                      //то каретка будет крутится против часовой стрелки
   rotatesteps=-rotatesteps;                                            //если с права на лево то каретка будет крутится по 
   Serial1.println("ROTATESTEPS= "+ rotatesteps);                       //по часовой стрелке
   delay(20);
 }
 if (stepmode==false)
 {
   FULLSTEP_MODE(true);                                                 //проверяем режи езды каретки, если режим полношаговый
   Serial1.println("FULLSTEP MODE MOVETO= "+moveto);                    //включаем на драйвере полношаговый режим 
   delay(20);                                                           //если выбран режим микрошагового режима, то
 }                                                                      //включаем на драйвере микрошаговый режим
 if (stepmode==true)                                                    //и умножаем количество шагов езды на делитель дайвера.
 {                                                                      // в данном случае это 16
   FULLSTEP_MODE(false);                                                // режим выберается в гуи атвоматически, если время заданно 
   moveto = moveto * 16;                                                //от 1 минуты до 14 минут выберается полношаговый режим
   Serial1.println("MICROSTEP MODE MOVETO= "+moveto);                   //если от 14 минут до 24 часов, то выберается микрошаговый режим
   delay(20);
 }
 if (rotatesteps > 0)                                                   //проверяем было ли задано в гуи режим езды и поворота
 {                                                                      //если да, то вычесляем скорость поворота
 rotatespeed=(rotatesteps*runspeed)/moveto;                             //она зависит от длины слайдера и угла поворота(а угол от растояния до обьекта)
 rotate_run.moveTo(rotatesteps);                                        // задаем параметры в обьект класа который отвечает за кручение
 rotate_run.setSpeed(rotatespeed);                                      
 rotate_run.setCurrentPosition(0);                                      //задаем начальную точку кручения текущей
 Serial1.println("BOGIE WILL BE RUN AND ROTATE");                       //это нужно что пользвователь руками выставил камеру на обьект
 delay(20);
 }
 Serial1.println("BOGIE WILL BE ONLY RUN");
 delay(20);
 while(bogie_run.currentPosition()!=moveto)                             //начинаем движение каретки в цикле, пока текущая позиция каретки не будет конечной
 {                                                                      //крутим и едем пока не достигнем конечной точки
   bogie_run.run();     
   rotate_run.runSpeedToPosition();
 }
 }
//--------------------------------------------------------------------------------------------------------------------------------------------------------------
void loop()
{
  if (change==true)
  {
    initdone=false;
    change=false;
  }
  if (initdone==false)
    initdone=initialization(direct,moveto);
  if (initdone==true && runspeed > 0 && accel > 0)
  {
    run_video_mode(runspeed, accel, moveto, stepmode, direct, rotatesteps);
    initdone=false;
    runspeed=0;
    stepmode=false;
    accel=0;
    direct=false;
    rotatespeed=0;
    moveto=0;
    change=false;
  }
}
//--------------------------------------------------------------------------------------------------------------------------------------------------------------
void serialEnableRun()
{
 int i;
 String substring[8]={"runspeed","stepmode","accel","direct","rotatesteps","moveto","change"}; //локальные переменные для принятия строки (s- runspeed, m- stepmode, a- accel, d- direct, r- rotatesteps, t- moveto, c- change)
 String mainstring[8];
 int first, last;                                                      //локальные переменные для определения индекса первого и последнего символа в строке
 while (Serial.available())                                            //пока открыто соеденение
  {
    incomingstring +=(char)(Serial.read());                            //вычитываем сообщение посимвольно и записываем в одну строку 
  }
 for (i=0; 7; i++)                                                     //в цикле выбераем по символам значения переменных и укладываем их поочереди в пустой массив
 {
   first=0;
   last=0;
   first = incomingstring.indexOf(message[i])+1;
   last = incomingstring.indexOf(message[i],first);
   if (first==0)                                                       //проверяем если в строке небыло символа, то ложим в масив пустое значение переменной
     mainstring[i]="";
   else 
     mainstring[i]=incomingstring.substring(first,last);
   Serial1.println(substring[i]+"= "+mainstring[i]);                  //ввыводим по ячейке значения переменных
 }
   runspeed=mainstring[0].toInt();                                    //преобразовываем строковые значения в нужный нам тип, и присваиваем их глобальным переменным
   Serial1.println(runspeed);
   delay (20);
   stepmode=mainstring[1].toInt();
   Serial1.println(stepmode);
   delay (20);
   accel=mainstring[2].toInt();
   Serial1.println(accel);
   delay (20);
   direct=mainstring[3].toInt();
   Serial1.println(direct);
   delay (20);
   char charBuf[7];
   mainstring[4].toCharArray(charBuf, 7);
   rotatesteps=atol(charBuf);
   Serial1.println(rotatesteps);
   delay (20);
   charBuf[7];
   mainstring[5].toCharArray(charBuf, 7);
   moveto=atol(charBuf);
   Serial1.println(moveto);
   delay (20);
   change=mainstring[6].toInt();
   Serial1.println(change);
   delay (20);
}
//--------------------------------------------------------------------------------------------------------------------------------------------------------------    
