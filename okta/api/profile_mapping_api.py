# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.9.2
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from okta.swagger_api_client import ApiClient


class ProfileMapping(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_profile_mapping(self, mapping_id, **kwargs):  # noqa: E501
        """Get Profile Mapping  # noqa: E501

        Fetches a single Profile Mapping referenced by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profile_mapping(mapping_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mapping_id: (required)
        :return: ProfileMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_profile_mapping_with_http_info(mapping_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_profile_mapping_with_http_info(mapping_id, **kwargs)  # noqa: E501
            return data

    def get_profile_mapping_with_http_info(self, mapping_id, **kwargs):  # noqa: E501
        """Get Profile Mapping  # noqa: E501

        Fetches a single Profile Mapping referenced by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_profile_mapping_with_http_info(mapping_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mapping_id: (required)
        :return: ProfileMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mapping_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_profile_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mapping_id' is set
        if ('mapping_id' not in params or
                params['mapping_id'] is None):
            raise ValueError("Missing the required parameter `mapping_id` when calling `get_profile_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mapping_id' in params:
            path_params['mappingId'] = params['mapping_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mappings/{mappingId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProfileMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_profile_mappings(self, **kwargs):  # noqa: E501
        """list_profile_mappings  # noqa: E501

        Enumerates Profile Mappings in your organization with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_profile_mappings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str after:
        :param int limit:
        :param str source_id:
        :param str target_id:
        :return: list[ProfileMapping]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_profile_mappings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_profile_mappings_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_profile_mappings_with_http_info(self, **kwargs):  # noqa: E501
        """list_profile_mappings  # noqa: E501

        Enumerates Profile Mappings in your organization with pagination.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_profile_mappings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str after:
        :param int limit:
        :param str source_id:
        :param str target_id:
        :return: list[ProfileMapping]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['after', 'limit', 'source_id', 'target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_profile_mappings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'source_id' in params:
            query_params.append(('sourceId', params['source_id']))  # noqa: E501
        if 'target_id' in params:
            query_params.append(('targetId', params['target_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mappings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProfileMapping]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_profile_mapping(self, body, mapping_id, **kwargs):  # noqa: E501
        """Update Profile Mapping  # noqa: E501

        Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_profile_mapping(body, mapping_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileMapping body: (required)
        :param str mapping_id: (required)
        :return: ProfileMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_profile_mapping_with_http_info(body, mapping_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_profile_mapping_with_http_info(body, mapping_id, **kwargs)  # noqa: E501
            return data

    def update_profile_mapping_with_http_info(self, body, mapping_id, **kwargs):  # noqa: E501
        """Update Profile Mapping  # noqa: E501

        Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_profile_mapping_with_http_info(body, mapping_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileMapping body: (required)
        :param str mapping_id: (required)
        :return: ProfileMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'mapping_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_profile_mapping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_profile_mapping`")  # noqa: E501
        # verify the required parameter 'mapping_id' is set
        if ('mapping_id' not in params or
                params['mapping_id'] is None):
            raise ValueError("Missing the required parameter `mapping_id` when calling `update_profile_mapping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mapping_id' in params:
            path_params['mappingId'] = params['mapping_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mappings/{mappingId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProfileMapping',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
