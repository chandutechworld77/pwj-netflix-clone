import os

PROMPT_DIR = "prompts"

def evaluate_prompt(prompt):
    # Simple scoring logic
    if len(prompt.split()) > 5:
        return 0.8
    return 0.5

def main():
    scores = []

    if not os.path.exists(PROMPT_DIR):
        print("❌ prompts folder not found")
        exit(1)

    for file in os.listdir(PROMPT_DIR):
        if file.endswith(".txt"):
            path = os.path.join(PROMPT_DIR, file)

            with open(path, "r") as f:
                content = f.read().strip()

                if not content:
                    print(f"❌ Empty file: {file}")
                    exit(1)

                score = evaluate_prompt(content)
                print(f"{file}: {score}")
                scores.append(score)

    if not scores:
        print("❌ No prompt files found")
        exit(1)

    final_score = sum(scores) / len(scores)
    print(f"FINAL_SCORE={final_score}")

if __name__ == "__main__":
    main()
