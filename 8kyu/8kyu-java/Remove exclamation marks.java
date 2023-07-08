class Solution {
  static String removeExclamationMarks(String s) {
    String result = "";
    
    for(String i: s.split("")){
      if(! i.equals("!")){
        result += i;
      }
    }
    return result;
  }
}
