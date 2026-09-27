from pydantic import BaseModel, ConfigDict


class EmployeeInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Numerical features
    Age: int
    DistanceFromHome: int
    EmpHourlyRate: int
    EmpJobLevel: int
    NumCompaniesWorked: int
    EmpLastSalaryHikePercent: int
    TotalWorkExperienceInYears: int
    TrainingTimesLastYear: int
    ExperienceYearsAtThisCompany: int
    ExperienceYearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int

    # Ordinal features
    EmpEducationLevel: int
    EmpEnvironmentSatisfaction: int
    EmpJobInvolvement: int
    EmpJobSatisfaction: int
    EmpRelationshipSatisfaction: int
    EmpWorkLifeBalance: int

    # Categorical features
    Gender: str
    EducationBackground: str
    MaritalStatus: str
    EmpDepartment: str
    EmpJobRole: str
    BusinessTravelFrequency: str
    OverTime: str
    Attrition: str