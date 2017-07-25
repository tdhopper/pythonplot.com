import plotly
import os
plotly.tools.set_credentials_file(username=os.environ.get('PLOTLY_USER'), api_key=os.environ.get('PLOTLY_API_KEY'))
