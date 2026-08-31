from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_generate_create_annotations_error_component import (
        ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_archived_at_error_component import (
        ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_archived_error_component import (
        ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_archived_reason_error_component import (
        ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_criticality_error_component import (
        ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_currency_error_component import (
        ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_debug_mode_error_component import (
        ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_display_name_error_component import (
        ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_generated_at_error_component import (
        ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_generated_by_error_component import (
        ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_is_manual_error_component import (
        ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_kind_error_component import (
        ApiV1PricingCostStatementsGenerateCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_labels_error_component import (
        ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_name_error_component import (
        ApiV1PricingCostStatementsGenerateCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_non_field_errors_error_component import (
        ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_period_end_error_component import (
        ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_period_start_error_component import (
        ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_platform_service_error_component import (
        ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_provider_error_component import (
        ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_provider_id_error_component import (
        ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_provider_reference_error_component import (
        ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_sla_availability_error_component import (
        ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_sla_target_error_component import (
        ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_slo_availability_error_component import (
        ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_slo_target_error_component import (
        ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_status_error_component import (
        ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_target_availability_error_component import (
        ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_tolerations_error_component import (
        ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_generate_create_total_net_error_component import (
        ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsGenerateCreateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsGenerateCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateKindErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateNameErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent |
            ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateKindErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateNameErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent
        | ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_generate_create_annotations_error_component import (
            ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_at_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_criticality_error_component import (
            ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_currency_error_component import (
            ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_display_name_error_component import (
            ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_generated_at_error_component import (
            ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_generated_by_error_component import (
            ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_kind_error_component import (
            ApiV1PricingCostStatementsGenerateCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_labels_error_component import (
            ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_name_error_component import (
            ApiV1PricingCostStatementsGenerateCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_period_end_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_period_start_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_platform_service_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_id_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_sla_target_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_slo_target_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_status_error_component import (
            ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_target_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_tolerations_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_total_net_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_generate_create_annotations_error_component import (
            ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_at_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_criticality_error_component import (
            ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_currency_error_component import (
            ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_display_name_error_component import (
            ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_generated_at_error_component import (
            ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_generated_by_error_component import (
            ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_is_manual_error_component import (
            ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_kind_error_component import (
            ApiV1PricingCostStatementsGenerateCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_labels_error_component import (
            ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_name_error_component import (
            ApiV1PricingCostStatementsGenerateCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_period_end_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_period_start_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_platform_service_error_component import (
            ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_id_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_sla_target_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_slo_target_error_component import (
            ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_status_error_component import (
            ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_target_availability_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_tolerations_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_generate_create_total_net_error_component import (
            ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateKindErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateNameErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent
                | ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_0 = (
                        ApiV1PricingCostStatementsGenerateCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_1 = (
                        ApiV1PricingCostStatementsGenerateCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_2 = (
                        ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_3 = (
                        ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_4 = (
                        ApiV1PricingCostStatementsGenerateCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_5 = (
                        ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_6 = (
                        ApiV1PricingCostStatementsGenerateCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_7 = (
                        ApiV1PricingCostStatementsGenerateCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_8 = (
                        ApiV1PricingCostStatementsGenerateCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_9 = (
                        ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_10 = (
                        ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_11 = (
                        ApiV1PricingCostStatementsGenerateCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_12 = (
                        ApiV1PricingCostStatementsGenerateCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_13 = (
                        ApiV1PricingCostStatementsGenerateCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_14 = (
                        ApiV1PricingCostStatementsGenerateCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_15 = (
                        ApiV1PricingCostStatementsGenerateCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_16 = (
                        ApiV1PricingCostStatementsGenerateCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_17 = (
                        ApiV1PricingCostStatementsGenerateCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_18 = (
                        ApiV1PricingCostStatementsGenerateCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_19 = (
                        ApiV1PricingCostStatementsGenerateCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_20 = (
                        ApiV1PricingCostStatementsGenerateCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_21 = (
                        ApiV1PricingCostStatementsGenerateCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_22 = (
                        ApiV1PricingCostStatementsGenerateCreatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_23 = (
                        ApiV1PricingCostStatementsGenerateCreatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_24 = (
                        ApiV1PricingCostStatementsGenerateCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_25 = (
                        ApiV1PricingCostStatementsGenerateCreateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_26 = (
                        ApiV1PricingCostStatementsGenerateCreateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_27 = (
                        ApiV1PricingCostStatementsGenerateCreateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_28 = (
                        ApiV1PricingCostStatementsGenerateCreateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_29 = (
                        ApiV1PricingCostStatementsGenerateCreateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_30 = (
                    ApiV1PricingCostStatementsGenerateCreateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_generate_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_generate_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_generate_create_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_generate_create_validation_error

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
