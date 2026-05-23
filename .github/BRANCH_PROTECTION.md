# Branch Protection Rules

Настраивается в GitHub → Settings → Branches.

## main

### Required status checks (must pass before merge):
- `Pre-checks: Lint · Types · SAST`
- `Unit Tests + Coverage`
- `Integration Tests`
- `API + Contract + Schemathesis`
- `External API Tests (dummyjson)`
- `Quality Gate`

### Settings:
- ✅ Require pull request reviews before merging (1 reviewer)
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Require linear history (rebase only, no merge commits)
- ✅ Include administrators
- ❌ Allow force pushes

## develop

### Required status checks:
- `Pre-checks: Lint · Types · SAST`
- `Unit Tests + Coverage`
- `Quality Gate`

### Settings:
- ✅ Require status checks to pass
- ❌ Require pull request reviews (allow direct push for solo dev)
