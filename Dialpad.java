package Test;

import java.util.HashMap;

public class Dialpad {

	
	static void mapNumbers(String str)
	{
		HashMap<Character, Integer> dialpadmap = new HashMap<>();
		char c = 'A';
		
		for (int i =0 ; i< 26;i++)
		{
			
			
			if(i>=0 && i<=2)
			dialpadmap.put(c, 2);
			
			else if(i>=3 && i<=5)
				dialpadmap.put(c, 3);
			
			else if(i>=6 && i<=8)
				dialpadmap.put(c, 4);
			
			else if(i>=9 && i<=11)
				dialpadmap.put(c, 5);
			
			else if(i>=12 && i<=14)
				dialpadmap.put(c, 6);
			
			else if(i>=15 && i<=18)
				dialpadmap.put(c, 7);
			
			else if(i>=19 && i<=21)
				dialpadmap.put(c, 8);
			
			else if(i>=22 && i<=25)
				dialpadmap.put(c, 9);
			
			
			c++;
		
		}
		
		System.out.println(dialpadmap);
		StringBuffer buff = new StringBuffer();
		
		for (int i =0 ; i< str.length();i++)
		{
			
			
			buff.insert(i,Integer.toString(dialpadmap.get(str.toUpperCase().charAt(i))));
			
		
		}

		System.out.println(buff);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		String str = "ujwal";
		
		mapNumbers(str);
		
		

	}

}
