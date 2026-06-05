# 🏢 Airbnb NYC Price Predictor - Web Application

A beautiful, interactive machine learning web application that predicts Airbnb listing prices in New York City using KNN regression with stunning 3D visualizations.

## 🌟 Features

✨ **Beautiful UI Design**
- Colorful gradient backgrounds with animations
- Glassmorphism effects and modern design
- Responsive layout for all devices

🎯 **Prediction Engine**
- KNN-based price prediction model
- Real-time price calculation
- Support for all NYC boroughs

📊 **3D Visualizations**
- Interactive 3D surface plots
- Price distribution analysis
- Animated charts and graphs

😊 **User Feedback System**
- Satisfaction emoji feedback (😍 / 😞)
- Positive and negative response animations
- User experience tracking

📈 **Analytics Dashboard**
- Model performance metrics
- RMSE, MAE, R² Score display
- Dataset information

## 📋 Requirements

- Python 3.8+
- All dependencies in `requirements.txt`

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd airbnb-price-predictor
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Ensure Model File Exists
Make sure `airbnb_knn_model.pkl` is in the same directory as `app.py`

### 5. Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📁 Project Structure

```
airbnb-price-predictor/
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── airbnb_knn_model.pkl         # Trained KNN model & encoders
├── KNN_regression_corrected.ipynb # Training notebook
└── README.md                     # This file
```

## 🎮 How to Use

### Step 1: Enter Property Details
- Select location (latitude, longitude, borough, neighbourhood)
- Choose room type (Entire home, Private room, Shared room)
- Set minimum nights and availability

### Step 2: Enter Review Information
- Number of reviews
- Reviews per month
- Host listings count

### Step 3: Get Prediction
- Click "🚀 PREDICT PRICE" button
- View predicted price in beautiful card
- Explore 3D surface plot analysis

### Step 4: Provide Feedback
- Choose satisfaction level (😍 / 😞)
- See animated response
- Help improve the model

## 📊 Model Information

**Algorithm**: K-Nearest Neighbors (KNN)
- K Value: 21
- Distance Metric: Euclidean

**Dataset**: Airbnb NYC 2019
- Total Samples: 48,017
- Training Samples: 38,413 (80%)
- Test Samples: 9,604 (20%)

**Features**: 9 total
- Numerical: latitude, longitude, minimum_nights, number_of_reviews, reviews_per_month, calculated_host_listings_count, availability_365
- Categorical: neighbourhood_group, room_type

**Performance Metrics**:
- RMSE: $77.17
- MAE: $47.15
- R² Score: 0.4496 (45% variance explained)

## 🎨 Design Features

- **Gradient Backgrounds**: Animated color gradients (purple → pink → blue → cyan)
- **Glassmorphism**: Modern frosted glass effect on cards
- **3D Visualizations**: Plotly 3D surface plots and distribution charts
- **Emoji Integration**: Status indicators and feedback system
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Custom CSS**: Styled tabs, metric cards, and input sections

## 💻 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML Library**: Scikit-learn
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Joblib

## 🔧 Customization

### Change Model
Replace `airbnb_knn_model.pkl` with your trained model

### Modify Styling
Edit CSS in the `st.markdown()` sections for custom colors/fonts

### Update Thresholds
Modify min/max sliders in the prediction section

### Add More Metrics
Insert new cards in the Analytics tab

## 📈 Deployment Options

### Streamlit Cloud (Free)
```bash
streamlit run app.py
# Then deploy via Streamlit Cloud dashboard
```

### Heroku
```bash
heroku create your-app-name
git push heroku main
```

### AWS, GCP, Azure
Compatible with any cloud platform supporting Python

### Local Docker
```bash
docker build -t airbnb-predictor .
docker run -p 8501:8501 airbnb-predictor
```

## 🐛 Troubleshooting

**Model not loading?**
- Ensure `airbnb_knn_model.pkl` is in the same directory as `app.py`
- Check file permissions

**Slow predictions?**
- Model is optimized for speed
- Clear cache if running multiple times

**Visualization not showing?**
- Ensure Plotly is installed: `pip install plotly`
- Check internet connection for Plotly CDN

## 📚 Training the Model

To retrain the model, use the Jupyter notebook:
```bash
jupyter notebook KNN_regression_corrected.ipynb
```

After training, save the model using:
```python
import joblib
joblib.dump({
    'model': model,
    'num_encod': STD,
    'num_encod_y': STD_y,
    'cat_encod': OHE,
    'cato_encod': OE
}, 'airbnb_knn_model.pkl')
```

## 📊 Expected Outputs

- **Predicted Price**: $30 - $799 range
- **Accuracy**: ±$47.15 on average
- **Price Factors**: Location, room type, reviews, availability

## 🎓 Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Scikit-learn KNN](https://scikit-learn.org/stable/modules/neighbors.html)
- [Plotly 3D Plots](https://plotly.com/python/3d-plots)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 👨‍💻 Author

Built with ❤️ for Data Science & AI

## 📞 Support

For issues or questions:
- Create an issue on GitHub
- Check existing discussions
- Review the documentation

## 🚀 Future Enhancements

- [ ] Add more ML models (Random Forest, XGBoost)
- [ ] Implement A/B testing
- [ ] Add price history tracking
- [ ] Include image upload for listing photos
- [ ] Deploy to Streamlit Cloud
- [ ] Add database for prediction history
- [ ] Implement user authentication

---

⭐ If you find this useful, please star the repository!

Made with 💻 and 🤖 by AI
