using System;  
using System.Collections.Generic;  
using System.Linq;  
using System.Text;  
namespace Hello_Word  
{  
   class Program  
   {  
      static void Main(string[] args)  
      {  
         int val = 5;  
         int i, j, k ;  
         for (i = 1; i <= val; i++)  
         {  
            for (j = 1; j <= val-i; j++)  
            {  
               // Console.Write("");  
            }  
            for (k = 1; k <= i; k++)  
            {  
               Console.Write("*");  
            }  
            Console.WriteLine("");  
         }  
         Console.ReadLine();  
      }  
   }  
}  
