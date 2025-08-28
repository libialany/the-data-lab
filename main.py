import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
eeg_data = pd.read_csv('EEG_machinelearing_data_BRMH.csv')
print("== Dataset Head ==\n")
print(eeg_data.head())

data_columns = eeg_data.columns
print("Data columns",data_columns)

data_info = eeg_data.info
print("The data info",data_info)

data_shape = eeg_data.shape
print("The data shape",data_shape)

data_dtypes = eeg_data.dtypes
print("The data dtypes",data_dtypes)

## Delete duplicates rows

duplicate = eeg_data.duplicated().sum()
print("Number of Duplicates: ", duplicate)
if duplicate > 0:
    print(eeg_data[eeg_data.duplicated()])

# ## Unique in each column

print(eeg_data["specific.disorder"].unique())
print(eeg_data["main.disorder"].unique())

## Checking for missing Values

missing_values = eeg_data.isnull().sum()
print('The missing values in the dataset are',missing_values)

## Handling missing values

mapping = {
    'Alcohol use disorder': 1,
    'Acute stress disorder': 2,
    'Depressive disorder': 3,
    'Healthy control': 4,
    'Behavioral addiction disorder': 5,
    'Obsessive compulsitve disorder': 6,
    'Schizophrenia': 7,
    'Panic disorder': 8,
    'Social anxiety disorder': 9,
    'Posttraumatic stress disorder': 10,
    'Adjustment disorder': 11,
    'Bipolar disorder': 12
}

eeg_data["specific_disorder_code"] = eeg_data["specific.disorder"].map(mapping)

print(eeg_data["specific_disorder_code"])

# Calculate the mean IMDb rating excluding null values
mean_rating = eeg_data['specific_disorder_code'].mean(skipna=True)
print(mean_rating)

# # Replace null values with the mean IMDb rating
eeg_data['specific_disorder_code'].fillna(mean_rating, inplace=True)
print(eeg_data)

null_values_after = eeg_data.isnull().sum()
print("Null values after replacing with mean:\n", null_values_after)

# ## Data Transformation

# # Convert the 'Age_num' column to integers
eeg_data['Age_num'] = eeg_data['age'].astype(int)
print(eeg_data['Age_num'])

# ## Outlier Detection

plt.hist(eeg_data['Age_num'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

## Data Normalization
#create scalers
scaler_minmax = MinMaxScaler()
scaler_normalize = Normalizer()

#scale data
data_minmax = scaler_minmax.fit_transform(eeg_data[['IQ']])  #rescale to [0,1] range

# explain to me what the normalize does and how it works?
data_normalize = scaler_normalize.fit_transform(eeg_data[['IQ']]) 

#add scaled features back to the data frame
eeg_data['IQ_MinMax'] = data_minmax
eeg_data['IQ_Normalize'] = data_normalize

print("Data with min-max scaling")
print(eeg_data.head())

print("\n\nData with feature normalization")
print(eeg_data.tail())

eeg_data.to_csv('eeg_data_scaled.csv', index=False)