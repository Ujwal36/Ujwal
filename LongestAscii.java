package com.TestAmazon.myPckage;

public class LongestAscii {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "UZWAL am Amazonian";
		int longest = str.charAt(0);
		for(int i=1;i<str.length();i++)
		{
			int Ascii_len = str.charAt(i);
			if(Ascii_len > longest)
			{
				longest =Ascii_len;
			}
		}
			System.out.println((char)(longest));
	}

}
