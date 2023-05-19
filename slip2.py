SLIP NO 2
Q1. Create a Simple Application, which reads a positive number from the user and display its factorial value in another activity.

xml file 1

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity">

<EditText

android:id="@+id/edit_text"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:layout_gravity="center"

android:layout_marginStart="50dp"

android:layout_marginEnd="50dp"

android:layout_marginTop="300dp"

android:hint="Enter any number"/>



<Button

android:id="@+id/btn_calculate"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:layout_marginStart="40dp"

android:layout_marginEnd="38dp"

android:layout_marginTop="30dp"

android:text="Calculate Factorial"/>









</LinearLayout>


Java file 1
package com.example.slip2factorialapplication;



import androidx.appcompat.app.AppCompatActivity;



import android.content.Intent;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.EditText;



public class MainActivityextends AppCompatActivity{

EditTexteditText;

Button btnCalculate;





@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);

editText=findViewById(R.id.edit_text);

btnCalculate=findViewById(R.id.btn_calculate);

btnCalculate.setOnClickListener(new View.OnClickListener() {

Bundle bundle=new Bundle();

@Override

public void onClick(View view) {

int user,fact=1 , i;

user= Integer.parseInt(editText.getText().toString());


for(i=1;i<=user;i++)

                 {

                     fact=fact*i;



                 }

bundle.putInt("key",fact);

Intent intent=new Intent(MainActivity.this,FactorialActivity.class);

intent.putExtras(bundle);



startActivity(intent);


            }

        });

    }

}

xml file2
<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

android:gravity="center"

tools:context=".FactorialActivity">

<TextView

android:id="@+id/text_view_result"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:gravity="center"

android:text=""/>



</LinearLayout>

Java file2

package com.example.slip2factorialapplication;



import androidx.appcompat.app.AppCompatActivity;



import android.content.Intent;

import android.os.Bundle;

import android.widget.TextView;



public class FactorialActivityextends AppCompatActivity{

TextViewtextView;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_factorial);

textView=(TextView) findViewById(R.id.text_view_result);

Intent intent= getIntent();

Bundle bundle= intent.getExtras();

int val=bundle.getInt("key");

String str=String.valueOf(val);

textView.setText(str);


    }

}


Question -2
XML file
<RelativeLayoutxmlns:android=http://schemas.android.com/apk/res/android
Xmlns:tools=http://schemas.android.com/tools
Android:layout_width=”match_parent”
Android:layout_height=”match_parent”
Android:paddingLeft=”16dp”
Android:paddingTop=”16dp”
Android:paddingRight=”16dp”
Android:paddingBottom=”16dp”
Tools:context=”.MainActivity”>

<Button
Android:id=”@+id/startButton”
Android:layout_width=”wrap_content”
Android:layout_height=”wrap_content”
Android:text=”Start”
Android:layout_centerInParent=”true” />

<Button
Android:id=”@+id/stopButton”
Android:layout_width=”wrap_content”
Android:layout_height=”wrap_content”
Android:text=”Stop”
Android:layout_below=”@id/startButton”
Android:layout_centerHorizontal=”true” />

</RelativeLayout>

Java file
Import android.content.Intent;
Import android.os.Bundle;
Import android.view.View;
Import android.widget.Button;

Import androidx.appcompat.app.AppCompatActivity;

Public class MainActivity extends AppCompatActivity {
    Private Button startButton, stopButton;
    Private Intent serviceIntent;

    @Override
    Protected void onCreate(Bundle savedInstanceState) {
Super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

startButton = findViewById(R.id.startButton);
stopButton = findViewById(R.id.stopButton);

serviceIntent = new Intent(this, AudioService.class);

startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            Public void onClick(View v) {
startService(serviceIntent);
            }
        });

stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            Public void onClick(View v) {
stopService(serviceIntent);
            }
        });
    }
}

Audio.java file
Import android.app.Service;
Import android.content.Intent;
Import android.media.MediaPlayer;
Import android.os.IBinder;

Import androidx.annotation.Nullable;

Public class AudioService extends Service {
    Private MediaPlayermediaPlayer;

    @Override
    Public void onCreate() {
Super.onCreate();
mediaPlayer = MediaPlayer.create(this, R.raw.your_audio_file);
mediaPlayer.setLooping(true); // To play audio in a loop
    }

    @Override
    Public int onStartCommand(Intent intent, int flags, int startId) {
mediaPlayer.start();
        return START_STICKY;
    }

    @Override
    Public void onDestroy() {
Super.onDestroy();
mediaPlayer.stop();
mediaPlayer.release();
    }

    @Nullable
    @Override
    Public IBinderonBind(Intent intent) {
        Return null;
    }
}

Manifest file
<manifest xmlns:android=http://schemas.android.com/apk/res/android
    Package=”com.example.audioplayer”>

<uses-permission android:name=”android.permission.FOREGROUND_SERVICE” />

<application
        …>

<service android:name=”.AudioService” />

<activity
Android:name=”.MainActivity”
            …>
            …
</activity>
</application>
</manifest



