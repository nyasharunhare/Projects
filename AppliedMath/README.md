# Modeling Matchmaking on Dating Apps — From Math to Machine Learning

This repository contains two connected projects exploring how mathematics and data science can model human compatibility on dating apps.  
Both projects use anonymized OkCupid profile data to investigate how shared traits like religion, education, and lifestyle choices can be quantified into compatibility scores.

---

## 🧮 Project 1: Modeling Matchmaking on Dating Apps Using Linear Algebra (AM50)

### Summary
This project explores whether linear algebra can be used to simulate compatibility on dating platforms. Using seven categorical traits — **diet, drinks, smokes, education, body type, pets, and religion** — I constructed a matrix representation of user profiles and tested three mathematical models:

- **Unweighted dot product** – treats all traits equally  
- **Weighted dot product** – gives more importance to religion and education  
- **Weighted trait similarity** – penalizes differences, rewarding closeness on key traits

### Key Findings
- The **similarity model** produced more balanced and interpretable results than the dot product models.  
- It generated thousands of mutual matches with realistic alignment in religion and education.  
- Demonstrated how basic math can capture aspects of compatibility, even without behavioral data.

### Technical Notes
Python • NumPy • pandas • seaborn • matplotlib  
Dataset: [OkCupid Profiles Dataset (Kaggle)](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles)

### Takeaway
Linear algebra provides a transparent, interpretable foundation for understanding compatibility, but it’s limited by how traits are encoded and cannot fully capture dynamic preferences.

---

## 🤖 Project 2: Modeling Matchmaking on Dating Apps Using Machine Learning (ME315)

### Summary
This project builds directly on the AM50 model — extending it from pure math to supervised machine learning.  
The same OkCupid dataset was used to create pairwise user features (trait differences and similarities), enabling both regression and classification tasks.

### Methods
- Regression models: **Linear, Ridge, Decision Tree, KNN, Random Forest** to predict compatibility scores  
- Classification models: **Logistic Regression, Naive Bayes, Random Forest** to predict whether two users “match”  
- Feature importances examined for interpretability

### Key Results
- **Random Forest** achieved the best performance (**R² ≈ 0.999, AUC ≈ 0.81**)  
- The model naturally prioritized **religion** and **education**, matching intuitive human logic  
- Compared model behavior and trade-offs between exploration (recall) and precision

### Technical Notes
Python • scikit-learn • NumPy • pandas • matplotlib  
Same Kaggle OkCupid dataset subset (≈1,000 users × 499k pairs)

### Takeaway
Machine learning successfully generalized the mathematical logic from AM50, learning to mimic human-aligned compatibility.  
This continuation shows how interpretable ML can balance precision and recall — echoing real-world dating app philosophies.

---

## 🌉 Connecting the Two Projects

These two projects tell a continuous story:

| Stage | Approach | Focus | Key Outcome |
|:------|:----------|:-------|:-------------|
| **AM50** | Linear algebra & weighted similarity | Mathematical modeling of compatibility | Built transparent, interpretable baseline |
| **ME315** | Supervised machine learning | Predictive modeling of compatibility | Captured complex, non-linear relationships and realistic ranking |

Together, they trace a path from **mathematical abstraction → data-driven prediction**, showing how an idea born in applied math evolved into an interpretable ML framework.

---

## ✨ Reflections

Both studies highlight the tension between **simplicity and realism** in modeling human relationships.  
They also emphasize the importance of transparency in algorithmic matchmaking — showing that while models can approximate compatibility, true connection remains far more nuanced than data alone.

---

## 🧠 References
- Sharabi, L. (2022). *How Do Dating Apps Work?* Harvard Data Science Review.  
- Rudder, C. (2014). *Inside OkCupid: The Math of Online Dating.* TED Talk.  
- *Kaggle: OkCupid Profiles Dataset.*  
- Karkeh Abadi & Prabhakar (2017). *Stable Matchings in Metric Spaces.*  
- Malysz, M. (2016). *OkCupid: The Math Behind Online Dating.* AMS Blog.
