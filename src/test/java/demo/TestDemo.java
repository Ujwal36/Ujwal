package demo;

import java.util.UUID;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.UUID;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.Assert;
import org.testng.annotations.Test;


public class TestDemo {

    //Annotation --> Testng
    @Test

    public static void testcase01() throws  java.lang.InterruptedException {
        
        // Launch browser (Selenium 4.25.0 automatically manages the driver behind the scenes!)
       // WebDriver driver = new ChromeDriver();
         ChromeOptions options = new ChromeOptions();
        WebDriver driver = new RemoteWebDriver(
                new URL("http://host.docker.internal:4444"),
                options
        );
        // Open website
        driver.get("https://qtripdynamic-qa-frontend.vercel.app/pages/register/");
        System.out.println(UserName + " " + Password);


        Thread.sleep(1000);

        String username = UserName + UUID.randomUUID();
        driver.findElement(By.id("floatingInput")).sendKeys(username);


        driver.findElement(By.id("floatingPassword")).sendKeys(Password);

        driver.findElement(By.name("confirmpassword")).sendKeys(Password);

        driver.findElement(By.cssSelector(".btn.btn-primary.btn-login")).click();
        Thread.sleep(10000);




        // Print title
        System.out.println("Title: " + driver.getTitle());
        Assert.assertEquals(driver.getTitle(), "QTrip");
        Assert.assertEquals(driver.getCurrentUrl(), "https://qtripdynamic-qa-frontend.vercel.app/pages/login");
        System.out.println("URL: "+ driver.getCurrentUrl());
       
        System.out.println("Closing the browser");
        // Close browser


        driver.quit();//Closes the broswer
    }
}
