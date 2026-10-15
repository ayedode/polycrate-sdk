from typing import Literal

ProviderDetailTenantSegmentation = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_TENANT_SEGMENTATION_VALUES: set[ProviderDetailTenantSegmentation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_tenant_segmentation(value: str) -> ProviderDetailTenantSegmentation:
    if value in PROVIDER_DETAIL_TENANT_SEGMENTATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_TENANT_SEGMENTATION_VALUES!r}")
