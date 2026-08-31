from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_calculator_states_formalize_create_access_count_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_annotations_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_archived_at_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_archived_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_archived_reason_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_booking_id_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_configuration_json_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_criticality_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_debug_mode_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_display_name_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_kind_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_labels_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_last_access_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_name_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_non_field_errors_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_platform_service_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_provider_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_provider_id_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_provider_reference_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_reconciliation_enabled_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_sla_availability_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_sla_target_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_slo_availability_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_slo_target_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_target_availability_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_tolerations_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_calculator_states_formalize_create_total_price_error_component import (
        ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCalculatorStatesFormalizeCreateValidationError")


@_attrs_define
class ApiV1PricingCalculatorStatesFormalizeCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent |
            ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent
        | ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_calculator_states_formalize_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_kind_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_labels_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_name_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent):
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
        from ..models.api_v1_pricing_calculator_states_formalize_create_access_count_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_annotations_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_at_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_archived_reason_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_booking_id_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_configuration_json_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_criticality_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_debug_mode_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_display_name_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_kind_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_labels_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_last_access_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_name_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_non_field_errors_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_platform_service_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_id_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_provider_reference_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_reconciliation_enabled_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_sla_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_sla_target_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_slo_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_slo_target_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_target_availability_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_tolerations_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_calculator_states_formalize_create_total_price_error_component import (
            ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent
                | ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_0 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_1 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_2 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_3 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_4 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_5 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_6 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_7 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_8 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_9 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_10 = (
                        ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_11 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_12 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_13 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_14 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_15 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_16 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_17 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_18 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_19 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_20 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_21 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_22 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_23 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateTotalPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_24 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateLastAccessErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_25 = (
                        ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_26 = (
                    ApiV1PricingCalculatorStatesFormalizeCreateBookingIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_calculator_states_formalize_create_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_calculator_states_formalize_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_calculator_states_formalize_create_validation_error.additional_properties = d
        return api_v1_pricing_calculator_states_formalize_create_validation_error

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
