def drag():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://draggable-and-droppable.webflow.io/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Drags the 'panel2' object.
    Aliases.browser.pageBallChair.panel2.Drag(141, 52, 792, -4)
    #Drags the 'panel3' object.
    Aliases.browser.pageBallChair.panel3.Drag(213, 50, 507, 253)
    #Drags the 'panel3' object.
    Aliases.browser.pageBallChair.panel3.Drag(234, 42, 523, 18)
    #Drags the 'panel3' object.
    Aliases.browser.pageBallChair.panel3.Drag(222, 60, -444, -226)
    #Drags the 'panel4' object.
    Aliases.browser.pageBallChair.panel4.Drag(202, 53, -476, -248)
