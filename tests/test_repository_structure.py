from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_learning_lab_structure_exists():
    required_paths = [
        "algorithms",
        "docs/learning-workflow.md",
        "docs/algorithm-index.md",
        "docs/templates/algorithm-note-template.md",
        "docs/templates/deterministic-algorithm-note-template.md",
        "docs/templates/concept-experiment-note-template.md",
        "docs/templates/project-validation-template.md",
        "examples",
        "projects",
        "notebooks",
        "tests",
    ]

    for relative_path in required_paths:
        assert (ROOT / relative_path).exists()
