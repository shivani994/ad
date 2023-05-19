Slip8


Q1 create an android application with login Screen. On successful login, give message go to next Activity(Without Using Database  and use Table layout)

Xml file 1

<?xml version="1.0" encoding="utf-8"?>
<TableLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TableRow
        android:layout_width="match_parent"
        android:layout_height="match_parent">
        <TextView
            android:id="@+id/textview"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Username"/>

    <EditText
        android:id="@+id/edittext1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:ems="10"
        android:inputType="text"/>
    </TableRow>
    <TableRow
        android:layout_width="match_parent"
        android:layout_height="match_parent">
    <TextView
    android:id="@+id/textview2"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Password"/>

    <EditText
        android:id="@+id/edittext2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:ems="10"
        android:inputType="text"/>

    </TableRow>
    <Button
        android:id="@+id/button1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="login"/>

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="cancle"/>
</TableLayout>

Java1

package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    EditText username;
    EditText password;
    Button login;
    Button cancle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username=(EditText)findViewById(R.id.edittext1);
        password=(EditText)findViewById(R.id.edittext2);
        login=(Button)findViewById(R.id.button1);
        cancle=(Button)findViewById(R.id.button2);
        login.setOnClickListener(this);
        cancle.setOnClickListener(this);


    }

    @Override
    public void onClick(View view) {
        String na=username.getText().toString();
        String pa=password.getText().toString();

        switch (view.getId())
        {
            case R.id.button1:
                if(na.equals("chaitu")&&pa.equals("admin")){
                    Intent i=new Intent(this,SecondActivity.class);
                    i.putExtra("c1",na);
                    startActivity(i);

                }
                else
                {
                    Toast.makeText(this, "check #username or #password",Toast.LENGTH_LONG).show();
                }
                break;

            case R.id.button2:
                username.setText("");
                password.setText("");
                break;

            default:
                break;

        }
    }
}

xml file 2

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".SecondActivity">
    <TextView
        android:id="@+id/text1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true"
        tools:content=".SecondActivity"/>

    <Button
        android:id="@+id/btn1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"

        android:text="Logout"/>

</RelativeLayout>

Javafile 2

package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity implements View.OnClickListener {
    Button Logout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        Intent i=getIntent();
        String str=i.getStringExtra("c1");
        TextView t1=(TextView) findViewById(R.id.text1);
        t1.setText("Logged In Sucessfully!"+str);
        Logout=(Button) findViewById(R.id.btn1);
        Logout.setOnClickListener(this);
    }

    @Override
    public void onClick(View view1) {
        switch (view1.getId())
        {
            case R.id.btn1:
                Intent i=new Intent(this,MainActivity.class);
                startActivity(i);
                finish();
                System.exit(0);
                break;
            default:
                break;

        }


    }
}

Q2 Create application to send email with attachment.

Xml file
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="10dp"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="To:"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
         android:id="@+id/edit_text_to"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textEmailAddress"/>


    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Subject:"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
        android:id="@+id/edit_text_subject"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:inputType="textEmailSubject"/>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Message"
        android:textAppearance="@style/TextAppearance.AppCompat.Large"/>
    <EditText
        android:id="@+id/edit_text_message"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:lines="10"
        android:gravity="start|top"/>

    <Button
        android:id="@+id/button_send"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="send"/>




</LinearLayout>

Java file
package com.example.emailsendapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    private EditText mEditTextTo;
    private EditText mEditTextSubject;

    private  EditText mEditTextMessage;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mEditTextTo=findViewById(R.id.edit_text_to);
        mEditTextSubject=findViewById(R.id.edit_text_subject);
        mEditTextMessage=findViewById(R.id.edit_text_message);

        Button buttonSend = findViewById(R.id.button_send);

        buttonSend.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                sendMail();

            }
        });

    }
    private void sendMail(){
        String recipientList=mEditTextTo.getText().toString();
        String[] recipients =recipientList.split(",");
        //example@gmail.com, example2@gmail.com
        String subject =mEditTextSubject.getText().toString();
        String message =mEditTextMessage.getText().toString();

        //here now important part start here
        Intent intent =new Intent(Intent.ACTION_SEND);
        intent.putExtra(Intent.EXTRA_EMAIL,recipients);
        intent.putExtra(Intent.EXTRA_SUBJECT,subject);
        intent.putExtra(Intent.EXTRA_TEXT,message);
        //here email client
        intent.setType("message/rfc822");
        startActivity(Intent.createChooser(intent,"Choose an email client"));

        //this below part for attachment

       // Uri attachmentUri = Uri.parse("file:///storage/emulated/0/Download/myfile.pdf");
       // intent.putExtra(Intent.EXTRA_STREAM, attachmentUri);

        //startActivity(Intent.createChooser(intent, "Send email..."));
    }
}
