# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from okta.models.application_settings_application import ApplicationSettingsApplication  # noqa: F401,E501

from okta.helpers import to_snake_case

class BookmarkApplicationSettingsApplication(ApplicationSettingsApplication):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_integration': 'bool',
        'url': 'str'
    }
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)

    attribute_map = {
        'request_integration': 'requestIntegration',
        'url': 'url'
    }
    if hasattr(ApplicationSettingsApplication, "attribute_map"):
        attribute_map.update(ApplicationSettingsApplication.attribute_map)

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, request_integration=None, url=None, *args, **kwargs):  # noqa: E501
        """BookmarkApplicationSettingsApplication - a model defined in Swagger"""  # noqa: E501
        self._request_integration = None
        self._url = None
        self.discriminator = None
        if request_integration is not None:
            self.request_integration = request_integration
        if url is not None:
            self.url = url

    @property
    def request_integration(self):
        """Gets the request_integration of this BookmarkApplicationSettingsApplication.  # noqa: E501


        :return: The request_integration of this BookmarkApplicationSettingsApplication.  # noqa: E501
        :rtype: bool
        """
        return self._request_integration

    @request_integration.setter
    def request_integration(self, request_integration):
        """Sets the request_integration of this BookmarkApplicationSettingsApplication.


        :param request_integration: The request_integration of this BookmarkApplicationSettingsApplication.  # noqa: E501
        :type: bool
        """

        self._request_integration = request_integration

    @property
    def url(self):
        """Gets the url of this BookmarkApplicationSettingsApplication.  # noqa: E501


        :return: The url of this BookmarkApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BookmarkApplicationSettingsApplication.


        :param url: The url of this BookmarkApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BookmarkApplicationSettingsApplication, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BookmarkApplicationSettingsApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
