package com.TestAmazon.myPckage;

import java.util.HashMap;

public class Test {
	
	static String encoding(String str)
	{
		String s="";
		int count =1;
		for(int i=0;i<str.length()-1;i++)
		{
			if(str.charAt(i)==str.charAt(i+1))
			{
				count ++;
				
			}
			else {
				s=s+str.charAt(i)+count;
				count =1;
			}
			
		}
		//To write the last one

		s= s+str.charAt(str.length()-1)+count;
		return s;
	}

	public static void main(String[] args) {

		String str = "aaaabbcaa";
		
		String encoded_str = encoding(str);
		System.out.println(encoded_str);
	}

}
