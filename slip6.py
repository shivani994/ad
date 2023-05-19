SLIP NO 6
Q1) 1. Create a Simple Application Which Send ―Hello! message from one activity to anotherwith help of Button (Use Intent).
1)xml file(first)
<?xml version="1.0" encoding="utf-8"?>

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

tools:context=".MainActivity">



<Button

android:id="@+id/btnSendHello"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:text="Send Hello!"

android:layout_centerInParent="true">



</Button>



</RelativeLayout>

1)java file(1)
package com.example.slip6_1;



import androidx.appcompat.app.AppCompatActivity;



import android.content.Intent;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;



public class MainActivity extends AppCompatActivity {



private Button btnSendHello;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);



btnSendHello = findViewById(R.id.btnSendHello);

btnSendHello.setOnClickListener(new View.OnClickListener() {

@Override

public void onClick(View view) {





                Intent intent = new Intent(MainActivity.this, MainActivity2.class);

intent.putExtra("message", "Hello!");

startActivity(intent);

}



            });

}

}


2)xml file(second)
<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity2">



<TextView

android:id="@+id/tvMessage"

android:layout_width="wrap_content"

android:layout_height="wrap_content"

android:textSize="24sp"

android:textStyle="bold"/>





</LinearLayout>

2)java file(second)

package com.example.slip6_1;



import androidx.appcompat.app.AppCompatActivity;



import android.os.Bundle;

import android.widget.TextView;



public class MainActivity2 extends AppCompatActivity {

private TextView tvMessage;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main2);



tvMessage = findViewById(R.id.tvMessage);



Bundle extras = getIntent().getExtras();

        if (extras != null) {

            String message = extras.getString("message");

tvMessage.setText(message);

}

    }

}



Q2). Create an Android Application that Demonstrates ListView and Onclick of List Displaythe Toast.

Activity_main_xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<ListView
android:id="@+id/simplelist"
android:layout_width="fill_parent"
android:layout_height="wrap_content"
android:dividerHeight="10dp"/>

</LinearLayout>

Main_activity.java
package com.example.listview;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity
implements AdapterView.OnItemSelectedListener {
ListView simplelist;
String countryList[]={"Indian","America","china"};
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
simplelist=(ListView)findViewById(R.id.simplelist);
simplelist.setOnItemSelectedListener(this);

ArrayAdapter aa =new ArrayAdapter(this, android.R.layout.simple_list_item_1,countryList);
simplelist.setAdapter(aa);

    }

@Override
public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
Toast.makeText(getApplicationContext(),
countryList[i],Toast.LENGTH_LONG).show();
    }

@Override
public void onNothingSelected(AdapterView<?> adapterView) {

    }
}


