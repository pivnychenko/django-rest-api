import urllib.request
import json
from typing import Any

from django.conf import settings


class GeoLocation:
	"""
	Pars Geo Location
	"""
	def __init__(self, request: Any):
		self.request = request
		self.ip = self.request.META.get('HTTP_X_FORWARDED_FOR', '')

	@property
	def data_geo_location(self) -> dict:
		"""
		method parser data from service geolocation-db by ip
		Args:
		    Nothing.
		Returns:
		    data: parse from geolocation-db
		"""

		with urllib.request.urlopen(f"{settings.GEOIP_LOCATION}{self.ip}") as url:
			data = json.loads(url.read().decode())
		return data

	@property
	def get_ip(self):
		"""
		method for get ip from self.request or from geolocation-db
		Args:
		    Nothing.
		Returns:
		    ip: parse from request
		"""
		ip = self.ip if self.ip else self.data_geo_location.get("IPv4")
		return ip

	@property
	def get_lat_long(self) -> dict:
		"""
		method parser lat, long from service geolocation-db by ip
		Args:
		    Nothing.
		Returns:
		    lat: parse from geolocation-db
		    long: parse from geolocation-db
		"""
		loc = self.data_geo_location
		return {"lat": loc.get("latitude"), "long": loc.get("longitude")}