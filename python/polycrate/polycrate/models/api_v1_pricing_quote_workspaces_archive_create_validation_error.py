from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_workspaces_archive_create_annotations_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_at_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_reason_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_criticality_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_debug_mode_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_display_name_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_host_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_host_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_hosts_count_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_kind_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_label_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_labels_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_count_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_name_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_non_field_errors_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_platform_service_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_id_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_reference_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_quote_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_availability_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_target_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_availability_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_target_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_support_product_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_support_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_target_availability_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_tolerations_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_archive_create_total_price_error_component import (
        ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteWorkspacesArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingQuoteWorkspacesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent |
            ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent
        | ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_workspaces_archive_create_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_kind_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_label_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_labels_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_name_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_quote_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_pricing_quote_workspaces_archive_create_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_kind_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_label_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_labels_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_name_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_quote_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_quote_workspaces_archive_create_total_price_error_component import (
            ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent
                | ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_0 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_1 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_2 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_3 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_4 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_5 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_6 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_7 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_8 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_9 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_10 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_11 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_12 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_13 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_14 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_15 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_16 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_17 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_18 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_19 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_20 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_21 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_22 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateQuoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_23 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateLabelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_24 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateClusterProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_25 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_26 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateHostProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_27 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateHostsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_28 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateHostQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_29 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSupportProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_30 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateSupportQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_31 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_32 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_33 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateObjectStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_34 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_35 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_36 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateBlockStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_37 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_38 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_39 = (
                        ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_40 = (
                    ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_workspaces_archive_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_workspaces_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_workspaces_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_quote_workspaces_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
