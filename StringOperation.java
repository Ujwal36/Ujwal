package Test;

public class StringOperation {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String str = "@#$@#              $#@$123";
		
		StringBuffer buff = new StringBuffer();
		
		
		
		int j=0;
		
		for(int i=str.length();i>0;i--)
		{
			char c = str.charAt(i-1);
			buff.insert(j, c);
			
			j++;
			
			
		}
		System.out.print(buff);
		
	}

}
