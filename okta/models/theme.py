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

class Theme(object):
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
        'links': 'dict(str, object)',
        'background_image': 'str',
        'email_template_touch_point_variant': 'EmailTemplateTouchPointVariant',
        'end_user_dashboard_touch_point_variant': 'EndUserDashboardTouchPointVariant',
        'error_page_touch_point_variant': 'ErrorPageTouchPointVariant',
        'primary_color_contrast_hex': 'str',
        'primary_color_hex': 'str',
        'secondary_color_contrast_hex': 'str',
        'secondary_color_hex': 'str',
        'sign_in_page_touch_point_variant': 'SignInPageTouchPointVariant'
    }

    attribute_map = {
        'links': '_links',
        'background_image': 'backgroundImage',
        'email_template_touch_point_variant': 'emailTemplateTouchPointVariant',
        'end_user_dashboard_touch_point_variant': 'endUserDashboardTouchPointVariant',
        'error_page_touch_point_variant': 'errorPageTouchPointVariant',
        'primary_color_contrast_hex': 'primaryColorContrastHex',
        'primary_color_hex': 'primaryColorHex',
        'secondary_color_contrast_hex': 'secondaryColorContrastHex',
        'secondary_color_hex': 'secondaryColorHex',
        'sign_in_page_touch_point_variant': 'signInPageTouchPointVariant'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, background_image=None, email_template_touch_point_variant=None, end_user_dashboard_touch_point_variant=None, error_page_touch_point_variant=None, primary_color_contrast_hex=None, primary_color_hex=None, secondary_color_contrast_hex=None, secondary_color_hex=None, sign_in_page_touch_point_variant=None):  # noqa: E501
        """Theme - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._background_image = None
        self._email_template_touch_point_variant = None
        self._end_user_dashboard_touch_point_variant = None
        self._error_page_touch_point_variant = None
        self._primary_color_contrast_hex = None
        self._primary_color_hex = None
        self._secondary_color_contrast_hex = None
        self._secondary_color_hex = None
        self._sign_in_page_touch_point_variant = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if background_image is not None:
            self.background_image = background_image
        if email_template_touch_point_variant is not None:
            self.email_template_touch_point_variant = email_template_touch_point_variant
        if end_user_dashboard_touch_point_variant is not None:
            self.end_user_dashboard_touch_point_variant = end_user_dashboard_touch_point_variant
        if error_page_touch_point_variant is not None:
            self.error_page_touch_point_variant = error_page_touch_point_variant
        if primary_color_contrast_hex is not None:
            self.primary_color_contrast_hex = primary_color_contrast_hex
        if primary_color_hex is not None:
            self.primary_color_hex = primary_color_hex
        if secondary_color_contrast_hex is not None:
            self.secondary_color_contrast_hex = secondary_color_contrast_hex
        if secondary_color_hex is not None:
            self.secondary_color_hex = secondary_color_hex
        if sign_in_page_touch_point_variant is not None:
            self.sign_in_page_touch_point_variant = sign_in_page_touch_point_variant

    @property
    def links(self):
        """Gets the links of this Theme.  # noqa: E501


        :return: The links of this Theme.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Theme.


        :param links: The links of this Theme.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def background_image(self):
        """Gets the background_image of this Theme.  # noqa: E501


        :return: The background_image of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this Theme.


        :param background_image: The background_image of this Theme.  # noqa: E501
        :type: str
        """

        self._background_image = background_image

    @property
    def email_template_touch_point_variant(self):
        """Gets the email_template_touch_point_variant of this Theme.  # noqa: E501


        :return: The email_template_touch_point_variant of this Theme.  # noqa: E501
        :rtype: EmailTemplateTouchPointVariant
        """
        return self._email_template_touch_point_variant

    @email_template_touch_point_variant.setter
    def email_template_touch_point_variant(self, email_template_touch_point_variant):
        """Sets the email_template_touch_point_variant of this Theme.


        :param email_template_touch_point_variant: The email_template_touch_point_variant of this Theme.  # noqa: E501
        :type: EmailTemplateTouchPointVariant
        """

        self._email_template_touch_point_variant = email_template_touch_point_variant

    @property
    def end_user_dashboard_touch_point_variant(self):
        """Gets the end_user_dashboard_touch_point_variant of this Theme.  # noqa: E501


        :return: The end_user_dashboard_touch_point_variant of this Theme.  # noqa: E501
        :rtype: EndUserDashboardTouchPointVariant
        """
        return self._end_user_dashboard_touch_point_variant

    @end_user_dashboard_touch_point_variant.setter
    def end_user_dashboard_touch_point_variant(self, end_user_dashboard_touch_point_variant):
        """Sets the end_user_dashboard_touch_point_variant of this Theme.


        :param end_user_dashboard_touch_point_variant: The end_user_dashboard_touch_point_variant of this Theme.  # noqa: E501
        :type: EndUserDashboardTouchPointVariant
        """

        self._end_user_dashboard_touch_point_variant = end_user_dashboard_touch_point_variant

    @property
    def error_page_touch_point_variant(self):
        """Gets the error_page_touch_point_variant of this Theme.  # noqa: E501


        :return: The error_page_touch_point_variant of this Theme.  # noqa: E501
        :rtype: ErrorPageTouchPointVariant
        """
        return self._error_page_touch_point_variant

    @error_page_touch_point_variant.setter
    def error_page_touch_point_variant(self, error_page_touch_point_variant):
        """Sets the error_page_touch_point_variant of this Theme.


        :param error_page_touch_point_variant: The error_page_touch_point_variant of this Theme.  # noqa: E501
        :type: ErrorPageTouchPointVariant
        """

        self._error_page_touch_point_variant = error_page_touch_point_variant

    @property
    def primary_color_contrast_hex(self):
        """Gets the primary_color_contrast_hex of this Theme.  # noqa: E501


        :return: The primary_color_contrast_hex of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._primary_color_contrast_hex

    @primary_color_contrast_hex.setter
    def primary_color_contrast_hex(self, primary_color_contrast_hex):
        """Sets the primary_color_contrast_hex of this Theme.


        :param primary_color_contrast_hex: The primary_color_contrast_hex of this Theme.  # noqa: E501
        :type: str
        """

        self._primary_color_contrast_hex = primary_color_contrast_hex

    @property
    def primary_color_hex(self):
        """Gets the primary_color_hex of this Theme.  # noqa: E501


        :return: The primary_color_hex of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._primary_color_hex

    @primary_color_hex.setter
    def primary_color_hex(self, primary_color_hex):
        """Sets the primary_color_hex of this Theme.


        :param primary_color_hex: The primary_color_hex of this Theme.  # noqa: E501
        :type: str
        """

        self._primary_color_hex = primary_color_hex

    @property
    def secondary_color_contrast_hex(self):
        """Gets the secondary_color_contrast_hex of this Theme.  # noqa: E501


        :return: The secondary_color_contrast_hex of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color_contrast_hex

    @secondary_color_contrast_hex.setter
    def secondary_color_contrast_hex(self, secondary_color_contrast_hex):
        """Sets the secondary_color_contrast_hex of this Theme.


        :param secondary_color_contrast_hex: The secondary_color_contrast_hex of this Theme.  # noqa: E501
        :type: str
        """

        self._secondary_color_contrast_hex = secondary_color_contrast_hex

    @property
    def secondary_color_hex(self):
        """Gets the secondary_color_hex of this Theme.  # noqa: E501


        :return: The secondary_color_hex of this Theme.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color_hex

    @secondary_color_hex.setter
    def secondary_color_hex(self, secondary_color_hex):
        """Sets the secondary_color_hex of this Theme.


        :param secondary_color_hex: The secondary_color_hex of this Theme.  # noqa: E501
        :type: str
        """

        self._secondary_color_hex = secondary_color_hex

    @property
    def sign_in_page_touch_point_variant(self):
        """Gets the sign_in_page_touch_point_variant of this Theme.  # noqa: E501


        :return: The sign_in_page_touch_point_variant of this Theme.  # noqa: E501
        :rtype: SignInPageTouchPointVariant
        """
        return self._sign_in_page_touch_point_variant

    @sign_in_page_touch_point_variant.setter
    def sign_in_page_touch_point_variant(self, sign_in_page_touch_point_variant):
        """Sets the sign_in_page_touch_point_variant of this Theme.


        :param sign_in_page_touch_point_variant: The sign_in_page_touch_point_variant of this Theme.  # noqa: E501
        :type: SignInPageTouchPointVariant
        """

        self._sign_in_page_touch_point_variant = sign_in_page_touch_point_variant

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
        if issubclass(Theme, dict):
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
        if not isinstance(other, Theme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
