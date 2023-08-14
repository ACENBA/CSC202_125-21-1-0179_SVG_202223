import requests

parameters = {
    "amount": 10,
    "type": "boolean"
    
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

question_data = [
    {
        
        "category": "Social science: Current affairs",
        "type": "boolean",
        "difficulty": "medium",
        "text": "A slug's blood is green.", "Answer": "True" 
        
    }
    
]