package Test;

import java.util.Scanner;

public class Palindrome {
	//static Boolean IsPal=true;
	
	public static Boolean isPalindrome(String str)
	{
		int i =0 ;
		int j = str.length()-1;
		
		while(i<j)
		{
			if(str.charAt(i)==str.charAt(j))
			{
				i++; j--;
			}
			else {
				return false;
				//break;
				
			}
		}
		return true;
		
		
		
	}
	
	
	public static void main(String[] args)
	{
		
		System.out.println("Enter a string");
		
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		Boolean IsPal = null;
		
		if(str!=null) {
			 IsPal = isPalindrome(str);
		}
				
		System.out.println("It is palindrome =" + IsPal);
		
	}
	
	

}
