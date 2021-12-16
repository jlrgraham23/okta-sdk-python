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

class AuthorizationServerCredentialsSigningConfig(object):
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
        'kid': 'str',
        'last_rotated': 'datetime',
        'next_rotation': 'datetime',
        'rotation_mode': 'AuthorizationServerCredentialsRotationMode',
        'use': 'AuthorizationServerCredentialsUse'
    }

    attribute_map = {
        'kid': 'kid',
        'last_rotated': 'lastRotated',
        'next_rotation': 'nextRotation',
        'rotation_mode': 'rotationMode',
        'use': 'use'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, kid=None, last_rotated=None, next_rotation=None, rotation_mode=None, use=None):  # noqa: E501
        """AuthorizationServerCredentialsSigningConfig - a model defined in Swagger"""  # noqa: E501
        self._kid = None
        self._last_rotated = None
        self._next_rotation = None
        self._rotation_mode = None
        self._use = None
        self.discriminator = None
        if kid is not None:
            self.kid = kid
        if last_rotated is not None:
            self.last_rotated = last_rotated
        if next_rotation is not None:
            self.next_rotation = next_rotation
        if rotation_mode is not None:
            self.rotation_mode = rotation_mode
        if use is not None:
            self.use = use

    @property
    def kid(self):
        """Gets the kid of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501


        :return: The kid of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this AuthorizationServerCredentialsSigningConfig.


        :param kid: The kid of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :type: str
        """

        self._kid = kid

    @property
    def last_rotated(self):
        """Gets the last_rotated of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501


        :return: The last_rotated of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._last_rotated

    @last_rotated.setter
    def last_rotated(self, last_rotated):
        """Sets the last_rotated of this AuthorizationServerCredentialsSigningConfig.


        :param last_rotated: The last_rotated of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :type: datetime
        """

        self._last_rotated = last_rotated

    @property
    def next_rotation(self):
        """Gets the next_rotation of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501


        :return: The next_rotation of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._next_rotation

    @next_rotation.setter
    def next_rotation(self, next_rotation):
        """Sets the next_rotation of this AuthorizationServerCredentialsSigningConfig.


        :param next_rotation: The next_rotation of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :type: datetime
        """

        self._next_rotation = next_rotation

    @property
    def rotation_mode(self):
        """Gets the rotation_mode of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501


        :return: The rotation_mode of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :rtype: AuthorizationServerCredentialsRotationMode
        """
        return self._rotation_mode

    @rotation_mode.setter
    def rotation_mode(self, rotation_mode):
        """Sets the rotation_mode of this AuthorizationServerCredentialsSigningConfig.


        :param rotation_mode: The rotation_mode of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :type: AuthorizationServerCredentialsRotationMode
        """

        self._rotation_mode = rotation_mode

    @property
    def use(self):
        """Gets the use of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501


        :return: The use of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :rtype: AuthorizationServerCredentialsUse
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this AuthorizationServerCredentialsSigningConfig.


        :param use: The use of this AuthorizationServerCredentialsSigningConfig.  # noqa: E501
        :type: AuthorizationServerCredentialsUse
        """

        self._use = use

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
        if issubclass(AuthorizationServerCredentialsSigningConfig, dict):
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
        if not isinstance(other, AuthorizationServerCredentialsSigningConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
