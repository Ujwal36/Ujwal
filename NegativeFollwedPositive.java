package com.TestAmazon.myPckage;

import java.util.Arrays;

public class NegativeFollwedPositive {

	public static void main(String[] args) {
		
		int nums[] = new int[] {0,-1,2,-999,300,4,-10};
		
		int i=0;
		int j=nums.length-1;
		
		while(i<j)
		{
			if(nums[i]<0 && nums[j]>=0)
			{
				i++;j--;
			}
			else if(nums[i]<0 && nums[j]<0)
			{
				i++;
			}
			else if(nums[i]>=0 && nums[j]<0)
			{
				int temp = nums[i];
				nums[i]=nums[j];
				nums[j]=temp;
			}
			else {
				j--;
			}
		}
		System.out.println(Arrays.toString(nums));

	}

}
