import http.server
import os
import socketserver
import jinja2

SERVER_PORT = int(os.getenv('SERVER_PORT', 8080))

Handler = http.server.SimpleHTTPRequestHandler

template_vars = {
    'app_name': os.getenv('APP_NAME', 'Oceannik'),
    'app_workspace': os.getenv('APP_WORKSPACE', 'default'),
    'app_debug_params': os.getenv('APP_DEBUG_PARAMS', {}),
}

current_script_path = os.path.dirname(os.path.abspath(__file__))
index_html_template_path = 'index.html.j2'
index_html_rendered_file_path = os.path.join('www', 'index.html')

jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(current_script_path))
rendered_index_html_file_content = jinja2_environment.get_template(index_html_template_path).render(template_vars)

with open(index_html_rendered_file_path, "w") as result_file:
    result_file.write(rendered_index_html_file_content)

# Serve the index.html file from the www/ directory

os.chdir('www')

with socketserver.TCPServer(('', SERVER_PORT), Handler) as httpd:
    print("serving at port", SERVER_PORT)
    httpd.serve_forever()
