import os
from python_a2a import OpenAIA2AServer, run_server
from python_a2a import AgentCard, AgentSkill
from dotenv import load_dotenv

load_dotenv() 
# Define the agent's profile
agent_card = AgentCard(
    name="Stock Market Expert",
    description="Expert in market trends, fundamentals, and investment strategies.",
    url="http://localhost:5000",
    version="1.0.0",
    skills=[
        AgentSkill(
            name="Market Analysis",
            description="Analyze overall market sentiment and key indicators.",
            examples=["What's the current market sentiment?", "Impact of interest rates on tech stocks?"]
        ),
        AgentSkill(
            name="Investment Strategies",
            description="Discuss risk management and portfolio diversification.",
            examples=["How to diversify my portfolio?", "Explanation of dollar-cost averaging."]
        ),
        AgentSkill(
            name="Company Analysis",
            description="Interpret financial ratios and company fundamentals.",
            examples=["How to read P/E ratios?", "Key metrics for evaluating growth stocks."]
        )
    ]
)
# Initialize and start the A2A server
a2a_server = OpenAIA2AServer(
    api_key=os.environ['OPENAI_API_KEY'],
    model="gpt-4o",
    temperature=0.0,
    system_prompt="You are a stock market and financial analysis expert. Provide factual, concise insights."
)
if __name__ == '__main__':
    run_server(a2a_server, host='0.0.0.0', port=5000)