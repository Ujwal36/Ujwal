events = [
    {"customer_id": 101, "version": 1, "status": "ACTIVE"},
    {"customer_id": 102, "version": 1, "status": "ACTIVE"},
    {"customer_id": 101, "version": 3, "status": "BLOCKED"},
    {"customer_id": 101, "version": 2, "status": "ACTIVE"},
    {"customer_id": 102, "version": 2, "status": "BLOCKED"},
    {"customer_id": 102, "version": 3, "status": "ACTIVE"}
]

event = iter(events)
expected = {}
for _ in range(len(events)):
    next_event = next(event)
    customer_id = next_event["customer_id"]
    status = next_event["status"]
    version = next_event["version"]
    if customer_id not in expected :
        expected[customer_id] = list([version,status])
    else:
        if version > expected[customer_id][0]:
            expected[customer_id] = list([version,status])
# modify expected as per the output format
for customer_id, list_values in expected.items():
    expected[customer_id]= list_values[1]
print(expected)
