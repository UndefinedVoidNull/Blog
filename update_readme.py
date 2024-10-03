# .github/workflows/update-readme.yml

name: Update README

on:
  push:
    paths:
      - 'posts/**/*.{md,pdf}'
      - 'update_readme.py'

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
      with:
        fetch-depth: 0  # Fetch all history for pushing changes

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install --upgrade pip

    - name: Run update_readme.py
      run: |
        python update_readme.py

    - name: Commit and push changes
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        git config --local user.name "github-actions[bot]"
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        # Check for changes
        if [[ `git status --porcelain` ]]; then
          git add README.md
          git commit -m "Update README with latest blog posts [skip ci]"
          git push
        else
          echo "No changes to README.md"
        fi
