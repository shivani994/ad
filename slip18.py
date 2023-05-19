// slip18Q1.
//Q1 Create an android Application that Demostrate Alert Dilog Box
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"/>

</LinearLayout>

//Java file


package com.example.alterdilogboxapplication;

import android.content.DialogInterface;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Single button dilog box
        AlertDialog alertDialog=new AlertDialog.Builder(this).create();
        alertDialog.setTitle("Terms & Condition");
        alertDialog.setIcon(R.drawable.baseline_info_24);
        alertDialog.setMessage("Have you read all the term and condition");

        alertDialog.setButton(DialogInterface.BUTTON_POSITIVE, "Yes", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {
                        Toast.makeText(MainActivity.this, " Yes,You Can Process now", Toast.LENGTH_SHORT).show();
                    }
                });


        alertDialog.show();
}



(OR)MAM
XML FILE
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <Button
        android:id="@+id/btn"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Close app"/>



</RelativeLayout>



JAVA FILE
package com.example.slip18dialogapplication;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button closeButton;
    AlertDialog.Builder builder;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        closeButton=(Button) findViewById(R.id.btn);
        builder =new AlertDialog.Builder(this);
        closeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                 builder.setMessage(R.string.dialog_message).setTitle(R.string.dialog_title);

                builder .setMessage("Do you want to close this application")
                     .setCancelable(false)
                    .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                      @Override
                      public void onClick(DialogInterface dialogInterface, int i) {
                          finish();
                          Toast.makeText(MainActivity.this, "you choose yes action for alert box", Toast.LENGTH_SHORT).show();

                      }
                  })
                .setNegativeButton("No", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialogInterface, int i) {

                        dialogInterface.cancel();

                        Toast.makeText(MainActivity.this, "you choose no action for alert bo", Toast.LENGTH_SHORT).show();
                    }
                });

                AlertDialog alert = builder.create();

                alert.setTitle("AlertDialogExample");
                alert.show();

            }
        });

    }
}

string file in res->valiue->string.xml

<resources>
    <string name="app_name">Slip18DialogApplication</string>
    <string name="dialog_message">Welcome to Alert Dialog</string>
    <string name="dialog_title">Javapoint Alert Dialog</string>

</resources>


Q2Create An android application to accept two number and find power and Average Display the result on the next Activity usin context menu


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
        android:id="@+id/number1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="numberDecimal"
        android:hint="Enter a number"/>

    <EditText
        android:id="@+id/number2"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="numberDecimal"
        android:hint="Enter another number"/>
    <Button
        android:id="@+id/calculate"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Calculate"/>



</LinearLayout>

Java file 1

package com.example.slip18contextmenuapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private EditText number1;
    private EditText number2;
    private Button calculate;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        number1 = findViewById(R.id.number1);
        number2 = findViewById(R.id.number2);
        calculate = findViewById(R.id.calculate);
        calculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                double num1 = Double.parseDouble(number1.getText().toString());
                double num2 = Double.parseDouble(number2.getText().toString());

                double power = Math.pow(num1, num2);
                double average = (num1 + num2) / 2;

                Intent intent = new Intent(MainActivity.this, SecondActivity.class);
                intent.putExtra("power", power);
                intent.putExtra("average", average);
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
        android:id="@+id/result_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>



</LinearLayout>

Java file2

package com.example.slip18contextmenuapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class SecondActivity extends AppCompatActivity {
    private TextView resultText;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        resultText = findViewById(R.id.result_text);

        double power = getIntent().getDoubleExtra("power", 0);
        double average = getIntent().getDoubleExtra("average", 0);

        String result = "Power: " + power + "\nAverage: " + average;
        resultText.setText(result);

        registerForContextMenu(resultText);


    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);
        getMenuInflater().inflate(R.menu.context_menu, menu);
    }

    @Override
    public boolean onContextItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case R.id.power:
                ClipboardManager clipboard = (ClipboardManager) getSystemService(Context.CLIPBOARD_SERVICE);
                ClipData clip = ClipData.newPlainText("result", resultText.getText().toString());
                clipboard.setPrimaryClip(clip);
                Toast.makeText(this, "Result copied to clipboard", Toast.LENGTH_SHORT).show();
                return true;
            case R.id.average:
                Intent shareIntent = new Intent(Intent.ACTION_SEND);
                shareIntent.setType("text/plain");
                shareIntent.putExtra(Intent.EXTRA_TEXT, resultText.getText().toString());
                startActivity(Intent.createChooser(shareIntent, "Share result"));
                return true;
            default:
                return super.onContextItemSelected(item);
        }

    }
}
Create menu file in res ->>creat new directori in  that create context_menu for this  go to res directorylayou resource in ok

<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/power"
        android:title="Power"/>
    <item
        android:id="@+id/average"
        android:title="Average"/>
</menu>

