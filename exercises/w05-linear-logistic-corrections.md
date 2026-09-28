# Corrections - W05 drill on linear & logistic regression

First attempt: exercises/w05-linear-logistic-first-attempt.pdf
First commit: 113112b
Review date: 28/09/2026, 10:00
Sources consulted: LinearRegression.pdf, LogisticRegression.pdf

Tags: [WRONG] outright error, [BLANK] left empty, [GUESS] correct but guessed, [SOLID] correct and I can re-derive it.

---

### Closed-form solution for linear regression  [GUESS]

**What I wrote:** I wrote the model coefficients for equation of linear regression model, but I could not write the derivation; I only noted "set the derivative to zero".

**What is correct:** Starting from E_D(w), the derivative of E_D(w). Setting it to 0^T and collect terms, which in matrix form is X^T.Xw = X^T.t.

**Source:** LinearRegression.pdf, slides 17–18.

**Why I got it wrong:** I had memorised the result without ever deriving it, so I could not recall what the derivative of a sum of squares looks like.

---

### Ridge versus LASSO  [BLANK]

**What I wrote:** nothing.

**What is correct:** Ridge penalises and has the closed-form solution. LASSO penalises $\Sigma|w_m|$ and has no closed form, because the absolute value is not differentiable at zero and the problem must be solved iteratively. That same kink at zero is what drives many LASSO coefficients to exactly zero, giving implicit feature selection.

**Source:** LinearRegression.pdf, slides 38–41.

**Why I left it blank:** I spent too long on part 3. I need to time-box each question in the next drill.

---

### Why least squares equals maximum likelihood  [SOLID]

**What I wrote:** With Gaussian noise, maximising the likelihood is the same as minimising the sum of squares, because taking the negative log of the Gaussian turns the exponent into a squared-error term.

**Confirmed against:** LinearRegression.pdf, slides 11 and 14–15.

---

### Hessian of the logistic loss  [GUESS]

**What I wrote:** H = X^T.RX, and I guessed that R was diagonal, but I could not say what its entries were.

**What is correct:** R is diagonal with R_m. Every entry lies in (0, 0.25], so R is positive definite and H is positive semi-definite, which is why the loss is convex and Newton–Raphson converges to the global minimum.

**Source:** LogisticRegression.pdf, slide 24.

**Why I got it wrong:** I remembered the shape of the formula but had never asked what R actually contains, so I also missed the connection to convexity.
