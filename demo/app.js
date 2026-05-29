const anomalies = [
  {
    symbol: "SOLUSDT",
    oneHour: "+4.2%",
    day: "+11.8%",
    volume: "3.6x",
    risk: "High",
    context: "Momentum extended, volatility spike",
  },
  {
    symbol: "BTCUSDT",
    oneHour: "+1.1%",
    day: "+3.4%",
    volume: "1.8x",
    risk: "Medium",
    context: "Range breakout under review",
  },
  {
    symbol: "ETHUSDT",
    oneHour: "-0.8%",
    day: "+2.2%",
    volume: "1.4x",
    risk: "Low",
    context: "Normal volatility regime",
  },
  {
    symbol: "WIFUSDT",
    oneHour: "+7.9%",
    day: "+18.5%",
    volume: "5.2x",
    risk: "High",
    context: "Overheated short-term move",
  },
];

const scannerRows = document.querySelector("#scannerRows");

function renderAnomalies(filter = "All") {
  scannerRows.innerHTML = anomalies
    .filter((item) => filter === "All" || item.risk === filter)
    .map((item) => {
      const riskClass = item.risk.toLowerCase();
      return `
      <tr>
        <td><strong>${item.symbol}</strong></td>
        <td>${item.oneHour}</td>
        <td>${item.day}</td>
        <td>${item.volume}</td>
        <td class="risk ${riskClass}">${item.risk}</td>
        <td>${item.context}</td>
      </tr>
    `;
    })
    .join("");
}

renderAnomalies();

const navLinks = Array.from(document.querySelectorAll("nav a"));

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.forEach((candidate) => candidate.classList.remove("active"));
    link.classList.add("active");
  });
});

document.querySelectorAll("[data-risk-filter]").forEach((button) => {
  button.addEventListener("click", () => {
    document
      .querySelectorAll("[data-risk-filter]")
      .forEach((candidate) => candidate.classList.remove("active"));
    button.classList.add("active");
    renderAnomalies(button.dataset.riskFilter);
  });
});

const riskInput = document.querySelector("#riskInput");
const plannedRisk = document.querySelector("#plannedRisk");

riskInput.addEventListener("input", () => {
  plannedRisk.textContent = `${Number(riskInput.value).toFixed(2)}%`;
});

document.querySelectorAll("[data-journal-card]").forEach((card) => {
  card.addEventListener("click", () => {
    document
      .querySelectorAll("[data-journal-card]")
      .forEach((candidate) => candidate.classList.remove("active"));
    card.classList.add("active");
  });
});

const replayProfiles = {
  trailing: {
    copy: "Trailing exit review preserved part of the move while reducing late reversal exposure.",
    heights: ["32%", "46%", "70%", "62%", "88%", "74%", "54%", "38%"],
    color: "#43b9a8",
  },
  fixed: {
    copy: "Fixed target review exits earlier and may leave momentum on the table.",
    heights: ["28%", "44%", "66%", "50%", "42%", "34%", "30%", "24%"],
    color: "#c7a23b",
  },
  nostop: {
    copy: "No-stop review shows maximum adverse excursion so risk is visible before a trade is repeated.",
    heights: ["30%", "52%", "78%", "45%", "36%", "26%", "48%", "72%"],
    color: "#c95f54",
  },
};

document.querySelectorAll("[data-replay]").forEach((button) => {
  button.addEventListener("click", () => {
    document
      .querySelectorAll("[data-replay]")
      .forEach((candidate) => candidate.classList.remove("active"));
    button.classList.add("active");
    const profile = replayProfiles[button.dataset.replay];
    document.querySelector("#replayCopy").textContent = profile.copy;
    document.querySelectorAll(".timeline span").forEach((bar, index) => {
      bar.style.height = profile.heights[index];
      bar.style.background = index === 4 ? "#c95f54" : profile.color;
    });
  });
});
