import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TerraSense AI | Command Center",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "flame" not in st.session_state:
    st.session_state.flame = False

if "vibration" not in st.session_state:
    st.session_state.vibration = True

if "flood" not in st.session_state:
    st.session_state.flood = False


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🌍 TerraSense AI")
    st.caption("Emergency Monitoring Console")

    st.divider()

    st.subheader("SYSTEM")

    st.success("● ESP32  ONLINE")
    st.success("● EDGE AI  ACTIVE")

    st.divider()

    st.subheader("SENSOR INPUT")

    st.session_state.flame = st.toggle(
        "🔥 Flame Detection",
        value=st.session_state.flame
    )

    st.session_state.vibration = st.toggle(
        "📳 Ground Vibration",
        value=st.session_state.vibration
    )

    st.session_state.flood = st.toggle(
        "🌊 Flood Detection",
        value=st.session_state.flood
    )

    st.divider()

    st.subheader("NODE")

    st.write("**Node ID:** TS-001")
    st.write("**Location:** Monitoring Station 01")
    st.write("**Connection:** USB / Serial")
    st.write("**AI Mode:** Edge Inference")

    st.divider()

    st.caption(
        "Demo controls will be replaced by live ESP32 telemetry."
    )


# =========================================================
# HEADER
# =========================================================

header1, header2 = st.columns([5, 1])

with header1:

    st.title("🌍 TerraSense AI")

    st.caption(
        "MULTI-HAZARD ENVIRONMENTAL EARLY WARNING COMMAND CENTER"
    )

with header2:

    st.success("● LIVE")


st.divider()


# =========================================================
# TOP SYSTEM METRICS
# =========================================================

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric(
        "Monitoring Node",
        "TS-001"
    )

with m2:
    st.metric(
        "ESP32",
        "ONLINE"
    )

with m3:
    st.metric(
        "Edge AI",
        "ACTIVE"
    )

with m4:
    st.metric(
        "Active Hazards",
        str(
            int(st.session_state.flame)
            + int(st.session_state.flood)
            + int(st.session_state.vibration)
        )
    )

with m5:
    st.metric(
        "Last Update",
        datetime.now().strftime("%H:%M:%S")
    )


# =========================================================
# RISK CALCULATION
# =========================================================

# FIRE

if st.session_state.flame:
    fire_risk = "CRITICAL"
    fire_score = 95
else:
    fire_risk = "LOW"
    fire_score = 5


# FLOOD

if st.session_state.flood:
    flood_risk = "CRITICAL"
    flood_score = 95
else:
    flood_risk = "LOW"
    flood_score = 5


# LANDSLIDE

if st.session_state.vibration and st.session_state.flood:

    landslide_risk = "CRITICAL"
    landslide_score = 94

elif st.session_state.vibration:

    landslide_risk = "HIGH"
    landslide_score = 72

else:

    landslide_risk = "LOW"
    landslide_score = 8


# =========================================================
# COMMAND STATUS
# =========================================================

st.subheader("🚨 Command Status")

if (
    fire_risk == "CRITICAL"
    or flood_risk == "CRITICAL"
    or landslide_risk == "CRITICAL"
):

    st.error(
        "🚨 CRITICAL ALERT — Immediate attention required"
    )

elif landslide_risk == "HIGH":

    st.warning(
        "⚠️ HIGH RISK — Abnormal environmental activity detected"
    )

else:

    st.success(
        "🟢 ALL SYSTEMS NORMAL — No active environmental threats"
    )


# =========================================================
# LIVE SENSOR TELEMETRY
# =========================================================

st.subheader("📡 Live Sensor Telemetry")

s1, s2, s3, s4 = st.columns(4)

# FIRE

with s1:

    with st.container(border=True):

        st.subheader("🔥 Flame")

        if st.session_state.flame:

            st.error("DETECTED")
            st.write("Fire condition detected")

        else:

            st.success("NORMAL")
            st.write("No flame detected")


# FLOOD

with s2:

    with st.container(border=True):

        st.subheader("🌊 Flood")

        if st.session_state.flood:

            st.error("DETECTED")
            st.write("Flood condition detected")

        else:

            st.success("NORMAL")
            st.write("Water level normal")


# VIBRATION

with s3:

    with st.container(border=True):

        st.subheader("📳 Ground")

        if st.session_state.vibration:

            st.warning("DETECTED")
            st.write("Possible ground movement")

        else:

            st.success("NORMAL")
            st.write("Ground conditions stable")


# AI

with s4:

    with st.container(border=True):

        st.subheader("🧠 Edge AI")

        st.success("ACTIVE")

        st.write("Risk engine operational")


# =========================================================
# HAZARD RISK MATRIX
# =========================================================

st.subheader("🎯 Hazard Risk Assessment")

r1, r2, r3 = st.columns(3)


# FIRE CARD

with r1:

    with st.container(border=True):

        st.markdown("### 🔥 Forest Fire")

        if fire_risk == "CRITICAL":

            st.error("CRITICAL")

        else:

            st.success("LOW")

        st.progress(fire_score / 100)

        st.caption(
            f"Risk score: {fire_score}%"
        )


# FLOOD CARD

with r2:

    with st.container(border=True):

        st.markdown("### 🌊 Flood")

        if flood_risk == "CRITICAL":

            st.error("CRITICAL")

        else:

            st.success("LOW")

        st.progress(flood_score / 100)

        st.caption(
            f"Risk score: {flood_score}%"
        )


# LANDSLIDE CARD

with r3:

    with st.container(border=True):

        st.markdown("### ⛰️ Landslide")

        if landslide_risk == "CRITICAL":

            st.error("CRITICAL")

        elif landslide_risk == "HIGH":

            st.warning("HIGH")

        else:

            st.success("LOW")

        st.progress(landslide_score / 100)

        st.caption(
            f"Risk score: {landslide_score}%"
        )


# =========================================================
# LANDSLIDE INTELLIGENCE
# =========================================================

st.subheader("⛰️ Landslide Intelligence")

l1, l2, l3, l4 = st.columns(4)

with l1:

    st.metric(
        "AI Risk Score",
        f"{landslide_score}%"
    )

with l2:

    st.metric(
        "Ground Movement",
        "DETECTED"
        if st.session_state.vibration
        else "NORMAL"
    )

with l3:

    st.metric(
        "Flood Correlation",
        "ACTIVE"
        if st.session_state.flood
        else "NONE"
    )

with l4:

    st.metric(
        "Risk Level",
        landslide_risk
    )


# =========================================================
# ALERT CENTER
# =========================================================

st.subheader("🚨 Alert Center")

alerts = []


if st.session_state.flame:

    alerts.append({
        "TIME": datetime.now().strftime("%H:%M:%S"),
        "HAZARD": "🔥 FIRE",
        "RISK": "CRITICAL",
        "PRIORITY": "CRITICAL",
        "STATUS": "ACTIVE"
    })


if st.session_state.flood:

    alerts.append({
        "TIME": datetime.now().strftime("%H:%M:%S"),
        "HAZARD": "🌊 FLOOD",
        "RISK": "CRITICAL",
        "PRIORITY": "CRITICAL",
        "STATUS": "ACTIVE"
    })


if st.session_state.vibration:

    alerts.append({
        "TIME": datetime.now().strftime("%H:%M:%S"),
        "HAZARD": "⛰️ LANDSLIDE",
        "RISK": landslide_risk,
        "PRIORITY": landslide_risk,
        "STATUS": "ACTIVE"
    })


if alerts:

    alert_df = pd.DataFrame(alerts)

    st.dataframe(
        alert_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No active alerts.")


# =========================================================
# MAP + NODE INFORMATION
# =========================================================

st.subheader("📍 Regional Monitoring")

map_col, node_col = st.columns([2.2, 1])

with map_col:

    map_data = pd.DataFrame({
        "latitude": [28.6139],
        "longitude": [77.2090]
    })

    st.map(
        map_data,
        latitude="latitude",
        longitude="longitude",
        zoom=10
    )

    st.caption(
        "TS-001 • Demonstration coordinates"
    )


with node_col:

    st.write("### Node TS-001")

    with st.container(border=True):

        st.write("🟢 **Status:** ONLINE")
        st.write("🟢 **Power:** STABLE")
        st.write("🟢 **Connectivity:** GOOD")
        st.write("🧠 **Inference:** EDGE")
        st.write("📡 **Telemetry:** ACTIVE")

        st.divider()

        st.write("**Hazard Sensors**")

        st.write(
            "🔥 Flame      "
            + ("DETECTED" if st.session_state.flame else "NORMAL")
        )

        st.write(
            "📳 Vibration  "
            + ("DETECTED" if st.session_state.vibration else "NORMAL")
        )

        st.write(
            "🌊 Flood      "
            + ("DETECTED" if st.session_state.flood else "NORMAL")
        )


# =========================================================
# RISK TREND
# =========================================================

st.subheader("📈 Environmental Risk Trend")

trend = pd.DataFrame({

    "Time": [
        "09:35",
        "09:36",
        "09:37",
        "09:38",
        "09:39",
        "09:40",
        "09:41",
        "09:42",
        "09:43",
        "NOW"
    ],

    "Risk": [
        8,
        11,
        14,
        18,
        25,
        32,
        40,
        49,
        61,
        landslide_score
    ]
})


st.line_chart(
    trend.set_index("Time"),
    height=300
)


# =========================================================
# RESPONSE PROTOCOL
# =========================================================

st.subheader("🛡️ Recommended Response")

if fire_risk == "CRITICAL":

    st.error(
        "🔥 FIRE RESPONSE\n\n"
        "Isolate the affected area and initiate "
        "fire emergency procedures."
    )

elif flood_risk == "CRITICAL":

    st.error(
        "🌊 FLOOD RESPONSE\n\n"
        "Activate flood response measures and "
        "monitor water conditions."
    )

elif landslide_risk == "CRITICAL":

    st.error(
        "⛰️ LANDSLIDE RESPONSE\n\n"
        "Abnormal ground movement combined with "
        "flood conditions. Immediate assessment required."
    )

elif landslide_risk == "HIGH":

    st.warning(
        "⛰️ LANDSLIDE PRECAUTION\n\n"
        "Inspect the monitored area and maintain "
        "continuous vibration monitoring."
    )

else:

    st.success(
        "🟢 MONITORING MODE\n\n"
        "No emergency response currently required."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🌍 TerraSense AI  |  Edge-first Multi-Hazard "
    "Environmental Early Warning System"
)

st.caption(
    "Flood • Landslide • Forest Fire  |  SIH Prototype"
)