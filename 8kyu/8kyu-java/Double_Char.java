public class Solution{
  public static String doubleChar(String s){
    char[] arr = s.toCharArray();
    String result = "";
    
    for (char i:arr){
      result += i+""+i;  
    }
    return result;
  }
}
