# Corrections - Release baseline W01-W04

First attempt: exercises/release-baseline-w01-w04.pdf
First commit: a4710ec (27/09/2026, 22:30)
Review date: 28/09/2026, 09:00
Sources consulted: ML-introduction.pdf, Decision_Tree.pdf

Tags: [WRONG] outright error, [BLANK] left empty, [GUESS] correct but guessed, [SOLID] correct and I can re-derive it.

---

### Definitions of FP and FN [WRONG]

**What I wrote**: 
- FP is a bounding box no matching ground-truth object exists in that location.
- FN is missing or failing to generate a valid bounding box although the real object exists.

**What is correct**:
Those are object-detection definitions, which assume predictions carry spatial extent. In a plain classification problem there is no location to match. 
For a given class c, FP is a sample whose true label is not c but which the model assigns to c; FN is a sample whose true label is c but which the model assigns elsewhere. In multi-class problems both are read off the confusion matrix: FP for class c is the column sum excluding the diagonal, FN is the row sum excluding the diagonal.
FP depends on the grounding box that model can generate (if model can draw infinite bounding box where no object exists, FP can be infinite). FN is limited by the real objects existing in the class c.

**Source:** ML-introduction.pdf, page 33-34.

**Why I got it wrong:** My formulas for precision, recall and F1 were all correct, so I never checked whether the definitions underneath them matched my own task. I had imported the object-detection version from a different context and never noticed the mismatch.

---

### Overfitting vs. Underfitting [SOLID]

**What I wrote**: I wrote the correct features between Overfitting model and Underfitting one. I also give the model that balanced the two error metrics (Good fit) that can capture a target object successfully but no memorize noise.

**Confirmed**: ML-introduction.pdf, page 25.

---

### Bias-Variance Decomposition [GUESS]

**What I wrote**: I wrote the correct formula, but I cannot explain how to derive this formula.

**What is correct**:
This formula originized from the Expected squared prediction error. Then we subtitute y = f(x) + e (f(x) is true function, e is random noise) and we continue interpreting. After the cross-term vanishes, we use Expected model prediction to perform it into the formula of Bias-Variance Decomposition.

**Source:** ML-introduction.pdf, page 43-46.

**Why I got it wrong:** I remembered the shape of the formula but I do not know the derivation to get this.

---

### Classification Tree vs. Regression Tree [SOLID]

**What I wrote**: I wrote the correct comparison between Classification and Regression Tree, so I can exactly distinguish from two these kinds of tree.

**Confirmed**: ML-introduction.pdf, page 4.

---

### Pre-pruning [GUESS]

**What I confused**: I wrote that when use pre-pruning approach in C4.5 Algorithm, a node is nearly pure when major proportion is large or equal than a specified parameter (called 'tau') but I do not know how exactly to decide this param.

**What is correct**: Because the slide Decision_Tree.pdf does not discuss how to determine the parameter 'tau', I decide to ask AI for this. I receive the answer that: this threshold depends on the metrics of validation set (befor that we need the train set), and then the test set will be used for evaluating the performance. 'tau' is used as a threshold to get a good-fit model.

**Source**: Claude.

---

### CART [BLANK]

**What I wrote**: I did not wrote anything about this CART.

**What I should write**:
- CART constructs binary decision trees for both classification and regression tasks.
- For classification, it evaluates Gini Impurity reduction and select splits that maximize it.
- For regression, it evaluates the sum of squared errors (SSE) and select binary splits that reduce it.
- The prediction at the leaf nodes is the majority class for classification, and typically the mean or median target value for regression.

**Source**: Decision_Tree.pdf, from page 53.