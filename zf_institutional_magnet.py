import hashlib, time; def generate_institutional_signal(): ts = str(int(time.time() // 86400)); sig = hashlib.sha3_256(f"ZHQ_{ts}".encode()).hexdigest(); return f"INST-{sig[:12].upper()}"
