# Sample AWS Bedrock knowledge base backed chatbot

## Project components
- **AWS Lambda Function Url** : Serves as a backend API and integrates with the Bedrock knowledge base
- **Streamlit** : Frontend for the chatbot
- **AWS Bedrock** : Knowledge base for the chatbot

### Project setup
This project is deployed using a SAM template (serverless.template) in the \backend folder. The 
template creates a lambda function with a function url that acts as our mini API for the chatbot.

In addition, the app.py contains the front end code written using Python + Streamlit. You can easily set up Streamlit to pull your initial front end code from your Github repository and also 
allow it to sync any changes pushed to a specific branch (main in our case).