# AI-BasedPermeability-Prediction
Machine learning-based approach to predict reservoir permeability using seismic and petrophysical parameters.
# AI-Based Permeability Prediction

##  Objective
Machine learning-based approach to estimate reservoir permeability using seismic and petrophysical parameters in the absence of direct permeability measurements.

##  Features Used
- Acoustic Impedance
- Shear Impedance
- Vp/Vs
- Lambda_rho (λρ)
- Mu_rho (μρ)
- Poisson Ratio
- Porosity

##  Models Applied
- XGBoost
- Random Forest
- LightGBM
- Linear Regression

##  Methodology
1. **Swirr Estimation** using Buckle’s Relationship (C=0.06 for shale/sandstone).
2. **Permeability Estimation** using Timur Model.
3. ML model training and evaluation using residual analysis, scatter plots, and error distributions.

## Results
- **Best performing model:** Random Forest

- **Evaluation Metrics:** Residuals, Feature Importance, Actual vs Predicted plots
- **Generalization:** Suitable for other wells with similar lithology


## 👤 Author
**Divya Meena**  
M.Sc. Tech. Applied Geophysics, IIT (ISM) Dhanbad  
Email: 23mc0036@iitism.ac.in  
GitHub: [DivyyaM](https://github.com/DivyyaM)
