def custom_file():
    print("Hello from practice file :)")

#  but how to run it?
# go to pyproject.toml, under the 'scripts'section we'll find the run commands
# we can also customize these commands as our wish just add 'uv run' before the variable name and run the command on terminal

# tan tadaa here's the output!!
# "Hello from uv-project2!"

# IMPORTANT NOTES 👇🏻
#if I have created a file named "main.py" and inside this main.py my function name is "custom_file" so 
# i'll make a command on .toml file like:
# practice = "uv_project2.main:custom_file" 
#   👆🏻          👆🏻        👆🏻        👆🏻
# variable = foldername.filename:functionname

# command will be "uv run variable"