package com.TestAmazon.myPckage;

public class Count1s {

	public static void main(String[] args) {
		
		String s = "10101110101";
		
		int i =0 ;
		int j=s.length()-1;
		int count =0;
		while(i<j)
		{
			if(s.charAt(i)=='1')
			{
				count ++;
			}
			if(s.charAt(j)=='1')
			{
				count++;
			}
			i++;j--;
			
		}
		if(i==j && s.charAt(i)=='1') count ++;
		System.out.println(count);
		
		

	}

}
