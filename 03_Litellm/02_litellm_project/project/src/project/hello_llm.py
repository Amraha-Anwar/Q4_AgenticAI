from litellm import completion
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyATSu5y4Pgg9pUpOBeLCGd05o5YI3jLUis"

def gemini():
    response = completion(
        model = "gemini/gemini-2.0-flash",
        messages = [{"content": "Hello How are you?", "role": "user"}]
    )

    print(response)

# OUTPUT 👇🏻
# ModelResponse(id='N5xMaJH1GsuM1PIPkIuSsAI', created=1749851190, model='gemini-2.0-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message
# -----------------------------------------------------------------------
# (content='I am doing well, thank you for asking! How are you today?\n', 
#  -----------------------------------------------------------------------
#  role='assistant', tool_calls=None, function_call=None, provider_specific_fields=None))], usage=Usage(completion_tokens=16, prompt_tokens=5, total_tokens=21, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetailsWrapper(audio_tokens=None, cached_tokens=None, text_tokens=5, image_tokens=None)), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])


def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)


# OUTPUT 👇🏻

# ModelResponse(id='eZxMaOyAHtixgLUP29rU0QE', created=1749851256, model='gemini-2.0-flash-exp', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message
# ---------------------------------------------------------------------------------------------------
# content="I am doing well, thank you for asking! As a large language model, I don't experience emotions or have feelings in the same way humans do, but I am f for asking! As a large language model, I don't experience emotions or have feelings in the same way humans do, but I am functioning optimally and ready to assist you. How can I help you today?\n", 
# ----------------------------------------------------------------------------------------------------
# role='assistant', tool_calls=None, function_caunctioning optimally and ready to assist you. How can I help you today?\n", role='assistant', tool_calls=None, function_call=None, provider_specific_fields=None))], usage=Usage(completion_tokens=51, prompt_tokens=6, total_tokens=57, completion_tokens_details=None, prompt_tokens_details=PromptTokensDetailsWrapper(audio_tokens=None, cached_tokens=None, text_tokens=6, image_tokens=None)), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])