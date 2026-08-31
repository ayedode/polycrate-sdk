from typing import Literal

ApiV1BlocksRepairCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_blocks_repair_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
