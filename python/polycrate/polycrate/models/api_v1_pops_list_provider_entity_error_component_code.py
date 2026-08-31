from typing import Literal

ApiV1PopsListProviderEntityErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_POPS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsListProviderEntityErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_pops_list_provider_entity_error_component_code(
    value: str,
) -> ApiV1PopsListProviderEntityErrorComponentCode:
    if value in API_V1_POPS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
