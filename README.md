\# Airbnb NYC Price Predictor



A machine learning web application that predicts Airbnb listing prices in New York City using K-Nearest Neighbors regression with interactive 3D visualizations.



\*\*Live Application:\*\* https://airbnb-price-predictor-viswanath.streamlit.app/



\*\*Repository:\*\* https://github.com/viswanath-0/airbnb-price-predictor



\---



\## Overview



This project implements a complete machine learning pipeline from data preprocessing to production deployment. The application predicts nightly rental prices for Airbnb listings across New York City's five boroughs using 9 property features and advanced visualization techniques.



\---



\## Features



\### Core Functionality

\- Real-time price prediction based on property characteristics

\- Interactive web interface with responsive design

\- 3D surface plots showing price variations

\- Model performance analytics and metrics dashboard

\- User feedback system for prediction satisfaction



\### Technical Highlights

\- K-Nearest Neighbors regression with optimized hyperparameters (K=21)

\- Feature scaling and categorical encoding pipeline

\- Streamlit-based web application with custom CSS styling

\- Plotly 3D visualizations for data exploration

\- Production-ready model serialization with Joblib



\---



\## Dataset



The model is trained on the Airbnb NYC 2019 dataset:

\- Total Records: 48,017 listings

\- Training Samples: 38,413 (80%)

\- Test Samples: 9,604 (20%)

\- Features: 9 (7 numerical + 2 categorical)

\- Target Variable: Nightly Price ($30-$799)



\---



\## Model Details



\### Algorithm

K-Nearest Neighbors Regression

\- K Value: 21 neighbors

\- Distance Metric: Euclidean

\- Weights: Uniform



\### Features Used



\*\*Numerical Features (7)\*\*

\- Latitude and Longitude (geographic coordinates)

\- Minimum Nights (minimum stay requirement)

\- Number of Reviews (total reviews received)

\- Reviews per Month (review frequency)

\- Calculated Host Listings Count (host experience)

\- Availability 365 (days available per year)



\*\*Categorical Features (2)\*\*

\- Neighbourhood Group (Manhattan, Brooklyn, Queens, Bronx, Staten Island)

\- Room Type (Entire home/apt, Private room, Shared room)



\### Performance Metrics

\- Root Mean Square Error (RMSE): $77.17

\- Mean Absolute Error (MAE): $47.15

\- R-squared Score: 0.4496 (explains 44.96% of price variance)



\---



\## Installation



\### Requirements

\- Python 3.8 or higher

\- Git

\- Virtual environment (recommended)



\### Setup Instructions



1\. Clone the repository:

```bash

git clone https://github.com/viswanath-0/airbnb-price-predictor.git

cd airbnb-price-predictor

```



2\. Create and activate virtual environment:

```bash

python -m venv venv

source venv/bin/activate  # On Windows: venv\\Scripts\\activate

```



3\. Install dependencies:

```bash

pip install -r requirements.txt

```



4\. Run the application:

```bash

streamlit run app.py

```



The application will open at `http://localhost:8501`



\---



\## Usage



\### Making Predictions



1\. \*\*Enter Property Details\*\*: Input location coordinates, borough, and neighbourhood information

2\. \*\*Specify Room Type\*\*: Select from Entire home, Private room, or Shared room

3\. \*\*Add Property Metrics\*\*: Set minimum nights, reviews count, and availability

4\. \*\*Get Prediction\*\*: Click the predict button to receive the estimated nightly price

5\. \*\*View Analysis\*\*: Explore 3D surface plots and price distribution charts

6\. \*\*Provide Feedback\*\*: Rate prediction satisfaction to help improve the model



\### Application Sections



\*\*Prediction Tab\*\*

\- Interactive input form for property details

\- Real-time price calculation

\- 3D visualization of price variations by location and availability

\- User satisfaction feedback system



\*\*Analytics Tab\*\*

\- Model performance metrics (RMSE, MAE, R-squared)

\- Historical performance data

\- Price distribution analysis

\- Dataset statistics



\*\*About Tab\*\*

\- Project information

\- Model specifications

\- Feature descriptions

\- Performance details



\---



\## Project Structure



```

airbnb-price-predictor/

├── app.py                      Main Streamlit application

├── requirements.txt            Python package dependencies

├── airbnb\_knn\_model.pkl       Trained KNN model and encoders

├── README.md                   Project documentation

├── .gitignore                  Git configuration

└── KNN\_regression\_corrected.ipynb   Training notebook (optional)

```



\---



\## Technology Stack



\*\*Frontend\*\*

\- Streamlit 1.28.1 (web framework)

\- Plotly 5.17.0 (3D visualizations)

\- Custom CSS (styling)



\*\*Backend \& ML\*\*

\- Python 3.8+

\- Scikit-learn 1.3.2 (machine learning)

\- Pandas 2.0.3 (data manipulation)

\- NumPy 1.24.3 (numerical computing)



\*\*Model Serialization\*\*

\- Joblib 1.3.2 (model persistence)



\---



\## Model Training



The model was trained using the complete machine learning pipeline:



1\. Data Cleaning: Handled missing values in reviews\_per\_month

2\. Feature Preprocessing: StandardScaler for numerical features, Label/Ordinal encoding for categorical

3\. Train-Test Split: 80-20 split with random seed for reproducibility

4\. Hyperparameter Tuning: Tested K values (3, 5, 7, 9, 11, 15, 21)

5\. Model Evaluation: Compared RMSE, MAE, and R-squared scores



For detailed implementation, see `KNN\_regression\_corrected.ipynb`



\---



\## Deployment



The application is deployed on Streamlit Cloud, providing:

\- Free hosting with automatic scaling

\- Continuous deployment from GitHub

\- 24/7 availability

\- Easy sharing and collaboration



\### Deploying Your Own Version



1\. Fork the repository

2\. Create account at https://streamlit.io/cloud

3\. Connect your GitHub repository

4\. Select main branch and app.py

5\. Deploy automatically



\---



\## Results and Interpretation



The model achieves:

\- Average prediction error of approximately $47 per night

\- Ability to explain 45% of price variance based on available features

\- Reasonable accuracy for a baseline predictive model



\### Price Factors



Based on the model, nightly prices are primarily influenced by:

\- Geographic location (latitude and longitude)

\- Room type (entire home commands premium pricing)

\- Number of reviews (indicator of popularity)

\- Host experience (number of listings)

\- Seasonal availability



\---



\## Limitations and Future Improvements



\### Current Limitations

\- Model does not account for temporal trends (seasonality)

\- Text-based listing descriptions are not analyzed

\- Image data from listings is not utilized

\- Recent price changes and market dynamics not captured



\### Potential Enhancements

\- Implement advanced models (Random Forest, XGBoost, Neural Networks)

\- Add temporal features (day of week, season)

\- Incorporate Natural Language Processing for descriptions

\- Implement ensemble methods for improved accuracy

\- Add prediction confidence intervals

\- Deploy with cloud database for prediction history tracking



\---



\## Code Quality



The codebase follows professional standards:

\- Clear variable naming and comments

\- Modular structure for maintainability

\- Error handling for user inputs

\- Efficient data processing pipelines

\- Reproducible results with fixed random seeds



\---



\## Performance Considerations



\- First application load: 2-3 seconds (model cached)

\- Subsequent predictions: < 1 second

\- 3D visualization rendering: 1-2 seconds

\- Model file size: 70 MB (stored efficiently with Joblib)



\---



\## Troubleshooting



\*\*Application Won't Load\*\*

\- Ensure all dependencies are installed: `pip install -r requirements.txt`

\- Check Python version (3.8+)

\- Verify model file exists in project directory



\*\*Predictions Seem Inaccurate\*\*

\- Model explains 45% of variance; other factors influence actual prices

\- Consider location-specific market conditions

\- Review input parameters for accuracy



\*\*Slow Performance\*\*

\- Clear browser cache

\- Refresh the page

\- Streamlit Cloud may be under load; try again later



\---



\## License



This project is provided as-is for educational and portfolio purposes.



\---



\## Contact and Support



For questions or issues:

\- Open an issue on GitHub

\- Check existing documentation

\- Review the training notebook for implementation details



\---



\## Acknowledgments



Dataset Source: Airbnb NYC 2019

Built with Streamlit, Scikit-learn, and Plotly



\---



Last Updated: 2024

