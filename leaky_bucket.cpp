#include<iostream>
using namespace std;

int main()
{
    int no_of_queries=4;
    int input_pkt_size=4;
    int output_pkt_size=1;
    int storage=0;
    int bucket_size=10;
    int size_left;

    for (int i = 0; i < no_of_queries; i++)
    {
        size_left=bucket_size-storage;
        if(input_pkt_size<=size_left){
            storage+=input_pkt_size;
        }
        else
        {
            cout<<"Packet loss "<<input_pkt_size<<endl;
        }
        cout<<"buffer size "<<storage<<" out of "<<bucket_size<<endl;
        storage-=output_pkt_size;
        
    }
    
}