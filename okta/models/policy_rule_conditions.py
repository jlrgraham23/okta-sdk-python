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

class PolicyRuleConditions(object):
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
        'app': 'AppAndInstancePolicyRuleCondition',
        'apps': 'AppInstancePolicyRuleCondition',
        'auth_context': 'PolicyRuleAuthContextCondition',
        'auth_provider': 'PasswordPolicyAuthenticationProviderCondition',
        'before_scheduled_action': 'BeforeScheduledActionPolicyRuleCondition',
        'clients': 'ClientPolicyCondition',
        'context': 'ContextPolicyRuleCondition',
        'device': 'DevicePolicyRuleCondition',
        'grant_types': 'GrantTypePolicyRuleCondition',
        'groups': 'GroupPolicyRuleCondition',
        'identity_provider': 'IdentityProviderPolicyRuleCondition',
        'mdm_enrollment': 'MDMEnrollmentPolicyRuleCondition',
        'network': 'PolicyNetworkCondition',
        'people': 'PolicyPeopleCondition',
        'platform': 'PlatformPolicyRuleCondition',
        'risk': 'RiskPolicyRuleCondition',
        'risk_score': 'RiskScorePolicyRuleCondition',
        'scopes': 'OAuth2ScopesMediationPolicyRuleCondition',
        'user_identifier': 'UserIdentifierPolicyRuleCondition',
        'user_status': 'UserStatusPolicyRuleCondition',
        'users': 'UserPolicyRuleCondition'
    }

    attribute_map = {
        'app': 'app',
        'apps': 'apps',
        'auth_context': 'authContext',
        'auth_provider': 'authProvider',
        'before_scheduled_action': 'beforeScheduledAction',
        'clients': 'clients',
        'context': 'context',
        'device': 'device',
        'grant_types': 'grantTypes',
        'groups': 'groups',
        'identity_provider': 'identityProvider',
        'mdm_enrollment': 'mdmEnrollment',
        'network': 'network',
        'people': 'people',
        'platform': 'platform',
        'risk': 'risk',
        'risk_score': 'riskScore',
        'scopes': 'scopes',
        'user_identifier': 'userIdentifier',
        'user_status': 'userStatus',
        'users': 'users'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, app=None, apps=None, auth_context=None, auth_provider=None, before_scheduled_action=None, clients=None, context=None, device=None, grant_types=None, groups=None, identity_provider=None, mdm_enrollment=None, network=None, people=None, platform=None, risk=None, risk_score=None, scopes=None, user_identifier=None, user_status=None, users=None):  # noqa: E501
        """PolicyRuleConditions - a model defined in Swagger"""  # noqa: E501
        self._app = None
        self._apps = None
        self._auth_context = None
        self._auth_provider = None
        self._before_scheduled_action = None
        self._clients = None
        self._context = None
        self._device = None
        self._grant_types = None
        self._groups = None
        self._identity_provider = None
        self._mdm_enrollment = None
        self._network = None
        self._people = None
        self._platform = None
        self._risk = None
        self._risk_score = None
        self._scopes = None
        self._user_identifier = None
        self._user_status = None
        self._users = None
        self.discriminator = None
        if app is not None:
            self.app = app
        if apps is not None:
            self.apps = apps
        if auth_context is not None:
            self.auth_context = auth_context
        if auth_provider is not None:
            self.auth_provider = auth_provider
        if before_scheduled_action is not None:
            self.before_scheduled_action = before_scheduled_action
        if clients is not None:
            self.clients = clients
        if context is not None:
            self.context = context
        if device is not None:
            self.device = device
        if grant_types is not None:
            self.grant_types = grant_types
        if groups is not None:
            self.groups = groups
        if identity_provider is not None:
            self.identity_provider = identity_provider
        if mdm_enrollment is not None:
            self.mdm_enrollment = mdm_enrollment
        if network is not None:
            self.network = network
        if people is not None:
            self.people = people
        if platform is not None:
            self.platform = platform
        if risk is not None:
            self.risk = risk
        if risk_score is not None:
            self.risk_score = risk_score
        if scopes is not None:
            self.scopes = scopes
        if user_identifier is not None:
            self.user_identifier = user_identifier
        if user_status is not None:
            self.user_status = user_status
        if users is not None:
            self.users = users

    @property
    def app(self):
        """Gets the app of this PolicyRuleConditions.  # noqa: E501


        :return: The app of this PolicyRuleConditions.  # noqa: E501
        :rtype: AppAndInstancePolicyRuleCondition
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this PolicyRuleConditions.


        :param app: The app of this PolicyRuleConditions.  # noqa: E501
        :type: AppAndInstancePolicyRuleCondition
        """

        self._app = app

    @property
    def apps(self):
        """Gets the apps of this PolicyRuleConditions.  # noqa: E501


        :return: The apps of this PolicyRuleConditions.  # noqa: E501
        :rtype: AppInstancePolicyRuleCondition
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this PolicyRuleConditions.


        :param apps: The apps of this PolicyRuleConditions.  # noqa: E501
        :type: AppInstancePolicyRuleCondition
        """

        self._apps = apps

    @property
    def auth_context(self):
        """Gets the auth_context of this PolicyRuleConditions.  # noqa: E501


        :return: The auth_context of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyRuleAuthContextCondition
        """
        return self._auth_context

    @auth_context.setter
    def auth_context(self, auth_context):
        """Sets the auth_context of this PolicyRuleConditions.


        :param auth_context: The auth_context of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyRuleAuthContextCondition
        """

        self._auth_context = auth_context

    @property
    def auth_provider(self):
        """Gets the auth_provider of this PolicyRuleConditions.  # noqa: E501


        :return: The auth_provider of this PolicyRuleConditions.  # noqa: E501
        :rtype: PasswordPolicyAuthenticationProviderCondition
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, auth_provider):
        """Sets the auth_provider of this PolicyRuleConditions.


        :param auth_provider: The auth_provider of this PolicyRuleConditions.  # noqa: E501
        :type: PasswordPolicyAuthenticationProviderCondition
        """

        self._auth_provider = auth_provider

    @property
    def before_scheduled_action(self):
        """Gets the before_scheduled_action of this PolicyRuleConditions.  # noqa: E501


        :return: The before_scheduled_action of this PolicyRuleConditions.  # noqa: E501
        :rtype: BeforeScheduledActionPolicyRuleCondition
        """
        return self._before_scheduled_action

    @before_scheduled_action.setter
    def before_scheduled_action(self, before_scheduled_action):
        """Sets the before_scheduled_action of this PolicyRuleConditions.


        :param before_scheduled_action: The before_scheduled_action of this PolicyRuleConditions.  # noqa: E501
        :type: BeforeScheduledActionPolicyRuleCondition
        """

        self._before_scheduled_action = before_scheduled_action

    @property
    def clients(self):
        """Gets the clients of this PolicyRuleConditions.  # noqa: E501


        :return: The clients of this PolicyRuleConditions.  # noqa: E501
        :rtype: ClientPolicyCondition
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this PolicyRuleConditions.


        :param clients: The clients of this PolicyRuleConditions.  # noqa: E501
        :type: ClientPolicyCondition
        """

        self._clients = clients

    @property
    def context(self):
        """Gets the context of this PolicyRuleConditions.  # noqa: E501


        :return: The context of this PolicyRuleConditions.  # noqa: E501
        :rtype: ContextPolicyRuleCondition
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PolicyRuleConditions.


        :param context: The context of this PolicyRuleConditions.  # noqa: E501
        :type: ContextPolicyRuleCondition
        """

        self._context = context

    @property
    def device(self):
        """Gets the device of this PolicyRuleConditions.  # noqa: E501


        :return: The device of this PolicyRuleConditions.  # noqa: E501
        :rtype: DevicePolicyRuleCondition
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PolicyRuleConditions.


        :param device: The device of this PolicyRuleConditions.  # noqa: E501
        :type: DevicePolicyRuleCondition
        """

        self._device = device

    @property
    def grant_types(self):
        """Gets the grant_types of this PolicyRuleConditions.  # noqa: E501


        :return: The grant_types of this PolicyRuleConditions.  # noqa: E501
        :rtype: GrantTypePolicyRuleCondition
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this PolicyRuleConditions.


        :param grant_types: The grant_types of this PolicyRuleConditions.  # noqa: E501
        :type: GrantTypePolicyRuleCondition
        """

        self._grant_types = grant_types

    @property
    def groups(self):
        """Gets the groups of this PolicyRuleConditions.  # noqa: E501


        :return: The groups of this PolicyRuleConditions.  # noqa: E501
        :rtype: GroupPolicyRuleCondition
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this PolicyRuleConditions.


        :param groups: The groups of this PolicyRuleConditions.  # noqa: E501
        :type: GroupPolicyRuleCondition
        """

        self._groups = groups

    @property
    def identity_provider(self):
        """Gets the identity_provider of this PolicyRuleConditions.  # noqa: E501


        :return: The identity_provider of this PolicyRuleConditions.  # noqa: E501
        :rtype: IdentityProviderPolicyRuleCondition
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this PolicyRuleConditions.


        :param identity_provider: The identity_provider of this PolicyRuleConditions.  # noqa: E501
        :type: IdentityProviderPolicyRuleCondition
        """

        self._identity_provider = identity_provider

    @property
    def mdm_enrollment(self):
        """Gets the mdm_enrollment of this PolicyRuleConditions.  # noqa: E501


        :return: The mdm_enrollment of this PolicyRuleConditions.  # noqa: E501
        :rtype: MDMEnrollmentPolicyRuleCondition
        """
        return self._mdm_enrollment

    @mdm_enrollment.setter
    def mdm_enrollment(self, mdm_enrollment):
        """Sets the mdm_enrollment of this PolicyRuleConditions.


        :param mdm_enrollment: The mdm_enrollment of this PolicyRuleConditions.  # noqa: E501
        :type: MDMEnrollmentPolicyRuleCondition
        """

        self._mdm_enrollment = mdm_enrollment

    @property
    def network(self):
        """Gets the network of this PolicyRuleConditions.  # noqa: E501


        :return: The network of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyNetworkCondition
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PolicyRuleConditions.


        :param network: The network of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyNetworkCondition
        """

        self._network = network

    @property
    def people(self):
        """Gets the people of this PolicyRuleConditions.  # noqa: E501


        :return: The people of this PolicyRuleConditions.  # noqa: E501
        :rtype: PolicyPeopleCondition
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this PolicyRuleConditions.


        :param people: The people of this PolicyRuleConditions.  # noqa: E501
        :type: PolicyPeopleCondition
        """

        self._people = people

    @property
    def platform(self):
        """Gets the platform of this PolicyRuleConditions.  # noqa: E501


        :return: The platform of this PolicyRuleConditions.  # noqa: E501
        :rtype: PlatformPolicyRuleCondition
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PolicyRuleConditions.


        :param platform: The platform of this PolicyRuleConditions.  # noqa: E501
        :type: PlatformPolicyRuleCondition
        """

        self._platform = platform

    @property
    def risk(self):
        """Gets the risk of this PolicyRuleConditions.  # noqa: E501


        :return: The risk of this PolicyRuleConditions.  # noqa: E501
        :rtype: RiskPolicyRuleCondition
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this PolicyRuleConditions.


        :param risk: The risk of this PolicyRuleConditions.  # noqa: E501
        :type: RiskPolicyRuleCondition
        """

        self._risk = risk

    @property
    def risk_score(self):
        """Gets the risk_score of this PolicyRuleConditions.  # noqa: E501


        :return: The risk_score of this PolicyRuleConditions.  # noqa: E501
        :rtype: RiskScorePolicyRuleCondition
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """Sets the risk_score of this PolicyRuleConditions.


        :param risk_score: The risk_score of this PolicyRuleConditions.  # noqa: E501
        :type: RiskScorePolicyRuleCondition
        """

        self._risk_score = risk_score

    @property
    def scopes(self):
        """Gets the scopes of this PolicyRuleConditions.  # noqa: E501


        :return: The scopes of this PolicyRuleConditions.  # noqa: E501
        :rtype: OAuth2ScopesMediationPolicyRuleCondition
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this PolicyRuleConditions.


        :param scopes: The scopes of this PolicyRuleConditions.  # noqa: E501
        :type: OAuth2ScopesMediationPolicyRuleCondition
        """

        self._scopes = scopes

    @property
    def user_identifier(self):
        """Gets the user_identifier of this PolicyRuleConditions.  # noqa: E501


        :return: The user_identifier of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserIdentifierPolicyRuleCondition
        """
        return self._user_identifier

    @user_identifier.setter
    def user_identifier(self, user_identifier):
        """Sets the user_identifier of this PolicyRuleConditions.


        :param user_identifier: The user_identifier of this PolicyRuleConditions.  # noqa: E501
        :type: UserIdentifierPolicyRuleCondition
        """

        self._user_identifier = user_identifier

    @property
    def user_status(self):
        """Gets the user_status of this PolicyRuleConditions.  # noqa: E501


        :return: The user_status of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserStatusPolicyRuleCondition
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this PolicyRuleConditions.


        :param user_status: The user_status of this PolicyRuleConditions.  # noqa: E501
        :type: UserStatusPolicyRuleCondition
        """

        self._user_status = user_status

    @property
    def users(self):
        """Gets the users of this PolicyRuleConditions.  # noqa: E501


        :return: The users of this PolicyRuleConditions.  # noqa: E501
        :rtype: UserPolicyRuleCondition
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this PolicyRuleConditions.


        :param users: The users of this PolicyRuleConditions.  # noqa: E501
        :type: UserPolicyRuleCondition
        """

        self._users = users

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
        if issubclass(PolicyRuleConditions, dict):
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
        if not isinstance(other, PolicyRuleConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
