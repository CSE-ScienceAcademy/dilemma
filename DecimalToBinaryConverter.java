public class DecimalToBinaryConverter {
 public static void main(String[] args) {
  int decimalNumber = 97;
  String binaryNumber = "";
  
   while (decimalNumber != 0) 
   {
    if (binaryNumber.length() % 5 == 0)
     binaryNumber = " " + binaryNumber;
   
    binaryNumber = (decimalNumber % 2) + binaryNumber;
    decimalNumber /= 2;
   }
   System.out.println("Binary: " + binaryNumber);
  }
 }
