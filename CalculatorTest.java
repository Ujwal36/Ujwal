import org.testng.Assert;
import org.testng.annotations.Test;

public class CalculatorTest {

    @Test
    public void additionTest() {

        int result = 2 + 3;

        System.out.println("Addition Result: " + result);

        Assert.assertEquals(result, 5);
    }

    @Test
    public void subtractionTest() {

        int result = 10 - 4;

        System.out.println("Subtraction Result: " + result);

        Assert.assertEquals(result, 6);
    }
}
