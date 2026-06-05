import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
from datetime import datetime

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="🏠 Airbnb NYC Price Predictor",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS FOR BEAUTIFUL DESIGN
# ============================================================================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 10px 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .input-section {
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 10px 0;
    }
    
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL AND ENCODERS
# ============================================================================
@st.cache_resource
def load_model():
    saved_objects = joblib.load('airbnb_knn_model.pkl')
    return saved_objects

try:
    saved_objects = load_model()
    model = saved_objects['model']
    STD = saved_objects['num_encod']
    STD_y = saved_objects['num_encod_y']
    OHE = saved_objects['cat_encod']
    OE = saved_objects['cato_encod']
    model_loaded = True
except:
    model_loaded = False
    st.error("❌ Could not load model. Please ensure 'airbnb_knn_model.pkl' is in the directory.")

# ============================================================================
# HEADER WITH ANIMATION
# ============================================================================
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1>🏢 AIRBNB NYC PRICE PREDICTOR 🗽</h1>
        <p style='color: white; font-size: 18px; font-weight: bold;'>
            Predict Your Perfect Listing Price with AI ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# MAIN CONTENT
# ============================================================================
if model_loaded:
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["🎯 PREDICTOR", "📊 ANALYTICS", "ℹ️ ABOUT"])
    
    # ========================================================================
    # TAB 1: PREDICTION
    # ========================================================================
    with tab1:
        st.markdown("""
        <div class='input-section'>
            <h2>📍 Enter Property Details</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Create columns for inputs
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<h3 style='color: white;'>📍 Location</h3>", unsafe_allow_html=True)
            latitude = st.slider("Latitude", 40.5, 40.9, 40.7, 0.01, key="lat")
            longitude = st.slider("Longitude", -74.0, -73.7, -73.95, 0.01, key="lon")
            neighbourhood_group = st.selectbox(
                "Borough",
                ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
            )
            neighbourhood = st.text_input("Neighbourhood", "Manhattan")
        
        with col2:
            st.markdown("<h3 style='color: white;'>🏠 Property Info</h3>", unsafe_allow_html=True)
            room_type = st.selectbox(
                "Room Type",
                ["Entire home/apt", "Private room", "Shared room"]
            )
            minimum_nights = st.slider("Minimum Nights Stay", 1, 365, 30, key="min_nights")
            availability_365 = st.slider("Available Days/Year", 0, 365, 200, key="avail")
        
        with col3:
            st.markdown("<h3 style='color: white;'>⭐ Reviews</h3>", unsafe_allow_html=True)
            number_of_reviews = st.slider("Total Reviews", 0, 500, 50, key="num_rev")
            reviews_per_month = st.slider("Reviews per Month", 0.0, 10.0, 2.5, 0.1, key="rev_month")
            calculated_host_listings_count = st.slider("Host Listings", 1, 300, 5, key="host_list")
        
        # Prediction button with animation
        st.markdown("<div style='text-align: center; margin: 30px 0;'>", unsafe_allow_html=True)
        predict_button = st.button(
            "🚀 PREDICT PRICE",
            use_container_width=True,
            key="predict_btn"
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        if predict_button:
            # Prepare data
            new_data = {
                'latitude': [latitude],
                'longitude': [longitude],
                'minimum_nights': [minimum_nights],
                'number_of_reviews': [number_of_reviews],
                'reviews_per_month': [reviews_per_month],
                'calculated_host_listings_count': [calculated_host_listings_count],
                'availability_365': [availability_365],
                'neighbourhood_group': [neighbourhood_group],
                'neighbourhood': [neighbourhood],
                'room_type': [room_type]
            }
            
            df_new = pd.DataFrame(new_data)
            
            # Transform features
            num_cols = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews',
                       'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
            
            num_trans = STD.transform(df_new[num_cols])
            cat_trans = OHE.transform(df_new[['neighbourhood_group', 'neighbourhood']])
            cato_trans = OE.transform(df_new[['room_type']])
            
            X_new = pd.DataFrame(np.column_stack([num_trans, cat_trans, cato_trans]))
            
            # Predict
            y_pred_scaled = model.predict(X_new)
            y_pred = STD_y.inverse_transform(y_pred_scaled.reshape(-1, 1))[0][0]
            
            # ============================================================
            # BEAUTIFUL PREDICTION DISPLAY
            # ============================================================
            st.markdown("<br>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 2, 1])
            
            with col2:
                st.markdown(f"""
                <div class='prediction-card'>
                    <h2>💰 PREDICTED PRICE</h2>
                    <h1 style='font-size: 80px; margin: 20px 0;'>${y_pred:.2f}</h1>
                    <p style='font-size: 16px; opacity: 0.9;'>Per Night | New York City</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # ============================================================
            # 3D VISUALIZATION
            # ============================================================
            st.markdown("<h3 style='color: white; text-align: center;'>📊 Price Analysis</h3>", unsafe_allow_html=True)
            
            # Create 3D surface plot showing how price varies with key features
            fig = go.Figure()
            
            # Generate prediction range
            lat_range = np.linspace(40.5, 40.9, 20)
            avail_range = np.linspace(0, 365, 20)
            
            prices = []
            for lat in lat_range:
                row = []
                for avail in avail_range:
                    test_data = {
                        'latitude': [lat],
                        'longitude': [longitude],
                        'minimum_nights': [minimum_nights],
                        'number_of_reviews': [number_of_reviews],
                        'reviews_per_month': [reviews_per_month],
                        'calculated_host_listings_count': [calculated_host_listings_count],
                        'availability_365': [avail],
                        'neighbourhood_group': [neighbourhood_group],
                        'neighbourhood': [neighbourhood],
                        'room_type': [room_type]
                    }
                    df_test = pd.DataFrame(test_data)
                    num_trans = STD.transform(df_test[num_cols])
                    cat_trans = OHE.transform(df_test[['neighbourhood_group', 'neighbourhood']])
                    cato_trans = OE.transform(df_test[['room_type']])
                    X_test = pd.DataFrame(np.column_stack([num_trans, cat_trans, cato_trans]))
                    pred_scaled = model.predict(X_test)
                    pred = STD_y.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]
                    row.append(pred)
                prices.append(row)
            
            fig.add_trace(go.Surface(
                x=avail_range,
                y=lat_range,
                z=prices,
                colorscale='Viridis',
                name='Price'
            ))
            
            fig.update_layout(
                title='3D Price Surface: Latitude vs Availability',
                scene=dict(
                    xaxis_title='Availability (days/year)',
                    yaxis_title='Latitude',
                    zaxis_title='Price ($)',
                    camera=dict(
                        eye=dict(x=1.5, y=1.5, z=1.3)
                    ),
                    bgcolor='rgba(0,0,0,0.1)',
                    xaxis=dict(backgroundcolor='rgba(200,200,200,0.2)'),
                    yaxis=dict(backgroundcolor='rgba(200,200,200,0.2)'),
                    zaxis=dict(backgroundcolor='rgba(200,200,200,0.2)')
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white', size=12),
                height=600
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # ============================================================
            # SATISFACTION FEEDBACK
            # ============================================================
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div class='input-section'>
                <h3 style='text-align: center; color: white;'>😊 How Satisfied Are You?</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("😍 VERY SATISFIED - EXCELLENT PREDICTION!", use_container_width=True):
                    st.markdown("""
                    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 15px; margin: 20px 0;'>
                        <h1>😍😍😍 AMAZING! 😍😍😍</h1>
                        <p style='color: white; font-size: 18px;'>Thank you for using our predictor!</p>
                        <p style='color: white; font-size: 14px; margin-top: 10px;'>Your feedback helps us improve! ⭐⭐⭐⭐⭐</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                if st.button("😞 NOT SATISFIED - NEEDS IMPROVEMENT", use_container_width=True):
                    st.markdown("""
                    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 15px; margin: 20px 0;'>
                        <h1>😞 WE'LL DO BETTER! 😞</h1>
                        <p style='color: white; font-size: 18px;'>Thanks for your feedback!</p>
                        <p style='color: white; font-size: 14px; margin-top: 10px;'>Help us improve by sharing more details 💪</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    # ========================================================================
    # TAB 2: ANALYTICS
    # ========================================================================
    with tab2:
        st.markdown("""
        <div class='input-section'>
            <h2>📈 Model Analytics Dashboard</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h3>RMSE</h3>
                <p style='font-size: 24px; font-weight: bold;'>$77.17</p>
                <p style='font-size: 12px; opacity: 0.8;'>Prediction Error</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h3>MAE</h3>
                <p style='font-size: 24px; font-weight: bold;'>$47.15</p>
                <p style='font-size: 12px; opacity: 0.8;'>Average Error</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='metric-card'>
                <h3>R² Score</h3>
                <p style='font-size: 24px; font-weight: bold;'>0.4496</p>
                <p style='font-size: 12px; opacity: 0.8;'>45% Variance</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class='metric-card'>
                <h3>K Value</h3>
                <p style='font-size: 24px; font-weight: bold;'>21</p>
                <p style='font-size: 12px; opacity: 0.8;'>Neighbors Used</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 3D Distribution plot
        fig2 = go.Figure()
        
        # Sample data for visualization
        sample_prices = np.random.normal(138, 103, 1000)
        sample_prices = np.clip(sample_prices, 30, 799)
        
        fig2.add_trace(go.Histogram(
            x=sample_prices,
            nbinsx=30,
            name='Price Distribution',
            marker=dict(
                color=sample_prices,
                colorscale='Viridis',
                showscale=True
            )
        ))
        
        fig2.update_layout(
            title='NYC Airbnb Price Distribution',
            xaxis_title='Price ($)',
            yaxis_title='Frequency',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0.1)',
            font=dict(color='white'),
            hovermode='x unified',
            height=500
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # ========================================================================
    # TAB 3: ABOUT
    # ========================================================================
    with tab3:
        st.markdown("""
        <div class='input-section'>
            <h2>ℹ️ About This Application</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h3>📊 Dataset</h3>
                <p>Airbnb NYC 2019</p>
                <p style='font-size: 12px;'>48,017 listings</p>
                <p style='font-size: 12px;'>9 features</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class='metric-card'>
                <h3>🤖 Algorithm</h3>
                <p>K-Nearest Neighbors</p>
                <p style='font-size: 12px;'>K = 21</p>
                <p style='font-size: 12px;'>Distance: Euclidean</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h3>🎯 Features Used</h3>
                <p>Latitude, Longitude</p>
                <p style='font-size: 12px;'>Reviews, Availability</p>
                <p style='font-size: 12px;'>Room Type, Borough</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class='metric-card'>
                <h3>⚡ Performance</h3>
                <p>RMSE: $77.17</p>
                <p style='font-size: 12px;'>MAE: $47.15</p>
                <p style='font-size: 12px;'>R²: 0.4496</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='input-section'>
            <h3 style='text-align: center; color: white;'>🚀 Built with</h3>
            <p style='text-align: center; color: white; font-size: 16px;'>
                Python 🐍 | Streamlit ⚡ | Scikit-learn 🤖 | Plotly 📊
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; padding: 20px; color: white; margin-top: 30px;'>
            <p>Made with ❤️ for Data Science & AI</p>
            <p style='font-size: 12px; opacity: 0.7;'>© 2024 | All Rights Reserved</p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.error("⚠️ Please ensure the model file is available!")
