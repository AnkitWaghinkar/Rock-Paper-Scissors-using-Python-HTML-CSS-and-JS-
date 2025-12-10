function playClick() {
    if (window.soundEnabled) {
        document.getElementById("clickSound").play();
    }
}

window.onload = () => {
    const resultText = document.getElementById("result");
    if (!resultText || !window.soundEnabled) return;

    const r = resultText.innerText.toLowerCase();

    if (r.includes("win")) document.getElementById("winSound").play();
    else if (r.includes("lose")) document.getElementById("loseSound").play();
    else if (r.includes("tie")) document.getElementById("tieSound").play();
};

function showLoading() {
    document.getElementById("gameArea").classList.add("hidden");
    document.getElementById("loading").classList.remove("hidden");
}
