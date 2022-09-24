package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void submitData(View view)
    {
        EditText textFirstName = (EditText) findViewById(R.id.editTextTextFirstName);
        String firstName = textFirstName.getText().toString();
        EditText textLastName = (EditText) findViewById(R.id.editTextTextLastName);
        String lastName = textLastName.getText().toString();
        Intent intent = new Intent(this, submission.class);
        intent.putExtra("firstName", firstName);
        intent.putExtra("lastName", lastName);
        startActivity(intent);


    }

    public void sendMessage(View view) {
        Intent intent = new Intent(this, MainActivity202.class);
        startActivity(intent);
    }


}