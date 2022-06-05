import streamlit as st
import sys
from utils import database,plotter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

conn = database.init_connection()

SMC_phenotypes_options="""
Difference_in_Tmax_No_log
Difference_in_slope_No_log
auc_Diff_log
calcy_osteo_No_P_log
calcy_pi_No_P_log
prolify_IL1_log
prolify_PDGF_log
prolify_TGFB1_log
prolifz_CONTROL_log
prolifz_IL1_log
prolifz_PDGF_log
prolifz_TGFB1_log
""".strip().split()

SMC_phenotypes_options=tuple(SMC_phenotypes_options)

first_phenotype = st.selectbox("First phenotype: ",
                               SMC_phenotypes_options)
second_phenotype = st.selectbox("Second phenotype: ",
                                SMC_phenotypes_options)


sql = f"""
SELECT *
FROM sample_SMC_phenotypes
WHERE SMC_phenotype = '{first_phenotype}' OR SMC_phenotype = '{second_phenotype}'
"""

df = pd.read_sql(sql, conn)
df = df.pivot(index='sample_id', columns='SMC_phenotype', values='value')


fig = plt.figure(figsize=(8, 8))
sns.scatterplot(data=df, x=first_phenotype,y=second_phenotype)

st.pyplot(fig)


