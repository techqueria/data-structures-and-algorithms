class node{
	
	constructor(data){
		
		this.data=data;
		this.next=null;

	}
}


class LinkedList{
	
	constructor(){
		this.head=null;
	}

//Function to insert a node in the singlely linkedlist.
	insert=(data)=>{
		
		var newnode=new node(data);
		if(head===null){
			this.head=newnode;
		}

		else{
			
			var temp=this.head;
			while(temp.next!==null){
				temp=temp.next;			
			}		
				
			temp=newnode;
		}	
	}

//Function to print the singlely linkedlist.
	printList=()=>{
		var temp=this.head;
		var list;
		while(temp!==null){
			list+=temp.data+"->";
			temp=temp.next;		
		}
		list+="null";
		console.log(list);
	}

	

//Function to remove dupliicate nodes from the singlely linkedlist.
	removeDuplicates=()=>{
	
		var temp1,temp2,duplicate;
	
		temp1=this.head;
		temp2=temp1;
		while(temp1!==null || temp.next!==null){
			
			while(temp2.next!==null){
				if(temp1.data===temp2.next.data){
					duplicate=temp2.next;
					temp2.next=temp2.next.next;
					delete(duplicate);
				}
				else{
					temp2=temp2.next;				
				}			
			}
			temp1=temp1.next;
		}
	
	}

}

//main function.
/*
Linkedlist list;
list.insert(0);
list.insert(1);
list.insert(2);
list.insert(3);
list.insert(1);
list.insert(4);
list.insert(4);
console.log("Original List with DUplicates:");
list.printList();
list.removeDuplicates();
console.log("List free of duplicates:");
list.printList();
*/

