from typing import Literal

ApiV1BlocksRepairCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_blocks_repair_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
