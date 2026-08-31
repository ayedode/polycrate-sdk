from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponentAttr = Literal["ssl_redirect"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SSL_REDIRECT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponentAttr
] = {
    "ssl_redirect",
}


def check_api_v1_loadbalancers_instances_archive_create_ssl_redirect_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateSslRedirectErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SSL_REDIRECT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_SSL_REDIRECT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
