import java.util.Scanner;

public class FizzMain {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		System.out.println("Please enter a number.");
		int count;
		count = in.nextInt();
			
		
		}

	// constants for multiples of 3,5,15
	//for easy changing of the multiples for future use
	
	public static final int Fizz =3;
	public static final int Buzz = 5;
	public static final int FizzBuzz= 15;
	
	
	public static String NumOutput(int count) {
		
		//moved to the top due to testing would output fizz instead of fizzbuzz
		if (count % FizzBuzz == 0) {
			return "FizzBuzz";
		}
		if( count % Fizz == 0) {
			return "Fizz";
		}
		if (count % Buzz == 0) {
			return "Buzz";
		}
			return Integer.toString(count);
		}
	
}
