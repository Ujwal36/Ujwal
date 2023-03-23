package Test;

import java.util.HashMap;

public class CharacterOccurance {

	
	static void Occurance(String str)
	{
		HashMap<Character, Integer> charsCount = new HashMap<>();
		
		for (int i =0 ; i< str.length();i++)
		{
			char c = str.charAt(i);
			
			if(charsCount.containsKey(c))
			{
				charsCount.put(c, charsCount.get(c)+1);
			}
			else {
				charsCount.put(c,1);
			}
		
		}
		
		System.out.print(charsCount);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		String str = "@12344#$#$";
		
		Occurance(str);
		
		

	}

}
