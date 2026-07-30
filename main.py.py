import requests
import datetime

url = "http://localhost:11434/api/generate"
log_file = "llm-conversation.txt"

models = {"1": "deepseek-r1", "2": "llama3.2"}

def generate(model, prompt):
    try:
        r = requests.post(url, json={
            "model": model,
            "prompt": prompt,
            "temperature": 0.7,
            "stream": False
        })
        return r.json()["response"].strip()
    except:
        return "Error contacting model"

def build_prompt(q, prev, debate, first):
    if first:
        return q
    if debate:
        return f"Argue against this:\n{prev}"
    return f"I asked: {q}\nAnswer was: {prev}\nContinue the discussion."

def main():
    open(log_file, "w").close()

    q = input("Enter question: ")
    debate = input("Debate mode? (yes/no): ").lower() == "yes"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Started: " + str(datetime.datetime.now()) + "\n")
        f.write("Question: " + q + "\n\n")

    prev = ""
    round_no = 1

    while True:
        print("\nRound", round_no)
        print("1 - Deepseek-r1")
        print("2 - Llama 3.2")
        print("Type 'exit' to stop")

        choice = input("Choose model: ").strip()
        if choice.lower() == "exit":
            break

        model = models.get(choice, "deepseek-r1")
        prompt = build_prompt(q, prev, debate, round_no == 1)
        res = generate(model, prompt)

        output = f"[{model}]\n{res}\n"
        print(output)

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(output + "\n")

        prev = res
        round_no += 1

    print("Conversation saved to llm-conversation.txt")

if __name__ == "__main__":
    main()