package Test;

public class sumOfNumbers{
	
	public static void main(String args[])
	{
		
		int number = 999;
		int NewNumber = number ;
		int sum =0;
		
		while( number != 0) {
			
			NewNumber = number%10;
			sum = sum + NewNumber;
			number = number/10;
			if(number == 0 && sum/10 != 0) {
				number = sum;
				sum=0;
			}
			
			
		}
		
		
		System.out.println(sum);
		
	}
}