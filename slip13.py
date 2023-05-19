Slip-13
Question 1
Xml file

Here take linear layout and orientation vertical and  buttongaravity remove by defalult left
Xml file
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayoutxmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">


<ScrollView
android:layout_width="match_parent"
android:layout_height="match_parent">

<LinearLayout
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:orientation="vertical">

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 1" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 2" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 3" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 4" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 5" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 6" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 7" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 10" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 8" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 9" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 11" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 12" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 13" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 14" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 15" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 16" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 17" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 18" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 19" />

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_gravity="center"
android:text="Button 20" />
</LinearLayout>
</ScrollView>


</androidx.constraintlayout.widget.ConstraintLayout>

Java file don not do anything in java

package com.example.slip13application;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivityextends AppCompatActivity{

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
    }
}


question-2
Q2. Write an application to accept a teacher name from user and display the names of studentsalong with subjects to whom they are teaching. Create table Student (sno ,s_name,s_class,s_addr) Teacher (tno, t_name, qualification, experience) Student-Teacher has Many to Many relationship.

Xml.file

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
xmlns:app="http://schemas.android.com/apk/res-auto"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:orientation="vertical"
tools:context=".MainActivity">
<TextView
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:id="@+id/studentsTextView"

/>
<EditText
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:id="@+id/teacherNameEditText"/>

<Button
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:text="Button"
android:id="@+id/displayButton"/>
</LinearLayout>

Main.java
package com.example.a13;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.HashMap;
import java.util.Map;

public class MainActivityextends AppCompatActivity{
private Map<String, Map<String, String>>teacherMapping;

private EditTextteacherNameEditText;
private TextViewstudentsTextView;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);

initializeTeacherMapping();

teacherNameEditText= findViewById(R.id.teacherNameEditText);
studentsTextView= findViewById(R.id.studentsTextView);
Button displayButton= findViewById(R.id.displayButton);

displayButton.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View v) {
// Retrieve the teacher's name from the EditText
String teacherName= teacherNameEditText.getText().toString();

// Display the students and subjects taught by the teacher
displayStudentsAndSubjects(teacherName);
            }
        });
    }



private void initializeTeacherMapping() {

teacherMapping= new HashMap<>();

// Add teacher-student-subject mappings
Map<String, String>msSmithStudents= new HashMap<>();
msSmithStudents.put("John", "Mathematics");
msSmithStudents.put("Emily", "Science");
msSmithStudents.put("Michael", "English");
teacherMapping.put("Ms. Smith", msSmithStudents);

Map<String, String>mrJohnsonStudents= new HashMap<>();
mrJohnsonStudents.put("Sarah", "History");
mrJohnsonStudents.put("Thomas", "Mathematics");
mrJohnsonStudents.put("Emily", "Geography");
teacherMapping.put("Mr. Johnson", mrJohnsonStudents);

Map<String, String>mrsDavisStudents= new HashMap<>();
mrsDavisStudents.put("Emma", "Science");
mrsDavisStudents.put("Jacob", "English");
mrsDavisStudents.put("Olivia", "Mathematics");
teacherMapping.put("Mrs. Davis", mrsDavisStudents);
    }


@SuppressLint("SetTextI18n")
private void displayStudentsAndSubjects(String teacherName) {
if (teacherMapping.containsKey(teacherName)) {
Map<String, String>studentsAndSubjects= teacherMapping.get(teacherName);
StringBuilder stringBuilder= new StringBuilder();
stringBuilder.append("Teacher: ").append(teacherName).append("\n");
stringBuilder.append("Students:\n");
assert studentsAndSubjects!= null;
for (Map.Entry<String, String>entry : studentsAndSubjects.entrySet()) {
String student = entry.getKey();
String subject = entry.getValue();
stringBuilder.append(student).append(": ").append(subject).append("\n");
                }
studentsTextView.setText(stringBuilder.toString());
            } else {
studentsTextView.setText("Teacher not found.");
            }
        }
    }

