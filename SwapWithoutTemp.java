package Test;

public class SwapWithoutTemp {
	
	 int a = 100;  int b = 0;
	
	static void Swap(SwapWithoutTemp obj)
	{
		obj.a= obj.a+obj.b;
		obj.b= obj.a - obj.b;
		obj.a = obj.a-obj.b;
		
	}
	
	public static void main(String[] args) {
		SwapWithoutTemp obj = new SwapWithoutTemp();
		
		Swap(obj);
		
		System.out.print(obj.a + " " + obj.b);
		
	}
	

}
