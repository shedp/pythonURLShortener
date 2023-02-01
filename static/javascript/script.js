const result = document.querySelector('#result a').innerText
const copyBtn = document.getElementById("copy")
const urlInput = document.getElementById('url')
const form = document.querySelector('form')

form.addEventListener("DOMContentLoaded", showCopy())

function showCopy() {
    if (result) {
        copyBtn.style.visibility = "visible"
    } else {
        copyBtn.style.visibility = "hidden"
    }
}

const input = document.querySelector("input")
form.addEventListener("submit", no_text)

function no_text(e) {
    if (urlInput.value == "") {
        e.preventDefault()
        alert("Please enter a URL")
    }
}

copyBtn.addEventListener("click", copyURL)

function copyURL(e) {
    navigator.clipboard.writeText(result).then(console.log("copied to clipboard"))
}