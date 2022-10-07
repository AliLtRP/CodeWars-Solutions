public class Bio {
  public String dnaToRna(String dna) {
    String result = "";
    char[] arr = dna.toCharArray();
    
    for(char i:arr){
      result += i == 'T' ? "U": i;
    }
    return result;
  } 
}
