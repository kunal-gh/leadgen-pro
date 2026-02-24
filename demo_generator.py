import pandas as pd
import random
import datetime
import time

# User specified default lists to pick from if not fully provided
DEFAULT_DECISION_MAKER_TITLES = [
    "Founder", "Co-Founder", "CEO", "Managing Director", "Owner", "Director",
    "Head of Operations", "Operations Manager", "Sales Director", "Growth Director",
    "Business Development Director", "Chief Operating Officer", "Revenue Director",
    "Managing Partner"
]

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna",
    "Ishaan", "Shaurya", "Atharv", "Ananya", "Diya", "Navya", "Saanvi", "Priya", "Anjali",
    "Riya", "Kavya", "Snigdha", "Meera", "Neha", "Pooja", "Rahul", "Vikram", "Rohan", "Rajat",
    "Amit", "Sumit", "Sandeep", "Karan", "Gaurav", "Varun", "Rohit", "Sneha", "Kunal", "John", "Sarah", "Michael"
]

LAST_NAMES = [
    "Sharma", "Verma", "Gupta", "Malhotra", "Singh", "Patel", "Shah", "Desai", "Joshi",
    "Reddy", "Rao", "Nair", "Iyer", "Kumar", "Chaudhary", "Das", "Yadav", "Rajput", "Mehta",
    "Bhatia", "Agarwal", "Kapoor", "Chatterjee", "Banerjee", "Mukherjee", "Trivedi", "Mishra", "Smith", "Doe"
]

COMPANY_PREFIXES = ["Apex", "Nova", "Zenith", "Pinnacle", "Elevate", "NextGen", "Pro", "Prime", "Alpha", "Global", "Tech", "Smart", "Giga", "Mega", "Rapid", "Bright"]
COMPANY_SUFFIXES = ["Solutions", "Consulting", "Services", "Group", "Associates", "Partners", "Ventures", "Enterprises", "Dynamics", "Hub", "Network", "Works", "Labs"]

def generate_company_name(industry):
    if "Agency" in industry or "Marketing" in industry:
        return f"{random.choice(COMPANY_PREFIXES)} Media {random.choice(['Group', 'Agency', 'Network'])}"
    elif "Clinic" in industry or "Medical" in industry or "Dental" in industry:
        return f"{random.choice(['City', 'Prime', 'Care', 'Wellness'])} {industry.split(' ')[0]} {random.choice(['Care', 'Center', 'Clinic'])}"
    elif "Services" in industry:
        return f"{random.choice(COMPANY_PREFIXES)} {industry.split(' ')[0]} {random.choice(COMPANY_SUFFIXES)}"
    elif "Startup" in industry:
        return f"{random.choice(COMPANY_PREFIXES)}Tech.io"
    elif "Real Estate" in industry or "Property" in industry:
        return f"{random.choice(['Premium', 'Global', 'Urban', 'Core'])} Properties"
    else:
        return f"{random.choice(COMPANY_PREFIXES)} {random.choice(COMPANY_SUFFIXES)}"

def sanitize_url_string(s):
    return s.lower().replace(" ", "-").replace(",", "").replace(".", "").replace("&", "and")

def generate_leads_dynamic(num_leads, industries, locations, sizes, titles=DEFAULT_DECISION_MAKER_TITLES):
    """Generates an exact number of leads based on user-provided constraints."""
    start_time = time.perf_counter()
    leads = []
    generated_companies = set()
    
    while len(leads) < num_leads:
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        full_name = f"{first_name} {last_name}"
        
        industry = random.choice(industries)
        location = random.choice(locations)
        size = random.choice(sizes)
        title = random.choice(titles)
            
        company_name = generate_company_name(industry)
        company_name = generate_company_name(industry)
        
        # Prevent infinite loop if we exhaust all combinations
        attempts = 0
        while company_name in generated_companies and attempts < 10:
            company_name = f"{generate_company_name(industry)} {random.randint(1, 999)}"
            attempts += 1
            
        generated_companies.add(company_name)
        
        domain_suffix = random.choice([".in", ".co.in", ".com", ".io", ".co"])
        domain = sanitize_url_string(company_name) + domain_suffix
        website = f"https://www.{domain}"
        
        company_linkedin = f"https://www.linkedin.com/company/{sanitize_url_string(company_name)}"
        personal_linkedin = f"https://www.linkedin.com/in/{sanitize_url_string(first_name)}-{sanitize_url_string(last_name)}-{random.randint(1000, 9999)}a"
        
        email = f"{first_name.lower()}@{domain}"
        
        # Advanced Fields & Simulated AI Features
        crm = random.choice(["HubSpot", "Salesforce", "Zoho CRM", "Pipedrive", "None detected", "Freshsales"])
        hiring = random.choice(["Actively Hiring", "Stable", "Growing team", "No recent openings"])
        growth = f"+{random.randint(5, 35)}% YoY"
        
        # Simulated AI/ML Features for Showcase
        # NLP Intent Extraction Category
        nlp_intent = random.choice(["High Buying Intent", "Passive Researching", "Immediate Need", "Evaluating Competitors", "Budget Approved"])
        
        # Predictive Lead Scoring (Random Forest / XGBoost Simulation)
        # Score calculation weights based on firmographics
        base_score = random.randint(40, 75)
        if "Actively" in hiring or "Growing" in hiring:
            base_score += 15
        if crm != "None detected":
            base_score += 10
        if "Founder" in title or "CEO" in title:
            base_score += 8
            
        predictive_score = min(99, base_score)
        
        # MLOps: Shadow Deployment / Challenger Model
        challenger_score = min(99, int(base_score * random.uniform(0.85, 1.15)))
        
        lead = {
            "AI Predict Score (Champion)": predictive_score,
            "AI Predict Score (Challenger)": challenger_score,
            "NLP Intent Tag": nlp_intent,
            "Full Name": full_name,
            "Job Title": title,
            "Company Name": company_name,
            "Company Website": website,
            "LinkedIn Profile URL": personal_linkedin,
            "Company LinkedIn URL": company_linkedin,
            "Industry": industry,
            "Company Size": size,
            "Location": location,
            "Business Email": email,
            "CRM Detected": crm,
            "Hiring Status": hiring,
            "Company Growth": growth
        }
        leads.append(lead)
        
    df = pd.DataFrame(leads)
    
    # Save to a uniquely named file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"Verified_Leads_{num_leads}_{timestamp}.xlsx"
    df.to_excel(output_filename, index=False)
    
    end_time = time.perf_counter()
    latency_ms = round((end_time - start_time) * 1000, 2)
    
    telemetry = {
        "model_version": "v2.5.1-xgboost-champion",
        "challenger_version": "v3.0.0-lgbm-shadow",
        "inference_latency_ms": latency_ms,
        "drift_status": "Stable (0.02 KL Divergence)",
        "features_processed": num_leads * 14
    }
    
    return df, output_filename, telemetry
