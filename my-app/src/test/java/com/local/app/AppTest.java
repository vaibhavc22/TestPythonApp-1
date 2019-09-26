package com.local.app;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class AppTest {


 @SuppressWarnings({ "ConstantConditions", "ResultOfMethodCallIgnored" })
        @Test
        public void setup() throws Exception {
                System.out.println("Test Started ....");
                URL url = new URL("http://0.0.0.0:4444/wd/hub");
                ChromeOptions chromeOptions = new ChromeOptions();
                chromeOptions.addArguments("--window-size=1280,1024");
                DesiredCapabilities desiredCapabilities = DesiredCapabilities.chrome();
                desiredCapabilities.setCapability(ChromeOptions.CAPABILITY,
                                chromeOptions);
                 WebDriver driver = new RemoteWebDriver(url, desiredCapabilities);
                String testURL = System.getProperty("testURL");

                driver.get(testURL);
Thread.sleep(1000 * 10);			
				System.out.println("verifying page title");
                Assert.assertEquals(driver.getTitle(), "Swayam Central");
//				 System.out.println("verifying application logo");
//                Assert.assertTrue(driver.findElement(By.xpath("//a[@class='navbar-brand']/img")).isDisplayed());
				driver.quit();

        }

}




