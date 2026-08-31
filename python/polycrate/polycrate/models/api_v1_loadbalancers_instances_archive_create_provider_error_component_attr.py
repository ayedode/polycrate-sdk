from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_loadbalancers_instances_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
