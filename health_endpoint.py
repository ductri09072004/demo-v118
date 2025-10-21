"""
Health endpoint cho Kubernetes health checks
"""
import time
import psutil
import platform
import sys
import os
from datetime import datetime

def get_health_status():
    """Lấy thông tin health status"""
    try:
        start_time = float(os.environ.get('START_TIME', time.time()))
        uptime_seconds = time.time() - start_time
        uptime_str = f"{int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m {int(uptime_seconds % 60)}s"
        
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        process = psutil.Process()
        process_memory = process.memory_info()
        
        return {
            "status": "healthy",
            "service": os.environ.get('SERVICE_NAME', 'unknown'),
            "uptime": uptime_str,
            "timestamp": datetime.now().isoformat(),
            "system": {
                "cpu_usage": f"{cpu_percent:.1f}%",
                "memory_usage": f"{memory.percent:.1f}%",
                "process_memory_mb": f"{process_memory.rss / 1024 / 1024:.1f} MB"
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def create_health_endpoint(app):
    """Thêm health endpoint vào Flask app"""
    @app.route('/api/health')
    def health():
        return get_health_status()
    
    @app.route('/health')
    def health_simple():
        return {"status": "ok"}
