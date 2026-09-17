# To retrive the data from response and print only those users who are active


response_data = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "user": "Alice",
            "active": True,
            "orders": [{"id": 101, "amount": 50}, {"id": 102, "amount": 150}]
        },
        {
            "id": 2,
            "user": "Bob",
            "active": False,
            "orders": [{"id": 103, "amount": 20}, {"id": 104, "amount": 30}]
        },
        {
            "id": 3,
            "user": "Charlie",
            "active": True,
            "orders": [{"id": 105, "amount": 500}]
        }
    ]
}

print(response_data['status'] == "success")

output_list = response_data["data"]
res = [item['user'] for item in output_list if item["active"]]

print(res)
