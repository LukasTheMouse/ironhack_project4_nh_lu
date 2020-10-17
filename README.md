# ironhack_project4_nh_lu

<h1>Data analysis business runners vs recreationist runners</h1>
<p>Group project Ironhack Niharika &amp; Lukas</p>


<h2> Intro to the topic </h2>
<p>Since the 80's on every third weekend September the <u>dam tot dam loop</u>, a ten-mile run from Amsterdam to Zaandam takes place. 
The run is the biggest running event in the Netherlands and attracts between 40-50k people ranging from competitive and recreationists runners. 

In this analysis we are going to see whether there are noticeable differences between two categories:

<b>Business runner category </b> 
Includes runners who participate in the event together with co-workers. 

<b>Recreationists runner</b>
Includes runners who participate in the event individually. 

</p>


<h2> Research questions </h2>
<p>
<span>&#8226;</span> Business runners run faster than recreational runners

<span>&#8226;</span> Female and male business runners run faster than the recreational runners of the same sex

<span>&#8226;</span>Runners from top 3 Dutch banks i.e. ING, Rabobank and ABN AMRO run faster than top 3 consultant Companies i.e Deloitte, Pwc, KPMG.

</p>


<h1>Content of the Repository</h1>

<h2>Data</h2>

<p>The dataset for this analysis comprises two files with running times from business and recreationist runners that participated in the dam tot damloop 2016 - 2018</p>

<h3>Business runners dataset</h3>
<p><b>name_x</b> Disregard	</p>
<p><b>sex</b> Gives the gender for the recreationist runners. In the business runners it is also present but disregard it</p>
<p><b>city</b>	City where the participants lives</p>
<p><b>company</b> Company team for which the participant runs</p>
<p><b>guntime</b> Time between the start signal and crossing the finish lines </p>
<p><b>realtime</b> Time measured between crossing the start and the finish lines </p>	
<p><b>BIB</b>	Runners start number </p>	
<p><b>year</b> Event year </p>
<p><b>guntime_in_second</b> Gun time converted to seconds</p>	 
<p><b>realtime_in_second</b>	Realtime converted to seconds</p>	
<p><b>speed</b>	speed of the runners in km/h</p>
<p><b>province</b> indicates whether the runner comes from the province of north holland or not </p>
<p><b>diff_gun_realtime</b> number of seconds between Realtime and gun time</p>
<p><b>speed_buckets</b>	speed buckets for km/h</p>
<p><b>firstname</b>	First name of the participant </p>
<p><b>gender</b>	Gender than was given to the name based on our gender guessing libaries <b>gender_guesser , gender_detector </b></p>
<p><b>name_y</b> Disregard</p>

<h3>Recreationist runners dataset</h3>
<p><b>sex</b> Gives the gender for the recreationist runners. In the business runners it is also present but disregard it</p>
<p><b>city</b>	City where the participants lives</p>
<p><b>guntime</b> Time between the start signal and crossing the finish lines </p>
<p><b>realtime</b> Time measured between crossing the start and the finish lines </p>	
<p><b>BIB</b>	Runners start number </p>	
<p><b>year</b> Event year </p>
<p><b>guntime_in_second</b> Gun time converted to seconds</p>	 
<p><b>realtime_in_second</b>	Realtime converted to seconds</p>	
<p><b>speed</b>	speed of the runners in km/h</p>
<p><b>province</b> indicates whether the runner comes from the province of north holland or not </p>
<p><b>diff_gun_realtime</b> number of seconds between Realtime and gun time</p>
<p><b>speed_buckets</b>	speed buckets for km/h</p>
<p><b>distance</b> distance between hometown of the runner and Amsterdam </p>

<h1>Download data</h1>

<p>go to the notebook <b>/config/data_collection_transformation_walkthrough.ipynb</b> and follow the steps in the notebook</p>

<h1>Run the analysis</h1>

<p>Open the notebook <b>Analysis.ipynb</b> and follow the steps in the notebook</p>

<p>Thanks for your interest in our project</p>
