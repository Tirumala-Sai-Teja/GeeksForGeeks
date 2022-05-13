class Solution{
public:	
	// Program for zig-zag conversion of array
	void zigZag(int arr[], int n) {
	    int i,t;
	    for(i=0;i<n-1;i++){
	        if(i%2==0 && arr[i]>arr[i+1]){
	            t=arr[i];
	            arr[i]=arr[i+1];
	            arr[i+1]=t;
	        }
	        else if(i%2!=0 && arr[i]<arr[i+1]){
	             t=arr[i];
	            arr[i]=arr[i+1];
	            arr[i+1]=t;
	        }
	    }

	    
	}
};
