SLIP NO 3
Q1. Create an Android Application that will change color of the College Name on click ofPush Button and change the font size, font style of text view using xml.
Activity main.xml

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical"
tools:context=".ClickButton">


<TextView
android:id="@+id/college_name"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="S.M.Joshi college in hadpsar"
android:textSize="30dp"
android:textStyle="italic"
android:layout_marginLeft="50dp"
android:layout_marginRight="50dp"
android:textAlignment="center"
android:layout_marginTop="100dp"
/>

<LinearLayout
android:layout_width="match_parent"
android:layout_height="match_parent">

<Button
android:id="@+id/change_button"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_weight="1"
android:text="push"
android:textSize="28dp"
android:textStyle="italic"
android:layout_marginLeft="30dp"
android:layout_marginTop="30dp"
android:layout_marginRight="30dp"
/>



</LinearLayout>

</LinearLayout>

Activity.java

public class MainActivity extends AppCompatActivity {
TextView college_name;
Button change_button;


@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

college_name = (TextView) findViewById(R.id.college_name);
change_button = (Button) findViewById(R.id.change_button);
change_button.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
college_name.setTextColor(Color.RED);
            }
        });


    }
}

Q2. Create an Android App, it reads the Students Details (Name, Surname, Class, Gender, Hobbies, Marks) and display the all information in another activity in table format on click of Submit button.
Activity.xml

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

MainActivity.java

public class MainActivity extends AppCompatActivity {
EditText txtname,txtsurname,txtclass,txtGender,txthobbies,txtmarks;
Button btnsubmit;
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

txtname=(EditText) findViewById(R.id.txtname);
txtsurname=(EditText) findViewById(R.id.txtsurname);
txtclass=(EditText)findViewById(R.id.txtclass);
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

//new intent open karna hai
Intent intent=new Intent(MainActivity.this,MainActivity2.class);
intent.putExtras(bundle);
        startActivity(intent);
    }
});


create a new activity
activity.xml

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


mainActivity2.java
TextView txt_name,txt_surname,txt_classname,txt_Gender,txt_hobbies,txt_marks;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);


Bundle bundle =getIntent().getExtras();

txt_name = (TextView) findViewById(R.id.txt_name);
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

