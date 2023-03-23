package com.TestAmazon.myPckage;

public class MaxProductFromSubArray {

	public static void main(String[] args) {
		//Kadence Algorithm
		
		int[] nums = new int[] {1,3,-11,4,-2,6,6};
		
		int current = nums[0];
		int max = nums[0];
		
		for(int i=1;i<nums.length;i++)
		{
			current = current*nums[i] < nums[i] ? nums[i] : current*nums[i];
			max = current > max ? current: max;
					
		}
		System.out.println(max);
		
	}

}
