from google.cloud import dialogflow_v2
import os


class DialogFlow:

    def __init__(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(
            os.path.abspath(__file__)) + "/keys/public-key.json"
        self.client = dialogflow_v2.SessionsAsyncClient

    async def message(self, text: str) -> str:
        text_input = dialogflow_v2.TextInput(text=text, language_code="es")
        query_input = dialogflow_v2.QueryInput(text=text_input)
        async with self.client() as async_client:
            session = async_client.session_path(os.environ.get("PROJECT_ID"), os.environ.get("SESSION_ID", "me"))
            response = await async_client.detect_intent(query_input=query_input, session=session)
        return response.query_result.fulfillment_text


DialogFlowService = DialogFlow()
