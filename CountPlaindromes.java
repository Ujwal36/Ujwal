package com.TestAmazon.myPckage;

public class CountPlaindromes {
	static int prev_Palindromic_str_length =0;
	static String prev_Palindromic_string = null;
	static Boolean isPalindrome(String str) {
		
		
		
		
		
		str = str.toLowerCase();
		int i=0;
		
		int j=str.length()-1;
		
		// Need to check logic for longest length
		
		if(j+1 > prev_Palindromic_str_length)
		{
			while(i<j)
			{
				if(str.charAt(i)==str.charAt(j)) {
					i++;
					j--;
				}
				else {
					return false;
				}
			}
			prev_Palindromic_str_length = str.length();
			prev_Palindromic_string = str;
			return true;
		}
		
		else
		{
			return false;
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String s = " Nitin is a good boy and he is from Gadag and speaks Malayalam 13108080131";
		
		
		String str[] = s.split(" ");
		int count =0;
		for (int i=0 ;i<str.length;i++)
		{
			if(isPalindrome(str[i]))
				count ++;

		}
		System.out.println(prev_Palindromic_string);
		System.out.println(count);
	}


}
