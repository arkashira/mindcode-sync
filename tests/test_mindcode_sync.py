from mindcode_sync import MindcodeSync, CodeSuggestion

def test_analyze_project_plan():
    project_plan = "Improve efficiency and reliability"
    mindcode_sync = MindcodeSync(project_plan)
    mindcode_sync.analyze_project_plan()
    assert len(mindcode_sync.get_suggestions()) == 4

def test_rank_suggestions():
    project_plan = "Improve efficiency and reliability"
    mindcode_sync = MindcodeSync(project_plan)
    mindcode_sync.analyze_project_plan()
    mindcode_sync.rank_suggestions()
    suggestions = mindcode_sync.get_suggestions()
    assert suggestions[0].relevance == 9
    assert suggestions[1].relevance == 8
    assert suggestions[2].relevance == 7
    assert suggestions[3].relevance == 6

def test_integrate_suggested_changes():
    project_plan = "Improve efficiency and reliability"
    mindcode_sync = MindcodeSync(project_plan)
    mindcode_sync.analyze_project_plan()
    mindcode_sync.rank_suggestions()
    suggestions = mindcode_sync.get_suggestions()
    code = "def example(): pass"
    integrated_code = mindcode_sync.integrate_suggested_changes(code, suggestions[0])
    assert integrated_code == code + "\n# Added error handling"

def test_edge_case_empty_project_plan():
    project_plan = ""
    mindcode_sync = MindcodeSync(project_plan)
    mindcode_sync.analyze_project_plan()
    assert len(mindcode_sync.get_suggestions()) == 0
