slip15
Q1.design following add a border to an AndroidLayout


-Border xml file
Create->go in drawavble->rightclick->drawable resource file give name-> next->the set this
Border.xml
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
<stroke
    android:width="30dp"
    android:color="#ffffff">

</stroke>

</shape>


Main xml File
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#000000"
    android:padding="10dp"
    tools:context=".MainActivity">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@drawable/border"
        android:orientation="vertical">

        <TextView
            android:id="@+id/text1"
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:background="#A00000FF"
            android:gravity="center_vertical|center_horizontal"
            android:text="Hello World!"
            android:textColor="#ffffff"
            android:textSize="40sp"/>

    </LinearLayout>

</RelativeLayout>


Java file in java not wirte code

package com.example.slip15bapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}



Q2 Create first activity to accept information like Employee Fisrt name Middle name Last name, salary,Address ,Email Id and display all information on Second activity where user click on Submit button


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
        android:id="@+id/efname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter employee first name"
        android:inputType="text"/>
    <EditText
        android:id="@+id/emname"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter employee middle name"
        android:inputType="text"/>

        <EditText
         android:id="@+id/elname"
         android:layout_width="match_parent"
         android:layout_height="wrap_content"
         android:layout_gravity="center"
         android:hint="Enter employee last name"
          android:inputType="text"/>
    <EditText
        android:id="@+id/esalary"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter employee salary"
        android:inputType="text"/>

    <EditText
        android:id="@+id/eaddress"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter employee address"
        android:inputType="text"/>
    <EditText
        android:id="@+id/eemail"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:hint="Enter employee email"
        android:inputType="text"/>



    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="next"/>





</LinearLayout>



Java file 1

package com.example.slip15employeeapplication;

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

        final EditText editText1= findViewById(R.id.efname);
        final EditText editText2=findViewById(R.id.emname);
        final EditText editText3=findViewById(R.id.elname);
        final EditText editText4=findViewById(R.id.esalary);
        final EditText editText5=findViewById(R.id.eaddress);
        final EditText editText6=findViewById(R.id.eemail);
        Button button1=findViewById(R.id.button);

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name1 =editText1.getText().toString().trim();
                String name2=editText2.getText().toString().trim();
                String name3=editText3.getText().toString().trim();
                String sal=editText4.getText().toString().trim();
                String add=editText5.getText().toString().trim();
                String email=editText6.getText().toString().trim();

                Bundle bundle =new Bundle();
                bundle.putString("value1",name1);
                bundle.putString("value2",name2);
                bundle.putString("value3",name3);
                bundle.putString("value4",sal);
                bundle.putString("value5",add);
                bundle.putString("value6",email);

                Intent intent =new Intent(MainActivity.this, SecondActivity.class);
                intent.putExtras(bundle);
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
    android:orientation="vertical"
    tools:context=".SecondActivity">

    <TextView
        android:id="@+id/text_efname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />

    <TextView
        android:id="@+id/text_emname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />

    <TextView
        android:id="@+id/text_elname"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_esal"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_eadd"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />
    <TextView
        android:id="@+id/text_eemail"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        />





</LinearLayout>

Java file 2
package com.example.slip15employeeapplication;

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

            TextView textView1=findViewById(R.id.text_efname);
            TextView textView2=findViewById(R.id.text_emname);
            TextView textView3=findViewById(R.id.text_elname);
            TextView textView4=findViewById(R.id.text_esal);
            TextView textView5=findViewById(R.id.text_eadd);
            TextView textView6=findViewById(R.id.text_eemail);
            textView1.setText(value1);
            textView2.setText(value2);
            textView3.setText(value3);
            textView4.setText(value4);
            textView5.setText(value5);
            textView6.setText(value6);
        }
    }
}
