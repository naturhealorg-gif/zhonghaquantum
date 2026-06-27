import streamlit as st
import hashlib
import time
import json
import os
import math

st.set_page_config(page_title="ZHQ INSTITUTIONAL CORE", page_icon="⚛️", layout="wide")

st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at center, #0b1528 0%, #02050a 100%); color: #e2e8f0; }
    .glass-card { background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
    .reaktor-img { width: 140px; height: 140px; border-radius: 50%; border: 4px solid #00E5FF; box-shadow: 0 0 30px #00E5FF; animation: spin 15s linear infinite; }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00E5FF;'>&#9883; ZHONGHAQUANTUM MAINNET</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["⚡ Konsensus Ledger", "📜 Doktrin Kedaulatan"])

with tab1:
    st.write("Sistem beroperasi. Resonansi Kuantum: " + str(1.0 + math.sin(time.time())) )

with tab2:
    st.markdown("## 📜 Doktrin Protokol Kedaulatan")
    st.latex(r'''V_{\text{Haqiqi}}(B, T) = \Psi_{\text{sensor}}(t) \times \left[ Z_c \cdot \sqrt{B} + \int (E_{\text{activity}} \cdot dt) \right]''')
