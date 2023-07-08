public static int strCount(String str, char letter) {
	int result = 0;
		    
	for (char i: str.toCharArray()){
		if (letter == i){
			result++;
		}
	}
	return result;
	}
}
