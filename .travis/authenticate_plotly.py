# DEPRECATED: This file is no longer used.
#
# With plotly v5+, credentials are not required for local rendering.
# Plotly authentication is only needed if uploading to Chart Studio.
# This project renders plots locally to PNG using Kaleido, so no
# authentication is necessary.
#
# Historical code (plotly v4):
# import plotly
# import os
# plotly.tools.set_credentials_file(username=os.environ.get('PLOTLY_USER'), api_key=os.environ.get('PLOTLY_API_KEY'))

import sys
print("Warning: plotly authentication is no longer needed with plotly v5+", file=sys.stderr)
print("This script is deprecated and can be removed.", file=sys.stderr)
