package com.TestAmazon.myPckage;

public class SecondLargestElement {

	public static void main(String[] args) {
		
		int [] num = new int[] {100,100,100,3,1,2};
		
		
		int first=Integer.MIN_VALUE,second=Integer.MIN_VALUE;
		for(int i=0; i< num.length;i++) {
			
			if(num.length>1)
			{
				
				if(num[i]> first)
				{
					second = first;
					first = num[i];
					
				}
				else if(num[i]> second && num[i] != first) 
				{
					second = num[i];
				}
				
				
			}
			else {
				System.out.println("There is no second largest");
			}
			
			
		}
		System.out.println(second);
		
		
		
	}

}
