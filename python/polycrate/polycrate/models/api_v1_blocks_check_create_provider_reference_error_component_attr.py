from typing import Literal

ApiV1BlocksCheckCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCKS_CHECK_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_blocks_check_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
