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

class GroupRuleAction(object):
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
        'assign_user_to_groups': 'GroupRuleGroupAssignment'
    }

    attribute_map = {
        'assign_user_to_groups': 'assignUserToGroups'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, assign_user_to_groups=None):  # noqa: E501
        """GroupRuleAction - a model defined in Swagger"""  # noqa: E501
        self._assign_user_to_groups = None
        self.discriminator = None
        if assign_user_to_groups is not None:
            self.assign_user_to_groups = assign_user_to_groups

    @property
    def assign_user_to_groups(self):
        """Gets the assign_user_to_groups of this GroupRuleAction.  # noqa: E501


        :return: The assign_user_to_groups of this GroupRuleAction.  # noqa: E501
        :rtype: GroupRuleGroupAssignment
        """
        return self._assign_user_to_groups

    @assign_user_to_groups.setter
    def assign_user_to_groups(self, assign_user_to_groups):
        """Sets the assign_user_to_groups of this GroupRuleAction.


        :param assign_user_to_groups: The assign_user_to_groups of this GroupRuleAction.  # noqa: E501
        :type: GroupRuleGroupAssignment
        """

        self._assign_user_to_groups = assign_user_to_groups

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
        if issubclass(GroupRuleAction, dict):
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
        if not isinstance(other, GroupRuleAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
