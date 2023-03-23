package Test;

import java.util.HashMap;
import java.util.Map;

public class SumofTwoIntegersTarget {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		int[] array = new int[]{3,3,3,3,4};
		
		int target = 7;
		
		
		Map<Integer, Integer> map = new HashMap<>();
		
		for(int i=0; i<array.length; i++)
		{
			int compliment = target - array[i];
			
			if(map.containsKey(compliment))
			{
				System.out.print(i + " " + map.get(compliment));
				break;
			}
			else
			{
				map.put(array[i], i);
			}
		}
		
		
	}

}
