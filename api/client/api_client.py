"""
Module:
    api_client.py

Description:
    Base HTTP client for API automation.

Author:
    Shubham Pandey
"""

import httpx


class APIClient:

    def __init__(
            self,
            base_url: str,
            logger,
            timeout: int = 30
    ):

        self.logger = logger

        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout
        )
    def _send_request(self,method: str,url: str,**kwargs):
        """
        Sends an HTTP request.
        """

        self.logger.info(
            f"{method} : {url}"
        )

        response = self.client.request(
            method=method,
            url=url,
            **kwargs
        )

        self.logger.info(
            f"Status Code : {response.status_code}"
        )
        return response
    
    def get(self,url: str,**kwargs):
        return self._send_request(
            "GET",
            url,
            **kwargs
        )
    def post(
            self,
            url: str,
            **kwargs
    ):
        return self._send_request(
            "POST",
            url,
            **kwargs
        )
    def put(
        self,
        url: str,
        **kwargs
    ):
        return self._send_request(
            "PUT",
            url,
            **kwargs
        )
    def patch(
        self,
        url: str,
        **kwargs
    ):
        return self._send_request(
            "PATCH",
            url,
            **kwargs
        )
    def delete(
        self,
        url: str,
        **kwargs
    ):
        return self._send_request(
            "DELETE",
            url,
            **kwargs
        )
    def close(self):
        """
        Closes the HTTP client.
        """

        self.client.close()