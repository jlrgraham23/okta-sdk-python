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

class IdentityProvider(object):
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
        'created': 'datetime',
        'id': 'str',
        'issuer_mode': 'IssuerMode',
        'last_updated': 'datetime',
        'name': 'str',
        'policy': 'IdentityProviderPolicy',
        'protocol': 'Protocol',
        'status': 'LifecycleStatus',
        'type': 'str'
    }

    attribute_map = {
        'links': '_links',
        'created': 'created',
        'id': 'id',
        'issuer_mode': 'issuerMode',
        'last_updated': 'lastUpdated',
        'name': 'name',
        'policy': 'policy',
        'protocol': 'protocol',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, created=None, id=None, issuer_mode=None, last_updated=None, name=None, policy=None, protocol=None, status=None, type=None):  # noqa: E501
        """IdentityProvider - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._created = None
        self._id = None
        self._issuer_mode = None
        self._last_updated = None
        self._name = None
        self._policy = None
        self._protocol = None
        self._status = None
        self._type = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if issuer_mode is not None:
            self.issuer_mode = issuer_mode
        if last_updated is not None:
            self.last_updated = last_updated
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if protocol is not None:
            self.protocol = protocol
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def links(self):
        """Gets the links of this IdentityProvider.  # noqa: E501


        :return: The links of this IdentityProvider.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IdentityProvider.


        :param links: The links of this IdentityProvider.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this IdentityProvider.  # noqa: E501


        :return: The created of this IdentityProvider.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this IdentityProvider.


        :param created: The created of this IdentityProvider.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this IdentityProvider.  # noqa: E501


        :return: The id of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityProvider.


        :param id: The id of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def issuer_mode(self):
        """Gets the issuer_mode of this IdentityProvider.  # noqa: E501


        :return: The issuer_mode of this IdentityProvider.  # noqa: E501
        :rtype: IssuerMode
        """
        return self._issuer_mode

    @issuer_mode.setter
    def issuer_mode(self, issuer_mode):
        """Sets the issuer_mode of this IdentityProvider.


        :param issuer_mode: The issuer_mode of this IdentityProvider.  # noqa: E501
        :type: IssuerMode
        """

        self._issuer_mode = issuer_mode

    @property
    def last_updated(self):
        """Gets the last_updated of this IdentityProvider.  # noqa: E501


        :return: The last_updated of this IdentityProvider.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this IdentityProvider.


        :param last_updated: The last_updated of this IdentityProvider.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def name(self):
        """Gets the name of this IdentityProvider.  # noqa: E501


        :return: The name of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityProvider.


        :param name: The name of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this IdentityProvider.  # noqa: E501


        :return: The policy of this IdentityProvider.  # noqa: E501
        :rtype: IdentityProviderPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this IdentityProvider.


        :param policy: The policy of this IdentityProvider.  # noqa: E501
        :type: IdentityProviderPolicy
        """

        self._policy = policy

    @property
    def protocol(self):
        """Gets the protocol of this IdentityProvider.  # noqa: E501


        :return: The protocol of this IdentityProvider.  # noqa: E501
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this IdentityProvider.


        :param protocol: The protocol of this IdentityProvider.  # noqa: E501
        :type: Protocol
        """

        self._protocol = protocol

    @property
    def status(self):
        """Gets the status of this IdentityProvider.  # noqa: E501


        :return: The status of this IdentityProvider.  # noqa: E501
        :rtype: LifecycleStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IdentityProvider.


        :param status: The status of this IdentityProvider.  # noqa: E501
        :type: LifecycleStatus
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this IdentityProvider.  # noqa: E501


        :return: The type of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityProvider.


        :param type: The type of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(IdentityProvider, dict):
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
        if not isinstance(other, IdentityProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
