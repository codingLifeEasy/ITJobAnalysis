import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset

df = pd.read_csv("data/ds_salaries.csv")

# 1.drop useless colum
df = df.drop(columns=["Unnamed: 0"])

# 2. Clean experience level column
exp_map = {
    "EN" : "Entry",
    "MI" : "Mid",
    "SE" : "Senior",
    "EX" : "Executive",
}

df["experience_level"] = df["experience_level"].map(exp_map)

#cleaning employment type

emp_map = {
   "FT": "Full-Time",
    "PT": "Part-Time",
    "CT": "Contract",
    "FL": "Freelance" 
}

df["employment_type"] = df["employment_type"].map(emp_map)

#preview cleaned data

print(df.head())

#Check unique values

print("\nExperience Levels:", df["experience_level"].unique())
print("Employment Types:", df["employment_type"].unique())



print("\nAverage Salary by Job Title:::::::::::::::::::::")
# Average salary by job title
salary_by_role = df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)

print("\nTop Paying Roles:")
print(salary_by_role.head(10))

salary_by_location = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)

print("\nTop Paying Locations:")
print(salary_by_location.head(10))





# Top 10 roles
top_roles = salary_by_role.head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_roles.values, y=top_roles.index)

plt.title("Top 10 Highest Paying Roles")
plt.xlabel("Average Salary (USD)")
plt.ylabel("Job Role")

plt.tight_layout()
plt.show()


salary_by_exp = df.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending=False)
plt.figure(figsize=(6,4))
sns.barplot(x=salary_by_exp.index, y=salary_by_exp.values)

plt.title("Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary (USD)")

plt.tight_layout()
plt.show()


salary_by_country = df.groupby("company_location")["salary_in_usd"].mean().sort_values(ascending=False)
top_countries = salary_by_country.head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)

plt.title("Top Paying Countries")
plt.xlabel("Average Salary (USD)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()























