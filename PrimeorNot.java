package  Test;

public class PrimeorNot
{
	
	public static void main(String args[])
	{
		int number = -0;
		Boolean flag = true;
		
		if (number == 0 || number ==1 || number < 0)
		{
			flag = false;
			System.out.println(" Not a prime number ...");
		}
		for (int i=2 ; i<=number/2; i++)
		{
			
			if(number % i == 0)
			{
				System.out.println(" Not a prime number ... Exiting");
				flag = false;
				break;
			}
		}
		if(flag)
			
		System.out.println(" This is prime number");
			
	}
	
}