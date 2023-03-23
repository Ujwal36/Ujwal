package com.TestAmazon.myPckage;

import java.util.LinkedHashMap;
import java.util.Stack;

public class Leader {

	public static void main(String[] args) {
		
		int num [] = new int[] {1,2,5,3,11,10,-1,0};
		
		
		Stack<Integer> s = new Stack();
		LinkedHashMap<Integer, Integer> hm= new LinkedHashMap<>();
		
		s.push(num[num.length-1]);
		hm.put(s.peek(), -1);
		
		for(int j=num.length-2; j>=0; j--)
		{
			if(num[j]<s.peek())
			{
				hm.put(num[j], s.peek());
				s.push(num[j]);
			}
			else {
				
				while(!s.empty())
				{
					
					
					if(s.peek()>num[j])
					{
						hm.put(num[j], s.peek());
						s.push(num[j]);
						break;
					}
					else
					{
						s.pop();
					}
				}
				if(s.empty()) {
					hm.put(num[j], -1);
					s.push(num[j]);
				}
				
			}
			System.out.println(hm);
			System.out.println("Stack is " + s);
			
		}
		
	//	System.out.println(hm);
		

	}

}
