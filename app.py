# app.py

# https://medium.com/@power.up1163/visualizing-topic-models-with-topicwizard-ee5b4428405e

# Deployment https://x-tabdeveloping.github.io/topic-wizard/usage.deployment.html
import topicwizard

# Since topicwizard is technically just like any Dash application you can easily deploy topicwizard to a cloud probvider or your own servers.
# You can either create the app from scratch with a trained topic pipeline.
# app = topicwizard.get_dash_app(vectorizer, topic_model, corpus=corpus)

# Or you can retrieve an app from loaded data.
app = topicwizard.load_app(filename="topic_data.joblib")

# Then you can run the server from the file manually:
if __name__ == "__app__":
    app.run_server(debug=False)
    # app.run_server(debug=False, port=8050)

# We recommend using Gunicorn for deployment in production.
# gunicorn main:app.server -b 8050

# You can easily package a topicwizard app with gunicorn into a Docker image as well.
