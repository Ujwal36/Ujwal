package com.TestAmazon.myPckage;

public class RemoveDuplicates {
	
	
	static void removeDuplicates(int[] nums)
	{
		int[] temp = new  int[4];
		int j=0,i=0;
		
		for(i=0 ; i<nums.length-1;i++)
		{
			if(nums[i]!=nums[i+1])
			{
				temp[j++]= nums[i];
			}
		}
		
		temp[j++]= nums[i];
		
		for(j=0; j<temp.length;j++)
		{
			System.out.println(temp[j]);
		}
		
	}
	
	public static void main(String[] args) {

		int [] nums = new int[] {10,20,20,30,40,40,40};
		removeDuplicates(nums);
		
		
		
	}
	

}
