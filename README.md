# Connected Systems API for Python (conSys4Py)
This package aims to help simplify the process of communicating with OGC's Connected Systems API.

 **Note:** This package is still in development and as such some of the features are lower level than they will be upon 
 a full release and are subject to change. Some features may not yet be fully tested as the spec is evolving and 
 differences may arise.

## Using the API
Currently, there are 3 main intended ways of using this API:
1. Direct API calls: With the part_1 and part_2 modules, there are separate files names for resource types recognized 
by the API that have simple functions relating to different types of requests you can make of the API.
2. Default API Helper: You can create an API helper object that assists with making repeated requests to the same endpoint.
Its methods involve providing a resource type, and any IDs, plus request bodies* if necessary.
3. Custom API requests: You can also manually build api helper objects that allow for the greatest customization of the
ultimate request.

__*Note: This refers to the ConnectedSystemsAPIRequest and ConnectedSystemsRequestBuilder classes.__



