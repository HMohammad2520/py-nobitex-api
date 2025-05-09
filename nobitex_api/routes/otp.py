from typing import Literal
from ._base import NobitexRoute

"""
https://api.nobitex.ir/otp/request #Done
"""

class OTP(NobitexRoute):
    """
    Nobitex API OTP endpoint.
    """

    _route_path: str = 'otp'
    _version: str = ''

    def send_request(
            self,
            type: Literal['email'],
            usage: Literal['address_book', 'anti_phishing_code'],
        ) -> dict:
        """
        Send OTP request to Nobitex API.

        Args:
            type (str): Type of OTP request.
            usage (str): Usage of OTP request.

        Returns:
            dict: Response from Nobitex API.
        """
        post_parms = {
            'type': type,
            'usage': usage,
            }
        
        return self._client._send_request(
            method='GET',
            route=self._create_route('request'),
            post_parms=post_parms,
        )