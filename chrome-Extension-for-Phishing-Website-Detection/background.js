chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "checkUrl") {
        console.log("Received checkUrl message");

        // Get the active tab's URL
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            const url = tabs[0].url;  // Get the URL of the current active tab
            console.log("URL of the current tab:", url);

            fetch('http://127.0.0.1:5000', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: url })
            })
            .then(response => response.json())
            .then(data => {
                console.log("Data received from Flask:", data);
                if (data.classification) {
                    sendResponse({ classification: data.classification });
                } else if (data.error) {
                    sendResponse({ error: data.error });
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
                sendResponse({ error: error.toString() });
            });

            
            return true;
        });
    }
});
