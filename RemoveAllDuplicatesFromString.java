package com.TestAmazon.myPckage;

import java.util.Arrays;

public class RemoveAllDuplicatesFromString {

	public static void main(String[] args) {
		
		String str = "automation";
		String s= "";
		
		for(int i=0;i<str.length();i++)
		{
			if(str.indexOf(str.charAt(i)) == str.lastIndexOf(str.charAt(i)) && s.indexOf(str.charAt(i))<0)
			{
				s+=str.charAt(i);
			}
			
		}
		System.out.println(s);
		
		
		
		// To count the number of non-duplicate elements
		int count =0;
		
		for(int i=0;i<str.length();i++)
		{
			if(str.indexOf(str.charAt(i)) == str.lastIndexOf(str.charAt(i)))
			{
				count ++;
			}
			
		}
		System.out.println(count);
		
		// To count the number of duplicate elements
		
				 count =0;
				 s ="";
				
				for(int i=0;i<str.length();i++)
				{
					if(str.indexOf(str.charAt(i)) != str.lastIndexOf(str.charAt(i)) && s.indexOf(str.charAt(i))<0)
					{
						s+=str.charAt(i);
					}
					
				}
				System.out.println(s.length());
				
				
				System.out.println("To reverse a string");
				int j=str.length()-1;
				int i=0;
				char[] string = str.toCharArray();
				while(i<j)
				{
					// Swap 2 chars
					
					char temp = string[i];
					string[i++]=string[j];
					string[j--]=temp;

				}
				
				String a = String.valueOf(string);
				System.out.println(a);

	}

}
