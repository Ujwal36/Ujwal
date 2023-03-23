package Test;

public class SwapStrings {
	
	public static String str1="null";
	public static String str2="jsqkd";
	
	public static void swap()
	{
		
		int len1 = str1.length();
		int len2 = str2.length();
		str1 = str1 + str2;
		str2 = str1.substring(0,len1);
		str1= str1 .substring(len1);
		
	}
	
	public static void main(String[] args)
	{
		swap();
		System.out.println(str1);
		System.out.println(str2);
	}
}
