package com.TestAmazon.myPckage;

public class CountMaxOccurance {

	public static void main(String[] args) {
		
		String str = "gulbargag";
		
		int[] alpha = new int[26];
		
		for(int i=0;i<str.length();i++)
		{
			alpha[str.charAt(i) - 'a']++;
		}
		int max = 0;
		int pos =0;
		for(int i=0;i<alpha.length;i++)
		{
			
			if(alpha[i]>max)
			{
				max=alpha[i];
				pos=i;
			}
			
		}
		System.out.println(max +" " + (char)(pos+'a'));

	}

}
