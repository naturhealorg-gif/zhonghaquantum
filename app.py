import streamlit as st
import pandas as pd
import numpy as np
import datetime
import hashlib
import hmac
import os
import time

# --- ZUHRI FORMALISM: INTEGRATED ZF-CORE ENGINE ---
# (Fungsi engine tetap sama sesuai kode asli Anda)
def get_master_seed():
    try:
        with open("master_seed.bin", "rb") as f:
            return f.read().hex()
    except:
        return os.environ.get("ZHQ_MASTER_SEED", "DEFAULT_QUANTUM_SEED_2026")

class ZHQ_Sovereign_Engine:
    def __init__(self):
        self.master_seed = get_master_seed()
        self.total_supply = 1000000.0

    def get_internal_valuation(self):
        base_price = 1500.0
        time_factor = datetime.datetime.now().hour * 0.15
        return base_price + time_factor

    def generate_hash(self, data):
        return hmac.new(self.master_seed.encode(), data.encode(), hashlib.sha3_512).hexdigest()

    def run_autopilot_audit(self):
        audit_tag = f"AUDIT-{datetime.datetime.utcnow().strftime('%Y%m%d')}"
        return self.generate_hash(audit_tag)[:20].upper()

    def auto_burn_mechanism(self, transaction_volume):
        burn_rate = transaction_volume * 0.01
        self.total_supply -= burn_rate
        return burn_rate

    def execute_autonomous_tx(self, target, amount):
        burn_amount = self.auto_burn_mechanism(amount)
        tx_hash = self.generate_hash(f"{target}{amount}{time.time()}")
        fee = amount * 0.0005
        return {
            "tx_id": f"ZHQ-TX-{tx_hash[:20].upper()}",
            "fee": fee,
            "net": amount - fee,
            "burned": burn_amount
        }

    def write_sovereign_audit(self, tx_data):
        audit_entry = f"[{datetime.datetime.utcnow().isoformat()}] TX: {tx_data['tx_id']} | BURN: {tx_data['burned']:.4f} ZHQ | STATUS: VERIFIED\n"
        with open("zhq_sovereign_ledger.log", "a") as f:
            f.write(audit_entry)
        return True

    def get_public_ledger(self):
        try:
            with open("zhq_sovereign_ledger.log", "r") as f:
                return f.readlines()[-10:]
        except:
            return ["Log kosong. Inisialisasi transaksi diperlukan."]

    def get_ledger_integrity_hash(self):
        try:
            with open("zhq_sovereign_ledger.log", "r") as f:
                content = f.read()
                return hashlib.sha3_256(content.encode()).hexdigest().upper()
        except:
            return "LOG_INITIALIZING_HASH..."

    def zf_core_network_sensor(self):
        current_value = self.get_internal_valuation()
        resonance_index = hashlib.sha3_256(f"{current_value}".encode()).hexdigest()
        smart_money_inflow = (int(resonance_index[:4], 16) % 1000000) + 500000.0
        whale_activity_status = "STABLE / ACCUMULATION" if smart_money_inflow > 750000 else "MONITORING"
        return {
            "resonance_index": resonance_index[:16].upper(),
            "inflow_volume_usd": smart_money_inflow,
            "status": whale_activity_status
        }

engine = ZHQ_Sovereign_Engine()

# --- GATEKEEPER ---
def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], os.environ.get("ZHQ_ACCESS_KEY", "PROTECTED")):
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False
            
    if "password_correct" not in st.session_state:
        st.title("ZHQ | RESTRICTED CORE")
        st.text_input("INPUT KUNCI BINARY:", type="password", on_change=password_entered, key="password")
        st.stop()
    elif not st.session_state["password_correct"]:
        st.error("AKSES DITOLAK: Kunci Tidak Valid.")
        st.stop()

check_password()

# --- UI & INTERFACE: BLOOMBERG QUANTUM STYLE ---
st.set_page_config(page_title="ZHQ | Sovereign Terminal", page_icon="⚛️", layout="wide")

st.markdown("""
<style>
    .stApp { background: #080808; color: #d1d1d1; font-family: 'Courier New', monospace; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .logo-spin { width: 50px; height: 50px; border-radius: 50%; border: 2px solid #00E5FF; animation: spin 10s linear infinite; }
    .header-box { display: flex; align-items: center; gap: 20px; border-bottom: 2px solid #333; padding-bottom: 10px; }
    .metric-card { background: #121212; border: 1px solid #333; padding: 15px; border-radius: 0px; text-align: center; }
    .stMetric { border-left: 4px solid #00E5FF; padding-left: 10px; }
</style>
""", unsafe_allow_html=True)

# Header Terminal
st.markdown("""<div class='header-box'>
    <img src='https://raw.githubusercontent.com/naturhealorg-gif/zhonghaquantum/main/1782533575219.jpg' class='logo-spin'>
    <div><h1 style='color: #00E5FF; margin:0;'>ZHQ TERMINAL v2026</h1><p style='margin:0;'>SYSTEM CLOUD SOVEREIGN | QUANTUM READY</p></div>
</div>""", unsafe_allow_html=True)

# Dashboard Grid
c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Stability", "99.9997%")
with c2: st.metric("Supply (ZHQ)", f"{engine.total_supply:,.0f}")
with c3: st.metric("Price (USD)", f"${engine.get_internal_valuation():,.2f}")
with c4: st.metric("Integrity Tag", engine.run_autopilot_audit()[:8])

st.write("---")

# Main Content
col_a, col_b = st.columns([2, 1])

with col_a:
    st.subheader("📈 MARKET RESONANCE & FLOW")
    # Simulated Bloomberg Chart
    chart_data = pd.DataFrame(np.random.randn(50, 2).cumsum(axis=0), columns=['Price', 'Resonance'])
    st.line_chart(chart_data)
    
    st.subheader("📜 SOVEREIGN LEDGER (STREAMING)")
    ledger = engine.get_public_ledger()
    st.code("".join(ledger), language="text")

with col_b:
    st.subheader("💠 QUANTUM VAULT")
    amount = st.number_input("Amount (ZHQ):", min_value=0.0)
    target = st.text_input("Target Address:")
    if st.button("EXECUTE TX"):
        res = engine.execute_autonomous_tx(target, amount)
        engine.write_sovereign_audit(res)
        st.success("TX VERIFIED")
    
    st.subheader("🛰️ ZF-CORE SENSOR")
    sensor = engine.zf_core_network_sensor()
    st.write(f"STATUS: `{sensor['status']}`")
    st.write(f"LIQUIDITY: `${sensor['inflow_volume_usd']:,.2f}`")
    st.progress(0.78) # Visual indicator
    
    st.info(f"HASH: {engine.get_ledger_integrity_hash()[:20]}...")

# Footer
st.markdown("---")
st.caption("ZHQ ZHONGHA QUANTUM | Institutional Cloud Engine | 2026 | No-Owner Entity")