SLIP NO 4
Q1) Create a Simple Application, that performs Arithmetic Operations. (Use constraint layout)
Activity.xml

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<TextView
android:id="@+id/textView"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="120dp"
android:text="Arithmetic Operator"
android:textAlignment="center"
android:textColor="#F60101"
android:textSize="40dp"
android:textStyle="bold"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintHorizontal_bias="1.0"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintTop_toTopOf="parent" />

<EditText
android:id="@+id/fnum"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="16dp"
android:hint="First Number"
android:inputType="number"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintHorizontal_bias="1.0"

app:layout_constraintTop_toBottomOf="@+id/textView"
/>

<EditText
android:id="@+id/snum"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="16dp"
android:hint="Second Number"
android:layout_marginLeft="30dp"
android:layout_marginRight="30dp"
android:inputType="number"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintTop_toBottomOf="@+id/fnum" />

<TextView
android:id="@+id/res"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginTop="36dp"
android:text="RESULT"
android:textSize="20dp"
android:textStyle="bold"
app:layout_constraintEnd_toEndOf="@+id/snum"
app:layout_constraintHorizontal_bias="0.097"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintTop_toBottomOf="@+id/snum" />


<Button
android:id="@+id/btn1"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginStart="48dp"
android:layout_marginTop="28dp"
android:text="ADDITION"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintHorizontal_bias="0.097"
app:layout_constraintTop_toBottomOf="@+id/res" />

<Button
android:id="@+id/btn2"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginStart="236dp"
android:layout_marginTop="28dp"
android:text="SUBSTRACTION"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintHorizontal_bias="0.097"
app:layout_constraintTop_toBottomOf="@+id/res" />

<Button
android:id="@+id/btn3"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginTop="100dp"
android:layout_marginEnd="232dp"
android:text="MULTIPLICATION"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintHorizontal_bias="0.097"
app:layout_constraintTop_toBottomOf="@+id/res" />

<Button
android:id="@+id/btn4"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:layout_marginTop="100dp"
android:layout_marginEnd="64dp"
android:text="DIVISION"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintHorizontal_bias="0.097"
app:layout_constraintTop_toBottomOf="@+id/res" />


</androidx.constraintlayout.widget.ConstraintLayout>

MainActivity.java

public class MainActivity extends AppCompatActivity {
EditText fnum;
EditText snum;
Button btn1;
Button btn2;
Button btn3;
Button btn4;
TextView res;



@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

btn1=(Button) findViewById(R.id.btn1);
btn2=(Button) findViewById(R.id.btn2);
btn3=(Button) findViewById(R.id.btn3);
btn4=(Button) findViewById(R.id.btn4);
fnum = (EditText)findViewById(R.id.fnum);
snum=(EditText)findViewById(R.id.snum);
res=(TextView)findViewById(R.id.res);


btn1.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
int n1 = Integer.parseInt(fnum.getText().toString());
int n2 = Integer.parseInt(snum.getText().toString());

int result = n1+n2;

res.setText(String.valueOf(result));

            }
        });


btn2.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
int n1 = Integer.parseInt(fnum.getText().toString());
int n2 = Integer.parseInt(snum.getText().toString());

int result = n1-n2;

res.setText(String.valueOf(result));

            }
        });

btn3.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
int n1 = Integer.parseInt(fnum.getText().toString());
int n2 = Integer.parseInt(snum.getText().toString());

int result = n1*n2;

res.setText(String.valueOf(result));

            }
        });

btn4.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View view) {
int n1 = Integer.parseInt(fnum.getText().toString());
int n2 = Integer.parseInt(snum.getText().toString());

int result = n1/n2;

res.setText(String.valueOf(result));

            }
        });
    }
}

Q2. Create an Android Application that sends the Notification on click of the button and displays the notification message on the second activity.

1)Xml file
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".MainActivity">

<TextView
android:id="@+id/textView"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="184dp"
android:text="NOTIFICATION"
android:textAlignment="center"
android:textSize="20dp"
android:textStyle="bold"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintHorizontal_bias="0.0"
app:layout_constraintStart_toStartOf="parent"
app:layout_constraintTop_toTopOf="parent" />

<Button
android:id="@+id/btn"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="280dp"
android:text="NOTIFY"
android:textSize="20dp"
android:textStyle="bold"
android:layout_marginRight="40dp"
android:layout_marginLeft="40dp"
app:layout_constraintHorizontal_bias="0.0"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintTop_toBottomOf="@+id/textView"
/>

</androidx.constraintlayout.widget.ConstraintLayout>

Main .java
package com.example.notification;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

final String CHANNEL_ID = "Sanju_Ki_Pathshala";
Button btn;
NotificationManagerCompat nNotificationCompat;
NotificationManagerCompat nNotificationManagerCompat;

@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        createNotificationChannel();

btn = (Button) findViewById(R.id.btn);

btn.setOnClickListener(this);
nNotificationManagerCompat = NotificationManagerCompat.from(MainActivity.this);

    }

@Override
public void onClick(View view) {
        createNotificationManagerCompat(getString(R.string.app_name), getString(R.string.title), 1);
    }


private void createNotificationManagerCompat(String title, String msg, int notificationId) {
        title = "Notification Done";
        msg = "This is Done Notification";

nNotificationManagerCompat.cancelAll();

Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.baseline_notifications_active_24);

Intent intent = new Intent(MainActivity.this, Activity2.class);

PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, 0);

Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setSmallIcon(R.drawable.baseline_notifications_active_24)
                .setContentTitle(title)
                .setContentText(msg)
                .setPriority(NotificationCompat.PRIORITY_DEFAULT)

                .setContentIntent(pendingIntent)

                .setAutoCancel(true)
                .build();


if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED) {
// TODO: Consider calling
//    ActivityCompat#requestPermissions
// here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.
return;
        }
nNotificationManagerCompat.notify(notificationId, notification);
    }
private void createNotificationChannel(){
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P){
CharSequence name = "Sanju_Ki_Pathshala";

String desc = "This is for VIP";

int imp = NotificationManager.IMPORTANCE_DEFAULT;

NotificationChannel Channel = new NotificationChannel(CHANNEL_ID,name,imp);

Channel.setDescription(desc);

NotificationManager notificationManager = getSystemService(NotificationManager.class);
notificationManager.createNotificationChannel(Channel);
        }
    }


}

create 2nd activity   activity.xml

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="match_parent"
android:layout_height="match_parent"
tools:context=".Activity2">

<TextView
android:id="@+id/txt"
android:layout_width="match_parent"
android:layout_height="wrap_content"
android:layout_marginTop="268dp"
android:text="Demo"
android:textAlignment="center"
android:textSize="30dp"
android:textStyle="bold"
app:layout_constraintEnd_toEndOf="parent"
app:layout_constraintTop_toTopOf="parent"
/>

</androidx.constraintlayout.widget.ConstraintLayout>

Java->new class ->Receive.java

package com.example.notification;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

import androidx.core.app.NotificationManagerCompat;

public class Recever extends BroadcastReceiver {
@Override
public void onReceive(Context context, Intent intent) {
if(intent != null){
int id = intent.getIntExtra("id",0);
NotificationManagerCompat notificationManagerCompat = NotificationManagerCompat.from(context);

notificationManagerCompat.cancel(id);
        }
    }
}

res->value->string.xml
<resources>
<string name="app_name">Notify</string>
<string name="title">Notification</string>
</resources>


