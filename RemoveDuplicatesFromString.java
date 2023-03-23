package com.TestAmazon.myPckage;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RemoveDuplicatesFromString {
	public static String RemoveDuplicates(String string)
	
	{
		String s = "";
		for(int i=0;i<string.length();i++)
		{
			if(!s.toLowerCase().contains(String.valueOf(string.toLowerCase().charAt(i))))
			{
				s = s+string.charAt(i);
			}
		}
		
		return s;
		
		
		
	}
	
public static String RemoveDuplicates_Index(String string)
	
	{
		String s = "";
		for(int i=0;i<string.length();i++)
		{
			if(s.indexOf(string.charAt(i))<0)
			{
				s=s+string.charAt(i);
			}
		}
		
		return s;
	}

//Using List

public static String RemoveDuplicatesList(String string)
{
	List<Character> list = new ArrayList<Character>();
	
	for(int i=0;i<string.length();i++)
	{
		if(!list.contains(string.charAt(i)))
		{
			list.add(string.charAt(i));
		}
	}
	
	String s = list.toString();
	System.out.println(s);
	return s;
}

	public static void main(String[] args) {
		
		String str = "Geeks For Geeks";
		System.out.println(RemoveDuplicates(str));
		System.out.println(RemoveDuplicates_Index(str));
		System.out.println(RemoveDuplicatesList(str));
		

	}

}
