## Log Analytics on S3 with Lambda + Athena


## Workflow:

Data Source: You have CSV/JSON log files (e.g., web clicks, IoT sensor data).

Storage: Upload raw data files into an S3 bucket (my-analytics-raw).

Processing: Use AWS Lambda to:

Trigger automatically when a new file is uploaded.

Parse the data (e.g., clean up fields, filter, add metadata).

Save the processed data to another S3 bucket (my-analytics-processed).

Querying: Use Athena (serverless SQL) to query the processed data in S3.

Visualization: Connect Amazon QuickSight to Athena for dashboards.