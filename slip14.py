Slip14
Q1. Create simple application which shows life cycle of Activity.(use log)

Java file

package com.example.tybca;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.os.Bundle;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
String tag="Events";
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
Log.d(tag,"in on create event");
//Displaying Toast with Hello Javatpoint message
Toast.makeText(getApplicationContext(),"Hello TYBCA
Student",Toast.LENGTH_SHORT).show();
}
@Override
public void onStart() {
super.onStart();
Log.d(tag,"in on start event");
}
@Override
public void onStop() {
super.onStop();
Log.d(tag,"in on stop event");
}
@Override
protected void onResume() {
super.onResume();
Log.d(tag,"in on resume event");
}
@Override
public void onPause() {
super.onPause();
Log.d(tag,"in on pause event");
}
@Override
protected void onDestroy() {
super.onDestroy();
Log.d(tag,"in on Destroy event");
}
}

Q2 Create An android aaplication to send email
Xml file
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="10dp"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="To:"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
         android:id="@+id/edit_text_to"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textEmailAddress"/>


    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Subject:"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
        android:id="@+id/edit_text_subject"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textEmailSubject"/>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Message"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
        android:id="@+id/edit_text_message"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:lines="10"
        android:gravity="start|top"/>

    <Button
        android:id="@+id/button_send"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="send"/>




</LinearLayout>

Java file
package com.example.emailsendapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    private EditText mEditTextTo;
    private EditText mEditTextSubject;

    private  EditText mEditTextMessage;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mEditTextTo=findViewById(R.id.edit_text_to);
        mEditTextSubject=findViewById(R.id.edit_text_subject);
        mEditTextMessage=findViewById(R.id.edit_text_message);

        Button buttonSend = findViewById(R.id.button_send);

        buttonSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                sendMail();

            }
        });

    }
    private void sendMail(){
        String recipientList=mEditTextTo.getText().toString();
        String[] recipients =recipientList.split(",");
        //example@gmail.com, example2@gmail.com
        String subject =mEditTextSubject.getText().toString();
        String message =mEditTextMessage.getText().toString();

        //here now important part start here
        Intent intent =new Intent(Intent.ACTION_SEND);
        intent.putExtra(Intent.EXTRA_EMAIL,recipients);
        intent.putExtra(Intent.EXTRA_SUBJECT,subject);
        intent.putExtra(Intent.EXTRA_TEXT,message);
        //here email client
        intent.setType("message/rfc822");
        startActivity(Intent.createChooser(intent,"Choose an email client"));

        //this below part for attachment

       // Uri attachmentUri = Uri.parse("file:///storage/emulated/0/Download/myfile.pdf");
       // intent.putExtra(Intent.EXTRA_STREAM, attachmentUri);

        //startActivity(Intent.createChooser(intent, "Send email..."));
    }
}






