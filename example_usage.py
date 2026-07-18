from client import OpenCodeWorkflowRunnerClient
client = OpenCodeWorkflowRunnerClient()
result = client.build_tree(
    workflow_description="Process new customer onboarding form",
    conditions={
        "email_verified == True": "Send welcome email and activate account",
        "payment_method == None": "Redirect to billing setup page",
        "referral_code != None": "Apply 20% discount and log referral attribution"
    }
)
print(f"Generated {result['branch_count']} branches:")
for node in result["execution_tree"]:
    print(f"  Step {node['step']} [{node['branch']}]: {node['action']}")
