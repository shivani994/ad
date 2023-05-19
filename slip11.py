slip11
Q1.Create android application to change Font Size, Color and Font Family of String

Neha
Xml file

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:layout_alignParentEnd="true"
android:layout_alignParentStart="true"
tools:context=".MainActivity"
android:layout_alignParentRight="true"
android:layout_alignParentLeft="true">

<TextView
android:id="@+id/myTextView"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Hello World!"
android:textSize="20sp"
android:textColor="#000000"
android:typeface="sans"
android:layout_centerInParent="true"/>

<Button
android:id="@+id/increaseSizeButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Increase Size"
android:layout_below="@+id/myTextView"
android:layout_alignParentStart="true"
android:layout_alignParentLeft="true" />

<Button
android:id="@+id/decreaseSizeButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Decrease Size"
android:layout_below="@+id/myTextView"
android:layout_alignParentEnd="true"
android:layout_alignParentRight="true" />

<Button
android:id="@+id/changeColorButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Change Color"
android:layout_below="@+id/increaseSizeButton"
android:layout_alignParentStart="true"
android:layout_alignParentLeft="true" />

<Button
android:id="@+id/changeFontButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Change Font"
android:layout_below="@+id/increaseSizeButton"
android:layout_alignParentEnd="true"
android:layout_alignParentRight="true" />

</RelativeLayout>



Java file

package com.example.slip9_1;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

private TextView textView;
    private Button increaseSizeButton;
    private Button decreaseSizeButton;
    private Button changeColorButton;
    private Button changeFontButton;
    private int fontSize = 20;
    private int textColor = Color.BLACK;
    private String fontFamily = "sans-serif";

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

textView = findViewById(R.id.myTextView);
increaseSizeButton = findViewById(R.id.increaseSizeButton);
decreaseSizeButton = findViewById(R.id.decreaseSizeButton);
changeColorButton = findViewById(R.id.changeColorButton);
changeFontButton = findViewById(R.id.changeFontButton);

textView.setTextSize(fontSize);
textView.setTextColor(textColor);
textView.setTypeface(Typeface.create(fontFamily, Typeface.NORMAL));

increaseSizeButton.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {

fontSize += 2;
textView.setTextSize(fontSize);
}
        });

decreaseSizeButton.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {

if (fontSize >2) {
fontSize -= 2;
textView.setTextSize(fontSize);
}
            }
        });

changeColorButton.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
textColor = Color.RED;
textView.setTextColor(textColor);
}
            });

changeFontButton.setOnClickListener(new View.OnClickListener() {


@Override
public void onClick(View view) {

fontFamily = "monospace";
textView.setTypeface(Typeface.create(fontFamily, Typeface.NORMAL));
}
        });
}
}



OR mam
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity"
android:background="@color/colorAccent">

<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Hello TYBCA!"
android:fontFamily="cursive"
android:textSize="70dp"
app:layout_constraintBottom_toBottomOf="parent"
app:layout_constraintLeft_toLeftOf="parent"
app:layout_constraintRight_toRightOf="parent"
app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>


Q2.Create android first activity to accept information like student fisrt name middle name, last name date of birth. Address, Email ID and display all information on Second Activity whenever click on the Submit button
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
        android:id="@+id/fname"
          android:layout_width="match_parent"
       android:layout_height="wrap_content"
       android:layout_gravity="center"
      android:hint="Enter  stud first name"
       android:inputType="text"/>
    <EditText
        android:id="@+id/mname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter  stud middle name"
        android:text="stud last name"
        android:inputType="text"/>
        <EditText
         android:id="@+id/lname"
           android:layout_width="match_parent"
           android:layout_height="wrap_content"
           android:layout_gravity="center"
            android:hint="Enter last name"
             android:inputType="text"/>
    <EditText
        android:id="@+id/birth_date"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter date of birth "
        android:inputType="text"/>

    <EditText
        android:id="@+id/address"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter address"
        android:inputType="text"/>

    <EditText
        android:id="@+id/email_id"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter email id"
        android:inputType="text"/>


    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="next"/>


</LinearLayout>




Java file 1
package com.example.slip11studapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final EditText editText1= findViewById(R.id.fname);
        final EditText editText2=findViewById(R.id.mname);
        final EditText editText3=findViewById(R.id.lname);
        final EditText editText4=findViewById(R.id.birth_date);
        final EditText editText5=findViewById(R.id.address);
        final EditText editText6=findViewById(R.id.email_id);

         Button button1=findViewById(R.id.button);

         button1.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View view) {
                 String name =editText1.getText().toString().trim();
                 String releseyr=editText2.getText().toString().trim();
                 String collection=editText3.getText().toString().trim();
                 String dob=editText4.getText().toString().trim();
                 String saddress=editText5.getText().toString().trim();
                 String emailid=editText6.getText().toString().trim();
                 Bundle bundle =new Bundle();
                 bundle.putString("value1",name);
                 bundle.putString("value2",releseyr);
                 bundle.putString("value3",collection);
                 bundle.putString("value4",dob);
                 bundle.putString("value5",saddress);
                 bundle.putString("value6",emailid);


                 Intent intent =new Intent(MainActivity.this, SecondActivity.class);
                 intent.putExtras(bundle);
                 startActivity(intent);
             }
         });

    }
}




Xml file2

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".SecondActivity">

    <TextView
        android:id="@+id/text_fname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />

    <TextView
        android:id="@+id/text_mname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />

    <TextView
        android:id="@+id/text_lname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_birth_date"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_address"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_emailid"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />


</LinearLayout>



Java file 2

package com.example.slip11studapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Bundle bundle =getIntent().getExtras();
        if(bundle!=null){
            String value1 =bundle.getString("value1");
            String value2 =bundle.getString("value2");
            String value3 = bundle.getString("value3");
            String value4 = bundle.getString("value4");
            String value5 = bundle.getString("value5");
            String value6 = bundle.getString("value6");

            TextView textView1=findViewById(R.id.text_fname);
            TextView textView2=findViewById(R.id.text_mname);
            TextView textView3=findViewById(R.id.text_lname);
            TextView textView4=findViewById(R.id.text_birth_date);
            TextView textView5=findViewById(R.id.text_address);
            TextView textView6=findViewById(R.id.text_emailid);

            textView1.setText(value1);
            textView2.setText(value2);
            textView3.setText(value3);
            textView4.setText(value4);
            textView5.setText(value5);
            textView6.setText(value6);
        }
    }
}
