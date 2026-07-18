class OpenCodeWorkflowRunnerClient:
    def build_tree(self, workflow_description: str, conditions: dict) -> dict:
        tree = [{"step": 0, "action": f"INIT: {workflow_description}", "branch": "main"}]
        branch_count = 0
        for condition, outcome in conditions.items():
            branch_count += 1
            tree.append({
                "step": branch_count,
                "action": f"IF {condition} THEN {outcome}",
                "branch": f"branch-{branch_count}"
            })
        tree.append({"step": len(tree), "action": "FINALIZE: Merge branches and deliver output", "branch": "main"})
        return {"execution_tree": tree, "branch_count": branch_count}
