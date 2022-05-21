# include <iostream>

void hanoi (int n , char from , char to , char aux ) 
{
if (n == 1)
{
std::cout << "Move disk 1 from " << from << " to " << to << std::endl;
}
else 
{
hanoi (n-1 , from , aux , to );
std::cout << "Move disk " << n << " from " << from << " to " << to << std::endl; 
hanoi (n-1 , aux , to , from );
}
}
int main () 
{
std::cout << "something\n";
hanoi (3 , 'A', 'C', 'B');
return 0;
}