# INDIa-CaNCER-PaTIENTS-aNaLYSIS
print("\nINDIa-CaNCER-PaTIENTS-aNaLYSIS")
print('\n author: amulya Srivastava')
print(" ---------------------------------------")
# =====================
# Imports
# =====================
import pandas as pd
import matplotlib.pyplot as plt
# =====================
# Load Data
# =====================

df1 = pd.read_csv("cancer-risk-factors.csv")

# dataset overview
print("Check if there is any missing values:")
print(df1.isnull().sum())
print("\n NUMBER OF ROWS aND COLUMN")
print(df1.shape)
print('\n COLUMNS PRESENT IN THE DaTaSET')
print(df1.columns)
print("----------------")
# types of cancer in the dataset
print('\n Types of Cancer:')
print(df1["Cancer_Type"].unique())
print("-----------------")
# ==============================
# Checking types of genders presents in the dataset
print(df1["Gender"].unique())

# =====================
# Data Cleaning
# =====================


# Replace 0 and 1
df1["Gender"] = df1["Gender"].replace({
    0: "Female",
    1: "Male"
})

# Check result
print("\nafter mapping:")
print(df1["Gender"].unique())

print("\nSample rows:")
print(df1[["Patient_ID", "Gender"]].head())

print("\nCounts:")
print(df1["Gender"].value_counts())

#  ====================
# analysis
# =====================
# how many gender based patients of breast cancer

breast_df = df1[df1["Cancer_Type"] == "Breast"]

counts = breast_df["Gender"].value_counts()

print(counts)

# plotting graph for breast cancer patient vs gender

breast_df = df1[df1["Cancer_Type"] == "Breast"]

counts = breast_df["Gender"].value_counts()

plt.bar(counts.index, counts.values,color="pink")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Breast Cancer Patients by Gender")
plt.show()

# from the graph we saw few male patients also have breast cancer thats a warning signal lets see how many male patients are found 
male_breast = df1[
    (df1["Gender"] == "Male") &
    (df1["Cancer_Type"] == "Breast")
]

print("Male breast cancer patients:", len(male_breast))

female_breast = df1[
    (df1["Gender"] == "Female") &
    (df1["Cancer_Type"] == "Breast")
]

print("Female breast cancer patients:", len(female_breast))

breast_df = df1[df1["Cancer_Type"] == "Breast"]

male_breast = len(
    breast_df[breast_df["Gender"] == "Male"]
)

total_breast = len(breast_df)

print("Male breast cancer percentage:",
      round((male_breast / total_breast) * 100, 2), "%")

breast_df = df1[df1["Cancer_Type"] == "Breast"]

plt.scatter(
    breast_df.index,
    breast_df["Overall_Risk_Score"],
    color="yellow"
)

plt.title("Breast Cancer Risk Factor")
plt.xlabel("Patient Index")
plt.ylabel("Overall Risk Score")
plt.show()

#  ====================
# PROSTATE CANCER analysis
# =====================
# how many gender based patients of prostate cancer

prostate_df = df1[df1["Cancer_Type"] == "Prostate"]

counts = prostate_df["Gender"].value_counts()

print(counts)

# plotting graph for prostate cancer patient vs gender

plt.bar(counts.index, counts.values, color="lightblue")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Prostate Cancer Patients by Gender")
plt.show()

# from the graph we saw NO female patients have prostate cancer, that makes sense biologically since only men have a prostate, lets confirm with the numbers

female_prostate = df1[
    (df1["Gender"] == "Female") &
    (df1["Cancer_Type"] == "Prostate")
]

print("Female prostate cancer patients:", len(female_prostate))

male_prostate = len(
    prostate_df[prostate_df["Gender"] == "Male"]
)

total_prostate = len(prostate_df)

print("Male prostate cancer percentage:",
      round((male_prostate / total_prostate) * 100, 2), "%")

plt.scatter(
    prostate_df.index,
    prostate_df["Overall_Risk_Score"],
    color="skyblue"
)

plt.title("Prostate Cancer Risk Factor")
plt.xlabel("Patient Index")
plt.ylabel("Overall Risk Score")
plt.show()

# prostate cancer patients are much older on average than other cancer types, lets check
print("\nAverage age of prostate cancer patients:",
      round(prostate_df["Age"].mean(), 2))

#  ====================
# SKIN CANCER analysis
# =====================
# how many gender based patients of skin cancer

skin_df = df1[df1["Cancer_Type"] == "Skin"]

counts = skin_df["Gender"].value_counts()

print(counts)

# plotting graph for skin cancer patient vs gender

plt.bar(counts.index, counts.values, color="peachpuff")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Skin Cancer Patients by Gender")
plt.show()

# from the graph the gender split looks fairly balanced for skin cancer, lets confirm the percentage

male_skin = len(
    skin_df[skin_df["Gender"] == "Male"]
)

total_skin = len(skin_df)

print("Male skin cancer percentage:",
      round((male_skin / total_skin) * 100, 2), "%")

plt.scatter(
    skin_df.index,
    skin_df["Overall_Risk_Score"],
    color="orange"
)

plt.title("Skin Cancer Risk Factor")
plt.xlabel("Patient Index")
plt.ylabel("Overall Risk Score")
plt.show()

# skin cancer is often linked to outdoor/occupational sun exposure, lets check occupational hazards by gender
print("\nAverage occupational hazard score by gender (Skin cancer):")
print(skin_df.groupby("Gender")["Occupational_Hazards"].mean().round(2))

#  ====================
# COLON CANCER analysis
# =====================
# how many gender based patients of colon cancer

colon_df = df1[df1["Cancer_Type"] == "Colon"]

counts = colon_df["Gender"].value_counts()

print(counts)

# plotting graph for colon cancer patient vs gender

plt.bar(counts.index, counts.values, color="peru")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Colon Cancer Patients by Gender")
plt.show()

# gender split looks close to even for colon cancer, lets confirm the percentage

male_colon = len(
    colon_df[colon_df["Gender"] == "Male"]
)

total_colon = len(colon_df)

print("Male colon cancer percentage:",
      round((male_colon / total_colon) * 100, 2), "%")

plt.scatter(
    colon_df.index,
    colon_df["Overall_Risk_Score"],
    color="brown"
)

plt.title("Colon Cancer Risk Factor")
plt.xlabel("Patient Index")
plt.ylabel("Overall Risk Score")
plt.show()

# colon cancer is strongly diet linked, lets check average red meat diet score by gender
print("\nAverage red meat diet score by gender (Colon cancer):")
print(colon_df.groupby("Gender")["Diet_Red_Meat"].mean().round(2))

#  ====================
# LUNG CANCER analysis
# =====================
# how many gender based patients of lung cancer

lung_df = df1[df1["Cancer_Type"] == "Lung"]

counts = lung_df["Gender"].value_counts()

print(counts)

# plotting graph for lung cancer patient vs gender

plt.bar(counts.index, counts.values, color="gray")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.title("Lung Cancer Patients by Gender")
plt.show()

# from the graph we saw more male patients than female for lung cancer, lets confirm the percentage

male_lung = len(
    lung_df[lung_df["Gender"] == "Male"]
)

total_lung = len(lung_df)

print("Male lung cancer percentage:",
      round((male_lung / total_lung) * 100, 2), "%")

plt.scatter(
    lung_df.index,
    lung_df["Overall_Risk_Score"],
    color="dimgray"
)

plt.title("Lung Cancer Risk Factor")
plt.xlabel("Patient Index")
plt.ylabel("Overall Risk Score")
plt.show()

# lung cancer is strongly smoking linked, lets check average smoking score by gender
print("\nAverage smoking score by gender (Lung cancer):")
print(lung_df.groupby("Gender")["Smoking"].mean().round(2))

print(df1["Age"].unique())

#  ====================
# CaNCER TYPE DISTRIBUTION (all cancers)
# =====================
# how many patients of each cancer type overall

cancer_counts = df1["Cancer_Type"].value_counts()

print("\nPatients per cancer type:")
print(cancer_counts)

# plotting pie chart for all cancer types
# (using the same color for each cancer type as its bar chart above)

cancer_colors = {
    "Breast": "pink",
    "Prostate": "lightblue",
    "Skin": "peachpuff",
    "Colon": "peru",
    "Lung": "gray"
}

plt.pie(
    cancer_counts.values,
    labels=cancer_counts.index,
    autopct="%1.1f%%",
    colors=[cancer_colors[c] for c in cancer_counts.index]
)

plt.title("Cancer Type Distribution")
plt.show()

# 