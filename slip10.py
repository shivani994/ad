Slip10
Q1). Create an Android Application that Demonstrate Switch and Toggle Button

Xml file

Xml file
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayoutxmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:padding="16dp"
tools:context=".MainActivity">

<Switch
android:id="@+id/switchButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Switch"
android:checked="false"
android:layout_marginBottom="100dp"
android:layout_centerHorizontal="true"/>


<ToggleButton
android:id="@+id/toggleButton"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:textOn="On"
android:textOff="Off"
android:checked="false"
android:layout_below="@id/switchButton"
android:layout_centerHorizontal="true"/>

</RelativeLayout>

Java file
package com.example.slip10_1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.Toast;
import android.widget.ToggleButton;

public class MainActivityextends AppCompatActivity{
private Switch switchButton;
private ToggleButtontoggleButton;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

switchButton= findViewById(R.id.switchButton);
toggleButton= findViewById(R.id.toggleButton);

switchButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
@Override
public void onCheckedChanged(CompoundButtonbuttonView, booleanisChecked) {
if (isChecked) {
// Switch is on
Toast.makeText(MainActivity.this, "Switch is on", Toast.LENGTH_SHORT).show();
                } else {
// Switch is off
Toast.makeText(MainActivity.this, "Switch is off", Toast.LENGTH_SHORT).show();
                }
            }
        });

toggleButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
@Override
public void onCheckedChanged(CompoundButtonbuttonView, booleanisChecked) {
if (isChecked) {
// Toggle button is on
Toast.makeText(MainActivity.this, "Toggle button is on", Toast.LENGTH_SHORT).show();
                } else {
// Toggle button is off
Toast.makeText(MainActivity.this, "Toggle button is off", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}




Q2 Demostrate Array Adapter using List View to Display list of fruits

Xml file

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <ListView
            android:id="@+id/fruit_list"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"/>
</LinearLayout>

</LinearLayout>



Java file



package com.example.slip10application;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MainActivity extends AppCompatActivity {
    String[] fruitArray={"Apple","mango","Banana","Blackberry","Pinaple","strawbery"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ArrayAdapter adapter=new ArrayAdapter<String>(this, androidx.appcompat.R.layout.support_simple_spinner_dropdown_item,fruitArray);
        ListView listView=(ListView) findViewById(R.id.fruit_list);
        listView.setAdapter(adapter);


    }
}


