
git clone $REPO_URL repo
cd repo
printf "ccc" > c.txt
git add c.txt
git commit -m "Add new file c.txt with some content"
git push origin master


# or provided during script invocation like in this task. You
# MUST use the REPO_URL variable that points to a repository.
# But you should NOT define REPO_URL in this script. When
# testing your solution locally, you must define it before
# calling script.sh (as shown in the task descption):
# REPO_URL="some-url" ./script.sh

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
