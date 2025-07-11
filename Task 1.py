import requests

API_TOKEN = "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"  
API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def summarize_text(text):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": 20,
            "max_length": 50
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    
    result = response.json()
    if isinstance(result, list) and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        raise ValueError("Unexpected response format: ", result)

def main():
    print("---TEXT SUMMARIZER---")
    print("Enter The Text You Want to Summarize (Press Enter wice to Finish):")

    user_input = ""
    while True:
        line = input()
        if line == "":
            break
        user_input += line + ""

    try:
        print("\nOriginal Text:\n", user_input)
        summary = summarize_text(user_input)
        print("\nSummary:\n", summary)
        
    except requests.exceptions.HTTPError as err:
        print("ERROR: Check your API token or internet connection.\n", err)
        
    except Exception as e:
        print("Unexpected error occurred:", e)

if __name__ == "__main__":
    main()


