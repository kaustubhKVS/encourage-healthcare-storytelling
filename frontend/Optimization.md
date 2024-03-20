https://docs.kanaries.net/topics/Streamlit/how-to-run-streamlit

Improving App Performance
Streamlit provides powerful caching primitives that can significantly enhance your app's performance. These caching primitives allow your app to remain performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

Streamlit offers two main types of caching: @st.cache_data and @st.cache_resource. The @st.cache_data decorator is used to cache functions that return data, such as dataframe transformations, database queries, or machine learning inference. On the other hand, @st.cache_resource is used to cache functions that return global resources, such as database connections or machine learning models.

Here's an example of how to use these decorators:

@st.cache_data
def long_function(param1, param2): # Perform expensive computation here or # fetch data from the web here
return data

@st.cache_resource
def init_model(): # Return a global resource here
return pipeline(
"sentiment-analysis",
model="distilbert-base-uncased-finetuned-sst-2-english"
)

You can also clear all in-memory and on-disk data caches using st.cache_data.clear() and st.cache_resource.clear().

Optimizing App Rendering
The performance of a Streamlit app can also be affected by the complexity of its user interface. If your app becomes unresponsive when resizing the browser window or expanding/collapsing the sidebar, it might be due to the rendering of complex UI elements.

One way to optimize the rendering of your Streamlit app is to simplify its UI. For example, instead of using a large number of sliders or select sliders, consider using other types of input widgets that are less resource-intensive.

Another approach is to optimize the rendering of your plots. If your app includes complex Plotly charts, consider using the use_container_width=True option when calling st.plotly_chart. This option ensures that your charts are rendered at the optimal size for your app's container, improving rendering performance.

Deploying Streamlit Apps Efficiently
When deploying a Streamlit app, it's important to consider the resources required by your app and the capabilities of your deployment platform. For example, if your app performs heavy computations or handles large datasets, you might need to choose a deployment platform with sufficient CPU and memory resources.

One common pitfall when deploying Streamlit apps is not accounting for memory optimization. If your app uses a large amount of memory, it can crash upon deployment or become unresponsive. To avoid this, consider using techniques such as caching, efficient data handling, and memory profiling to reduce your app's memory usage.

In summary, optimizing a Streamlit app involves a combination of improving computational performance, optimizing UI rendering, and deploying your app efficiently. By applying these techniques, you can ensure that your Streamlit apps are fast, responsive, and reliable.

https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker

The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. Your container needs to listen to Streamlit’s (default) port 8501:

EXPOSE 8501
The HEALTHCHECK instruction tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501:

HEALTHCHECK CMD curl --fail http://localhost:8501/\_stcore/health
An ENTRYPOINT allows you to configure a container that will run as an executable. Here, it also contains the entire streamlit run command for your app, so you don’t have to call it from the command line:

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
