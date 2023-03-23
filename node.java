package com.TestAmazon.myPckage;

	public class node
	{
		int key;
		node next;
		
		
		
		public  node insert(node n,int e)
		{
			
			node newnode = new node();
			node head;
			if(n==null)
			{
				System.out.println("First element");
				newnode.key =e;
				newnode.next=null;
				
				head = newnode;
				
			}
			else
			{
				
				head=n;
				while(n.next!=null)
				{
					n=n.next;
				}
				newnode.key=e;
				n.next=newnode;
				newnode.next=null;
			}
			return head;
			
		}
		
		public  void display(node n)
		{
			while(n!=null)
			{
				System.out.println(n.key);
				n=n.next;
			}
			
			
		}
	}


