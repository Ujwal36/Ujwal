package Test;

public class StringPalindrome {
	
	public static Boolean isPalindrome(String str)
	{
		int i =0, j= str.length()-1;
		
		// To check case sensitive.
		str=str.toLowerCase();
		
		System.out.println("String is :" + str);
		while(i<j)
		{
			if(str.charAt(i)==str.charAt(j))
			{
				i++;j--;
			}
			else {
				break;
			}
		}
		
		if(i>=j)
			return true;
		else
			return false;
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "My name is nitin and I speak Malayalam 1441";
		
		String[] list = str.split(" ");
		StringBuffer buff = new StringBuffer();
		for(String s: list)
		{
			Boolean palindrome = false;
			palindrome = isPalindrome(s);
			if(palindrome)
			{
				
				buff.append(s);
				buff.append(" ");
			}
		}
		
		System.out.print(buff);

	}

}
