document.addEventListener("DOMContentLoaded", function () {
  const checkButton = document.getElementById("check-button");

  checkButton.addEventListener("click", function () {
    console.log("Check button clicked");
    chrome.runtime.sendMessage({ action: "checkUrl" }, function(response) {
      console.log("Response received:", response);
      if (response.classification) {
        alert('Classification: ' + response.classification);
      } else if (response.error) {
        alert('Error: ' + response.error);
      } else {
        alert('Unexpected response format');
      }
    });
  });
});
