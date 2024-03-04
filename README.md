Hello fellow interns! <br>

As you can see there are two folders in this repository. <br> <br>
  python_implementation - this is a demo I've set up to show how to use the NewsAPI API. It is functional and can be tested by:
      - 1. installing the required dependencies
      - 2. running app.py
      - 3. searching the url "localhost:5000/topic/your_topic_here" where you replace your_topic_here with any news topic.<br><br>
  React/my-app - for now, an empty react project for us to get started with.<br><br>

As of now the python_implementation section is doing some of the things we want it to, but we have a long way to go. 
Right now we can pull news sources based on search topic. We can also look for key words in the news sources using the YAKE python library<br><br>

Here are some of the things we want to be able to do:
  - Firstly, we want at least the amount of functionality for the React implementation as the python one currently has.
  - Second, in React, we want to create widgets that contain the top three keyword searches from the API call "localhost:5000/topic/politics"
        Each widget should contain one additional API call containing a popular keyword from the politics topic.
        For example, if the most popular words were "Biden, election, and politics" we want one widget to contain "localhost:5000/topic/Biden" and so on.
  - Third, eventually we do not want to have to depend on frequent API calls. We should implement a database to store the results of these calls.
  - Last, we want some additional functionality. This one is pretty much open to interpretation, but some key things to make might be:
          - 1. a search bar that lets the user search by topic or by news source
          - 2. keyword filtering that keeps us from getting silly topics. For example one popular keyword might be representative, but that is not a newsworthy category.<br><br>

Good luck and please contact me frequently with questions, suggestions, or progress updates. 
