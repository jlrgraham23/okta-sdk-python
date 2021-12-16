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

class WsFederationApplicationSettingsApplication(ApplicationSettingsApplication):
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
        'attribute_statements': 'str',
        'audience_restriction': 'str',
        'authn_context_class_ref': 'str',
        'group_filter': 'str',
        'group_name': 'str',
        'group_value_format': 'str',
        'name_id_format': 'str',
        'realm': 'str',
        'site_url': 'str',
        'username_attribute': 'str',
        'w_reply_override': 'bool',
        'w_reply_url': 'str'
    }
    if hasattr(ApplicationSettingsApplication, "swagger_types"):
        swagger_types.update(ApplicationSettingsApplication.swagger_types)

    attribute_map = {
        'attribute_statements': 'attributeStatements',
        'audience_restriction': 'audienceRestriction',
        'authn_context_class_ref': 'authnContextClassRef',
        'group_filter': 'groupFilter',
        'group_name': 'groupName',
        'group_value_format': 'groupValueFormat',
        'name_id_format': 'nameIDFormat',
        'realm': 'realm',
        'site_url': 'siteURL',
        'username_attribute': 'usernameAttribute',
        'w_reply_override': 'wReplyOverride',
        'w_reply_url': 'wReplyURL'
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

    def set_attributes(self, attribute_statements=None, audience_restriction=None, authn_context_class_ref=None, group_filter=None, group_name=None, group_value_format=None, name_id_format=None, realm=None, site_url=None, username_attribute=None, w_reply_override=None, w_reply_url=None, *args, **kwargs):  # noqa: E501
        """WsFederationApplicationSettingsApplication - a model defined in Swagger"""  # noqa: E501
        self._attribute_statements = None
        self._audience_restriction = None
        self._authn_context_class_ref = None
        self._group_filter = None
        self._group_name = None
        self._group_value_format = None
        self._name_id_format = None
        self._realm = None
        self._site_url = None
        self._username_attribute = None
        self._w_reply_override = None
        self._w_reply_url = None
        self.discriminator = None
        if attribute_statements is not None:
            self.attribute_statements = attribute_statements
        if audience_restriction is not None:
            self.audience_restriction = audience_restriction
        if authn_context_class_ref is not None:
            self.authn_context_class_ref = authn_context_class_ref
        if group_filter is not None:
            self.group_filter = group_filter
        if group_name is not None:
            self.group_name = group_name
        if group_value_format is not None:
            self.group_value_format = group_value_format
        if name_id_format is not None:
            self.name_id_format = name_id_format
        if realm is not None:
            self.realm = realm
        if site_url is not None:
            self.site_url = site_url
        if username_attribute is not None:
            self.username_attribute = username_attribute
        if w_reply_override is not None:
            self.w_reply_override = w_reply_override
        if w_reply_url is not None:
            self.w_reply_url = w_reply_url

    @property
    def attribute_statements(self):
        """Gets the attribute_statements of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The attribute_statements of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._attribute_statements

    @attribute_statements.setter
    def attribute_statements(self, attribute_statements):
        """Sets the attribute_statements of this WsFederationApplicationSettingsApplication.


        :param attribute_statements: The attribute_statements of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._attribute_statements = attribute_statements

    @property
    def audience_restriction(self):
        """Gets the audience_restriction of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The audience_restriction of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._audience_restriction

    @audience_restriction.setter
    def audience_restriction(self, audience_restriction):
        """Sets the audience_restriction of this WsFederationApplicationSettingsApplication.


        :param audience_restriction: The audience_restriction of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._audience_restriction = audience_restriction

    @property
    def authn_context_class_ref(self):
        """Gets the authn_context_class_ref of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The authn_context_class_ref of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._authn_context_class_ref

    @authn_context_class_ref.setter
    def authn_context_class_ref(self, authn_context_class_ref):
        """Sets the authn_context_class_ref of this WsFederationApplicationSettingsApplication.


        :param authn_context_class_ref: The authn_context_class_ref of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._authn_context_class_ref = authn_context_class_ref

    @property
    def group_filter(self):
        """Gets the group_filter of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The group_filter of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._group_filter

    @group_filter.setter
    def group_filter(self, group_filter):
        """Sets the group_filter of this WsFederationApplicationSettingsApplication.


        :param group_filter: The group_filter of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._group_filter = group_filter

    @property
    def group_name(self):
        """Gets the group_name of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The group_name of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this WsFederationApplicationSettingsApplication.


        :param group_name: The group_name of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def group_value_format(self):
        """Gets the group_value_format of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The group_value_format of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._group_value_format

    @group_value_format.setter
    def group_value_format(self, group_value_format):
        """Sets the group_value_format of this WsFederationApplicationSettingsApplication.


        :param group_value_format: The group_value_format of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._group_value_format = group_value_format

    @property
    def name_id_format(self):
        """Gets the name_id_format of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The name_id_format of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._name_id_format

    @name_id_format.setter
    def name_id_format(self, name_id_format):
        """Sets the name_id_format of this WsFederationApplicationSettingsApplication.


        :param name_id_format: The name_id_format of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._name_id_format = name_id_format

    @property
    def realm(self):
        """Gets the realm of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The realm of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this WsFederationApplicationSettingsApplication.


        :param realm: The realm of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def site_url(self):
        """Gets the site_url of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The site_url of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._site_url

    @site_url.setter
    def site_url(self, site_url):
        """Sets the site_url of this WsFederationApplicationSettingsApplication.


        :param site_url: The site_url of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._site_url = site_url

    @property
    def username_attribute(self):
        """Gets the username_attribute of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The username_attribute of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._username_attribute

    @username_attribute.setter
    def username_attribute(self, username_attribute):
        """Sets the username_attribute of this WsFederationApplicationSettingsApplication.


        :param username_attribute: The username_attribute of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._username_attribute = username_attribute

    @property
    def w_reply_override(self):
        """Gets the w_reply_override of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The w_reply_override of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: bool
        """
        return self._w_reply_override

    @w_reply_override.setter
    def w_reply_override(self, w_reply_override):
        """Sets the w_reply_override of this WsFederationApplicationSettingsApplication.


        :param w_reply_override: The w_reply_override of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: bool
        """

        self._w_reply_override = w_reply_override

    @property
    def w_reply_url(self):
        """Gets the w_reply_url of this WsFederationApplicationSettingsApplication.  # noqa: E501


        :return: The w_reply_url of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :rtype: str
        """
        return self._w_reply_url

    @w_reply_url.setter
    def w_reply_url(self, w_reply_url):
        """Sets the w_reply_url of this WsFederationApplicationSettingsApplication.


        :param w_reply_url: The w_reply_url of this WsFederationApplicationSettingsApplication.  # noqa: E501
        :type: str
        """

        self._w_reply_url = w_reply_url

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
        if issubclass(WsFederationApplicationSettingsApplication, dict):
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
        if not isinstance(other, WsFederationApplicationSettingsApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
