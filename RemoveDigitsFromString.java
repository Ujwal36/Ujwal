package Test;

public class RemoveDigitsFromString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String str = "Ujwal36k@gmail.com/06-04-1992";
		
		
		StringBuffer buff = new StringBuffer();
		
		for(int i=0; i<str.length();i++)
		{
			char c =str.charAt(i);
			int j = c;
			//System.out.println(j);
			if(j>=48 && j<=57)
			{
				//buff.append(c);
				continue;
			}
			else {
				buff.append(c);
			}
		}
		System.out.println(buff);

}
}
