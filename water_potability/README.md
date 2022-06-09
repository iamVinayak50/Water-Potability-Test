# Water_Potability

Potable water is defined as water that is suitable for human consumption (i.e., water that can be used for drinking or cooking). The term implies that the water is drinkable as well as safe. Here we our predicting the water potability i.e Water is Good for human resources or not potable.

## Demo app

Launch the app [![Open In Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/mridul-sharma01/water_potablity/main/app.py)

## App info

This repository creates a Data Web App  about safe water for human consumption by using Streamlit Python Package. More specifically, it allows its users to change the values of the nine predictor variables:
1. pH
2. Hardness
3. Solids
4. Chloramines
5. Sulfate
6. Conductivity
7. Organic_carbon
8. Trihalomethanes
9. Turbidity

Trains a Random Forest Classifier model and, finally, observe the prediction of the trained model.

## Dataset

The imported csv file contains water quality metrics for 3276 different water bodies.

## Reproducing the App

1. First, we create a virtual Python environment called my_venv
```
  python3 -m venv my_venv
```
2. Then, we activate the virtual environment
```
source path_to_your_virtual_environment/bin/activate
```
3. After getting to the virtual environment's file, install prerequisite packages
```
wget https://raw.githubusercontent.com/Mridul-Sharma01/Water_Potability/main/requirements.txt
```
   and
```
pip install -r requirements.txt
```
4. Dowload and unzip contents from Github repo

Dowload and unzip contents from https://github.com/Mridul-Sharma01/Water_Potablity/archive/refs/heads/main.zip

5. Launch the app
```
streamlit run app.py
```


## Requirements

| Package | Version |
--- | ---
| streamlit | 1.10.0 |
| pandas |  1.4.2 |
| sci-kit learn | 1.1.1 |
| numpy |  1.9.2 |

## Useful Resources

1.  [Youtube tutorial from Chanin Nantasenamat (Data Professor) ](https://www.youtube.com/watch?v=8M20LyCZDOY )
