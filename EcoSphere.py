import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="EcoSphere.ai Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR A VIBRANT DARK THEME ---
st.markdown("""
<style>
/* --- Main App Styling (Dark Theme) --- */
:root {
    --primary-color: #10B981; /* Vibrant Green */
    --background-color: #0F172A; /* Slate-900 */
    --secondary-background-color: #1E293B; /* Slate-800 */
    --text-color: #E2E8F0; /* Slate-200 */
    --h-color: #FFFFFF;
    --card-color: #1E293B; /* Slate-800 */
    --accent-color: #F59E0B; /* Amber-500 */
}

html, body, [class*="st-"] {
    background-color: var(--background-color);
    color: var(--text-color);
}

h1, h2, h3 {
    color: var(--h-color);
    font-family: 'Inter', sans-serif;
}

/* --- Sidebar Styling --- */
[data-testid="stSidebar"] {
    background-color: var(--secondary-background-color);
    border-right: 1px solid #334155; /* Slate-700 */
}
[data-testid="stSidebar"] .stButton button {
    background-color: transparent;
    color: var(--text-color);
    border: none;
    text-align: left;
    padding: 10px;
    width: 100%;
    border-radius: 8px;
    font-size: 16px;
    transition: background-color 0.2s, color 0.2s;
}
[data-testid="stSidebar"] .stButton button:hover {
    background-color: #334155; /* Slate-700 */
    color: var(--h-color);
}
[data-testid="stSidebar"] .stButton button.active {
    background-color: var(--primary-color);
    color: var(--h-color);
    font-weight: bold;
}
[data-testid="stSidebar"] h1 {
    color: var(--primary-color);
}

/* --- Metric & Card Styling --- */
[data-testid="stMetric"], .card {
    background-color: var(--card-color);
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* --- Button Styling --- */
.stButton>button {
    border-radius: 8px;
    border: 2px solid var(--primary-color);
    background-color: var(--primary-color);
    color: white;
    font-weight: bold;
    padding: 10px 24px;
    transition: all 0.3s ease-in-out;
}
.stButton>button:hover {
    background-color: #059669; /* Darker Green */
    border-color: #059669;
}

/* --- Plotly Chart Background --- */
.plotly-chart {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --- DATA & MODEL LOADING ---
@st.cache_data
def load_data(filepath):
    """Loads the final dataset, caching it for performance."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        st.error(f"Error: The data file '{filepath}' was not found. Please ensure it's in the app directory.")
        return None

@st.cache_resource
def load_model(filepath):
    """Loads the trained ML model, caching it for performance."""
    try:
        return joblib.load(filepath)
    except FileNotFoundError:
        st.error(f"Error: The model file '{filepath}' was not found. Please ensure it's in the app directory.")
        return None

df = load_data('EcoSphereAI_Final.csv')
model = load_model('EcoSphereAI_RFModel.pkl')

# Set default plotly template
px.defaults.template = "plotly_dark"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("EcoSphere.ai 🌱")

# Use st.session_state to track the active page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name

pages = {
    "Home": "🏠 Home",
    "Analytics": "📊 Fleet Analytics",
    "Predictor": "🤖 CO₂ Emission Predictor",
    "Optimizer": "🗺️ Route Optimizer"
}

for page_key, page_title in pages.items():
    is_active = "active" if st.session_state.page == page_key else ""
    st.sidebar.button(page_title, on_click=set_page, args=(page_key,), type="secondary", use_container_width=True)


# --- PAGE 1: HOME ---
if st.session_state.page == "Home":
    st.title("Welcome to the EcoSphere.ai Dashboard")
    st.markdown("### AI-Driven Insights for Sustainable Transportation")
    st.markdown("""
        Transportation accounts for nearly a quarter of global CO₂ emissions. Inefficient logistics not only harms the environment but also increases operational costs.
        **EcoSphere.ai** addresses this by leveraging a high-accuracy machine learning model to predict and minimize vehicle carbon emissions.
    """)

    st.image("https://placehold.co/1200x400/0F172A/10B981?text=EcoSphere.ai&font=inter", use_column_width=True)

    st.markdown("---")
    st.subheader("Dashboard Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card'><h4>📊 Fleet Analytics</h4><p>Dive deep into your fleet's emission data. Use interactive filters to analyze performance and identify high-emission assets.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'><h4>🤖 CO₂ Predictor & What-If Analysis</h4><p>Forecast CO₂ emissions instantly and simulate how improvements in maintenance or load can reduce your carbon footprint.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='card'><h4>🗺️ Route Optimizer</h4><p>Simulate routes to find the most carbon-efficient path, complete with estimated fuel cost savings to align environmental goals with financial incentives.</p></div>", unsafe_allow_html=True)
    st.success("Navigate through the dashboard using the modern, icon-based menu on the left.")


# --- PAGE 2: FLEET ANALYTICS ---
elif st.session_state.page == "Analytics" and df is not None:
    st.title("📊 Fleet Analytics Dashboard")
    st.markdown("Analyze fleet-wide emissions and identify key performance indicators.")

    # --- Sidebar Filters ---
    st.sidebar.header("Dashboard Filters")
    vehicle_types = st.sidebar.multiselect("Vehicle Type", options=df['vehicle_type'].unique(), default=df['vehicle_type'].unique())
    fuel_types = st.sidebar.multiselect("Fuel Type", options=df['fuel_type'].unique(), default=df['fuel_type'].unique())
    age_range = st.sidebar.slider("Vehicle Age", int(df['vehicle_age'].min()), int(df['vehicle_age'].max()), (int(df['vehicle_age'].min()), int(df['vehicle_age'].max())))

    filtered_df = df[(df['vehicle_type'].isin(vehicle_types)) & (df['fuel_type'].isin(fuel_types)) & (df['vehicle_age'] >= age_range[0]) & (df['vehicle_age'] <= age_range[1])]

    if not filtered_df.empty:
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Vehicles", f"{len(filtered_df):,}")
        col2.metric("Avg. CO₂ (g/km)", f"{filtered_df['co2_emission'].mean():.2f}")
        col3.metric("Avg. Mileage (km/L)", f"{filtered_df['mileage_kmpl'].mean():.2f}")
        
        # Find the vehicle type with the highest average emissions
        top_emitter = filtered_df.groupby('vehicle_type')['co2_emission'].mean().idxmax()
        col4.metric("Top Emitter", top_emitter)

        st.markdown("---")
        col1, col2 = st.columns([2, 1])

        with col1:
            fig_scatter = px.scatter(
                filtered_df, x='mileage_kmpl', y='co2_emission',
                color='fuel_type', title='<b>Mileage vs. CO₂ Emissions</b>',
                labels={'mileage_kmpl': 'Mileage (km/L)', 'co2_emission': 'CO₂ Emission (g/km)'},
                color_discrete_sequence=px.colors.qualitative.Plotly
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

        with col2:
            fuel_dist = filtered_df['fuel_type'].value_counts().reset_index()
            fuel_dist.columns = ['fuel_type', 'count']
            fig_pie = px.pie(
                fuel_dist, names='fuel_type', values='count',
                title='<b>Fleet Fuel Distribution</b>', hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Plotly
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
        fig_hist = px.histogram(
            filtered_df, x='co2_emission', nbins=50,
            color_discrete_sequence=['#10B981'],
            title='<b>Distribution of CO₂ Emissions</b>',
            labels={'co2_emission': 'CO₂ Emission (g/km)'}
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.warning("No data matches the selected filters.")


# --- PAGE 3: EMISSION PREDICTOR & WHAT-IF ANALYSIS ---
elif st.session_state.page == "Predictor" and model is not None and df is not None:
    st.title("🤖 Real-Time CO₂ Predictor")
    st.markdown("Fill in vehicle details for an instant forecast and perform 'What-If' analysis.")

    if 'prediction' not in st.session_state:
        st.session_state.prediction = None
    if 'base_input' not in st.session_state:
        st.session_state.base_input = None

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Vehicle Parameters")
        with st.form("prediction_form"):
            v_type = st.selectbox("Vehicle Type", df['vehicle_type'].unique(), key="pred_v_type")
            f_type = st.selectbox("Fuel Type", df['fuel_type'].unique(), key="pred_f_type")
            mileage = st.slider("Mileage (km/L)", 5.0, 25.0, 10.0, 0.1, key="pred_mileage")
            load = st.slider("Load Weight (kg)", 0, 20000, 500, 50, key="pred_load")
            age = st.slider("Vehicle Age (years)", 0, 20, 5, 1, key="pred_age")
            maint = st.slider("Maintenance Efficiency", 0.7, 1.0, 0.85, 0.01, key="pred_maint")
            submitted = st.form_submit_button("Predict Emission")

    with col2:
        st.subheader("Prediction Result")
        if submitted:
            emission_factors = {"Petrol": 2.31, "Diesel": 2.68, "Natural Gas": 2.74, "Ethanol": 1.91, "EV": 0.0}
            e_factor = emission_factors.get(f_type, 2.31)
            
            base_input_data = {
                "vehicle_type": v_type, "fuel_type": f_type, "mileage_kmpl": mileage,
                "load_weight": load, "emission_factor": e_factor, "vehicle_age": age,
                "maintenance_efficiency": maint
            }
            st.session_state.base_input = pd.DataFrame([base_input_data])
            st.session_state.prediction = model.predict(st.session_state.base_input)[0]

        if st.session_state.prediction is not None:
            prediction_val = st.session_state.prediction
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number", value=prediction_val,
                title={'text': "Predicted CO₂ (g/km)", 'font': {'size': 24, 'color': 'white'}},
                gauge={
                    'axis': {'range': [df['co2_emission'].min(), 450], 'tickwidth': 1, 'tickcolor': "white"},
                    'bar': {'color': "#10B981"},
                    'steps': [
                        {'range': [0, 150], 'color': '#059669'},
                        {'range': [150, 300], 'color': '#F59E0B'},
                        {'range': [300, 450], 'color': '#EF4444'}],
                }))
            fig_gauge.update_layout(height=280, margin=dict(l=20, r=20, t=60, b=20), paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig_gauge, use_container_width=True)

    if st.session_state.prediction is not None:
        st.markdown("---")
        st.subheader("💡 What-If Analysis")
        st.markdown("Simulate improvements to see potential CO₂ reductions.")
        
        what_if_param = st.selectbox("Parameter to Improve", ["Maintenance Efficiency", "Load Weight"])
        
        if what_if_param == "Maintenance Efficiency":
            improved_maint = st.slider(
                "Improved Maintenance Efficiency", 
                float(st.session_state.base_input['maintenance_efficiency']), 1.0, 
                float(st.session_state.base_input['maintenance_efficiency']), 0.01
            )
            what_if_input = st.session_state.base_input.copy()
            what_if_input['maintenance_efficiency'] = improved_maint
        else: # Load Weight
            reduced_load = st.slider(
                "Reduced Load Weight (kg)", 0, 
                int(st.session_state.base_input['load_weight']), 
                int(st.session_state.base_input['load_weight']), 50
            )
            what_if_input = st.session_state.base_input.copy()
            what_if_input['load_weight'] = reduced_load

        new_prediction = model.predict(what_if_input)[0]
        reduction = st.session_state.prediction - new_prediction
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Original Prediction (g/km)", f"{st.session_state.prediction:.2f}")
        col2.metric("New Prediction (g/km)", f"{new_prediction:.2f}")
        col3.metric("Potential Reduction (g/km)", f"{reduction:.2f}", delta=f"{reduction:.2f}")


# --- PAGE 4: ROUTE OPTIMIZER ---
elif st.session_state.page == "Optimizer" and model is not None:
    st.title("🗺️ Route Emission & Cost Optimizer")
    st.markdown("Find the most eco-friendly and cost-effective route for your journey.")

    G = nx.Graph()
    cities = {
        "Nagpur": (21.1458, 79.0882), "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.7041, 77.1025), "Pune": (18.5204, 73.8567),
        "Bangalore": (12.9716, 77.5946), "Chennai": (13.0827, 80.2707),
        "Hyderabad": (17.3850, 78.4867), "Kolkata": (22.5726, 88.3639)
    }
    G.add_nodes_from(cities.keys())
    G.add_edge("Nagpur", "Mumbai", distance=825); G.add_edge("Nagpur", "Hyderabad", distance=500)
    G.add_edge("Nagpur", "Delhi", distance=1080); G.add_edge("Mumbai", "Pune", distance=150)
    G.add_edge("Mumbai", "Bangalore", distance=980); G.add_edge("Pune", "Hyderabad", distance=560)
    G.add_edge("Pune", "Bangalore", distance=840); G.add_edge("Hyderabad", "Bangalore", distance=575)
    G.add_edge("Hyderabad", "Chennai", distance=627); G.add_edge("Bangalore", "Chennai", distance=347)
    G.add_edge("Delhi", "Kolkata", distance=1470); G.add_edge("Nagpur", "Kolkata", distance=1120)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Route & Vehicle Details")
        start_city = st.selectbox("Start City", cities.keys(), index=0)
        end_city = st.selectbox("End City", cities.keys(), index=1)

        with st.expander("Vehicle Parameters for Simulation", expanded=True):
            v_type_r = st.selectbox("Vehicle Type", df['vehicle_type'].unique(), key="r_v_type")
            f_type_r = st.selectbox("Fuel Type", ["Petrol", "Diesel"], key="r_f_type") # Simplified for cost
            mileage_r = st.slider("Mileage (km/L)", 5.0, 25.0, 10.0, 0.1, key="r_mileage")
            load_r = st.slider("Load Weight (kg)", 0, 20000, 500, 50, key="r_load")
            age_r = st.slider("Vehicle Age (years)", 0, 20, 5, 1, key="r_age")
            maint_r = st.slider("Maintenance Efficiency", 0.7, 1.0, 0.85, 0.01, key="r_maint")
            fuel_price = st.number_input("Fuel Price (₹/L)", value=104.0 if f_type_r == "Petrol" else 92.0, step=0.5)

        find_route_btn = st.button("Find Optimal Route")

    with col2:
        st.subheader("Route Analysis Results")
        if find_route_btn:
            if start_city == end_city: st.error("Start and End cities cannot be the same.")
            else:
                with st.spinner('Analyzing routes...'):
                    emission_factors = {"Petrol": 2.31, "Diesel": 2.68}
                    vehicle_input = pd.DataFrame({
                        "vehicle_type": [v_type_r], "fuel_type": [f_type_r], "mileage_kmpl": [mileage_r],
                        "load_weight": [load_r], "emission_factor": [emission_factors.get(f_type_r)],
                        "vehicle_age": [age_r], "maintenance_efficiency": [maint_r]
                    })
                    emission_per_km = model.predict(vehicle_input)[0]

                    paths = list(nx.all_simple_paths(G, source=start_city, target=end_city, cutoff=4))
                    if not paths:
                        st.warning("No routes found within 4 stops.")
                    else:
                        route_results = []
                        for path in paths:
                            dist = sum(G[path[i]][path[i+1]]['distance'] for i in range(len(path)-1))
                            fuel_needed = dist / mileage_r
                            cost = fuel_needed * fuel_price
                            emission_kg = (dist * emission_per_km) / 1000
                            route_results.append({
                                "Route": " → ".join(path), "Distance (km)": dist,
                                "Total CO₂ (kg)": emission_kg, "Est. Fuel Cost (₹)": cost
                            })

                        results_df = pd.DataFrame(route_results).sort_values(by="Total CO₂ (kg)").reset_index(drop=True)
                        best_route = results_df.iloc[0]
                        worst_route = results_df.iloc[-1]
                        
                        st.success(f"**Optimal Route:** {best_route['Route']}")
                        
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Lowest CO₂ Emissions", f"{best_route['Total CO₂ (kg)']:.2f} kg")
                        c2.metric("Estimated Cost", f"₹ {best_route['Est. Fuel Cost (₹)']:.2f}")
                        if len(results_df) > 1:
                           cost_saving = worst_route['Est. Fuel Cost (₹)'] - best_route['Est. Fuel Cost (₹)']
                           c3.metric("Potential Savings", f"₹ {cost_saving:.2f}", help=f"Compared to the least efficient route ({worst_route['Route']})")

                        st.dataframe(results_df.style.highlight_min(subset=['Total CO₂ (kg)', 'Est. Fuel Cost (₹)'], color='#059669').format({'Total CO₂ (kg)': '{:.2f}', 'Est. Fuel Cost (₹)': '₹{:.2f}'}))
                        
                        best_path_nodes = best_route['Route'].split(' → ')
                        fig_map = go.Figure()
                        for edge in G.edges():
                            fig_map.add_trace(go.Scattermapbox(lat=[cities[edge[0]][0], cities[edge[1]][0]], lon=[cities[edge[0]][1], cities[edge[1]][1]], mode='lines', line=dict(width=1, color='grey'), hoverinfo='none'))
                        fig_map.add_trace(go.Scattermapbox(lat=[cities[c][0] for c in cities], lon=[cities[c][1] for c in cities], mode='markers+text', marker=dict(size=10, color='#1E293B', symbol='circle', opacity=0.8), text=list(cities.keys()), textposition="bottom right", hoverinfo='text'))
                        fig_map.add_trace(go.Scattermapbox(lat=[cities[c][0] for c in best_path_nodes], lon=[cities[c][1] for c in best_path_nodes], mode='lines', line=dict(width=4, color='#10B981'), name="Optimal Route", hoverinfo='none'))
                        
                        fig_map.update_layout(title='<b>Route Network & Optimal Path</b>', mapbox_style="carto-darkmatter", mapbox_center_lon=79, mapbox_center_lat=21, mapbox_zoom=3.8, showlegend=False, margin={"r":0,"t":40,"l":0,"b":0}, paper_bgcolor='rgba(0,0,0,0)', geo_bgcolor='rgba(0,0,0,0)')
                        st.plotly_chart(fig_map, use_container_width=True)
        else:
             st.info("Select your route and vehicle details to begin the analysis.")

elif df is None or model is None:
    st.error("Dashboard cannot be loaded due to missing files.")