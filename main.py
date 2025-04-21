import pandas as pd
import joblib
import tkinter as tk
from tkinter import messagebox

model = joblib.load('permeability_model.pkl')

def predict():
    try:
        ai = float(entry_ai.get())
        si = float(entry_si.get())
        vp_vs = float(entry_vp_vs.get())
        lambda_rho = float(entry_lambda_rho.get())
        mu_rho = float(entry_mu_rho.get())
        pr = float(entry_pr.get())
        phin = float(entry_phin.get())

        input_df = pd.DataFrame([[ai, si, vp_vs, lambda_rho, mu_rho, pr, phin]],
                                columns=['AI', 'SI', 'Vp/Vs', 'Lambda_Rho', 'Mu_Rho', 'Poisson_Ratio', 'PHInoise'])
        prediction = model.predict(input_df)[0]
        result_var.set(f"Predicted Permeability: {round(prediction, 4)} mD")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Permeability Prediction")

labels = ["Acoustic Impedance (AI)",
          "Shear Impedance (SI)",
          "Vp/Vs",
          "λρ",
          "µρ",
          "Poisson Ratio",
          "Porosity (in decimal)"]

entries = []

for i, label_text in enumerate(labels):
    tk.Label(root, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_ai, entry_si, entry_vp_vs, entry_lambda_rho, entry_mu_rho, entry_pr, entry_phin = entries

tk.Button(root, text="Predict", command=predict).grid(row=7, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=('Arial', 12, 'bold')).grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
