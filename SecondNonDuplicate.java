package com.TestAmazon.myPckage;

import java.util.LinkedHashMap;
import java.util.Map.Entry;

public class SecondNonDuplicate {
	public static void main(String[] args) {
		
		String str = "Automation";
		int count = 0;
		
		for(int i=0; i< str.length();i++)
		{
			if(str.indexOf(str.toLowerCase().charAt(i))== str.toLowerCase().lastIndexOf(str.charAt(i)))
			{
				
				
				count ++;
				if(count ==2)
					System.out.println(str.charAt(i));
			}
		}
		
		LinkedHashMap<Character, Integer > hm = new LinkedHashMap<>();
		
		for(int i=0; i< str.length();i++)
		{
			if(hm.containsKey(str.toLowerCase().charAt(i)))
			{
				hm.put(str.toLowerCase().charAt(i), hm.get(str.toLowerCase().charAt(i))+1);
				
			}
			else {
				hm.put(str.toLowerCase().charAt(i), 1);
			}
		}
		count =0;
		System.out.println(hm);
		
		for(Entry m: hm.entrySet())
		{
			if((m.getValue().toString()).equals("1"))
				count ++;
			if(count ==2)
				System.out.println(m.getKey());
		}
		
		
	}

}
