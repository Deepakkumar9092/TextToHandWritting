# import pywhatkit as pw

# txt = """This is Deepak Kumar. I am from Jharkhand and I completed my 10th and 12th 
#     from Jharkhand itself. I have completed my Bachelor's of Technology from Arya Institute Of 
#     Engineering and Technology it is affiliate from Rajasthan Technical University. I am skilled in for Frontend Developer is 
#     Html, Css, JavaScript and Reactjs and for backend development is Core Java, JDBC, Hibernate, Data Jpa, Servlets
#     and Spring Boot. I have experience in working with Google Cloud Storage and Google."""

# pw.text_to_handwriting(txt, "about.png",[0, 0, 30])
# print("END")


# import pywhatkit as pw
# from pywhatkit.core.exceptions import UnableToAccessApi

# txt = """This is Deepak Kumar. I am from Jharkhand and I completed my 10th and 12th 
#     from Jharkhand itself. I have completed my Bachelor's of Technology from Arya Institute Of 
#     Engineering and Technology it is affiliate from Rajasthan Technical University. I am skilled in for Frontend Developer is 
#     Html, Css, JavaScript and Reactjs and for backend development is Core Java, JDBC, Hibernate, Data Jpa, Servlets
#     and Spring Boot. I have experience in working with Google Cloud Storage and Google."""

# try:
#     pw.text_to_handwriting(txt, "demo.png", [0, 0, 30])
#     print("Handwriting saved as 'demo.png'")
# except UnableToAccessApi as e:
#     print("Error:", e)
# print("END")


import pywhatkit as pw
from pywhatkit.core.exceptions import UnableToAccessApi

txt = """This is Deepak Kumar. I am from Jharkhand and I completed my 10th and 12th 
from Jharkhand itself. I have completed my Bachelor's of Technology from Arya Institute Of 
Engineering and Technology it is affiliate from Rajasthan Technical University. I am skilled in for Frontend Developer is 
Html, Css, JavaScript and Reactjs and for backend development is Core Java, JDBC, Hibernate, Data Jpa, Servlets
and Spring Boot. I have experience in working with Google Cloud Storage and Google."""

try:
    pw.text_to_handwriting(txt, "about.png", [0, 0, 30])
    print("Handwriting image saved as 'about.png'")
except UnableToAccessApi as e:
    print("PyWhatKit API Error:", e)
