package Test;

import java.util.HashMap;

public class RomanToInteger {

public static int romanToInt(String s) {
        
	HashMap<Character,Integer> map = new HashMap<>();
    
    map.put('I',1);
    map.put('V',5);
    map.put('X',10);
    map.put('L',50);
    map.put('C', 100);
    map.put('D',500);
    map.put('M',1000);
    
    int integer=0;
    
    for(int i=0;i<s.length();i++)
    {
        // Additional logic for 4x and 9x.
        
        //if(map.get(s.charAt(i))+map.get(s.charAt(i+1)) == 6)
        
        char c = s.charAt(i);
        int current = map.get(c); int next=0;
        if(i!=s.length()-1)
         next = map.get(s.charAt(i+1));
        
        if(current < next)
        {
            
        
               switch(current + next)
               {
                   case 6:
                   case 11:
                   case 60:
                   case 110:
                   case 600:
                   case 1100: integer = integer + (next-current); i++;
                   //default: integer = integer + map.get(c);
               }
        }
        else{
            integer = integer + map.get(c);
        }
        
        
    }
    return integer;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "LVIII";
		int integer = romanToInt(str);
		
		System.out.println(integer);
		
	}

}
