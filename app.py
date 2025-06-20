import streamlit as st
from typing import List, Dict
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu

# ==============================================
# DATA AND CONFIGURATION
# ==============================================

JOB_SUGGESTIONS = [
    {"text": "Software Engineer"},
    {"text": "Data Scientist"},
    {"text": "Product Manager"},
    {"text": "DevOps Engineer"},
    {"text": "UI/UX Designer"},
    {"text": "Frontend Developer"},
    {"text": "Backend Developer"},
    {"text": "Full Stack Developer"},
    {"text": "Machine Learning Engineer"},
    {"text": "Cloud Architect"}
]

LOCATION_SUGGESTIONS = [
    {"text": "Bangalore", "type": "city", "state": "Karnataka"},
    {"text": "Mumbai", "type": "city", "state": "Maharashtra"},
    {"text": "Delhi", "type": "city", "state": "Delhi"},
    {"text": "Hyderabad", "type": "city", "state": "Telangana"},
    {"text": "Pune", "type": "city", "state": "Maharashtra"},
    {"text": "Chennai", "type": "city", "state": "Tamil Nadu"},
    {"text": "Gurgaon", "type": "city", "state": "Haryana"},
    {"text": "Remote", "type": "work_mode"},
    {"text": "Hybrid", "type": "work_mode"},
    {"text": "Karnataka", "type": "state"},
    {"text": "Maharashtra", "type": "state"},
    {"text": "Telangana", "type": "state"},
    {"text": "Tamil Nadu", "type": "state"}
]

# ==============================================
# UTILITY FUNCTIONS
# ==============================================

def filter_suggestions(query: str, suggestions: List[Dict]) -> List[Dict]:
    """Filter suggestions based on user input"""
    if not query:
        return []
    return [s for s in suggestions if query.lower() in s["text"].lower()][:5]

def filter_location_suggestions(query: str, suggestions: List[Dict]) -> List[Dict]:
    """Filter location suggestions with smart categorization"""
    if not query or len(query) < 2:
        return []
        
    matching_states = [s for s in suggestions if s.get("type") == "state" and query.lower() in s["text"].lower()]
    matching_cities = [s for s in suggestions if s.get("type") == "city" and query.lower() in s["text"].lower()]
    matching_work_modes = [s for s in suggestions if s.get("type") == "work_mode" and query.lower() in s["text"].lower()]
    
    return matching_states + matching_cities + matching_work_modes[:7]

def get_filter_options():
    """Get filter options for job search"""
    return {
        "experience_levels": [
            {"id": "all", "text": "All Levels"},
            {"id": "fresher", "text": "Fresher"},
            {"id": "0-1", "text": "0-1 years"},
            {"id": "1-3", "text": "1-3 years"},
            {"id": "3-5", "text": "3-5 years"},
            {"id": "5-7", "text": "5-7 years"},
            {"id": "7-10", "text": "7-10 years"},
            {"id": "10+", "text": "10+ years"}
        ],
        "salary_ranges": [
            {"id": "all", "text": "All Ranges"},
            {"id": "0-3", "text": "0-3 LPA"},
            {"id": "3-6", "text": "3-6 LPA"},
            {"id": "6-10", "text": "6-10 LPA"},
            {"id": "10-15", "text": "10-15 LPA"},
            {"id": "15+", "text": "15+ LPA"}
        ],
        "job_types": [
            {"id": "all", "text": "All Types"},
            {"id": "full-time", "text": "Full Time"},
            {"id": "part-time", "text": "Part Time"},
            {"id": "contract", "text": "Contract"},
            {"id": "remote", "text": "Remote"}
        ]
    }

# ==============================================
# CORE COMPONENTS
# ==============================================

class JobPortal:
    """Mock job portal class"""
    def search_jobs(self, job_query: str, location: str, experience: Dict) -> List[Dict]:
        """Mock job search function"""
        return [{
            "portal": "LinkedIn",
            "icon": "fab fa-linkedin",
            "title": f"{job_query} at Tech Company",
            "company": "Tech Corp Inc.",
            "location": location or "Remote",
            "experience": experience["text"],
            "salary": "₹10-15 LPA",
            "url": "https://linkedin.com"
        }, {
            "portal": "Indeed",
            "icon": "fas fa-search",
            "title": f"Senior {job_query}",
            "company": "Software Solutions",
            "location": location or "Hybrid",
            "experience": "5-7 years",
            "salary": "₹15-20 LPA",
            "url": "https://indeed.com"
        }]

def render_company_section():
    """Render featured companies section"""
    st.markdown("""
        <style>
        .company-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1rem;
            padding: 1rem 0;
        }
        .company-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 1rem;
            transition: transform 0.2s;
            cursor: pointer;
        }
        .company-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.08);
        }
        .company-header {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .company-icon {
            font-size: 1.5rem;
            margin-right: 0.5rem;
        }
        .company-categories {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.5rem;
        }
        .company-category {
            background: rgba(255, 255, 255, 0.1);
            padding: 0.2rem 0.5rem;
            border-radius: 15px;
            font-size: 0.8rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### 🏢 Featured Companies")
    
    companies = [
        {
            "name": "Google",
            "icon": "fab fa-google",
            "color": "#4285F4",
            "description": "Search engine and cloud computing company",
            "categories": ["Tech", "Global"],
            "careers_url": "https://careers.google.com"
        },
        {
            "name": "Microsoft",
            "icon": "fab fa-microsoft",
            "color": "#7FBA00",
            "description": "Computer software and hardware company",
            "categories": ["Tech", "Global"],
            "careers_url": "https://careers.microsoft.com"
        },
        {
            "name": "TCS",
            "icon": "fas fa-building",
            "color": "#3D8BFF",
            "description": "Indian multinational IT services company",
            "categories": ["Tech", "Indian"],
            "careers_url": "https://www.tcs.com/careers"
        }
    ]
    
    st.markdown('<div class="company-grid">', unsafe_allow_html=True)
    for company in companies:
        st.markdown(f"""
            <a href="{company['careers_url']}" target="_blank" style="text-decoration: none; color: inherit;">
                <div class="company-card">
                    <div class="company-header">
                        <i class="{company['icon']} company-icon" style="color: {company['color']}"></i>
                        <h3 style="margin: 0;">{company['name']}</h3>
                    </div>
                    <p style="margin: 0.5rem 0; color: #888;">{company['description']}</p>
                    <div class="company-categories">
                        {' '.join(f'<span class="company-category">{cat}</span>' for cat in company['categories'])}
                    </div>
                </div>
            </a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_market_insights():
    """Render job market insights"""
    insights = {
        "trending_skills": [
            {"name": "Python", "icon": "fab fa-python", "growth": "25%"},
            {"name": "React", "icon": "fab fa-react", "growth": "30%"},
            {"name": "AWS", "icon": "fab fa-aws", "growth": "40%"}
        ],
        "top_locations": [
            {"name": "Bangalore", "icon": "fas fa-city", "jobs": "15K+"},
            {"name": "Hyderabad", "icon": "fas fa-building", "jobs": "8K+"}
        ],
        "salary_insights": [
            {"role": "Software Engineer", "range": "10-20 LPA", "experience": "3-5 years"}
        ]
    }
    
    st.markdown("### 📊 Job Market Insights")
    tab1, tab2, tab3 = st.tabs(["Trending Skills", "Top Locations", "Salary Insights"])
    
    with tab1:
        cols = st.columns(3)
        for i, skill in enumerate(insights["trending_skills"]):
            with cols[i]:
                st.markdown(f"""
                    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 10px;">
                        <i class="{skill['icon']}" style="font-size: 2rem; color: #00bfa5;"></i>
                        <h4>{skill['name']}</h4>
                        <p style="color: #00c853; font-weight: bold;">Growth: {skill['growth']}</p>
                    </div>
                """, unsafe_allow_html=True)

def render_linkedin_scraper():
    """Render LinkedIn scraper interface"""
    st.markdown("### 🔗 LinkedIn Job Scraper")
    with st.form("linkedin_form"):
        job = st.text_input("Job Title", placeholder="Software Engineer")
        location = st.text_input("Location", placeholder="India")
        if st.form_submit_button("Search LinkedIn"):
            st.success(f"Searching for {job} jobs in {location}")

# ==============================================
# MAIN APPLICATION
# ==============================================

def render_job_search():
    """Main job search interface"""
    st.set_page_config(
        page_title="JobSearch AI",
        page_icon="💼",
        layout="wide"
    )
    
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: white;
        }
        .stButton>button {
            background: linear-gradient(90deg, #00bfa5, #00897b);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🔍 Smart Job Search")
    
    # Market Insights
    render_market_insights()
    
    # Job Search
    with st.container():
        st.markdown("### 🚀 Find Your Dream Job")
        tab1, tab2 = st.tabs(["Job Portal", "LinkedIn"])
        
        with tab1:
            col1, col2 = st.columns([2, 1])
            with col1:
                job = st.text_input("Job Title", placeholder="Software Engineer")
            with col2:
                location = st.text_input("Location", placeholder="Bangalore")
            
            if st.button("Search Jobs", type="primary"):
                if job:
                    portal = JobPortal()
                    results = portal.search_jobs(job, location, {"text": "1-3 years"})
                    
                    for result in results:
                        st.markdown(f"""
                            <div style="padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 10px; margin-bottom: 1rem;">
                                <h3>{result['title']}</h3>
                                <p><i class="fas fa-building"></i> {result['company']}</p>
                                <p><i class="fas fa-map-marker-alt"></i> {result['location']}</p>
                                <a href="{result['url']}" target="_blank" style="display: inline-block; background: #00bfa5; color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none;">
                                    View Job <i class="fas fa-external-link-alt"></i>
                                </a>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("Please enter a job title")
        
        with tab2:
            render_linkedin_scraper()
    
    # Featured Companies
    render_company_section()

if __name__ == "__main__":
    render_job_search()