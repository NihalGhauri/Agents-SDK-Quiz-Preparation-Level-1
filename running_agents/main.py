from agents import Agent , Runner, AsyncOpenAI , OpenAIChatCompletionsModel, set_tracing_disabled
import os

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

external_model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model= "gemini-1.5-flash",
)

agent = Agent(
    name="assistant",
    instructions="A helpful assistant that can answer questions and provide information.",
    model=external_model,
)

result = Runner.run_sync(agent, "What is the capital of France?")
print(f"Result: {result.final_output}")
