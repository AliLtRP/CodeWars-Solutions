public class Kata{
  public static int squareSum(int[] n){ 
   int result = 0;
    
   for(int i:n){
    result += Math.pow(i, 2);
   }
    
  return result;
 }
}
