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
	insert(data){
		
		var newnode=new node(data);
		if(this.head==null){
			this.head=newnode;
		}

		else{
			
			var temp=this.head;
			while(temp.next){
				temp=temp.next;			
			}		
				
			temp.next=newnode;
		}	
	}

//Function to print the singlely linkedlist.
	printList(){
		var temp=this.head;
		var list="";
		while(temp){
			list+=temp.data+"->";
			temp=temp.next;		
		}
		list+="null";
		console.log(list);
	}

	

//Function to remove dupliicate nodes from the singlely linkedlist.
	removeDuplicates(){
	
		var temp1,temp2;
	
		temp1=this.head;
		while(temp1 && temp1.next){
			temp2=temp1;
			while(temp2.next){
				if(temp1.data==temp2.next.data){
					temp2.next=temp2.next.next;
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
/*var list_1=new LinkedList();
list_1.insert(0);
list_1.insert(1);
list_1.insert(2);
list_1.insert(3);
list_1.insert(1);
list_1.insert(4);
list_1.insert(4);
console.log("Original List with Duplicates:");
list_1.printList();
list_1.removeDuplicates();
console.log("New List free of duplicates:");
list_1.printList();
*/
