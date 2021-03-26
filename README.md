This browser-based tool that visualizes the launch schedule is an interactive site that shows a calendar 
which will have different days highlighted depending on the rocket launch on that day. 
It incorporates the following technologies: HTML, CSS, Javascript, Express.js(a Node.js framework), and Python. 

The following is a quick description of the site and how to use it. 

Download all the necessary files(all the filse must be in the correct folders).

Go to cmd and type "node app.js" to run the webapp.

On any browser(I used google chrome), type in localhost:8080.

This should direct you to a page with a calendar that has days highlighted
depending on the rocket launch that day. The legend key will be above the calendar and shows the corresponding colors to the rocket launches. 
There is a button called "Delay Schedule" and you can press it so that the new delayed schedule will appear. You can then only click on the
red dates to show which launches were delayed to their respective dates and how far delayed(in days) from original date
and the total cost of delaying that launch to that day. Only the red dates will 
have this feature as those launches were delayed to that day and necessary info must be given. The "Delay Schedule" button is now changed to 
"Original Schedule" button and can be pressed to return to the original schedule. 

The JSON file contains all the launches and each launch's corresponding information such as the name of the rocket, the original scheduled launch date, 
the new delayed launch date(if any), and the cost of delay for each day(if any). I used python to make the json file. 
