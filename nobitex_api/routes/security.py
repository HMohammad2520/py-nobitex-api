# nobitex_api\routes\security.py
from ._base import NobitexRoute

"""
https://api.nobitex.ir/security/anti-phishing #Done 2
https://api.nobitex.ir/security/emergency-cancel/activate #Done
"""

class Security(NobitexRoute):
    """
    Nobitex API Security endpoint.
    """

    _route_path: str = 'security'
    _version: str = ''

    def get_anti_phishing(
            self,
        ) -> str:

        return self._client._send_request(
            method='POST',
            route=self._create_route('anti-phishing')
        ).get('antiPhishingCode')

    def set_anti_phishing(
            self,
            code: str,
            otpCode:str,
        ) -> dict:
        """
        Set Anti-phishing endpoint.

        Args:
            code (str): anti-phishing code.
            otpCode (str): 2FA code.
        Returns:
            dict: response from server.
        """

        post_parms = {
            'code': code,
            'otpCode': otpCode,
        }

        return self._client._send_request(
            method='POST',
            route=self._create_route('anti-phishing'),
            post_parms=post_parms,
        )
    
    def activate_emergency_cancel(
            self,
        ) -> dict:
        """
        Activate emergency cancel endpoint.
        
        Returns:
            dict: response from server.
        """
        return self._client._send_request(
            method='GET',
            route=self._create_route('emergency-cancel', 'activate'),
        )