# Import flask module to render the application.
from flask import Flask
 
# Create an app.
app = Flask(__name__)
 
# App route created as per requirements.
@app.route('/')
def index():
    name_of_company = "<strong>Wild Rydes</strong>"
    developer_name = "Tailong Cheng"
    student_id = "100898513"
    
    # Create HTML with centered and styled content.
    html_content = f"<div style='text-align: center; padding-top: 20px;'>" \
                   f"<p>Company Name: {name_of_company}<br>" \
                   f"Developer: {developer_name}<br>" \
                   f"Student ID: {student_id}</p></div>"
    
    return html_content
 
# Run it on port 8080 on local host.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
