SLIP NO 9
Q1)Write an android application to accept two numbers from the user and display them and reject input if both numbers are greater than 10 and ask for two new numbers.
1)xml file
<?xml version="1.0" encoding="utf-8"?>

<LinearLayout

xmlns:android="http://schemas.android.com/apk/res/android"

xmlns:app="http://schemas.android.com/apk/res-auto"

xmlns:tools="http://schemas.android.com/tools"

android:layout_width="match_parent"

android:layout_height="match_parent"

android:padding="16dp"

android:orientation="vertical"

tools:context=".MainActivity">



<EditText

android:id="@+id/first_number_edittext"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:hint="Enter first number"

android:inputType="number" />



<EditText

android:id="@+id/second_number_edittext"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:hint="Enter second number"

android:inputType="number" />



<Button

android:id="@+id/submit_button"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:text="Submit" />



<TextView

android:id="@+id/result_textview"

android:layout_width="match_parent"

android:layout_height="wrap_content"

android:paddingTop="16dp" />



</LinearLayout>

1)java file
package com.example.slip91;



import androidx.appcompat.app.AppCompatActivity;



import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.EditText;

import android.widget.TextView;

import android.widget.Toast;



public class MainActivity extends AppCompatActivity {



private EditText firstNumberEditText;

    private EditText secondNumberEditText;

    private Button submitButton;

    private TextView resultTextView;



@Override

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

setContentView(R.layout.activity_main);



firstNumberEditText = findViewById(R.id.first_number_edittext);

secondNumberEditText = findViewById(R.id.second_number_edittext);

submitButton = findViewById(R.id.submit_button);

resultTextView = findViewById(R.id.result_textview);



submitButton.setOnClickListener(new View.OnClickListener() {

@Override

public void onClick(View view) {



                String firstNumberString = firstNumberEditText.getText().toString();

String secondNumberString = secondNumberEditText.getText().toString();



                if (firstNumberString.isEmpty() || secondNumberString.isEmpty()) {

                    Toast.makeText(MainActivity.this, "Please enter two numbers", Toast.LENGTH_SHORT).show();

                    return;

}



int firstNumber = Integer.parseInt(firstNumberString);

                int secondNumber = Integer.parseInt(secondNumberString);



                if (firstNumber >10 && secondNumber >10) {

                    Toast.makeText(MainActivity.this, "Both numbers cannot be greater than 10", Toast.LENGTH_SHORT).show();

firstNumberEditText.getText().clear();

secondNumberEditText.getText().clear();

                    return;

}



                String resultString = "First number: " + firstNumber + "\n" + "Second number: " + secondNumber;

resultTextView.setText(resultString);

}

        });

}

}


Q2. Create table Company (id, name, address, phno). Create Application for Performing the following operation on the table. a) Insert New Company details. b) Show All Company details
xmlfile
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
android:id="@+id/editTextId"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="ID"/>

<EditText
android:id="@+id/editTextName"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="Name"/>

<EditText
android:id="@+id/editTextAddress"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="Address"/>

<EditText
android:id="@+id/editTextPhno"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:hint="Phone Number"/>

<Button
android:id="@+id/buttonInsert"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="Insert"/>

<Button
android:id="@+id/buttonShow"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:text="Show All"/>



</LinearLayout>

Java file
package com.example.slip9_2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.SimpleCursorAdapter;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

EditText editTextId = findViewById(R.id.editTextId);
EditText editTextName = findViewById(R.id.editTextName);
EditText editTextAddress = findViewById(R.id.editTextAddress);
EditText editTextPhno = findViewById(R.id.editTextPhno);
Button buttonInsert = findViewById(R.id.buttonInsert);
Button buttonShow = findViewById(R.id.buttonShow);

buttonInsert.setOnClickListener(new View.OnClickListener() {

@Override
public void onClick(View view) {

int id = Integer.parseInt(editTextId.getText().toString());
String name = editTextName.getText().toString();
String address = editTextAddress.getText().toString();
String phno = editTextPhno.getText().toString();

// Insert new company details into database
CompanyDatabaseHelper dbHelper = new CompanyDatabaseHelper(getApplicationContext());
SQLiteDatabase db = dbHelper.getWritableDatabase();
ContentValues values = new ContentValues();
values.put("id", id);
values.put("name", name);
values.put("address", address);
values.put("phno", phno);
db.insert("Company", null, values);
db.close();

// Clear UI components
editTextId.setText("");
editTextName.setText("");
editTextAddress.setText("");
editTextPhno.setText("");

// Show success message
Toast.makeText(getApplicationContext(), "New company details inserted.", Toast.LENGTH_SHORT).show();
            }
        });

buttonShow.setOnClickListener(new View.OnClickListener() {

@Override
public void onClick(View view) {


// Query all company details from database
CompanyDatabaseHelper dbHelper = new CompanyDatabaseHelper(getApplicationContext());
SQLiteDatabase db = dbHelper.getReadableDatabase();
String[] projection = {"id", "name", "address", "phno"};
Cursor cursor = db.query("Company", projection, null, null, null, null, null);

// Display results in a ListView
ListView listView = new ListView(getApplicationContext());
SimpleCursorAdapter adapter = new SimpleCursorAdapter(
                        getApplicationContext(),
android.R.layout.simple_list_item_2,
cursor,
new String[] {"name", "address"},
new int[] {android.R.id.text1, android.R.id.text2},
0);
listView.setAdapter(adapter);
                setContentView(listView);
            }
        });
    }
}

Databasefile
package com.example.slip9_2;

import android.annotation.SuppressLint;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;

public class CompanyDatabaseHelper extends SQLiteOpenHelper {

public static final String DATABASE_NAME = "company.db";
public static final int DATABASE_VERSION = 1;

public static final String TABLE_COMPANY = "company";
public static final String COLUMN_ID = "_id";
public static final String COLUMN_NAME = "name";
public static final String COLUMN_ADDRESS = "address";
public static final String COLUMN_PHNO = "phno";

private static final String DATABASE_CREATE = "create table " +
TABLE_COMPANY + "(" + COLUMN_ID +
" integer primary key autoincrement, " +
COLUMN_NAME + " text not null, " +
COLUMN_ADDRESS + " text not null, " +
COLUMN_PHNO + " text not null);";
private SQLiteDatabase database;


public CompanyDatabaseHelper(Context context) {
super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

@Override
public void onCreate(SQLiteDatabase sqLiteDatabase) {
database.execSQL(DATABASE_CREATE);
    }





@Override
public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
database.execSQL("DROP TABLE IF EXISTS " + TABLE_COMPANY);
        onCreate(database);
    }
public void insertCompany(String name, String address, String phno) {
SQLiteDatabase db = this.getWritableDatabase();

ContentValues values = new ContentValues();
values.put(COLUMN_NAME, name);
values.put(COLUMN_ADDRESS, address);
values.put(COLUMN_PHNO, phno);

db.insert(TABLE_COMPANY, null, values);
db.close();
    }

@SuppressLint("Range")
public List<Company>getAllCompanies() {
        List<Company>companyList = new ArrayList<>();
String selectQuery = "SELECT  * FROM " + TABLE_COMPANY;

SQLiteDatabase db = this.getWritableDatabase();
Cursor cursor = db.rawQuery(selectQuery, null);

if (cursor.moveToFirst()) {
do {
                Company company = new Company();
company.setId(cursor.getInt(cursor.getColumnIndex(COLUMN_ID)));
company.setName(cursor.getString(cursor.getColumnIndex(COLUMN_NAME)));
company.setAddress(cursor.getString(cursor.getColumnIndex(COLUMN_ADDRESS)));
company.setPhno(cursor.getString(cursor.getColumnIndex(COLUMN_PHNO)));
companyList.add(company);
            } while (cursor.moveToNext());
        }

cursor.close();
db.close();

return companyList;
    }
}



