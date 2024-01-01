# Python Mushroom Classifier

This is an application I created while working through my BSCS. This was a chance for me to cut my teeth on a machine learning problem for the very first time.  

The gist of the assignment was to go forth and choose a data set from Kaggle, and then build an application around that data set. We were required to use one descriptive method and one predictive method. The descriptive method should have at least three types of visualizations.

I decided to use [this data set](https://www.kaggle.com/datasets/uciml/mushroom-classification) from Kaggle to create an application around the problem of mushroom classification for a fictional company called "Shroomin' USA" that sells mushroom grow kits and other mushroom related accessories. The web interface for the application was created using [Streamlit](https://streamlit.io/), so I was able to write the entire application using only Python. 

The application is hosted on the Streamlit Community Cloud. If you want to check it out, [click here](https://brungardtdb-shroomin-usa-mushroom-classifier-main-0imnba.streamlit.app).


If you have Docker installed, you can also check out the application by running the following command:

`docker run -p 8501:8501 brungardt/python-mushroom-classifier:latest`

*Depending on your configuration, if you are on Linux, you may need to run the above command as "sudo"*

Once the Docker container is running, you should see the following text in your console:

> You can now view your Streamlit app in your browser.
>
>  URL: http://0.0.0.0:8501

If you visit that URL in your browser, or click on the URL to open it in the browser, you should see the application running.

For the descriptive method, I gave the user three types of visualizations to choose from: a count plot, a heatmap, and a pie chart. To create these visualizations, I used the [Seaborn](https://seaborn.pydata.org/) library. These visualizations can be viewed by selecting the "explore the data set" tab on the left-hand side menu, or by appending "/explore_the_data_set" to the main application url. 

The user can choose any of the mushroom characteristics present in the data set. Once the user has made a selection, they can hit the "display visualization" button and the visualization will be rendered in the browser.

For the predictive method, I used Gradient Boost for classification from the [Scikit-learn](https://scikit-learn.org/stable/) library. 

The user can interact with the mushroom classifier by selecting the "mushroom classifier" tab on the left-hand side menu, or by appending "/mushroom_classifier" to the main application url. 

The user can select options for seven different mushroom characteristics: 

* odor
* stalk root
* bruises
* stalk surface below ring
* spore print color
* ring type
* gill spacing

Once the user has made their selection, they can prompt the application by selecting the "classify mushroom" button at the bottom of the form, and the application will indicate whether the mushroom is most likely edible or poisonous. 

The data set contained 23 different properties for each mushroom, but for the sake of simplicity I limited the user to the top seven most impactful charateristics and defaulted the rest to whichever option was most common in the data set. 