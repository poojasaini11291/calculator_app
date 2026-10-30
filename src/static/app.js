const form = document.querySelector("#calculator-form");
const firstNumber = document.querySelector("#first-number");
const secondNumber = document.querySelector("#second-number");
const operation = document.querySelector("#operation");
const result = document.querySelector("#result");
const resultHint = document.querySelector("#result-hint");
const errorMessage = document.querySelector("#error-message");
const clearButton = document.querySelector("#clear-button");
const squareRootButton = document.querySelector("#square-root-button");
const defaultOperation = "addition";

function clearStaleResult() {
    result.textContent = "";
    resultHint.textContent = "Your answer will appear here.";
    errorMessage.textContent = "";
    errorMessage.hidden = true;
}

[firstNumber, secondNumber].forEach((input) => {
    input.addEventListener("input", clearStaleResult);
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    errorMessage.hidden = true;
    errorMessage.textContent = "";

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                first_number: firstNumber.value,
                second_number: secondNumber.value,
                operation: operation.value,
            }),
        });
        const payload = await response.json();

        if (!response.ok) {
            throw new Error(payload.detail || "Unable to calculate with those values.");
        }

        result.textContent = payload.result;
        resultHint.textContent = "Calculation complete.";
    } catch (error) {
        errorMessage.textContent = error.message;
        errorMessage.hidden = false;
    }
});

squareRootButton.addEventListener("click", async () => {
    const activatedAt = performance.now();
    errorMessage.hidden = true;
    errorMessage.textContent = "";
    const currentValue = result.textContent.trim() || firstNumber.value;

    if (!currentValue) {
        errorMessage.textContent = "Enter a number first.";
        errorMessage.hidden = false;
        return;
    }

    try {
        const response = await fetch("/sqrt", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ value: currentValue }),
        });
        const payload = await response.json();

        if (!response.ok) {
            throw new Error(payload.detail || "Unable to calculate the square root.");
        }

        result.textContent = payload.result;
        firstNumber.value = payload.result;
        resultHint.textContent = "Square root calculated. Use this value in your next operation.";

        // Include the browser/API round trip and wait for the updated result
        // to pass through a paint before recording the agreed timing interval.
        await new Promise((resolve) => {
            requestAnimationFrame(() => requestAnimationFrame(resolve));
        });
        performance.clearMeasures("square-root-activation-to-result-display");
        performance.measure("square-root-activation-to-result-display", {
            start: activatedAt,
            end: performance.now(),
        });
    } catch (error) {
        result.textContent = "";
        resultHint.textContent = "";
        errorMessage.textContent = error.message;
        errorMessage.hidden = false;
    }
});

clearButton.addEventListener("click", () => {
    form.reset();
    operation.value = defaultOperation;
    result.textContent = "";
    resultHint.textContent = "Your answer will appear here.";
    errorMessage.textContent = "";
    errorMessage.hidden = true;
});