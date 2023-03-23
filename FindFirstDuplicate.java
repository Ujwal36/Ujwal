package com.TestAmazon.myPckage;

public class FindFirstDuplicate {

	public static void main(String[] args) {
		int[] nums = new int[] {3,3,6,5,4,2};
		int firstDuplicate=nums[0];
		for(int i=0;i<nums.length;i++)
		{
			int index = Math.abs(nums[i])-1;
			
			if(nums[index]<0)
			{
				firstDuplicate = Math.abs(nums[i]);
				break;
			}
			
			else {
				nums[index] = - nums[index];
			}
		}
		System.out.println(firstDuplicate);
	}

}
