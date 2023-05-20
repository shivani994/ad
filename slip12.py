Slip 12
Q1 create a simple application which sends –hii message from one activity to another with help of button
Xml file 1
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

android:inputType="text"/>

<Button

android:id="@+id/btn"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:text="Click here"

android:layout_gravity="center"

android:layout_marginTop="16dp"/>









</LinearLayout>

Java file1

package com.example.slip12hillapplication;



import androidx.appcompat.app.AppCompatActivity;



import android.content.Intent;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.EditText;

import android.widget.TextView;



import java.time.temporal.ValueRange;



public class MainActivityextends AppCompatActivity{

private static  Stringvalue;

public static String getValue(){

return value;

    }



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);

final EditTextedittext= (EditText)findViewById(R.id.edit_text);

Button button= (Button)findViewById(R.id.btn);

button.setOnClickListener(new View.OnClickListener() {

@Override

public void onClick(View view) {

value = edittext.getText().toString().trim();

Intent intent=new Intent(MainActivity.this,SecondActivity.class);

startActivity(intent);

            }

        });



    }

}

xml file 2

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

tools:context=".SecondActivity">

<TextView

android:id="@+id/text_view"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:layout_gravity="center"/>



</LinearLayout>

Java file2

package com.example.slip12hillapplication;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
public class SecondActivityextends AppCompatActivity{

@Override

protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_second);
TextViewtextView=findViewById(R.id.text_view);
textView.setText(MainActivity.getValue());

    }

}


Q2) Create a custom "Contact" layout to hold multiple pieces of information, including: Photo, Name, Contact Number, E-mail id.

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity">



<ImageView

android:id="@+id/contact_photo"

android:layout_width="120dp"

android:layout_height="120dp"

android:src="drawable/img.png"

android:scaleType="centerCrop"

android:padding="16dp"

android:layout_gravity="center_horizontal"

android:contentDescription="@string/todo">



</ImageView>



<TextView

android:id="@+id/contact_name"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:textSize="24sp"

android:textStyle="bold"

android:textColor="@color/black"

android:layout_marginTop="16dp"

android:gravity="center_horizontal"

android:text="@string/full_name"/>



<TextView

android:id="@+id/contact_number"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:textSize="16sp"

android:textColor="@color/black"

android:layout_marginTop="8dp"

android:text="@string/contact_number"/>



<TextView

android:id="@+id/contact_email"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:textSize="16sp"

android:textColor="@color/black"

android:layout_marginTop="8dp"

android:text="@string/email_address"/>







</LinearLayout>
(adda image in drawable file)

Javafile
package com.example.slip12_2;



import androidx.appcompat.app.AppCompatActivity;



import android.graphics.Bitmap;

import android.os.Bundle;

import android.widget.ImageView;

import android.widget.TextView;



public class MainActivityextends AppCompatActivity{



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);



ImageView photo = findViewById(R.id.contact_photo);

TextView name = findViewById(R.id.contact_name);

TextView number = findViewById(R.id.contact_number);

TextView email = findViewById(R.id.contact_email);



// Retrieve contact information from a database or other source

String fullName= "John Doe";

String phoneNumber= "555-1234";

String emailAddress= "johndoe@example.com";

Object contactId;

contactId= null;

Bitmap photoBitmap= retrieveContactPhoto(this,contactId); // Retrieve photo as a Bitmap object



        // Display the contact information in the layout

photo.setImageBitmap(photoBitmap);

name.setText(fullName);

number.setText(phoneNumber);

email.setText(emailAddress);

    }



private Bitmap retrieveContactPhoto(MainActivitymainActivity, Object contactId) {

return null;

    }

}


