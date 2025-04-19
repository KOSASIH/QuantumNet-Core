// src/dashboard/frontend/static/script.js

async function fetchMetrics() {
    const metricsContainer = document.getElementById("metrics");
    metricsContainer.innerHTML = "";  // Clear previous metrics

    // Show loading spinner
    const loadingSpinner = document.createElement("div");
    loadingSpinner.className = "loading";
    metricsContainer.appendChild(loadingSpinner);

    try {
        const response = await fetch("http://localhost:8000/api/v1/metrics/");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const metrics = await response.json();
        
        // Remove loading spinner
        metricsContainer.removeChild(loadingSpinner);

        // Update the DOM with new metrics
        metrics.forEach(metric => {
            const metricDiv = document.createElement("div");
            metricDiv.className = "metric";
            metricDiv.innerHTML = `<h2>${metric.name}</h2><p>Value: ${metric.value}</p>`;
            metricsContainer.appendChild(metricDiv);
        });
    } catch (error) {
        console.error("Failed to fetch metrics:", error);
        metricsContainer.innerHTML = `<p class="error">Error fetching metrics: ${error.message}</p>`;
    }
}

// Function to filter metrics based on user input
function filterMetrics() {
    const filterInput = document.getElementById("filterInput").value.toLowerCase();
    const metricDivs = document.querySelectorAll(".metric");
    
    metricDivs.forEach(div => {
        const metricName = div.querySelector("h2").innerText.toLowerCase();
        if (metricName.includes(filterInput)) {
            div.style.display = "block";
        } else {
            div.style.display = "none";
        }
    });
}

// Set up event listener for filtering
document.getElementById("filterInput").addEventListener("input", filterMetrics);

// Fetch metrics every 5 seconds
setInterval(fetchMetrics, 5000);

// Initial fetch
fetchMetrics();
