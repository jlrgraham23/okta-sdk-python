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

class AuthenticatorProviderConfiguration(object):
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
        'auth_port': 'int',
        'host_name': 'str',
        'instance_id': 'str',
        'shared_secret': 'str',
        'user_name_template': 'AuthenticatorProviderConfigurationUserNameTemplate'
    }

    attribute_map = {
        'auth_port': 'authPort',
        'host_name': 'hostName',
        'instance_id': 'instanceId',
        'shared_secret': 'sharedSecret',
        'user_name_template': 'userNameTemplate'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, auth_port=None, host_name=None, instance_id=None, shared_secret=None, user_name_template=None):  # noqa: E501
        """AuthenticatorProviderConfiguration - a model defined in Swagger"""  # noqa: E501
        self._auth_port = None
        self._host_name = None
        self._instance_id = None
        self._shared_secret = None
        self._user_name_template = None
        self.discriminator = None
        if auth_port is not None:
            self.auth_port = auth_port
        if host_name is not None:
            self.host_name = host_name
        if instance_id is not None:
            self.instance_id = instance_id
        if shared_secret is not None:
            self.shared_secret = shared_secret
        if user_name_template is not None:
            self.user_name_template = user_name_template

    @property
    def auth_port(self):
        """Gets the auth_port of this AuthenticatorProviderConfiguration.  # noqa: E501


        :return: The auth_port of this AuthenticatorProviderConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._auth_port

    @auth_port.setter
    def auth_port(self, auth_port):
        """Sets the auth_port of this AuthenticatorProviderConfiguration.


        :param auth_port: The auth_port of this AuthenticatorProviderConfiguration.  # noqa: E501
        :type: int
        """

        self._auth_port = auth_port

    @property
    def host_name(self):
        """Gets the host_name of this AuthenticatorProviderConfiguration.  # noqa: E501


        :return: The host_name of this AuthenticatorProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this AuthenticatorProviderConfiguration.


        :param host_name: The host_name of this AuthenticatorProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def instance_id(self):
        """Gets the instance_id of this AuthenticatorProviderConfiguration.  # noqa: E501


        :return: The instance_id of this AuthenticatorProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AuthenticatorProviderConfiguration.


        :param instance_id: The instance_id of this AuthenticatorProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def shared_secret(self):
        """Gets the shared_secret of this AuthenticatorProviderConfiguration.  # noqa: E501


        :return: The shared_secret of this AuthenticatorProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this AuthenticatorProviderConfiguration.


        :param shared_secret: The shared_secret of this AuthenticatorProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def user_name_template(self):
        """Gets the user_name_template of this AuthenticatorProviderConfiguration.  # noqa: E501


        :return: The user_name_template of this AuthenticatorProviderConfiguration.  # noqa: E501
        :rtype: AuthenticatorProviderConfigurationUserNameTemplate
        """
        return self._user_name_template

    @user_name_template.setter
    def user_name_template(self, user_name_template):
        """Sets the user_name_template of this AuthenticatorProviderConfiguration.


        :param user_name_template: The user_name_template of this AuthenticatorProviderConfiguration.  # noqa: E501
        :type: AuthenticatorProviderConfigurationUserNameTemplate
        """

        self._user_name_template = user_name_template

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
        if issubclass(AuthenticatorProviderConfiguration, dict):
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
        if not isinstance(other, AuthenticatorProviderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
