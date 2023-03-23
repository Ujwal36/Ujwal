package com.TestAmazon.myPckage;

public class LongPalInString {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		LongestPalindrome longest  = new LongestPalindrome();
		String str = longest.longest("A Nitin is ab gog boy and he is from Gadaga and speaks Malayalam ");
		System.out.println(str);
		
		
		ReturnIndicesofTarget indices = new ReturnIndicesofTarget();
		int[] index = new int[2];
		index = indices.findIndex(new int[] {1,2,6,4,5}, 11);
		for(int i: index)
		System.out.println(i);
		

	}

}
