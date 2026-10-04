# test
from src.agent import amazn_agent
if __name__ == "__main__":
    response = amazn_agent.run(
        "What is the current status of order ORD1098?"
    )
    print("\nFinal Answer:")
    print(response)
