package com.TestAmazon.myPckage;

public class BitsSorting {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "0101001011001000010111010101000011010111010101010110010110";
		char [] bitString = str.toCharArray();
		System.out.println(bitString);
		int j=str.length()-1;
		int i=0;
		while(i<j) {
			if(bitString[i]=='0' && bitString[j]=='0')
			{
				i++;
			}
			else if(bitString[i]=='0' && bitString[j]=='1')
			{
				i++;j--;
			}
			else if(bitString[i]=='1' && bitString[j]=='0')
			{
				bitString[i]= '0';
				bitString[j] = '1';
				i++;j--;	
			}
			else 
			{
				j--;
			}
		}	
		System.out.println(bitString);
	
	}

}
