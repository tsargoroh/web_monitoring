Main functions:
1. Reads a list of web pages (HTTP URLs) and corresponding page content requirements from a configuration file (web_pages.ini).
2. Periodically makes an HTTP request to each page.
3. Verifies that the page content received from the server matches the content requirements (strings).
4. Measures the time it took for the web server to complete the whole request.
5. Writes a log file that shows the progress of the periodic checks (web_info.log).
6. Sends email to administartor in case content requirements are not fulfilled or web site is down.

Details:
- The “content requirements” are strings that must be included in the HTML response
received from the server. As an example, one potential rule might be that the page at the URL
“http://www.example.com/login” must contain the text “Please login:”.
- The checking period is configurable by a setting in the configuration file (settings.ini).
- The log file contains the checked URLs, their status and the response times.
- The program distinguishes between connection level problems (e.g. the web site is down) and content
problems (e.g. the content requirements were not fulfilled).
