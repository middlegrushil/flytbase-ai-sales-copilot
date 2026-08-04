from agents.qualification import qualify_lead
from agents.research import research_company
from agents.strategy import create_strategy
from agents.recommendation import recommend_solution

from agents.meeting_prep import generate_meeting_prep
from agents.email_generator import generate_email
from agents.objection_handler import generate_objections
from agents.risk_analysis import analyze_risks
from agents.stakeholder import identify_stakeholders
from agents.crm_summary import generate_crm_summary
from agents.next_action import generate_next_action
from agents.discovery_questions import generate_discovery_questions

from agents.report import generate_report


print("=" * 70)
print("              FlytBase AI Sales Copilot")
print("=" * 70)

print("\n[1/12] Qualifying Lead...")
qualify_lead()

print("\n[2/12] Researching Company...")
research_company()

print("\n[3/12] Creating Sales Strategy...")
create_strategy()

print("\n[4/12] Recommending FlytBase Solution...")
recommend_solution()

print("\n[5/12] Preparing Meeting Brief...")
generate_meeting_prep()

print("\n[6/12] Generating Follow-up Email...")
generate_email()

print("\n[7/12] Generating Discovery Questions...")
generate_discovery_questions()

print("\n[8/12] Predicting Customer Objections...")
generate_objections()

print("\n[9/12] Performing Risk Analysis...")
analyze_risks()

print("\n[10/12] Mapping Stakeholders...")
identify_stakeholders()

print("\n[11/12] Generating CRM Summary...")
generate_crm_summary()

print("\n[12/12] Generating Next Action & Sales Brief...")
generate_next_action()
generate_report()

print("\n" + "=" * 70)
print("🎉 FlytBase AI Sales Copilot Completed Successfully!")
print("=" * 70)

print("\nGenerated Files:")

print("✓ qualification.json")
print("✓ research.json")
print("✓ strategy.json")
print("✓ recommendation.json")
print("✓ meeting_prep.md")
print("✓ followup_email.md")
print("✓ discovery_questions.md")
print("✓ objections.json")
print("✓ risk_analysis.json")
print("✓ stakeholders.json")
print("✓ crm_summary.md")
print("✓ next_action.json")
print("✓ sales_brief.md")

print("\nEverything has been saved inside the output folder.")