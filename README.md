## Dataset Content
The dataset provided is a list of fictitious student performance data from an unnamed college. The dataset can be found here:
https://www.kaggle.com/datasets/desalegngeb/students-exam-scores

the source offers 2 versions of the dataset, a smaller one with complete data and fewer features, and a larger one with fewer datarows, but more alvailable features. This larger dataset also has the additional requirement of some data cleaning as some values are missing, and need to be corrected for.

For the purpose of this project, I will use the second set to demonstrate some data cleaning that might be required before the exploratory data analysis and model training.

Available features are:

* Gender: Gender of the student (male/female)
* EthnicGroup: Ethnic group of the student (group A to E)
* ParentEduc: Parent(s) education background (from some_highschool to master's degree)
* LunchType: School lunch type (standard or free/reduced)
* TestPrep: Test preparation course followed (completed or none)
* ParentMaritalStatus: Parent(s) marital status (married/single/widowed/divorced)
* PracticeSport: How often the student parctice sport (never/sometimes/regularly))
* IsFirstChild: If the child is first child in the family or not (yes/no)
* NrSiblings: Number of siblings the student has (0 to 7)
* TransportMeans: Means of transport to school (schoolbus/private)
* WklyStudyHours: Weekly self-study hours(less that 5hrs; between 5 and 10hrs; more than 10hrs)
* MathScore: math test score(0-100)
* ReadingScore: reading test score(0-100)
* WritingScore: writing test score(0-100)

The target(s) will be the predicted score for Math, Reading and Writing for a given student.


## Business Requirements

The following metrics were decided with the stakeholder (school administration) that is looking to incorporate ML capability in supporting their counselling staff to monitor and help students achieve the academic standard.

### Purpose:
The primary objective is to create an interactive, user-friendly dashboard for school counselors and educators. This tool aims to predict student performance in math, reading, and writing, focusing on identifying students at risk of not achieving a passing grade. The dashboard will facilitate early intervention and personalized support strategies. The dashboard should be deployed to their internal server and allow counsellors secure access to the database and prediction model so they can prepapre for student counselling sessions.


## Hypothesis

I hypothesize that most of the listed Features in the available student dataset will have some degree of influence on the overall performance of the student.

### Gender: Gender of the student (male/female)
depending on the subject, gender will probably influence the students overall performance.
### EthnicGroup: Ethnic group of the student (group A to E)
ethnicity (when regarded in socio-economic terms) will influence student perfromance. In this case the specfic groups are anonymized.
### ParentEduc: Parent(s) education background (from some_highschool to master's degree)
Parental education will influence student performance as I hypothesize that higher educated individuals will also prioritize the education of their children.
### LunchType: School lunch type (standard or free/reduced)
similar to ehtnicity, the availability of a healthy regular meal will most likely influence performance directly by affecting concentration, but also indirectly as a factor of other socio-economic variables such as financial security enabling additional schooling support (materials, study partners etc)
### TestPrep: Test preparation course followed (completed or none)
Availability and participation in test prep courses most likely will influence test performance for most students
### ParentMaritalStatus: Parent(s) marital status (married/single/widowed/divorced)
parental status might influence students performance on a motivationl level as well as more basic factors such as avaiable study time and less distractions
### PracticeSport: How often the student parctice sport (never/sometimes/regularly))
Presumably regular sport will also help with concentration and brain development, leading to better academic performance
### IsFirstChild: If the child is first child in the family or not (yes/no)
First children tend to have more focussed attention from their parents and might possibly have a better start in their education path
### NrSiblings: Number of siblings the student has (0 to 7)
more youngers siblings might negatively impact performance due to distrctions and additional chores. Older siblings might help however in providing additional help in school studies. I hypothesize that this will not be an obvious lindicator of student performance.
### TransportMeans: Means of transport to school (schoolbus/private)
transportation will presumanbly have some influence again in socio-economic terms (private transport might equate to access to othr extracurricular activites that might help student performance)
### WklyStudyHours: Weekly self-study hours(less that 5hrs; between 5 and 10hrs; more than 10hrs)
I hypothesize that the mount of study time per week devoted to exam preparation will have a significant impact on student performance.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* The dataset with final results for Math, Reading and Writing will allow an EDA to identify which features of the data set have the most influence on the student performance.  This will allow a reasonable assessment of the evaluation of my hypothesies and corrobrate the schools assumptions so far. 
* The new step and direect business requirement will be to train a machine learning algorithm to predict the final score on a new class of students on unseen data. To achieve this, some feature enineering might be neccessary to encode categorical varibles into numerical values which can be interpreted by an ML pipleine. The initial approach will be supervised learning on known student results while allowing the algorithm to identify the key features that have the most influence on teh result.
* To satisfy the business requirement, we aim to train the model to have a greater than 0.7 accuracy in predicting the scores for math, reading and writing


## ML Business Case
* ML will help in identifying key features of the data that significantly impact the final scores of a given student. Armed with this knowledge, ML gives the unique capability to predict the probable student outcome and allow early intervention to ensure good student performance throught the school year.


## Dashboard Design
* The dashboard will analyze and display student data, including math, reading, and writing scores.
* It will incorporate various student features such as sex, weekly study hours, lunch type, parental status, and parental education levels.
* The tool will predict individual student scores based on entered data, using machine learning algorithms.
* It will flag students who are likely to struggle in achieving passing grades, enabling timely intervention.
* The dashboard will generate reports listing students who may require additional support or resources.

### Dashboard Pages:

1. **Project Summary** - An introduction to the business requirement and key features of the dataset. Also an bsic instruction of how to use the dashboard
2. **Project Hypothesis and evaluation** - presentation of the project hyposthesis and potential outcomes
3. **Exploratory Data Analysis (EDA)** - EDA of the dataset and explanation of the dataset strengths and weaknesses
4. **Report Generator** Page to generate a report of all students enrolled in the school in danger of not reaching a passing grade in Math. The user will be able to selecte the passing grade as a percentage
5. **Prediction Engine** - Page to allow the counsellor to input all known variables about a new student (or changes in circumstance of a known student) and predict the current score probablilty.
6. **Technical Explanations** Summary page for education experts interested in the model training steps and performance levels.

## Unfixed Bugs
 
## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

