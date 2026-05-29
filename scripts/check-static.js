const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");

const requiredFiles = [
  "index.html",
  "site.css",
  "demo/index.html",
  "demo/styles.css",
  "demo/app.js",
  "reports/daily-review-sample.html",
  "reports/report.css",
  "sample_data/anomalies.json",
  "sample_data/paper_trades.json",
  "assets/hero-dashboard.png",
  "assets/video-thumbnail.png",
  "assets/social-og.png",
  "assets/video-thumbnail-clean.png",
  "assets/screenshots/home.png",
  "assets/screenshots/demo.png",
  "assets/screenshots/report.png",
  "assets/gallery/product-hunt-01.png",
  "assets/gallery/product-hunt-02.png",
  "assets/gallery/product-hunt-03.png",
  "assets/gallery/product-hunt-04.png",
  "video/crypto-replay-journal-promo.mp4",
  "video/crypto-replay-journal-promo-narrated.mp4",
  "video/narration.srt",
  "video/narration.txt",
  "video/narration-energetic-male.mp3",
  "docs/COMPLIANCE_BOUNDARY.md",
  "marketing/DEMO_STORYBOARD.md",
  "marketing/PUBLISHING_CHECKLIST.md",
  "marketing/PROMOTION_READY.md",
  "LICENSE",
  "CONTRIBUTING.md",
  "SECURITY.md",
  "RELEASE_NOTES.md",
  ".gitignore",
  ".github/ISSUE_TEMPLATE/bug_report.md",
  ".github/ISSUE_TEMPLATE/feature_request.md",
  "scripts/package-release.ps1",
];

const forbiddenPatterns = [
  /buy signal/i,
  /sell signal/i,
  /guaranteed profit/i,
  /guaranteed return/i,
  /profit promise/i,
  /copy trading platform/i,
];

const textExtensions = new Set([".html", ".css", ".js", ".json", ".md"]);

function readText(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}

for (const file of requiredFiles) {
  if (!fs.existsSync(path.join(root, file))) {
    throw new Error(`Missing required file: ${file}`);
  }
}

const publicCopyFiles = [
  "index.html",
  "demo/index.html",
  "demo/app.js",
  "reports/daily-review-sample.html",
  "marketing/LAUNCH_COPY.md",
  "marketing/DEMO_STORYBOARD.md",
];

for (const file of publicCopyFiles) {
  if (!textExtensions.has(path.extname(file))) {
    continue;
  }

  const text = readText(file);
  for (const pattern of forbiddenPatterns) {
    if (pattern.test(text)) {
      throw new Error(`Forbidden phrase matched ${pattern} in ${file}`);
    }
  }
}

for (const jsonFile of [
  "sample_data/anomalies.json",
  "sample_data/paper_trades.json",
]) {
  const parsed = JSON.parse(readText(jsonFile));
  if (!Array.isArray(parsed) || parsed.length === 0) {
    throw new Error(`Expected non-empty array in ${jsonFile}`);
  }
}

const site = readText("index.html");
const demo = readText("demo/index.html");
const report = readText("reports/daily-review-sample.html");

for (const [name, text] of [
  ["index.html", site],
  ["demo/index.html", demo],
  ["reports/daily-review-sample.html", report],
]) {
  if (!text.includes("Not financial advice")) {
    throw new Error(`Missing disclaimer in ${name}`);
  }
}

console.log("Static product checks passed.");
