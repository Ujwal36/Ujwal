package demo;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class TestParallelExecution {

    @Test
    public void test_case01() throws InterruptedException {
        System.out.println("Executing Testcase01");
        WebDriver driver = new ChromeDriver();

        driver.get("https://qtripdynamic-qa-frontend.vercel.app/");
        Thread.sleep(3000);

        System.out.println("Test1 Title: " + driver.getCurrentUrl());
        driver.quit();
    }

    @Test
    public void test_case02() throws InterruptedException {
        System.out.println("Executing Testcase02");
        WebDriver driver = new ChromeDriver();

        driver.get("https://qtripdynamic-qa-frontend.vercel.app/pages/register/");
        Thread.sleep(3000);

        System.out.println("Test2 Title: " + driver.getCurrentUrl());
        driver.quit();
    }
    
}
