import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class FizzTest {
	
	@Test
	public void testFizzReturnOne() {
		
		 String result = FizzMain.NumOutput(1);
		 assertEquals("1",result);

	}
	
	@Test
	public void testFizzReturnFizzfor3() {
		
		String result = FizzMain.NumOutput(3);
		 assertEquals("Fizz",result);
		
	}
	
	@Test
	public void testFizzReturnTwofor2() {
		
		String result = FizzMain.NumOutput(2);
		 assertEquals("2",result);
	}
	
	@Test
	public void testFizzReturnBuzzfor5() {
		
		String result = FizzMain.NumOutput(5);
		 assertEquals("Buzz",result);
	}
	
	@Test
	public void testFizzReturnTenfor10() {
		
		String result = FizzMain.NumOutput(10);
		 assertEquals("Buzz",result);
	}
	
	@Test
	public void testFizzReturnFizzfor9() {
		
		String result = FizzMain.NumOutput(9);
		 assertEquals("Fizz",result);
	}
	
	@Test
	public void testFizzReturnElevenfor11() {
		
		String result = FizzMain.NumOutput(11);
		 assertEquals("11",result);
	}
	@Test
	public void testFizzReturnFizzBuzzfor15() {
		
		String result = FizzMain.NumOutput(15);
		 assertEquals("FizzBuzz",result);
	}
	
	
	
	
}
