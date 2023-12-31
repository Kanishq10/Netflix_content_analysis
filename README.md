# Netflix_content_analysis


# **Problem Statement:** 
Analyze and predict the viewership and success of movies and TV shows on a streaming platform based on various attributes such as type, title, director, cast, country, date added, release year, rating, duration, listed in, and description. 

Specifically, I want to answer the following questions and perform tasks related to this dataset:

1. **Viewership and Popularity Analysis:** 
   - What are the most popular types of content on the platform (Movies or TV Shows)?
   - Which countries contribute the most content?
   - Does the release year affect the popularity of content?

2. **Content Duration Analysis:**

   - Are there any trends in content duration over the years?
   
3. **Genre Analysis:**
   - Which genres are most prevalent on the platform?
   - Are there any trends in the popularity of specific genres?

4. **Country Analysis:**
   - Do viewers have a preference for content from certain countries?  

4. **Predictive Modeling:**
   - Can we build a model to predict the success (e.g., viewership, ratings) of a movie or TV show based on its attributes?


By addressing these questions and tasks, the streaming platform can gain insights into its content library, viewer preferences

## About this Dataset
Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.

***Description of each column in the dataset:***

1. **show_id:** A unique identifier for each show or movie.
   
2. **type:** The type of content, either "Movie" or "TV Show."

3. **title:** The title of the movie or TV show.

4. **director:** The director of the movie or TV show. In the first and third entries, this information is not available (NaN).

5. **cast:** The cast or actors in the movie or TV show. In the first entry, this information is not available (NaN). In the second entry, there is a list of actors from the TV show "Blood & Water."

6. **country:** The country where the movie or TV show was produced or is associated with.

7. **date_added:** The date when the content was added to the streaming platform, in the format "Month Day, Year."

8. **release_year:** The year the movie or TV show was originally released.

9. **rating:** The content's rating, which indicates the recommended audience age or maturity level (e.g., "PG-13" or "TV-MA").

10. **duration:** The duration of the movie or TV show. In the first entry, the duration is given in minutes ("90 min"). In the second and third entries, it's indicated in the number of seasons ("2 Seasons" and "1 Season").

11. **listed_in:** The genre or category of the content, which can help classify it (e.g., "Documentaries," "International TV Shows," "Crime TV Shows").

12. **description:** A brief description or synopsis of the movie or TV show, providing an overview of the plot or subject matter.
