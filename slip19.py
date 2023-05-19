Slip19
Q1.Create an android application that on/off the bulb using Toggle Button
Xml file
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <ToggleButton
        android:id="@+id/toggle_button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"/>
</LinearLayout>

Java file
package com.example.slip19bulbonoffapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import android.widget.ToggleButton;

public class MainActivity extends AppCompatActivity {
    ToggleButton toggleButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        toggleButton=(ToggleButton)findViewById(R.id.toggle_button);
        toggleButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(((ToggleButton)view).isChecked()){
                    Toast.makeText(MainActivity.this, "Bulb is on", Toast.LENGTH_SHORT).show();
                }else {
                    Toast.makeText(MainActivity.this, "Bilb is off", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
Q2).Create application to send SMS message. After sending message display delivery report of message.
Xml file
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayoutxmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<TextView
android:id="@+id/textView1"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_alignParentTop="true"
android:layout_centerHorizontal="true"
android:textSize="30dp" />

<TextView
android:id="@+id/textView2"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:textSize="30dp"
android:layout_below="@+id/textView1" />


<EditText
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:id="@+id/editText"
android:hint="Enter Phone Number"
android:layout_centerHorizontal="true" />

<EditText
android:id="@+id/editText2"
android:layout_width="wrap_content"
android:layout_height="wrap_content"

android:layout_below="@+id/editText"
android:layout_centerHorizontal="true"
android:hint="Enter SMS" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Send Sms"
android:id="@+id/btnSendSMS"
android:layout_below="@+id/editText2"
android:layout_centerHorizontal="true"
android:layout_marginTop="48dp" />

</RelativeLayout>

Main.java
public class MainActivityextends AppCompatActivity{

private static final int MY_PERMISSIONS_REQUEST_SEND_MSG = 0;
Button sendBtn;
EditTexttxtphoneNo;
EditTexttxtMessage;
String phoneNo;
String message;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

sendBtn= (Button) findViewById(R.id.btnSendSMS);
txtphoneNo= (EditText) findViewById(R.id.editText);
txtMessage= (EditText) findViewById(R.id.editText2);

sendBtn.setOnClickListener(new View.OnClickListener() {
public void onClick(View view) {
sendSMSMessage();
            }
        });
    }

protected void sendSMSMessage() {
phoneNo= txtphoneNo.getText().toString();
message = txtMessage.getText().toString();

if (ContextCompat.checkSelfPermission(this,
SEND_MSG)
                != PackageManager.PERMISSION_GRANTED) {
if (ActivityCompat.shouldShowRequestPermissionRationale(this,
SEND_MSG)) {
            } else {
ActivityCompat.requestPermissions(this,
new String[]{Manifest.permission.SEND_MSG},
MY_PERMISSIONS_REQUEST_SEND_MSG);
            }
        }
    }


@Override
public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {
super.onRequestPermissionsResult(requestCode, permissions, grantResults);
switch (requestCode) {
case MY_PERMISSIONS_REQUEST_SEND_MSG: {
if (grantResults.length>0
&&grantResults[0] == PackageManager.PERMISSION_GRANTED) {
SmsManagersmsManager= SmsManager.getDefault();
smsManager.sendTextMessage(phoneNo, null, message, null, null);
Toast.makeText(getApplicationContext(), "SMS sent.",
Toast.LENGTH_LONG).show();
                } else {
Toast.makeText(getApplicationContext(),
"SMS faild, please try again.", Toast.LENGTH_LONG).show();
return;
                }
            }
        }

    }

private class SEND_MSG {
    }
}

manefiest file.xml

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools">
<uses-permission android:name="android.permission.SEND_MSG" />

<application

android:allowBackup="true"
android:dataExtractionRules="@xml/data_extraction_rules"
android:fullBackupContent="@xml/backup_rules"
android:icon="@mipmap/ic_launcher"
android:label="@string/app_name"
android:supportsRtl="true"
android:theme="@style/Theme.Slip19_2"
tools:targetApi="31">


<activity
android:name=".MainActivity"
android:exported="true">
<intent-filter>
<action android:name="android.intent.action.MAIN" />

<category android:name="android.intent.category.LAUNCHER" />
</intent-filter>

</activity>

</application>
</manifest>


