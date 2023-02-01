const result = document.querySelector('#result a').innerText
const copyBtn = document.getElementById("copy")
const form = document.querySelector('form')
const resultDiv = document.getElementById('result')

// Displaying copy button when short url generated
form.addEventListener("DOMContentLoaded", showCopy())
function showCopy() {
    if (result) {
        copyBtn.style.visibility = "visible"
    } else {
        copyBtn.style.visibility = "hidden"
    }
}

// Only allow submission if url has been entered
const input = document.querySelector("input")
form.addEventListener("submit", no_text)

function no_text(e) {
    if (!input.value.includes("http")) {
        e.preventDefault()
        alert("Please enter a http:// url")
    }
}

// Copy to clipboard functionary
copyBtn.addEventListener("click", copyURL)
function copyURL(e) {
    navigator.clipboard.writeText(result).then(console.log("copied to clipboard"))
    const copyMessage = document.createElement('p')
    copyMessage.textContent = "Copied to clipboard :)";
    resultDiv.appendChild(copyMessage);

    copyBtn.disabled = true
}