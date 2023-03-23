package com.TestAmazon.myPckage;

public class LongestPalindrome {
	
	public String longest(String str)
	{
		
		
		String[] s = str.split(" ");
		
		String longest_string = null;
		
		int longest_string_length = 0;
		
		for(String string : s)
		{
			
			int i=0;
			int j = string.length()-1;
			
			
			if(string.length()>longest_string_length)
			{
				
				while(i<=j)
				{
					if(string.toLowerCase().charAt(i)== string.toLowerCase().charAt(j))
					{
						i++;j--;
						
					}
					else
					{
						break;
						
					}
					
				}
				if(i>j)
				{
					longest_string=string;
					longest_string_length = string.length();
					System.out.println("Longest string: "+ longest_string);
				}
				
				
				
			
			}
			
			
		}
		if(longest_string == null)
		{
			return "No palindromes exists.....!!!";
		}
		return longest_string;
		
		
	}
	
	
	

}
