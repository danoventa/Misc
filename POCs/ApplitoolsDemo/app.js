import 'dotenv/config';
import 'chromedriver';

import { Eyes } from "eyes.selenium";
import  webDriver from "selenium-webdriver";

const getConfiguredEyes =  () => {
    const eyes = new Eyes();
    eyes.setApiKey("FjYTqtP2REi10863JqmLbXSCszQBeBHZH6se2FZlhNFVM110");
    eyes.setForceFullPageScreenshot(true);
    eyes.setMatchLevel("Strict");
    console.log("Eyes configured");
    return eyes;
};

const runTests = async () => {
    console.log("Building driver");

    let driver;
    try {
       driver = new webDriver.Builder()
            .forBrowser('chrome')
            .build();
       driver.sleep(50000);
    } catch (error) {
        console.log(`Failed to build driver: ${error}.`)
    }


    console.log("Generating new eyes");
    const eyes = getConfiguredEyes();
    console.log(eyes);
    let result;
    try {
        let failed = false;
        try {
            driver =  await eyes.open(driver, "Test app", "First test", { width: 1024, height: 700});
        } catch (error) {
            failed = true;
            console.log(`Error openning eyes: ${error}`)
        }
        if (!failed){
            await driver.get("https://demo.applitools.com");
            await eyes.checkWindow("Login Window Test");
        }
    } catch (error) {
        console.log("#####Throw ERROR");
        console.log(`Error: ${error}`);
    } finally {
        console.log("#####Close Eyes");
        try {
            result =  eyes ? eyes.close(false) : console.error("eyes was null");
        } finally {
            eyes.abortIfNotClosed();
            driver.quit();
        }
        console.log("#####Quit Driver");
        console.log("#####abort eyes");

    }
    console.log("#####leave and return stuff?");

    console.log(result);
    return result;
};

console.log(runTests());

