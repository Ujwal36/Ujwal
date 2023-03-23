package com.TestAmazon.myPckage;

import java.util.HashMap;

public class TestHitachi {

	public static void main(String[] args) {
		
		String str = "my name is ankit";
		
		
		// My Name Is Ankit
		int[] arr = new int[] {10,20,30,40,50};

		String output = "";
		int first = Integer.MIN_VALUE;
		int second = first;
		
		for(int i=0;i<arr.length;i++)
		{
			if(arr[i] > first) {
				second = first;
				first = arr[i];
				
			}
			else if(arr[i] > second && arr[i] != first){
				second= arr[i];
			}
		}
		
		System.out.println(second);
		
		String[] s = str.split(" ");
		
		for(String string  :s)
		{
			output = output+ string.substring(0,1).toUpperCase() + string.substring(1)+ " ";
		}
		
		
		System.out.println(output);

		
		 output = "";
		
		// str--> ankit is name my
		
		
		for(int i=s.length-1 ; i>=0; i--)
		{
			output = output + s[i] + " ";
		}
		
		
		System.out.println(output);
		
		// to reverse a given string
		
		
		output ="";
		
		for(int i = str.length()-1; i>=0 ; i--)
		{
			output += str.charAt(i);
		}
		System.out.println(output);
		
		String string = "Ankit Rohit Suman Ujwal anjum prajwal Anik Harshita Deshna Sankit Anjan Arom";
		
		// Count the number of names starting with A
		
		
		s = string.split(" ");
		int count =0;
		for (String ss : s)
		{
			
				if(ss.substring(0, 1).equalsIgnoreCase("A"))
			{
					
				System.out.println(ss);
				count++;
			}
			
		}
		System.out.println(count);
		
		// 10, 20, 30 ,40 ,50
		// 50, 10, 20,30,40
		
		
		
		int i=0 , j=arr.length-1;
		
		
		while(i<j)
		{
			int temp = arr[i];
			arr[i++] = arr[j];
			arr[j] = temp;
			
			
		}
		for( i=0 ; i< arr.length;i++)
		System.out.println(arr[i]);
			
	}

}
