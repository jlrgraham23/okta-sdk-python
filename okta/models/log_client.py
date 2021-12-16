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

from okta.helpers import to_snake_case

class LogClient(object):
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
        'device': 'str',
        'geographical_context': 'LogGeographicalContext',
        'id': 'str',
        'ip_address': 'str',
        'user_agent': 'LogUserAgent',
        'zone': 'str'
    }

    attribute_map = {
        'device': 'device',
        'geographical_context': 'geographicalContext',
        'id': 'id',
        'ip_address': 'ipAddress',
        'user_agent': 'userAgent',
        'zone': 'zone'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, device=None, geographical_context=None, id=None, ip_address=None, user_agent=None, zone=None):  # noqa: E501
        """LogClient - a model defined in Swagger"""  # noqa: E501
        self._device = None
        self._geographical_context = None
        self._id = None
        self._ip_address = None
        self._user_agent = None
        self._zone = None
        self.discriminator = None
        if device is not None:
            self.device = device
        if geographical_context is not None:
            self.geographical_context = geographical_context
        if id is not None:
            self.id = id
        if ip_address is not None:
            self.ip_address = ip_address
        if user_agent is not None:
            self.user_agent = user_agent
        if zone is not None:
            self.zone = zone

    @property
    def device(self):
        """Gets the device of this LogClient.  # noqa: E501


        :return: The device of this LogClient.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this LogClient.


        :param device: The device of this LogClient.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def geographical_context(self):
        """Gets the geographical_context of this LogClient.  # noqa: E501


        :return: The geographical_context of this LogClient.  # noqa: E501
        :rtype: LogGeographicalContext
        """
        return self._geographical_context

    @geographical_context.setter
    def geographical_context(self, geographical_context):
        """Sets the geographical_context of this LogClient.


        :param geographical_context: The geographical_context of this LogClient.  # noqa: E501
        :type: LogGeographicalContext
        """

        self._geographical_context = geographical_context

    @property
    def id(self):
        """Gets the id of this LogClient.  # noqa: E501


        :return: The id of this LogClient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogClient.


        :param id: The id of this LogClient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip_address(self):
        """Gets the ip_address of this LogClient.  # noqa: E501


        :return: The ip_address of this LogClient.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this LogClient.


        :param ip_address: The ip_address of this LogClient.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def user_agent(self):
        """Gets the user_agent of this LogClient.  # noqa: E501


        :return: The user_agent of this LogClient.  # noqa: E501
        :rtype: LogUserAgent
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this LogClient.


        :param user_agent: The user_agent of this LogClient.  # noqa: E501
        :type: LogUserAgent
        """

        self._user_agent = user_agent

    @property
    def zone(self):
        """Gets the zone of this LogClient.  # noqa: E501


        :return: The zone of this LogClient.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this LogClient.


        :param zone: The zone of this LogClient.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if issubclass(LogClient, dict):
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
        if not isinstance(other, LogClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
