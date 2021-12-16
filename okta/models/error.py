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

class Error(object):
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
        'error_code': 'str',
        'error_summary': 'str',
        'error_link': 'str',
        'error_id': 'str',
        'error_causes': 'list[ErrorErrorCauses]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_summary': 'errorSummary',
        'error_link': 'errorLink',
        'error_id': 'errorId',
        'error_causes': 'errorCauses'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, error_code=None, error_summary=None, error_link=None, error_id=None, error_causes=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._error_summary = None
        self._error_link = None
        self._error_id = None
        self._error_causes = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if error_summary is not None:
            self.error_summary = error_summary
        if error_link is not None:
            self.error_link = error_link
        if error_id is not None:
            self.error_id = error_id
        if error_causes is not None:
            self.error_causes = error_causes

    @property
    def error_code(self):
        """Gets the error_code of this Error.  # noqa: E501

        An Okta code for this type of error  # noqa: E501

        :return: The error_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Error.

        An Okta code for this type of error  # noqa: E501

        :param error_code: The error_code of this Error.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_summary(self):
        """Gets the error_summary of this Error.  # noqa: E501

        A short description of what caused this error. Sometimes this contains dynamically-generated information about your specific error.  # noqa: E501

        :return: The error_summary of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_summary

    @error_summary.setter
    def error_summary(self, error_summary):
        """Sets the error_summary of this Error.

        A short description of what caused this error. Sometimes this contains dynamically-generated information about your specific error.  # noqa: E501

        :param error_summary: The error_summary of this Error.  # noqa: E501
        :type: str
        """

        self._error_summary = error_summary

    @property
    def error_link(self):
        """Gets the error_link of this Error.  # noqa: E501

        An Okta code for this type of error  # noqa: E501

        :return: The error_link of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_link

    @error_link.setter
    def error_link(self, error_link):
        """Sets the error_link of this Error.

        An Okta code for this type of error  # noqa: E501

        :param error_link: The error_link of this Error.  # noqa: E501
        :type: str
        """

        self._error_link = error_link

    @property
    def error_id(self):
        """Gets the error_id of this Error.  # noqa: E501

        A unique identifier for this error. This can be used by Okta Support to help with troubleshooting.  # noqa: E501

        :return: The error_id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this Error.

        A unique identifier for this error. This can be used by Okta Support to help with troubleshooting.  # noqa: E501

        :param error_id: The error_id of this Error.  # noqa: E501
        :type: str
        """

        self._error_id = error_id

    @property
    def error_causes(self):
        """Gets the error_causes of this Error.  # noqa: E501


        :return: The error_causes of this Error.  # noqa: E501
        :rtype: list[ErrorErrorCauses]
        """
        return self._error_causes

    @error_causes.setter
    def error_causes(self, error_causes):
        """Sets the error_causes of this Error.


        :param error_causes: The error_causes of this Error.  # noqa: E501
        :type: list[ErrorErrorCauses]
        """

        self._error_causes = error_causes

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
