from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_partial_update_annotations_error_component import (
        ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_archived_at_error_component import (
        ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_archived_error_component import (
        ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_archived_reason_error_component import (
        ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_criticality_error_component import (
        ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_currency_error_component import (
        ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_debug_mode_error_component import (
        ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_display_name_error_component import (
        ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_generated_at_error_component import (
        ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_generated_by_error_component import (
        ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_is_manual_error_component import (
        ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_kind_error_component import (
        ApiV1PricingCostStatementsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_labels_error_component import (
        ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_name_error_component import (
        ApiV1PricingCostStatementsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_non_field_errors_error_component import (
        ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_period_end_error_component import (
        ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_period_start_error_component import (
        ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_platform_service_error_component import (
        ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_provider_error_component import (
        ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_provider_id_error_component import (
        ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_provider_reference_error_component import (
        ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_sla_availability_error_component import (
        ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_sla_target_error_component import (
        ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_slo_availability_error_component import (
        ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_slo_target_error_component import (
        ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_status_error_component import (
        ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_target_availability_error_component import (
        ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_tolerations_error_component import (
        ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_partial_update_total_net_error_component import (
        ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateKindErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateNameErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent |
            ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateKindErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateNameErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent
        | ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_partial_update_annotations_error_component import (
            ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_at_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_reason_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_criticality_error_component import (
            ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_currency_error_component import (
            ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_debug_mode_error_component import (
            ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_display_name_error_component import (
            ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_generated_at_error_component import (
            ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_generated_by_error_component import (
            ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_kind_error_component import (
            ApiV1PricingCostStatementsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_labels_error_component import (
            ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_name_error_component import (
            ApiV1PricingCostStatementsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_non_field_errors_error_component import (
            ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_period_end_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_period_start_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_platform_service_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_id_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_reference_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_sla_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_sla_target_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_slo_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_slo_target_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_status_error_component import (
            ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_target_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_tolerations_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_total_net_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_partial_update_annotations_error_component import (
            ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_at_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_archived_reason_error_component import (
            ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_criticality_error_component import (
            ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_currency_error_component import (
            ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_debug_mode_error_component import (
            ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_display_name_error_component import (
            ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_generated_at_error_component import (
            ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_generated_by_error_component import (
            ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_is_manual_error_component import (
            ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_kind_error_component import (
            ApiV1PricingCostStatementsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_labels_error_component import (
            ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_name_error_component import (
            ApiV1PricingCostStatementsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_non_field_errors_error_component import (
            ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_period_end_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_period_start_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_platform_service_error_component import (
            ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_id_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_provider_reference_error_component import (
            ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_sla_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_sla_target_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_slo_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_slo_target_error_component import (
            ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_status_error_component import (
            ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_target_availability_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_tolerations_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_partial_update_total_net_error_component import (
            ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateKindErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateNameErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent
                | ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_0 = (
                        ApiV1PricingCostStatementsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_1 = (
                        ApiV1PricingCostStatementsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_2 = (
                        ApiV1PricingCostStatementsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_3 = (
                        ApiV1PricingCostStatementsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_4 = (
                        ApiV1PricingCostStatementsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_5 = (
                        ApiV1PricingCostStatementsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_6 = (
                        ApiV1PricingCostStatementsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_7 = (
                        ApiV1PricingCostStatementsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_8 = (
                        ApiV1PricingCostStatementsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_9 = (
                        ApiV1PricingCostStatementsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_10 = (
                        ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_11 = (
                        ApiV1PricingCostStatementsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_12 = (
                        ApiV1PricingCostStatementsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_13 = (
                        ApiV1PricingCostStatementsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_14 = (
                        ApiV1PricingCostStatementsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_15 = (
                        ApiV1PricingCostStatementsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_16 = (
                        ApiV1PricingCostStatementsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_17 = (
                        ApiV1PricingCostStatementsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_18 = (
                        ApiV1PricingCostStatementsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_19 = (
                        ApiV1PricingCostStatementsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_20 = (
                        ApiV1PricingCostStatementsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_21 = (
                        ApiV1PricingCostStatementsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_22 = (
                        ApiV1PricingCostStatementsPartialUpdatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_23 = (
                        ApiV1PricingCostStatementsPartialUpdatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_24 = (
                        ApiV1PricingCostStatementsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_25 = (
                        ApiV1PricingCostStatementsPartialUpdateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_26 = (
                        ApiV1PricingCostStatementsPartialUpdateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_27 = (
                        ApiV1PricingCostStatementsPartialUpdateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_28 = (
                        ApiV1PricingCostStatementsPartialUpdateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_29 = (
                        ApiV1PricingCostStatementsPartialUpdateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_30 = (
                    ApiV1PricingCostStatementsPartialUpdateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_partial_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_partial_update_validation_error

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
