from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_void_create_annotations_error_component import (
        ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_archived_at_error_component import (
        ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_archived_error_component import (
        ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_archived_reason_error_component import (
        ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_criticality_error_component import (
        ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_currency_error_component import (
        ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_debug_mode_error_component import (
        ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_display_name_error_component import (
        ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_generated_at_error_component import (
        ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_generated_by_error_component import (
        ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_is_manual_error_component import (
        ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_kind_error_component import (
        ApiV1PricingCostStatementsVoidCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_labels_error_component import (
        ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_name_error_component import (
        ApiV1PricingCostStatementsVoidCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_non_field_errors_error_component import (
        ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_period_end_error_component import (
        ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_period_start_error_component import (
        ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_platform_service_error_component import (
        ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_provider_error_component import (
        ApiV1PricingCostStatementsVoidCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_provider_id_error_component import (
        ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_provider_reference_error_component import (
        ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_sla_availability_error_component import (
        ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_sla_target_error_component import (
        ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_slo_availability_error_component import (
        ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_slo_target_error_component import (
        ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_status_error_component import (
        ApiV1PricingCostStatementsVoidCreateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_target_availability_error_component import (
        ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_tolerations_error_component import (
        ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_void_create_total_net_error_component import (
        ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsVoidCreateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsVoidCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent |
            ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent |
            ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent |
            ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent |
            ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent |
            ApiV1PricingCostStatementsVoidCreateKindErrorComponent |
            ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent |
            ApiV1PricingCostStatementsVoidCreateNameErrorComponent |
            ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsVoidCreateProviderErrorComponent |
            ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent |
            ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent |
            ApiV1PricingCostStatementsVoidCreateStatusErrorComponent |
            ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent |
            ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent
        | ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent
        | ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent
        | ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent
        | ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent
        | ApiV1PricingCostStatementsVoidCreateKindErrorComponent
        | ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent
        | ApiV1PricingCostStatementsVoidCreateNameErrorComponent
        | ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsVoidCreateProviderErrorComponent
        | ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent
        | ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent
        | ApiV1PricingCostStatementsVoidCreateStatusErrorComponent
        | ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent
        | ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_void_create_annotations_error_component import (
            ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_at_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_criticality_error_component import (
            ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_currency_error_component import (
            ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_display_name_error_component import (
            ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_generated_at_error_component import (
            ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_generated_by_error_component import (
            ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_kind_error_component import (
            ApiV1PricingCostStatementsVoidCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_labels_error_component import (
            ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_name_error_component import (
            ApiV1PricingCostStatementsVoidCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_period_end_error_component import (
            ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_period_start_error_component import (
            ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_platform_service_error_component import (
            ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_id_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_sla_target_error_component import (
            ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_slo_target_error_component import (
            ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_status_error_component import (
            ApiV1PricingCostStatementsVoidCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_target_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_tolerations_error_component import (
            ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_total_net_error_component import (
            ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_void_create_annotations_error_component import (
            ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_at_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_criticality_error_component import (
            ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_currency_error_component import (
            ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_display_name_error_component import (
            ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_generated_at_error_component import (
            ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_generated_by_error_component import (
            ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_is_manual_error_component import (
            ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_kind_error_component import (
            ApiV1PricingCostStatementsVoidCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_labels_error_component import (
            ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_name_error_component import (
            ApiV1PricingCostStatementsVoidCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_period_end_error_component import (
            ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_period_start_error_component import (
            ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_platform_service_error_component import (
            ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_id_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_sla_target_error_component import (
            ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_slo_target_error_component import (
            ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_status_error_component import (
            ApiV1PricingCostStatementsVoidCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_target_availability_error_component import (
            ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_tolerations_error_component import (
            ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_cost_statements_void_create_total_net_error_component import (
            ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent
                | ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent
                | ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent
                | ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent
                | ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent
                | ApiV1PricingCostStatementsVoidCreateKindErrorComponent
                | ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent
                | ApiV1PricingCostStatementsVoidCreateNameErrorComponent
                | ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsVoidCreateProviderErrorComponent
                | ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent
                | ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent
                | ApiV1PricingCostStatementsVoidCreateStatusErrorComponent
                | ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent
                | ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_0 = (
                        ApiV1PricingCostStatementsVoidCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_1 = (
                        ApiV1PricingCostStatementsVoidCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_2 = (
                        ApiV1PricingCostStatementsVoidCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_3 = (
                        ApiV1PricingCostStatementsVoidCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_4 = (
                        ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_5 = (
                        ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_6 = (
                        ApiV1PricingCostStatementsVoidCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_7 = (
                        ApiV1PricingCostStatementsVoidCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_8 = (
                        ApiV1PricingCostStatementsVoidCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_9 = (
                        ApiV1PricingCostStatementsVoidCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_10 = (
                        ApiV1PricingCostStatementsVoidCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_11 = (
                        ApiV1PricingCostStatementsVoidCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_12 = (
                        ApiV1PricingCostStatementsVoidCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_13 = (
                        ApiV1PricingCostStatementsVoidCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_14 = (
                        ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_15 = (
                        ApiV1PricingCostStatementsVoidCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_16 = (
                        ApiV1PricingCostStatementsVoidCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_17 = (
                        ApiV1PricingCostStatementsVoidCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_18 = (
                        ApiV1PricingCostStatementsVoidCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_19 = (
                        ApiV1PricingCostStatementsVoidCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_20 = (
                        ApiV1PricingCostStatementsVoidCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_21 = (
                        ApiV1PricingCostStatementsVoidCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_22 = (
                        ApiV1PricingCostStatementsVoidCreatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_23 = (
                        ApiV1PricingCostStatementsVoidCreatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_24 = (
                        ApiV1PricingCostStatementsVoidCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_25 = (
                        ApiV1PricingCostStatementsVoidCreateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_26 = (
                        ApiV1PricingCostStatementsVoidCreateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_27 = (
                        ApiV1PricingCostStatementsVoidCreateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_28 = (
                        ApiV1PricingCostStatementsVoidCreateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_29 = (
                        ApiV1PricingCostStatementsVoidCreateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_30 = (
                    ApiV1PricingCostStatementsVoidCreateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_void_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_void_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_void_create_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_void_create_validation_error

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
