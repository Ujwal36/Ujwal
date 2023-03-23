package com.TestAmazon.myPckage;

import java.util.HashMap;
import java.util.Stack;

public class NextGreaterElement {

	public static void main(String[] args) {
		
		int[] num = new int[] {5,1,1,1,6,3,10,0,800};
		int[] output = new int[num.length];
		Stack<Integer> s = new Stack<>();
		HashMap<Integer, Integer> hm = new HashMap<>();
		
		s.push(num[0]);
		
		for(int i=1; i<num.length; i++)
		{
			if(num[i]>s.peek())
			{
				//System.out.println(s.indexOf(s.peek()));
				hm.put(s.pop(),num[i]);
				//output[i] = num[i];
			//	s.pop();
			
				while(!s.empty() && s.peek()<num[i])
				{
					//System.out.println(s.indexOf(s.peek()));
					hm.put(s.pop(),num[i]);
				//	s.pop();
				}
				s.push(num[i]);
			}
			else {
				s.push(num[i]);
			}
		}
		while(!s.empty())
		{
			hm.put(s.pop(), -1);
		}
		
		System.out.println(hm + " " + hm.size());
		
		for(int i=0; i<num.length;i++)
		{
			output[i]=hm.get(num[i]);
			System.out.println(output[i]);
		}
		
	}

}
