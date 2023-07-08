public class Kata {
  public static String findNeedle(Object[] haystack) {
    int i = 0;
      
    while (true) {
      if (haystack[i] != null && haystack[i].equals("needle")) {
        return "found the needle at position "+ Integer.toString(i);
      }
      i++; 
    }
  }
}
