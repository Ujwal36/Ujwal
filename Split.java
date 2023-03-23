package com.TestAmazon.myPckage;

public class Split {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "Hello World";
		
		String[] s = str.split(" ");
		
		for(String string : s)
		System.out.println(string.length());

	}

}
