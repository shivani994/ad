slip7
Q1. Create an Android Application That Demostrate Radio Button

Xml file

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="100dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Select your gender:"/>

        <RadioGroup
            android:id="@+id/rg"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal">
            <RadioButton
                android:id="@+id/rb1"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="male"/>

            <RadioButton
                android:id="@+id/rb2"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="femal"/>
     </RadioGroup>
        <Button
            android:id="@+id/button"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="submit"/>
        </LinearLayout>

</LinearLayout>

javaFile

package com.example.radiobuttonslip7application;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private RadioGroup radioGroupGender;
    private RadioButton radioButtonSelected;
    private Button buttonSubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        radioGroupGender=findViewById(R.id.rg);
        buttonSubmit=findViewById(R.id.button);

        buttonSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                 int selectedId=radioGroupGender.getCheckedRadioButtonId();  // this  method used to return which  id selected h
                 //here we check
                if(selectedId==-1){
                    Toast.makeText(MainActivity.this, "please select your gender", Toast.LENGTH_SHORT).show();
                }
                else {
                    radioButtonSelected=findViewById(selectedId);
                    String selectedGender=radioButtonSelected.getText().toString();
                    Toast.makeText(MainActivity.this, "your gender is"+selectedGender, Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
}



Q2 Create an Android Application to Demostrate phone call using implicit Intent

Xml file
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:layout_gravity="center"
    tools:context=".MainActivity">
    <EditText
        android:id="@+id/edit_phone"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Phone Number"
        android:layout_marginLeft="30dp"
        android:layout_marginRight="30dp"
        android:inputType="number"
        android:gravity="center" />


    <Button
        android:id="@+id/btn_Dial"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Call"
        android:backgroundTint="#DEDBDB"
        android:layout_marginLeft="50dp"
        android:layout_marginRight="50dp"
        android:layout_marginTop="20dp"
        android:layout_gravity="center"/>



</LinearLayout>

Java file 

package com.example.phonecallslip7application;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    Button btnDial;
    EditText edtPhone;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        edtPhone=findViewById(R.id.edit_phone);
        btnDial=findViewById(R.id. btn_Dial);
        btnDial.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String phoneNumber =edtPhone.getText().toString();
                Intent iDial= new Intent(Intent.ACTION_DIAL,Uri.fromParts("tel",phoneNumber,null));
                startActivity(iDial);

            }
        });
    }
}

