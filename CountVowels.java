package Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;

public class CountVowels {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "I am a Good BOy";
		int count = 0;
		//HashSet<Character> hash = new HashSet<>();
		LinkedHashMap <Character, Integer> hash = new LinkedHashMap<>();
		
		
		hash.put('a', 0);
		hash.put('e', 0);
		hash.put('i', 0);
		hash.put('o', 0);
		hash.put('u', 0);
		
		for(int i=0;i<str.length();i++)		
		{
			char ch = str.toLowerCase().charAt(i);
					
			if(hash.containsKey(ch))
			{
				//count ++;
				//System.out.println(str.charAt(i));
				hash.put(ch, hash.get(ch)+1);
				
				
			}
		}
		System.out.println(hash);
	}

}


