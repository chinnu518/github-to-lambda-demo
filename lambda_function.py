import requests
import pandas

def lambda_handler(event, context):
    print("event received:", event)
    response = requests.get('https://www.google.com')
    print(response.text)
    data = {'col1':[1,2], 'col2':[3,4]}
    df = pd.DataFrame(data=data)
    print("Demo completed !!!")


