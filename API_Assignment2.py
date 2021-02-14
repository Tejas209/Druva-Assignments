import requests
from API_Payload import *
import time
url = "http://216.10.245.166/Library/Addbook.php"
headers = {"Content-Type": "application/json"}

# api post method to add a book
isbn = "pqr12345"
add_response = requests.post(url, json=addBookPayload(isbn), headers=headers)
response_json = add_response.json()
print(response_json)
bookId = response_json['ID']
print(bookId)
print(add_response.elapsed.total_seconds())
# api method to delete a book
url_delete = "http://216.10.245.166/Library/DeleteBook.php"
delete_response = requests.post(url_delete, json={'ID': bookId}, headers=headers)
print(delete_response.json())
assert delete_response.status_code == 200

