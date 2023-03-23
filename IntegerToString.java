package Test;

import java.util.ArrayList;
import java.util.List;

public class IntegerToString {

	

	public static void main(String[] ujwal) {
		// TODO Auto-generated method stub
		
		String str1 = "Ujwal is a good boy";
		List<Integer> li = new ArrayList<Integer>();
		
		li.add(1);
		li.add(1001);
		li.add(0);
		li.add(123);
		li.add(-1);
		
		
		for(int i : li)
		{
			String str = Integer.toString(i); 
			System.out.println(str);
			
			
		
			
			System.out.println(str.startsWith("1"));
			
			
			if(str.indexOf('1')==0)
				System.out.
				println(i);
			
		
		}
		
		Integer[] st = {1,123};
		main(st);
		
		
		
	}
	
public static void main(Integer[] args) {
		
		System.out.print("Inside overloaded main");

	}

}

	
	
	
	
