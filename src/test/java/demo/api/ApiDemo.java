package demo.api;

import org.testng.annotations.Test;

import com.relevantcodes.extentreports.ExtentReports;
import com.relevantcodes.extentreports.ExtentTest;

import io.restassured.RestAssured;
import io.restassured.response.Response;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class ApiDemo {

    private static final Logger log = LogManager.getLogger(ApiDemo.class);

    @Test
    public void api_test_01() {

        log.info("Starting API test");

        RestAssured.baseURI = "https://qtrip-backend.labs.crio.do";
        RestAssured.basePath = "/api/v1/cities";

        Response resp = RestAssured.given().when().get();
         log.info("respnse status code is: " +resp.getStatusCode());

        System.out.println(resp.asPrettyString());

        System.out.println(resp.getStatusCode());

        System.out.println(resp.getTime());

         log.info("finished API test");
    }
}