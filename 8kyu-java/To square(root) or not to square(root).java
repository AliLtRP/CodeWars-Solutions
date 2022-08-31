import java.util.*;

public class Kata{
  public static int[] squareOrSquareRoot(int[] array){
    List<Integer> arr = new ArrayList<Integer>();
    
    for (int i : array){
      int y = (int) Math.sqrt(i);
      if (y*y ==i ){
        arr.add(y);
      } else arr.add(i*i);
    }
    return arr.stream().mapToInt(i -> i).toArray();
  }
}
