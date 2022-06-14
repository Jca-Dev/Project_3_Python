<h1>Car Manufacturer Survey</h1>
<hr>
The Car Manufacturer Survey Python terminal is designed for the collection of survey data to be easily input to a google sheet document.<br> 
<a href="https://car-manufacturer-survey.herokuapp.com/">Click Here</a> to go to the live website.
<hr>

![Responsive site test](/images/responsive.jpg)
<hr>

<h1>How it works</h1>
<ul>
    <li>The user follows the instructions printed at the top of the terminal. Entering the 10 numbers separated by comma's from the survey results.</li>
    <li>The terminal runs and gives updates and feedback to the user that their input is valid and that its updating the sheet and finally when the sheet has updated successfully.</li>
    <li>Once the terminal has updated the sheet and verified to the user it was successful, it prints the current survey totals.</li>
    <li>The google sheet is updated with the data and returns the totals with a SUM within the sheet at the top.</li>
</ul>

![Terminal preview](/images/project.jpg)
<hr>

![google sheet results updated](/images/sheet.jpg)
<hr>

<h1>Features</h1>
<ul>
    <li>Instructions to the user.</li>
    <li>Feedback and updates while running.</li>
    <li>Prints current totals after each data input.</li>
    <li>Has a loop at the end that asks if the user wants to enter more data (restarts) or not (ends all functions)</li>
</ul>
<h2>Future features</h2>
<ul>
    <li>Survey sheet selection for multiple surveys. This is why there are f strings in the current code for "scoreboard" sheet.</li>
</ul>

<hr>

<h1>Technologies Used</h1>
<ul>
    <li>Python 3 - coding language.</li>
    <li>API - google sheet API.</li>
    <li>Git - Version control by utilizing the Gitpod terminal to add and commit to Git then Push to GitHub.</li>
    <li>Git Hub - stores the project code and hosts the website.</li>
    <li>Visual Code Studio - system used to write code via Git</li>
    <li>Paint 3D - to create the logo and edit screenshots for the README.md</li>
    <li>Heroku - for hosting the python code and downloading requirements.</li>
    <li>Pep8 - testing code.</li>
</ul>
<hr>
<h1>Deployment</h1>
<h2>Heroku</h2>
The project was deployed to Heroku via GitHub by:
<ol>
    <li>Logging Into Heroku, selecting my project, going to the settings page and adding the two required build packs (python) (nodejs).</li>
    <li>Going to deploy, selecting deployment method as GitHub and typing in the GitHub repository name.</li>
    <li>Finally you can select deploy branch to manually deploy or select automatic deployment (allows Heroku to rebuild the project after each push to GitHub.</li>
</ol>
The page is now published and the link is in the sett section at the bottom in Domains.

<br>

<h2>Making a Local Clone</h2>
<ol>
<li>Log in to GitHub and locate the [GitHub Repository](https://github.com/)</li>
<li>Under the repository name, click "Clone or download".</li>
<li>To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.</li>
<li>Open Git Bash</li>
<li>Change the current working directory to the location where you want the cloned directory to be made.</li>
<li>Type `git clone`, and then paste the URL you copied in Step 3.</li>
<li>Press Enter. Your local clone will be created.</li>
<li>Create a new Heroku app and follow the steps in Heroku deployment above.</li>
</ol>

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for retrieve pictures and more detailed explanations of the above process.
    
<hr>
<h1>Testing</h1>
<h2>Manual test</h2>
<ul>
    <li>Given invalid input such as letters and incorrect amount of data, both resulting in a succesful error message.</li>
    <li>Tested in the Code Institute Heroku terminal and my local terminal.</li>
</ul>

<h2>Softwares</h2>
<ul>
    <li><a href="http://pep8online.com/" target="_blank" rel="noopener">Pep8 Validation Service</a></li>

![Pep8](/images/pep8.jpg)

</ul>

<h2>Bugs & Fixes</h2>
<ul>
   <li>Pep8 picked up a random blank line in a """ message """. Fix - deleted the blank line.</li>
   <li>Pep8 also picked up a print statement with an unused f string inside. Fix - remove f string from print statement.</li>
   <li>Microsoft Visual Studio internal validator showed me that a "from" and "import" were not used but in the code. Fix - deleted said "from" and "import" then tested code again with no errors.</li>
</ul>

<h2>Known Bugs</h2>
<ul>
    <li>So far through my testing I have not identified any more known bugs after my fixes. There is however a potential problem if the survey input is submitted over 100 times. The totals will only update 100 times unless you modify the SUM in the google sheet directly.</li>
</ul>
<hr>
<h2>Sources/Credits</h2>
<hr>
<ul>
    <li>My Mentor for her feedback.</li>
    <li>Code Institute for thier deployment terminal template from <a href="https://github.com/Code-Institute-Org/python-essentials-template" target="_blank" rel="noopener">GitHub</a></li>
    <li>Code Institute's Love_sandwiches walkthrough provided a very clear idea on how to create a data entry project. <a href="https://github.com/Jca-Dev/Love_sandwiches" target="_blank" rel="noopener">GitHub Link</a></li>
    <li>Gathered information and troubleshooting from <a href="https://stackoverflow.com/" target="_blank" rel="noopener">Stackoverflow</li>