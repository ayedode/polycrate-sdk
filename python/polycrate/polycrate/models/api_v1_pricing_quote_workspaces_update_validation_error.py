from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_workspaces_update_annotations_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_archived_at_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_archived_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_archived_reason_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_block_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_block_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_block_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_cluster_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_cluster_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_criticality_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_debug_mode_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_display_name_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_host_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_host_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_hosts_count_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_kind_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_label_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_labels_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_count_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_name_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_non_field_errors_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_object_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_object_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_object_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_platform_service_error_component import (
        ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_provider_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_provider_id_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_provider_reference_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_quote_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_sla_availability_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_sla_target_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_slo_availability_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_slo_target_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_support_product_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_support_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_target_availability_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_tolerations_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_update_total_price_error_component import (
        ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteWorkspacesUpdateValidationError")


@_attrs_define
class ApiV1PricingQuoteWorkspacesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent | ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent
            | ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent | ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent |
            ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent
        | ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_workspaces_update_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_kind_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_label_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_labels_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_name_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_quote_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent):
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
        from ..models.api_v1_pricing_quote_workspaces_update_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_kind_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_label_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_labels_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_name_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_quote_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_update_total_price_error_component import (
            ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent
                | ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_0 = (
                        ApiV1PricingQuoteWorkspacesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_1 = (
                        ApiV1PricingQuoteWorkspacesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_2 = (
                        ApiV1PricingQuoteWorkspacesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_3 = (
                        ApiV1PricingQuoteWorkspacesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_4 = (
                        ApiV1PricingQuoteWorkspacesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_5 = (
                        ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_6 = (
                        ApiV1PricingQuoteWorkspacesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_7 = (
                        ApiV1PricingQuoteWorkspacesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_8 = (
                        ApiV1PricingQuoteWorkspacesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_9 = (
                        ApiV1PricingQuoteWorkspacesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_10 = (
                        ApiV1PricingQuoteWorkspacesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_11 = (
                        ApiV1PricingQuoteWorkspacesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_12 = (
                        ApiV1PricingQuoteWorkspacesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_13 = (
                        ApiV1PricingQuoteWorkspacesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_14 = (
                        ApiV1PricingQuoteWorkspacesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_15 = (
                        ApiV1PricingQuoteWorkspacesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_16 = (
                        ApiV1PricingQuoteWorkspacesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_17 = (
                        ApiV1PricingQuoteWorkspacesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_18 = (
                        ApiV1PricingQuoteWorkspacesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_19 = (
                        ApiV1PricingQuoteWorkspacesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_20 = (
                        ApiV1PricingQuoteWorkspacesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_21 = (
                        ApiV1PricingQuoteWorkspacesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_22 = (
                        ApiV1PricingQuoteWorkspacesUpdateQuoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_23 = (
                        ApiV1PricingQuoteWorkspacesUpdateLabelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_24 = (
                        ApiV1PricingQuoteWorkspacesUpdateClusterProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_25 = (
                        ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_26 = (
                        ApiV1PricingQuoteWorkspacesUpdateHostProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_27 = (
                        ApiV1PricingQuoteWorkspacesUpdateHostsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_28 = (
                        ApiV1PricingQuoteWorkspacesUpdateHostQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_29 = (
                        ApiV1PricingQuoteWorkspacesUpdateSupportProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_30 = (
                        ApiV1PricingQuoteWorkspacesUpdateSupportQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_31 = (
                        ApiV1PricingQuoteWorkspacesUpdateObjectStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_32 = (
                        ApiV1PricingQuoteWorkspacesUpdateObjectStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_33 = (
                        ApiV1PricingQuoteWorkspacesUpdateObjectStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_34 = (
                        ApiV1PricingQuoteWorkspacesUpdateBlockStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_35 = (
                        ApiV1PricingQuoteWorkspacesUpdateBlockStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_36 = (
                        ApiV1PricingQuoteWorkspacesUpdateBlockStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_37 = (
                        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_38 = (
                        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_39 = (
                        ApiV1PricingQuoteWorkspacesUpdateLoadbalancerQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_40 = (
                    ApiV1PricingQuoteWorkspacesUpdateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_workspaces_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_workspaces_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_workspaces_update_validation_error.additional_properties = d
        return api_v1_pricing_quote_workspaces_update_validation_error

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
