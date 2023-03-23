package com.TestAmazon.myPckage;

public class PrintDuplicatesString {

	public static void main(String[] args) {

		
		String str = "ujwal";
		//char[] charstr = str.trim().toLowerCase().toCharArray();
		//System.out.println(charstr);
		String s = "";
		
		for(int i=0; i<str.length();i++)
		{
			if(i!=str.lastIndexOf(str.charAt(i)) && s.indexOf(str.charAt(i)) < 0)
			{
				
				s = s+ str.charAt(i);
			}
		}
		
		System.out.println(s);
	}

}
