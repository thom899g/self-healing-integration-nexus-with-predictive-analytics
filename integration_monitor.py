import logging
from typing import Dict, Any
import requests

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class IntegrationMonitor:
    """Monitors external integrations and reports health metrics."""
    
    def __init__(self):
        self.integration_endpoints = []
    
    def check_health(self) -> Dict[str, Any]:
        """Checks the health of all monitored integrations.
        
        Returns:
            Dictionary with integration health status.
        """
        results = {}
        for endpoint in self.integration_endpoints:
            result = self._check_endpoint(endpoint)
            results[endpoint] = result
        return results
    
    def _check_endpoint(self, endpoint: str) -> Dict[str, Any]:
        """Checks the health of a specific integration endpoint."""
        try:
            response = requests.get(endpoint)
            status = response.status_code == 200
            latency = response.elapsed.total_seconds()
            
            logger.info(f"Checked {endpoint}: Status {status}, Latency {latency}")
            
            return {
                'status': status,
                'latency': latency,
                'timestamp': self._get_current_time()
            }
        except Exception as e:
            logger.error(f"Failed to check {endpoint}: {str(e)}")
            return {'status': False, 'error': str(e)}
    
    def _get_current_time(self) -> float:
        """Returns current timestamp in seconds."""
        pass
    
    def add_endpoint(self, endpoint: str):
        """Adds an integration endpoint for monitoring."""
        self.integration_endpoints.append(endpoint)