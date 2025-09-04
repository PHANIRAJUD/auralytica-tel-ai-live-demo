import matplotlib.pyplot as plt

def visualize(data):
    # Dummy plot
    plt.bar(["Positive", "Negative"], [data.get('positive', 0), data.get('negative', 0)])
    plt.title("Sentiment Analysis Result")
    plt.savefig("sentiment_graph.png")