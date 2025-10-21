import os
import time
from health_endpoint import create_health_endpoint

# Set start time for uptime calculation
os.environ['START_TIME'] = str(time.time())
os.environ['SERVICE_NAME'] = 'demo-v117.4'

# Import your main app
try:
    from app import app
    create_health_endpoint(app)
    print("Health endpoint added to Flask app")
    
    if __name__ == "__main__":
        app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
except ImportError:
    try:
        from main import app
        create_health_endpoint(app)
        print("Health endpoint added to Flask app")
        
        if __name__ == "__main__":
            app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    except ImportError:
        print("No Flask app found")
