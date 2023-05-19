SLIP NO 5
Q1) Create an android application to accept two numbers and find power and average.
1)xml file(first)

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity">



<EditText

android:id="@+id/editTextNumber1"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:inputType="numberDecimal"

android:hint="Enter first number" />



<EditText

android:id="@+id/editTextNumber2"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:inputType="numberDecimal"

android:hint="Enter second number" />



<Button

android:id="@+id/buttonCalculate"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:text="Calculate" />



</LinearLayout>

1)java file(first)
package com.example.slip5_1;



import androidx.appcompat.app.AppCompatActivity;



import android.content.Intent;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.EditText;



public class MainActivity extends AppCompatActivity {

private EditText etNumber1, etNumber2;

    private Button btnCalculate;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);



etNumber1 =(EditText) findViewById(R.id.editTextNumber1);

etNumber2 =(EditText) findViewById(R.id.editTextNumber2);

btnCalculate =(Button) findViewById(R.id.buttonCalculate);



btnCalculate.setOnClickListener(new View.OnClickListener() {

@Override

public void onClick(View view) {

double num1 = Double.parseDouble(etNumber1.getText().toString());

                double num2 = Double.parseDouble(etNumber2.getText().toString());



                double power = Math.pow(num1, num2);

                double average = (num1 + num2) / 2;



Intent intent = new Intent(MainActivity.this, MainActivity2.class);

intent.putExtra("power", power);

intent.putExtra("average", average);

startActivity(intent);

}

        });





}

}

2)xml file (second)
<?xml version="1.0" encoding="utf-8"?>

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:orientation="vertical"

tools:context=".MainActivity2">



<TextView

android:id="@+id/tvPower"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:textSize="24sp"

android:textColor="@android:color/black"

android:textStyle="bold"

android:layout_marginBottom="8dp"/>



<TextView

android:id="@+id/tvAverage"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:textSize="24sp"

android:textColor="@android:color/black"

android:textStyle="bold"/>



</LinearLayout>

2)java file(second)
package com.example.slip5_1;



import androidx.appcompat.app.AppCompatActivity;



import android.os.Bundle;

import android.widget.TextView;



public class MainActivity2 extends AppCompatActivity {

private TextView tvPower, tvAverage;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main2);



tvPower = findViewById(R.id.tvPower);

tvAverage = findViewById(R.id.tvAverage);



Bundle extras = getIntent().getExtras();

        double power = extras.getDouble("power");

        double average = extras.getDouble("average");



tvPower.setText(String.format("Power: %.2f", power));

tvAverage.setText(String.format("Average: %.2f", average));

}

}


Q2) . Create an Android application that creates a custom Alert Dialog containing Friends Name and onClick of Friend Name Button greet accordingly.
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<Button
android:id="@+id/getBtn"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginLeft="150dp"
android:layout_marginTop="200dp"
android:text="Show Alert" />

</RelativeLayout>

Mainactivity.java
package com.example.slip5_1;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
final CharSequence[] Friend = { "Neha", "Shivani", "Mahek", "Sonal" };
ArrayList<Integer>slist = new ArrayList();
boolean icount[] = new boolean[Friend.length];
String msg ="";
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

Button btn = (Button)findViewById(R.id.getBtn);
btn.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View v) {
AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
builder.setTitle("Choose Friends")
                        .setMultiChoiceItems(Friend,icount, new DialogInterface.OnMultiChoiceClickListener() {
@Override
public void onClick(DialogInterface arg0, int arg1, boolean arg2) {
if (arg2) {
// If user select a item then add it in selected items
slist.add(arg1);
                                } else if (slist.contains(arg1)) {
// if the item is already selected then remove it
slist.remove(Integer.valueOf(arg1));
                                }
                            }
                        })      .setCancelable(false)
                        .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
@Override
public void onClick(DialogInterface dialog, int which) {
msg = "";
for (int i = 0; i <slist.size(); i++) {
msg = msg + "\n" + (i + 1) + " : " + Friend[slist.get(i)];
                                }
Toast.makeText(getApplicationContext(), "Total " + slist.size() + " Items Selected.\n" + msg, Toast.LENGTH_SHORT).show();
                            }
                        })
                        .setNegativeButton("No", new DialogInterface.OnClickListener() {
@Override
public void onClick(DialogInterface dialog, int which) {
Toast.makeText(MainActivity.this,"No Option Selected",Toast.LENGTH_SHORT).show();
                            }
                        });
//Creating dialog box
AlertDialog dialog  = builder.create();
dialog.show();
            }
        });
    }
}

