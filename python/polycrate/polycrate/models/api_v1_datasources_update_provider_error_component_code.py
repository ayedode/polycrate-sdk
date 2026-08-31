from typing import Literal

ApiV1DatasourcesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DATASOURCES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_datasources_update_provider_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateProviderErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
