package Test;

import java.util.Stack;

public class StackOperation {

	public static Stack<Integer> numberValue(int i)
    {
        long number =0L;
    
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(i);
        return stack;
    }
	
        
        
        
        
        
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Stack<Integer> stack1;
		Stack<Integer> stack2;
		stack1 = numberValue(1);
		stack2 = numberValue(2);
		
		System.out.println(stack1);
		System.out.println(stack2);

	}

}
