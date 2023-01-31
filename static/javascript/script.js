const result = document.getElementById("result")
const link = document.querySelector('a')

const form = document.querySelector('form')

form.addEventListener("submit", show_url())

function show_url() {
    result.style.visibility = "visible"
}

const copyBtn = document.getElementById("copy")
copyBtn.addEventListener("onclick", copyURL)

function copyURL(e) {
    copy_text = document.getElementById('url')
    copy_text.select()
    navigator.clipboard.writeText(copy_text.value)
}