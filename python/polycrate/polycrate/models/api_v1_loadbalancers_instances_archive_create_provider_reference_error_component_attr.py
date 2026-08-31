from typing import Literal

ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_loadbalancers_instances_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersInstancesArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
