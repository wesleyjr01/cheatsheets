### Deployment of Python Lambdas with .zip
* https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

### Event
* An event is a JSON-formatted document that contains data for a Lambda function to process. The runtime converts the event to an object and passes it to your function code. When you invoke a function, you determine the structure and contents of the event.
* **Example custom event - weather data:**
```
{
  "TemperatureK": 281,
  "WindKmh": -3,
  "HumidityPct": 0.55,
  "PressureHPa": 1020
}
```

* **Example service event – Amazon SNS notification:**
```
{
  "Records": [
    {
      "Sns": {
        "Timestamp": "2019-01-02T12:45:07.000Z",
        "Signature": "tcc6faL2yUC6dgZdmrwh1Y4cGa/ebXEkAi6RibDsvpi+tE/1+82j...65r==",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "Message": "Hello from SNS!",
        ...
```

### Python Lambda Handler:
* https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
* The Lambda function handler is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. When the handler exits or returns a response, it becomes available to handle another event.
```python
def handler_name(event, context): 
    ...
    return some_value
```
* A function handler can be any name; however, the default name in the Lambda console is `lambda_function.lambda_handler`.
* How it works, when Lambda invokes your function handler, the Lambda runtime passes two arguments to the function handler:
  * The first argument is the [event object](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-event). An event is a JSON-formatted document that contains data for a Lambda function to process. The Lambda runtime converts the event to an object and passes it to your function code. It is usually of the `Python dict` type. It can also be `list, str, int, float, or the NoneType` type. The event object contains information from the invoking service. When you invoke a function, you determine the structure and contents of the event. When an AWS service invokes your function, the service defines the event structure.
  * The second argument is the [context object](https://docs.aws.amazon.com/lambda/latest/dg/python-context.html). A context object is passed to your function by Lambda at runtime. This object provides methods and properties that provide information about the invocation, function, and runtime environment. Example:

        import time

        def lambda_handler(event, context):   
            print("Lambda function ARN:", context.invoked_function_arn)
            print("CloudWatch log stream name:", context.log_stream_name)
            print("CloudWatch log group name:",  context.log_group_name)
            print("Lambda Request ID:", context.aws_request_id)
            print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
            # We have added a 1 second delay so you can see the time remaining in get_remaining_time_in_millis.
            time.sleep(1) 
            print("Lambda time remaining in MS:", context.get_remaining_time_in_millis())