def mobile_orders():
    #Connect to BitBar device "Google Pixel 6 -US".
    #Mobile.ConnectDevice("https://appium-us.bitbar.com/wd/hub/", '{\"automationName\":\"UiAutomator2\",\"bitbar_app\":\"144856190\",\"bitbar_device\":\"Google Pixel 6 -US\",\"bitbar_findDevice\":false,\"bitbar_target\":\"android\",\"deviceName\":\"Google Pixel 6 -US\",\"platformName\":\"ANDROID\"}', 600)
    #Simulates a touch on the view.
    Aliases.Device.processSmartbearExampleOrders.listView1.textViewText13.Touch()
    #Simulates a touch on the view.
    Aliases.Device.processSmartbearExampleOrders.buttonEdit.Touch()
    #Checks whether the 'Text' property of the Aliases.Device.processSmartbearExampleOrders.scrollView.textViewTextTotal object equals '160'.
    aqObject.CheckProperty(Aliases.Device.processSmartbearExampleOrders.scrollView.textViewTextTotal, "Text", cmpEqual, "160")
   


    
    

def ContactUS_loop():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    Project.Variables.varloop.Reset()
    RecordIdx = 1
    while RecordIdx <= 2:
        #Clicks the 'linkContactUs' link.
        Aliases.browser.pageShop.header.navUsd.navContactUs.linkContactUs.Click()
        #Waits until the browser loads the page and is ready to accept user input.
        Aliases.browser.pageContactus.Wait()
        #Clicks the 'textboxYourName' control.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Click()
        #Sets the text KeywordTests.ContactUS_loop.Variables.varloop["Name"] in the 'textboxYourName' text editor.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.SetText(Project.Variables.varloop.Value["Name"])
        #Enters '[Tab]' in the 'textboxYourName' object.
        Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Keys("[Tab]")
        #Sets the text KeywordTests.ContactUS_loop.Variables.varloop["Email"] in the 'emailinputYourEmail' text editor.
        Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.SetText(Project.Variables.varloop.Value["Email"])
        #Clicks the 'textareaEnquiry' control.
        Aliases.browser.pageContactus.sectionContent.formYourName.textareaEnquiry.Click()
        #Enters KeywordTests.ContactUS_loop.Variables.varloop["Enquiry"] in the 'textareaEnquiry' object.
        Aliases.browser.pageContactus.sectionContent.formYourName.textareaEnquiry.Keys(Project.Variables.varloop.Value["Enquiry"])
        #Clicks the 'buttonSendEmail' button.
        Aliases.browser.pageBallChair.sectionContent.formYourName.buttonSendEmail.ClickButton()
        #Checks whether the 'contentText' property of the Aliases.browser.pageContactus.FindElement("//div[contains(text(), 'Your enquiry has been successfully sent to the store owner.')]") object equals 'enquiry has been successfully sent to the store owner.'.
        aqObject.CheckProperty(Aliases.browser.pageContactus.FindElement("//div[contains(text(), 'Your enquiry has been successfully sent to the store owner.')]"), "contentText", cmpEqual, "enquiry has been successfully sent to the store owner.")
        Project.Variables.varloop.Next()
        RecordIdx = RecordIdx + 1

def web():
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'linkContactUs' link.
    Aliases.browser.pageShop.header.navUsd.navContactUs.linkContactUs.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageContactus.Wait()
    #Clicks the 'textboxYourName' control.
    Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Click()
    #Sets the text 'Dan ' in the 'textboxYourName' text editor.
    Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.SetText("Daniel")
    #Enters '[Tab]' in the 'textboxYourName' object.
    Aliases.browser.pageContactus.sectionContent.formYourName.textboxYourName.Keys("[Tab]")
    #Sets the text 'd' in the 'emailinputYourEmail' text editor.
    Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.SetText("d")
    #Sets the text 'd@sb.com' in the 'emailinputYourEmail' text editor.
    Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.SetText("d@sb.com")
    #Enters '[Tab]' in the 'emailinputYourEmail' object.
    Aliases.browser.pageContactus.sectionContent.formYourName.emailinputYourEmail.Keys("[Tab]")
    #Enters 'Where's my order?' in the 'textareaEnquiry' object.
    Aliases.browser.pageContactus.sectionContent.formYourName.textareaEnquiry.Keys("Where's my order?")
    #Clicks the 'buttonSendEmail2' button.
    Aliases.browser.pageContactus.sectionContent.formYourName.buttonSendEmail2.ClickButton()
    #Checks whether the 'contentText' property of the Aliases.browser.pageContactus.FindElement("//h1[.='Contact Us']") object equals 'Contact Us'.
    aqObject.CheckProperty(Aliases.browser.pageContactus.FindElement("//h1[.='Contact Us']"), "contentText", cmpEqual, "Contact Us")

def SmartStore():
    Var1 = ""
    #Launches the specified browser and opens the specified URL in it.
    Browsers.Item[btChrome].Run("https://bearstore-testsite.smartbear.com/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'imagePictureForCategoryBasketbal' control.
    Aliases.browser.pageShop.sectionContent.articleBasketball.linkBasketball.imagePictureForCategoryBasketbal.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageBasketball.Wait()
    TimeoutValue = Options.Run.Timeout
    Options.Run.Timeout = 15000
    #Clicks the 'imageShowDetailsForHighSchool' control.
    Aliases.browser.pageBallChair.sectionContent.article25.linkShowDetailsForHighSchool.imageShowDetailsForHighSchool.Click()
    Options.Run.Timeout = TimeoutValue
    #Checks whether the 'contentText' property of the Aliases.browser.pageBasketball.sectionContent.textnodeBasketball object equals 'hockey'.
    aqObject.CheckProperty(Aliases.browser.pageBasketball.sectionContent.textnodeBasketball, "contentText", cmpEqual, "hockey")
