package Test;

import java.util.Scanner;

public class IntegerPalindrome {
	
	public static Boolean isPalindrome(int number)
	{
		int reversedNumber = 0;
		int num= number;
		
		while(num>0)
		{
			reversedNumber = reversedNumber * 10;
			reversedNumber += (num%10);
			num = num/10;
		}
		
		
		if(reversedNumber == number)
			return true;
		
		else return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("Enter an Integer");
		Scanner sc = new Scanner(System.in);
		
		int number = sc.nextInt();
		
		System.out.println(isPalindrome(number));
		
				
		

	}

	

}
