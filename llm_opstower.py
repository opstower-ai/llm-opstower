import llm
from llm.default_plugins.openai_models import Chat

@llm.hookimpl
def register_models(register):
    chat_model = Chat(
                  'opstower',
                  model_name='opstower',
                  api_base="https://app.opstower.ai/api/v1"
                 )
    chat_model.needs_key = 'opstower'
    register(chat_model)