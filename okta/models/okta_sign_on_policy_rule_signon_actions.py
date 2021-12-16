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

class OktaSignOnPolicyRuleSignonActions(object):
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
        'access': 'PolicyAccess',
        'factor_lifetime': 'int',
        'factor_prompt_mode': 'OktaSignOnPolicyFactorPromptMode',
        'remember_device_by_default': 'bool',
        'require_factor': 'bool',
        'session': 'OktaSignOnPolicyRuleSignonSessionActions'
    }

    attribute_map = {
        'access': 'access',
        'factor_lifetime': 'factorLifetime',
        'factor_prompt_mode': 'factorPromptMode',
        'remember_device_by_default': 'rememberDeviceByDefault',
        'require_factor': 'requireFactor',
        'session': 'session'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, access=None, factor_lifetime=None, factor_prompt_mode=None, remember_device_by_default=False, require_factor=False, session=None):  # noqa: E501
        """OktaSignOnPolicyRuleSignonActions - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self._factor_lifetime = None
        self._factor_prompt_mode = None
        self._remember_device_by_default = None
        self._require_factor = None
        self._session = None
        self.discriminator = None
        if access is not None:
            self.access = access
        if factor_lifetime is not None:
            self.factor_lifetime = factor_lifetime
        if factor_prompt_mode is not None:
            self.factor_prompt_mode = factor_prompt_mode
        if remember_device_by_default is not None:
            self.remember_device_by_default = remember_device_by_default
        if require_factor is not None:
            self.require_factor = require_factor
        if session is not None:
            self.session = session

    @property
    def access(self):
        """Gets the access of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The access of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: PolicyAccess
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this OktaSignOnPolicyRuleSignonActions.


        :param access: The access of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: PolicyAccess
        """

        self._access = access

    @property
    def factor_lifetime(self):
        """Gets the factor_lifetime of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The factor_lifetime of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: int
        """
        return self._factor_lifetime

    @factor_lifetime.setter
    def factor_lifetime(self, factor_lifetime):
        """Sets the factor_lifetime of this OktaSignOnPolicyRuleSignonActions.


        :param factor_lifetime: The factor_lifetime of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: int
        """

        self._factor_lifetime = factor_lifetime

    @property
    def factor_prompt_mode(self):
        """Gets the factor_prompt_mode of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The factor_prompt_mode of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: OktaSignOnPolicyFactorPromptMode
        """
        return self._factor_prompt_mode

    @factor_prompt_mode.setter
    def factor_prompt_mode(self, factor_prompt_mode):
        """Sets the factor_prompt_mode of this OktaSignOnPolicyRuleSignonActions.


        :param factor_prompt_mode: The factor_prompt_mode of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: OktaSignOnPolicyFactorPromptMode
        """

        self._factor_prompt_mode = factor_prompt_mode

    @property
    def remember_device_by_default(self):
        """Gets the remember_device_by_default of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The remember_device_by_default of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: bool
        """
        return self._remember_device_by_default

    @remember_device_by_default.setter
    def remember_device_by_default(self, remember_device_by_default):
        """Sets the remember_device_by_default of this OktaSignOnPolicyRuleSignonActions.


        :param remember_device_by_default: The remember_device_by_default of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: bool
        """

        self._remember_device_by_default = remember_device_by_default

    @property
    def require_factor(self):
        """Gets the require_factor of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The require_factor of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: bool
        """
        return self._require_factor

    @require_factor.setter
    def require_factor(self, require_factor):
        """Sets the require_factor of this OktaSignOnPolicyRuleSignonActions.


        :param require_factor: The require_factor of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: bool
        """

        self._require_factor = require_factor

    @property
    def session(self):
        """Gets the session of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501


        :return: The session of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :rtype: OktaSignOnPolicyRuleSignonSessionActions
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this OktaSignOnPolicyRuleSignonActions.


        :param session: The session of this OktaSignOnPolicyRuleSignonActions.  # noqa: E501
        :type: OktaSignOnPolicyRuleSignonSessionActions
        """

        self._session = session

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
        if issubclass(OktaSignOnPolicyRuleSignonActions, dict):
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
        if not isinstance(other, OktaSignOnPolicyRuleSignonActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
