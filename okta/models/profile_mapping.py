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

class ProfileMapping(object):
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
        'id': 'str',
        'properties': 'dict(str, ProfileMappingProperty)',
        'source': 'ProfileMappingSource',
        'target': 'ProfileMappingSource'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'properties': 'properties',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, id=None, properties=None, source=None, target=None):  # noqa: E501
        """ProfileMapping - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._id = None
        self._properties = None
        self._source = None
        self._target = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if properties is not None:
            self.properties = properties
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def links(self):
        """Gets the links of this ProfileMapping.  # noqa: E501


        :return: The links of this ProfileMapping.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ProfileMapping.


        :param links: The links of this ProfileMapping.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this ProfileMapping.  # noqa: E501


        :return: The id of this ProfileMapping.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProfileMapping.


        :param id: The id of this ProfileMapping.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this ProfileMapping.  # noqa: E501


        :return: The properties of this ProfileMapping.  # noqa: E501
        :rtype: dict(str, ProfileMappingProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ProfileMapping.


        :param properties: The properties of this ProfileMapping.  # noqa: E501
        :type: dict(str, ProfileMappingProperty)
        """

        self._properties = properties

    @property
    def source(self):
        """Gets the source of this ProfileMapping.  # noqa: E501


        :return: The source of this ProfileMapping.  # noqa: E501
        :rtype: ProfileMappingSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ProfileMapping.


        :param source: The source of this ProfileMapping.  # noqa: E501
        :type: ProfileMappingSource
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this ProfileMapping.  # noqa: E501


        :return: The target of this ProfileMapping.  # noqa: E501
        :rtype: ProfileMappingSource
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ProfileMapping.


        :param target: The target of this ProfileMapping.  # noqa: E501
        :type: ProfileMappingSource
        """

        self._target = target

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
        if issubclass(ProfileMapping, dict):
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
        if not isinstance(other, ProfileMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
