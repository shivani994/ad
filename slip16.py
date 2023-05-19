SLIP16
Q1.
Q2.Crea an Android application Ap [p it reads the Student Detail (Name Surname, Class, Gender, Hobbies, Marks)display the all information in another activity in table format on click of submit button

Xml file1
<LinearLayout>
<EditText
android:id="@+id/txtname"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:hint="Enter Name"
android:layout_marginTop="20dp"/>

<EditText
android:id="@+id/txtsurname"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:hint="Enter SurName"
android:layout_marginTop="20dp"/>

<EditText
android:id="@+id/txtclass"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:hint="Enter Classname"
android:layout_marginTop="20dp"/>


<EditText
android:id="@+id/txtGender"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:hint="Gender"
android:layout_marginTop="20dp"/>

<EditText
android:id="@+id/txthobbies"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:hint="Enter Hobbies"
android:layout_marginTop="20dp"/>

<EditText
android:id="@+id/txtmarks"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:inputType="number"
android:hint="Enter Marks"
android:layout_marginTop="20dp"/>

<Button
android:id="@+id/btnsubmit"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="50dp"
android:text="Submit"
android:layout_marginLeft="50dp"
android:layout_marginRight="50dp"/>

</LinearLayout>

Java file 1
Public class MainActivityextends AppCompatActivity{
EditTexttxtname,txtsurname,txtclass,txtGender,txthobbies,txtmarks;
Button btnsubmit;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

txtname=(EditText) findViewById(R.id.txtname);
txtsurname=(EditText) findViewById(R.id.txtsurname);
txtclass public =(EditText)findViewById(R.id.txtclass);
txtGender=(EditText) findViewById(R.id.txtGender);
txthobbies=(EditText) findViewById(R.id.txthobbies);
txtmarks=(EditText) findViewById(R.id.txtmarks);

btnsubmit=(Button) findViewById(R.id.btnsubmit);

btnsubmit.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
String name=txtname.getText().toString().trim();
String surname=txtsurname.getText().toString().trim();
String classes=txtclass.getText().toString().trim();
String Gender=txtGender.getText().toString().trim();
String hobbies=txthobbies.getText().toString().trim();
String marks=txtmarks.getText().toString().trim();//fetching data

Bundle bundle=new Bundle();//bundle import........... variable careate
        //bundle variable use...
bundle.putString("name",name);//key and where stroed name
bundle.putString("surname",surname);
bundle.putString("classes",classes);
bundle.putString("Gender",Gender);
bundle.putString("hobbies",hobbies);
bundle.putString("marks",marks);

//new intent open karnahai
Intent intent=new Intent(MainActivity.this,MainActivity2.class);
intent.putExtras(bundle);
startActivity(intent);
    }
});
}
}

Xml file2
<TableLayout>
<TableRow
android:layout_marginTop="300dp"
android:layout_marginLeft="40dp"
android:layout_marginRight="40dp">

<TextView
android:id="@+id/txt_name"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="30dp"
android:layout_marginLeft="40dp"
android:text="Hello"
android:textAlignment="center"/>

<TextView
android:id="@+id/txt_surname"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
android:text="Hello"/>
</TableRow>

<TableRow
android:layout_marginTop="30dp"
android:layout_marginLeft="40dp"
android:layout_marginRight="40dp">
<TextView
android:id="@+id/txt_classname"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
android:text="Hello"
/>
<TextView
android:id="@+id/txt_Gender"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
android:text="Hello"/>
</TableRow>

<TableRow
android:layout_marginTop="30dp"
android:layout_marginLeft="40dp"
android:layout_marginRight="40dp">
<TextView
android:id="@+id/txt_hobbies"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
android:text="Hello"/>

<TextView
android:id="@+id/txt_marks"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
android:text="Hello"/>
</TableRow>
</TableLayout>

Java file 2
TextViewtxt_name,txt_surname,txt_classname,txt_Gender,txt_hobbies,txt_marks;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main2);


Bundle bundle=getIntent().getExtras();

txt_name= (TextView) findViewById(R.id.txt_name);
txt_surname=(TextView) findViewById(R.id.txt_surname);
txt_classname=(TextView) findViewById(R.id.txt_classname);
txt_Gender=(TextView) findViewById(R.id.txt_Gender);
txt_hobbies=(TextView) findViewById(R.id.txt_hobbies);
txt_marks=(TextView) findViewById(R.id.txt_marks);


if( bundle != null)
        {
String name = bundle.getString("name");
String surname = bundle.getString("surname");
String classes = bundle.getString("classes");
String Gender = bundle.getString("Gender");
String hobbies = bundle.getString("hobbies");
String marks = bundle.getString("marks");

txt_name.setText(name);
txt_surname.setText(surname);
txt_classname.setText(classes);
txt_Gender.setText(Gender);
txt_hobbies.setText(hobbies);
txt_marks.setText(marks);

        }
    }
}



Q2 .Create an android application that demonstrate TimePicker and display selected time on TextView.
1)Xml file
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<TimePicker
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:id="@+id/timepicker">

</TimePicker>


<TextView
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_centerInParent="true"
android:layout_below="@+id/timepicker"
android:id="@+id/time">

</TextView>


</RelativeLayout>

2)Java file
package com.example.slip16_2;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.TimePicker;

public class MainActivity extends AppCompatActivity {
  TimePicker timePicker;
TextView textView;
@SuppressLint("MissingInflatedId")
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

timePicker=findViewById(R.id.timepicker);
textView=findViewById(R.id.time);

timePicker.setOnTimeChangedListener(new TimePicker.OnTimeChangedListener() {
@Override
public void onTimeChanged(TimePicker timePicker, int i, int i1) {
textView.setText(i+":"+i1);
}
        });
}
}


