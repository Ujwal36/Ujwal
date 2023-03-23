package com.TestAmazon.myPckage;

public class BinaryToDecimal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		String str = "0101";
		int base =1;
		int decimal=0;
		
		for(int i=str.length()-1;i>=0;i--)
		{
			if(str.charAt(i)=='1')
			{
				decimal= decimal+ base;
				

			}
			base=base*2;
		}
		System.out.println(decimal);
	}

}
