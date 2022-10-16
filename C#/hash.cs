using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;
using System.Security.Cryptography;
using System.Text;

namespace Desktop3
{
    internal class MyClass
    {
        public static string makeHash(string text) 
        {
            return string.Join("", MD5.Create().ComputeHash(Encoding.UTF8.GetBytes(text)).Select(s => s.ToString("x2")));
        }
    }
}
