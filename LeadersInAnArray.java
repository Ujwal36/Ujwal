package com.TestAmazon.myPckage;

import java.util.Stack;

public class LeadersInAnArray {

	public static void main(String[] args) {
		int[] nums = new int[] {2,5,-11,6,3,1};
		
		Stack<Integer> s = new Stack<>();
		s.push(nums[nums.length-1]);
		for(int j = nums.length-2;j>=0;j--)
		{
			if(nums[j] > s.peek())
			{
				s.push(nums[j]);
			}
		}
		System.out.println(s);
		
	}

}
