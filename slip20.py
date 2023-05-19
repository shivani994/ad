//slip20
//q1.create Android Program to Change The image on the Screen
Xml file
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:orientation="vertical"
    android:gravity="center">
    <Button
        android:id="@+id/changeImageButton"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click here to channge image"
        android:layout_marginBottom="100dp"
        android:gravity="center"/>
    <ImageView
        android:id="@+id/image_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:src="@drawable/image1"/>

Java file

package com.example.sliceapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
    private ImageView i1;  //create variable for ImageView
    //  private int[] //image={R.drawable.image,R.drawable.nature_image,R.drawable.sun_sine_img};
    // private  int imageIndex=0; //declare here give private specifier
    //here we create array of images that you want to display in our app. and strore this images in app resource i.e res->drawable
    int[] image = {R.drawable.image1, R.drawable.image2, R.drawable.image3};
    int imageIndex = 0;     // set counter variable equal to 0

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // here initialize the ImageView variable by findViewById()
        i1 = findViewById(R.id.image_view);
        //here we create array of images that you want to display in our app. and strore this images in app resource i.e res->drawable
        int[] image = {R.drawable.image1, R.drawable.image2, R.drawable.image3};



        Button b1 = findViewById(R.id.changeImageButton);  //button will change image
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                changeImg();   //here we call changeImg() merhod
            }
        });
    }
        private void changeImg(){          
        imageIndex = (imageIndex + 1) % image.length;  
        i1.setImageResource(image[imageIndex]);
    }

}

(OR) MAM 


Xml file
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <LinearLayout

        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:paddingBottom="40px"
        android:weightSum="2">

        <RadioGroup
            android:id="@+id/rg"
            android:layout_width="wrap_content"
            android:layout_height="match_parent"
            android:orientation="vertical">

            <RadioButton
                android:id="@+id/rb1"
                 android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Image 1"/>


            <RadioButton
                android:id="@+id/rb2"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Image 2"/>

            <RadioButton
                android:id="@+id/rb3"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="Image 3"/>




        </RadioGroup>


    </LinearLayout>
    <ImageView
        android:id="@+id/imageView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:src="@drawable/image1"/>


</RelativeLayout>
Java file

package com.example.imageapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.RadioGroup;

public class MainActivity extends AppCompatActivity implements RadioGroup.OnCheckedChangeListener {
    RadioGroup group1;

    ImageView img;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        group1 = (RadioGroup) findViewById(R.id.rg);
        group1.setOnCheckedChangeListener((RadioGroup.OnCheckedChangeListener)this);
        img = (ImageView) findViewById(R.id.imageView);

    }

    @Override
    public void onCheckedChanged(RadioGroup radioGroup, int i) {
        switch (i) {
            case R.id.rb1:
                img.setImageResource(R.drawable.image1);
                break;

            case R.id.rb2:
                img.setImageResource(R.drawable.image2);
                break;

            case R.id.rb3:
                img.setImageResource(R.drawable.image3);
                break;

            default:
                break;

        }


    }
}






Q.2. Demostrate Array Adapter using List View display list of Country
XML file

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"

    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".S20OrQ1MenuActivity">

   <ListView
       android:id="@+id/country_list"
       android:layout_width="match_parent"
       android:layout_height="492dp" />

</LinearLayout>


//JAVA File

package com.example.sliceapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;
// array adpater with list view

public class S20OrQ1MenuActivity extends AppCompatActivity {
     ListView countryListView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_s20_or_q1_menu);

        //Initialize the ListView
        countryListView=findViewById(R.id.country_list);
         ArrayList<String>country=new ArrayList<>();
        country.add("india");
        country.add("china");
        country.add("America");


        //Creat an array of countires
        ArrayAdapter<String>arrayAdapter=new ArrayAdapter<>(this,android.R.layout.simple_list_item_1,country);
       // array adapter h vo android ki class hoti h jo ki jo madat kari h java ke array adapte karne m ya niki agar android ko java ke array list view me dikhane h to usko array Adapter class ka estmal karna padega
        countryListView.setAdapter(arrayAdapter);
    }

}

