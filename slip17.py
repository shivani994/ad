Slip 17

Q1 Write an android code to make phone call using intent

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






Q2 Construct an android Application to accept a number and calculate Factorial and sum of Digit of a give number using Context Menu
Xml File
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
        android:id="@+id/number_edit_text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter a number" />

    <TextView
        android:id="@+id/factorial_text_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Factorial: " />

    <TextView
        android:id="@+id/sum_of_digits_text_view"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Sum of Digits: " />



</LinearLayout>



Java file
package com.example.myapplication;



import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.ContextMenu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText numberEditText;
    private TextView factorialTextView;
    private TextView sumOfDigitsTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        numberEditText = findViewById(R.id.number_edit_text);
        factorialTextView = findViewById(R.id.factorial_text_view);
        sumOfDigitsTextView = findViewById(R.id.sum_of_digits_text_view);

        registerForContextMenu(numberEditText);
    }

    private int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    private int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menu, v, menuInfo);
        menu.setHeaderTitle("Choose an operation");
        menu.add(0, 1, 0, "Calculate Factorial");
        menu.add(0, 2, 0, "Calculate Sum of Digits");
        factorialTextView.setText("Factorial: ");
        sumOfDigitsTextView.setText("Sum of Digits: ");
    }

    @Override
    public boolean onContextItemSelected(@NonNull MenuItem item) {
        int number = Integer.parseInt(numberEditText.getText().toString());
        switch (item.getItemId()) {
            case 1:
                int factorialResult = factorial(number);
                factorialTextView.setText("Factorial: " + factorialResult);
                return true;
            case 2:
                int sumResult = sumOfDigits(number);
                sumOfDigitsTextView.setText("Sum of Digits: " + sumResult);
                return true;
            default:
                return super.onContextItemSelected(item);
        }
    }
}







