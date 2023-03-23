package com.TestAmazon.myPckage;

public class DecimalToBinary {

	public static void main(String[] args) {
		
		int d = 7;
		
		String b = "";
		int r=0;
		while(d!=0)
		{
			r= d%2;
			b = r+b;
			d=d/2;
			
		}
		
		System.out.println(b);
	}

}
