from typing import Literal

ApiV1BlocksCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_BLOCKS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateProviderIdErrorComponentAttr] = {
    "provider_id",
}


def check_api_v1_blocks_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateProviderIdErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
